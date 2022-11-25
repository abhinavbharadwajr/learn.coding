userinput = list(map(str, input()))

for i in range (0, len(userinput)) :
    if (i == len(userinput)-1) :
        print(userinput[i])
        break
    else :
        print(userinput[i], end=",")