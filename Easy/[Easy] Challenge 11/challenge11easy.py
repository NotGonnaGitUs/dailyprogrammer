import datetime
day = int(input("Enter the day as an integer "))
month = int(input("Enter the month as an integer "))
year = int(input("Enter the month as an integer "))

date = datetime.date(year,month,day)
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print (days[date.weekday()])
