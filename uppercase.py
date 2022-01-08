file = input('Enter the filename:')
try :
	fhand = open(file)
	for i in fhand :
		i = i.rstrip()
		print(i.upper())
except :
	print('File not found.')
	quit()
