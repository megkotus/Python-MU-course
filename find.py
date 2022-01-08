#Strings
str = 'X-DSPAM-Confidence: 0.8475 '
pos = str.find(': ')
pos2 = str.find(' ',pos+2)
print(pos2)
x = str[pos+1:pos2]
x = float(x)
print(x)