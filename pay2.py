hours = input('Enter the number of your work hours:')
#if somebody types text
try:
	hours = float(hours)
except :
	hours = -1
	print ('Not a number.')
rate = input('Enter your rate per hour:')
try:
	rate = float(rate)
except :
	rate = -1
	print ('Not a number.')
#again for the text
if hours == -1 :
	print ('Wrong value.')
elif hours <= 40 :
	pay = hours * rate
else :
	pay = hours * rate + (hours%40)*1.5*rate
print ('Pay:', round(pay,2))

