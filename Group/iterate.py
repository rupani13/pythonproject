# First merge row and remove duplicate value in csv file
import pandas as pd

# Using index attribute of the Dataframe
df = pd.read_csv("Textoutput.csv")
df1 = pd.DataFrame(df, columns=['Image_Path', 'Image_Name', 'TEXT'])
# print(df1)
# for ind in df1.index:
# print(df['Image_Path'][ind], df['TEXT'][ind])
# iterate through each row and select 'Image_Path' and 'TEXT' column respectively.
'''for i in range(len(df1)) :
    print(df.loc[i, "Image_Path"], df.loc[i, "TEXT"])'''

# Project work csv to Excel file
var = {}
for i, row in df1.iterrows():
    try:
        var[row['Image_Path']].append(row['TEXT'])
    except KeyError:
        var[row['Image_Path']] = []
df1.drop_duplicates('Image_Path', inplace=True)
df1['TEXT'] = ['; '.join(v) for v in var.values()]
print(df1)
df2 = pd.DataFrame(df1, columns=['Image_Path', 'TEXT'])
df2.to_excel("group1.xlsx")
print("Successfully Added the data in the excel file")
