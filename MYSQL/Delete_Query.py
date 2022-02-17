# Delete Query python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
query = "DELETE FROM fruit WHERE Fruit_Sweet = 'Sour'"
cursorObject.execute(query)

attrValues = "DELETE FROM fruit WHERE Fruit_Name = 'Apple'"
cursorObject.execute(attrValues)

dataBase.commit()
print(cursorObject.rowcount, "record(s) deleted")
# disconnecting from server
dataBase.close()