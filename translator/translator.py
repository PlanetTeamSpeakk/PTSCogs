import discord
from discord.ext import commands
from subprocess import check_output
try:
    import goslate
    goslateInstalled = True
except:
    try:
        from lib import goslate # for my own bot (which is Impulse)
        goslateInstalled = True
    except:
        try:
            print("Goslate is not installed, installing it now...")
            check_output("pip3 install goslate", shell=True)
            import goslate
            goslateInstalled = True
        except:
            goslateInstalled = False

class Translator:
    """Translate text using google translate."""

    def __init__(self, bot):
        self.bot = bot
        self.gs = goslate.Goslate()

    @commands.group(pass_context=True, invoke_without_command=True)
    async def translate(self, ctx, to_lang, *, text):
        """Translate text using google translate."""
        if to_lang in self.gs.get_languages():
            try:
                lang_id = self.gs.detect(text)
                lang = self.gs.get_languages()[lang_id]
                await self.bot.say("{} (detected as {} ({}))".format(self.gs.translate(text, to_lang), lang, lang_id))
            except Exception as e:
                await self.bot.say("An error occured while translating. ({})".format(e))
        else:
            await self.bot.say("That language could not be found in the list, for a list of supported languages do {}translate langlist".format(ctx.prefix))

    @translate.command()
    async def langlist(self):
        """Shows you a list of supported languages."""
        msg = "```fix\nCurrent available languages are:\n"
        for lang in self.gs.get_languages():
            msg += "\t{}: {}\n".format(self.gs.get_languages()[lang], lang)
            if len(msg) > 1750:
                await self.bot.say(msg + "```")
                msg = "```fix\n"
        await self.bot.say(msg + "```")
            
def setup(bot):
    if not goslateInstalled:
        raise RuntimeError("Could not install goslate, cog cannot be loaded.")
    bot.add_cog(Translator(bot))