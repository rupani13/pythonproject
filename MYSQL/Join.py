# Join python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
statement ="SELECT i.item_id,i.item_name,p.Price FROM item i JOIN price p on i.[item_id]=p.[item_id]"
cursorObject.execute(statement)

var1 = cursorObject.fetchall()

for x in var1:
  print(x)
