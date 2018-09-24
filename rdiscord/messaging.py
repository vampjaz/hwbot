import websocket
import threading
import time

from rdiscord import rhttp
from rdiscord import jsonparse
from rdiscord import jsongen
from rdiscord import config


message_callback = None # holds a pointer to the upper level app's recv callback

## message reception:

def handle_message(mesg):
	if message_callback:
		message_callback(mesg)


## message sending:     (TBD)

def send_message(target,mesg):
	if config.VERBOSE:
			print("sending: "+repr(mesg))
	resp = rhttp.auth_data_request(config.GATEWAY_MESSAGE_SEND.format(target), jsongen.gen_message(mesg))
	if config.VERBOSE:
			print(resp)


def send_typing(target):
	if config.VERBOSE:
			print("typing...")
	resp = rhttp.auth_data_request(config.GATEWAY_TYPING_SEND.format(target), '')
	if config.VERBOSE:
			print(resp)