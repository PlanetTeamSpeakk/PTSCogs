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
        await self.bot.say("{}'s current avatar is: \n{}".format(user.mention, user.avatar_url))
		
    @commands.command(pass_context=True, name="defaultavatar", aliases=["defav", "defavatar"])
    async def defaultavatar(self, ctx, user : discord.Member):
        await self.bot.say("{}'s default avatar is: \n{}".format(user.mention, user.default_avatar_url))
	
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
    async def owner(self, ctx):
        """Shows you who's boss!"""
        await self.bot.say("My owner is **{}**.".format(ctx.message.server.owner))

def setup(bot):
    bot.add_cog(useful(bot))