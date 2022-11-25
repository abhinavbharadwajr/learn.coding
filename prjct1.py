stk = []

#while True:
#    val=int(input("Enter list element :"))
#    stk.append(val)
#    ans=input("Do you want to continue?(y/n)")
#    if ans!='y':
#        break

#item=int(input("Enter the value to be searched :"))

#for i in range(len(stk)):
#    if stk[i]==item:
#        print("Element found at position :",i)
#    else:
#        print("Item not found.")

n = int(input("Enter the number of List Elements : "))

for i in range(n):
    ele=int(input("Enter Element #"+str(i)+" : "))
    stk.append(ele)

val = int(input("Enter Value to be searched for : "))

for i in range(len(stk)):
    if stk[i]==val:
        print("Value found at position :",i+1)
        break
else:
    print("Item not found.")