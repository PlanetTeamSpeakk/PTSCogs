import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os

class Welcomr:
    """Welcome new members and say goodbye to old members."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/welcomr/settings.json")

    @commands.group(pass_context=True)
    @checks.admin_or_permissions()
    async def welcomeset(self, ctx):
        """Manage the settings for the greeting and farewell messages."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'channel': None, 'farewell': '**{0}** has left **{0.server}**, bye bye **{0}**.', 'greeting': 'Welcome **{0.mention}** to **{0.server}**!', 'dm': False, 'disabled': False}
        
    @welcomeset.command(pass_context=True)
    async def greeting(self, ctx, *, message):
        """Sets the greeting message. You can use some stuff to make it look legit. Like:
        {0} will turn into the new member's name with discriminator. 
        {0.mention} will mention the new member.
        {0.server} is the name of the server."""
        await self.bot.say("Testing the new greeting...\n" + message.format(ctx.message.author))
        await self.bot.say("Do you want to keep this or set another one? (yes/no)")
        msg = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
        if msg.content.lower() == "yes":
            self.settings[ctx.message.server.id]['greeting'] = message
            self.save_settings()
            await self.bot.say("Greeting set.")
        else:
            await self.bot.say("You can set a new greeting with {}welcomeset greeting.".format(ctx.prefix))
            
    @welcomeset.command(pass_context=True)
    async def farewell(self, ctx, *, message):
        """Sets the farewell message. You can use some stuff to make it look legit. Like:
        {0} will turn into the old member's name with discriminator. 
        {0.mention} will mention the old member.
        {0.server} is the name of the server."""
        await self.bot.say("Testing the new farewell...\n" + message.format(ctx.message.author))
        await self.bot.say("Do you want to keep this or set another one? (yes/no)")
        msg = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
        if msg.content.lower() == "yes":
            self.settings[ctx.message.server.id]['farewell'] = message
            self.save_settings()
            await self.bot.say("Farewell set.")
        else:
            await self.bot.say("You can set a new farewell with {}welcomeset farewell.".format(ctx.prefix))
        
    @welcomeset.command(pass_context=True)
    async def channel(self, ctx, channel:discord.Channel):
        """Set the channel the bot should send the welcome message to, not needed if you toggled DM mode."""
        self.settings[ctx.message.server.id]['channel'] = channel.id
        self.save_settings()
        await self.bot.say("Channel set!")
        
    @welcomeset.command(pass_context=True)
    async def dm(self, ctx):
        """Toggle if welcome message should be send in dm or not."""
        if self.settings[ctx.message.server.id]['dm']:
            self.settings[ctx.message.server.id]['dm'] = False
            await self.bot.say("The bot will no longer send welcome messages via dm.")
        else:
            self.settings[ctx.message.server.id]['dm'] = True
            await self.bot.say("The bot will now send welcome message via dm.")
        self.save_settings()
        
    @welcomeset.command(pass_context=True)
    async def disable(self, ctx):
        """Disabled the welcome messages."""
        if self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = False
            await self.bot.say("Welcome system is no longer disabled.")
        else:
            self.settings[ctx.message.server.id]['disabled'] = True
            await self.bot.say("Welcome system has been disabled.")
        self.save_settings()
        
    async def on_member_join(self, member):
        if member.server.id in self.settings:
            serversettings = self.settings[member.server.id]
            if not serversettings['disabled']:
                if (serversettings['channel'] != None) and not (serversettings['dm']):
                    channel = discord.utils.get(member.server.channels, id=serversettings['channel'])
                    await self.bot.send_message(channel, serversettings['greeting'].format(member))
                elif serversettings['dm']:
                    await self.bot.send_message(member, serversettings['greeting'].format(member))
        
    async def on_member_remove(self, member):
        if member.server.id in self.settings:
            serversettings = self.settings[member.server.id]
            if not serversettings['disabled']:
                if (serversettings['channel'] != None) and not (serversettings['dm']):
                    channel = discord.utils.get(member.server.channels, id=serversettings['channel'])
                    await self.bot.send_message(channel, serversettings['farewell'].format(member))
                elif serversettings['dm']:
                    await self.bot.send_message(member, serversettings['farewell'].format(member))
        
    def save_settings(self):
        dataIO.save_json("data/welcomr/settings.json", self.settings)
        
def check_folders():
    if not os.path.exists("data/welcomr"):
        print("Creating data/welcomr folder...")
        os.makedirs("data/welcomr")
        
def check_files():
    if not os.path.exists("data/welcomr/settings.json"):
        print("Creating data/welcomr/settings.json file...")
        dataIO.save_json("data/welcomr/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Welcomr(bot))