import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os
import asyncio

class AntiFilter:
    """Only let messages through that you allow."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/antifilter/settings.json")

    @commands.group(pass_context=True)
    @checks.admin_or_permissions()
    async def antifilter(self, ctx):
        """Only let messages through that you allow."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'channels': {ctx.message.channel.id: {'disabled': True, 'notfiltered': []}}, 'message': '{0.mention} you\'re not allowed to say that.'}
            self.save_settings()
        for channel in ctx.message.server.channels:
            if (channel.id not in self.settings[ctx.message.server.id]['channels']) and (str(channel.type) == "text"):
                self.settings[ctx.message.server.id]['channels'][channel.id] = {'disabled': True, 'notfiltered': []}
        self.save_settings()
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)

    @antifilter.command(pass_context=True)
    async def list(self, ctx):
        """List all settings for each channel."""
        msg = "```Message: {}\n\n".format(self.settings[ctx.message.server.id]['message'])
        for channel in self.settings[ctx.message.server.id]['channels']:
            channel = discord.utils.get(ctx.message.server.channels, id=channel)
            if channel != None:
                msg += "{}:\n\tDisabled: {}\n\tNot filtered: {}\n\n".format(channel.name, self.settings[ctx.message.server.id]['channels'][channel.id]['disabled'], ", ".join(self.settings[ctx.message.server.id]['channels'][channel.id]['notfiltered']))
                if len(msg) > 1750:
                    await self.bot.say(msg + "```")
                    msg = "```"
        await self.bot.say(msg + "```")
        
    @antifilter.command(pass_context=True)
    async def toggle(self, ctx, channel:discord.Channel=None):
        """Toggle if AntiFilter will only let set messages through in a channel."""
        if channel == None:
            channel = ctx.message.channel
        if str(channel.type) == "text":
            if self.settings[ctx.message.server.id]['channels'][channel.id]['disabled']:
                self.settings[ctx.message.server.id]['channels'][channel.id]['disabled'] = False
                await self.bot.say("I will delete messages in that channel.")
            else:
                self.settings[ctx.message.server.id]['channels'][channel.id]['disabled'] = True
                await self.bot.say("I will no longer delete messages in that channel.")
            self.save_settings()
        else:
            await self.bot.say("This command is only for text channels.")
            
    @antifilter.command(pass_context=True)
    async def add(self, ctx, channel:discord.Channel, *, filter):
        """Add something that the bot should not delete in the given channel."""
        if str(channel.type) == "text":
            if filter in self.settings[ctx.message.server.id]['channels'][channel.id]['notfiltered']:
                await self.bot.say("That filter is already added.")
            else:
                self.settings[ctx.message.server.id]['channels'][channel.id]['notfiltered'].append(filter)
                self.save_settings()
                await self.bot.say("Filter added.")
        else:
            await self.bot.say("This command is only for text channels.")
            
    @antifilter.command(pass_context=True)
    async def remove(self, ctx, channel:discord.Channel, *, filter):
        """Removes something so the bot will delete it in the given channel."""
        if str(channel.type) == "text":
            if filter not in self.settings[ctx.message.server.id]['channels'][channel.id]['notfiltered']:
                await self.bot.say("That filter hasn't been added yet.")
            else:
                self.settings[ctx.message.server.id]['channels'][channel.id]['notfiltered'].remove(filter)
                self.save_settings()
                await self.bot.say("Filter removed.")
        else:
            await self.bot.say("This command is only for text channels.")
            
    @antifilter.command(pass_context=True)
    async def help(self, ctx):
        """Wtf is this command about?"""
        await self.bot.say("```So you wanna know what this command is about huh? Well it's not that hard;\n"
                            "So this command will only let messages through that you specify, so if you have a channel that is only used for a specific command like, {0}giveme access.\n"
                            "Ofcourse after you enabled this for the given channel, so if you would type something like 'hello' in that channel, it would get removed but if you would've done {0}antifilter add {1} hello, it wouldn't.```".format(ctx.prefix, ctx.message.channel.name))
            
    async def on_message(self, message):
        if message.server != None:
            if message.author.id != message.server.me.id:
                if (message.server.id in self.settings) and not (self.settings[message.server.id]['channels'][message.channel.id]['disabled']):
                    canStay = False
                    for filter in self.settings[message.server.id]['channels'][message.channel.id]['notfiltered']:
                        if not (canStay) and (message.content == filter):
                            canStay = True
                    if not canStay:
                        try:
                            await self.bot.delete_message(message)
                            msg = await self.bot.send_message(message.channel, self.settings[message.server.id]['message'].format(message.author))
                            await asyncio.sleep(4)
                            await self.bot.delete_message(msg)
                        except:
                            pass
            
    def save_settings(self):
        dataIO.save_json("data/antifilter/settings.json", self.settings)
        
def check_folders():
    if not os.path.exists("data/antifilter"):
        print("Creating data/antifilter folder...")
        os.makedirs("data/antifilter")
        
def check_files():
    if not os.path.exists("data/antifilter/settings.json"):
        print("Creating data/antifilter/settings.json file...")
        dataIO.save_json("data/antifilter/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(AntiFilter(bot))