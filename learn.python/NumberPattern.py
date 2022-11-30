''' 
You can define the Value of 'rows' when you need to
Print the Pattern Only for a Fixed number of Rows
'''
# rows = 6

# if you want user to enter a number, below line does it
rows = int(input("\nEnter the number of rows : "))

# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
