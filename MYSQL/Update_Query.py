# Update Query python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()

sql = "UPDATE item_value SET item_name = 'Tap' WHERE item_name = 'Oven'"
cursorObject.execute(sql)
dataBase.commit()
