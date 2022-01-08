file = input('Enter the filename:')
try :
	fhand = open(file)
	inp = fhand.read()
	print(len(inp))
except :
	if file == 'banana' :
		print('Ba-na-na!!!')
	else :
		print('File not found: ', file)
		exit()
