def factorial(numb) :
    fact = 1
    for i in range(1, numb+1):
        fact = fact * i
    return fact

userInput = int(input())

print(factorial(userInput))

## Alternatively you can use built-in function from math
## 
##   math.factorial(x)
##
## this function computes and returns the Factorial of 
## the given number 'x'