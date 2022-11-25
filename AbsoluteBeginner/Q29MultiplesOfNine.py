number = int(input())

if(number < 0 or number == 0):
    print("NULL")
else:
    for i in range (1, number+1):
        if(i == number):
            print(9*i)
        else:
            print(9*i, end=" ")
