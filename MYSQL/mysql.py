# using Mssql program
import pyodbc

dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')
cursor = dataBase.cursor()
cursor.execute('SELECT * FROM Rupani')

for i in cursor:
    print(i)

data = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HBGGD1G;'
                      'Database=Rupani Test;'
                      'Trusted_Connection=yes;')
cursor = data.cursor()
cursor.execute('SELECT * FROM test_database')

print("test_database:")
for i in cursor:
    print(i)
