from rdiscord import jsonparse
from rdiscord import config
import requests


def json_request(url):
	raw_json = requests.get(url, headers={'User-Agent':config.USER_AGENT}).text
	return jsonparse.parse(raw_json)

def auth_data_request(url,data):
	print(url)
	print(data)
	head = {'User-Agent':config.USER_AGENT, 'Authorization':'Bot '+config.ACTIVE_TOKEN, 'Content-Type':'application/json'}
	print(head)
	raw_data = requests.post(url, data=str.encode(data), headers=head).text
	return raw_data

