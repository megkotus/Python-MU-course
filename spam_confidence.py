file = input('Enter the filename:')
try:
	fhand = open(file)
except :
	print('File not found: ', file)
	quit()
count = 0
total = 0
for i in fhand :
	if i.startswith('X-DSPAM-Confidence: ') :
		#x = i[21:]
		y = i.find(' ')
		x = i[y+1:]
		x = float(x)
		count = count + 1
		total = x + total
print('Average spam confidence: ', total/count)
