# Python Datetime Strftime
from datetime import datetime as dt
from pytz import timezone

now_date = dt.now()
print("Without formatting", now_date)
var = now_date.strftime("%A %m %Y")
print('var values:', var)
var1 = now_date.strftime("%a %m %y")
print('var1 values:', var1)
var2 = now_date.strftime("%I %p %S")
print('var2 value:', var2)
var3 = now_date.strftime("%H:%M:%S")
print('var3 values:', var3)

# Python Datetime strptime
time_data = ["25/01/22 02:35:8.023", "26/01/22 12:45:0.003",
             "27/01/22 07:35:5.523", "28/01/22 05:15:55.523"]
format_data = "%d/%m/%y %H:%M:%S.%f"
print("Datetime strptime:")
for i in time_data:
    print( dt.strptime(i, format_data))

# Handling Python DateTime timezone
format = "%Y%m%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = dt.now(timezone('UTC'))
print("Current time in UTC:", now_utc.strftime(format))

timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']
print("Handling Python DateTime timezone:")
for zone in timezones:
    now_asia = now_utc.astimezone(timezone(zone))
    print( now_asia.strftime(format))