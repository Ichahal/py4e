inp = input('Enter the name of file: ')
try :
	hand = open(inp)
except :
		exit('Invalid file name')
		#to avaid tracebacks for wrong file name etc .
import re
#importing regular expressions.
num = []
# a list for all the numbers in file .
for line in hand : 
	line = line.rstrip()
	tmp = re.findall('[0-9]+' ,line)
	#a temporary file for numbers extracted by regex in line .
	if len(tmp) == 0 :
		#if no match is found by regex it creates a blanck list , this is for that .
		continue
	for sval in tmp :
		#to convert extracted data into int from strings .
		ival = int(sval)
		num.append(ival)
		# now all contains list of all the extracted data in int .
total = sum(num)
# total of all the numbers extracted .
print(total)
