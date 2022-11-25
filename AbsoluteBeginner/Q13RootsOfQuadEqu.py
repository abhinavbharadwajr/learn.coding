import math

userInput = list(map(int, input().split()))

a = userInput[0]
b = userInput[1]
c = userInput[2]

r1 = float((-b + math.sqrt((b*b) - (4*a*c))) / (2*a))
r2 = float((-b - math.sqrt((b*b) - (4*a*c))) / (2*a))

print('%.2f' %r1, end="\n")
print('%.2f' %r2)
