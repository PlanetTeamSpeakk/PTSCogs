import discord
from discord.ext import commands
from .utils import checks
from __main__ import send_cmd_help, settings
from cogs.utils.dataIO import dataIO
import os

class Adkillr:
    """Adkillr"""

    def __init__(self, bot):
        self.bot = bot
        self.adkillr = dataIO.load_json("data/adkillr/adkillr.json")
        
    async def adkill(self, message):
        """Kill them ads!"""
        serverid = message.server.id
        ad = message
        if ad.server is None:
            pass
        try:
            temp = self.adkillr[ad.server.id]['toggle']
        except:
            temp = ""
            self.adkillr[serverid] = {'toggle': True}
            dataIO.save_json("data/adkillr/adkillr.json", self.adkillr)
        if self.adkillr[serverid]['toggle'] is True:
            if "http://" in ad.content.lower() or "https://" in ad.content.lower():
                if "." in ad.content.lower():
                    if ad.author.id == settings.owner:
                        pass
                    elif ad.author.permissions_in(ad.channel).manage_messages:
                        pass
                    else:
                        if self.bot.user.permissions_in(ad.channel).manage_messages:
                            await self.bot.delete_message(ad)
                            await self.bot.send_message(message.channel, "{} don't send links!".format(ad.author.mention))

    @commands.group(name = "adkillr", pass_context=True, no_pm=True)
    async def _adkillr(self, ctx):
        """Manages the settings for Adkillr."""
        serverid = ctx.message.server.id
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
        if serverid not in self.adkillr:
            self.adkillr[serverid] = {'toggle': True}
            dataIO.save_json("data/adkillr/adkillr.json", self.adkillr)

    @_adkillr.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def toggle(self, ctx):
        """Enable/disables Adkillr in the server."""
        serverid = ctx.message.server.id
        if self.adkillr[serverid]['toggle'] is True:
            self.adkillr[serverid]['toggle'] = False
            await self.bot.say('Adkillr is now disabled')
        elif self.adkillr[serverid]['toggle'] is False:
            self.adkillr[serverid]['toggle'] = True
            await self.bot.say('Adkillr is now enabled')
        dataIO.save_json("data/adkillr/adkillr.json", self.adkillr)
        
def check_folders():
    if not os.path.exists("data/adkillr"):
        print("Creating data/adkillr folder...")
        os.makedirs("data/adkillr")
        
def check_files():
    if not os.path.exists("data/adkillr/adkillr.json"):
        print("Creating data/adkillr/adkillr.json file...")
        dataIO.save_json("data/adkillr/adkillr.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    n = Adkillr(bot)
    bot.add_listener(n.adkill, "on_message")
    bot.add_cog(Adkillr(bot))