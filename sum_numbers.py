import re
hand = open('mbox.txt')
tot = list()
count = 0
new = 0
for line in hand :
	y = re.findall('^New Revision: ([0-9]+)',line)
	if len(y) !=1 : continue
	count = count + 1
	#extract number from a list
	for i in y :
		x = float(i)
		new = new + x
print(new/count)
