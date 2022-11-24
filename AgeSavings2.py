import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

def convert(toDate) :
    format = '%d-%m-%Y'
    dateFormat = datetime.datetime.strptime(toDate, format)
    dateFormat = dateFormat.date()
    return dateFormat

def numOfDays(date1, date2) :
    return (date1-date2).days

def numOfMonths(date1, date2) :
    return (date1-date2).months

def numOfYears(date1, date2) :
    return relativedelta(date1, date2).years