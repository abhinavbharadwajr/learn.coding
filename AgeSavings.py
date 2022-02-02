import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def convert(toDate):
    format = '%d-%m-%Y'
    dateFormat = datetime.datetime.strptime(toDate, format)
    dateFormat = dateFormat.date()
    return dateFormat

def numOfDays(date1, date2) :
    return (date1-date2).days

def numOfYears(date1, date2) :
    return relativedelta(date1, date2).years

dob = input("\n Enter your Date of Birth (in dd-MM-yyyy format) : ")
dobDate = convert(dob)
birthYear = dobDate.year

currDate = date.today()
currYear = currDate.year
numofDaysOld = numOfDays(currDate, dobDate)
numofYearsOld = numOfYears(currDate, dobDate)
loopcounter = 1
savings = 0
yearCounter = birthYear

if((birthYear % 400 == 0) or ((birthYear % 4 == 0) and (birthYear % 100 != 0))) :
            savings = 366
else :
            savings = 365

#for loopcounter in range(numofYearsOld,0,-1) :

#    if((yearCounter % 400 == 0) or ((yearCounter % 4 == 0) and (yearCounter % 100 != 0))) :
#        savings = savings + (loopcounter*366)
#    else :
#        savings = savings + (loopcounter*365)

while(loopcounter<numofYearsOld) :
    if((yearCounter % 400 == 0) or ((yearCounter % 4 == 0) and (yearCounter % 100 != 0))) :
        savings = savings + (loopcounter*366)
    else :
        savings = savings + (loopcounter*365)
    loopcounter += 1
    
print("\n You are ",numofDaysOld," Days Old!")
print("\n You are ",numofYearsOld," Years Old!")
print("\n Your Total estimated Savings would be : Rs.",savings)