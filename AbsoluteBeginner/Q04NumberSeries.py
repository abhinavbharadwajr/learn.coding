userinput = int(input())

if(userinput >= 0 and userinput == 0 ) :
    print(int(0))
else :
    for res in range (1, userinput) :
        res = res * userinput

print(userinput+res)