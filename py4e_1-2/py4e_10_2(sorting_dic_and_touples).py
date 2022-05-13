file = open('mbox-short.txt')
hours = []
count = {}
for line in file : 
	if line.startswith('From ') :
		words = line.split()
		word = words[5]
		tmp = word.split(':')
		hours.append(tmp[0])
for hour in hours : 
	count[hour] = count.get(hour,0)+1
count_s = sorted(count.items())
for k,v in count_s : 
	print(k,v)
