import datetime as dt
x = dt.datetime(2023, 12, 31, 9, 30, 33)
result = x.strftime("%A of week number %U of the year %Y")
print(result)