import discord
from .utils import checks
from discord.ext import commands
from .utils import cmdlogger

class embed:
    """embed"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions()
    async def embed(self, ctx, is_announcement, color, title, description, footer=None):
        """Embeds a message in the current channel."""
        await cmdlogger.logcmd(ctx)
        if is_announcement == "true":
            await self.bot.say("@everyone @here, announcement!")
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            pass
        if color == "red":
            try:
                em = discord.Embed(description=description, color=discord.Color.red(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "blue":
            try:
                em = discord.Embed(description=description, color=discord.Color.blue(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "green":
            try:
                em = discord.Embed(description=description, color=discord.Color.green(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "gold":
            try:
                em = discord.Embed(description=description, color=discord.Color.gold(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "purple":
            try:
                em = discord.Embed(description=description, color=discord.Color.purple(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "dark_red":
            try:
                em = discord.Embed(description=description, color=discord.Color.dark_red(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "dark_blue":
            try:
                em = discord.Embed(description=description, color=discord.Color.dark_blue(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        elif color == "dark_green":
            try:
                em = discord.Embed(description=description, color=discord.Color.dark_green(), title=title)
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author.name
                em.set_author(name=author, icon_url=avatar)
                em.set_footer(text=footer)
                await self.bot.say(embed=em)
                return
            except discord.NotFound:
                await self.bot.say("Couldn't find the message to embed, did it get deleted?")
                return
            except discord.HTTPException:
                await self.bot.say("Hmm, an unknown error occured when embedding.")
                return
        else:
            await self.bot.say("That's not a valid color")
            return

def setup(bot):
    bot.add_cog(embed(bot))