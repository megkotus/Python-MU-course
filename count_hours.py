fhand = open('mbox-short.txt')
l_hours = list()
d_hours = dict()
for line in fhand :
	if not line.startswith('From') : continue
	words = line.split()
	if len(words) >= 6 :
		hour = words[5].split(':')
		l_hours.append(hour[0])
for hour in l_hours:
	d_hours[hour] = d_hours.get(hour, 0) +1

#list comprehension variant --> for k,v in sorted([(k,v) for k,v in d_hours.items()]) :
y = sorted(d_hours.items())
for k,v in y :
	print (k,v)

