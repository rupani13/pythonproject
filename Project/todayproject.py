# import openpyxl
import pandas as pd

'''
df1 = openpyxl.load_workbook("OfficeM&A_RootWords.xlsx")
print(type(df1))
sheets = df1.sheetnames
print(sheets)
sheet = df1['RootWords']
s = sheet['A12'].value
print(s)
print(sheet.cell(14, 4).value)'''

# find The All data excel particular sheet file

# df2 = openpyxl.load_workbook("OfficeM&A_RootWords.xlsx")
'''sheet1 = df2['RootWords']
row = sheet1.max_row
column = sheet1.max_column
x3 = sheet1.cell(row=3, column=1)
#print(x3.value)
for i in range(1, row+1):
    for j in range(1, column):
        print(sheet1.cell(i, j).value)'''

df = pd.read_excel("OfficeM&A_RootWords.xlsx")
df1 = pd.read_excel("OfficeM&A_RootWords.xlsx", sheet_name='RootWords', usecols="B")
print(df1)
'''df.to_excel("OfficeM&A_RootWords.xlsx", engine='xlsxwriter')

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

workbook.close()'''
