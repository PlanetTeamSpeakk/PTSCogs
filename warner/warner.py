import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
import os
from .utils import checks

class Warner:
    """Warn people."""

    def __init__(self, bot):
        self.bot = bot
        self.warnings = dataIO.load_json("data/warner/warnings.json")
        
    @checks.mod_or_permissions()
    @commands.command(pass_context=True)
    async def warn(self, ctx, user:discord.Member):
        """Warn people for their actions."""
        serverid = ctx.message.server.id
        userid = user.id
        if serverid not in self.warnings:
            self.warnings[serverid] = {}
            dataIO.save_json("data/warner/warnings.json", self.warnings)
        if userid not in self.warnings[serverid]:
            self.warnings[serverid][userid] = 1
            dataIO.save_json("data/warner/warnings.json", self.warnings)
            await self.bot.say("1 warning has been added for the user.\nThat makes a total of 1 warning for this user.")
            return
        else:
            self.warnings[serverid][userid] = self.warnings[serverid][userid] + 1
            dataIO.save_json("data/warner/warnings.json", self.warnings)
            if self.warnings[serverid][userid] == 3:
                del self.warnings[serverid][userid]
                dataIO.save_json("data/warner/warnings.json", self.warnings)
                await self.bot.say("User has 3 warnings, what are you consequences? (btw, warnings are reset for this user!)")
                return
            if self.warnings[serverid][userid] > 3:
                await self.bot.say("User has over 3 warnings, wut?")
                return
            else:
                await self.bot.say("1 warning has been added for the user.\nThat makes a total of {} warnings for this user.".format(self.warnings[serverid][userid]))
                return
               
    @checks.mod_or_permissions()
    @commands.command(pass_context=True)
    async def resetwarns(self, ctx, user:discord.Member):
        """Reset the self.warnings you gave to someone"""
        serverid = ctx.message.server.id
        userid = user.id
        if serverid not in self.warnings:
            await self.bot.say("No one in this server has got a warning yet.")
            return
        elif userid not in self.warnings[serverid]:
            await self.bot.say("This user doesn't have a warning yet.")
            return
        else:
            del self.warnings[serverid][userid]
            dataIO.save_json("data/warner/warnings.json", self.warnings)
            await self.bot.say("Users warnings succesfully reset!")
            return
               
def check_folders():
    if not os.path.exists("data/warner"):
        print("Creating data/warner folder...")
        os.makedirs("data/warner")

def check_files():
    if not os.path.exists("data/warner/warnings.json"):
        print("Creating data/warner/warnings.json file...")
        dataIO.save_json("data/warner/warnings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Warner(bot))
