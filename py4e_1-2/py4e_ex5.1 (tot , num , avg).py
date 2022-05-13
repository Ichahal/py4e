num = 0
tot = 0.0
while True  : 
	sval = input("Enter A Number : ")
	if sval == 'done' :
		break
	try  : 
		fval = float(sval)
	except :
		print ("Invalid Input")
		continue
#	print(fval)
	num = num + 1
	tot = tot + fval 
	avg = (tot / num )
#print ('All Done')
print( tot,num,avg)
	
