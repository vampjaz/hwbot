### main low-level discord library (py3)

import websocket # so far the only required dependency
import threading
import time
import json
# local imports:
from rdiscord import messaging
from rdiscord import rhttp
from rdiscord import jsonparse
from rdiscord import jsongen
from rdiscord import util
from rdiscord import config

# global vars:
discord_token = None
wsocket = None
s_value = None   # no idea what this is.. something to do with th socket heartbeat
is_running = True # this tells the other threads to quit when the app closes 

def setup(token,callback):
	global discord_token
	discord_token = token
	config.ACTIVE_TOKEN = token
	messaging.message_callback = callback
	if config.VERBOSE:
			print("initialization completed")

def connect():
	_socket_connect(util.get_gateway_url())


## private  ================================================================

def _socket_connect(ws_url):
	global wsocket, is_running
	if config.VERBOSE:
			print("opening socket...")
			websocket.enableTrace(True) # enable this trace temporarily
	wsocket = websocket.WebSocketApp(ws_url, on_message=_ws_mesg_cb, on_error=_ws_error_cb, on_close=_ws_close_cb)
	wsocket.on_open = _ws_open_cb
	wsocket.run_forever()
	is_running = False
	if config.VERBOSE:
			print("program ending..")

def _ws_mesg_cb(ws, message):
	global s_value
	if config.VERBOSE:
		print(message)
	mesg = jsonparse.parse(message)
	s_value = mesg.get('s')
	opcode = mesg.get('op')
	if opcode == 10:
		if config.VERBOSE:
			print("received welcome message from discord")
		interval = mesg.get('d.heartbeat_interval')
		heartbeat_thread = threading.Thread(target=_heartbeat_thread, args=(interval,))
		heartbeat_thread.start()
		id_mesg = jsongen.pack(2,jsongen.gen_identify(discord_token))
		if config.VERBOSE:
			print("sending identify message: "+id_mesg)
		ws.send(id_mesg)
	elif opcode == 11:
		if config.VERBOSE:
			print("heartbeat ack")
	elif opcode == 0:
		messaging.handle_message(mesg)



def _ws_error_cb(ws, error):
	print("WebSocket Error: "+repr(error))

def _ws_open_cb(ws):
	print("WebSocket opened!")

def _ws_close_cb(ws):
	print("WebSocket closed!")

def _heartbeat_thread(interval):
	interval_sec = interval/1000.0
	if config.VERBOSE:
			pass#print("heartbeat thread started, sending every {} seconds".format(interval_sec))
	last_s = '12345'
	current_json = ''
	while is_running:
		if s_value != last_s:
			tempdata = {'op':1, 'd':s_value}
			current_json = json.dumps(tempdata)
		wsocket.send(current_json)
		time.sleep(interval_sec)