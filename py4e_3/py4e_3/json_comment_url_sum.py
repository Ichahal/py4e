#need to import these in python for this code to work .
import urllib.request, urllib.parse, urllib.error
import json
import ssl

#to get access to https sites .
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#create handle for webpage in url and quit's in case of wrong input .
link = input('Enter url - ')
try : url = urllib.request.urlopen(link, context=ctx)
except : quit('Invalid input')

# read and decode the web page , parse the json text , make a list of count in comments .
data = url.read().decode()
data_js = json.loads(data)
count = []
for number in data_js['comments'] : count.append(number['count'])

# make a file of all the counts combined , and if count is not in itr format converts it into int and then make total.
try : total = sum(count)
except :
	counts = []
	for number in count :
		 counts.append(int(number.text))
		 total = sum(counts)


print(total)
