# All Group Pandas Dataframe Program
import pandas as pd

df = pd.read_csv("Textoutput.csv")
df1 = pd.DataFrame(df, columns=['Image_Path', 'Image_Name', 'TEXT'])
#print(df1)
df2 = df1.groupby(['Image_Path'])

print(df.groupby('Image_Path').groups)
# Now we print the first entries in all the groups formed
print(df2.first())

# Iterating through groups
grp = df1.groupby('Image_Path')
for name, group in grp:
    print(name)
    print(group)

# Now we iterate an element of group containing multiple keys
grp1 = df1.groupby(['Image_Path', 'TEXT'])
for name, group in grp1:
    print(name)
    print(group)
# Applying function to group
grp = df1.groupby('Image_Path')
grp.agg({'Image_Path': 'sum', })
# Write data in Excel file
#df1.to_excel("group.xlsx")
print("Successfully Added the data in the excel file")