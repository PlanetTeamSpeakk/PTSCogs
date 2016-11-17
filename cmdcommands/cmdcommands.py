import discord
from os import name
from .utils import checks
from discord.ext import commands
from __main__ import send_cmd_help
from subprocess import check_output, CalledProcessError

class cmdcommands:
    """Commands for the owner to run using the CommandPrompt!"""

    def __init__(self, bot):
        self.bot = bot
        if name != "nt":
            raise Exception("This cog is for Windows only")

    @commands.group(name="cmdcommands", pass_context=True)
    @checks.is_owner()
    async def _cmdcommands(self, ctx):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_cmdcommands.command()
    @checks.is_owner()
    async def cmd(self, *, command):
        """Runs a command from the commandprompt."""
        if command == "del System32":
            await self.bot.say("Hell nah I ain't deleting System32.")
            return
        try:
            output = check_output(command, shell=True)
            await self.bot.say("Command `{}` ran from the commandprompt!".format(command))
        except CalledProcessError as error:
            output = error.output
			
    @_cmdcommands.command(name="md", aliases=["makedir", "mdir", "mdirectory", "makedirectory"])
    @checks.is_owner()
    async def md(self, directoryname):
        """Makes a directory (a folder)."""
        try:
            output = check_output("mkdir {}".format(directoryname), shell=True)
            await self.bot.say("Directory `{}` made! Check your root folder.".format(directoryname))
        except CalledProcessError as error:
            output = error.output
			
    @_cmdcommands.command()
    @checks.is_owner()
    async def pip3install(self, *, packagename):
        """Makes you able to install Python programs for Python 3.5"""
        try:
            output = check_output("pip3 install {}".format(packagename), shell=True)
            await self.bot.say("`{}` installed succesfully!".format(packagename))
        except CalledProcessError as error:
            output = error.output
			
    @_cmdcommands.command()
    @checks.is_owner()
    async def pipinstall(self, *, packagename):
        """Makes you able to install Python programs."""
        try:
            output = check_output("pip install {}".format(packagename), shell=True)
            await self.bot.say("`{}` installed succesfully!".format(packagename))
        except CalledProcessError as error:
            output = error.output
            
    @_cmdcommands.command()
    @checks.is_owner()
    async def pip3upgrade(self, *, packagename):
        """Makes you able to install Python programs for Python 3.5 with the --upgrade tag."""
        try:
            output = check_output("pip3 install {} --upgrade".format(packagename), shell=True)
            await self.bot.say("`{}` upgraded succesfully!".format(packagename))
        except CalledProcessError as error:
            output = error.output
			
    @_cmdcommands.command()
    @checks.is_owner()
    async def pipupgrade(self, *, packagename):
        """Makes you able to install Python programs with the --upgrade tag."""
        try:
            output = check_output("pip install {} --upgrade".format(packagename), shell=True)
        except CalledProcessError as error:
            output = error.output
			
    @_cmdcommands.command(pass_context=True)
    @checks.is_owner()
    async def emptycog(self, ctx, cogname):
        """Makes an empty cog for you."""
        try:
            output = check_output("copy emptycog.py cogs\{}.py".format(cogname), shell=True)
            await self.bot.say("Cog `{}.py` created, do you want to open the cog to edit it? (yes/no)".format(cogname))
            answer = await self.bot.wait_for_message(timeout=15, author=ctx.message.author)
            if answer is None:
                await self.bot.say("Didn't edit the file, no response.")
                return
            elif "yes" not in answer.content.lower():
                await self.bot.say("Didn't edit the file, answer was not yes.")
                return
            output = check_output("start cogs\{}".format(cogname), shell=True)
            await self.bot.say("Cog editing launched.")
        except CalledProcessError as error:
            output = error.output
            
    @_cmdcommands.command(pass_context=True)
    @checks.is_owner()
    async def startcog(self, ctx, cogname):
        """Starts a cog in the cogs folder to edit it."""
        try:
            output = check_output("start cogs\{}.py".format(cogname), shell=True)
            await self.bot.say("Cog `{}` started.".format(cogname))
        except CalledProcessError as error:
            output = error.output
            await self.bot.say(error.output)

def setup(bot):
    bot.add_cog(cmdcommands(bot))