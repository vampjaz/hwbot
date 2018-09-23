from rdiscord import jsonparse
from rdiscord import config
import requests


def json_request(url):
	raw_json = requests.get(url, headers={'User-Agent':config.USER_AGENT}).text
	return jsonparse.parse(raw_json)

def auth_data_request(url,data):
	raw_json = requests.get(url, data=str.encode(data), headers={'User-Agent':config.USER_AGENT, 'Authorization':'Bot '+config.ACTIVE_TOKEN}).text
	return jsonparse.parse(raw_json)

