import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os
import asyncio

class WordFilter:
    """Filter out items."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/wordfilter/settings.json")

    @commands.group(pass_context=True)
    @checks.mod_or_permissions()
    async def wordfilter(self, ctx):
        """Filter out items."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'disabled': False, 'filtered': [], 'message': '{0.mention}, you\'re not allowed to say that.'}
            self.save_settings()
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say("```Disabled: {}\nMessage: {}\nFiltered: {}```".format(self.settings[ctx.message.server.id]['disabled'], self.settings[ctx.message.server.id]['message'], ", ".join(self.settings[ctx.message.server.id]['filtered'])))
            
    @wordfilter.command(pass_context=True)
    async def disable(self, ctx):
        """Toggle if the bot should or should not filter words."""
        if self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = False
            await self.bot.say("The bot will no longer filter words.")
        else:
            self.settings[ctx.message.server.id]['disabled'] = True
            await self.bot.say("The bot will once again filter words.")
        self.save_settings()
         
    @wordfilter.command(pass_context=True)
    async def add(self, ctx, *, item):
        """Adds an item to the list of filtered items.
        This is NOT case sensitive, if you use cases it will NOT filter."""
        if item in self.settings[ctx.message.server.id]['filtered']:
            await self.bot.say("That item is already in the list of filtered items.")
        else:
            await self.bot.say("Item has been added.")
            await asyncio.sleep(0.5)
            self.settings[ctx.message.server.id]['filtered'].append(item)
            self.save_settings()
        
    @wordfilter.command(pass_context=True)
    async def remove(self, ctx, *, item):
        """Removes an item from the list of filtered items."""
        if item not in self.settings[ctx.message.server.id]['filtered']:
            await self.bot.say("That item is not in the list of filtered items.")
        else:
            self.settings[ctx.message.server.id]['filtered'].remove(item)
            self.save_settings()
            await self.bot.say("Item has been removed.")
            
    @wordfilter.command(pass_context=True)
    async def setmessage(self, ctx, *, message):
        """Sets the message the bot should send when it filtered a message.
        {0} will turn into the user's name with discriminator.
        {0.mention} will mention the user.
        {0.server} is the server.
        Default is {0.mention} you're not allowed to say that."""
        self.settings[ctx.message.server.id]['message'] = message
        self.save_settings()
        await self.bot.say("Message has been set.")
        
    async def on_message(self, message):
        if (message.server != None) and (message.server.id in self.settings) and not (self.settings[message.server.id]['disabled']) and not (message.author == message.server.me):
            for filter in self.settings[message.server.id]['filtered']:
                if filter in message.content.lower():
                    try:
                        await self.bot.delete_message(message)
                        msg = await self.bot.send_message(message.channel, self.settings[message.server.id]['message'].format(message.author))
                        await asyncio.sleep(4)
                        await self.bot.delete_message(msg)
                        return
                    except:
                        return
            
    def save_settings(self):
        dataIO.save_json("data/wordfilter/settings.json", self.settings)

def check_folders():
    if not os.path.exists("data/wordfilter"):
        print("Creating data/wordfilter folder...")
        os.makedirs("data/wordfilter")
        
def check_files():
    if not os.path.exists("data/wordfilter/settings.json"):
        print("Creating data/wordfilter/settings.json file...")
        dataIO.save_json("data/wordfilter/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(WordFilter(bot))