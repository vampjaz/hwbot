

import rdiscord
from dogecord import lists
from dogecord import config
from dogecord import commands


def setup(token):
	rdiscord.setup(token,_message_cb)

def run():
	rdiscord.connect()

send_message = rdiscord.messaging.send_message

def _message_cb(mesg):
	act = mesg.get('t')
	if act in config.PASS_TO_LISTS:
		lists.handle_mesg(mesg)
	if act in config.PASS_TO_COMMANDS:
		commands.handle_mesg(mesg)

