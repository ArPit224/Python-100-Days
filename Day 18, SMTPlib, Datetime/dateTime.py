import datetime as dt

now = dt.datetime.now()

print(now.year)

print(now.second)

print(now.weekday())

specificDate = dt.datetime(year = 2022, month = 12, day = 12, hour = 4, minute = 56, second = 33)
print(specificDate)