sinp = input('Enter Score: ')
try:
	score = float(sinp)
except:
	exit ('input invalid')
if score > 1.0 :
	exit('input exeed 1.0')
elif score < 0.0 : 
	exit ('input lower then 0.0')
if score >= 0.9 :
	print('A')
elif score >= 0.8:
	print('B')
elif score >= 0.7:
	print('C')
elif score >= 0.6:
	print('D')
elif score < 0.6:
	print('F')
