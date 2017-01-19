import discord
from discord.ext import commands
from __main__ import send_cmd_help

class Coder:
    """Coder"""

    def __init__(self, bot):
        self.bot = bot

    # from text to something coded
    @commands.group(name="to", pass_context=True)
    async def _to(self, ctx):
        """Convert text to a coded something."""
        if not ctx.invoked_subcommand:
            await send_cmd_help(ctx)

    @_to.command(pass_context=True, name="binary")
    async def _binary(self, ctx, *, text):
        """Convert text to binary."""
        try:
            self.bot.delete_message(ctx.message)
        except:
            pass
        alpha_to_binary = {
        " ": "00100000", "!": "00100001", "?": "00111111", ":": "00111010", ";": "00111011", "\"": "00100010", "'": "00100111", "/": "00101111", "\\": "01011100", "{": "01111011", "}": "01111101", "(": "00101000", ")": "00101001", ".": "00101110",
        "A": "01000001", "B": "01000010", "C": "01000011", "D": "01000100", "E": "01000101", "F": "01000110", "G": "01000111", "H": "01001000", "I": "01001001", "J": "01001010", "K": "01001011", "L": "01001100", "M": "01001101", "N": "01001110", "O": "01001111", "P": "01010000", "Q": "01010001", "R": "01010010", "S": "01010011", "T": "01010100", "U": "01010101", "V": "01010110", "W": "01010111", "X": "01011000", "Y": "01011001", "Z": "01011010",
        "a": "01100001", "b": "01100010", "c": "01100011", "d": "01100100", "e": "01100101", "f": "01100110", "g": "01100111", "h": "01101000", "i": "01101001", "j": "01101010", "k": "01101011", "l": "01101100", "m": "01101101", "n": "01101110", "o": "01101111", "p": "01110000", "q": "01110001", "r": "01110010", "s": "01110011", "t": "01110100", "u": "01110101", "v": "01110110", "w": "01110111", "x": "01111000", "y": "01111001", "z": "01111010",
        "0": "00110000", "1": "00110001", "2": "00110010", "3": "00110011", "4": "00110100", "5": "00110101", "6": "00110110", "7": "00110111", "8": "00111000", "9": "00111001"}
        try:
            binary = [alpha_to_binary[char] for char in text]
        except KeyError:
            await self.bot.say("One of the characters you filled in is not in the list.")
            return
        except:
            await self.bot.say("An unknown error occured while translating your text.")
            return
        await self.bot.say(" ".join(binary))

    @_to.command(pass_context=True, name="morse")
    async def _morse(self, ctx, *, text):
        """Convert text to morse."""
        try:
            self.bot.delete_message(ctx.message)
        except:
            pass
        alpha_to_morse = {
        " ": " ", ".": ".-.-.-", "!": "-.-.--", "?": "..--..", ":": "---...", ";": "-.-.-.", "\"": ".-..-.", "'": ".----.", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}
        try:
            morse = [alpha_to_morse[char] for char in text]
        except KeyError:
            await self.bot.say("One of the characters you filled in is not in the list.")
            return
        except:
            await self.bot.say("An unknown error occured while translating your text.")
            return
        await self.bot.say(" ".join(morse))
        
    @_to.command(pass_context=True, name="reversed")
    async def _reversed(self, ctx, *, msg):
        """Reverses your text"""
        await self.bot.say(msg[::-1])
        
    # from something coded to text
    @commands.group(name="from", pass_context=True)
    async def _from(self, ctx):
        """Convert a coded something to text."""
        if not ctx.invoked_subcommand:
            await send_cmd_help(ctx)

    @_from.command(pass_context=True)
    async def binary(self, ctx, *, binary):
        """Convert binary to text."""
        try:
            self.bot.delete_message(ctx.message)
        except:
            pass
        binary = binary.split()
        binary_to_alpha = {
        "00100000": " ", "00100001": "!", "00111111": "?", "00111010": ":", "00111011": ";", "00100010": "\"", "00100111": "'", "00101111": "/", "01011100": "\\", "01111011": "{", "01111101": "}", "00101000": "(", "00101001": ")", "00101110": ".",
        "01000001": "A", "01000010": "B", "01000011": "C", "01000100": "D", "01000101": "E", "01000110": "F", "01000111": "G", "01001000": "H", "01001001": "I", "01001010": "J", "01001011": "K", "01001100": "L", "01001101": "M", "01001110": "N", "01001111": "O", "01010000": "P", "01010001": "Q", "01010010": "R", "01010011": "S", "01010100": "T", "01010101": "U", "01010110": "V", "01010111": "W", "01011000": "X", "01011001": "Y", "01011010": "Z",
        "01100001": "a", "01100010": "b", "01100011": "c", "01100100": "d", "01100101": "e", "01100110": "f", "01100111": "g", "01101000": "h", "01101001": "i", "01101010": "j", "01101011": "k", "01101100": "l", "01101101": "m", "01101110": "n", "01101111": "o", "01110000": "p", "01110001": "q", "01110010": "r", "01110011": "s", "01110100": "t", "01110101": "u", "01110110": "v", "01110111": "w", "01111000": "x", "01111001": "y", "01111010": "z",
        "00110000": "0", "00110001": "1", "00110010": "2", "00110011": "3", "00110100": "4", "00110101": "5", "00110110": "6", "00110111": "7", "00111000": "8", "00111001": "9"}
        try:
            alpha = [binary_to_alpha[char] for char in binary]
        except KeyError:
            await self.bot.say("One of the characters you filled in is not in the list.")
            return
        except:
            await self.bot.say("An unknown error occured while translating your text.")
            return
        await self.bot.say("".join(alpha))
        
    @_from.command(pass_context=True)
    async def morse(self, ctx, *, morse):
        """Convert morse to text."""
        try:
            self.bot.delete_message(ctx.message)
        except:
            pass
        morse = morse.split()
        morse_to_alpha = {
        " ": " ", ".-.-.-": ".", "-.-.--": "!", "..--..": "?", "---...": ":", "-.-.-.": ";", ".-..-.": "\"", ".----.": "'", "-..-.": "/", "-.--.": "(", "-.--.-": ")",
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"}
        try:
            alpha = [morse_to_alpha[char] for char in morse]
        except KeyError:
            await self.bot.say("One of the characters you filled in is not in the list.")
            return
        except:
            await self.bot.say("An unknown error occured while translating your text.")
            return
        await self.bot.say("".join(alpha))
        
    @_from.command(pass_context=True)
    async def reversed(self, ctx, *, msg):
        """Unreverses your text"""
        await self.bot.say(msg[::-1])
        
def setup(bot):
    bot.add_cog(Coder(bot))
