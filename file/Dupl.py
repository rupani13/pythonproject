import pandas as pd

df = pd.read_csv("Textoutput.csv")

df1 = pd.DataFrame(df, columns=['Image_Path', 'Image_Name', 'TEXT'])

# dup = df1[df1.duplicated('Image_Path')]    # For find duplicate in row
df4 = df1.groupby('Image_Path', as_index=False).agg({'Image_Path': 'first', 'TEXT': lambda x: ','.join(x.astype(str))})
df2 = df4.drop_duplicates('Image_Path')
df3 = pd.DataFrame(df2, columns=['Image_Path', 'TEXT'])

df3.to_excel("student.xlsx")
print("Successfully Added the data in the excel file")
