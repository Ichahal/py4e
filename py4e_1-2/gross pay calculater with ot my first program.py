hinp = input('Enter Hours')
pinp = input('Hourly Rate')
hours=float(hinp)
pay =float(pinp)
ot = 0
if hours > 40 : 
	ot = (hours % 40) * pay * 1.5
	hours = hours - (hours % 40)
gpay = hours * pay + ot
print(gpay)
