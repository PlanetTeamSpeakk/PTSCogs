from discord.ext import commands
from random import randint
from random import choice as choice
import random
import discord
import aiohttp
import os
from .utils.dataIO import dataIO
from .utils import checks

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
"http://i.imgur.com/ISuTCuL.gifv",
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
"http://i.imgur.com/aWsJTdC.gif"
]
        
class memes:
    """Dank memes."""

    def __init__(self, bot):
        self.bot = bot
        self.memelist = dataIO.load_json("data/memes/memes.json")
        
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        """Shows a random meme."""
        await self.bot.send_message(ctx.message.channel, choice(self.memelist))
        
    @commands.command(pass_context=True)
    async def addmeme(self, ctx, memelink_imgurpls):
        """Adds a meme to the global list of memes."""
        memelink = memelink_imgurpls
        if memelink.startswith("http://i.imgur.com/"):
            self.memelist.append(memelink + " by {}".format(ctx.message.author))
            dataIO.save_json("data/memes/memes.json", self.memelist)
            await self.bot.say("Meme added!")
        else:
            await self.bot.say("Memelink was not an imgur link, an example imgur link would be: <http://i.imgur.com/OyNz2uG.png>")
        
    @checks.mod_or_permissions()
    @commands.command()
    async def delmeme(self, memelink_and_owner):
        """Deletes a meme.
        
        Example:
        [p]delmeme "http://i.imgur.com/OyNz2uG.png by PlanetTeamSpeak#4157"
        """
        memelink = memelink_and_owner
        try:
            self.memelist.remove(memelink)
            dataIO.save_json("data/memes/memes.json", self.memelist)
            await self.bot.say("Meme removed!")
        except:
            await self.bot.say("Couldn't delete the meme from memes.json, was the format correct? A correct format would be \n\"http://i.imgur.com/OyNz2uG.png by PlanetTeamSpeak#4157\"")
		
    @commands.command()
    async def goodshit(self):
        """Good shit"""
        await self.bot.say("sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit\nhttps://www.youtube.com/watch?v=OYjv8ogsEGE&ab_channel=HeadStriker",)

    @commands.command()
    async def yesno(self):
        """Says yes or no."""
        self.yesno = ["yes. https://media.giphy.com/media/l46CabMtEkqUtrzkA/giphy.gif", "yes. https://media.giphy.com/media/l3vRhtXnCLgypqh7a/giphy.gif", "yes. https://media.giphy.com/media/l3vR3ACyHLgbOIjZe/source.gif", "no. https://media.giphy.com/media/3oz8xM4Qy4IVCelqZq/source.gif", "no. https://media.giphy.com/media/KaXENSCPjqnK0/giphy.gif", "no. https://media.giphy.com/media/T5QOxf0IRjzYQ/giphy.gif"]
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
        
    async def memes(self, message):
        if "ayy" in message.content.split():
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
            
        if "oh shit" in message.content.lower():
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
            
        if "o shit" in message.content.lower():
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
            
        if "feels bad man" in message.content.lower():
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
            
def check_folders():
    if not os.path.exists("data/memes"):
        print("Creating data/memes folder...")
        os.makedirs("data/memes")
        
def check_files():
    if not os.path.exists("data/memes/memes.json"):
        print("Creating data/memes/memes.json file...")
        dataIO.save_json("data/memes/memes.json", memelist)
        
def setup(bot):
    check_folders()
    check_files()
    n = memes(bot)
    bot.add_listener(n.memes, "on_message")
    bot.add_cog(n)