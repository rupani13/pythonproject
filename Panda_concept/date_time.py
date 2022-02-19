# Working with date and time using Pandas
import pandas as pd
import datetime

fun = pd.date_range(19 / 2 / 2022, periods=5, freq='h')
print("Data Range:", fun)
var = ['17 / 2 / 2022', '18 / 2 / 2022', '19 / 2 / 2022']
df = pd.DatetimeIndex(var)
print("Date time index:\n", df)
df1 = pd.to_datetime(var)
print("Date time index:\n", df1)
fun1 = pd.Series(['February 19 2022', '19 / 2 / 2022', 'Today date', 'June 22 2022'])
var1 = pd.to_datetime(fun1, errors='coerce')
print("Date time index:\n", var1)
unixtime = [1234567, 2345678, 3456789]
var2 = pd.to_datetime(unixtime, unit='s')
print("Date time index:\n", var2)
# Print the dates in dd-mm-yy format
rng = pd.DataFrame()
rng['date'] = pd.date_range('19/2/2022', periods=72, freq='H')
rng[:5]

# Create features for year, month, day, hour, and minute
rng['year'] = rng['date'].dt.year
rng['month'] = rng['date'].dt.month
rng['day'] = rng['date'].dt.day
rng['hour'] = rng['date'].dt.hour
rng['minute'] = rng['date'].dt.minute
print(rng.head(6))
