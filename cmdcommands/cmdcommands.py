import discord
from os import name
from .utils import checks
from discord.ext import commands
from __main__ import send_cmd_help
from subprocess import check_output, CalledProcessError
import os
import aiohttp
import asyncio

class cmdcommands:
    """Commands for the owner to run using the CommandPrompt!"""

    def __init__(self, bot):
        self.bot = bot
        if name != "nt":
            raise Exception("This cog is for Windows only")

    @commands.group(name="cmdcommands", pass_context=True, invoke_without_command=True)
    @checks.is_owner()
    async def _cmdcommands(self, ctx, *, command):
        if command == "del System32":
            await self.bot.say("Hell nah I ain't deleting System32.")
            return
        elif command == "del Windows/System32":
            await self.bot.say("Hell nah I ain't deleting System32.")
            return
        elif command == "del C:/Windows/System32":
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
            output = check_output("copy data\cmdcommands\emptycog.py cogs\{}.py".format(cogname), shell=True)
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
            
    async def on_ready(self):
        self.emptycogLoaded = os.path.exists('data/cmdcommands/emptycog.py')
        if not self.emptycogLoaded:
            print('Emptycog.py was not found, trying to download')
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/emptycog.py") as r:
                    emptycog = await r.content.read()
                with open('data/cmdcommands/emptycog.py','wb') as f:
                    f.write(emptycog)
                print('Succesfully downloaded emptycog.py')
            except Exception as e:
                print(e)
                print("Error occured, did not download emptycog.py, go to https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/emptycog.py press ctrl+s and save it in the data/cmdcommands/ folder.")
        else:
            await asyncio.sleep(0.5)
            print('Found emptycog.py, this is good.')
            
def check_folders():
    if not os.path.exists("data/cmdcommands"):
        print("Creating data/cmdcommands folder...")
        os.makedirs("data/cmdcommands")

def setup(bot):
    check_folders()
    n = cmdcommands(bot)
    bot.add_cog(cmdcommands(bot))