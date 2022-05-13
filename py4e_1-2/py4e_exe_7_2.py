fname = input('Enter the file name: ')
try : 
	file = open(fname)
except :
	print('Invalid input: ',fname)
	exit()
count = 0
total = 0.0
for line in file : 
	if not 'X-DSPAM-Confidence:' in line :
		continue
	count = count + 1 
	index = line.find(':')
	sval = line[index+2 : ]
	sval_rs = sval.rstrip()
	fval = float(sval_rs)
	total = total + fval
avg = total / count
print('Average spam confidence:',avg)
