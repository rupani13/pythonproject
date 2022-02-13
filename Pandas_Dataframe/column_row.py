# All Pandas Dataframe Program using columns and rows
import pandas as pd

list1 = {'Employee_name': ['Shiva', 'Ram', 'Mohit', 'Ravi'],
         'Employee_Id': ['ABC12', 'DEF23', 'GHI34', 'JKL45'],
         'Employee_Stream': ['Development', 'Fiance', 'Marketing', 'Sales']}

df = pd.DataFrame(list1)
print(df)
# Columns Selection
print(df[['Employee_name', 'Employee_Stream']])
print(df[['Employee_name', 'Employee_Id']])
print(df[['Employee_Stream', 'Employee_Id']])

# Rows Selection
df1 = pd.DataFrame(list1)
print(df1.loc[0])