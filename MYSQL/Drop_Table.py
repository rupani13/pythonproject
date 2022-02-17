# Drop Table python mssql program

import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
statement = "Drop Table fruit_detial"

cursorObject.execute(statement)
sql = "DROP TABLE IF EXISTS fruit_detial"
cursorObject.execute(sql)