import sys

userInput = list(sys.stdin.read())

newList = []

for i in range (0, len(userInput)) :
    #newList.append(userInput[i])
    if userInput[i] == '\n' :
        continue
    else :
        newList.append(userInput[i])

print(*newList)