list = []
x = open('romeo.txt')
for y in x :
	z = y.split()
	for word in z :
		if word not in list :
			list.append(word)
list.sort()
print(list)
