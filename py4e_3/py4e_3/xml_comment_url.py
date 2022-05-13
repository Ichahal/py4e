#need to import these in python for this code to work 
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#to get access to https sites 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#create handle for webpage in url and quit's in case of wrong input 
link = input('Enter url - ')
try : url = urllib.request.urlopen(link, context=ctx)
except : quit('Invalid input')

# read the web page , create xml elementry tree and search for comment counts in xml
data = url.read()
tree = ET.fromstring(data)
count_et = tree.findall('comments/comment/count')

# get count values in strings from ET and convert them into int 
count = []
for number in count_et : count.append(int(number.text))

# add up all the int in count and save them ,then print it .
total = sum(count)
print(total)
