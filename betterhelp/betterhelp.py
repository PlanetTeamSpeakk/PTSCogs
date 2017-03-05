import discord
from discord.ext import commands
import asyncio
import inspect

class BetterHelp:
    """Some better help than the default one."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['cmds', 'commands'])
    @commands.cooldown(3, 10, commands.BucketType.user)
    async def help(self, ctx, *, command_or_cog=None):
        """How does this work?
        Example:
        [p]help
        [p]help trivia
        [p]help Trivia (Note the capital T to get all the commands for that cog/category.)"""
        command = command_or_cog
        if command == None:
            if not ctx.message.channel.is_private:
                msg = await self.bot.say("I am sending you help in dms!")
            commands = {}
            help_msg = ""
            counter = 0
            for cog in self.bot.cogs:
                commands[cog] = []
                for cmd in self.bot.commands:
                    if self.bot.commands[cmd].cog_name == cog:
                        if (len(self.bot.commands[cmd].checks) != 0) and (ctx.message.server != None):
                            found = False
                            if ("serverowner" in str(self.bot.commands[cmd].checks[0])) and (ctx.message.author.id == ctx.message.server.owner.id):
                                found = True
                            elif ctx.message.author.id == self.bot.settings.owner:
                                found = True
                            elif ("mod" in str(self.bot.commands[cmd].checks[0])):
                                mod_role = self.bot.settings.get_server_mod(ctx.message.server)
                                admin_role = self.bot.settings.get_server_admin(ctx.message.server)
                                for role in ctx.message.server.roles:
                                    if role.name.lower() == str(mod_role).lower():
                                        mod_role = role
                                    elif role.name.lower() == str(admin_role).lower():
                                        admin_role = role
                                for role in ctx.message.author.roles:
                                    if role == mod_role:
                                        found = True
                                        break
                                    elif role == admin_role:
                                        found = True
                                        break
                            elif ("admin" in str(self.bot.commands[cmd].checks[0])):
                                admin_role = self.bot.settings.get_server_admin(ctx.message.server)
                                for role in ctx.message.server.roles:
                                    if role.name.lower() == str(admin_role).lower():
                                        admin_role = role
                                        break
                                for role in ctx.message.author.roles:
                                    if role == admin_role:
                                        found = True
                                        break
                            else: # no idea what the permission is
                                found = True
                            if not found:
                                continue
                        commands[cog].append(cmd)
            commandsCopy = commands.copy()
            for cog in commandsCopy:
                if len(commands[cog]) == 0:
                    del commands[cog]
            for cog in list(commands.keys()):
                help_msg += "**{}**\n".format(cog)
                for cmd in commands[cog]:
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
            if command in self.bot.cogs:
                await self.send_cog_help(ctx, command)
            elif command in self.bot.commands:
                await self.send_cmd_help(ctx, command)
            else:
                await self.bot.say("That's not a valid command nor a cog/category.")
            
    async def send_cog_help(self, ctx, cog):
        if cog not in self.bot.cogs: # for if it's used from anywhere else which will be very rare and unusual.
            raise TypeError("That's not a valid cog.")
        else:
            commands = []
            for cmd in self.bot.commands:
                if self.bot.commands[cmd].cog_name == cog:
                    if (len(self.bot.commands[cmd].checks) != 0) and (ctx.message.server != None):
                        found = False
                        if ("serverowner" in str(self.bot.commands[cmd].checks[0])) and (ctx.message.author.id == ctx.message.server.owner.id):
                            found = True
                        elif ctx.message.author.id == self.bot.settings.owner:
                            found = True
                        elif ("mod" in str(self.bot.commands[cmd].checks[0])):
                            mod_role = self.bot.settings.get_server_mod(ctx.message.server)
                            admin_role = self.bot.settings.get_server_admin(ctx.message.server)
                            for role in ctx.message.server.roles:
                                if role.name.lower() == str(mod_role).lower():
                                    mod_role = role
                                elif role.name.lower() == str(admin_role).lower():
                                    admin_role = role
                            for role in ctx.message.author.roles:
                                if role == mod_role:
                                    found = True
                                    break
                                elif role == admin_role:
                                    found = True
                                    break
                        elif ("admin" in str(self.bot.commands[cmd].checks[0])):
                            admin_role = self.bot.settings.get_server_admin(ctx.message.server)
                            for role in ctx.message.server.roles:
                                if role.name.lower() == str(admin_role).lower():
                                    admin_role = role
                                    break
                            for role in ctx.message.author.roles:
                                if role == admin_role:
                                    found = True
                                    break
                        else: # no idea what the permission is
                            found = True
                        if not found:
                            continue
                    commands.append(cmd)
            help_msg = "**{}**:\n\n{}\n\n**Commands**:\n\t".format(cog, self.bot.cogs[cog].__doc__)
            for cmd in commands:
                help_msg += "{}: {}\n\t".format(cmd, self.bot.commands[cmd].short_doc)
                if len(help_msg) >= 1750:
                    await self.bot.send_message(ctx.message.channel, help_msg)
                    help_msg = ""
            await self.bot.send_message(ctx.message.channel, help_msg)
            
    async def send_cmd_help(self, ctx, command=None):
        ctx.prefix = ctx.prefix.replace("\\\\", "\\\\\\\\") # for my own bot, Impulse Beta (private)
        if command == None:
            command = str(ctx.command)
        for cmd in self.bot.commands.keys():
            if cmd == command.split()[0]:
                if len(command.split()) == 2:
                    if hasattr(self.bot.commands[command.split()[0]], "commands"):
                        subcommands = self.bot.commands[command.split()[0]].commands
                    else:
                        await self.bot.send_message(ctx.message.channel, "That command has no subcommands.")
                        return
                    if command.split()[1] not in subcommands:
                        await self.bot.send_message(ctx.message.channel, "That is not a valid subcommand.")
                        return
                    command = str(command) # just making sure it's still a string.
                    params = list(self.bot.commands[command.split()[0]].commands[command.split()[1]].params)
                    paramsCopy = params[::]
                    params = []
                    for param in paramsCopy:
                        if (str(param) != "self") and (str(param) != "ctx") and (str(param) != "context"):
                            for attr in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                if command.split()[1].lower() in attr:
                                    while not hasattr(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr), "params"):
                                        for attr1 in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                            if hasattr(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr1), "params") and command.split()[1] in attr1:
                                                attr = attr1
                                                break
                                    while param not in dict(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr).params):
                                        for attr1 in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                            if hasattr(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr1), "params") and command.split()[1] in attr1 and attr1 != attr:
                                                attr = attr1
                                                break
                                    if dict(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr).params)[param].default == inspect._empty:
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
                            await self.bot.send_message(ctx.message.channel, "**{}{} {} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command.split()[0], command.split()[1], " ".join(list(params)), help, "\n\t".join(subcommands)))
                        else:
                            await self.bot.send_message(ctx.message.channel, "**{}{} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command.split()[0], command.split()[1], help, "\n\t".join(subcommands)))
                    else:
                        if params != []:
                            await self.bot.send_message(ctx.message.channel, "**{}{} {} {}**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], " ".join(list(params)), help))
                        else:
                            await self.bot.send_message(ctx.message.channel, "**{}{} {}**:\n\n{}".format(ctx.prefix, command.split()[0], command.split()[1], help))
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
                                        if (str(param) != "self") and (str(param) != "ctx") and (str(param) != "context"):
                                            for attr in dir(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name]):
                                                if command.split()[2].lower() in attr and hasattr(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr), "params"):
                                                    if dict(self.bot.cogs[self.bot.commands[command.split()[0]].cog_name].__getattribute__(attr).params)[param].default == inspect._empty:
                                                        params.append("<" + param + ">")
                                                    else:
                                                        params.append("[" + param + "]")
                                                    break
                                    if params != []:
                                        await self.bot.send_message(ctx.message.channel, "**{}{} {}**:\n\n{}".format(ctx.prefix, command, " ".join(params), help))
                                    else:
                                        await self.bot.send_message(ctx.message.channel, "**{}{}**:\n\n{}".format(ctx.prefix, command, help))
                                else:
                                    await self.bot.send_message(ctx.message.channel, "That's not a valid subcommand of that subcommand.")
                            else:
                                await self.bot.send_message(ctx.message.channel, "That subcommand has no other subcommands.")
                        else:
                            await self.bot.send_message(ctx.message.channel, "That command has no subcommands.")
                else:
                    if command not in self.bot.commands:
                        await self.bot.send_message(ctx.message.channel, "That's not a valid command")
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
                        if (str(param) != "self") and (str(param) != "ctx") and (str(param) != "context"): # the list will turn into a NoneType if you remove the 'self' param with params.remove("self")
                            for attr in dir(self.bot.cogs[self.bot.commands[command].cog_name]):
                                if command.lower() in attr and hasattr(self.bot.cogs[self.bot.commands[command].cog_name].__getattribute__(attr), "params"):
                                    while param not in dict(self.bot.cogs[self.bot.commands[command].cog_name].__getattribute__(attr).params):
                                        for attr1 in dir(self.bot.cogs[self.bot.commands[command].cog_name]):
                                            if hasattr(self.bot.cogs[self.bot.commands[command].cog_name].__getattribute__(attr1), "params") and command in attr1 and attr1 != attr:
                                                attr = attr1
                                                break
                                    if dict(self.bot.cogs[self.bot.commands[command].cog_name].__getattribute__(attr).params)[param].default == inspect._empty:
                                        params.append("<" + param + ">")
                                    else:
                                        params.append("[" + param + "]")
                                    break
                    help = self.bot.commands[command].help
                    if params != []:
                        if subcommands != []:
                            await self.bot.send_message(ctx.message.channel, "**{}{} {}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, " ".join(list(params)), help, "\n\t".join(subcommands)))
                        else:
                            await self.bot.send_message(ctx.message.channel, "**{}{} {}**:\n\n{}".format(ctx.prefix, command, " ".join(list(params)), help))
                    else:
                        if subcommands != []:
                            await self.bot.send_message(ctx.message.channel, "**{}{}**:\n\n{}\n\n**Commands**:\n\t{}".format(ctx.prefix, command, help, "\n\t".join(subcommands)))
                        else:
                            await self.bot.send_message(ctx.message.channel, "**{}{}**:\n\n{}".format(ctx.prefix, command, help))
        
def setup(bot):
    bot.remove_command("help") # removing the old help command to be replaced by the new one.
    bot.send_cmd_help = BetterHelp(bot).send_cmd_help
    bot.add_cog(BetterHelp(bot))