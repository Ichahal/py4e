file = open('mbox-short.txt')
count = dict()
mostk = None
mostv = None
id = list()
for line in file : 
	if line.startswith('From: ') :
		senders = line.split()
		id.append(senders[1])
for sender in id : 
	count[sender] = count.get(sender,0) + 1
	if mostk is None or mostv < count[sender] : 
		mostk = sender
		mostv = count[sender]
print(mostk,mostv)
