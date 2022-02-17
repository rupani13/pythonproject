# Where clause python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
sql = "select * from student where Name>= 'Rit Saha'"
sql1 = "select * from student where Section>= 'IT-3'"
cursorObject.execute(sql)
cursorObject.execute(sql1)
result1 = cursorObject.fetchall()
for x in result1:
    print(x)

dataBase.close()