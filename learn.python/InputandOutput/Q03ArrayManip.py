inputList = list(map(int, input().split()))

arrsize = inputList[0]
KVal = inputList[1]

array = list(map(int, input().split()))

print(arrsize, KVal)

for j in range (0, arrsize-1) :
    print(array[j], end=" ")

print(array[arrsize-1])