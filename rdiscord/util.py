

from rdiscord import rhttp
from rdiscord import jsonparse
from rdiscord import jsongen
from rdiscord import config

def get_gateway_url():
	jdata = rhttp.json_request(config.GATEWAY_REQ_URL)
	url = jdata.get('url')
	if config.VERBOSE:
		print("websocket base URL message: "+url)
	return "{}/?v={}&encoding=json".format(url, config.GATEWAY_VERSION)