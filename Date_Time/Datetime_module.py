# Datetime modules
from datetime import date
from datetime import datetime
import time
my_date = date.today()
print("Date passed as argument is", my_date)
print("Current year:", my_date.year)
print("Current month:", my_date.month)
print("Current day:", my_date.day)

# Get date from Timestamp
date1 = datetime.fromtimestamp(12345678)
print("Datetime from timestamp:", date1)

# Convert Date to String
today1 = date.today()

# Converting the date to the string
Str = date.isoformat(today1)
print("String Representation", Str)
print("Type of string:", type(Str))
# Return a string representing the date
Str1 = date.ctime(today1)
print("Return a string representing the date", Str1)
# Returns a date corresponding to the ISO calendar
Str2 = date.fromisocalendar(2022, 22, 2)
print("Returns a date corresponding to the ISO calendar", Str2)
# Returns a date object from the proleptic Gregorian ordinal
ordinal = 1234567
Str3 = datetime.fromordinal(ordinal)
print("Returns a date object from the proleptic Gregorian ordinal", ordinal, Str3)
# Returns a date object from the POSIX timestamp
today_time = time.time()
print(today_time)
Str4 = datetime.fromtimestamp(today_time)
print("Returns a date object from the POSIX timestamp", Str4)

