# Problem statement : write program Excel file from pandas

import pandas as pd
print("Reading the excel file")
df = pd.read_excel("./new.xls")

#Reading Specific Columns using ‘usecols’ parameter of read_excel columns method.
require_cols = [1, 2]
require_df = pd.read_excel("./new.xls", usecols=require_cols)
print(require_df)

# write in Excel
data = {
    'rollno': [1, 2, 3],
    'name': ['sita', 'gita', 'Mohan'],
    'subject': ['math', 'Physics', 'Art'],
    'class': [10, 9, 9]
}
dataframe = pd.DataFrame(data)
df_writer = pd.ExcelWriter("student.xls", engine='xlsxwriter')
dataframe.to_excel(df_writer, sheet_name='Sheet1', index=False)
df_writer.save()
df_read = pd.read_excel("student.xls")
print(df_read)
