smallest = None
biggest = 0
while True:
	sval = input('Enter number:')
	if sval == 'done':
		break
	try:
		fval = float(sval)
		if smallest is None :
			smallest = fval
		elif smallest > fval :
			smallest = fval
		if biggest < fval :
			biggest = fval
	except :
		print('Invalid input.')
		continue
		
print(biggest, smallest)
