import discord
from discord.ext import commands
import os
from .utils import checks
from __main__ import settings

class marry:
    """marry"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def marry(self, ctx, yourlovedone:discord.Member):
        """Now you can finally marry your loved one."""
        await self.bot.say("{} do you take {} as your husband/wife? (yes/no)".format(yourlovedone.mention, ctx.message.author.mention))
        answer = await self.bot.wait_for_message(timeout=60, author=yourlovedone)
        if answer is None:
            await self.bot.say("The user you tried to marry didn't respond, I'm sorry.")
            return
        elif "yes" not in answer.content.lower():
            await self.bot.say("The user you tried to marry didn't say yes, I'm sorry.")
            return
        married_role = await self.bot.create_role(server=ctx.message.server, name="{} ❤ {}".format(ctx.message.author.name, yourlovedone.name),  colour=discord.Colour(value=0XFF00EE), mentionable=True, hoist=True)
        await self.bot.say(married_role.id)
        await self.bot.add_roles(ctx.message.author, married_role)
        await self.bot.add_roles(yourlovedone, married_role)
        await self.bot.say("{} is now married to {}, congratulations!".format(ctx.message.author.mention, yourlovedone.mention))
        
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def forcemarry(self, ctx, yourlovedone:discord.Member):
        """Now you can finally marry your loved one."""
        married_role = await self.bot.create_role(server=ctx.message.server,  name="{} ❤ {}".format(ctx.message.author.name, yourlovedone.name),  colour=discord.Colour(value=0XFF00EE), mentionable=True, hoist=True)
        await self.bot.add_roles(ctx.message.author, married_role)
        await self.bot.add_roles(yourlovedone, married_role)
        await self.bot.send_message(ctx.message.author, "Your divorce id is {}, don't ever give this to anyone or they can divorce you!".format(married_role.id))
        if not yourlovedone.bot:
            await self.bot.send_message(yourlovedone, "Your divorce id is {}, don't ever give this to anyone or they can divorce you!".format(married_role.id))
        else:
            pass
        await self.bot.say("{} is now married to {}, congratulations!".format(ctx.message.author.mention, yourlovedone.mention))
        
    @commands.command(pass_context=True)
    async def divorce(self, ctx, divorce_id):
        """Divorce your ex."""
        try:
            married_role = getRoleObj(divorce_id, ctx.message.server)
            await self.bot.delete_role(ctx.message.server, married_role)
            await self.bot.say("You're now divorced!")
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