import discord
from .utils import checks
from __main__ import settings
from discord.ext import commands

class spam:
    """Spams."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.mod_or_permissions()
    async def spam(self, ctx, user : discord.Member, spamtext, number : int=0):
        """Spams x times, default is 4."""
        if user.id == "96987941519237120":
            await self.bot.say("Hell nah, I ain't spamming him.")
            return
        if user.id == settings.owner:
            await self.bot.say("Hell nah, I ain't spamming him. If you want to spam my owner use the `suggest` command!")
            return
        if number >> 8:
            await self.bot.say("Hell nah, not past 8 for fck sakes.")
            return
        if number == 0:
            number = 4
        counter = 0
        while counter < number:
            try:
                await self.bot.send_message(user, "{}, sent by **{}**".format(spamtext, ctx.message.author))
            except discord.Forbidden:
                await self.bot.say("{} blocked me :sob:".format(user.mention))
                return
            counter = counter + 1
            if counter == 1:
                await self.bot.say("Hehe, {} got spammed {} time!".format(user.mention, counter))
            else:
                await self.bot.say("Hehe, {} got spammed {} time!".format(user.mention, counter))
            
    @commands.command(pass_context = True)
    @checks.mod_or_permissions()
    async def aspam(self, ctx, user : discord.Member, spamtext, number : int=0):
        """Spams x times, default is 4."""
        if user.id == "96987941519237120":
            await self.bot.say("Hell nah, I ain't spamming him.")
            return
        if user.id == settings.owner:
            await self.bot.say("Hell nah, I ain't spamming him. If you want to spam my owner use the `suggest` command!")
            return
        if number >> 8:
            await self.bot.say("Hell nah, not past 8 for fck sakes.")
            return
        if number == 0:
            number = 4
        counter = 0
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            pass
        while counter < number:
            try:
                await self.bot.send_message(user, "{}".format(spamtext))
            except discord.Forbidden:
                await self.bot.say("{} blocked me :sob:".format(user.mention))
                return
            counter = counter + 1
            if counter == 1:
                await self.bot.say("Hehe, {} got spammed {} time!".format(user.mention, counter))
            else:
                await self.bot.say("Hehe, {} got spammed {} times!".format(user.mention, counter))
            
    @commands.command(pass_context = True)
    @checks.mod_or_permissions()
    async def cspam(self, ctx, spamtext, number : int=0):
        """Spams x times in the channel, default is 4."""
        if number == 0:
            number = 4
        counter = 0
        while counter < number:
            await self.bot.say("{}, sent by **{}**.".format(spamtext, ctx.message.author))
            counter = counter + 1  
            
    @commands.command(pass_context = True)
    @checks.mod_or_permissions()
    async def acspam(self, ctx, spamtext, number : int=0):
        """Spams x times in the channel anonymously, default is 10."""
        if number == 0:
            number = 4
        counter = 0
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            pass
        while counter < number:
            await self.bot.say("{}".format(spamtext))
            counter = counter + 1  

def setup(bot):
    if bot.user.id == "271320945115791371":
        raise RuntimeError("Gfy Nathan, just use Impulse ffs. Cunt.")
    bot.add_cog(spam(bot))