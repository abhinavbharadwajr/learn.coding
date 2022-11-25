Monthswith30 = [4, 6, 9, 11]
Monthswith31 = [1, 3, 5, 7, 8, 10, 12]

Month = int(input())

if (Month == 2) :
    print("28")
elif (Month in Monthswith30) :
    print("30")
elif (Month in Monthswith31) :
    print("31")
else :
    print("Error")