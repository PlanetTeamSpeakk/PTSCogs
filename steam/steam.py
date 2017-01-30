import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os
import requests
import json

class Steam:
    """Get some steam info from people or games."""

    def __init__(self, bot):
        self.bot = bot
        self.key = dataIO.load_json("data/steam/key.json")[0]

    @commands.command()
    @checks.is_owner()
    async def setsteamkey(self, key):
        """Set the steam api key so people can use the steam commands."""
        self.key = key
        dataIO.save_json("data/steam/key.json", [self.key])
        try:
            await self.bot.delete_message(ctx.message)
        except:
            pass
        await self.bot.say("Key set.")
        
    @commands.group(pass_context=True)
    async def steam(self, ctx):
        """Get some steam info."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        
    @steam.command(pass_context=True)
    async def getuserinfo(self, ctx, username):
        """Get an user's information with their name, not nickname, name."""
        if self.key != None:
            request = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + self.key + "&vanityurl=" + username)
            request = json.loads(request.content.decode("utf-8"))['response']
            if request['success'] == 42:
                await self.bot.say("That's not a valid username.")
                return
            else:
                userid = request['steamid']
            request = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + self.key + "&steamids=" + str(userid))
            request = json.loads(request.content.decode("utf-8"))['response']['players']
            if request == []:
                await self.bot.say("That's not a valid id.")
            else:
                request = request[0]
                request['games'] = json.loads(requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.key + "&steamid=" + str(userid)).content.decode("utf-8"))['response']
                games = []
                for game in range(len(request['games']['games'])):
                    games.append(str(request['games']['games'][game]['appid']))
                await self.bot.say("```fix\nUsername: {}\nSteam ID: {}\nProfile URL: {}\nAvatar: {}\nGame count: {}\nGames owned: {} (you can do a lookup for every id with {}steam applookup <id>)```".format(request['personaname'], str(request['steamid']), request['profileurl'], request['avatarfull'], str(request['games']['game_count']), ", ".join(games), ctx.prefix))
        else:
            await self.bot.say("My owner has not set a steam api key yet, if you would like to donate one (you can only do this if you've bought a game on steam), go to <https://steampowered.com/dev/apikey>, and do {}steam donatekey <key>.".format(ctx.prefix))
            
    @steam.command(pass_context=True)
    async def donatekey(self, ctx, key):
        """Donate a steam api key to my owner."""
        if self.key == None:
            if self.bot.settings.owner != None:
                owner = discord.utils.get(self.bot.get_all_members(), id=self.bot.settings.owner)
                await self.bot.send_message(owner, "**{}** has donated a steam api key:\n**{}**".format(str(ctx.message.author), key))
                await self.bot.say("Key has been sent to my owner ({}).".format(owner.mention))
            else:
                await self.bot.say("I can't find my owner.")
        else:
            await self.bot.say("My owner has already set a steam api key, so this is not needed anymore.")
            
    @steam.command()
    async def applookup(self, appid:int):
        """See what game or app is attached to this mysterious id :O"""
        request = requests.get("https://steamspy.com/api.php?request=appdetails&appid=" + str(appid))
        request = json.loads(request.content.decode("utf-8"))
        await self.bot.say("```fix\nID: {}\nName: {}\nDeveloper: {}\nPublisher: {}\nRank: {}\nOwners: {}\nPrice: ${}.{}```".format(request['appid'], request['name'], request['developer'], request['publisher'], request['score_rank'], request['owners'], int(request['price']) // 100, int(request['price']) % 100))
    
    @steam.command()
    async def top100forever(self):
        """Gives you the top 100 games played by players since march 2009."""
        request = requests.get("https://steamspy.com/api.php?request=top100forever")
        request = json.loads(request.content.decode("utf-8"))
        msg = "```fix\n"
        counter = 1
        for game in request:
            msg += "{}. {}\n".format(str(counter), request[game]['name'])
            counter += 1
            if len(msg) > 1750:
                await self.bot.say(msg + "```")
                msg = "```fix\n"
        await self.bot.say(msg + "```")
        
    @steam.command()
    async def top100in2weeks(self):
        """Gives you the top 100 games played by players since 2 weeks ago."""
        request = requests.get("https://steamspy.com/api.php?request=top100in2weeks")
        request = json.loads(request.content.decode("utf-8"))
        msg = "```fix\n"
        counter = 1
        for game in request:
            msg += "{}. {}\n".format(str(counter), request[game]['name'])
            counter += 1
            if len(msg) > 1750:
                await self.bot.say(msg + "```")
                msg = "```fix\n"
        await self.bot.say(msg + "```")        
    
def check_folders():
    if not os.path.exists("data/steam"):
        print("Creating data/steam folder...")
        os.makedirs("data/steam")
        
def check_files():
    if not os.path.exists("data/steam/key.json"):
        print("Creating data/steam/key.json file...")
        dataIO.save_json("data/steam/key.json", [None])
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Steam(bot))