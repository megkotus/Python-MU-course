count = 0
total = 0.0
while True:
	sval = input ('Enter a number:')
	if sval == 'done':
         break
	try : 
         fval = float(sval)
	except :
	     print('Invalid input.')
	     continue
	count = count + 1
	total = fval+total
			
if count == 0 :
	print('No data.')
else :
	print(total, count, total/count)
	