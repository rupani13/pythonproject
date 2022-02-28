# All Pandas Series Program
# 1. Creating a Pandas Series
import pandas as pd
import numpy as np

df = ['The', 'Book', 'Animal', 'Study']
arr = np.array(df)
print("Array:\n", arr)
df1 = pd.Series(arr)
print("Series in pandas:\n", df1)

# 2. Accessing element of Series: there are two-way
# 1. Accessing Element from Series with Position
var = ['Subject', 'Theory', 'Study', 'Class', 'Book', 'Pen']
arr1 = np.array(var)
print("Array:\n", arr1)
df2 = pd.Series(arr1[:4])
print("Accessing Element from Series with Position:\n", df2)

# 2. Accessing Element Using Label (index)
var1 = ['Subject', 'Theory', 'Study', 'Class', 'Book', 'Pen']
arr2 = np.array(var1)
print("Array:\n", arr2)
df3 = pd.Series(arr2, index=[7, 8, 9, 10, 11, 12])
print("Accessing Element Using Label (index):\n", df3)
print("Accessing Element Using Label (index):\n", df3[10])

# 3. Indexing and Selecting Data in Series
# Indexing a Series using indexing operator
df4 = pd.read_csv("Book1.csv")
print("CSV File:\n", df4)
fun = pd.Series(df4['Name'])
fun1 = fun.head(4)
fun2 = fun[2:4]
print("Indexing a Series using indexing operator:\n", fun)
print("Indexing a Series using indexing operator:\n", fun1)
print("Indexing a Series using indexing operator:\n", fun2)

# Indexing a Series using .loc[ ]
fun3 = fun.loc[2:4]
print("Indexing a Series using loc Function:\n", fun3)

# Indexing a Series using .iloc[ ]
fun4 = fun.iloc[2:4]
print("Indexing a Series using iloc Function:\n", fun4)

# 4. Binary Operation on Series
list1 = [12, 19, 10, 5, 25, 45]
list2 = [13, 17, 21, 6, 30, 25]
van = pd.Series(list1, index=['i', 'j', 'k', 'l', 'm', 'n'])
print("Print List in Series:\n", van)
van1 = pd.Series(list2, index=['i', 'j', 'k', 'l', 'm', 'n'])
print("Print List in Series:\n", van1)
van2 = van.add(van1)
print("Binary Operation on Series in add:\n", van2)
van3 = van.mul(van1)
print("Binary Operation on Series in mul:\n", van3)
van4 = van.cov(van1)
print("Method is used to find covariance of two series:\n", van4)

# 5. Conversion Operation on Series
funct = pd.read_csv("Book1.csv")
# storing dtype before converting
before = funct.dtypes
funct['List'] = funct['List'].astype(int)
funct['Name'] = funct['Name'].astype(str)
# storing dtype after converting
after = funct.dtypes
print("BEFORE CONVERSION\n", before)
print("AFTER CONVERSION\n", after)

# Pandas series method:
# Method is used to combine two series into one
series1 = [12, 19, 10, 5]
series2 = [13, 17, 20, 7]
vo = series1.__le__(series2)
vo1 = series1.__ne__(series2)
print("Used to compare every element of Caller series with passed series:", vo)
print("Method is used to combine two series into one:", vo1)
vo2 = pd.read_csv("Book1.csv")
vo2['Id_New'] = vo2['Id'].tolist()
print("Used to clip values below a passed least value:", vo2)
