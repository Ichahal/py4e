# program will not work without imports in python .
import urllib.request , urllib.parse , urllib .error
import json
import ssl

#to get access to https sites .
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# api link and api_key
api = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

# to build a loop for convenience of multipul searches .
while True :
	address = input('Enter location: ')
	if len(address) < 1: break

# parms = parameters dict needed for urlencode to work .
	parms = {}
	parms['address'] = address
	parms['key'] = api_key
	
# urlencode converts address and key in url syntext and url is handle for webpage , data is decoded data of webpage in json while data_js is dict of parsed json .
	link = api + urllib.parse.urlencode(parms)
	url = urllib.request.urlopen(link, context=ctx)
	data = url.read().decode()
	data_js = json.loads(data)

# assignment objective , finding the place id .
	place_id = data_js['results'][0]['place_id']
	print(place_id)

#to end the loop	
	print('Press enter to exit the loop')

print('Done')


