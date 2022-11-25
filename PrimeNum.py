# Program to find Prime Number

num = int(input("\nEnter a Number : "))
isPrime = True

if (num < 0) :
    print("\n Unable to Determine the Result! Not a valid Input!")
elif (num == 0 or num == 1) :
    isPrime = False
else :
    for i in range (2, num) :
        if (num % i == 0) :
            isPrime = False

if(isPrime) :
    print(f'\n{num} is a Prime Number!\n')
else :
    print(f'\n{num} is not a Prime Number!\n')
