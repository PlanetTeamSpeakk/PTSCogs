import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os
import requests
import json
from datetime import datetime
from .utils import checks

class Wargaming:
    """Get user information from games by Wargaming."""

    def __init__(self, bot):
        self.bot = bot
        self.key = dataIO.load_json("data/wargaming/key.json")['key']
        self.servers = {'eu': 'eu', 'ru': 'ru', 'asia': 'asia', 'na': 'com', 'kr': 'kr'}
        
    @commands.group(pass_context=True)
    async def wot(self, ctx):
        """Get some user or tankinfo from wot."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        
    @commands.command()
    @checks.is_owner()
    async def setapikey(self, key):
        """Set the api key to use can be obtained here https://developers.wargaming.net/applications/"""
        self.key = key
        dataIO.save_json("data/wargaming/key.json", {'key': self.key})
        await self.bot.say("API key set!")
        
    @wot.command(pass_context=True)
    async def getuserinfo(self, ctx, user, server):
        """Get some info from a user.
        Example:
        [p]wows getuserinfo DiamondCrusher EU"""
        if self.key != None:
            server = server.lower()
            if server not in self.servers:
                await self.bot.say("That's not a valid server, you can pick from {}.".format(", ".join(list(self.servers.keys()))))
            else:
                server = self.servers[server]
                request = requests.get("https://api.worldofwarships." + server + "/wows/account/list/?application_id=" + self.key + "&search=" + user)
                request = json.loads(request.content.decode("utf-8"))
                if 'error' in request:
                    await self.bot.say("An error occured while getting the user information: {}, {}".format(request['error']['code'], request['error']['message']))
                elif request['meta']['count'] == 0:
                    await self.bot.say("Found no results.")
                elif request['meta']['count'] > 1:
                    users = {}
                    for user in range(len(request['data'])):
                        users[user] = {'username': request['data'][user]['nickname'], 'id': request['data'][user]['account_id']}
                    msg = ""
                    for i in list(users.keys()):
                        msg += "{}. {}\n".format(i, users[i]['username'])
                    await self.bot.say("Found a lot results, please pick one:\n{}".format(msg))
                    response = await self.bot.wait_for_message(timeout=15, author=ctx.message.author)
                    if response == None:
                        await self.bot.say("Didn't get a reaction.")
                    elif int(response.content) in users:
                        user = users[int(response.content)]['id']
                        msg = await self.bot.say("Gathering data for **{}**...".format(users[int(response.content)]['username']))
                        request = requests.get("https://api.worldofwarships." + server + "/wows/account/info/?application_id=" + self.key + "&account_id=" + str(user))
                        request = json.loads(request.content.decode("utf-8"))['data'][str(user)]
                        username = request['nickname']
                        global_rating = request['global_rating']
                        client_language = request['client_language']
                        last_battle_time = request['last_battle_time']
                        created_at = request['created_at']
                        request = request['statistics']['all']
                        request['nickname'] = username
                        request['global_rating'] = global_rating
                        request['client_language'] = client_language
                        request['last_battle_time'] = last_battle_time
                        request['created_at'] = created_at
                        await self.bot.edit_message(msg, "**```fix\nUser ID: {}\nUsername: {}\nCreated at: {} (DD/MM/YY)\nLast battle: {} (DD/MM/YY)\nGlobal rating: {}\nClient language: {}\nSpotted: {}\nMax xp earned: {}\nAverage damage blocked: {}\nDirect hits received: {}\nAmmoracked someone: {}\nPenetrations received: {}\nPenetrations done: {}\nHits: {}\nHit percentage: {}\nFree xp: {}\nBattles done: {}\nSurived battles: {}\nBattles won: {}\nBattles lost: {}\nBattles drawn: {}\nDropped capture points: {}\nTotal damage dealt: {}```**"
                        "".format(str(user), request['nickname'], datetime.fromtimestamp(request['created_at']).strftime("%d/%m/%Y %X"), datetime.fromtimestamp(request['last_battle_time']).strftime("%d/%m/%Y %X"), request['global_rating'], request['client_language'], request['spotted'], request['max_xp'], request['avg_damage_blocked'], request['direct_hits_received'], request['explosion_hits'], request['piercings_received'], request['piercings'], request['hits'], request['hits_percents'], request['xp'], request['battles'], request['survived_battles'], request['wins'], request['losses'], request['draws'], request['dropped_capture_points'], request['damage_dealt']))
                    else:
                        await self.bot.say("That's not a valid option.")
                elif request['meta']['count'] == 1:
                    user = request['data'][0]['account_id']
                    msg = await self.bot.say("Gathering data for **{}**...".format(request['data'][0]['nickname']))
                    request = requests.get("https://api.worldoftanks." + server + "/wot/account/info/?application_id=" + self.key + "&account_id=" + str(user))
                    request = json.loads(request.content.decode("utf-8"))['data'][str(user)]
                    username = request['nickname']
                    global_rating = request['global_rating']
                    client_language = request['client_language']
                    last_battle_time = request['last_battle_time']
                    created_at = request['created_at']
                    request = request['statistics']['all']
                    request['nickname'] = username
                    request['global_rating'] = global_rating
                    request['client_language'] = client_language
                    request['last_battle_time'] = last_battle_time
                    request['created_at'] = created_at
                    await self.bot.edit_message(msg, "**```fix\nUser ID: {}\nUsername: {}\nCreated at: {}(DD/MM/YY)\nLast battle: {} (DD/MM/YY)\nGlobal rating: {}\nClient language: {}\nSpotted: {}\nMax xp earned: {}\nAverage damage blocked: {}\nDirect hits received: {}\nAmmoracked someone: {}\nPenetrations received: {}\nPenetrations done: {}\nHits: {}\nHit percentage: {}\nFree xp: {}\nBattles done: {}\nSurived battles: {}\nBattles won: {}\nBattles lost: {}\nBattles drawn: {}\nDropped capture points: {}\nTotal damage dealt: {}```**"
                    "".format(str(user), request['nickname'], datetime.fromtimestamp(request['created_at']).strftime("%d/%m/%Y %X"), datetime.fromtimestamp(request['last_battle_time']).strftime("%d/%m/%Y %X"), request['global_rating'], request['client_language'], request['spotted'], request['max_xp'], request['avg_damage_blocked'], request['direct_hits_received'], request['explosion_hits'], request['piercings_received'], request['piercings'], request['hits'], request['hits_percents'], request['xp'], request['battles'], request['survived_battles'], request['wins'], request['losses'], request['draws'], request['dropped_capture_points'], request['damage_dealt']))
        else:
            await self.bot.say("My owner hasn't set an API key yet.")
        
    @wot.command()
    async def gettankinfo(self, *, tank):
        """Do a tank lookup, short name of the tanks."""
        if self.key != None:
            msg = await self.bot.say("Getting data for **{}**.".format(tank))
            request = requests.get("https://api.worldoftanks.com/wot/encyclopedia/tanks/?application_id=" + self.key)
            request = json.loads(request.content.decode("utf-8"))['data']
            found = False
            for tankID in request:
                if request[tankID]['short_name_i18n'].lower() == tank.lower():
                    tank = tankID
                    found = True
                    break
            if not found:
                await self.bot.edit_message(msg, "Could not find that tank.")
                return
            request = requests.get("https://api.worldoftanks.com/wot/encyclopedia/tankinfo/?application_id=" + self.key + "&tank_id=" + str(tank))
            request = json.loads(request.content.decode("utf-8"))['data']
            if request[tank] == None: # just because.
                await self.bot.say("No data found for that tank.")
            else:
                request = request[tank]
                await self.bot.edit_message(msg, "**```fix\nTank ID: {}\nTank name: {}\nTier: {}\nEngine power: {}\nVision radius: {} (metres)\nMax gun penetration: {} (mm)\nMax health: {}\nWeight (tonnes): {}\nRadio distance: {}\nTank type: {}\nChassis rotation speed (degrees per second): {}\nGun name: {}\nMax ammo: {}\nNation: {}\nTurret rotation speed: {}\nGold price: {}\nCredit price: {}\nXp price: {}\nSpeed limit: {}\nMax damage: {}\n```**"
                "".format(str(tank), request['name_i18n'], str(request['level']), str(request['engine_power']), str(request['circular_vision_radius']), str(request['gun_piercing_power_max']), str(request['max_health']), str(request['weight']), str(request['radio_distance']), request['type_i18n'], str(request['chassis_rotation_speed']), request['gun_name'], str(request['gun_max_ammo']), request['nation_i18n'], str(request['turret_rotation_speed']), request['price_gold'], request['price_credit'], str(request['price_xp']), str(request['speed_limit']), str(request['gun_damage_max'])))
        
    @commands.group(pass_context=True)
    async def wows(self, ctx):
        """Get some user or shipinfo from wows."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        
    @wows.command(pass_context=True)
    async def getuserinfo(self, ctx, user, server):
        """Get some info from a user.
        Example:
        [p]wows getuserinfo DiamondCrusher EU"""
        if self.key != None:
            server = server.lower()
            if server not in self.servers:
                await self.bot.say("That's not a valid server, you can pick from {}.".format(", ".join(list(self.servers.keys()))))
            else:
                server = self.servers[server]
                request = requests.get("https://api.worldofwarships." + server + "/wows/account/list/?application_id=" + self.key + "&search=" + user)
                request = json.loads(request.content.decode("utf-8"))
                if 'error' in request:
                    await self.bot.say("An error occured while getting the user information: {}, {}".format(request['error']['code'], request['error']['message']))
                elif request['meta']['count'] == 0:
                    await self.bot.say("Found no results.")
                elif request['meta']['count'] > 1:
                    users = {}
                    for user in range(len(request['data'])):
                        users[user] = {'username': request['data'][user]['nickname'], 'id': request['data'][user]['account_id']}
                    msg = ""
                    for i in list(users.keys()):
                        msg += "{}. {}\n".format(i, users[i]['username'])
                    await self.bot.say("Found a lot results, please pick one:\n{}".format(msg))
                    response = await self.bot.wait_for_message(timeout=15, author=ctx.message.author)
                    if response == None:
                        await self.bot.say("Didn't get a reaction.")
                    elif int(response.content) in users:
                        user = users[int(response.content)]['id']
                        msg = await self.bot.say("Gathering data for **{}**...".format(request['data'][0]['nickname']))
                        request = requests.get("https://api.worldofwarships." + server + "/wows/account/info/?application_id=" + self.key + "&account_id=" + str(user))
                        request = json.loads(request.content.decode("utf-8"))['data'][str(user)]
                        username = request['nickname']
                        last_battle_time = request['last_battle_time']
                        created_at = request['created_at']
                        request = request['statistics']['pvp']
                        request['nickname'] = username
                        request['last_battle_time'] = last_battle_time
                        request['created_at'] = created_at
                        request['winrate'] = (100 / request['battles']) * request['wins']
                        await self.bot.edit_message(msg, "**```fix\nUser ID: {}\nUsername: {}\nCreated at: {}(DD/MM/YY)\nLast battle: {} (DD/MM/YY)\nMax xp earned in a battle: {}\nSpotted: {}\nFrags: {}\nTotal xp earned untill now: {}\nBattles done: {}\nSurived battles: {}\nBattles won: {}\nBattles lost: {}\nBattles drawn: {}\nWin rate (percent): {}\nTotal damage dealt: {}\nProfile URL: {}```**"
                        "".format(str(user), request['nickname'], datetime.fromtimestamp(request['created_at']).strftime("%d/%m/%Y %X"), datetime.fromtimestamp(request['last_battle_time']).strftime("%d/%m/%Y %X"), request['max_xp'], request['ships_spotted'], request['frags'], request['xp'], request['battles'], request['survived_battles'], request['wins'], request['losses'], request['draws'], request['winrate'], request['damage_dealt'], "https://worldofwarships." + server + "/en/community/accounts/" + str(user) + "-" + request['nickname']))
                    else:
                        await self.bot.say("That's not a valid option.")
                elif request['meta']['count'] == 1:
                    user = request['data'][0]['account_id']
                    msg = await self.bot.say("Gathering data for **{}**...".format(request['data'][0]['nickname']))
                    request = requests.get("https://api.worldofwarships." + server + "/wows/account/info/?application_id=" + self.key + "&account_id=" + str(user))
                    request = json.loads(request.content.decode("utf-8"))['data'][str(user)]
                    username = request['nickname']
                    last_battle_time = request['last_battle_time']
                    created_at = request['created_at']
                    request = request['statistics']['pvp']
                    request['nickname'] = username
                    request['last_battle_time'] = last_battle_time
                    request['created_at'] = created_at
                    request['winrate'] = (100 / request['battles']) * request['wins']
                    await self.bot.edit_message(msg, "**```fix\nUser ID: {}\nUsername: {}\nCreated at: {}(DD/MM/YY)\nLast battle: {} (DD/MM/YY)\nMax xp earned in a battle: {}\nSpotted: {}\nFrags: {}\nTotal xp earned untill now: {}\nBattles done: {}\nSurived battles: {}\nBattles won: {}\nBattles lost: {}\nBattles drawn: {}\nWin rate (percent): {}\nTotal damage dealt: {}\nProfile URL: {}```**"
                    "".format(str(user), request['nickname'], datetime.fromtimestamp(request['created_at']).strftime("%d/%m/%Y %X"), datetime.fromtimestamp(request['last_battle_time']).strftime("%d/%m/%Y %X"), request['max_xp'], request['ships_spotted'], request['frags'], request['xp'], request['battles'], request['survived_battles'], request['wins'], request['losses'], request['draws'], request['winrate'], request['damage_dealt'], "https://worldofwarships." + server + "/en/community/accounts/" + str(user) + "-" + request['nickname']))
        else:
            await self.bot.say("My owner hasn't set an API key yet.")
        
    @wows.command()
    async def getshipinfo(self, *, ship):
        """Do a ship lookup."""
        if self.key != None:
            msg = await self.bot.say("Getting data for **{}**.".format(ship))
            request = requests.get("https://api.worldofwarships.eu/wows/encyclopedia/ships/?application_id=" + self.key)
            request = json.loads(request.content.decode("utf-8"))['data']
            found = False
            for shipID in request:
                if request[shipID]['name'].lower() == ship.lower():
                    ship = shipID
                    found = True
                    break
            if not found:
                await self.bot.edit_message(msg, "Could not find that ship.")
                return
            
            else:
                request = request[ship]
                await self.bot.edit_message(msg, "**```fix\nShip ID: {}\nShip name: {}\nNation: {}\nDescription: {}\nTier: {}\nEngine power: {}\nMax health: {}\nShip type: {}\nCredit price: {}\nGold price: {}```**"
                "".format(str(ship), 
                request['name'],
                request['nation'],
                request['description'],
                str(request['tier']), 
                str(request['default_profile']['engine']['max_speed']), 
                str(request['default_profile']['hull']['health']), 
                request['type'], 
                str(request['price_credit']),
                str(request['price_gold'])))
        
def check_folders():
    if not os.path.exists("data/wargaming"):
        print("Creating data/wargaming folder...")
        os.makedirs("data/wargaming")
        
def check_files():
    if not os.path.exists("data/wargaming/key.json"):
        print("Creating data/wargaming/key.json file...")
        dataIO.save_json("data/wargaming/key.json", {'key': None})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Wargaming(bot))