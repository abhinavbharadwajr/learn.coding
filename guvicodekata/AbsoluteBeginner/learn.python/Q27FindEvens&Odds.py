userInput = list(map(int, input().strip()))

evenNumbs = []
oddNumbs = []

for i in range (0, len(userInput)):
    if(userInput[i] % 2 == 0):
        evenNumbs.append(userInput[i])
    else:
        oddNumbs.append(userInput[i])

#sort - Not Necessary But
#       Needed if you need to print the
#       output as a sorted List
evenNumbs.sort()
oddNumbs.sort()

#print
print(*evenNumbs, end="\n")
print(*oddNumbs)