# Limit Clause python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
set1 ="SELECT top 3 * FROM item_value "
cursorObject.execute(set1)
var1 = cursorObject.fetchall()
print("Limit Clause python:")
for x in var1:
    print(x)
