import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os

class Autorole:
    """Automatically assign roles to new members on join."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/autorole/settings.json")

    @commands.group(pass_context=True)
    @checks.admin_or_permissions()
    async def autorole(self, ctx):
        """Manage autorole settings."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'ROLE': None, 'TOGGLED': False}
            self.save_settings()
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say("```Role: {}\nDisabled: {}```".format(self.settings[ctx.message.server.id]['ROLE'], self.settings[ctx.message.server.id]['TOGGLED']))

    @autorole.command(pass_context=True)
    async def setrole(self, ctx, role:discord.Role):
        """Set the role the bot should assign on join, the highest role that the bot has should be higher than this one."""
        self.settings[ctx.message.server.id]['ROLE'] = role.id
        self.save_settings()
        await self.bot.say("Role has been set.")
        
    @autorole.command(pass_context=True)
    async def toggle(self, ctx):
        """Toggle if the bot should assign a role on member join."""
        if not self.settings[ctx.message.server.id]['TOGGLED']:
            self.settings[ctx.message.server.id]['TOGGLED'] = True
            await self.bot.say("The bot will once again assign a role on member join.")
        else:
            self.settings[ctx.message.server.id]['TOGGLED'] = True
            await self.bot.say("The bot will no longer assign a role on member join.")
        self.save_settings()
        
    async def on_member_join(self, member):
        if (member.server.id in self.settings) and (self.settings[member.server.id]['ROLE'] != None):
            role = discord.utils.get(member.server.roles, id=self.settings[member.server.id]['ROLE'])
            if role != None:
                try:
                    await self.bot.add_roles(member, role)
                except:
                    pass
            
    def save_settings(self):
        dataIO.save_json("data/autorole/settings.json", self.settings)
            
def check_folders():
    if not os.path.exists("data/autorole"):
        print("Creating data/autorole folder...")
        os.makedirs("data/autorole")
        
def check_files():
    if not os.path.exists("data/autorole/settings.json"):
        print("Creating data/autorole/settings.json file...")
        dataIO.save_json("data/autorole/settings.json", {})
            
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Autorole(bot))