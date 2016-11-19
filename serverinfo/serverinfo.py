import discord
from cogs.utils.chat_formatting import pagify
from cogs.utils.chat_formatting import box
from __main__ import send_cmd_help
from discord.ext import commands

class serverinfo:
    """Adds [p]server and all subcommands!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="server", pass_context=True)
    async def _server(self, ctx):
        """Server info commands."""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_server.command(pass_context=True, no_pm=True)
    async def owner(self, ctx):
        """Tells you who's the boss on this server"""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server owner", description="{}, the server owner is {}.".format(ctx.message.author.mention, ctx.message.server.owner.mention), colour=0X008CFF))
        
    @_server.command(pass_context=True, no_pm=True)
    async def name(self, ctx):
        """Shows you the server name."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server name", description="{}, the server name is {}.".format(ctx.message.author.mention, ctx.message.server), colour=0X008CFF))
		
    @_server.command(pass_context=True, no_pm=True)
    async def sid(self, ctx):
        """Shows you the server ID."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server ID", description="{}, the Server ID is {}.".format(ctx.message.author.mention, ctx.message.server.id), colour=0X008CFF))
        
    @_server.command(pass_context=True, no_pm=True)
    async def channelname(self, ctx):
        """Shows you the channel name."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Channel name", description="{}, the channelname is #{}.".format(ctx.message.author.mention, ctx.message.channel.name), colour=0X008CFF))
		
    @_server.command(pass_context=True, no_pm=True)
    async def cid(self, ctx):
        """Shows you the channel ID."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Channel ID", description="{}, the Channel ID is {}.".format(ctx.message.author.mention, ctx.message.channel.id), colour=0X008CFF))
        
    @_server.command(pass_context=True, no_pm=True)
    async def time(self, ctx):
        """Shows you the server time."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server time", description="{}, the server time is {}.".format(ctx.message.author.mention, ctx.message.timestamp), colour=0X008CFF))
        
    @_server.command(pass_context=True, no_pm=True)
    async def roles(self, ctx):
        """Lists all Roles"""
        list = "{}".format([r.name for r in ctx.message.server.role_hierarchy])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Roles", description="{}, the current roles are {}".format(ctx.message.author.mention, box(page, "Prolog")), colour=0X008CFF))
			
    @_server.command(pass_context=True, no_pm=True)
    async def emojis(self, ctx):
        """Lists all emojis"""
        list = "{}".format([e.name for e in ctx.message.server.emojis])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Roles", description="{}, the current emojis are {}".format(ctx.message.author.mention, box(page, "Prolog")), colour=0X008CFF))
			
    @_server.command(pass_context=True, no_pm=True)
    async def users(self, ctx):
        """Lists all users"""
        list = "{}".format([m.name for m in ctx.message.server.members])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Roles", description="{}, the current users are {}".format(ctx.message.author.mention, box(page, "Prolog")), colour=0X008CFF))
			
    @_server.command(pass_context=True, no_pm=True)
    async def channels(self, ctx):
        """Lists all channels"""
        list = "{}".format([c.name for c in ctx.message.server.channels])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Roles", description="{}, the current channels are {}".format(ctx.message.author.mention, box(page, "Prolog")), colour=0X008CFF))
			
    @_server.command(pass_context=True, no_pm=True)
    async def compareids(self, ctx):
        """Compares the id of the server and the channel to see if the channel is the default one."""
        if ctx.message.server.id == ctx.message.channel.id:
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Channel is default", description=
            "{}, the ids of the channel and the server are the same, so this is the default channel.\n(SID=`{}`, CID=`{}`)".format(ctx.message.author.mention, ctx.message.server.id, ctx.message.channel.id), colour=0X008CFF))
        else:
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Channel isn't default", description=
            "{}, The ids of the channel and the server are not the same, this is not the default channel. If there is a #general try it in that channel first.\n(SID=`{}`, CID=`{}`)".format(ctx.message.author.mention, ctx.message.server.id, ctx.message.channel.id), colour=0X008CFF))
            
    @_server.command(pass_context=True, no_pm=True)
    async def icon(self, ctx):
        """Shows the server icon."""
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server icon", description="{}, the server icon is {}.".format(ctx.message.author.mention, ctx.message.server.icon_url), colour=0X008CFF))
        
    @_server.command(pass_context=True, allow_pm=False)
    async def info(self, ctx):
        """Show server info."""
        server = ctx.message.server
        channel = ctx.message.channel
        members = set(server.members)

        owner = server.owner

        offline = filter(lambda m: m.status is discord.Status.offline, members)
        offline = set(offline)

        bots = filter(lambda m: m.bot, members)
        bots = set(bots)

        users = members - bots

        msg = '\n'.join((
            'Server Name     : ' + server.name,
            'Server ID       : ' + str(server.id),
            'Server Created  : ' + str(server.created_at),
            'Server Region   : ' + str(server.region),
            'Verification    : ' + str(server.verification_level),
            'Server # Roles  : %i' % (len(server.roles) - 1),
            '',
            'Server Owner    : ' + str(server.owner.name),
            'Owner ID        : ' + str(owner.id),
            'Owner Nickname  : ' + str(server.owner.nick),
            'Owner Status    : ' + str(owner.status),
            '',
            'Total Bots      : %i' % len(bots),
            'Bots Online     : %i' % len(bots - offline),
            'Bots Offline    : %i' % len(bots & offline),
            '',
            'Total Users     : %i' % len(users),
            'Users Online    : %i' % len(users - offline),
            'Users Offline   : %i' % len(users & offline),
            '',
            'Current Channel : ' + str(channel.name),
            'Channel ID      : ' + str(channel.id),
            'Channel Created : ' + str(channel.created_at),
            'Default Channel : ' + str(channel.is_default),
            'Channel Position: ' + str(channel.position),
            'Channel Type    : ' + str(channel.type)
        ))
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Server icon", description="{}, here you go {}.".format(ctx.message.author.mention, box(msg)), colour=0X008CFF))

def setup(bot):
    bot.add_cog(serverinfo(bot))