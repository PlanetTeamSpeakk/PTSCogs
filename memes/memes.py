from discord.ext import commands
from random import randint
from random import choice as choice
import random
import discord

class memes:
    """Dank memes."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self):
        """Displays a random meme"""
        self.meme = ["http://i.imgur.com/yeF0kg4.jpg", 
        "http://i.imgur.com/OyNz2uG.png", 
        "https://media.giphy.com/media/3o6ZtjVtr71Zkiw9Lq/source.gif", 
        "https://media.giphy.com/media/ZEVc9uplCUJFu/giphy.gif", 
        "https://tenor.co/uX4C.gif", 
        "https://media.giphy.com/media/2xV1VE0BIxKpy/giphy.gif", 
        "https://tenor.co/v0Qz.gif", "http://i.imgur.com/dKTMitf.png", 
        "https://media.giphy.com/media/FHCHRtwAZgGFq/giphy.gif", 
        "https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif", 
        "https://media.giphy.com/media/l0HlK8QU5ls1w0Jkk/giphy.gif", 
        "https://i.ytimg.com/vi/P2lOpy2z7Cc/maxresdefault.jpg", 
        "https://media.giphy.com/media/FxtRGakpKOa6Q/giphy.gif", 
        "https://media.giphy.com/media/XQ9eJDq4kS1wI/giphy.gif", 
        "https://media.giphy.com/media/26FPr0GKKPaPiUbbG/giphy.gif", 
        "https://media.giphy.com/media/xT0BKiaM2VGJ553P9K/giphy.gif", 
        "https://media.giphy.com/media/cguATjVdh3hzG/giphy.gif", 
        "http://i.imgur.com/LkAIhqW.png", 
        "https://media.giphy.com/media/10tN8bxISI1IZi/giphy.gif", 
        "http://i.imgur.com/ISuTCuL.gifv", 
        "https://cdn.discordapp.com/attachments/235041682440192008/235045049946079233/large.png", 
        "https://cdn.discordapp.com/attachments/235041682440192008/235046843011039232/i-hate-it-when-jesus-rides-dinosaurs-in-my-house.png", 
        "https://cdn.discordapp.com/attachments/235041682440192008/235054795491115008/why-is-this-potato-looking-at-me.png", 
        "https://cdn.discordapp.com/attachments/235041682440192008/238661337750831105/dVj_RUK4.png", 
        "https://cdn.discordapp.com/attachments/235041682440192008/235041717416361985/bruno_mars_dragging_a_piano.png",
        "http://i.imgur.com/VP4qJVp.png",
        "https://media.giphy.com/media/U7P2vnWfPkIQ8/giphy.gif",
        "https://media.giphy.com/media/ehc19YLR4Ptbq/giphy.gif",
        "https://media.giphy.com/media/ydBBZCByqY9xu/giphy.gif",
        "https://media.giphy.com/media/y0yGfn4JsQCGY/giphy.gif",
        "https://i.reddituploads.com/a8aceb3701214e71a605719845485002?fit=max&h=1536&w=1536&s=9162f07c6f6046befdb915d50b7b55cd",
        "https://i.reddituploads.com/36c84863444c44c99a8607620899d874?fit=max&h=1536&w=1536&s=d48ae5fc1ab29be9446ef10b641a0438",
        "https://i.reddituploads.com/7f94d6bd73eb428283a3233ac3a3b6c2?fit=max&h=1536&w=1536&s=a42e5cd7915370a30acf678859fb6a98",
        "https://i.reddituploads.com/629cfb252d1144c3abb0f413f5ddedb3?fit=max&h=1536&w=1536&s=c8bd1ff11b7480167427452c801375ed",
        "https://i.reddituploads.com/0ac3a6f96ff5433bab726729a0cb1123?fit=max&h=1536&w=1536&s=6d3bcc9dc2ad96268923f5eb39aee1f7",
        "https://i.reddituploads.com/30ba3cc5cebc4a338eefe062adda8f74?fit=max&h=1536&w=1536&s=29e2714e2ed1ecb183402ab69503382a",]
        await self.bot.say(choice(self.meme))
		
    @commands.command()
    async def goodshit(self):
        """Good shit"""
        await self.bot.say("sign me the FUCK up :ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes::ok_hand::eyes: good shit go౦ԁ sHit:ok_hand: thats :heavy_check_mark: some good:ok_hand::ok_hand:shit right:ok_hand::ok_hand:there:ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit\nhttps://www.youtube.com/watch?v=OYjv8ogsEGE&ab_channel=HeadStriker",)

    @commands.command()
    async def yesno(self):
        """Displays an anonymous random fuck off message for items."""
        self.yesno = ["yes. https://media.giphy.com/media/l46CabMtEkqUtrzkA/giphy.gif", "yes. https://media.giphy.com/media/l3vRhtXnCLgypqh7a/giphy.gif", "yes. https://media.giphy.com/media/l3vR3ACyHLgbOIjZe/source.gif", "no. https://media.giphy.com/media/3oz8xM4Qy4IVCelqZq/source.gif", "no. https://media.giphy.com/media/KaXENSCPjqnK0/giphy.gif", "no. https://media.giphy.com/media/T5QOxf0IRjzYQ/giphy.gif"]
        await self.bot.say("I say " + choice(self.yesno))
        
    @commands.command()
    async def datboi(self):
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
        await self.bot.say("http://i1.kym-cdn.com/photos/images/newsfeed/001/112/704/8a8.jpg")
        
    async def on_message(self, message):
        if "ayy" in message.content.split():
            L = "\U0001f1f1"
            M = "\U0001f1f2"
            A = "\U0001f1e6"
            O = "\U0001f1f4"
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
            
def setup(bot):
    bot.add_cog(memes(bot))