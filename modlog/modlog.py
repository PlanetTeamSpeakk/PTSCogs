import discord
from discord.ext import commands
from .utils import checks
from cogs.utils.dataIO import dataIO
import os
import datetime

class Modlog:
    """Logs moderation stuff."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/modlog/settings.json")
        
    @commands.group(pass_context=True)
    @checks.mod_or_permissions()
    async def modlogset(self, ctx):
        """Set the settings for the moderation logs."""
        if not ctx.invoked_subcommand:
            await self.bot.send_cmd_help(ctx)
        if ctx.message.server.id not in self.settings:
            self.settings[ctx.message.server.id] = {'channel': None, 'disabled': False, 'join': True, 'leave': True, 'voicechat': True, 'msgedit': True, 'msgdelete': True, 'roleedit': True, 'ban': True, 'reactions': True}
            self.save_settings()
            
    @modlogset.command(pass_context=True)
    async def channel(self, ctx, channel:discord.Channel):
        """Sets the channel the bot should log to."""
        self.settings[ctx.message.server.id]['channel'] = channel.id
        self.save_settings()
        await self.bot.say("Channel set, I will now log to {}.".format(channel.mention))
            
    @modlogset.command(pass_context=True)
    async def disable(self, ctx):
        """Disable the logging system completely."""
        if not self.settings[ctx.message.server.id]['disabled']:
            self.settings[ctx.message.server.id]['disabled'] = True
            self.save_settings()
            await self.bot.say("Logging system has been disabled.")
        else:
            self.settings[ctx.message.server.id]['disabled'] = False
            self.save_settings()
            await self.bot.say("Logging system has been enabled.")
            
    @modlogset.command(pass_context=True)
    async def toggle(self, ctx, module=None):
        """Toggle what the bot should and what the bot shouldn't log."""
        server = ctx.message.server
        modules = ['join', 'leave', 'ban', 'voicechat', 'msgedit', 'msgdelete', 'roleedit', 'channels', 'nicknames']
        if module == None:
            await self.bot.say("```py"
                            "\nChannel: " + str(self.settings[server.id]['channel']) + 
                            "\nDisabled: " + str(self.settings[server.id]['disabled']) +
                            "\nJoin: " + str(self.settings[server.id]['join']) + 
                            "\nLeave: " + str(self.settings[server.id]['leave']) +
                            "\nBan: " + str(self.settings[server.id]['ban']) + 
                            "\nVoicechat: " + str(self.settings[server.id]['voicechat']) +
                            "\nMessage edit: " + str(self.settings[server.id]['msgedit']) +
                            "\nMessage delete: " + str(self.settings[server.id]['msgdelete']) +
                            "\nRole edit: " + str(self.settings[server.id]['roleedit']) +
                            "\nChannels: " + str(self.settings[server.id]['channels']) +
                            "\nNicknames: " + str(self.settings[server.id]['nicknames']) +
                            "\n\nFalse = not being logged.\nTrue = being logged." + "```" + 
                            "You can toggle\n{}.".format(", ".join(modules)))
                            
        elif module.lower() == 'join':
            if self.settings[server.id]['join']:
                self.settings[server.id]['join'] = False
                self.save_settings()
                await self.bot.say("Join logging has been disabled.")
            else:
                self.settings[server.id]['join'] = True
                self.save_settings()
                await self.bot.say("Join logging has been enabled.")
                
        elif module.lower() == 'leave':
            if self.settings[server.id]['leave']:
                self.settings[server.id]['leave'] = False
                self.save_settings()
                await self.bot.say("Leave (and kick) logging has been disabled.")
            else:
                self.settings[server.id]['leave'] = True
                self.save_settings()
                await self.bot.say("Leave (and kick) logging has been enabled.")
                
        elif module.lower() == 'ban':
            if self.settings[server.id]['ban']:
                self.settings[server.id]['ban'] = False
                self.save_settings()
                await self.bot.say("Ban logging has been disabled.")
            else:
                self.settings[server.id]['ban'] = True
                self.save_settings()
                await self.bot.say("Ban logging has been enabled.")
                
        elif module.lower() == 'voicechat':
            if self.settings[server.id]['voicechat']:
                self.settings[server.id]['voicechat'] = False
                self.save_settings()
                await self.bot.say("Voicechat logging has been disabled.")
            else:
                self.settings[server.id]['voicechat'] = True
                self.save_settings()
                await self.bot.say("Voicechat logging has been enabled.")
                
        elif module.lower() == 'msgedit':
            if self.settings[server.id]['msgedit']:
                self.settings[server.id]['msgedit'] = False
                self.save_settings()
                await self.bot.say("Message edit has been disabled.")
            else:
                self.settings[server.id]['msgedit'] = True
                self.save_settings()
                await self.bot.say("Message edit has been enabled.")
                
        elif module.lower() == 'msgdelete':
            if self.settings[server.id]['msgdelete']:
                self.settings[server.id]['msgdelete'] = False
                self.save_settings()
                await self.bot.say("Message delete has been disabled.")
            else:
                self.settings[server.id]['msgdelete'] = True
                self.save_settings()
                await self.bot.say("Message delete has been enabled.")
                
        elif module.lower() == 'roleedit':
            if self.settings[server.id]['roleedit']:
                self.settings[server.id]['roleedit'] = False
                self.save_settings()
                await self.bot.say("Role edit has been disabled.")
            else:
                self.settings[server.id]['roleedit'] = True
                self.save_settings()
                await self.bot.say("Role edit has been enabled.")
                
        elif module.lower() == 'channels':
            if 'channels' not in self.settings[server.id]:
                self.settings[server.id]['channels'] = True
                self.save_settings()
                return
            elif self.settings[server.id]['channels']:
                self.settings[server.id]['channels'] = False
                self.save_settings()
                await self.bot.say("Channels have been disabled.")
            else:
                self.settings[server.id]['channels'] = True
                self.save_settings()
                await self.bot.say("Channels have been enabled.")
                
        elif module.lower() == 'nicknames':
            if 'nicknames' not in self.settings[server.id]:
                self.settings[server.id]['nicknames'] = True
                self.save_settings()
                await self.bot.say("Nicknames have been enabled.")
            elif self.settings[server.id]['nicknames']:
                self.settings[server.id]['nicknames'] = False
                self.save_settings()
                await self.bot.say("Nicknames have been disabled.")
            else:
                self.settings[server.id]['nicknames'] = True
                self.save_settings()
                await self.bot.say("Nicknames have been enabled.")
                
        else:
            await self.bot.say("That module cannot be toggled, you can toggle\n{}.".format(", ".join(modules)))
        
    async def on_member_join(self, member):
        if self.is_module(member.server, 'join'):
            await self.log(member.server, "`[{}]` :inbox_tray: **Member Join Log**\n"
                                        "```Member Joined: {}```".format(self.get_time(), str(member)))
                                        
    async def on_member_remove(self, member):
        if self.is_module(member.server, 'leave'):
            await self.log(member.server, "`[{}]` :outbox_tray: **Member Leave/Kick Log**\n"
                                        "```Member Left/Kicked: {}```".format(self.get_time(), str(member)))
        
    async def on_member_ban(self, member):
        if self.is_module(member.server, 'ban'):
            await self.log(member.server, "`[{}]` :hammer: **Member Ban Log**\n"
                                        "```Member Banned: {}```".format(self.get_time(), str(member)))
                                        
    async def on_voice_state_update(self, before, after):
        if self.is_module(before.server, 'voicechat'):
            if before.voice_channel != after.voice_channel:
                await self.log(before.server, "`[{}]` :bangbang: **Voicechat Log**\n"
                                            "```User: {}"
                                            "\nBefore: {}".format(self.get_time(), str(before), str(before.voice_channel)) +
                                            "\nAfter: {}```".format(str(after.voice_channel)))
                                                
    async def on_message_edit(self, before, after):
        if before.author == before.server.me:
            return
        if self.is_module(before.server, 'msgedit'):
            if before.content != after.content:
                await self.log(before.server, "`[{}]` :pencil2: **Message Edit Log**\n"
                                            "```User: {}"
                                            "\nChannel: {}"
                                            "\nBefore: {}".format(self.get_time(), before.author.name, before.channel.name, before.content) +
                                            "\nAfter: {}```".format(after.content))
                                            
    async def on_message_delete(self, message):
        if message.author == message.server.me:
            return
        if self.is_module(message.server, 'msgdelete'):
            await self.log(message.server, "`[{}]` :wastebasket: **Message Delete Log**\n"
                                            "```User: {}\n"
                                            "Channel: {}\n"
                                            "Message: {}\n```".format(self.get_time(), str(message.author), str(message.channel), message.content))
                                            
    async def on_server_role_create(self, role):
        if self.is_module(role.server, 'roleedit'):
            perms = role.permissions
            await self.log(role.server, "`[{}]` :game_die: **Role Create Log**\n"
                                        "```py\nRole: {}"
                                        "\nColour: {}"
                                        "\nPermissions:"
                                        "\n\tMentionable: {}"
                                        "\n\tDisplay Separatly: {}"
                                        "\n\tAdministrator: {}"
                                        "\n\tCan ban members: {}"
                                        "\n\tCan kick members: {}"
                                        "\n\tCan change nickname: {}"
                                        "\n\tCan connect to voice channels: {}"
                                        "\n\tCan create instant invites: {}"
                                        "\n\tCan deafen members: {}"
                                        "\n\tCan embed links: {}"
                                        "\n\tCan manage channels: {}"
                                        "\n\tCan manage emojis: {}"
                                        "\n\tCan manage messages: {}"
                                        "\n\tCan manage nicknames: {}"
                                        "\n\tCan manage roles: {}"
                                        "\n\tCan manage server: {}"
                                        "\n\tCan mention everyone: {}"
                                        "\n\tCan move members: {}"
                                        "\n\tCan mute members: {}"
                                        "\n\tCan read message history: {}```".format(self.get_time(), str(role.name), str(role.colour), str(role.mentionable), str(role.hoist), str(perms.administrator), str(perms.ban_members), str(perms.kick_members), str(perms.change_nickname), str(perms.connect), str(perms.create_instant_invite), str(perms.deafen_members), str(perms.embed_links), str(perms.manage_channels), str(perms.manage_emojis), str(perms.manage_messages), str(perms.manage_nicknames), str(perms.manage_roles), str(perms.manage_server), str(perms.mention_everyone), str(perms.move_members), str(perms.mute_members), str(perms.read_message_history), str(perms.send_messages), str(perms.speak), str(perms.use_voice_activation), str(perms.manage_webhooks), str(perms.add_reactions)))
                                        
    async def on_server_role_delete(self, role):
        if self.is_module(role.server, 'roleedit'):
            await self.log(role.server, "`[{}]` :game_die: **Role Delete Log**\n"
                                        "```Role: {}```".format(self.get_time(), role.name))
        
    async def on_server_role_update(self, before, after):
        if self.is_module(before.server, 'roleedit'):
            if not (before.permissions == after.permissions) and (before.color == after.color):
                perms = before.permissions
                perms2 = after.permissions
                await self.log(before.server, "`[{}]` :game_die: **Role Edit Log**\n"
                                            "```py\nBefore:\nRole: {}"
                                            "\nColour: {}"
                                            "\nPermissions:"
                                            "\n\tMentionable: {}"
                                            "\n\tDisplay Separatly: {}"
                                            "\n\tAdministrator: {}"
                                            "\n\tCan ban members: {}"
                                            "\n\tCan kick members: {}"
                                            "\n\tCan change nickname: {}"
                                            "\n\tCan connect to voice channels: {}"
                                            "\n\tCan create instant invites: {}"
                                            "\n\tCan deafen members: {}"
                                            "\n\tCan embed links: {}"
                                            "\n\tCan manage channels: {}"
                                            "\n\tCan manage emojis: {}"
                                            "\n\tCan manage messages: {}"
                                            "\n\tCan manage nicknames: {}"
                                            "\n\tCan manage roles: {}"
                                            "\n\tCan manage server: {}"
                                            "\n\tCan mention everyone: {}"
                                            "\n\tCan move members: {}"
                                            "\n\tCan mute members: {}"
                                            "\n\tCan read message history: {}".format(self.get_time(), str(before.name), str(before.colour), str(before.mentionable), str(before.hoist), str(perms.administrator), str(perms.ban_members), str(perms.kick_members), str(perms.change_nickname), str(perms.connect), str(perms.create_instant_invite), str(perms.deafen_members), str(perms.embed_links), str(perms.manage_channels), str(perms.manage_emojis), str(perms.manage_messages), str(perms.manage_nicknames), str(perms.manage_roles), str(perms.manage_server), str(perms.mention_everyone), str(perms.move_members), str(perms.mute_members), str(perms.read_message_history), str(perms.send_messages), str(perms.speak), str(perms.use_voice_activation), str(perms.manage_webhooks), str(perms.add_reactions)) +
                                            "\n\nAfter:\nRole: {}"
                                            "\nColour: {}"
                                            "\nPermissions:"
                                            "\n\tMentionable: {}"
                                            "\n\tDisplay Separatly: {}"
                                            "\n\tAdministrator: {}"
                                            "\n\tCan ban members: {}"
                                            "\n\tCan kick members: {}"
                                            "\n\tCan change nickname: {}"
                                            "\n\tCan connect to voice channels: {}"
                                            "\n\tCan create instant invites: {}"
                                            "\n\tCan deafen members: {}"
                                            "\n\tCan embed links: {}"
                                            "\n\tCan manage channels: {}"
                                            "\n\tCan manage emojis: {}"
                                            "\n\tCan manage messages: {}"
                                            "\n\tCan manage nicknames: {}"
                                            "\n\tCan manage roles: {}"
                                            "\n\tCan manage server: {}"
                                            "\n\tCan mention everyone: {}"
                                            "\n\tCan move members: {}"
                                            "\n\tCan mute members: {}"
                                            "\n\tCan read message history: {}```".format(str(after.name), str(after.colour), str(after.mentionable), str(after.hoist), str(perms2.administrator), str(perms2.ban_members), str(perms2.kick_members), str(perms2.change_nickname), str(perms2.connect), str(perms2.create_instant_invite), str(perms2.deafen_members), str(perms2.embed_links), str(perms2.manage_channels), str(perms2.manage_emojis), str(perms2.manage_messages), str(perms2.manage_nicknames), str(perms2.manage_roles), str(perms2.manage_server), str(perms2.mention_everyone), str(perms2.move_members), str(perms2.mute_members), str(perms2.read_message_history), str(perms2.send_messages), str(perms2.speak), str(perms2.use_voice_activation), str(perms2.manage_webhooks), str(perms2.add_reactions)))
        
    async def on_channel_create(self, channel):
        if self.is_module(channel.server, 'channels'):
            await self.log(channel.server, "`[{}]` :pick: **Channel Create Log**\n"
                                        "```Channel: {}```".format(self.get_time(), channel.name))
                                        
    async def on_channel_delete(self, channel):
        if self.is_module(channel.server, 'channels'):
            await self.log(channel.server, "`[{}]` :pick: **Channel Delete Log**\n"
                                            "```Channel: {}```".format(self.get_time(), channel.name))
                                            
    async def on_channel_update(self, before, after):
        if self.is_module(before.server, 'channels'):
            if not before.name == after.name:
                await self.log(before.server, "`[{}]` :pick: **Channel Edit Log**\n"
                                            "```Before: {}\nAfter: {}```".format(self.get_time(), before.name, after.name))
        
    async def on_member_update(self, before, after):
        if self.is_module(before.server, 'nicknames'):
            if not before.nick == after.nick:
                await self.log(before.server, "`[{}]` :warning: **Nickname Change Log**\n"
                                            "```User: {}\nBefore: {}\nAfter: {}```".format(self.get_time(), str(before), before.nick, after.nick))
        
    async def log(self, server, message):
        channel = discord.utils.get(server.channels, id=self.settings[server.id]['channel'])
        await self.bot.send_message(channel, message)
        
    def get_time(self):
        return datetime.datetime.now().strftime("%X")
        
    def is_module(self, server, module):
        try:
            if not self.settings[server.id]['disabled']:
                if (self.settings[server.id]['channel'] != None) and (self.settings[server.id][module]):
                    return True
                else:
                    return False
            else:
                return False
        except KeyError:
            return False
        
    def save_settings(self):
        dataIO.save_json("data/modlog/settings.json", self.settings)
        
def check_folders():
    if not os.path.exists("data/modlog"):
        print("Creating data/modlog folder...")
        os.makedirs("data/modlog")
        
def check_files():
    if not os.path.exists("data/modlog/settings.json"):
        print("Creating data/modlog/settings.json file...")
        dataIO.save_json("data/modlog/settings.json", {})
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Modlog(bot))