import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
import os
from .utils import checks

class GiveMe:
    """Makes members able to give themselves roles."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/giveme/settings.json")

    @commands.group(pass_context=True, invoke_without_command=True, no_pm=True)
    async def giveme(self, ctx, *, role):
        """Give yourself roles"""
        if ctx.message.server.id not in self.settings:
            await self.bot.say("There are no giveme's for this server.")
            return
        elif role not in self.settings[ctx.message.server.id]['givemes']:
            await self.bot.say("You can't assign that role to yourself. Yet...")
        else:
            role = discord.utils.get(ctx.message.server.roles, id=self.settings[ctx.message.server.id]['givemes'][role])
            await self.bot.add_roles(ctx.message.author, role)
            await self.bot.say("The role has been added, you're welcome.")

            
    @giveme.command(pass_context=True)
    async def list(self, ctx):
        """Lists the giveme's this server has."""
        if ctx.message.server.id not in self.settings:
            await self.bot.say("This server has no givemes.")
            return
        elif self.settings[ctx.message.server.id]['givemes'] == {}:
            await self.bot.say("This server has no givemes.")
            return
        else:
            await self.bot.say("This server has the following givemes:\n{}.".format(", ".join(self.settings[ctx.message.server.id]['givemes'].keys())))
            return
            
    @giveme.command(pass_context=True)
    @checks.admin_or_permissions()
    async def add(self, ctx, name, role:discord.Role):
        """Adds a role to the list of giveme's, if the role contains spaces put it in quotes (").
        Example:
        [p]giveme add "role name" role_mention OR
        [p]giveme add "role name" "name of the new role\""""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'givemes': {}}
        self.settings[ctx.message.server.id]['givemes'][name] = role.id
        self.save_settings()
        await self.bot.say("Giveme has been added.")
        
    @giveme.command(pass_context=True)
    @checks.admin_or_permissions()
    async def remove(self, ctx, role):
        """Removes a role from the list of giveme's."""
        if ctx.message.server.id not in self.settings:
            await self.bot.say("This server has no giveme's.")
            return
        elif role not in self.settings[ctx.message.server.id]['givemes'].keys():
            await self.bot.say("That is not a valid giveme.")
            return
        else:
            del self.settings[ctx.message.server.id]['givemes'][role]
            self.save_settings()
            await self.bot.say("Giveme has been removed.")
                
    def save_settings(self):
        dataIO.save_json("data/giveme/settings.json", self.settings)
            
def check_folders():
    if not os.path.exists("data/giveme"):
        print("Creating data/giveme folder...")
        os.makedirs("data/giveme")

def check_files():
    if not os.path.exists("data/giveme/settings.json"):
        print("Creating data/giveme/settings.json file...")
        dataIO.save_json("data/giveme/settings.json", {})
            
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(GiveMe(bot))