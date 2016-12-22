import discord
from discord.ext import commands
import ftplib
from cogs.utils.dataIO import dataIO
import os
from .utils import checks
from __main__ import send_cmd_help
import asyncio

class FTPStats:
    """Uploads server statistics to an ftp server!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/ftpstats/settings.json")
        self.stats = dataIO.load_json("data/ftpstats/stats.json")
        
    @checks.is_owner()
    @commands.group(name="ftpset", pass_context=True)
    async def ftpset(self, ctx):
        """Manage all ftpstats settings"""
        if not ctx.invoked_subcommand:
            await send_cmd_help(ctx)
            
    @checks.is_owner()
    @ftpset.command()
    async def server(self, server):
        """Set the server for the ftp stats. Has to be a link
        
        example:
        [p]ftpset server ftp.yoursite.com
        DON'T ADD FTP://!"""
        self.settings['ftp_server'] = server
        dataIO.save_json("data/ftpstats/settings.json", self.settings)
        await self.bot.say("Done!")
    
    @checks.is_owner()
    @ftpset.command()
    async def username(self, username):
        """Sets the username to log in to the server."""
        self.settings['ftp_username'] = username
        dataIO.save_json("data/ftpstats/settings.json", self.settings)
        await self.bot.say("Done!")
       
    @checks.is_owner()
    @ftpset.command(pass_context=True)
    async def password(self, ctx, password):
        """Sets the password to log in to the server, 
        for security it only works in Direct Messages"""
        if ctx.message.server is not None:
            try:
                self.bot.delete_message(ctx.message)
            except:
                pass
            await self.bot.say("Direct messages only please, security reasons.")
        else:
            self.settings['ftp_password'] = password
            dataIO.save_json("data/ftpstats/settings.json", self.settings)
            await self.bot.say("Done!")
        
    @checks.is_owner()
    @ftpset.command()
    async def defaultdir(self, dir):
        """Set a directory to which the bot should upload the files 
        (stats for every server are in it's own folder.)"""
        self.settings['ftp_defaultdir'] = dir
        dataIO.save_json("data/ftpstats/settings.json", self.settings)
        await self.bot.say("Done!")
        
    @checks.is_owner()
    @ftpset.command()
    async def refreshrate(self, refresh_rate:int):
        """Sets the refresh rate at which the bot should refresh the stats in seconds
        default is 120"""
        self.settings['ftp_refreshrate'] = refresh_rate
        dataIO.save_json("data/ftpstats/settings.json", self.settings)
        await self.bot.say("Done!")
        
    @checks.is_owner()
    @ftpset.command()
    async def start(self):
        """Start uploading the stats to the ftp server."""
        # Setting up
        if self.settings['ftp_server'] is None:
            await self.bot.say("Your ftp settings are not set yet, you can set them with [p]ftpset")
            return
        else:
            if self.settings['ftp_password'] is None:
                self.settings['ftp_password'] = "anonymous@"
            try:
                ftp = ftplib.FTP(self.settings['ftp_server'])
            except:
                await self.bot.say("Can't connect to the FTP server, are you sure you didn't add ftp:// to the beginning?\nThis error is not because of your password or username though.")
                return
            try:
                ftp.login(self.settings['ftp_username'], self.settings['ftp_password'])
            except:
                await self.bot.say("Can't login to the FTP server, are you sure your login credentials are correct?\nThe ip is correct though.")
                return
            if self.settings['ftp_defaultdir'] is not None:
                ftp.cwd(self.settings['ftp_defaultdir'])
            self.settings['ftp_started'] = True
            dataIO.save_json("data/ftpstats/settings.json", self.settings)
            await self.bot.say("Succesfully connected!")
            # Uploading stats file
            while True:
                for server in self.bot.servers:
                    serverid = server.id
                    members = set(server.members)
                    offline = filter(lambda m: m.status is discord.Status.offline, members)
                    offline = set(offline)
                    bots = filter(lambda m: m.bot, members)
                    bots = set(bots)
                    users = members - bots
                    if serverid not in self.stats:
                        self.stats[serverid] = {'server_name': None, 'server_icon': None, 'server_region': None, 'server_verification': None, 'server_created_at': None,
                        'owner_avatar': None, 'owner': None, 
                        'online_bots': None, 'offline_bots': None, 'online_users': None, 'offline_users': None}
                    self.stats[serverid]['server_name'] = server.name
                    self.stats[serverid]['server_icon'] = server.icon_url
                    self.stats[serverid]['server_region'] = str(server.region)
                    self.stats[serverid]['server_verification'] = str(server.verification_level)
                    self.stats[serverid]['server_id'] = server.id
                    self.stats[serverid]['server_created_at'] = server.created_at.strftime("%d %b %Y %H:%M")
                    self.stats[serverid]['owner_avatar'] = server.owner.avatar_url
                    self.stats[serverid]['owner'] = server.owner.display_name
                    self.stats[serverid]['online_bots'] = len(bots - offline)
                    self.stats[serverid]['offline_bots'] = len(bots & offline)
                    self.stats[serverid]['online_users'] = len(users - offline)
                    self.stats[serverid]['offline_users'] = len(users & offline)
                dataIO.save_json("data/ftpstats/stats.json", self.stats)
                filename = "stats.json"
                file = open("data/ftpstats/stats.json", "rb")
                ftp.storbinary("STOR " + filename, file)
                file = None
                asyncio.sleep(self.settings['ftp_refreshrate'])
        
    async def on_ready():
        # Setting up
        if self.settings['ftp_started']:
            if self.settings['ftp_server'] is None:
                print("Your ftp settings are not set yet, you can set them with [p]ftpset")
                return
            else:
                if self.settings['ftp_password'] is None:
                    self.settings['ftp_password'] = "anonymous@"
                try:
                    ftp = ftplib.FTP(self.settings['ftp_server'])
                except:
                    print("Can't connect to the FTP server, are you sure you didn't add ftp:// to the beginning?\nThis error is not because of your password or username though.")
                    return
                try:
                    ftp.login(self.settings['ftp_username'], self.settings['ftp_password'])
                except:
                    print("Can't login to the FTP server, are you sure your login credentials are correct?\nThe ip is correct though.")
                    return
                if self.settings['ftp_defaultdir'] is not None:
                    ftp.cwd(self.settings['ftp_defaultdir'])
                print("Succesfully connected to the FTP Server!")
                # Uploading stats file
                while True:
                    for server in self.bot.servers:
                        serverid = server.id
                        members = set(server.members)
                        offline = filter(lambda m: m.status is discord.Status.offline, members)
                        offline = set(offline)
                        bots = filter(lambda m: m.bot, members)
                        bots = set(bots)
                        users = members - bots
                        if serverid not in self.stats:
                            self.stats[serverid] = {'server_name': None, 'server_icon': None, 'server_region': None, 'server_verification': None, 'server_created_at': None,
                            'owner_avatar': None, 'owner': None, 
                            'online_bots': None, 'offline_bots': None, 'online_users': None, 'offline_users': None}
                        self.stats[serverid]['server_name'] = server.name
                        self.stats[serverid]['server_icon'] = server.icon_url
                        self.stats[serverid]['server_region'] = str(server.region)
                        self.stats[serverid]['server_verification'] = str(server.verification_level)
                        self.stats[serverid]['server_id'] = server.id
                        self.stats[serverid]['server_created_at'] = server.created_at.strftime("%d %b %Y %H:%M")
                        self.stats[serverid]['owner_avatar'] = server.owner.avatar_url
                        self.stats[serverid]['owner'] = server.owner.display_name
                        self.stats[serverid]['online_bots'] = len(bots - offline)
                        self.stats[serverid]['offline_bots'] = len(bots & offline)
                        self.stats[serverid]['online_users'] = len(users - offline)
                        self.stats[serverid]['offline_users'] = len(users & offline)
                    dataIO.save_json("data/ftpstats/stats.json", self.stats)
                    try:
                        ftp.delete("stats.json")
                    except:
                        pass
                    filename = "stats.json"
                    file = open("data/ftpstats/stats.json", "rb")
                    ftp.storbinary("STOR " + filename, file)
                    file = None
                    asyncio.sleep(self.settings['ftp_refreshrate'])
        
def check_folders():
    if not os.path.exists("data/ftpstats"):
        print("Creating data/ftpstats folder...")
        os.makedirs("data/ftpstats")
        
def check_files():
    if not os.path.exists("data/ftpstats/settings.json"):
        print("Creating data/ftpstats/settings.json file...")
        dataIO.save_json("data/ftpstats/settings.json", {'ftp_server': None, 'ftp_username': None, 'ftp_password': "anonymous@", 'ftp_defaultdir': None, 'ftp_refreshrate': 120})
    if not os.path.exists("data/ftpstats/stats.json"):
        print("Creating data/ftpstats/stats.json file...")
        dataIO.save_json("data/ftpstats/stats.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    cog = FTPStats(bot)
    bot.add_cog(cog)