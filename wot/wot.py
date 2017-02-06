import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
import os
import requests
import json
from datetime import datetime
from .utils import checks

class WorldofTanks:
    """Get user information from World of Tanks."""

    def __init__(self, bot):
        self.bot = bot
        self.key = dataIO.load_json("data/wot/key.json")['key']
        self.servers = {'eu': 'eu', 'ru': 'ru', 'asia': 'asia', 'na': 'com', 'kr': 'kr'}
        
    @commands.group(pass_context=True)
    async def wot(self, ctx):
        """Get some user or tankinfo from wot."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        
    @wot.command()
    @checks.is_owner()
    async def setapikey(self, key):
        """Set the api key to use can be obtained here https://developers.wargaming.net/applications/"""
        self.key = key
        dataIO.save_json("data/wot/key.json", {'key': self.key})
        await self.bot.say("API key set!")
        
    @wot.command(pass_context=True)
    async def getuserinfo(self, ctx, user, server):
        """Get some info from a user."""
        if self.key != None:
            server = server.lower()
            if server not in self.servers:
                await self.bot.say("That's not a valid server, you can pick from {}.".format(", ".join(list(self.servers.keys()))))
            else:
                server = self.servers[server]
                request = requests.get("https://api.worldoftanks." + server + "/wot/account/list/?application_id=" + self.key + "&search=" + user)
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
        """Do a tank lookup, full name of the tanks, not short names."""
        if self.key != None:
            msg = await self.bot.say("Getting data for **{}**.".format(tank))
            request = requests.get("https://api.worldoftanks.com/wot/encyclopedia/tanks/?application_id=" + self.key)
            request = json.loads(request.content.decode("utf-8"))['data']
            found = False
            for tankID in request:
                if request[tankID]['name_i18n'].lower() == tank.lower():
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
                await self.bot.edit_message(msg, "**```fix\nTank ID: {}\nTank name: {}\nEngine power: {}\nVision radius: {} (metres)\nMax gun penetration: {} (mm)\nMax health: {}\nWeight (tonnes): {}\nRadio distance: {}\nTank type: {}\nChassis rotation speed (degrees per second): {}\nGun name: {}\nMax ammo: {}\nNation: {}\nTurret rotation speed: {}\nGold price: {}\nCredit price: {}\nXp price: {}\nSpeed limit: {}\nMax damage: {}\n```**"
                "".format(str(tank), request['name_i18n'], str(request['engine_power']), str(request['circular_vision_radius']), str(request['gun_piercing_power_max']), str(request['max_health']), str(request['weight']), str(request['radio_distance']), request['type_i18n'], str(request['chassis_rotation_speed']), request['gun_name'], str(request['gun_max_ammo']), request['nation_i18n'], str(request['turret_rotation_speed']), request['price_gold'], request['price_credit'], str(request['price_xp']), str(request['speed_limit']), str(request['gun_damage_max'])))
        
def check_folders():
    if not os.path.exists("data/wot"):
        print("Creating data/wot folder...")
        os.makedirs("data/wot")
        
def check_files():
    if not os.path.exists("data/wot/key.json"):
        print("Creating data/wot/key.json file...")
        dataIO.save_json("data/wot/key.json", {'key': None})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(WorldofTanks(bot))