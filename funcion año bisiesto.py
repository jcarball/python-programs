def isYearLeap(year):
#
    if (year % 4 == 0) and (year%100 !=0 or year%400 == 0):
        result = True
        print(result)
    else:
        result = False
        print(result)
    return result
# coloca tu código aquí
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	year = testData[i]
	print(year,"->",end="")
	result = isYearLeap(year)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")