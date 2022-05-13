from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re
url = input('Enter the url: ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
soup_str = str(soup)
numbers_str = re.findall('"comments">(.+?)<', soup_str)
numbers_int = []
for number in numbers_str :
	numbers_int.append(int(number))
total = sum(numbers_int)
print(total)
