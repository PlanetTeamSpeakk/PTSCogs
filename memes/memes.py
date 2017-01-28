from discord.ext import commands
from random import randint
from random import choice as choice
import random
import discord
import aiohttp
import os
import asyncio
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus-0.dll')
except OSError:
    opus = False
except:
    opus = None
else:
    opus = True

memelist = [
"http://i.imgur.com/yeF0kg4.jpg",
"http://i.imgur.com/OyNz2uG.png",
"http://i.imgur.com/E0NtqiR.gif",
"http://i.imgur.com/oUdWheT.gif",
"http://i.imgur.com/lTTGPTl.gif", 
"http://i.imgur.com/4SUPkgB.gif",
"http://i.imgur.com/oiBCuSk.gif",
"http://i.imgur.com/dKTMitf.png", 
"http://i.imgur.com/eVXxdPX.gif",
"http://i.imgur.com/FTgbH6V.gif",
"http://i.imgur.com/mKDz3CB.gif",
"http://i.imgur.com/ZkDEFVc.jpg",
"http://i.imgur.com/a2t7ilg.gif",
"http://i.imgur.com/1InP4XV.gif",
"http://i.imgur.com/9O9HPNh.gif",
"http://i.imgur.com/XIX8kag.gif",
"http://i.imgur.com/rkNFKdW.gif",
"http://i.imgur.com/LkAIhqW.png",
"http://i.imgur.com/2PjPLsK.gif",
"http://i.imgur.com/ISuTCuL.gif",
"http://i.imgur.com/rq4LLyx.png",
"http://i.imgur.com/zxHK2YJ.png",
"http://i.imgur.com/GQRxbPR.png",
"http://i.imgur.com/ynJWUjf.png",
"http://i.imgur.com/scnHxiW.png",
"http://i.imgur.com/VP4qJVp.png",
"http://i.imgur.com/H2QY5H8.gif",
"http://i.imgur.com/TFy8o7J.gif",
"http://i.imgur.com/a7oc0h4.gif",
"http://i.imgur.com/7AgiFiQ.gif",
"http://i.imgur.com/cIyXtKP.jpg",
"http://i.imgur.com/nrecDTy.jpg",
"http://i.imgur.com/w8vQAnI.jpg",
"http://i.imgur.com/JqCqC96.jpg",
"http://i.imgur.com/OrTu9dY.jpg",
"http://i.imgur.com/bbCjewo.jpg",
"http://i.imgur.com/aWsJTdC.gif",
"http://i.imgur.com/QOmWLWW.jpg",
"http://i.imgur.com/bV0FoPt.jpg",
"http://i.imgur.com/BkuCizz.jpg",
"http://i.imgur.com/EiYJueo.jpg",
"http://i.imgur.com/ge3lODN.jpg",
"http://i.imgur.com/jtOMMmu.jpg",
"http://i.imgur.com/pG2MNpN.png",
"http://i.imgur.com/1BP4XXS.png",
"http://i.imgur.com/L67XuUz.jpg",
"http://i.imgur.com/6Brq0mL.jpg",
"http://i.imgur.com/nlJiz4F.png",
"http://i.imgur.com/RCIZVlk.jpg",
"http://i.imgur.com/ZR3jJtN.png"
]
        
class Memes:
    """Dank memes."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/memes/settings.json")
        self.airhorn = [
        "data/memes/airhorns/airhorn1.mp3",
        "data/memes/airhorns/airhorn2.mp3",
        "data/memes/airhorns/airhorn3.mp3"
        ]
        self.yesno = [
        "yes. https://media.giphy.com/media/l46CabMtEkqUtrzkA/giphy.gif", 
        "yes. https://media.giphy.com/media/l3vRhtXnCLgypqh7a/giphy.gif", 
        "yes. https://media.giphy.com/media/l3vR3ACyHLgbOIjZe/source.gif", 
        "no. https://media.giphy.com/media/3oz8xM4Qy4IVCelqZq/source.gif", 
        "no. https://media.giphy.com/media/KaXENSCPjqnK0/giphy.gif", 
        "no. https://media.giphy.com/media/T5QOxf0IRjzYQ/giphy.gif"
        ]
        
    @commands.command(pass_context=True, no_pm=True)
    async def meme(self, ctx):
        """Shows a random meme."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'memes': memelist, 'disabled': False}
            self.save_settings()
        await self.bot.say(choice(self.settings[ctx.message.server.id]['memes']))
        
    @commands.command(pass_context=True, no_pm=True)
    async def addmeme(self, ctx, memelink_imgurpls):
        """Adds a meme to the list of memes of this server."""
        memelink = memelink_imgurpls
        if memelink.startswith("http://i.imgur.com/"):
            if ctx.message.server.id not in self.settings:
                self.settings[ctx.message.server.id] = {'memes': memelist, 'disabled': False}
            self.settings[ctx.message.server.id]['memes'].append(memelink + " by {}.".format(str(ctx.message.author)))
            self.save_settings()
            await self.bot.say("Meme added!")
        else:
            await self.bot.say("Memelink was not an imgur link, an example imgur link would be: <http://i.imgur.com/OyNz2uG.png>")
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions()
    async def delmeme(self, ctx, *, memelink):
        """Deletes a meme.
        
        Example:
        [p]delmeme http://i.imgur.com/OyNz2uG.png
        """
        if ctx.message.server.id not in self.settings:
            await self.bot.say("This server has no memes to delete.")
            return
        found = False
        for meme in self.settings[ctx.message.server.id]['memes']:
            if memelink in meme:
                found = True
                memelink = meme
        if not found:
            await self.bot.say("That's not a valid meme.")
        else:
            self.settings[ctx.message.server.id]['memes'].remove(memelink)
            self.save_settings()
            await self.bot.say("Meme removed!")
		
    @commands.command()
    async def goodshit(self):
        """Good shit"""
        await self.bot.say("sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit\nhttps://www.youtube.com/watch?v=OYjv8ogsEGE&ab_channel=HeadStriker",)

    @commands.command(name="yesno")
    async def _yesno(self):
        """Says yes or no."""
        await self.bot.say("I say " + choice(self.yesno))
        
    @commands.command(pass_context=True)
    async def datboi(self, ctx):
        """Here come dat boi,
        
        Oh shit waddup"""
        await self.bot.say("Here come dat boi.")
        ohshit = await self.bot.say("Oh shit")
        W = "\U0001f1fc"
        A = "\U0001f1e6"
        D = "\U0001f1e9"
        U = "\U0001f1fa"
        P = "\U0001f1f5"
        await self.bot.add_reaction(ohshit, W)
        await self.bot.add_reaction(ohshit, A)
        await self.bot.add_reaction(ohshit, D)
        await self.bot.add_reaction(ohshit, U)
        await self.bot.add_reaction(ohshit, P)
        self.datboiLoaded = os.path.exists('data/memes/datboi.png')
        if not self.datboiLoaded:
            try:
                async with aiohttp.get("http://i.imgur.com/KEb9OJv.jpg") as r:
                    image = await r.content.read()
                with open('data/memes/datboi.png', 'wb') as f:
                    f.write(image)
            except Exception as e:
                print(e)
                print("Memes error D: I couldn't download the file, so we're gonna use the url instead.")
            await self.bot.send_file(ctx.message.channel, fp="data/memes/datboi.png", filename="datboi.png")
        else:
            await self.bot.send_file(ctx.message.channel, fp="data/memes/datboi.png", filename="datboi.png")
            
    @commands.command(pass_context=True, name="airhorn", no_pm=True)
    async def _airhorn(self, ctx):
        """Plays an airhorn in the voice channel you're in."""
        self.ah1Loaded = os.path.exists('data/memes/airhorns/airhorn1.mp3')
        self.ah2Loaded = os.path.exists('data/memes/airhorns/airhorn2.mp3')
        self.ah3Loaded = os.path.exists('data/memes/airhorns/airhorn3.mp3')
        if not self.ah1Loaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhorns/airhorn1.mp3") as r:
                    ah1 = await r.content.read()
                with open('data/memes/airhorns/airhorn1.mp3', 'wb') as f:
                    f.write(ah1)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the airhorn sounds, I suggest disabling the airhorn command.")
                return
        if not self.ah2Loaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhorns/airhorn2.mp3") as r:
                    ah1 = await r.content.read()
                with open('data/memes/airhorns/airhorn2.mp3', 'wb') as f:
                    f.write(ah1)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the airhorn sounds, I suggest disabling the airhorn command.")
                return
        if not self.ah3Loaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhorns/airhorn3.mp3") as r:
                    ah1 = await r.content.read()
                with open('data/memes/airhorns/airhorn3.mp3', 'wb') as f:
                    f.write(ah1)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the airhorn sounds, I suggest disabling the airhorn command.")
                await self.bot.say("Couldn't download the airhorn sounds, I suggest disabling the airhorn command.")
                return
        if not ctx.message.author.voice_channel:
            await self.bot.say("You're not in a voice channel, how am I supposed to play you an airhorn if you're not in a voice channel?")
            return
        elif ctx.message.author.self_deaf:
            await self.bot.say("You're deafened, I am not gonna play an airhorn to annoy everyone in the voice channel but you.")
            return
        elif ctx.message.author.deaf:
            await self.bot.say("You're deafened, I am not gonna play an airhorn to annoy everyone in the voice channel but you. Maybe ask a moderator to undeafen you?")
            return
        server = ctx.message.server
        if self.bot.is_voice_connected(server):
            try:
                airhornchoice = choice(self.airhorn)
                vcdc = self.bot.voice_client_in(server)
                await vcdc.disconnect()
                await asyncio.sleep(0.5)
                airhorn_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                airhorn = airhorn_join.create_ffmpeg_player(airhornchoice)
                airhorn.start()
                ahplaying = True
                if airhornchoice == "data/memes/airhorns/airhorn1.mp3":
                    await asyncio.sleep(1.75)
                elif airhornchoice == "data/memes/airhorns/airhorn2.mp3":
                    await asyncio.sleep(1.5)
                else:
                    await asyncio.sleep(3)
                vcdc = self.bot.voice_client_in(server)
                await vcdc.disconnect()
                ahplaying = False
                return
            except:
                return
        else:
            try:
                airhornchoice = choice(self.airhorn)
                airhorn_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                airhorn = airhorn_join.create_ffmpeg_player(airhornchoice)
                airhorn.start()
                if airhornchoice == "data/memes/airhorns/airhorn1.mp3":
                    await asyncio.sleep(1.75)
                elif airhornchoice == "data/memes/airhorns/airhorn2.mp3":
                    await asyncio.sleep(1.5)
                else:
                    await asyncio.sleep(3)
                vcdc = self.bot.voice_client_in(server)
                await vcdc.disconnect()
                return
            except:
                return
                
    @commands.group(name="airhornsong", pass_context=True, no_pm=True)
    async def _airhornsong(self, ctx):
        """Some air horn songs."""
        if not ctx.invoked_subcommand:
            await send_cmd_help(ctx)
            
    @_airhornsong.command(no_pm=True)
    async def credits(self):
        """Some credits to the song makers."""
        await self.bot.say("All songs are made by Cyranek \n<https://www.youtube.com/channel/UCMYTaTc_gVRyGF6LWzdIsqA>")
        
    @_airhornsong.command(no_pm=True)
    async def list(self):
        """Shows you the current list of airhorn songs."""
        await self.bot.say("You can currently choose from:\nletitgo\nturndownforwhat\ndarudesandstorm\nsonic")
            
    @_airhornsong.command(pass_context=True, no_pm=True)
    async def letitgo(self, ctx):
        """Plays let it go airhorn version."""
        self.letitgoLoaded = os.path.exists("data/memes/airhornsongs/letitgo.mp3")
        if not self.letitgoLoaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhornsongs/letitgo.mp3") as r:
                    letitgo = await r.content.read()
                with open('data/memes/airhornsongs/letitgo.mp3', 'wb') as f:
                    f.write(letitgo)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the letitgo airhorn song, I suggest disabling the airhornsong command.")
                return
        server = ctx.message.server
        if ctx.message.author.voice_channel:
            if self.bot.is_voice_connected(server):
                try:
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    await asyncio.sleep(0.5)
                    letitgo_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    letitgo = letitgo_join.create_ffmpeg_player("data/memes/airhornsongs/letitgo.mp3")
                    letitgo.start()
                    await asyncio.sleep(218)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
            else:
                try:
                    letitgo_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    letitgo = letitgo_join.create_ffmpeg_player("data/memes/airhornsongs/letitgo.mp3")
                    letitgo.start()
                    await asyncio.sleep(218)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
        else:
            await self.bot.say("You're not in a voice channel.")
            return
                
    @_airhornsong.command(pass_context=True, no_pm=True)
    async def turndownforwhat(self, ctx):
        """Plays the turn down for what song airhorn version."""
        self.turndownforwhatLoaded = os.path.exists("data/memes/airhornsongs/turndownforwhat.mp3")
        if not self.turndownforwhatLoaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhornsongs/turndownforwhat.mp3") as r:
                    turndownforwhat = await r.content.read()
                with open('data/memes/airhornsongs/turndownforwhat.mp3', 'wb') as f:
                    f.write(turndownforwhat)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the turndownforwhat airhorn song, I suggest disabling the airhornsong command.")
                return
        server = ctx.message.server
        if ctx.message.author.voice_channel:
            if self.bot.is_voice_connected(server):
                try:
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    await asyncio.sleep(0.5)
                    turndownforwhat_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    turndownforwhat = turndownforwhat_join.create_ffmpeg_player("data/memes/airhornsongs/turndownforwhat.mp3")
                    turndownforwhat.start()
                    await asyncio.sleep(192)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
            else:
                try:
                    turndownforwhat_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    turndownforwhat = turndownforwhat_join.create_ffmpeg_player("data/memes/airhornsongs/turndownforwhat.mp3")
                    turndownforwhat.start()
                    await asyncio.sleep(192)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
        else:
            await self.bot.say("You're not in a voice channel.")
            return
                
    @_airhornsong.command(pass_context=True, no_pm=True)
    async def darudesandstorm(self, ctx):
        """Plays the darude sandstorm song airhorn version."""
        self.darudesandstormLoaded = os.path.exists("data/memes/airhornsongs/darudesandstorm.mp3")
        if not self.darudesandstormLoaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhornsongs/darudesandstorm.mp3") as r:
                    darudesandstorm = await r.content.read()
                with open('data/memes/airhornsongs/darudesandstorm.mp3', 'wb') as f:
                    f.write(darudesandstorm)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the darudesandstorm airhorn song, I suggest disabling the airhornsong command.")
                return
        server = ctx.message.server
        if ctx.message.author.voice_channel:
            if self.bot.is_voice_connected(server):
                try:
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    await asyncio.sleep(0.5)
                    darudesandstorm_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    darudesandstorm = darudesandstorm_join.create_ffmpeg_player("data/memes/airhornsongs/darudesandstorm.mp3")
                    darudesandstorm.start()
                    await asyncio.sleep(89)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
            else:
                try:
                    darudesandstorm_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    darudesandstorm = darudesandstorm_join.create_ffmpeg_player("data/memes/airhornsongs/darudesandstorm.mp3")
                    darudesandstorm.start()
                    await asyncio.sleep(89)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
        else:
            await self.bot.say("You're not in a voice channel.")
            return
                
    @_airhornsong.command(pass_context=True, no_pm=True)
    async def sonic(self, ctx):
        """Plays sonic song airhorn version."""
        self.sonicLoaded = os.path.exists("data/memes/airhornsongs/sonic.mp3")
        if not self.sonicLoaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/airhornsongs/sonic.mp3") as r:
                    sonic = await r.content.read()
                with open('data/memes/airhornsongs/sonic.mp3', 'wb') as f:
                    f.write(sonic)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the sonic airhorn song, I suggest disabling the airhornsong command.")
                return
        server = ctx.message.server
        if ctx.message.author.voice_channel:
            if self.bot.is_voice_connected(server):
                try:
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    await asyncio.sleep(0.5)
                    sonic_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    sonic = sonic_join.create_ffmpeg_player("data/memes/airhornsongs/sonic.mp3")
                    sonic.start()
                    await asyncio.sleep(80)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
            else:
                try:
                    sonic_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    sonic = sonic_join.create_ffmpeg_player("data/memes/airhornsongs/sonic.mp3")
                    sonic.start()
                    await asyncio.sleep(80)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
        else:
            await self.bot.say("You're not in a voice channel.")
            return
            
    @commands.command(pass_context=True, no_pm=True)
    async def sadpiano(self, ctx):
        """Plays sad piano for you."""
        self.sadpianoLoaded = os.path.exists("data/memes/sadpiano.mp3")
        if not self.sadpianoLoaded:
            try:
                async with aiohttp.get("https://raw.githubusercontent.com/PlanetTeamSpeakk/PTSCogs/master/sadpiano.mp3") as r:
                    sadpiano = await r.content.read()
                with open('data/memes/sadpiano.mp3', 'wb') as f:
                    f.write(sadpiano)
            except Exception as e:
                print(e)
                print("Memes error, couldn't download the sad piano song, I suggest disabling the airhornsong command.")
                return
        server = ctx.message.server
        if ctx.message.author.voice_channel:
            if self.bot.is_voice_connected(server):
                try:
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    await asyncio.sleep(0.5)
                    sadpiano_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    sadpiano = sadpiano_join.create_ffmpeg_player("data/memes/sadpiano.mp3")
                    sadpiano.start()
                    await asyncio.sleep(252)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
            else:
                try:
                    sadpiano_join = await self.bot.join_voice_channel(ctx.message.author.voice_channel)
                    sadpiano = sadpiano_join.create_ffmpeg_player("data/memes/sadpiano.mp3")
                    sadpiano.start()
                    await asyncio.sleep(252)
                    vcdc = self.bot.voice_client_in(server)
                    await vcdc.disconnect()
                    return
                except:
                    return
        else:
            await self.bot.say("You're not in a voice channel.")
            return
            
    @commands.command(hidden=True)
    async def spoopy(self):
        await self.bot.say("This command will never show up in help, now isn't that weird?")
        
    @commands.command()
    async def banned(self, user:discord.Member=None):
        """Tells someone they're banned."""
        if user != None:
            await self.bot.say("{} http://i.imgur.com/HQGh7tL.gif".format(user.mention))
        else:
            await self.bot.say("http://i.imgur.com/HQGh7tL.gif")
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.mod_or_permissions()
    async def togglereactions(self, ctx):
        """Disables reactions like "ayy" and "oh shit\""""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'memes': memelist, 'disabled': False}
        if not self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = True
            await self.bot.say("Bot will no longer respond to \"ayy\" and \"oh shit\".")
        else:
            self.settings[ctx.message.server.id]['disabled'] = False
            await self.bot.say("Bot will once again respond to \"ayy\" and \"oh shit\".")
        self.save_settings()
        
    async def memes(self, message):
        if message.server != None:
            if not "bots" in message.server.name.lower():
                if message.server.id not in self.settings:
                    self.settings[message.server.id] = {'memes': memelist, 'disabled': False}
                    self.save_settings()
                if not (self.settings[message.server.id]['disabled']) and ("ayy" in message.content.lower()):
                    self.lmaoLoaded = os.path.exists('data/memes/maolmao.png')
                    if not self.lmaoLoaded:
                        try:
                            async with aiohttp.get("http://i.imgur.com/yfkKXGQ.png") as r:
                                image = await r.content.read()
                            with open('data/memes/maolmao.png','wb') as f:
                                f.write(image)
                            L = "\U0001f1f1"
                            M = "\U0001f1f2"
                            A = "\U0001f1e6"
                            O = "\U0001f1f4"
                            await self.bot.send_file(message.channel, fp="data/memes/maolmao.png", filename="maolmao.png")
                            await self.bot.add_reaction(message, L)
                            await self.bot.add_reaction(message, M)
                            await self.bot.add_reaction(message, A)
                            await self.bot.add_reaction(message, O)
                            
                        except Exception as e:
                            print(e)
                            print("Memes error D: I couldn't download the file, so we're gonna use the url instead.")
                            L = "\U0001f1f1"
                            M = "\U0001f1f2"
                            A = "\U0001f1e6"
                            O = "\U0001f1f4"
                            await self.bot.send_message(message.channel, "http://i.imgur.com/yfkKXGQ.png")
                            await self.bot.add_reaction(message, L)
                            await self.bot.add_reaction(message, M)
                            await self.bot.add_reaction(message, A)
                            await self.bot.add_reaction(message, O)
                    else:
                        L = "\U0001f1f1"
                        M = "\U0001f1f2"
                        A = "\U0001f1e6"
                        O = "\U0001f1f4"
                        await self.bot.send_file(message.channel, fp="data/memes/maolmao.png", filename="maolmao.png")
                        await self.bot.add_reaction(message, L)
                        await self.bot.add_reaction(message, M)
                        await self.bot.add_reaction(message, A)
                        await self.bot.add_reaction(message, O)       
                    
                if message.content.lower() == "oh shit":
                    W = "\U0001f1fc"
                    A = "\U0001f1e6"
                    D = "\U0001f1e9"
                    U = "\U0001f1fa"
                    P = "\U0001f1f5"
                    await self.bot.add_reaction(message, W)
                    await self.bot.add_reaction(message, A)
                    await self.bot.add_reaction(message, D)
                    await self.bot.add_reaction(message, U)
                    await self.bot.add_reaction(message, P)
                    
                if message.content.lower() == "o shit":
                    W = "\U0001f1fc"
                    A = "\U0001f1e6"
                    D = "\U0001f1e9"
                    U = "\U0001f1fa"
                    P = "\U0001f1f5"
                    await self.bot.add_reaction(message, W)
                    await self.bot.add_reaction(message, A)
                    await self.bot.add_reaction(message, D)
                    await self.bot.add_reaction(message, U)
                    await self.bot.add_reaction(message, P)
                    
                if (message.content.lower() == "feels bad man") or (message.content.lower() == "feelsbadman"):
                    self.fbmLoaded = os.path.exists('data/memes/feelsbadman.png')
                    if not self.fbmLoaded:
                        try:
                            async with aiohttp.get("http://i.imgur.com/U26pQQo.png") as r:
                                image = await r.content.read()
                            with open('data/memes/feelsbadman.png','wb') as f:
                                f.write(image)
                            await self.bot.send_file(message.channel, fp="data/memes/feelsbadman.png", filename="feelsbadman.png")
                        except Exception as e:
                            print(e)
                            print("Memes error D: I couldn't download the file, so we're gonna use the url instead.")
                            await self.bot.send_message(message.channel, "http://i.imgur.com/U26pQQo.png")
                    else:
                        await self.bot.send_file(message.channel, fp="data/memes/feelsbadman.png", filename="feelsbadman.png")
            
    def save_settings(self):
        dataIO.save_json("data/memes/settings.json", self.settings)
            
def check_folders():
    if not os.path.exists("data/memes"):
        print("Creating data/memes folder...")
        os.makedirs("data/memes")
    if not os.path.exists("data/memes/airhorns"):
        print("Creating data/memes/airhorns folder...")
        os.makedirs("data/memes/airhorns")
    if not os.path.exists("data/memes/airhornsongs"):
        print("Creating data/memes/airhornsongs folder...")
        os.makedirs("data/memes/airhornsongs")
        
def check_files():
    if not os.path.exists("data/memes/settings.json"):
        print("Creating data/memes/settings.json file...")
        dataIO.save_json("data/memes/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    n = Memes(bot)
    bot.add_listener(n.memes, "on_message")
    bot.add_cog(n)