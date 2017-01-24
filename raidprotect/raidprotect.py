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
    async def raidprotect(self, ctx):
        """Manage raidprotect."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        if not ctx.message.server.id in self.settings:
            self.settings[ctx.message.server.id] = {'joined': 0, 'channel': None, 'members': 4, 'protected': False}
            self.save_settings()
            
    @raidprotect.command(pass_context=True)
    @checks.admin_or_permissions()
    async def setchannel(self, ctx, channel:discord.Channel):
        """Sets the channel new members should see when protected."""
        self.settings[ctx.message.server.id]['channel'] = channel.id
        self.save_settings()
        await self.bot.say("Channel set.")
            
    @raidprotect.command(pass_context=True)
    @checks.admin_or_permissions()
    async def toggle(self, ctx):
        """Toggle raidprotect."""
        if self.settings[ctx.message.server.id]['protected']:
            self.settings[ctx.message.server.id]['protected'] = False
            await self.bot.say("Your server is no longer protected, anyone that joins will be able to see all channels.")
        else:
            self.settings[ctx.message.server.id]['protected'] = True
            await self.bot.say("Your server is now protected, anyone that joins will only be able to see the set channel.")
        self.save_settings()
        
    @raidprotect.command(pass_context=True)
    @checks.admin_or_permissions()
    async def setmembers(self, ctx, members:int):
        """Sets after how many members join in 8 seconds the bot will protect the server.
        0 is unlimited, so that will turn it off. Default is 4."""
        self.settings[ctx.message.server.id]['members'] = members
        self.save_settings()
        await self.bot.say("Members set")
    
    @raidprotect.command(pass_context=True)
    async def members(self, ctx):
        """Shows you how much people should join within 8 seconds before the bot should turn on raid protect.
        0 is unlimited."""
        await self.bot.say("The bot will turn on raidprotect when {} people join in 8 seconds.".format(self.settings[ctx.message.server.id]['members']))
    
    def save_settings(self):
        dataIO.save_json("data/raidprotect/settings.json", self.settings)
        
    async def on_member_join(self, member):
        if (member.server.id in self.settings) and not ("bots" in member.server.name.lower()):
            try:
                temp = self.settings[member.server.id]['joined']
            except KeyError:
                self.settings[member.server.id]['joined'] = 0
            try:
                self.settings[member.server.id]['joined'] += 1
                self.save_settings()
                if self.settings[member.server.id]['members'] != 0:
                    if (self.settings[member.server.id]['joined'] >= self.settings[member.server.id]['members']) and not (self.settings[member.server.id]['protected']):
                        self.settings[member.server.id]['protected'] = True
                        self.save_settings()
                        for channel in member.server.channels:
                            if (channel.id == self.settings[member.server.id]['channel']) and (self.settings[member.server.id]['channel'] != None):
                                await self.bot.send_message(channel, "Raid protect has been turned on, more than {} people joined within 8 seconds.".format(self.settings[member.server.id]['members']))
                await asyncio.sleep(8)
                self.settings[member.server.id]['joined'] = 0
                self.save_settings()
            except KeyError:
                pass
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