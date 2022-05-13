x = open('mbox-short.txt')
count = 0
for y in x : 
	if y.startswith('From ') :
		count = count + 1
		z = y.split()
		print(z[1])
