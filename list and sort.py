fhand = open('romeo.txt')
words = list()
for x in fhand :
	lwords = x.split()
	for y in lwords :
		if y not in words :
			words.append(y)
words.sort()
print(words)