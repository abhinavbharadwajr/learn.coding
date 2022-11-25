import csv

print("Processing Mark Register ...")
fldir = input("Enter the directory where you want to store the file [C: / D:] : ")
flname = input("Enter your File Name (Don't specify the Extension) : ")

if fldir == 'd' or 'D':
    path='D://'+flname+'.csv'
if fldir == 'c' or 'C':
    path="C://"+flname+'.csv'

flopen = open(path,"a+")
flwriter = csv.writer(flopen)

examName = input("Enter the Name of the Exam :")
flwriter.writerow(examName+'\n')

ch='y'
while ch == 'y' or 'Y':
    print("Please enter all marks in %")
    sub1 = float(input("Enter the marks for Physics/Commerce :"))
    sub2 = float(input("Enter the marks for Chemistry/Buisness Studies :"))
    sub3 = float(input("Enter the marks for Maths :"))
    sub4 = float(input("Enter the marks for English :"))
    sub5 = float(input("Enter the marks for CS/Accountancy :"))
    avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
    res = [sub1,sub2,sub3,sub4,sub5,avg]
    heading=["PHYSICS/COMMERCE","CHEMISTRY/BUISNESS STUDIES","MATHS","ENGLISH","CS/ACCOUNTANCY","AVERAGE %"]
    flwriter.writerow(heading)
    flwriter.writerow(res)
    ch = input("Do you want to add more records (y/N)")
    if ch == 'n' or 'N':
        print("Database updated sucessfully!!")
        break

flopen.close()
