import discord
from discord.ext import commands
from .utils import checks
from cogs.utils.dataIO import dataIO
import os
import asyncio

class RaidProtect:
    """Protect yourself from server raids."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/raidprotect/settings.json")

    @commands.group(pass_context=True)
    @checks.admin_or_permissions()
    async def raidprotect(self, ctx):
        """Manage raidprotect."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
            
    @raidprotect.command(pass_context=True)
    async def setchannel(self, ctx, channel:discord.Channel):
        """Sets the channel new members should see when protected."""
        try:
            self.settings[ctx.message.server.id]['channel'] = channel.id
        except KeyError:
            self.settings[ctx.message.server.id] = {'channel': channel.id}
        self.save_settings()
        await self.bot.say("Channel set.")
            
    @raidprotect.command(pass_context=True)
    async def toggle(self, ctx):
        """Toggle raidprotect."""
        try:
            if self.settings[ctx.message.server.id]['protected']:
                self.settings[ctx.message.server.id]['protected'] = False
                await self.bot.say("Your server is no longer protected, anyone that joins will be able to see all channels.")
            else:
                self.settings[ctx.message.server.id]['protected'] = True
                await self.bot.say("Your server is now protected, anyone that joins will only be able to see the set channel.")
        except KeyError:
            self.settings[ctx.message.server.id] = {'protected': True}
            await self.bot.say("Your server is now protected, anyone that joins will only be able to see the set channel.")
        self.save_settings()
        
    def save_settings(self):
        dataIO.save_json("data/raidprotect/settings.json", self.settings)
        
    async def on_member_join(self, member):
        if not "bots" in member.server.name.lower():
            try:
                temp = self.settings[member.server.id]['joined']
            except KeyError:
                self.settings[member.server.id]['joined'] = 0
            self.settings[member.server.id]['joined'] += 1
            self.save_settings()
            if (self.settings[member.server.id]['joined'] == 4) and not (self.settings[member.server.id]['protected']):
                self.settings[member.server.id]['protected'] = True
                self.save_settings()
                for channel in member.server.channels:
                    if channel.id == self.settings[member.server.id]['channel']:
                        await self.bot.send_message(channel, "Raid protect has been turned on, more than 4 people joined within 8 seconds.")
            await asyncio.sleep(8)
            self.settings[member.server.id]['joined'] = 0
            self.save_settings()
            try:
                if self.settings[member.server.id]['protected']:
                    for channel in member.server.channels:
                        if channel.id != self.settings[member.server.id]['channel']:
                            perms = discord.PermissionOverwrite()
                            perms.read_messages = False
                            perms.send_messages = False
                            await self.bot.edit_channel_permissions(channel, member, perms)
                        else:
                            await self.bot.send_message(channel, "{}, you have been muted in every channel because raidprotect is on, if you are not here to raid just wait patiently and your permissions will be restored.".format(member.mention))
            except KeyError:
                return
        
def check_folders():
    if not os.path.exists("data/raidprotect"):
        print("Creating data/raidprotect folder...")
        os.makedirs("data/raidprotect")
        
def check_files():
    if not os.path.exists("data/raidprotect/settings.json"):
        print("Creating data/raidprotect/settings.json file...")
        dataIO.save_json("data/raidprotect/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(RaidProtect(bot))