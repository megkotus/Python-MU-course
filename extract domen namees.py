fhand = open('mbox-short.txt')
l_domain_names = list()
d_domain_names = dict()
for line in fhand :
	if not line.startswith('From') : continue
	words = line.split()
	if len(words) >= 3 :
		domain = words[1].split('@')
		l_domain_names.append(domain[1])
for address in l_domain_names:
	d_domain_names[address] = d_domain_names.get(address, 0) +1
print(d_domain_names.items())

#looking for the longest domain name
bigcount = None
bigword = None
for domain, count in d_domain_names.items() :
	if bigcount is None or count > bigcount :
		bigword = domain
		bigcount = count
print(bigword, bigcount)