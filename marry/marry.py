import discord
from discord.ext import commands
import os
from .utils import checks
from __main__ import settings
from cogs.utils.dataIO import dataIO
import asyncio

class Marry:
    """Marry your loved one."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/marry/settings.json")

    @commands.command(pass_context=True, no_pm=True)
    async def marry(self, ctx, yourlovedone:discord.Member):
        """Now you can finally marry your loved one."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'marry_limit': 0, 'disabled': False}
            self.save_settings()
        if 'disabled' not in self.settings[ctx.message.server.id]:
            self.settings[ctx.message.server.id]['disabled'] = False
            self.save_settings()
        if not self.settings[ctx.message.server.id]['disabled']:
            if yourlovedone.id == ctx.message.author.id:
                await self.bot.say("You can't marry yourself, that would be weird wouldn't it?")
                return
            for role in ctx.message.author.roles:
                if ctx.message.author.name in role.name:
                    if " ❤ " in role.name:
                        if yourlovedone.name in role.name:
                            await self.bot.say("You're already married with this person.")
                            return
            times_married = 0
            if self.settings[ctx.message.server.id]['marry_limit'] is not 0:
                for role in ctx.message.server.roles:
                    if ctx.message.author.name in role.name:
                        if " ❤ " in role.name:
                            times_married = times_married + 1
                if times_married > self.settings[ctx.message.server.id]['marry_limit']:
                    await self.bot.say("You have reached the marry limit ({}).".format(self.settings[ctx.message.server.id]['marry_limit']))
                    return
                times_married = 0
                for role in ctx.message.server.roles:
                    if yourlovedone.name in role.name:
                        if " ❤ " in role.name:
                            times_married = times_married + 1
                if times_married > self.settings[ctx.message.server.id]['marry_limit']:
                    await self.bot.say("Your loved one has reached the marry limit ({}).".format(self.settings[ctx.message.server.id]['marry_limit']))
                    return
            elif yourlovedone.id == ctx.message.server.me.id:
                if ctx.message.author.id != settings.owner:
                    await self.bot.say("I'd only marry my owner.")
                    return
            await self.bot.say("{} do you take {} as your husband/wife? (yes/no)".format(yourlovedone.mention, ctx.message.author.mention))
            answer = await self.bot.wait_for_message(timeout=60, author=yourlovedone)
            if answer is None:
                await self.bot.say("The user you tried to marry didn't respond, I'm sorry.")
                return
            elif "yes" not in answer.content.lower():
                await self.bot.say("The user you tried to marry didn't say yes, I'm sorry.")
                return
            try:
                married_role = await self.bot.create_role(server=ctx.message.server, name="{} ❤ {}".format(ctx.message.author.name, yourlovedone.name), colour=discord.Colour(value=0XFF00EE), hoist=True)
            except discord.Forbidden:
                await self.bot.say("I do not have the `manage roles` permission, you can't marry untill I do.")
                return
            except Exception as e:
                await self.bot.say("Couldn't make your loved role, unknown error occured,\n{}.".format(e))
                return
            await self.bot.add_roles(ctx.message.author, married_role)
            await self.bot.add_roles(yourlovedone, married_role)
            await self.bot.send_message(ctx.message.author, "You married **{0}** in **{1}**\nYour divorce id is `{2}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{3}divorce {2}`.".format(str(yourlovedone), ctx.message.server.name, married_role.id, ctx.prefix))
            if not yourlovedone.bot:
                await self.bot.send_message(yourlovedone, "You married **{0}** in **{1}**\nYour divorce id is `{2}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{3}divorce {2}`.".format(str(ctx.message.author), ctx.message.server.name, married_role.id, ctx.prefix))
            else:
                pass
            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
            if marchan:
                await self.bot.say("You're now married, congratulations!")
                await self.bot.send_message(marchan, "{} married {} congratulations!".format(ctx.message.author.mention, yourlovedone.mention))
            else:
                try:
                    marchan = await self.bot.create_channel(ctx.message.server, "marriage")
                    await self.bot.say("You're now married, congratulations!")
                    await self.bot.send_message(marchan, "{} married {} congratulations!".format(ctx.message.author.mention, yourlovedone.mention))
                except:
                    await self.bot.say("{} married {}, congratulations! I suggest telling the server owner or moderators to make a #marriage channel though.".format(ctx.message.author.mention, yourlovedone.mention))
            return
        else:
            await self.bot.say("Marriages are disabled in this server.")
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def forcemarry(self, ctx, person:discord.Member, lovedone:discord.Member):
        """Now you can finally marry your loved one."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'marry_limit': 0, 'disabled': False}
            self.save_settings()
        if 'disabled' not in self.settings[ctx.message.server.id]:
            self.settings[ctx.message.server.id]['disabled'] = False
            self.save_settings()
        if not self.settings[ctx.message.server.id]['disabled']:
            if lovedone.id == person.id:
                await self.bot.say("You can't let someone marry him/herself that would be weird wouldn't it?")
                return
            for role in person.roles:
                if person.name in role.name:
                    if " ❤ " in role.name:
                        if lovedone.name in role.name:
                            await self.bot.say("This person is already married with his/her loved one.")
                            return
            times_married = 0
            if self.settings[ctx.message.server.id]['marry_limit'] is not 0:
                for role in ctx.message.server.roles:
                    if person.name in role.name:
                        if " ❤ " in role.name:
                            times_married = times_married + 1
                if times_married > self.settings[ctx.message.server.id]['marry_limit']:
                    await self.bot.say("This person has reached the marry limit ({}).".format(self.settings[ctx.message.server.id]['marry_limit']))
                    return
                times_married = 0
                for role in ctx.message.server.roles:
                    if lovedone.name in role.name:
                        if " ❤ " in role.name:
                            times_married = times_married + 1
                if times_married > self.settings[ctx.message.server.id]['marry_limit']:
                    await self.bot.say("This person's loved one has reached the marry limit ({}).".format(self.settings[ctx.message.server.id]['marry_limit']))
                    return
            elif person.id == ctx.message.server.me.id:
                if lovedone.id is not settings.owner:
                    await self.bot.say("I'd only marry my owner.")
                    return
            elif lovedone.id == ctx.message.server.me.id:
                if person.id is not settings.owner:
                    await self.bot.say("I'd only marry my owner.")
                    return
            try:
                married_role = await self.bot.create_role(server=ctx.message.server, name="{} ❤ {}".format(person.name, lovedone.name), colour=discord.Colour(value=0XFF00EE), hoist=True)
            except discord.Forbidden:
                await self.bot.say("I do not have the `manage roles` permission, you can't marry untill I do.")
                return
            except Exception as e:
                await self.bot.say("Couldn't make your loved role, unknown error occured,\n{}.".format(e))
                return
            await self.bot.add_roles(person, married_role)
            await self.bot.add_roles(lovedone, married_role)
            try:
                await self.bot.send_message(person, "**{0}** married you to **{1}** in **{2}**.\nYour divorce id is `{3}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{4}divorce {3}`.".format(ctx.message.author.name, str(lovedone), ctx.message.server.name, married_role.id, ctx.prefix))
            except:
                pass
            try:
                await self.bot.send_message(lovedone, "**{0}** married you to **{1}** in **{2}**.\nYour divorce id is `{3}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{4}divorce {3}`.".format(ctx.message.author.name, str(person), ctx.message.server.name, married_role.id, ctx.prefix))
            except:
                pass
            else:
                pass
            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
            if marchan:
                await self.bot.say("They're now married, congratulations!")
                await self.bot.send_message(marchan, "{} was forced to marry {}.".format(person.mention, lovedone.mention))
            else:
                try:
                    marchan = await self.bot.create_channel(ctx.message.server, "marriage")
                    await self.bot.say("They're now married, congratulations!")
                    await self.bot.send_message(marchan, "{} was forced to marry {}.".format(person.mention, lovedone.mention))
                except:
                    await self.bot.say("{} married {}, congratulations! I suggest telling the server owner or moderators to make a #marriage channel though.".format(person.mention, lovedone.mention))
            return
        else:
            await self.bot.say("Marriages are disabled in this server.")
        
    @commands.command(pass_context=True, no_pm=True)
    async def divorce(self, ctx, divorce_id):
        """Divorce your ex."""
        try:
            married_role = getRoleObj(divorce_id, ctx.message.server)
            if not "❤" in married_role.name.split():
                await self.bot.say("That's not a valid ID.")
                return
            elif not ctx.message.author.name in married_role.name.split():
                await self.bot.say("That's not a valid ID")
            else:
                pass
            await self.bot.delete_role(ctx.message.server, married_role)
            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
            if marchan:
                await self.bot.say("You're now divorced.")
                await self.bot.send_message(marchan, "{} divorced ID `{}`.".format(ctx.message.author.mention, divorce_id))
            else:
                try:
                    marchan = await self.bot.create_channel(ctx.message.server, "marriage")
                    await self.bot.say("You're now divorced.")
                    await self.bot.send_message(marchan, "{} divorced ID `{}`.".format(ctx.message.author.mention, divorce_id))
                except:
                    await self.bot.say("You're now divorced! I suggest telling the server owner or moderators to make a #marriage channel though.")
                    return
        except discord.Forbidden:
            await self.bot.say("I do not have the `manage roles` permission, I need it to divorce you.")
            return
        except:
            await self.bot.say("That's not a valid ID.")
            return
            
    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def setmarrylimit(self, ctx, times:int):
        """Sets the limit someone can marry someone. 0 is unlimited."""
        self.settings[ctx.message.server.id] = {'marry_limit': times}
        self.save_settings()
        await self.bot.say("Done!")
       
    @commands.command(pass_context=True, no_pm=True)
    async def marrylimit(self, ctx):
        """Shows you the current marrylimit."""
        if (ctx.message.server.id not in self.settings) or ("marrylimit" not in self.settings[ctx.message.server.id]):
            await self.bot.say("There is no marry limit.")
        elif self.settings[ctx.message.server.id]['marrylimit'] == 0:
            await self.bot.say("There is no marry limit.")
        else:
            await self.bot.say("The marry limit is {}.".format(self.settings[ctx.message.server.id]['marrylimit']))
        
    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def massdivorce(self, ctx):
        """Divorces everyone on the server."""
        await self.bot.say("Are you sure you want to divorce everyone on the server? (yes/no)")
        answer = await self.bot.wait_for_message(timeout=15, author=ctx.message.author)
        if answer is None:
            await self.bot.say("K then not.")
            return
        elif "yes" in answer.content.lower():
            divorced = 0
            for role in ctx.message.server.roles:
                if " ❤ " in role.name:
                    try:
                        await self.bot.delete_role(role=role, server=ctx.message.server)
                        divorced = divorced + 1
                    except:
                        pass
            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
            if marchan:
                await self.bot.say("Done! Divorced {} couples.".format(divorced))
                await self.bot.send_message(marchan, "{} divorced everyone ({} couples).".format(ctx.message.author.mention, divorced))
            else:
                try:
                    marchan = await self.bot.create_channel(ctx.message.server, "marriage")
                    await self.bot.say("Done! Divorced {} couples.".format(divorced))
                    await self.bot.send_message(marchan, "{} divorced everyone ({} couples).".format(ctx.message.author.mention, divorced))
                except:
                    await self.bot.say("Done! Everyone has been divorced. I suggest telling the server owner or moderators to make a #marriage channel though.")
                    return
        else:
            await self.bot.say("K then not.")
            return
            
    @commands.command(pass_context=True, no_pm=True)
    async def marrycount(self, ctx):
        """Counts all the married couples in this server."""
        count = 0
        for role in ctx.message.server.roles:
            if " ❤ " in role.name:
                count += 1
        if count == 1:
            await self.bot.say("There is currently {} married couple in this server.".format(count))
        else:
            await self.bot.say("There are currently {} married couples in this server.".format(count))
            
    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions()
    async def admindivorce(self, ctx, person, person2):
        """Divorces someone by NAME. If the name is bigger than one word put quotes around it
        Example: "much name, such words"."""
        for role in ctx.message.server.roles:
            if person in role.name:
                if " ❤ " in role.name:
                    if person2 in role.name:
                        try:
                            await self.bot.delete_role(ctx.message.server, role)
                            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
                            if marchan:
                                await self.bot.send_message(marchan, "{} admindivorced {} and {}.".format(ctx.message.author.name, person, person2))
                            else:
                                marchan = self.bot.create_channel(ctx.message.server, "marriage")
                                await self.bot.send_message(marchan, "{} admindivorced {} and {}.".format(ctx.message.author.name, person, person2))
                            await self.bot.say("Succesfully divorced {} and {}.".format(person, person2))
                            return
                        except:
                            await self.bot.say("The role for the marriage was found but could not be deleted.")
                            return
        await self.bot.say("The role of that marriage could not be found.")
        
    @commands.command(pass_context=True)
    @checks.admin_or_permissions()
    async def togglemarriage(self, ctx):
        """Toggles if members of your server should be able to marry each other using [p]marry."""
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'marrylimit': 0, 'disabled': False}
        if not self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = True
            await self.bot.say("Members can no longer marry each other anymore.")
        else:
            self.settings[ctx.message.server.id]['disabled'] = False
            await self.bot.say("Members can once again marry each other.")
        self.save_settings()
        
    def save_settings(self):
        dataIO.save_json("data/marry/settings.json", self.settings)
            
def getRoleObj(roleID, server):
    for role in server.roles:
        if role.id == roleID:
            return role
        
def check_folders():
    if not os.path.exists("data/marry"):
        print("Creating data/marry folder...")
        os.makedirs("data/marry")
    if not os.path.exists("data/marry/images"):
        print("Creating data/marry/images folder...")
        os.makedirs("data/marry/images")
        
def check_files():
    if not os.path.exists("data/marry/settings.json"):
        print("Creating data/marry/settings.json file...")
        dataIO.save_json("data/marry/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Marry(bot))