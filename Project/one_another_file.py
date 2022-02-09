# We are creating an Excel sheet from another workbook
import pandas as pd

df = pd.read_excel("OfficeM&A_RootWords.xlsx")
df1 = pd.read_excel("OfficeM&A_RootWords.xlsx", sheet_name='RootWords', usecols="B")
print(df1)
df.to_excel("OfficeM&A_RootWords.xlsx", engine='xlsxwriter')
# Open it with xlsxwriter
writer = pd.ExcelWriter("OfficeM&A_RootWords.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='RootWords')

# Assign the workbook and worksheet
workbook = writer.book
worksheet = writer.sheets['RootWords']

# Adding the header and Datavalidation list
worksheet.write('D1', 'Status')
worksheet.data_validation('D2', {'validate': 'list',
                                 'source': ['Approved', ' Rejected', 'Partially Approved']})

workbook.close()
