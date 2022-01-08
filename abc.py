#not working
fhand = open('sample.txt')
letters = dict()
abc = ['a', 'b', 'c','d','e','f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for line in fhand :
	line.strip()
	words = line.split()
	for letter in words : 
		letter = letter.low()
for a in abc:

	abc[address] = d_emails.get(address, 0) +1
#print(d_emails.items())

tpl = list()
#create tuples with reversed order
for k,v in d_emails.items() :
	newtup = (v,k)
	tpl.append(newtup)
#sort tuples by values; reverse puts the largest values left
tpl = sorted(tpl, reverse=True)
#limit the number of tuples for printing and reverse the order
for v, k in tpl[:1] :
	print(k,v)