def getSum(strl):
	digits = list(map(int, strl.strip()))
	return sum(digits)

userInput = str(input())
print(getSum(userInput))
