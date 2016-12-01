import discord
from discord.ext import commands
import os
from .utils import checks
from __main__ import settings
import asyncio

class marry:
    """Marry your loved one."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def marry(self, ctx, yourlovedone:discord.Member):
        """Now you can finally marry your loved one."""
        if yourlovedone.id == self.bot.user.id:
            if ctx.message.author.id != settings.owner:
                await self.bot.say("I only marry my owner!")
                return
            else:
                pass
        else:
            pass
        if yourlovedone.id == ctx.message.author.id:
            await self.bot.say("You can't marry yourself, that would be weird wouldn't it?")
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
        await self.bot.send_message(ctx.message.author, "Your divorce id is `{0}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{1}divorce {0}`.".format(married_role.id, ctx.prefix))
        if not yourlovedone.bot:
            await self.bot.send_message(yourlovedone, "Your divorce id is `{0}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{1}divorce {0}`.".format(married_role.id, ctx.prefix))
        else:
            pass
        marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels, type=discord.ChannelType.text)
        if marchan:
            await self.bot.say("You're now married, congratulations!")
            await self.bot.send_message(marchan, "{} married {} congratulations!".format(ctx.message.author.mention, yourlovedone.mention))
        else:
            await self.bot.say("{} married {}, congratulations! I suggest telling the server owner or moderators to make a #marriage channel though.".format(ctx.message.author.mention, yourlovedone.mention))
            return
        
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def forcemarry(self, ctx, person:discord.Member, lovedone:discord.Member):
        """Now you can finally marry your loved one."""
        if lovedone.id == self.bot.user.id:
            if person.id != settings.owner:
                await self.bot.say("I only marry my owner!")
                return
            else:
                pass
        else:
            pass
        if person.id == self.bot.user.id:
            if lovedone.id != settings.owner:
                await self.bot.say("I only marry my owner!")
                return
            else:
                pass
        else:
            pass
        if lovedone.id == person.id:
            await self.bot.say("You can't let someone marry him/herself that would be weird wouldn't it?")
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
        if not person.bot:
            await self.bot.send_message(person, "**{0}** married you to **{1}**.\nYour divorce id is `{2}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{3}divorce {2}`.".format(ctx.message.author.name, lovedone.name, married_role.id, ctx.prefix))
        else:
            pass
        if not lovedone.bot:
            await self.bot.send_message(lovedone, "**{0}** married you to **{1}**.\nYour divorce id is `{2}`, don't ever give this to anyone or they can divorce you!\nTo divorce type `{3}divorce {2}`.".format(ctx.message.author.name, lovedone.name, married_role.id, ctx.prefix))
        else:
            pass
        marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels, type=discord.ChannelType.text)
        if marchan:
            await self.bot.say("You're now married, congratulations!")
            await self.bot.send_message(marchan, "{} was forced to marry {}.".format(person.mention, lovedone.mention))
        else:
            await self.bot.say("{} was forced to marry {}. I suggest telling the server owner or moderators to make a #marriage channel though.".format(person.mention, lovedone.mention))
            return
        
    @commands.command(pass_context=True)
    async def divorce(self, ctx, divorce_id):
        """Divorce your ex."""
        try:
            married_role = getRoleObj(divorce_id, ctx.message.server)
            if not "❤" in married_role.name.split():
                await self.bot.say("That's not a valid ID.")
                return
            else:
                pass
            await self.bot.delete_role(ctx.message.server, married_role)
            marchan = discord.utils.find(lambda c: c.name == 'marriage', ctx.message.server.channels)
            if marchan:
                await self.bot.say("You're now divorced.")
                await self.bot.send_message(marchan, "{} divorced ID `{}`.".format(ctx.message.author.mention, divorce_id))
            else:
                await self.bot.say("You're now divorced! I suggest telling the server owner or moderators to make a #marriage channel though.")
                return
        except discord.Forbidden:
            await self.bot.say("I do not have the `manage roles` permission, I need it to divorce you.")
            return
        except:
            await self.bot.say("That's not a valid ID.")
            return
        
def getRoleObj(roleID, server):
    for role in server.roles:
        if role.id == roleID:
            return role
        
def setup(bot):
    bot.add_cog(marry(bot))