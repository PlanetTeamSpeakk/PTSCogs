from discord.ext import commands
from .utils import checks
from __main__ import settings
import os
import discord
import glob
from .utils.chat_formatting import pagify, box
import re
import os
import aiohttp
import urllib
import asyncio
import random
from random import choice
from subprocess import check_output
try:
    import ffmpy
    ffmpyinstalled = True
except:
    print("You don't have ffmpy installed, installing it now...")
    try:
        check_output("pip3 install ffmpy", shell=True)
        print("FFMpy installed succesfully!")
        import ffmpy
        ffmpyinstalled = True
    except:
        print("FFMpy didn't install succesfully.")
        ffmpyinstalled = False
try:
    from pyshorteners import Shortener
    pyshortenersinstalled = True
except:
    print("You don't have pyshorteners installed, installing it now...")
    try:
        check_output("pip3 install pyshorteners", shell=True)
        print("Pyshorteners installed succesfully!")
        import pyshorteners
        pyshortenersinstalled = True
    except:
        print("Pyshorteners didn't install succesfully.")
        pyshortenersinstalled = False

class Useful:
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
        em.set_image(url=avatar)
        await self.bot.say(embed=em)

    @commands.command(pass_context=True, name="calc", aliases=["calculate"])
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
            
    @commands.command(pass_context=True)
    @checks.mod_or_permissions()
    async def uploadcog(self, ctx, cogname):
        """Uploads a cog for you to use, for a list of cogs use [p]show_cogs"""
        await self.bot.say("Here you go:")
        await self.bot.send_file(ctx.message.channel, fp="cogs/{}.py".format(cogname), filename="{}.py".format(cogname))

    # copied from the owner cog since the command there was owner only and here it isn't :3
    @commands.command()
    @checks.mod_or_permissions()
    async def show_cogs(self):
        """Shows loaded/unloaded cogs"""
        loaded = [c.__module__.split(".")[1] for c in self.bot.cogs.values()]
        unloaded = [c.split(".")[1] for c in self._list_cogs()
                    if c.split(".")[1] not in loaded]
        if not unloaded:
            unloaded = ["None"]
        msg = ("+ Loaded\n{}\n\n- Unloaded\n{}".format(", ".join(sorted(loaded)), ", ".join(sorted(unloaded))))
        for page in pagify(msg, [" "], shorten_by=16):
            await self.bot.say(box(page.lstrip(" "), lang="diff"))

    @commands.command()
    async def discrim(self, discriminator: str):
        """Shows you all the members I can find with the discrim you gave."""
        discriminator = discriminator.replace("#", "")
        if not discriminator.isdigit():
            await self.bot.say("A Discrimnator can only have digits and a #\nExamples\n`#4157`, `4157`")
            return

        members = [str(s) for s in list(self.bot.get_all_members()) if s.discriminator == discriminator]
        members = ", ".join(list(set(members)))
        if not members:
            await self.bot.say("I could not find any users in any of the servers I'm in with a discriminator of `{}`".format(discriminator))
            return
        else:
            embed = discord.Embed(colour=0X00B6FF)
            embed.add_field(name="Discriminator #{}".format(discriminator), value=str(members), inline=False)
            try:
                await self.bot.say(embed=embed)
            except:
                await self.bot.say("An unknown error occured while embedding.")

    @commands.command()
    async def emoteurl(self, *, emote:discord.Emoji):
        """Gets the url for a CUSTOM emote (meaning no emotes like :eyes: and :ok_hand:)"""
        await self.bot.say(emote.url)

    @commands.command()
    async def showservers(self):
        """Shows you all the servers the bot is in."""
        servers = sorted(list(self.bot.servers), key=lambda s: s.name.lower())
        serversmsg = ""
        for i, server in enumerate(servers):
            serversmsg += "{}: {}\n".format(i+1, server.name)
        await self.bot.say("I am currently in\n" + serversmsg)

    @commands.command()
    async def milestones(self):
        """Shows you in how many servers the bot is."""
        stats = await self.bot.say("Getting stats, this may take a while.")
        edit_message = self.bot.edit_message
        uniquemembers = []
        servercount = len(self.bot.servers)
        channelcount = len(list(self.bot.get_all_channels()))
        membercount = len(list(self.bot.get_all_members()))
        for member in list(self.bot.get_all_members()):
            if member.name not in uniquemembers:
                uniquemembers.append(member.name)
        uniquemembercount = len(uniquemembers)
        statsmsg = "I am currently in **{}** servers with **{}** channels, **{}** members of which **{}** unique.".format(servercount, channelcount, membercount, uniquemembercount)
        await self.bot.edit_message(stats, statsmsg)
        # start of servercount milestones
        await asyncio.sleep(0.3)
        if servercount >= 10:
            statsmsg = statsmsg + "\n\n:white_check_mark: Reach 10 servers."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 10 servers."
        if servercount >= 50:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 50 servers."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 50 servers."
        if servercount >= 100:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 100 servers."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 100 servers."
        if servercount >= 500:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 500 servers."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 500 servers."
        if servercount >= 1000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 1000 servers."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 1000 servers."
        await self.bot.edit_message(stats, statsmsg)
        # start of channelcount milestones
        await asyncio.sleep(0.3)
        if channelcount >= 10:
            statsmsg = statsmsg + "\n\n:white_check_mark: Reach 10 channels."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 10 channels."
        if channelcount >= 50:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 50 channels."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 50 channels."
        if channelcount >= 100:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 100 channels."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 100 channels."
        if channelcount >= 500:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 500 channels."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 500 channels."
        if channelcount >= 1000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 1000 channels."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 1000 channels."
        await self.bot.edit_message(stats, statsmsg)
        # start of membercount milestones
        await asyncio.sleep(0.3)
        if membercount >= 1000:
            statsmsg = statsmsg + "\n\n:white_check_mark: Reach 1000 members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 1000 members."
        if membercount >= 5000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 5000 members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 5000 members."
        if membercount >= 10000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 10000 members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 10000 members."
        if membercount >= 50000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 50000 members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 50000 members."
        if membercount >= 100000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 100000 members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 100000 members.\n"
        await self.bot.edit_message(stats, statsmsg)
        # start of uniquemembercount milestones
        await asyncio.sleep(0.3)
        if uniquemembercount >= 1000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 1000 unique members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 1000 unique members."
        if uniquemembercount >= 5000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 5000 unique members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 5000 unique members."
        if uniquemembercount >= 10000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 10000 unique members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 10000 unique members."
        if uniquemembercount >= 50000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 50000 unique members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 50000 unique members."
        if uniquemembercount >= 100000:
            statsmsg = statsmsg + "\n:white_check_mark: Reach 100000 unique members."
        else:
            statsmsg = statsmsg + "\n:negative_squared_cross_mark: Reach 100000 unique members."
        await self.bot.edit_message(stats, statsmsg)
        
    @commands.command(pass_context=True)
    @commands.cooldown(5, 60)
    async def bugreport(self, ctx, *, bug:str):
        """Report a bug in the bot."""
        if settings.owner == "id_here":
            await self.bot.say("I have no owner set, cannot report the bug.")
            return
        owner = discord.utils.get(self.bot.get_all_members(), id=settings.owner)
        author = ctx.message.author
        if ctx.message.channel.is_private is False:
            server = ctx.message.server
            source = "server **{}** (`{}`)".format(server.name, server.id)
        else:
            source = "direct message"
        sender = "**{0}** (`{0.id}`) sent you a bug report from {1}:\n\n".format(author, source)
        message = sender + bug
        try:
            await self.bot.send_message(owner, message)
        except discord.errors.InvalidArgument:
            await self.bot.say("I cannot send your bug report, I'm unable to find my owner... *sigh*")
        except discord.errors.HTTPException:
            await self.bot.say("Your bug report is too long.")
        except:
            await self.bot.say("I'm unable to deliver your bug report. Sorry.")
        else:
            await self.bot.say("Your bug report has been sent.")

    @commands.command(pass_context=True)
    @commands.cooldown(5, 60)
    async def convert(self, ctx, file_url, *, output_format):
        """Convert a video or audio file to anything you like
        correct output formats would be mp4, mp3, wav, that kind of stuff.
        Correct outputs can also be png, jpg, gif all that stuff.
        
        You can also get a copy of Rick Astley - Never gonna give you up by doing [p]convert rickrolled rick astley
        You can also get a copy of LazyTown - We are number one by doing [p]convert lazytown number one"""
        convertmsg = await self.bot.say("Setting up...")
        # The copy of rickrolled part.
        if file_url == "rickrolled":
            file_url = "https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs-attributes/master/rickrolled.ogg"
            meme = True
            number = 'rickrolled_' + ''.join([choice('0123456789') for x in range(6)])
            if output_format == "rick astley":
                input_format = "ogg"
                output_format = "mp3"
        # The copy of We are number one part.
        elif file_url == "lazytown":
            meme = True
            file_url = "https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs-attributes/master/numberone.ogg"
            number = 'numberone_' + ''.join([choice('0123456789') for x in range(6)])
            if output_format == "number one":
                input_format = "ogg"
                output_format = "mp3"
        else:
            meme = False
            number = ''.join([choice('0123456789') for x in range(6)])
        if meme is False:
            form_found = False
            for i in range(6):
                if file_url[len(file_url) - i:].startswith("."):
                    input_format = file_url[len(file_url) - i:]
                    form_found = True
                else:
                    if form_found is not True:
                        form_found = False
            if form_found is not True:
                await bot.edit_message(convertmsg, "Your link is corrupt, it should end with something like .mp3, .mp4, .png, etc.")
                print(form_found)
                return
        input = "data/useful/{}.{}".format(number, input_format)
        output = "data/useful/{}.{}".format(number, output_format)
        outputname = "{}.{}".format(number, output_format)
        await self.bot.edit_message(convertmsg, "Downloading...")
        try:
            async with aiohttp.get(file_url) as r:
                file = await r.content.read()
            with open(input, 'wb') as f:
                f.write(file)
        except:
            await self.bot.edit_message(convertmsg, "Could not download the file.")
            try:
                os.remove(input)
            except:
                pass
            return
        try:
            converter = ffmpy.FFmpeg(inputs={input: "-y"}, outputs={output: "-y"})
            await self.bot.edit_message(convertmsg, "Converting...")
            converter.run()
        except:
            await self.bot.edit_message(convertmsg, "Could not convert your file, an error occured.")
            try:
                os.remove(input)
                os.remove(output)
            except:
                pass
            return
        await self.bot.send_file(ctx.message.channel, content="Convertion done!", fp=output, filename=outputname)
        await self.bot.delete_message(convertmsg)
        os.remove(input)
        os.remove(output)
        
    @commands.command(pass_context=True)
    @checks.mod_or_permissions()
    async def showservermembers(self, ctx):
        """Lists all the members of a server."""
        servers = sorted(list(self.bot.servers), key=lambda s: s.name.lower())
        msg = ""
        for i, server in enumerate(servers):
            msg += "{}: {}\n".format(i, server.name)
        msg += "\nTo show a servers members just type its number."
        for page in pagify(msg, ['\n']):
            await self.bot.say(page)
        while msg is not None:
            msg = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
            try:
                msg = int(msg.content)
                await self.show_confirmation(servers[msg], ctx.message.author, ctx)
                break
            except (IndexError, ValueError, AttributeError):
                pass

    async def show_confirmation(self, server, author, ctx):
        await self.bot.say("Are you sure you want to show {}'s members? (yes/no)".format(server.name))
        msg = await self.bot.wait_for_message(author=author, timeout=15)
        offline = []
        online = []
        offline_bot = []
        online_bot = []
        for member in server.members:
            if not member.bot:
                if member.status == discord.Status.offline:
                    offline.append(member.name)
                else:
                    online.append(member.name)
            else:
                if member.status == discord.Status.offline:
                    offline_bot.append(member.name)
                else:
                    online_bot.append(member.name)
        if not offline:
            offline = ["None"]
        if not online:
            online = ["None"]
        if not offline_bot:
            offline_bot = ["None"]
        if not online_bot:
            online_bot = ["None"]
        if msg is None:
            await self.bot.say("I guess not.")
        elif msg.content.lower() == "yes":
            msg = "**Online bots**:\n**{}**.\n\n**Offline bots**:\n**{}**.\n\n**Online members**:\n**{}**.\n\n**Offline members**\n**{}**.".format("**, **".join(sorted(online_bot)), "**, **".join(sorted(offline_bot)), "**, **".join(sorted(online)), "**, **".join(sorted(offline)))
            for page in pagify(msg, ['\n']):
                await self.bot.say(page)
        else:
            await self.bot.say("I guess not.")
            
    @commands.command(pass_context=True)
    @checks.mod_or_permissions()
    async def sendservermessage(self, ctx, *, message):
        """Lists all servers the bot is in and sends a message there."""
        servers = sorted(list(self.bot.servers), key=lambda s: s.name.lower())
        msg = ""
        for i, server in enumerate(servers):
            msg += "{}: {}\n".format(i, server.name)
        msg += "\nTo send this message to a server just type it's number."
        for page in pagify(msg, ['\n']):
            await self.bot.say(page)
        while msg is not None:
            msg = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
            try:
                msg = int(msg.content)
                await self.send_confirmation(servers[msg], ctx.message.author, ctx, message)
                break
            except (IndexError, ValueError, AttributeError):
                pass

    async def send_confirmation(self, server, author, ctx, message):
        await self.bot.say("Are you sure you want to send a message to {}? (yes/no)".format(server.name))
        msg = await self.bot.wait_for_message(author=author, timeout=15)
        if msg is None:
            await self.bot.say("I guess not.")
        elif msg.content.lower() == "yes":
            members = [member.name for member in server.members]
            await self.bot.send_message(server.default_channel, "{}, sent by {}.".format(message, str(author)))
            await self.bot.say("Message sent.")
        else:
            await self.bot.say("I guess not.")
            
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def serverwidemessage(self, ctx, *, msg):
        """Sends a message in every server."""
        for server in self.bot.servers:
            try:
                await self.bot.send_message(server.default_channel, "{}, sent by {}.".format(msg, str(ctx.message.author)))
            except:
                pass
        await self.bot.say("Done!")
        
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def serverwideembed(self, ctx, is_announcement, color, title, description, footer):
        """Sends an embedded message in every server."""
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
            for server in self.bot.servers:
                if is_announcement:
                    try:
                        await self.bot.send_message(server.default_channel, "@everyone @here, announcement!")
                    except:
                        pass
                await self.bot.send_message(server.default_channel, embed=em)
            return
        except discord.NotFound:
            await self.bot.say("Couldn't find the message to embed, did it get deleted?")
            return
        except discord.HTTPException:
            await self.bot.say("Hmm, an unknown error occured when embedding.")
            return
          
    @commands.command(pass_context=True)
    @checks.is_owner()
    async def serverwidetts(self, ctx, *, msg):
        """Sends a tts message in every server."""
        for server in self.bot.servers:
            await self.bot.say(tts=msg)
        await self.bot.say("Done!")
        
    @commands.command(pass_context=True)
    async def shorten(self, ctx, url):
        """Shorten a link."""
        shorten = Shortener('Bitly', bitly_token='dd800abec74d5b12906b754c630cdf1451aea9e0')
        await self.bot.say("{}, here you go <{}>.".format(ctx.message.author.mention, shorten.short(url)))
        
    @commands.command(pass_context=True)
    async def qrcode(self, ctx, url):
        """Creates a qrcode from a link."""
        shorten = Shortener('Bitly', bitly_token='dd800abec74d5b12906b754c630cdf1451aea9e0')
        short_link = shorten.short(url)
        async with aiohttp.get(shorten.qrcode(width=128, height=128)) as r:
            file = await r.content.read()
        number = random.randint(1000, 9999)
        fileloc = "data/useful/qrcode{}.png".format(number)
        with open(fileloc, 'wb') as f:
            f.write(file)
            file = None
            f = None
        await self.bot.send_file(ctx.message.channel, fp="data/useful/qrcode{}.png".format(number), filename="qrcode{}.png".format(number))
        os.remove("data/useful/qrcode{}.png".format(number))

    @commands.command(name="autopost")
    @checks.mod_or_permissions()
    async def _autopost(self, times:int, interval:float, *, msg):
        """Posts a message every set amount of minutes.
        The interval is in minutes."""
        time = 0
        while time < times:
            await self.bot.say(msg)
            time = time + 1
            await asyncio.sleep(interval * 60)
        
    def _list_cogs(self):
        cogs = [os.path.basename(f) for f in glob.glob("cogs/*.py")]
        return ["cogs." + os.path.splitext(f)[0] for f in cogs]
        
def check_folders():
    if not os.path.exists("data/useful"):
        print("Creating data/useful folder...")
        os.makedirs("data/useful")
        
class ModuleNotFound(Exception):
    pass
        
def setup(bot):
    if not ffmpyinstalled:
        raise ModuleNotFound("FFmpy is not installed, install it with pip3 install ffmpy.")
    if not pyshortenersinstalled:
        raise ModuleNotFound("Pyshorteners is not installed, install it with pip3 install pyshorteners.")
    check_folders()
    bot.add_cog(Useful(bot))