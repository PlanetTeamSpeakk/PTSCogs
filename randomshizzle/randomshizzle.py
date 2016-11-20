from discord.ext import commands
from __main__ import send_cmd_help, settings
import discord
import datetime
from random import choice
from cogs.utils.chat_formatting import box

class randomshizzle:
    """Random shizzle."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cooldog(self):
        """Cooldog."""
        await self.bot.say("╭━━━━╮               This is cooldog. Help \n╰┃ ┣▇━▇                cooldog take over \n ┃ ┃  ╰━▅╮ Discord by pasting\n ╰┳╯ ╰━━┳╯        him in 10 other\n  ╰╮ ┳━━╯            servers or you\n ▕▔▋ ╰╮╭━╮   will never be a cool dog.\n╱▔╲▋╰━┻┻╮╲╱▔▔▔╲\n▏  ▔▔▔▔▔▔▔  O O┃ \n╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱\n ▏╳▕▇▇▕ ▏╳▕▇▇▕\n ╲▂╱╲▂╱ ╲▂╱╲▂╱")

    @commands.command()
    async def soundsfromspace(self):
        """Ooh, spooky."""
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
    async def fliptext(self, ctx, *, text):
        """Flips text."""
        if text != None:
            msg = ""
            char = "abcdefghijklmnopqrstuvwxyz<>?.:!&"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz><¿˙:¡⅋"
            table = str.maketrans(char, tran)
            name = text.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z><¿˙:¡⅋"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
	
    @commands.command(pass_context=True)
    async def dontflipme(self, ctx):
        """K sorry."""
        await self.bot.say("{} ノ( ゜-゜ノ) sorry.".format(ctx.message.author.name))
			
    @commands.command()
    async def punch(self, user : discord.Member):
        """I'll punch everyone!"""
        await self.bot.say("*Punches " + user.mention + "* \nGet punched, SON!")
		
    @commands.command()
    async def ipunch(self, *, item):
        """I'll punch anything!"""
        await self.bot.say("*Punches " + item + "* \nGet punched, SON!")

    @commands.command()
    async def face(self):
        """Displays a random ASCII face."""
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '¯\\\_{}_/¯', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '\\\({})/', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        face = choice(ears).format(choice(eyes)).format(choice(mouth))
        await self.bot.say(face)
		
    @commands.command(pass_context=True)
    async def kys(self, ctx, user : discord.Member=None):
        """kill yourself"""
        if user == None:
            await self.bot.say("( ͡° ͜ʖ ͡°)               ( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)              ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)          ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)      ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)                                   ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                              ( ͡° ͜ʖ ͡°)                      ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                            ( ͡° ͜ʖ ͡°)                                        ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)                  ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                     ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)")
        else:
            await self.bot.say("{},\n( ͡° ͜ʖ ͡°)               ( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)              ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)          ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)      ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°)    ( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)                                   ( ͡° ͜ʖ ͡°)                   ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)     ( ͡° ͜ʖ ͡°)                              ( ͡° ͜ʖ ͡°)                      ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)       ( ͡° ͜ʖ ͡°)                            ( ͡° ͜ʖ ͡°)                                        ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)         ( ͡° ͜ʖ ͡°)                          ( ͡° ͜ʖ ͡°)             ( ͡° ͜ʖ ͡°)                  ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                ( ͡° ͜ʖ ͡°)            ( ͡° ͜ʖ ͡°) \n( ͡° ͜ʖ ͡°)           ( ͡° ͜ʖ ͡°)                        ( ͡° ͜ʖ ͡°)                     ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)".format(user.mention))
            
    @commands.command()
    async def triggered(self):
        """TRIGGERED"""
        await self.bot.say("***__TRIGGERED__***")
		
    @commands.command(hidden=True)
    async def hidden(self):
        """How did you find this hidden command?"""
        await self.bot.say("How did you find this hidden command?\nI think PlanetTeamSpeak needs to hide this better :confused:")
		
    @commands.command()
    async def trump(self):
        """TRUMP IS PRESIDENT! #TheWallWillCome!"""
        await self.bot.say("**#TheWallWillCome**!\nhttp://i.imgur.com/iSwmX2c.jpg")
		
    @commands.command()
    async def whydidievenmakethiscommand(self):
        """In all honesty, why did I take 60 seconds of my life to make this command? - PlanetTeamSpeak"""
        await self.bot.say("In all honesty, why did I take 60 seconds of my life to make this command? - PlanetTeamSpeak")

    @commands.command()
    async def dogburrito(self):
        """OH MER GAWD IT'S A DOG BURRITO!"""
        await self.bot.say("https://tenor.co/vu6b.gif")
		
    @commands.command()
    async def bumbridges(self):
        """DON'T BUM THE BRIDGES"""
        await self.bot.say("DON'T BUM DEM BRIDGES\nhttp://i.imgur.com/vgDJui2.jpg")
		
    @commands.command()
    async def dealwithit(self):
        """DEAL WITH IT"""
        await self.bot.say("Deal with it\nhttp://i.imgur.com/mZ5lElF.jpg")

def setup(bot):
    bot.add_cog(randomshizzle(bot))
