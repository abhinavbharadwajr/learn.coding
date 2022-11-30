''' 
You can define the Value of 'rows' when you need to
Print the Pattern Only for a Fixed number of Rows
'''
# rows = 6

# if you want user to enter a number, below line does it
rows = int(input("\nEnter the number of rows : "))

print('')
# for loop to Print Number Pyramid
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')