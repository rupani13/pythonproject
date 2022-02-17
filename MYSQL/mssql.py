# using Mssql program
import pyodbc

dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')
cursor = dataBase.cursor()
df = cursor.execute('SELECT * FROM item')

print("Item database:", df)
for i in cursor:
    print(i)