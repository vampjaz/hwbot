## takes text messages from Discord and parses them for commands

from dogecord import lists
from dogecord import config


class Command:
	pass

command_map = {}

def register_command(ctext,function):
	pass


def handle_mesg(message):
	text = message.get('d.content','').strip()
	print('text: ' + text)
	is_cmd = False
	command = ''
	temp = None
	if text.startswith(config.COMMAND_PREFIX):
		temp = text[len(config.COMMAND_PREFIX):]
	elif text.startswith(lists.get_my_mention()):
		temp = text[len(lists.get_my_mention()):]
	if not temp: 
		return
	temp = temp.split(None,1)
	command = temp[0]
	if len(temp) > 1:
		args = temp[1]
	is_cmd = True
	if not is_cmd:
		return
	channelid = message.get('d.channel_id')
	guildid = message.get('d.guild_id')
	userid = message.get('d.author.id')
	username = message.get('d.author.username')
	nickname = message.get('d.nick')
	if not nickname:
		nickname = username
	print('<{}> {}'.format(nickname,text))