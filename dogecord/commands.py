## takes text messages from Discord and parses them for commands

from dogecord import lists
from dogecord import config


class Command:
	pass

command_map = {}

def register_command(ctext,function):
	pass


def handle_message(mesg):
	text = message.get('m.text') # TODO: figure out what this actually is
	is_cmd = False
	command = ''
	if text.startswith(config.COMMAND_PREFIX):
		command,args = text[len(config.COMMAND_PREFIX):].split(None,1)
		is_cmd = True
	elif text.startswith(lists.get_my_mention()):