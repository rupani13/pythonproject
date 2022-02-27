# All Group Pandas Dataframe Program
import pandas as pd

df = pd.read_csv("Group.csv")
df1 = pd.DataFrame(df, columns=['Name', 'Team', 'Number', 'Age',  'Salary'])
#print(df1)
df2 = df1.groupby(['Team'])
# using groupby function with one key
print(df.groupby('Team').groups)
# Now we print the first entries in all the groups formed
print(df2.first())

# Grouping data by sorting keys
df3 = df1.groupby(['Team', 'Age']).sum()
print(df3)
df4 = df1.groupby('Team').groups
print(df4)
# Write data in Excel file
#df1.to_excel("group.xlsx")
print("Successfully Added the data in the excel file")