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
        await self.bot.say("The server owner is {}.".format(ctx.message.server.owner.mention))
		
    @_server.command(pass_context=True, no_pm=True)
    async def name(self, ctx):
        """Shows you the server name."""
        await self.bot.say("The servername is `{}`.".format(ctx.message.server))
		
    @_server.command(pass_context=True, no_pm=True)
    async def sid(self, ctx):
        """Shows you the server ID."""
        await self.bot.say("The server ID is `{}`.".format(ctx.message.server.id))
		
    @_server.command(pass_context=True, no_pm=True)
    async def channelname(self, ctx):
        """Shows you the channel name."""
        await self.bot.say("The channelname is `#{}`.".format(ctx.message.channel))
		
    @_server.command(pass_context=True, no_pm=True)
    async def cid(self, ctx):
        """Shows you the channel ID."""
        await self.bot.say("The channel ID is `{}`.".format(ctx.message.channel.id))
		
    @_server.command(pass_context=True, no_pm=True)
    async def time(self, ctx):
        """Shows you the server time."""
        await self.bot.say("The server time is `{}`.".format(ctx.message.timestamp))
		
    @_server.command(pass_context=True, no_pm=True)
    async def roles(self, ctx):
        """Lists all Roles"""
        list = "{}".format([r.name for r in ctx.message.server.role_hierarchy])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.say("The current roles are:\n{}".format(box(page, "Prolog")))
			
    @_server.command(pass_context=True, no_pm=True)
    async def emojis(self, ctx):
        """Lists all emojis"""
        list = "{}".format([e.name for e in ctx.message.server.emojis])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.say("The current custom emojis are:\n{}".format(box(page, "Prolog")))
			
    @_server.command(pass_context=True, no_pm=True)
    async def users(self, ctx):
        """Lists all users"""
        list = "{}".format([m.name for m in ctx.message.server.members])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.say("The current users are:\n{}".format(box(page, "Prolog")))
			
    @_server.command(pass_context=True, no_pm=True)
    async def channels(self, ctx):
        """Lists all channels"""
        list = "{}".format([c.name for c in ctx.message.server.channels])
        for page in pagify(list, ["\n"], shorten_by=13, page_length=2000):
            await self.bot.say("The current channels are:\n{}".format(box(page, "Prolog")))
			
    @_server.command(pass_context=True, no_pm=True)
    async def compareids(self, ctx):
        """Compares the id of the server and the channel to see if the channel is the default one."""
        if ctx.message.server.id == ctx.message.channel.id:
            await self.bot.say("The ids of the channel and the server are the same, so this is the default channel.\n(SID=`{}`, CID=`{}`)".format(ctx.message.server.id, ctx.message.channel.id))
        else:
            await self.bot.say("The ids of the channel and the server are not the same, this is not the default channel. If there is a #general try it in that channel first.\n(SID=`{}`, CID=`{}`)".format(ctx.message.server.id, ctx.message.channel.id))

    @_server.command(pass_context=True, no_pm=True)
    async def icon(self, ctx):
        """Shows the server icon."""
        await self.bot.say("{} the server icon is {}".format(ctx.message.author.mention, ctx.message.server.icon_url))
        
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
        await self.bot.say(box(msg))

def setup(bot):
    bot.add_cog(serverinfo(bot))