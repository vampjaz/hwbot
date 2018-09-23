# -*- coding: UTF-8 -*-
## downloads the intel ark catalog and parses it into an sql file

import requests
import json
import sqlite3
import os
import sys

fields_to_grab = ['ProductId:int','Lithography:str','MaxTDP:int','ProcessorNumber:str','CoreCount:int','HyperThreading:bool','MemoryTypes:str','NumMemoryChannels:int',
				  'MaxCPUs:int','IntegratedGraphics:str','ThermalJunctionRateCode:str','InstructionSet:str','BusBandwidth:int','BusTypeUnits:str','MaxMem:str',
				  'GraphicsMaxMem:str','GraphicsFreq:str','GraphicsMaxFreq:str','ClockSpeed:str','ClockSpeedMax:str','ThreadCount:int','BrandBadge:str',
				  'ProcessorBrandName:str','BornOnDate:str','ProductName:str','Link:str','GraphicsModel:str','NumDisplaysSupported:int','SocketsSupported:str',
				  'GraphicsMaxResolutionHDMI:str','GraphicsMaxResolutionDP:str','GraphicsMaxResolutionIFP:str','GraphicsMaxResolutionVGA:str',
				  'GraphicsDirectXSupport:str','GraphicsOpenGLSupport:str']

sqlite_datatypes = {'int':'integer','str':'text','bool':'boolean'}
null_values = {'int':-1,'str':'null','bool':False}

search_field = 'ProcessorNumber'
search_elim = ['m3-','i3-','i5-','i7-','i9-','e3-','e5-','e7-','w-','e-','d-','-',' ']

api_url = 'https://odata.intel.com/API/v1_0/Products/Processors()?$format=json'

base_dir = os.path.dirname(os.path.realpath(__file__))
cache_file = os.path.join(base_dir, 'cache/intel_ark.json')
data_file = os.path.join(base_dir, 'intel_ark.db')


def search_name(term):
	temp = term.lower()
	for i in search_elim:
		temp.replace(i,'')
	return temp

def download_and_update():
	raw_data = ''
	if len(sys.argv) >= 2 and sys.argv[1] == 'cached': # specify not to re-download the file and use the cached version
		if not os.path.exists(cache_file):
			print('error: no cache file to read from')
			exit(5)
		raw_data = open(cache_file).read() # read the raw json from the cache
		print("read from cache file")
	else:
		print("downloading...")
		req = requests.get(api_url)
		if req.status_code != 200:
			print('error: bad http code')
			exit(6)
		raw_data = req.text
		print("downloaded!")
		cf = open(cache_file,'w') # open the cache file and save it all
		cf.write(raw_data)
		cf.close()

	parsed_data = json.loads(raw_data).get('d',[]) # parse it to a dict

	if os.path.exists(data_file):
		os.remove(data_file)

	db = sqlite3.connect(data_file)

	keys = []
	schema_list = ['search_field']
	for field in fields_to_grab:
		fname,dtype = field.split(':',1)
		keys.append((fname,dtype))
		schema_list.append(fname + ' ' + sqlite_datatypes.get(dtype,'text'))
	schema = '(' + ','.join(schema_list) + ')'

	c = db.cursor()
	c.execute('CREATE TABLE processors '+schema)
	db.commit()

	search_cache = set()
	processor_nums = []

	for procdata in parsed_data:
		procnum = procdata.get(search_field,'')
		search = 'undefined'
		if procnum != None:
			procnum = procnum.strip()
			processor_nums.append(procnum)
			search = search_name(procnum)
			if search in search_cache:
				print("warning: {} has a duplicate in the search system".format(procdata.get('ProductName','')))
			search_cache.add(search)
		else:
			print("error: {} has null product number".format(procdata.get('ProductName','')))
		values = [search]
		for key,dtype in keys:
			raw = procdata.get(key)
			if raw == None:
				raw = null_values.get(dtype)
			formatted = None
			if dtype == 'str':
				formatted = raw.strip()
			elif dtype == 'int':
				formatted = int(raw)
			elif dtype == 'bool':
				formatted = raw
			values.append(formatted)
		rowph = '(' + ','.join(['?']*len(values)) + ')'
		c.execute('INSERT INTO processors VALUES ' + rowph, values)

	db.commit()
	db.close()

	print(processor_nums)



if __name__ == '__main__':
	download_and_update()