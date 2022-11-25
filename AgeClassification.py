adultCount = 0
childCount = 0

AgeList = []

AgeListSize = int(input("\n Enter the Total number Members in the List : "))

print("\n Enter the Member's Ages : ")
for i in range(0, AgeListSize):
    listEle = int(input())
    AgeList.append(listEle)
    if(listEle >= 18):
        adultCount+=1
    else :
        childCount+=1
    #print(" ")

print("\n Number of Adult(s) : "+str(adultCount))
print("\n Number of Children : "+str(childCount))
print()