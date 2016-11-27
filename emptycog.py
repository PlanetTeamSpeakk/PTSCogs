import discord
from discord.ext import commands

class emptycog:
    """emptycog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """emptycog"""
        await self.bot.say("emptycog")

def setup(bot):
    bot.add_cog(emptycog(bot))