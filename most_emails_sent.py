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
print(d_emails.items())

#looking for the longest address
bigcount = None
bigword = None
for email, count in d_emails.items() :
	if bigcount is None or count > bigcount :
		bigword = email
		bigcount = count
print(bigword, bigcount)