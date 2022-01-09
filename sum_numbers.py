import re
hand = open('mbox.txt')
for line in hand :
	y = re.findall('New Revision: '('[0-9]+)',line))
	if y !=1 : continue
	print(y)
