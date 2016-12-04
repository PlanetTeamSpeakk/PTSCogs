from discord.ext import commands
from .utils import checks
from __main__ import settings
import os
import discord
import glob
from .utils.chat_formatting import pagify, box
import re

class Useful:
    """Useful stuffz!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="avatar", aliases=["av"])
    async def avatar(self, ctx, user:discord.Member=None):
        if not user:
            user = ctx.message.author.mention
        if user.avatar_url:
            avatar = user.avatar_url
        else:
            avatar = user.default_avatar_url
        em = discord.Embed(color=discord.Color.red())
        em.add_field(name=user.mention + "'s avatar", value="[Avatar]({})".format(avatar))
        em.set_image(url=avatar)
        await self.bot.say(embed=em)
       
    @commands.command(pass_context=True, name="calc")
    async def _calc(self, ctx, evaluation):
        """Solves a math problem so you don't have to!
        + = add, - = subtract, * = multiply, and / = divide
        
        Example:
        [p]calc 1+1+3*4"""
        prob = re.sub("[^0-9+-/* ]", "", ctx.message.content[len(ctx.prefix + "calc "):].strip())
        try:
            answer = str(eval(prob))
            await self.bot.say("`{}` = `{}`".format(prob, answer))
        except:
            await self.bot.say("I couldn't solve that problem, it's too hard")
			
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
        url = discord.utils.oauth_url(self.bot.user.id)
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
        """Generates an oauth url (aka invite link) for your bot.
        For permissions goto https://discordapi.com/permissions.html. Or just put 'all' or 'admin'.
        Doesn't always work"""
        url = discord.utils.oauth_url(bot.id)
        if not bot.bot:
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
        """Uploads a cog for you to use, for a list of cogs use [p]show_cogs"""
        await self.bot.say("Here you go:")
        await self.bot.send_file(ctx.message.channel, fp="cogs/{}.py".format(cogname), filename="{}.py".format(cogname))
        
    # copied from the owner cog since the command there was owner only and here it isn't :3
    @checks.mod_or_permissions()
    @commands.command()
    async def show_cogs(self):
        """Shows loaded/unloaded cogs"""
        loaded = [c.__module__.split(".")[1] for c in self.bot.cogs.values()]
        unloaded = [c.split(".")[1] for c in self._list_cogs()
                    if c.split(".")[1] not in loaded]

        if not unloaded:
            unloaded = ["None"]

        msg = ("+ Loaded\n"
               "{}\n\n"
               "- Unloaded\n"
               "{}"
               "".format(", ".join(sorted(loaded)),
                         ", ".join(sorted(unloaded)))
               )
        for page in pagify(msg, [" "], shorten_by=16):
            await self.bot.say(box(page.lstrip(" "), lang="diff"))
         
    @commands.command()
    async def discrim(self, number):
        """Shows you how many people the bot can see that have that discrim."""
        members = []
        for member in list(self.bot.get_all_members()):
            if member.discriminator == number and member not in members:
                members.append(member)
        if len(members) == 0:
            members = "I could not find any users in any of the servers I'm in with a discriminator of `{}`".format(number)
        else:
            members = "```{}.```".format(", ".join(members))
        await self.bot.say("I found {}".format(members))

    def _list_cogs(self):
        cogs = [os.path.basename(f) for f in glob.glob("cogs/*.py")]
        return ["cogs." + os.path.splitext(f)[0] for f in cogs]
        
def setup(bot):
    bot.add_cog(Useful(bot))
