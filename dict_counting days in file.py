fhand = open('mbox-short.txt')
ldays = list()
ddays = dict()
for line in fhand :
	if not line.startswith('From') : continue
	words = line.split()
	if len(words) >= 3 :
		ldays.append(words[2])
for day in ldays:
	ddays[day] = ddays.get(day, 0) +1
print(ddays.items())