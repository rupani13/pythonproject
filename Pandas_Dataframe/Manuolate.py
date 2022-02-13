# Manipulating All Data
import pandas as pd

var = pd.read_csv("Employee.csv")
print("Type-", type(var))
var
# Dataframe using head
print("Head-", var.head(1))
var
# DataFrame using shape
print("Shape-", var.shape)
# DataFrame using describe
print("Describe-", var.describe())
# DataFrame using dropna: it removes all the NaN values in the dataframe
print("Dropna-", var.dropna())
# DataFrame using merge
df1 = pd.read_csv("Employee.csv")
merged_col = pd.merge(var, df1)
print("merge:", merged_col)
# DataFrame using rename
Employee1 = var.rename(columns={'Number': 'Num',
                                'Employee_name': 'EmpNam',
                                'Employee_Id': 'EmpId'},
                       inplace=False)
print("Rename:", Employee1)
# DataFrame using rename
Employee1 = pd.DataFrame({'Number': [3, 4],
                          'Employee_name': ['Rohan', 'Rahul'],
                          'Employee_Id': ['ADC12', 'GTE23'],
                          'Employee_Stream': ['Marketing', 'Sales']})
Employee1.to_csv("./ Employee.csv", mode='a', index=False, header=False)
print("Successfully Added the data in the CSV file")
var = pd.read_csv("Employee.csv")
print(var)
