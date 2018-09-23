## config for dogecord
## different than the rdiscord one

PASS_TO_LISTS = ['READY','GUILD_CREATE','PRESENCE_UPDATE']
PASS_TO_COMMANDS = ['MESSAGE_CREATE']

COMMAND_PREFIX = '!'

COMMAND_NOT_FOUND = None   # set to a string to display a message if the command is not found
#COMMAND_NOT_FOUND = 'that command does not seem to exist. try finding a command with {}help'.format(COMMAND_PREFIX)