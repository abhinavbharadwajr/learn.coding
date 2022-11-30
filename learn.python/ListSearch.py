stk=[]

listLen = int(input("\nEnter the List Length : "))

for i in range (0, listLen) :
    while True:
        val = int(input("\nEnter list Element : "))
        stk.append(val)
        
        ans=input("\n Do you want to add more? (Y/N) : ")
        
        if ans == 'n' or ans == 'N':
            break

item=int(input("\nEnter the value to be searched for : "))

for i in range (0,len(stk)-1):
    
    if stk[i] == item :
        print(f'\n{item} found at position {i}')
    else:
        print(f'\n {item} not found in the List.')