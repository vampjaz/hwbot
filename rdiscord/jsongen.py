import json
import time

from rdiscord import config

def pack(opcode,data):
	newdict = {'op':opcode, 'd':data}
	return json.dumps(newdict)

def gen_identify(token):
	newdict = {
		'token': token,
		'properties': {
			'$os': 'darwin',
			'$browser': config.LIBRARY_NAME,
			'$device': config.LIBRARY_NAME
		},
		'compress': False,
		'large_threshold': 50,
		'presence': {
			'game': {
				'name': config.DEFAULT_RP,
				'type': 0
			},
			'status': 'online',
			'since': int(time.time()),
			'afk': False
		}
	}
	return newdict

def gen_message(content):
	newdict = {
		'content':content.replace('\n','\\n')
	}
	return json.dumps(newdict)