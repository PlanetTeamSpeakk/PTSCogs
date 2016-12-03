from discord.ext import commands
from __main__ import send_cmd_help, settings
import discord
import os
from cogs.utils.dataIO import dataIO

pressfcount = [
0
]

class randomshizzle:
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
      
def check_folders():
    if not os.path.exists("data/pressf"):
        print("Creating data/pressf folder...")
        os.makedirs("data/pressf")

def check_files():
    if not os.path.exists("data/pressf/pressf.json"):
        print("Creating data/pressf/pressf.json file...")
        dataIO.save_json("data/pressf/pressf.json", pressfcount)
      
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(randomshizzle(bot))
