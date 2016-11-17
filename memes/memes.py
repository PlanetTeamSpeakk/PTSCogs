from discord.ext import commands
from random import randint
from random import choice as choice
import random
import discord
import asyncio

class memes:
    """Dank memes."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self):
        """Displays a random meme"""
        self.meme = ["http://i.imgur.com/yeF0kg4.jpg", "http://i.imgur.com/OyNz2uG.png", "https://media.giphy.com/media/3o6ZtjVtr71Zkiw9Lq/source.gif", "https://media.giphy.com/media/ZEVc9uplCUJFu/giphy.gif", "https://tenor.co/uX4C.gif", "https://media.giphy.com/media/2xV1VE0BIxKpy/giphy.gif", "https://tenor.co/v0Qz.gif", "http://i.imgur.com/dKTMitf.png", "https://media.giphy.com/media/FHCHRtwAZgGFq/giphy.gif", "https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif", "https://media.giphy.com/media/l0HlK8QU5ls1w0Jkk/giphy.gif", "https://i.ytimg.com/vi/P2lOpy2z7Cc/maxresdefault.jpg", "https://media.giphy.com/media/FxtRGakpKOa6Q/giphy.gif", "https://media.giphy.com/media/XQ9eJDq4kS1wI/giphy.gif", "https://media.giphy.com/media/26FPr0GKKPaPiUbbG/giphy.gif", "https://media.giphy.com/media/xT0BKiaM2VGJ553P9K/giphy.gif", "https://media.giphy.com/media/cguATjVdh3hzG/giphy.gif", "http://i.imgur.com/LkAIhqW.png", "https://media.giphy.com/media/10tN8bxISI1IZi/giphy.gif", "http://i.imgur.com/ISuTCuL.gifv", "https://cdn.discordapp.com/attachments/235041682440192008/235045049946079233/large.png", "https://cdn.discordapp.com/attachments/235041682440192008/235046843011039232/i-hate-it-when-jesus-rides-dinosaurs-in-my-house.png", "https://cdn.discordapp.com/attachments/235041682440192008/235054795491115008/why-is-this-potato-looking-at-me.png", "https://cdn.discordapp.com/attachments/235041682440192008/238661337750831105/dVj_RUK4.png", "https://cdn.discordapp.com/attachments/235041682440192008/235041717416361985/bruno_mars_dragging_a_piano.png"]
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
    async def fuckthisshit(self):
        """Fuck this shit I'm out."""
        sleep = asyncio.sleep
        await sleep(1.0)
        await self.bot.say("Fuck this shit I'm out.")
        await sleep(1.2)
        await self.bot.say("Mmmmmm Hmmmmm")
        await sleep(0.1)
        await self.bot.say("Fuck this shit I'm out.")
        await sleep(1.2)
        await self.bot.say("No thanks.")
        await sleep(0.1)
        await self.bot.say("Don't mind me.")
        await sleep(1.2)
        await self.bot.say("Imma just grab my stuff and leave.")
        await sleep(2.0)
        await self.bot.say("Excuse me please.")
        await sleep(1.1)
        await self.bot.say("Fuck this shit I'm out.")
        await sleep(1.2)
        await self.bot.say("NOPE!")
        await sleep(0.5)
        await self.bot.say("Fuck this shit I'm out.")
        await sleep(1.2)
        await self.bot.say("Alright then.")
        await sleep(0.5)
        await self.bot.say("I dunno know what the fck just happened.")
        await sleep(1.8)
        await self.bot.say("But I don't really care.")
        await sleep(1.2)
        await self.bot.say("Imma get the fuck up outta here.")
        await sleep(1.5)
        await self.bot.say("Fuck this shit I'm out.")
        await sleep(1.5)
        await self.bot.say("https://youtu.be/9wO5TnYaJ4o?t=53s")
     
    @commands.command()
    async def princeofbelair(self, user : discord.Member=None):
        sleep = asyncio.sleep
        say = self.bot.say
        if user == None:
            await say("https://www.youtube.com/watch?v=AVbQo3IOC_A")
            await sleep(3)
            await say("Now this is a story, all about how my life got flipped, turned upside down.")
            await sleep(4)
            await say("And I like to take minute just sit right there, I'll tell you how I became the price of a town called Bel Air.")
            await sleep(23)
            await say("In west Philadalphea born 'n raised, on the play ground where I spent most of my days.")
            await sleep(5)
            await say("Chillin' out, maxin' relaxin' and all cool and all shooting some bball outside of the school.")
            await sleep(5)
            await say("When a couple of guys said we were up to no good! Started making trouble in my neighborhood.")
            await sleep(4)
            await say("I got in one little fight and my mom got scared and said 'you're moving to your auntie and uncle in Bel Air'.")
            await sleep(5)
            await say("I begged and pleaded with her to have the day but she pack my suit-case and sent me on my way.")
            await sleep(4)
            await say("She gave me a kiss and she gave me my ticket, I put my walkman on and said 'I might as well kick it'.")
            await sleep(5)
            await say("First class, sho' this is bad, drinking orange juice outta a champange glass.")
            await sleep(5)
            await say("Is this what the people of Bel Air living like?")
            await sleep(2)
            await say("Hmm, this might be all right.")
            await sleep(2)
            await say("But wait I hear the prissy, booze, wine and all.")
            await sleep(3)
            await say("Is this the type of place they should send this cool-cat?")
            await sleep(2)
            await say("I don't think so, I'll see when I get there, I hope they're prepared for The Prince of Bel Air.")
            await sleep(22)
            await say("Well I, the plane landed and when I came out, there was a dude who looked like a cop standing there with my name out, I ain't trying to get arrested yet I just got here!")
            await sleep(8)
            await say("I sprang with the quickness the lightning disappeared.")
            await sleep(2)
            await say("I whistled for a cab, and when it came near, the license plate said fresh and had a dice in the mirror.")
            await sleep(6)
            await say("If anything I could say this cat was rare, but I thought 'man forget yet, yo homes the Bel Air'.")
            await sleep(13)
            await say("I pulled up to the house about 7 or 8 and I yelled to the cabbie 'yo homes smell ya later'.")
            await sleep(6)
            await say("Looked at my kingdom, I was finally here to sit on my throne as The Prince of Bel Air.")
        else:
            await say("https://www.youtube.com/watch?v=AVbQo3IOC_A")
            await sleep(3)
            await say("Now this is a story, all about how my life got flipped, turned upside down.")
            await sleep(4)
            await say("And I like to take minute just sit right there, I'll tell you how I became the price of a town called Bel Air.")
            await sleep(23)
            await say("In west Philadalphea born 'n raised, on the play ground where I spent most of my days.")
            await sleep(5)
            await say("Chillin' out, maxin' relaxin' and all cool and all shooting some bball outside of the school.")
            await sleep(5)
            await say("When a couple of guys said we were up to no good! Started making trouble in my neighborhood.")
            await sleep(4)
            await say("I got in one little fight and my mom got scared and said 'you're moving to your auntie and uncle in Bel Air'.")
            await sleep(5)
            await say("I begged and pleaded with her to have the day but she pack my suit-case and sent me on my way.")
            await sleep(4)
            await say("She gave me a kiss and she gave me my ticket, I put my walkman on and said 'I might as well kick it'.")
            await sleep(5)
            await say("First class, sho' this is bad, drinking orange juice outta a champange glass.")
            await sleep(5)
            await say("Is this what the people of Bel Air living like?")
            await sleep(2)
            await say("Hmm, this might be all right.")
            await sleep(2)
            await say("But wait I hear the prissy, booze, wine and all.")
            await sleep(3)
            await say("Is this the type of place they should send this cool-cat?")
            await sleep(2)
            await say("I don't think so, I'll see when I get there, I hope they're prepared for {}.".format(user.mention))
            await sleep(22)
            await say("Well I, the plane landed and when I came out, there was a dude who looked like a cop standing there with my name out, I ain't trying to get arrested yet I just got here!")
            await sleep(8)
            await say("I sprang with the quickness the lightning disappeared.")
            await sleep(2)
            await say("I whistled for a cab, and when it came near, the license plate said fresh and had a dice in the mirror.")
            await sleep(6)
            await say("If anything I could say this cat was rare, but I thought 'man forget yet, yo homes the Bel Air'.")
            await sleep(13)
            await say("I pulled up to the house about 7 or 8 and I yelled to the cabbie 'yo homes smell ya later'.")
            await sleep(6)
            await say("Looked at my kingdom, I was finally here to sit on my throne as {}.".format(user.mention))

def setup(bot):
    bot.add_cog(memes(bot))