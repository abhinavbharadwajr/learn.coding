# Python to demonstrate Matrix
#       1. Using Numpy Library functions.

import numpy as np

rows = int(input("\n Enter the number of Rows : "))
columns = int(input("\n Enter the number of Columns : "))

matrix = []                     #Intialize Matrix

print("\n Enter the Matrix's Elements (seperated by space) : ")

elements = list(map(int, input().split()))

matrix = np.array(elements).reshape(rows, columns)

print(matrix)