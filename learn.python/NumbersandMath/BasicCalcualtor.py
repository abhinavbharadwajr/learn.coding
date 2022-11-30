import math

def menu() :
    print("\n\t 1. Sum")
    print("\n\t 2. Difference")
    print("\n\t 3. Product")
    print("\n\t 4. Division")

numone = int(input("\nEnter Number One : "))
numtwo = int(input("\nEnter Number Two : "))

menu()

uChoice = int(input("\n Enter choose an Action to perform : "))

if uChoice == 1 or uChoice == 'sum' or 'add' :
    sum = numone + numtwo
    print(f'\nSum of {numone} and {numtwo} is {sum}')
    exit()

elif uChoice == 2 or uChoice == 'diff' or 'sub' :
    diff = numone - numtwo
    print(f'\nDifference of {numone} and {numtwo} is {diff}')
    exit()

elif uChoice == 3 or uChoice == 'product' or 'multiply' :
    prod = numone * numtwo
    print(f'\nProduct of {numone} and {numtwo} is {prod}')
    exit()

elif uChoice == 4 or uChoice == 'divide' or 'div' :
    div = float(numone / numtwo)
    print(f'\nSum of {numone} and {numtwo} is {div}')
    exit()

else :
    exit("\nNot a Valid Option! Try again!")