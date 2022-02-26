import pandas as pd

df = pd.read_csv("Textoutput.csv", usecols=[1, 3])

# write in the Excel file
df1 = pd.DataFrame(df)
# find duplicate column
#Dup = df1[df1.duplicated()]      # For find duplicate in row
df3 = df1.drop_duplicates(['Image_Path'])
df3.to_excel("student.xlsx")
print("Successfully Added the data in the excel file")
df2 = pd.read_excel("student.xlsx")
print(df2)
