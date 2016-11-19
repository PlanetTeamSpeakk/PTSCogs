from discord.ext import commands
import discord

class harambe:
    """#DixOutForHarambe"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def harambe(self):
        """#DixOutForHarambe"""
        await self.bot.say("#DixOutForHarambe, our dix will forever be out for you Harambe. \nR.I.P. Harambe the American gorilla, May 28th 2016. :sob: \nDo `[p]harambeinfo` for some information about the (sadly now dead :sob:) Harambe.")

    @commands.command()
    async def harambeinfo(self):
        """Gives you some information about the (sadly now dead) Harambe"""
        await self.bot.say("Species	    Western lowland gorilla \nSex	        Male \nBorn	    May 27, 1999 \nDied        May 28, 2016 (aged 17) Cincinnati Zoo and Botanical Garden, Cincinnati, Ohio, US \nKnown for	Circumstances of death \nResidence	Gladys Porter Zoo (1999–2014) \nWeight	    440 lb (200 kg) \nNamed after `Harambe (Working Together for Freedom)`, song by Rita Marley \nR.I.P. Harambe May 28th 2016, our dix will forever be out for you Harambe :sob:")

def setup(bot):
    bot.add_cog(harambe(bot))
