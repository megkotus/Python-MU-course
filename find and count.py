fhand = open('mbox-short.txt')
count = 0
for line in fhand :
		if not line.startswith('From') : continue
		i = line.split()
		print(i[1])
		count = count+1
	
print('There are ', count, 'lines in the file that start with From.')