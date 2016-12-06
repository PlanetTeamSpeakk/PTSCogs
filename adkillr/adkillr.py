import discord
from discord.ext import commands
from .utils import checks
from __main__ import send_cmd_help, settings

class Adkillr:
    """Adkillr"""

    def __init__(self, bot):
        self.bot = bot
        
    async def adkillr(self, message):
        """Kill them ads!"""
        ad = message
        if ad.server is None:
            pass
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
                    else:
                        pass
            else: # I know these aren't needed but I like my else and passes :3.
                pass
        else:
            pass
        
def setup(bot):
    n = Adkillr(bot)
    bot.add_listener(n.adkillr, "on_message")
    bot.add_cog(Adkillr(bot))