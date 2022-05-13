#get bs4 folder containing beutiful soup in this folder for this code to work 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#to get access to https sites 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# all the inputs and values for loop to work
link = input('Enter url - ')
position = input('Enter link position- ')
loop = input('Enter number of times to run the loop - ')
try :
	position = int(position)
	loop = int(loop)
except :
	quit('Invalid Input')
loopcount = 0

# a list of all the url that need to be found 
urls = []
urls.append(link)

while loopcount != loop :
	html = urllib.request.urlopen(urls[loopcount], context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	count = 0
	for tag in tags:
		count = count + 1 
		if count == position :
			break
	print(tag['href'])
	urls.append(tag['href'])
	loopcount = loopcount + 1
print('Done')
