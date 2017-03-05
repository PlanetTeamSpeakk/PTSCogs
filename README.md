[![Discord Server](https://img.shields.io/badge/Discord%20Server-Impulse-orange.svg)](https://discord.gg/tzsmCyk) [![Website](https://img.shields.io/badge/Website-impulsebot.co.nf-yellow.svg)](https://impulsebot.com) [![Build Status](https://travis-ci.org/PlanetTeamSpeakk/PTSCogs.svg?branch=master)](https://travis-ci.org/PlanetTeamSpeakk/PTSCogs)
# PTSCogs

1. [Description](#description)
2. [Installation](#installation)
3. [Cogs](#cogs)
  1. [Adkillr](#adkillr)
  2. [Antifilter](#antifilter)
  3. [Autorole](#autorole)
  4. [Battleship](#battleship)
  5. [Betterhelp](#betterhelp)
  6. [CMDCommands](#cmdcommands)
  7. [CMDSuffix](#cmdsuffix)
  8. [Coder](#coder) 
  9. [Embed](#embed)
  10. [FTPStats](#ftpstats)
  11. [Fuckoff](#fuckoff)
  12. [Gardener](#gardener)
  13. [Giveme](#giveme)
  14. [Harambe](#harambe)
  15. [Lyriccommands](#lyriccommands)
  16. [Marry](#marry)
  17. [Memes](#memes)
  18. [Modlog](#modlog)
  19. [Raidprotect](#raidprotect)
  20. [Randomshizzle](#randomshizzle)
  21. [Serverinfo](#serverinfo)
  22. [Spam](#spam)
  23. [Steam](#steam)
  24. [Translator](#translator)
  25. [Useful](#useful)
  26. [Warner](#warner)
  27. [Welcomr](#welcomr)
  28. [Wordfilter](#wordfilter)
  29. [WoT](#wot)
4. [Needed](#needed)
5. [Annotations](#annotations)
6. [Assistance](#assistance)

## Description
This is a repository with all of the cogs I make, some are fun others are for serious things.

## Installation
If you want to install the repository make sure you have discord.py 0.15.0 or higher

```
[p]cog repo add PTSCogs https://github.com/PlanetTeamSpeakk/PTSCogs
```

You can then list and install the available cogs.

```
[p]cog list PTSCogs
```

Need more help with installation? [Assistance](#assistance)

## Cogs
### CMDCommands
Some commands that run from the command prompt, currently windows only, most of them are not meant for a VPS but if you're selfhosting the bot there's no problemo.

#### CMDCommands Commands
- `[p]cmdcommands <cmd command>`¹ runs a command from the commandprompt.
- `[p]cmdcommands md <directoryname>`¹ creates a directory with the given name, a folder.
- `[p]cmdcommands pip3install <packagename>`¹ install pip3 packages, like if a cog says you need to run pip3 install Packagename you can use this.
- `[p]cmdcommands pipinstall <packagename>`¹ same as pip3install but for pip instead of pip3.
- `[p]cmdcommands pip3upgrade <packagename>`¹ same as pip3install but also adds --upgrade behind the packagename to indicate it has to be updated.
- `[p]cmdcommands pipupgrade <packagename>`¹ same as pip3upgrade but for pip instead of pip3.
- `[p]cmdcommands emptycog <cogname>¹` creates an emptycog for you.
- `[p]cmdcommands startcog <cogname>`¹ starts a cog for you to edit, requires standard open software for .py files to be a .py editor.

### Embed
Embeds a message for you, can be an announcement.

#### Embed Commands
- `[p]embed`² dm's you help for the embed command.
- `[p]embed true <color> <title> <description> <footer>`² it is all explained pretty well in the embed command.
- `[p]embed false <color> <title> <description> <footer>`² it is all explained pretty well in the embed command. 

### Fuckoff
Tell someone to fuck off.

#### Fuckoff Commands
- `[p]foff <@user>` tells someone to fuck off.
- `[p]afoff <@user>` tells someone to fuck off but doesn't mention your name and deletes your message if it has perms.
- `[p]ifoff <item>` allows you to fuckoff anything, even roles!
- `[p]iafoff <item>` same as the afoff command but for items.

### Harambe
\#DixOutForHarambe

#### Harambe Commands
- `[p]harambe` shows you a little text for harambe. Our dix will forever be out for you Harambe.
- `[p]harambeinfo` gives you some info about, the sadly now dead, harambe.

### Lyriccommands
Some commands for song lyrics.

#### Lyriccommands Commands
- `[p]fuckthisshit` gives the lyrics for <https://youtu.be/9wO5TnYaJ4o?t=53s>.
- `[p]princeofbelair [@user]` gives the lyrics for <https://www.youtube.com/watch?v=AVbQo3IOC_A>, but changes The Prince of Bel Air to the user if one was given.
- `[p]heman` gives the lyrics for <https://www.youtube.com/watch?v=ZZ5LpwO-An4>.

### Memes
Some dank commands.

#### Memes Commands
- `[p]meme` shows you a random meme.
- `[p]addmeme` adds a meme to the meme list, must be hosted on imgur (to prevent non-image links).
- `[p]delmeme`² deletes a meme from the meme list.
- `[p]goodshit` shows the goodshit copypasta.
- `[p]yesno` says yes or no with a meme.
- `[p]datboi` oh shit waddup.
- `[p]airhorn` plays a random airhorn sound.
- `[p]airhornsong <songname>` plays a airhornsong for a list of songs type in `[p]airhornsong list`.
- Reacts to ayy.
- Reacts to o shit
- Reacts to oh shit.
- Reacts to feels bad man.

### Randomshizzle
Some random commands that don't really serve a purpose.

#### Randomshizzle Commands
- `[p]cooldog` the cooldog copypasta.
- `[p]flipitem <item>` flips anything.
- `[p]soundsfromspace` gives a link to the spoopy <http://github.audio> website.
- `[p]punch <@user>` punches a user.
- `[p]ipunch <item>` punches everything.
- `[p]triggered` TRIGGEREDDDD.
- `[p]kys` the lenny kys copypasta.
- `[p]pressf [times]` shows your respect x amounts of times, default is 1 max is 4.
- `[p]colorrole <color>` creates a color role for you and only for you.
- `[p]rainbow <times> <interval>` creates a rainbow message for you!

### Serverinfo
Some commands about the server.

#### Serverinfo Commands
- `[p]server owner` shows you the server owner.
- `[p]server name` for if you for some reason can't read the servername yourself, like if you're a total dipshit.
- `[p]server sid` shows you the server ID.
- `[p]server channelname` again for if you're a total dipshit and can't read the channelname yourself.
- `[p]server cid` shows you the channel ID.
- `[p]server time` I dunno.
- `[p]server roles` shows you all of the server roles.
- `[p]server emojis` shows you all of the custom server emojis.
- `[p]server users` shows you all of the server users, unless there are more than 32 than it dm's you the users to prevent spam.
- `[p]server channels` shows you all of the server channels.
- `[p]server compareids` compares the server and channel ID's to see if it is default, could've used is_default but too late now.
- `[p]server icon` gives you a link to the server icon.
- `[p]server info` shows you about everything you want to know about the server.
- `[p]server channelinfo [#channel]` shows you the information for the given channel, if none for the channel you're in.
- `[p]server userinfo [@user]` shows you information for the given user, if none it gives it for you.

### Spam
Some spam commands.

#### Spam Commands
- `[p]spam <@user> <spamtext> [amount]`² spams the user x amounts of times, default is 4.
- `[p]aspam <@user> <spamtext [amount]`² spams the user x amounts of times but doesn't show your name, default is, again, 4.
- `[p]cspam <spamtext [amount]`² spams x times in the channel, default is 4.
- `[p]acspam <spamtext> amount`² spams x times in the channel but deletes the message containing the command and doesn't show your name, default is again 4.

### Useful
Some useful commands.

#### Useful Commands
- `[p]avatar <@user>` shows you the avatar of the given user.
- `[p]calc <num1> <operation> <num2>` calculates something for you, current operations are -, /, \*, and x (x is just another way for \*)
- `[p]suggest` suggests something to the bot owner, just another way of using `[p]contact`.
- `[p]botowner` shows you who's boss.
- `[p]invite` sends you an invite link for the bot.
- `[p]genoauth <client_id> [perms]` generates an oauth url for the given client ID, perms can be calculated at <https://discordapi.com/permissions.html>
- `[p]genbotoauth <@bot> [perms]` generates an oauth url for the given bot, doesn't always work.
- `[p]uploadcog <cogname>` uploads a cog the bot uses to discord.
- `[p]show_cogs` shows all the cogs, just like `[p]cogs` but not owneronly.
- `[p]emoteurl <emote>` gives a link for a custom emoji.
- `[p]showservers` shows you the servers the bot is in.
- `[p]convert <file_url> <input_format> <output_format>` convert a video or audio file to stuff like mp4 mp3 wav avi and that kind of stuff.
- `[p]showservermembers`² lists all the servers the bot is in and allows you to view all members of one of the servers.

### Marry
You can now marry your loved one!

#### Marry Commands
- `[p]marry <@yourlovedone>` marry your loved one!
- `[p]divorce <divorce_id>` divorce your ex.
- `[p]forcemarry <person> <lovedone>`¹ marry someone to his or her loved one.

### Adkillr
Deletes all the links people send.

#### Adkillr Commands
- `[p]adkillr toggle` toggle if the bot should delete your links.
- `[p]adkillr message <message>` sets the message that shows up when someone's link gets removed.

### Warner
Warn people for their actions.

#### Warner Commands
- `[p]warn <user>` warn a user for his/her actions.
- `[p]resetwarns <user>` reset the warnings for someone.

### Coder
Some coding and decoding commands.

#### Coder Commands
- `[p]to <language> <text>` convert a text to a code language.
- `[p]from <language> <text>`

### FTPStats
Allows you to upload server stats to an FTP Server.

#### FTPStats Commands
- `[p]ftpset`¹ set the settings for the ftpstats cog.

### Antifilter
Only let messages through that you allow.

#### Antifilter Commands
- `[p]antifilter` manages settings for antifilter.

### Autorole
Automatically assign a role on join to a member.

#### Autorole Commadns
- `[p]autorole` manages settings for autorole.

### Battleship
Play that old game called Battleship with the bot.

#### Battleship Commands
- `[p]battleship` play battleship with the bot.

### Betterhelp
Replaces the old help command to a better looking one.

#### Betterhelp Commands
- `[p]help` how does this work?

### CMDSuffix
Process commands when the message ends with something instead of beginning with it.

#### CMDSuffix Commands
- `[p]setsuffix <suffix>` set the cmd suffix.
- `[p]togglesuffix` toggle whether users should be able to use command suffixes.

### Gardener
Plant, harvest and get info on your crops.

#### Gardener Commands
- `[p]garden plant <plant>` plant a plant.
- `[p]garden harvest <plant>` harvest a plant.
- `[p]garden info <plant>` gives information about your plant.
- `[p]garden plants` shows a list of available plants and your plants.
- `[p]garden items` shows all the items you can sell.
- `[p]garden sell <item>` sell a harvested item.
- `[p]garden buy <item>` buy an item to let your plants grow faster.

### Giveme
Allow members to give themselves roles.

#### Giveme Commands
- `[p]giveme <role>` gives you a role.
- `[p]giveme list` gives you a list of available roles.
- `[p]giveme add <role>` adds a role to the list of givemes.
- `[p]giveme remove <role>` removes a role from the list of givemes.
- `[p]giveme getoff <role>` removes a giveme from your roles.

### Modlog
Log moderation stuff.

#### Modlog Commands
- `[p]modlogset` manages modlog settings.

### Raidprotect
Protects your server from raids.

#### Raidprotect Commands
- `[p]raidprotect toggle` toggles raidprotect on or off.
- `[p]raidprotect setchannel <channel>` sets the channel the bot should send messages to.
- `[p]raidprotect setmembers <members>` sets the amount of members after which the bot should turn on raidprotect.
- `[p]raidprotect members` shows the amount set with `[p]raidprotect setmembers`.

### Steam
Get some steam info from people or games.

#### Steam Commands
- `[p]setsteamkey` sets the steam api key for the user lookup command.
- `[p]steam userid` tells you how to get someone's userid.
- `[p]steam getuserinfo <userid>` gets user's information using their Steam 64 ID.
- `[p]steam donatekey <key>` donates a Steam API key if not yet set.
- `[p]steam applookup <appid>` gets information for an app or game.
- `[p]steam top100forever` gives you the top 100 games played by people since march 2009.
- `[p]steam top100in2weeks` gives you the top 100 games played by people since 2 weeks ago.

### Translator
Translate text using Google translate, for free.

#### Translator Commands
- `[p]translate <to_lang> <text>` translate text using google translate.
- `[p]translate langlist` shows a list of available languages.

### Welcomr
Welcome new members and say goodbye to old ones!

#### Welcomr Commands
- `[p]welcomeset` manages settings.

### Wordfilter
Filter out words so people can't say those.

#### Wordfilter Commands
- `[p]wordfilter` manages settings.

### WoT
Get some user and tanks information.

#### WoT Commands
- `[p]wot setapikey <key>` sets the api key to use.
- `[p]wot getuserinfo <user> <server>` get some info from users.
- `[p]wot gettankinfo <tank>` get info on a tank, uses NA server.

## Needed
The Useful cog needs the FFMpy library, install it with `pip3 install ffmpy`.

## Annotations
¹ bot owner only.

² moderators only.

<> Mandatory.

[] Optional.

[p] means prefix.

## Assistance
Need help? Have an idea for a new cog or a new command for any of the already existing cogs?
Post an issue or contact me (PlanetTeamSpeak#4157) on 

[The official Red - Discord Bot server](https://discord.gg/geqnqEP). Or

[My server (Impulse Music)](https://discord.gg/tzsmCyk).
