from discord.ext import commands
from .utils import checks
from __main__ import settings
import aiohttp
import asyncio
import os
import discord
import discord.utils
import time
import datetime
import sys

class useful:
    """Useful stuffz!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="avatar", aliases=["av"])
    async def avatar(self, ctx, user : discord.Member):
        if user.avatar_url:
            avatar = user.avatar_url
        else:
            avatar = user.default_avatar_url
        em = discord.Embed(color=discord.Color.red())
        em.add_field(name=user.mention + "'s avatar", value=avatar)
        em.set_image(url=avatar, height="128", width="128")
        await self.bot.say(embed=em)
	
    @commands.command(pass_context=True, name="calc", aliases=["calculate"])
    async def _calc(self, ctx, num, operation, num2):
        if operation == "/":
            await self.bot.say("{} / {} = {}".format(num, num2, int(num) / int(num2)))
        elif operation == "+":
            await self.bot.say("{} + {} = {}".format(num, num2, int(num) + int(num2)))
        elif operation == "*":
            await self.bot.say("{} * {} = {}".format(num, num2, int(num) * int(num2)))
        elif operation == "x":
            await self.bot.say("{} x {} = {}".format(num, num2, int(num) * int(num2)))
        elif operation == "-":
            await self.bot.say("{} - {} = {}".format(num, num2, int(num) - int(num2)))
        else:
            await self.bot.say("Correct Usage: [p]calc [number] [operation] [second number]")
			
    @commands.command(pass_context=True)
    async def suggest(self, ctx, *, suggestion : str):
        """Sends a suggestion to the owner."""
        if settings.owner == "id_here":
            await self.bot.say("I have no owner set, cannot suggest.")
            return
        owner = discord.utils.get(self.bot.get_all_members(), id=settings.owner)
        author = ctx.message.author
        if ctx.message.channel.is_private is False:
            server = ctx.message.server
            source = "server **{}** ({})".format(server.name, server.id)
        else:
            source = "direct message"
        sender = "**{}** ({}) sent you a suggestion from {}:\n\n".format(author, author.id, source)
        message = sender + suggestion
        try:
            await self.bot.send_message(owner, message)
        except discord.errors.InvalidArgument:
            await self.bot.say("I cannot send your message, I'm unable to find"
                               " my owner... *sigh*")
        except discord.errors.HTTPException:
            await self.bot.say("Your message is too long.")
        except:
            await self.bot.say("I'm unable to deliver your message. Sorry.")
        else:
            await self.bot.say("Your message has been sent.")
            
    @commands.command(pass_context=True)
    async def botowner(self, ctx):
        """Shows you who's boss!"""
        await self.bot.say("My owner is <@{}>.".format(settings.owner))
        
    @commands.command(pass_context=True)
    async def saytts(self, ctx, *, msg):
        """Sends a message with text to speech."""
        try:
            await self.bot.send_message(ctx.message.channel, tts=True, content=msg)
        except discord.Forbidden:
            await self.bot.say("Can't send tts message.")
            
    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """Sends you a link to invite the bot to your server."""
        url = await get_oauth_url(self)
        self.bot.oauth_url = url
        await self.bot.say(""
        "{}, to invite the bot to your server use this link:\n"
        "{}&permissions=-1"
        "\n**BEWARE** You need the 'manage server' permission to add bots.".format(ctx.message.author.mention, url))
        
    @commands.command(pass_context=True)
    async def genoauth(self, ctx, client_id:int, perms=None):
        """Generates an oauth url (aka invite link) for your bot, for permissions goto https://discordapi.com/permissions.html. Or just put 'all' or 'admin'."""
        url = discord.utils.oauth_url(client_id)
        if perms == "all":
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions=-1".format(ctx.message.author.mention, url))
        elif perms == "admin":
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions=8".format(ctx.message.author.mention, url))
        elif perms:
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions={}".format(ctx.message.author.mention, url, perms))
        else:
            await self.bot.say(""
            "{}, here you go:\n"
            "{}".format(ctx.message.author.mention, url))
            
    @commands.command(pass_context=True)
    async def genbotoauth(self, ctx, bot:discord.Member, perms=None):
        """Generates an oauth url (aka invite link) for your bot, for permissions goto https://discordapi.com/permissions.html. Or just put 'all' or 'admin'."""
        url = discord.utils.oauth_url(bot.id)
        if bot.bot == False:
            await self.bot.say("User is not a bot.")
            return
        if perms == "all":
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions=-1".format(ctx.message.author.mention, url))
        elif perms == "admin":
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions=8".format(ctx.message.author.mention, url))
        elif perms:
            await self.bot.say(""
            "{}, here you go:\n"
            "{}&permissions={}".format(ctx.message.author.mention, url, perms))
        else:
            await self.bot.say(""
            "{}, here you go:\n"
            "{}".format(ctx.message.author.mention, url))
            
    @checks.mod_or_permissions()
    @commands.command(pass_context=True)
    async def uploadcog(self, ctx, cogname):
        await self.bot.say("Here you go:")
        await self.bot.send_file(ctx.message.channel, fp="cogs/{}.py".format(cogname), filename="{}.py".format(cogname))

async def get_oauth_url(self):
    try:
        data = await self.bot.application_info()
    except AttributeError:
        return "Your discord.py is outdated. Couldn't retrieve invite link."
    return discord.utils.oauth_url(data.id)

def setup(bot):
    bot.add_cog(useful(bot))