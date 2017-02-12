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
            if not ctx.message.channel.is_private:
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
            if not ctx.message.channel.is_private:
                await self.bot.edit_message(msg, "I've sent you help in dms!")
        else:
            ctx.prefix = ctx.prefix.replace("\\", "\\\\") # for my own bot, Impulse Beta (private)
            for cmd in self.bot.commands.keys():
                if cmd == command.split()[0]:
                    if len(command.split()) == 2:
                        if hasattr(self.bot.commands[command.split()[0]], "commands"):
                            subcommands = self.bot.commands[command.split()[0]].commands
                        else:
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
                                for attr in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                    if command.split()[1].lower() in attr:
                                        if dict(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr).params)[param].default != None: # For if it's optional ;), finally found a way.
                                            params.append("<" + param + ">")
                                        else:
                                            params.append("[" + param + "]")
                                        break
                        help = self.bot.commands[command.split()[0]].commands[command.split()[1]].help
                        if hasattr(self.bot.commands[command.split()[0]], "commands"):
                            if hasattr(self.bot.commands[command.split()[0]].commands[command.split()[1]], "commands"):
                                subcommands = self.bot.commands[command.split()[0]].commands[command.split()[1]].commands
                            else:
                                subcommands = []
                        if subcommands != []:
                            if params != []:
                                await self.bot.say("**{}{} {} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command.split()[0], command.split()[1], " ".join(list(params)), help, "\n\t".join(subcommands)))
                            else:
                                await self.bot.say("**{}{} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command.split()[0], command.split()[1], help, "\n\t".join(subcommands)))
                        else:
                            if params != []:
                                await self.bot.say("**{}{} {} {}**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], " ".join(list(params)), help))
                            else:
                                await self.bot.say("**{}{} {}**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], help))
                    elif len(command.split()) == 3:
                        command = str(command)
                        if hasattr(self.bot.commands[command.split()[0]], "commands"):
                            subcommands = self.bot.commands[command.split()[0]].commands
                            if command.split()[1] in subcommands:
                                if hasattr(self.bot.commands[command.split()[0]].commands[command.split()[1]], "commands"):
                                    subcommands = self.bot.commands[command.split()[0]].commands[command.split()[1]].commands
                                    if command.split()[2] in subcommands:
                                        help = self.bot.commands[command.split()[0]].commands[command.split()[1]].commands[command.split()[2]].help
                                        params = list(self.bot.commands[command.split()[0]].commands[command.split()[1]].commands[command.split()[2]].params)
                                        paramsCopy = params[::]
                                        params = []
                                        for param in paramsCopy:
                                            if (str(param) != "self") and (str(param) != "ctx"):
                                                for attr in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                                    if command.split()[2].lower() in attr:
                                                        if dict(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr).params)[param].default != None: # For if it's optional ;), finally found a way.
                                                            params.append("<" + param + ">")
                                                        else:
                                                            params.append("[" + param + "]")
                                                        break
                                        if params != []:
                                            await self.bot.say("**{}{} {}**:\n\n{}".format(ctx.prefix, command, " ".join(params), help))
                                        else:
                                            await self.bot.say("**{}{}**:\n\n{}".format(ctx.prefix, command, help))
                                    else:
                                        await self.bot.say("That's not a valid subcommand of that subcommand.")
                                else:
                                    await self.bot.say("That subcommand has no other subcommands.")
                            else:
                                await self.bot.say("That command has no subcommands.")
                    else:
                        if command not in self.bot.commands:
                            await self.bot.say("That's not a valid command")
                            return
                        if hasattr(self.bot.commands[command], "command"):
                            subcommands = self.bot.commands[command].commands
                        else:
                            subcommands = []
                        command = str(command) # just making sure it's still a string.
                        params = list(self.bot.commands[command].params)
                        paramsCopy = params[::] 
                        params = []
                        for param in paramsCopy:
                            if (str(param) != "self") and (str(param) != "ctx"): # the list will turn into a NoneType if you remove the 'self' param with params.remove("self")
                                for attr in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                    if command.lower() in attr:
                                        if dict(self.bot.cogs[self.bot.commands[command].cog_name].__getattribute__(command).params)[param].default != None: # For if it's optional ;), finally found a way.
                                            params.append("<" + param + ">")
                                        else:
                                            params.append("[" + param + "]")
                        help = self.bot.commands[command].help
                        if params != []:
                            if subcommands != []:
                                await self.bot.say("**{}{} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, " ".join(list(params)), help, "\n\t".join(subcommands)))
                            else:
                                await self.bot.say("**{}{} {}**:\n\n{}".format(ctx.prefix, command, " ".join(list(params)), help))
                        else:
                            if subcommands != []:
                                await self.bot.say("**{}{}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, help, "\n\t".join(subcommands)))
                            else:
                                await self.bot.say("**{}{}**:\n\n{}".format(ctx.prefix, command, help))
        
def setup(bot):
    bot.remove_command("help") # removing the old help command to be replaced by the new one.
    bot.add_cog(BetterHelp(bot))