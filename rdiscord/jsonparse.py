import json
import time

from rdiscord import config


def parse(jsondat):
	return jsonobj(jsondat)

## this class will act as a semi-transparent dictionary with a few extra features
class jsonobj:
	def __init__(self,jsondat):
		self.rawjson = jsondat
		self.parsed = json.loads(jsondat)

	def get(self,tree,failsafe=None):
		'''gets an object in the tree indexed by dot notation; 'data.info.date' '''
		steps = tree.split('.')
		temptree = self.parsed.copy()
		for i in steps:
			temp = temptree.get(i,None)
			if temp == None:
				return failsafe
			temptree = temp
		return temptree

	def __getitem__(self, key):
		return self.parsed[key]

