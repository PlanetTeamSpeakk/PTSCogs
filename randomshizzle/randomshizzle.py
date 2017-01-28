from discord.ext import commands
from __main__ import send_cmd_help, settings
import discord
import asyncio
from random import choice
import random
from cogs.utils.dataIO import dataIO
import os

class Randomshizzle:
    """Random shizzle."""

    def __init__(self, bot):
        self.bot = bot
        self.pressfcount = dataIO.load_json("data/pressf/pressf.json")
        
    @commands.command()
    async def cooldog(self):
        await self.bot.say("╭━━━━╮               This is cooldog. Help \n╰┃ ┣▇━▇                cooldog take over \n ┃ ┃  ╰━▅╮ Discord by pasting\n ╰┳╯ ╰━━┳╯        him in 10 other\n  ╰╮ ┳━━╯            servers or you\n ▕▔▋ ╰╮╭━╮   will never be a cool dog.\n╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱")

    @commands.command()
    async def soundsfromspace(self):
        await self.bot.say("Ooh, spooky. \n<https://github.audio/>")

    @commands.command(pass_context=True)
    async def flipuser(self, ctx, user : discord.Member):
        """Flips a user."""
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
			
    @commands.command(pass_context=True)
    async def flipitem(self, ctx, item):
        """Flips a item."""
        msg = ""
        char = "abcdefghijklmnopqrstuvwxyz"
        tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
        table = str.maketrans(char, tran)
        name = item.translate(table)
        char = char.upper()
        tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
        table = str.maketrans(char, tran)
        name = name.translate(table)
        await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
			
    @commands.command()
    async def punch(self, user : discord.Member):
        """I'll punch everyone!"""
        await self.bot.say("*Punches " + user.mention + "* \nGet punched, SON!")
		
    @commands.command()
    async def ipunch(self, *, item):
        """I'll punch anything!"""
        await self.bot.say("*Punches " + item + "* \nGet punched, SON!")
        
    @commands.command()
    async def triggered(self):
        """TRIGGERED"""
        await self.bot.say("***__TRIGGERED__***\nhttps://media.giphy.com/media/ZEVc9uplCUJFu/giphy.gif")

    @commands.command(pass_context=True)
    async def kys(self, ctx, user : discord.Member = None):
        """kill yourself"""
        if user != None and user.id == self.bot.user.id:
            await self.bot.say("You think this is funny?\nHow about *this* instead.")
            await self.bot.say(ctx.message.author.mention +
            "\n( ͡° ͜ʖ ͡°)               ( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)              ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)          ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)      ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)                                   ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                              ( ͡° ͜ʖ ͡°)                      ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                            ( ͡° ͜ʖ ͡°)                                        ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)                  ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                     ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)")
        elif user != None and user.id == ctx.message.author.id:
            await self.bot.say("You wanna kys?")
            return
        elif user != None and user.id != self.bot.user.id:
            await self.bot.say(user.mention +
            "\n( ͡° ͜ʖ ͡°)               ( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)              ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)          ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)      ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)                                   ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                              ( ͡° ͜ʖ ͡°)                      ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                            ( ͡° ͜ʖ ͡°)                                        ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)                  ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                     ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)")
        elif user == None:
            await self.bot.say(""
            "( ͡° ͜ʖ ͡°)               ( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)              ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)          ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)      ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)                                   ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                              ( ͡° ͜ʖ ͡°)                      ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                            ( ͡° ͜ʖ ͡°)                                        ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)                  ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)"
            "\n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                     ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def rainbow(self, times:int, interval:float):
        """Make a happy rainbow!"""
        rainbow = await self.bot.say(embed=discord.Embed(title="Rainbow!", color=discord.Color.red()))
        time = 0
        error = 0
        if interval < 1.4:
            interval = 1.5
        while times > time:
            time = time + 1
            color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            try:
                await self.bot.edit_message(rainbow, embed=discord.Embed(title="Rainbow!", color=discord.Color(value=color)))
            except:
                if error < 1:
                    await self.bot.say("An error occured, trying again.")
                    error = error + 1
                else:
                    await self.bot.say("Another error occured, exiting.")
                    return
            await asyncio.sleep(interval)
            
    @commands.command()
    async def sombra(self):
        """Sombra."""
        await self.bot.say("```fix\n"
        "                       :PB@Bk:                         \n"
        "                   ,jB@@B@B@B@BBL.                     \n"
        "                7G@B@B@BMMMMMB@B@B@Nr                  \n"
        "            :kB@B@@@MMOMOMOMOMMMM@B@B@B1,              \n"
        "        :5@B@B@B@BBMMOMOMOMOMOMOMM@@@B@B@BBu.          \n"
        "     70@@@B@B@B@BXBBOMOMOMOMOMOMMBMPB@B@B@B@B@Nr       \n"
        "   G@@@BJ iB@B@@  OBMOMOMOMOMOMOM@2  B@B@B. EB@B@S     \n"
        "   @@BM@GJBU.  iSuB@OMOMOMOMOMOMM@OU1:  .kBLM@M@B@     \n"
        "   B@MMB@B       7@BBMMOMOMOMOMOBB@:       B@BMM@B     \n"
        "   @@@B@B         7@@@MMOMOMOMM@B@:         @@B@B@     \n"
        "   @@OLB.          BNB@MMOMOMM@BEB          rBjM@B     \n"
        "   @@  @           M  OBOMOMM@q  M          .@  @@     \n"
        "   @@OvB           B:u@MMOMOMMBJiB          .BvM@B     \n"
        "   @B@B@J         0@B@MMOMOMOMB@B@u         q@@@B@     \n"
        "   B@MBB@v       G@@BMMMMMMMMMMMBB@5       F@BMM@B     \n"
        "   @BBM@BPNi   LMEB@OMMMM@B@MMOMM@BZM7   rEqB@MBB@     \n"
        "   B@@@BM  B@B@B  qBMOMB@B@B@BMOMBL  B@B@B  @B@B@M     \n"
        "    J@@@@PB@B@B@B7G@OMBB.   ,@MMM@qLB@B@@@BqB@BBv      \n"
        "       iGB@,i0@M@B@MMO@E  :  M@OMM@@@B@Pii@@N:         \n"
        "          .   B@M@B@MMM@B@B@B@MMM@@@M@B                \n"
        "              @B@B.i@MBB@B@B@@BM@::B@B@                \n"
        "              B@@@ .B@B.:@B@ :B@B  @B@O                \n"
        "                :0 r@B@  B@@ .@B@: P:                  \n"
        "                    vMB :@B@ :BO7                      \n"
        "                        ,B@B                        ```\n")
        
    @commands.command()
    async def apologize(self):
        """Let the bot apologize"""
        await self.bot.say(":regional_indicator_n: :regional_indicator_o: :regional_indicator_p: :regional_indicator_e:")
        
    @commands.command(pass_context=True)
    async def colorrole(self, ctx, color):
        """Creates a colored role for you!
        
        Example
        [p]colorrole #8C5200
        Hex pls."""
        if not color.startswith("#"):
            await send_cmd_help(ctx)
            return
        colorhex = color[1:]
        color_role = await self.bot.create_role(server=ctx.message.server, name=color, colour=discord.Colour(value=int(colorhex, 16)))
        await self.bot.add_roles(ctx.message.author, color_role)
        await self.bot.say("Done!")

    @commands.command()
    async def pressf(self, times:int=1):
        """Pay your respect!"""
        if times > 4:
            await self.bot.say("Wow not higher than 4")
            return
        self.pressfcount.append(int(self.pressfcount[0]) + int(times))
        self.pressfcount.remove(self.pressfcount[0])
        dataIO.save_json("data/pressf/pressf.json", self.pressfcount)
        await self.bot.say("Respects paid: {}.".format(self.pressfcount[0]))

    @commands.command(name="pressfcount", pass_context=True)
    async def _pressfcount(self, ctx):
        """Tells you how much people paid their respect."""
        await self.bot.say("Currently {} people paid their respect using {}pressf!".format(self.pressfcount[0], ctx.prefix))
      
    @commands.command()
    @commands.cooldown(2, 60, commands.BucketType.user)
    async def cancermeter(self, *, torate=None):
        """Tells you how cancerous something is."""
        if torate != None:
            await self.bot.say("```Cancer meter for '{}':\n"
                                "0    1    2    3    4    5    6    7    8    9   10\n"
                                "|----|----|----|----|----|----|----|----|----|----|\n".format(torate)
                                + "     " * random.randint(0, 5)+ "^```")
        else:
            await self.bot.say("```Cancer meter:\n"
                                "0    1    2    3    4    5    6    7    8    9   10\n"
                                "|----|----|----|----|----|----|----|----|----|----|\n"
                                + "     " * random.randint(0, 5)+ "^```")
                                
    @commands.command(pass_context=True)
    async def rate(self, ctx, *, something):
        """Rate something."""
        for mention in ctx.message.mentions:
            if mention.id == ctx.message.server.me.id:
                await self.bot.say("I would rate myself a 10/10.")
                return
            elif mention.id == self.bot.settings.owner:
                await self.bot.say("I would rate my owner a 10/10.")
                return
        await self.bot.say("I would rate {} a {}/10.".format(something, random.randint(0, 10)))
      
def check_folders():
    if not os.path.exists("data/pressf"):
        print("Creating data/pressf folder...")
        os.makedirs("data/pressf")

def check_files():
    if not os.path.exists("data/pressf/pressf.json"):
        print("Creating data/pressf/pressf.json file...")
        dataIO.save_json("data/pressf/pressf.json", [0])
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Randomshizzle(bot))
