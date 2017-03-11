import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
import os
from asyncio import sleep

__author__ = "PlanetTeamSpeak"

class Gardener:
    """Plant, harvest and get info on your crops."""

    def __init__(self, bot):
        self.bot = bot
        self.times = {'second': 1, 'minute': 60, 'hour': 3600, 'day': 86400, 'week': 604800, 'month': 18144000}
        self.plants = { 
                    # === VEGETABLES ===
                    'carrots': {'growthtime': 15*self.times['minute'], 'growthtime-worded': '15 minutes', 'item': 'carrot', 'value': 250, 'price': 65},
                    'potatoes': {'growthtime': 15*self.times['minute'], 'growthtime-worded': '15 minutes', 'item': 'potatoe', 'value': 250, 'price': 65},
                    'melon': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'melon', 'value': 1000, 'price': 250},
                    'pumpkin': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'melon', 'value': 1000, 'price': 250},
                    'tomatoes': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'tomatoe', 'value': 500, 'price': 125},
                    'cabbage': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'cabbage', 'value': 500, 'price': 125},
                    'cucumber': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'cucumber', 'value': 750, 'price': 190},
                    'onions': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'onion', 'value': 500, 'price': 125},
                    'broccoli': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'broccoli', 'value': 1000, 'price': 250},
                    'lettuce': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'lettuce', 'value': 750, 'price': 190},
                    'spinach': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'spinach', 'value': 750, 'price': 190},
                    'eggplant': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'eggplant', 'value': 1000, 'price': 250},
                    'cauliflower': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'cauliflower', 'value': 1000, 'price': 250},
                    'peas': {'growthtime': 15*self.times['minute'], 'growthtime-worded': '15 minutes', 'item': 'pea', 'value': 250, 'price': 65},
                    'maize': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'maize', 'value': 1000, 'price': 250},
                    'radish': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'radish', 'value': 500, 'price': 125},
                    'garlic': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'garlic', 'value': 750, 'price': 190},
                    'celery': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'celery', 'value': 500, 'price': 125},
                    'kale': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'kale', 'value': 500, 'price': 125},
                    'sprout': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'sprout', 'value': 500, 'price': 125},
                    'bell pepper': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'bell pepper', 'value': 750, 'price': 190},
                    'asparagus': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'asparagus', 'value': 1000, 'price': 250},
                    'turnip': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'turnip', 'value': 750, 'price': 190},
                    'bean': {'growthtime': 15*self.times['minute'], 'growthtime-worded': '15 minutes', 'item': 'bean', 'value': 250, 'price': 65},
                    'leek': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'leek', 'value': 500, 'price': 125},
                    'zucchini': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'zucchini', 'value': 750, 'price': 190},
                    'artichoke': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'artichoke', 'value': 750, 'price': 190},
                    'chilli pepper': {'growthtime': 15*self.times['minute'], 'growthtime-worded': '15 minutes', 'item': 'chilli pepper', 'value': 250, 'price': 65},
                    'red cabbage': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'red cabbage', 'value': 1000, 'price': 250},
                    # === FRUITS ===
                    'apple tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'apple', 'value': 3000, 'price': 750},
                    'orange tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'orange', 'value': 3000, 'price': 750},
                    'banana tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'banana', 'value': 3000, 'price': 750},
                    'grapevine': {'growthtime': 2*self.times['hour'], 'growthtime-worded': '2 hours', 'item': 'grape', 'value': 2000, 'price': 500},
                    'strawberry bush': {'growthtime': 30*self.times['minute'], 'growthtime-worded': '30 minutes', 'item': 'strawberry', 'value': 500, 'price': 125},
                    'pear tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'pear', 'value': 3000, 'price': 750},
                    'pineapple': {'growthtime': 1*self.times['hour'], 'growthtime-worded': '1 hour', 'item': 'pineapple', 'value': 1000, 'price': 250},
                    'cherry tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'cherry', 'value': 3000, 'price': 750},
                    'lemon tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'lemon', 'value': 3000, 'price': 750}, # why do so many goddamn fruits grow on trees?
                    'peach tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'peach', 'value': 3000, 'price': 750}, # value = (seconds / 60) / 15 * 4
                    'mango tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'mango', 'value': 3000, 'price': 750}, # price = value / 4
                    'berry tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'berry', 'value': 3000, 'price': 750},
                    'watermelon': {'growthtime': 45*self.times['minute'], 'growthtime-worded': '45 minutes', 'item': 'watermelon', 'value': 750, 'price': 190},
                    'grapefruit tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'grapefruit', 'value': 3000, 'price': 750},
                    'kiwi tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'kiwi', 'value': 3000, 'price': 750},
                    'papaya tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'papaya', 'value': 3000, 'price': 750},
                    'pomegranate tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'pomegranate', 'value': 3000, 'price': 750}, 
                    'fig tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'fig', 'value': 3000, 'price': 750},
                    'avocado tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'avocado', 'value': 3000, 'price': 750},
                    'apricot tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'apricot', 'value': 3000, 'price': 750}, # SO MUCH TREES
                    'blackberry bush': {'growthtime': 2*self.times['hour'], 'growthtime-worded': '2 hours', 'item': 'blackberry', 'value': 2000, 'price': 500},
                    'cranberry bush': {'growthtime': 2*self.times['hour'], 'growthtime-worded': '2 hours', 'item': 'cranberry', 'value': 2000, 'price': 500}, # finally a fruit that does not grow on a tree.
                    'cantaloupe bush': {'growthtime': 2*self.times['hour'], 'growthtime-worded': '2 hours', 'item': 'cantaloupe', 'value': 2000, 'price': 500},
                    'palm tree': {'growthtime': 4*self.times['hour'], 'growthtime-worded': '4 hours', 'item': 'coconut', 'value': 4000, 'price': 1000},
                    'passion fruit bush': {'growthtime': 2*self.times['hour'], 'growthtime-worded': '2 hours', 'item': 'passion fruit', 'value': 2000, 'price': 500},
                    'olive tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'olive', 'value': 3000, 'price': 750},
                    'raspberry': {'growthtime': 30*self.times['hour'], 'growthtime-worded': '30 minutes', 'item': 'raspberry', 'value': 500, 'price': 125},
                    'lime tree': {'growthtime': 3*self.times['hour'], 'growthtime-worded': '3 hours', 'item': 'lime', 'value': 3000, 'price': 750},
                    # === REMAINING === 
                    'adobe rainbow': {'growthtime': 1*self.times['week'], 'growthtime-worded': '1 week', 'item': 'adobe rainbow', 'value': 168000, 'price': 42000}
                    }
        self.settings = dataIO.load_json("data/gardener/settings.json")
        self.started = False

    @commands.group(pass_context=True)
    async def garden(self, ctx):
        """Plant, harvest and get info on your crops.
        This is not limited to one server."""
        if not ctx.invoked_subcommand:  
            await self.bot.send_cmd_help(ctx)
            
    @garden.command(pass_context=True)
    async def plant(self, ctx, *, plant):
        """Plant a crop.
        Please do [p]garden plants first to get a list of plants."""
        plant = plant.lower()
        if plant not in self.plants.keys():
            await self.bot.say("That's not a valid plant, for a list of valid plants type {}garden plants.".format(ctx.prefix))
        else:
            bank = self.bot.get_cog('Economy').bank
            user = ctx.message.author
            if ctx.message.author.id not in self.settings['gardeners']:
                self.settings['gardeners'][ctx.message.author.id] = {'plants' : {}, 'items': {}}
            if plant in self.settings['gardeners'][ctx.message.author.id]['plants']:
                await self.bot.say("You already planted that plant, you'll have to wait untill it's ready to harvest.")
            elif not bank.account_exists(user):
                await self.bot.say("You are not registered at the bank, you can register with {}bank register.".format(ctx.prefix))
            elif not bank.can_spend(user, self.plants[plant]['price']):
                await self.bot.say("You cannot afford that plant.")
            else:
                await self.bot.say("Are you sure you want to plant a **{}** for **{} credits**? (yes/no)".format(plant, self.plants[plant]['price']))
                confirm = await self.bot.wait_for_message(author=user, timeout=15)
                if (confirm == None) or (confirm.content.lower() != "yes"):
                    await self.bot.say("K, then not.")
                else:
                    bank.withdraw_credits(user, self.plants[plant]['price'])
                    self.settings['gardeners'][ctx.message.author.id]['plants'][plant] = {'growthtime': self.plants[plant]['growthtime']}
                    self.save_settings()
                    await self.bot.say("A **{}** has been planted, it will take **{}** to grow, you can always get information on the growth status with **{}garden info {}**, you can also buy a growth pulse with **{}garden buy growthpulse 1-3 {}**.".format(plant, self.plants[plant]['growthtime-worded'], ctx.prefix, plant, ctx.prefix, plant))
            
    @garden.command(pass_context=True)
    async def harvest(self, ctx, *, plant):
        """Harvest one of your plants."""
        plant = plant.lower()
        if plant not in self.plants.keys():
            await self.bot.say("That's not a valid plant, for a list of valid plants type {}garden plants.".format(ctx.prefix))
        else:
            if ctx.message.author.id not in self.settings['gardeners']:
                await self.bot.say("You don't have any plants planted to harvest.")
            elif plant not in self.settings['gardeners'][ctx.message.author.id]['plants']:
                await self.bot.say("You didn't plant that plant yet.")
            elif self.settings['gardeners'][ctx.message.author.id]['plants'][plant]['growthtime'] >= 0:
                await self.bot.say("That plant isn't ready to be harvested yet.")
            else:
                if self.plants[plant]['item'] not in self.settings['gardeners'][ctx.message.author.id]['items']:
                    self.settings['gardeners'][ctx.message.author.id]['items'][self.plants[plant]['item']] = {'amount': 1, 'value': self.plants[plant]['value']}
                else:
                    self.settings['gardeners'][ctx.message.author.id]['items'][self.plants[plant]['item']]['amount'] += 1
                del self.settings['gardeners'][ctx.message.author.id]['plants'][plant]
                self.save_settings()
                await self.bot.say("You harvested your **{}**, you got **1 {}** which brings you to a total of **{} {}s**.".format(plant, self.plants[plant]['item'], str(self.settings['gardeners'][ctx.message.author.id]['items'][self.plants[plant]['item']]['amount']), self.plants[plant]['item']))
            
    @garden.command(pass_context=True)
    async def info(self, ctx, *, plant):
        """Get information on one of your planted plants."""
        if plant.lower() not in self.plants.keys():
            await self.bot.say("That's not a valid plant, for a list of valid plants type {}garden plants.".format(ctx.prefix))
        else:
            if ctx.message.author.id not in self.settings['gardeners']:
                await self.bot.say("You don't have any plants planted to get information for.")
            elif plant not in self.settings['gardeners'][ctx.message.author.id]['plants']:
                await self.bot.say("You didn't plant that plant yet.")
            else:
                em = discord.Embed(color=discord.Color.green(), title="Info on {}".format(plant))
                em.add_field(name="Growth time left (seconds)", value=str(self.settings['gardeners'][ctx.message.author.id]['plants'][plant]['growthtime']))
                em.add_field(name="\a", value="\a")
                em.add_field(name="\a", value="\a")
                em.add_field(name="Original growth time", value="{} ({})".format(self.plants[plant]['growthtime-worded'], str(self.plants[plant]['growthtime'])))
                em.add_field(name="Reward", value=self.plants[plant]['item'])
                await self.bot.say(embed=em)
                
    @garden.command(pass_context=True, name="plants")
    async def _plants(self, ctx):
        """Shows you all available plants and the ones you have planted."""
        msg = "```css\nAvailable plants\nPlant\t\t\t\tPrice\tValue\tGrowth time\tItem\n"
        for plant in list(self.plants.keys()):
            msg += "{}{}{}{}{}{}{}{}{}\n".format(plant, " " * (21 - len(plant)), str(self.plants[plant]['price']), " " * (9 - len(str(self.plants[plant]['price']))), str(self.plants[plant]['value']), " " * (9 - len(str(self.plants[plant]['value']))), self.plants[plant]['growthtime-worded'], " " * (15 - len(str(self.plants[plant]['growthtime-worded']))), self.plants[plant]['item'])
            if len(msg) > 1750:
                await self.bot.say(msg + "```")
                msg = "```css\n"
        user = ctx.message.author
        if user.id in self.settings['gardeners']:
            msg += "\nYour plants\nPlant\t\t\t\tTime left\tValue\tItem\n"
            for plant in list(self.settings['gardeners'][user.id]['plants'].keys()):
                msg += "{}{}{}{}{}{}{}\n".format(plant, " " * (21 - len(plant)), str(self.settings['gardeners'][user.id]['plants'][plant]['growthtime']), " " * (12 - len(str(self.plants[plant]['price']))), str(self.plants[plant]['value']), " " * (9 - len(str(self.plants[plant]['value']))), self.plants[plant]['item'])
                if len(msg) > 1750:
                    await self.bot.say(msg + "```")
                    msg = "```css\n"
        await self.bot.say(msg + "```")
            
    @garden.command(pass_context=True)
    async def items(self, ctx):
        """Shows you all the items you have farmed."""
        user = ctx.message.author
        if (user.id not in self.settings['gardeners']) or (self.settings['gardeners'][user.id]['items'] == {}):
            await self.bot.say("You do not have any items.")
        else:
            msg = ""
            for item in self.settings['gardeners'][user.id]['items']:
                msg += "{} {}s\n".format(str(self.settings['gardeners'][user.id]['items'][item]['amount']), item)
            await self.bot.say(embed=discord.Embed(title="Your items", color=discord.Color.green(), description=msg))
            
    @garden.command(pass_context=True)
    async def sell(self, ctx, *, item):
        """Sell an item to get some money."""
        user = ctx.message.author
        bank = self.bot.get_cog('Economy').bank
        if user.id not in self.settings['gardeners']:
            await self.bot.say("You have no items to sell.")
        elif item not in self.settings['gardeners'][user.id]['items']:
            await self.bot.say("You do not have that item.")
        elif not bank.account_exists(user):
            await self.bot.say("You do not have a bank account, you can register with {}bank register.".format(ctx.prefix))
        else:
            bank.deposit_credits(user, self.settings['gardeners'][user.id]['items'][item]['value'])
            await self.bot.say("Successfully deposited **{} credits** to your account and sold **{} {}s**.".format(self.settings['gardeners'][user.id]['items'][item]['value'] * self.settings['gardeners'][user.id]['items'][item]['amount'], self.settings['gardeners'][user.id]['items'][item]['amount'], item))
            del self.settings['gardeners'][user.id]['items'][item]
            self.save_settings()
            
    @garden.group(pass_context=True, name="buy")
    async def buy(self, ctx):
        """Buy items to let your plants grow faster."""
        if ctx.message.content.lower() == "{}garden buy".format(ctx.prefix):
            await self.bot.send_cmd_help(ctx)
            
    @buy.command(pass_context=True)
    async def growthpulse(self, ctx, level:int, *, plant):
        """Buy a growth pulse so you don't have to wait as long.
        
        LEVELS:
        1: 5 minutes, 250 credits
        2: 15 minutes, 500 credits
        3: 1 hour, 1500 credits"""
        bank = self.bot.get_cog('Economy').bank
        user = ctx.message.author
        payments = {1: 250, 2: 500, 3: 1500}
        times = {1: 5*self.times['minute'], 2: 15*self.times['minute'], 3: 1*self.times['hour']}
        if (level > 3) or (level < 1):
            await self.bot.say("The level has to be between 1 and 3.")
        elif not bank.account_exists(user):
            await self.bot.say("You do not have a bank account, you can register yourself with {}bank register.".format(ctx.prefix))
        elif not bank.can_spend(user, payments[level]):
            await self.bot.say("You cannot afford that.")
        elif plant.lower() not in self.plants.keys():
            await self.bot.say("That's not a valid plant, for a list of valid plants type {}garden plants.".format(ctx.prefix))
        elif user.id not in self.settings['gardeners']:
            await self.bot.say("You do not have any plants planted.")
        elif plant not in self.settings['gardeners'][user.id]['plants']:
            await self.bot.say("You do not have that plant planted.")
        else:
            await self.bot.say("Are you sure you want to buy **a growthpulse of level {}** for **{} credits**? (yes/no)".format(level, payments[level]))
            confirm = await self.bot.wait_for_message(author=user, timeout=15)
            if (confirm == None) or (confirm.content.lower() != "yes"):
                await self.bot.say("Okay, then not.")
            else:
                bank.withdraw_credits(user, payments[level])
                self.settings['gardeners'][user.id]['plants'][plant]['growthtime'] -= times[level]
                self.save_settings()
                await self.bot.say("The growth time for **{}** has been successfully lowered by **{}** seconds and is now at **{}** seconds.".format(plant, times[level], self.settings['gardeners'][user.id]['plants'][plant]['growthtime']))
            
    def save_settings(self):
        return dataIO.save_json("data/gardener/settings.json", self.settings)
            
    async def on_command(self, command, ctx):
        if not self.started:
            self.started = True
            counter = 0
            while True:
                for gardener in self.settings['gardeners']:
                    for plant in self.settings['gardeners'][gardener]['plants']:
                        self.settings['gardeners'][gardener]['plants'][plant]['growthtime'] -= 1
                counter += 1
                if counter % 10 == 0: # just so we don't save it every second, but every 10 seconds instead.
                    error = True
                    while error:
                        try:
                            self.save_settings()
                            error = False
                        except:
                            error = True
                await sleep(1)
            
def check_folders():
    if not os.path.exists("data/gardener"):
        print("Creating data/gardener folder...")
        os.makedirs("data/gardener")
        
def check_files():
    if not os.path.exists("data/gardener/settings.json"):
        print("Creating data/gardener/settings.json file...")
        dataIO.save_json("data/gardener/settings.json", {'gardeners': {}})
        
def setup(bot):
    check_folders()
    check_files()
    if bot.get_cog('Economy') == None:
        cogs = dataIO.load_json("data/red/cogs.json")
        if not cogs['cogs.economy']:
            raise RuntimeError("Economy cog has to be loaded, you can load it with [p]load economy.")
        else:
            bot.load_extension("cogs.economy")
    bot.add_cog(Gardener(bot))