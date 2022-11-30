import sys

def getHCF(x, y):

	minimum = min(x, y)
	if (x % minimum == 0 and y % minimum == 0):
		return minimum

	for i in range(minimum // 2, 1, -1):
		if (x % i == 0 and y % i == 0):
			return i

	return 1

# Driver code
userInput = list(map(int, sys.stdin.read().split()))

print(getHCF(userInput[0], userInput[1]))
