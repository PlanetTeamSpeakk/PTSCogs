import discord
from discord.ext import commands
import asyncio

class BetterHelp:
    """Some better help than the default one."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['cmds', 'commands'])
    async def help(self, ctx, *, command=None):
        """How does this work?"""
        if command == None:
            if ctx.message.channel != None:
                msg = await self.bot.say("I am sending you help in dms!")
            help_msg = ""
            counter = 0
            for cog in self.bot.cogs:
                help_msg += "**{}**\n".format(cog)
                for cmd in self.bot.commands:
                    if (self.bot.commands[cmd].cog_name == cog) and not (self.bot.commands[cmd].hidden):
                        if self.bot.commands[cmd].help == None:
                            help_msg += "\t\t**{}**\n".format(cmd)
                        else:
                            if len(self.bot.commands[cmd].help) > 64:
                                help_msg += "\t\t**{}**: {}...\n".format(cmd, self.bot.commands[cmd].help[:64].replace("\n", " "))
                            else:
                                help_msg += "\t\t**{}**: {}\n".format(cmd, self.bot.commands[cmd].help.replace("\n", " "))
                            if len(help_msg) > 1750:
                                if counter >= 5:
                                    await asyncio.sleep(5)
                                    counter = 0
                                try:
                                    await self.bot.send_message(ctx.message.author, help_msg)
                                except:
                                    pass
                                help_msg = ""
                                counter += 1
            try:
                await self.bot.send_message(ctx.message.author, help_msg)
            except:
                pass
            await self.bot.edit_message(msg, "I've sent you help in dms!")
        else:
            for cmd in self.bot.commands.keys():
                if cmd == command.split()[0]:
                    if len(command.split()) > 1:
                        try:
                            subcommands = self.bot.commands[command.split()[0]].commands
                        except:
                            await self.bot.say("That command has no subcommands.")
                            return
                        if command.split()[1] not in subcommands:
                            await self.bot.say("That is not a valid subcommand.")
                            return
                        command = str(command) # just making sure it's still a string.
                        params = list(self.bot.commands[command.split()[0]].commands[command.split()[1]].params)
                        paramsCopy = params[::]
                        params = []
                        for param in paramsCopy:
                            if (str(param) != "self") and (str(param) != "ctx"):
                                params.append(param)
                        help = self.bot.commands[command.split()[0]].commands[command.split()[1]].help
                        if params != []:
                            await self.bot.say("**{}{} {} <{}>**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], "> <".join(list(params)), help))
                        else:
                            await self.bot.say("**{}{} {}**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], help))
                    else:
                        try:
                            subcommands = self.bot.commands[command].commands
                        except:
                            subcommands = None
                        command = str(command) # just making sure it's still a string.
                        params = list(self.bot.commands[command].params)
                        paramsCopy = params[::]
                        params = []
                        for param in paramsCopy:
                            if (str(param) != "self") and (str(param) != "ctx"):
                                params.append(param)
                        help = self.bot.commands[command].help
                        if params != []:
                            if subcommands != None:
                                await self.bot.say("**{}{} <{}>**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, "> <".join(list(params)), help, "\n\t".join(subcommands)))
                            else:
                                await self.bot.say("**{}{} <{}>**:\n\n{}".format(ctx.prefix, command, "> <".join(list(params)), help))
                        else:
                            if subcommands != None:
                                await self.bot.say("**{}{}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, help, "\n\t".join(subcommands)))
                            else:
                                await self.bot.say("**{}{}**:\n\n{}".format(ctx.prefix, command, help))
        
def setup(bot):
    bot.remove_command("help") # removing the old help command to be replaced by the new one.
    bot.add_cog(BetterHelp(bot))