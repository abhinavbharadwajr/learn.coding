# Basic Program to 
#   1. Get input of Matrix elements from User.
#   2. And print the Matrix.

rows = int(input("\n Enter the number of Rows : "))
columns = int(input("\n Enter the number of Columns : "))

matrix = []                     #Intialize Matrix

print("\n Enter the Matrix's Elements Row-wise : ")

# nested loop to get input
for row in range(rows):
	elements = []
	for clmn in range(columns):	 # A for loop for column entries
		elements.append(int(input()))
	matrix.append(elements)

# nested loop to print the matrix
for row in range(rows):
	for clmn in range(columns):
		print(matrix[row][clmn], end = " ")
	print()
