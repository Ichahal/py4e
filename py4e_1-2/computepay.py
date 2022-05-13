def computepay (hours, pay): 
	if hours > 40:
		ot = 0
		ot = (hours % 40) * (pay * 1.5)
		hours = hours - (hours % 40)
		return (hours * pay + ot)
	else :
		return (hours * pay)
hinp = input('Enter Hours')
pinp = input('Hourly Rate')
try :
	hinp=float(hinp)
	pinp =float(pinp)
except :
	exit("Please Enter Valid Input")
gpay = computepay(hinp, pinp)
print ('pay',gpay)
