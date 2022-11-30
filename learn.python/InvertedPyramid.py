''' 
You can define the Value of 'rows' when you need to
Print the Pattern Only for a Fixed number of Rows
'''
# rows = 6

# if you want user to enter a number, below line does it
rows = int(input("\nEnter the number of rows : "))

b = 0
print('')
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')