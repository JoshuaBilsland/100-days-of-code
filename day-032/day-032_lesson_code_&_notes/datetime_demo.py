import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()

date_of_birth = dt.datetime(year=1900, month=1, day=1)
print(date_of_birth)
