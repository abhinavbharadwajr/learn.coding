stk=[]
while True:
    val=int(input("Enter list element :"))
    stk.append(val)
    ans=input("Do you want to continue?(y/n)")
    if ans=='n':
        break
item=int(input("Enter the value to be searched :"))
for i in range(0,len(stk)-1):
    if stk[i]==item:
        print("Element found at position :",i)
    else:
        print("Item not found.")
