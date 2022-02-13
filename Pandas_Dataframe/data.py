# Working with Missing Data
import pandas as pd


list1 = {'Employee_name': ['Shiva', 'Ram', 'Mohit', 'Ravi'],
         'Employee_Id': ['ABC12', 'DEF23', 'GHI34', 'JKL45'],
         'Employee_Stream': ['Development', 'Fiance', 'Marketing', 'Sales']}

df = pd.DataFrame(list1)
print(df.isnull())
print(df.notnull())

# iterate over rows
print(df.fillna(0))
for i, j in df.iterrows():
    print(i, j)

# iterate over columns
columns = list(df)
for a in columns:
    print(df[a][1])
