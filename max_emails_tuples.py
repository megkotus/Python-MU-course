fhand = open('mbox-short.txt')
l_emails = list()
d_emails = dict()
for line in fhand :
	if not line.startswith('From') : continue
	words = line.split()
	if len(words) >= 3 :
		l_emails.append(words[1])
for address in l_emails:
	d_emails[address] = d_emails.get(address, 0) +1
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