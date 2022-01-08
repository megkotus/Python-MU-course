hours = input('Enter the number of your work hours:')
#if somebody types text
try :
	hours = float(hours)
except :
	print ('Error: Not a number.')
	quit()
rate = input('Enter your rate per hour:')
try :
	rate = float(rate)
except :
	print ('Error: Not a number.')
	quit()
if hours <= 40 :
	pay = hours * rate
else :
	pay = hours * rate + (hours%40) * 1.5 * rate
print ('Pay:', round(pay,2))
