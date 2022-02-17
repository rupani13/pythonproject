# Order By Clause python mssql program
import pyodbc
dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
statement = "SELECT * FROM Student1 ORDER BY Student_Name"
cursorObject.execute(statement)
set1 = cursorObject.fetchall()
print("Ascending order by name:")
for x in set1:
    print(x)

stat = "SELECT * FROM Student1 ORDER BY Student_Name DESC "
cursorObject.execute(stat)
set2 = cursorObject.fetchall()
print("Descending order by name:")
for x in set2:
    print(x)
dataBase.close()