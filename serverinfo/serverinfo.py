import discord
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
        
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Roles", description="{}, the current roles are \n{}".format(ctx.message.author.mention, [r.name for r in ctx.message.server.role_hierarchy]), colour=0X008CFF))

    @_server.command(pass_context=True, no_pm=True)
    async def emojis(self, ctx):
        """Lists all emojis"""
        
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Emojis", description="{}, the current emojis are \n{}".format(ctx.message.author.mention, [e.name for e in ctx.message.server.emojis]), colour=0X008CFF))
            
    @_server.command(pass_context=True, no_pm=True)
    async def users(self, ctx):
        """Lists all users"""
        
        if len(ctx.message.server.members) < 128:
            await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Users", description="{}, the current users are \n{}".format(ctx.message.author.mention, [m.name for m in ctx.message.server.members]), colour=0X008CFF))
        else:
            await self.bot.send_message(ctx.message.author, embed=discord.Embed(title="Users", description="The current users in **{}** are \n{}".format(ctx.message.server.name, [m.name for m in ctx.message.server.members]), colour=0X008CFF))
            
    @_server.command(pass_context=True, no_pm=True)
    async def channels(self, ctx):
        """Lists all channels"""
        
        await self.bot.send_message(ctx.message.channel, embed=discord.Embed(title="Channels", description="{}, the current channels are \n{}".format(ctx.message.author.mention, [c.name for c in ctx.message.server.channels]), colour=0X008CFF))
			
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
        members = set(ctx.message.server.members)
        offline = filter(lambda m: m.status is discord.Status.offline, members)
        offline = set(offline)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        users = members - bots
        servericon = ctx.message.server.icon_url
        
        em = discord.Embed(description="{}, here you go:".format(ctx.message.author.mention), color=0X008CFF, title="Server Info")
        em.set_thumbnail(url=servericon, height="32", width="32")
        em.add_field(name="Server Name", value=str(ctx.message.server.name))
        em.add_field(name="Server ID", value=str(ctx.message.server.id))
        em.add_field(name="Server Created", value=str(ctx.message.server.created_at))
        em.add_field(name="Server Region", value=str(ctx.message.server.region))
        em.add_field(name="Server Verification", value=str(ctx.message.server.verification_level))
        em.add_field(name="Server Roles", value=str(len(ctx.message.server.roles) -1))
        em.add_field(name="Server Owner", value=str(ctx.message.server.owner.name))
        em.add_field(name="Owner ID", value=str(ctx.message.server.owner.id))
        em.add_field(name="Owner Nick", value=str(ctx.message.server.owner.nick))
        em.add_field(name="Owner Status", value=str(ctx.message.server.owner.status))
        em.add_field(name="Total Bots", value=str(len(bots)))
        em.add_field(name="Bots Online", value=str(len(bots - offline)))
        em.add_field(name="Bots Offline", value=str(len(bots & offline)))
        em.add_field(name="Total Users", value=str(len(users)))
        em.add_field(name="Online Users", value=str(len(users - offline)))
        em.add_field(name="Offline Users", value=str(len(users & offline)))
        em.add_field(name="Channel Name", value=str(ctx.message.channel.name))
        em.add_field(name="Channel ID", value=str(ctx.message.channel.id))
        em.add_field(name="Channel Default", value=str(ctx.message.channel.is_default))
        em.add_field(name="Channel Position", value=str(ctx.message.channel.position))
        await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(serverinfo(bot))