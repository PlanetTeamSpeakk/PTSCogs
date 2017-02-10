import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os

class CMDSuffix:
    """Process commands when the message ends with something and doesn't begin with it."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/cmdsuffix/settings.json")

    @commands.command(name="setsuffix", pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def _setsuffix(self, ctx, *, suffix):
        """Sets the command suffix."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'suffix': None, 'disabled': False}
        self.settings[ctx.message.server.id]['suffix'] = suffix
        self.save_settings()
        await self.bot.say("Suffix set, if you want to disable this do {}togglesuffix.".format(ctx.prefix))
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def togglesuffix(self, ctx):
        """Toggles if users can use command suffixes."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'suffix': None, 'disabled': True}
            await self.bot.say("Command suffixes have been disabled.")
        elif self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = False
            await self.bot.say("Command suffixes have been enabled.")
        else:
            self.settings[ctx.message.server.id]['disabled'] = True
            await self.bot.say("Command suffixes have been disabled.")
        self.save_settings()
        
    async def on_message(self, message):
        if message.server != None:
            if message.server.id in self.settings:
                if message.content.endswith(self.settings[message.server.id]['suffix']) and not self.settings[message.server.id]['disabled']:
                    message.content = list(self.bot.command_prefix(self.bot, message))[0] + message.content[:(len(message.content) - len(self.settings[message.server.id]['suffix']))]
                    await self.bot.process_commands(message)
        
    def save_settings(self):
        dataIO.save_json("data/cmdsuffix/settings.json", self.settings)
        
def check_folders():
    if not os.path.exists("data/cmdsuffix"):
        print("Creating data/cmdsuffix folder...")
        os.makedirs("data/cmdsuffix")
   
def check_files():
    if not os.path.exists("data/cmdsuffix/settings.json"):
        print("Creating data/cmdsuffix/settings.json file...")
        dataIO.save_json("data/cmdsuffix/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(CMDSuffix(bot))