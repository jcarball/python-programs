def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True  #bisiesto

def daysInMonth(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		days = days[m] + days[m+1]
		if res == 29:
		    days = days + 1
		# if statement
			# ...
		days += md
	md = daysInMonth(year, month)
	#if day >= 1 and day <= md:
		# ...
	#else:
		# ...
	return(days)

print (dayOfYear(2000, 12, 31))