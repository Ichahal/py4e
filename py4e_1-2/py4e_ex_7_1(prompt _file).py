fname = input('Enter the file name: ')
try : 
	file = open(fname)
except :
	print('Invalid input: ',fname)
	exit()
fdata = file.read()
fdata_u = fdata.upper()
fdata_u_st = fdata_u.rstrip()
print (fdata_u_st)
