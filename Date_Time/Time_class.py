# Time class
from datetime import time
from datetime import datetime, timedelta
my_time1 = time(11, 39, 56)
print("Entered time", my_time1)
my_time = time(minute=25)
print("Time with one argument", my_time)
my_time = time()
print("Time without argument", my_time)
print("hour =", my_time1.hour)
print("minute =", my_time1.minute)
print("second =", my_time1.second)
print("microsecond =", my_time1.microsecond)

# Convert Time object to String
Time = time(12, 25, 35, 1313)
Str = Time.isoformat()
print("Converting Time object to string:", Str)

# Returns tzinfo.dst() is tzinfo is not None
sen = time(12, 25, 35)
Str1 = sen.dst()
print("Returns tzinfo.dst() is tzinfo is not None:", Str1)

# Timedelta class
ini_time = datetime.now()
print("initial_date", str(ini_time))
# Calculating future dates for two years
future_date_after_2yrs = ini_time + timedelta(days=730)
future_date_after_7days = ini_time + timedelta(days=7)
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_7days:', str(future_date_after_7days))

# Difference between two date and times
new_final_time = ini_time + timedelta(days=5)
print("new_final_time", str(new_final_time))   # printing new final_date
print('Time difference:', str(new_final_time - ini_time))