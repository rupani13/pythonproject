# All panda series Program
import pandas as pd
import numpy as np

fun = ['T', 'h', 'e', '_', 'B', 'o', 'o', 'k']  # using array
data = np.array(fun)
var = pd.Series(data)
print("The value of series:\n", var)

# using list
list1 = [['T', 'h', 'e', '_', 'B', 'o', 'o', 'k'], ['R', 'm', 'a', 'y', 'n', 'a']]
var1 = pd.Series(list)
print("The value of series:\n", var1)
s = var1.apply(pd.Series).stack().reset_index(drop=True)
print("\nPrinting the converted series:", s)

# Indexing and Selecting Data in Series
fun1 = ['T', 'h', 'e', '_', 'B', 'o', 'o', 'k']  # using array
data1 = np.array(fun1)
var1 = pd.Series(data1)
print("Accessing Element from Series with Position :\n", var1[:7])

# Accessing Element Using Label (index)
fun2 = ['T', 'h', 'e', '_', 'B', 'o', 'o', 'k']  # using array
data2 = np.array(fun2)
var2 = pd.Series(data2, index=[9, 10, 11, 12, 13, 14, 15, 16])
print("Accessing Element Using Label :\n", var2[12])

# Indexing a Series using indexing operator []
df = pd.read_csv("Employee.csv")
print(df)
ser = pd.Series(df['Name'])
data = ser.head(5)
print("Read csv file :\n", ser, data)
data2 = data[2:5]
print("Read csv file using indexing operator:\n", data2)
data1 = data.loc[3:6]
print("Read csv file in loc:\n", data1)
# Binary Operation on Series
list2 = [13, 17, 20, 25]
data3 = pd.Series(list2, index=['a', 'b', 'c', 'd'])
list3 = [12, 15, 19, 24]
data4 = pd.Series(list3, index=['a', 'b', 'd', 'f'])
print("The value in binary:\n", data3, data4)
# adding two series using
var3 = data3.add(data4, fill_value=0)
print("Using adding two series in binary:\n", data4)
