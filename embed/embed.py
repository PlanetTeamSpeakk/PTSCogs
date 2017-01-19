import discord
from .utils import checks
from __main__ import send_cmd_help
from discord.ext import commands

class embed:
    """embed"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, name="embed")
    @checks.mod_or_permissions()
    async def _embed(self, ctx):
        """Embeds a message in the current channel."""
        if ctx.invoked_subcommand is None:
            await self.bot.send_message(ctx.message.author, '```'
            'To use the embed command you need the following things,\n\n'
            
            'You need to know if it is an announcement,\n'
            'False: if it is not an announcement.\n'
            'True: if it is an announcement.\n\n'
            
            'You need a color (not colour, that\'s American), valid colors are:\n'
            'blue, dark_blue, dark_gold, dark_green, dark_grey, dark_magenta, dark_orange, dark_purple, dark_red, dark_teal, darker_grey, default, gold, green, light_grey, lighter_grey, magenta, orange, purple, red and teal.\n\n'
            
            'You need a title, if you want the title to be a sentence,\n'
            'Put it in quotes like "This is a title with more words".\n\n'
            
            'You need a description, this is optional but it is the text that will come under the title.\n'
            'This also has to be in quotes like "This is a description with more words".\n\n'
            
            'You can also leave parts away\n'
            'You can do this by just putting 2 quotes ("") and not putting anything inside of them.\n\n'
            
            'So an example would be \n'
            '{0}embed false red "This is a title" "This is a description" "This is a footer" or\n'
            '{0}embed true red "This is a title" "This is a description" "This is a footer" or\n'
            'Rembember, title, description and footer are optional.'
            '```'.format(ctx.prefix))
            await self.bot.send_message(ctx.message.author, "The examples would give the following output:")
            em = discord.Embed(description="This is a description", color=discord.Color.red(), title="This is a title")
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author.name
            em.set_author(name=author, icon_url=avatar)
            em.set_footer(text="This is a footer")
            await self.bot.send_message(ctx.message.author, embed=em)
            await self.bot.send_message(ctx.message.author, "And,")
            await self.bot.send_message(ctx.message.author, "@everyone @here, announcement!")
            em = discord.Embed(description="This is a description", color=discord.Color.red(), title="This is a title")
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author.name
            em.set_author(name=author, icon_url=avatar)
            em.set_footer(text="This is a footer")
            await self.bot.send_message(ctx.message.author, embed=em)

    @_embed.command(pass_context=True)
    @checks.mod_or_permissions()
    async def false(self, ctx, color, title, description, footer):
        """Embeds a message in the current channel."""
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            pass
        if color == "blue":
            color = 0X3498DB
        elif color == "dark_blue":
            color = 0X206694
        elif color == "dark_gold":
            color = 0XC27C0E
        elif color == "dark_green":
            color = 0X1F8B4C
        elif color == "dark_grey":
            color = 0X607D8B
        elif color == "dark_magenta":
            color = 0XAD1457
        elif color == "dark_orange":
            color = 0XA84300
        elif color == "dark_purple":
            color = 0X71368A
        elif color == "dark_red":
            color = 0X992D22
        elif color == "dark_teal":
            color = 0X11806A
        elif color == "darker_grey":
            color = 0X546E7A
        elif color == "default":
            color = 0X000000
        elif color == "gold":
            color = 0XF1C40F
        elif color == "green":
            color = 0X2ECC71
        elif color == "light_grey":
            color = 0X979C9f
        elif color == "lighter_grey":
            color = 0X95A5A6
        elif color == "magenta":
            color = 0XE91E63
        elif color == "orange":
            color = 0XE67E22
        elif color == "purple":
            color = 0X9B59B6
        elif color == "red":
            color = 0XE74C3C
        elif color == "teal":
            color = 0X1ABC9C
        try:
            em = discord.Embed(description=description, color=color, title=title)
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
            
    @_embed.command(pass_context=True)
    @checks.mod_or_permissions()
    async def true(self, ctx, color, title, description, footer):
        """Embeds a message in the current channel."""
        try:
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            pass
        if color == "blue":
            color = 0X3498DB
        elif color == "dark_blue":
            color = 0X206694
        elif color == "dark_gold":
            color = 0XC27C0E
        elif color == "dark_green":
            color = 0X1F8B4C
        elif color == "dark_grey":
            color = 0X607D8B
        elif color == "dark_magenta":
            color = 0XAD1457
        elif color == "dark_orange":
            color = 0XA84300
        elif color == "dark_purple":
            color = 0X71368A
        elif color == "dark_red":
            color = 0X992D22
        elif color == "dark_teal":
            color = 0X11806A
        elif color == "darker_grey":
            color = 0X546E7A
        elif color == "default":
            color = 0X000000
        elif color == "gold":
            color = 0XF1C40F
        elif color == "green":
            color = 0X2ECC71
        elif color == "light_grey":
            color = 0X979C9f
        elif color == "lighter_grey":
            color = 0X95A5A6
        elif color == "magenta":
            color = 0XE91E63
        elif color == "orange":
            color = 0XE67E22
        elif color == "purple":
            color = 0X9B59B6
        elif color == "red":
            color = 0XE74C3C
        elif color == "teal":
            color = 0X1ABC9C
        try:
            em = discord.Embed(description=description, color=color, title=title)
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author.name
            em.set_author(name=author, icon_url=avatar)
            em.set_footer(text=footer)
            await self.bot.say("@everyone, @here, announcement!", embed=em)
            return
        except discord.NotFound:
            await self.bot.say("Couldn't find the message to embed, did it get deleted?")
            return
        except discord.HTTPException:
            await self.bot.say("Hmm, an unknown error occured when embedding.")
            return
            
def setup(bot):
    bot.add_cog(embed(bot))