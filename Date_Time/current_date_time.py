# Get Current Date and Time using Python
import datetime
import pytz

current_time = datetime.datetime.now()
print("Current Time now is : ", current_time)

# Attributes of now
print("The attributes of now() are : ")
print("Year : ", current_time.year)  # For Year
print("Month : ", current_time.month)  # For Month
print("Day : ", current_time.day)  # For Day
print("Hour : ", current_time.hour)  # For Time
print("Minute : ", current_time.minute)  # For Minute
print("Second : ", current_time.second)  # For Second
print("Microsecond : ", current_time.microsecond)  # For Microsecond

# Getting time of particular timezone
current_time1 = datetime.datetime.now(pytz.timezone("Asia/kolkata"))
print("Current time at India:", current_time1)



