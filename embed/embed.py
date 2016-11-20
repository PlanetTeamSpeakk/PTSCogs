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
            'red, blue, green, gold, purple, dark_red, dark_blue and dark_green.\n\n'
            
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
            await self.bot.say("The examples would give the following output:")
            em = discord.Embed(description="This is a description", color=discord.Color.red(), title="This is a title")
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author.name
            em.set_author(name=author, icon_url=avatar)
            em.set_footer(text="This is a footer")
            await self.bot.say(embed=em)
            await self.bot.say("And,")
            await self.bot.say("@everyone @here, announcement!")
            em = discord.Embed(description="This is a description", color=discord.Color.red(), title="This is a title")
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author.name
            em.set_author(name=author, icon_url=avatar)
            em.set_footer(text="This is a footer")
            await self.bot.say(embed=em)

    @_embed.command(pass_context=True)
    @checks.mod_or_permissions()
    async def false(self, ctx, color, title, description, footer):
        """Embeds a message in the current channel."""
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
            await self.bot.say("That's not a valid color, use {}embed help to view help.".format(ctx.prefix))
            return
            
    @_embed.command(pass_context=True)
    @checks.mod_or_permissions()
    async def true(self, ctx, color, title, description, footer):
        """Embeds a message in the current channel."""
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
            await self.bot.say("That's not a valid color, use {}embed help to view help.".format(ctx.prefix))
            return
            
def setup(bot):
    bot.add_cog(embed(bot))