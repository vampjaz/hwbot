

import rdiscord
from dogecord import lists


def setup(token):
	rdiscord.setup(token,_message_cb)

def run():
	rdiscord.connect()

send_message = rdiscord.messaging.send_message

def _message_cb(mesg,server,user):
	pass