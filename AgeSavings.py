import csv
import datetime
from datetime import date

def convert(toDate):
    format = '%d-%m-%Y'
    dateFormat = datetime.datetime.strptime(toDate, format)
    return dateFormat

def numOfDays(date1, date2) :
    return (date1-date2).days

def numOfYears(date1, date2) :
    return (date1-date2).years

dob = input("\n Enter your Date of Birth (in dd-MM-yyyy format) : ")
dobDate = convert(dob)
birthYear = dobDate.year
yearCounter = birthYear
currDate = date.today()
currYear = date.today()
numofDaysOld = numOfDays(dobDate, currDate)
numofYearsOld = numOfYears(dobDate, currDate)
savings = 0

if((birthYear % 400 == 0) or ((birthYear % 4 == 0) and (birthYear % 100 != 0))) :
            savings = 366
else :
            savings = 365

print("\n You are "+numofDaysOld+" Days Old!")
print("\n You are "+numofYearsOld+" Years Old!")
print("\n Your Total estimated Savings would be : Rs."+savings)