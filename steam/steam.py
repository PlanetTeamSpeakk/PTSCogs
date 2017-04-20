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
    async def getuserinfo(self, ctx, *, username):
        """Get an user's information with their name, not nickname, name. Or Steam 64 ID, whichever you prefer."""
        if self.key != None:
            if " " in username:
                await self.bot.say("Unfortunately, Steam API has this little bug that doesn't allow spaces in usernames, nothing I or my owner can do about it.")
                return
            status = await self.bot.say("Gathering data, please stand by...")
            if username.isdigit():
                userid = username
            else:
                request = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + self.key + "&vanityurl=" + username)
                request = json.loads(request.content.decode("utf-8"))['response']
                if request['success'] == 42:
                    await self.bot.edit_message(status, "That's not a valid username.")
                    return
                else:
                    userid = request['steamid']
            request = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + self.key + "&steamids=" + str(userid))
            request = json.loads(request.content.decode("utf-8"))['response']['players']
            if request == []:
                await self.bot.edit_message(status, "That's not a valid id.")
            else:
                request = request[0]
                request['games'] = json.loads(requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.key + "&steamid=" + str(userid)).content.decode("utf-8"))['response']
                games = []
                gamelist = []
                for game in range(len(request['games']['games'])):
                    games.append(str(request['games']['games'][game]['appid']))
                gamerequest = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
                gamerequest = json.loads(gamerequest.content.decode("utf-8"))['applist']['apps']
                for game in games:
                    for i in range(len(gamerequest)):
                        if int(gamerequest[i]['appid']) == int(game):
                            gamelist.append("\t{} ({})\n".format(gamerequest[i]['name'], game))
                msg = "```fix\nUsername: {}\nSteam ID: {}\nProfile URL: {}\nAvatar: {}\nGame count: {}\nGames owned:\n".format(request['personaname'], str(request['steamid']), request['profileurl'], request['avatarfull'], str(request['games']['game_count']))
                for game in gamelist:
                    msg += game
                    if len(msg) > 1750:
                        await self.bot.say(msg + "```")
                        msg = "```fix\n"
                await self.bot.delete_message(status)
                await self.bot.say(msg + "```")
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
    async def applookup(self, *, app):
        """See what game or app is attached to this mysterious id :O, or just use a name, whatever you like."""
        if app.isdigit():
            request = requests.get("https://steamspy.com/api.php?request=appdetails&appid=" + str(app))
            request = json.loads(request.content.decode("utf-8"))
            if request['name'] == None:
                await self.bot.say("Could not find a game with that ID.")
                return
        else:
            request = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
            request = json.loads(request.content.decode("utf-8"))['applist']['apps']
            found = False
            for game in range(len(request)):
                if request[game]['name'].lower() == app.lower():
                    request = requests.get("https://steamspy.com/api.php?request=appdetails&appid=" + str(request[game]['appid']))
                    request = json.loads(request.content.decode("utf-8"))
                    found = True
                    if request['name'] == None:
                        await self.bot.say("This game or app is too new, could not find any data.")
                        return
                    break
            if not found:
                await self.bot.say("Could not find that game.")
                return
        await self.bot.say("```fix\nID: {}\nName: {}\nDeveloper: {}\nPublisher: {}\nOwners: {}\nUrl: https://store.steampowered.com/app/{}\nPrice: ${}.{}```".format(request['appid'], request['name'], request['developer'], request['publisher'], request['owners'], request['appid'], int(request['price']) // 100, int(request['price']) % 100))
    
    @steam.command()
    async def top100forever(self):
        """Gives you the top 100 games played by players since march 2009."""
        request = requests.get("https://steamspy.com/api.php?request=top100forever")
        request = json.loads(request.content.decode("utf-8"))
        msg = "```fix\n"
        counter = 1
        for game in range(len(list(request.keys()))):
            game = list(request.keys())[game]
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
        for game in range(len(list(request.keys()))):
            game = list(request.keys())[game]
            msg += "{}. {}\n".format(str(counter), request[game]['name'])
            counter += 1
            if len(msg) > 1750:
                await self.bot.say(msg + "```")
                msg = "```fix\n"
        await self.bot.say(msg + "```")
        
    @steam.command()
    async def appcount(self):
        """Counts the amount of apps and games on Steam."""
        request = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
        request = json.loads(request.content.decode("utf-8"))['applist']['apps']
        await self.bot.say("```fix\nThere are currently {} apps and games on Steam (latest game: {}).```".format(len(request), request[len(request) - 1]['name']))
    
    @steam.command(alliases=['getscgostats'])
    async def getcsgostats(self, *, username):
        """Get CS:GO stats from a user.
        Example:
        [p]steam getcsgostats PlanetTeamSpeak (Warning: I am noob)
        [p]steam getcsgostats 76561198187354157 (Same user but with Steam 64 ID)"""
        status = await self.bot.say("Getting data, please stand by...")
        if not username.isdigit():
            request = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={}&vanityurl={}".format(self.key, username))
            request = json.loads(request.content.decode("utf-8"))['response']
            if request['success'] == 42:
                await self.bot.edit_message(status, "That's not a valid user ID.")
                return
            else:
                userid = request['steamid']
                username = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(self.key, userid)).json()['response']['players'][0]['personaname']
        request = requests.get("http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={}&steamid={}".format(self.key, userid)).json()['playerstats']['stats']
        if request == {}:
            await self.bot.edit_message(status, "That's not a valid username or this user has no CS:GO.")
        else:
            requestCopy = request.copy()
            request = {}
            for i in range(len(requestCopy)):
                request[requestCopy[i]['name']] = requestCopy[i]['value']
            await self.bot.edit_message(status, "```fix\nUsername: {}\nUser ID: {}\nTotal kills: {}\nTotal deaths: {}\nKDR: {}\nTotal time played: {}\nTotal bombs planted: {}\nTotal wins: {}\nTotal damage done: {}\nTotal money earned: {}\nHeadshots done: {}\nTotal shots fired: {}\nTotal shots hit: {}\nHit ratio: {}\nTotal rounds played: {}```".format(
            username, userid, request['total_kills'], request['total_deaths'], request['total_kills'] / request['total_deaths'], self.secondsToText(request['total_time_played']), request['total_planted_bombs'], request['total_wins'], request['total_damage_done'], request['total_money_earned'], request['total_kills_headshot'], request['total_shots_fired'], request['total_shots_hit'], request['total_shots_fired'] / request['total_shots_hit'], request['total_rounds_played']))
        
    # http://bit.ly/2ofiay3
    def secondsToText(self, secs):
        days = secs//86400
        hours = (secs - days*86400)//3600
        minutes = (secs - days*86400 - hours*3600)//60
        seconds = secs - days*86400 - hours*3600 - minutes*60
        result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
        ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
        ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
        ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
        return result
        
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