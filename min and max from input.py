numlist = list()
try :
	while True :
		inp = input('Enter a number:')
		if inp == 'done' : break
		value = float(inp)
		numlist.append(value)
	print(max(numlist), min(numlist))
except :
	print('Not a number.')

