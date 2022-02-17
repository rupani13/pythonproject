# Select Query in python program
import pyodbc

dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursorObject = dataBase.cursor()
print("Displaying NAME and ROLL columns from the STUDENT table:")

# selecting query
query = "SELECT Name, Roll_No FROM student"
query1 = "SELECT Section,Age FROM student"
query2 = "SELECT *FROM student"
cursorObject.execute(query)
cursorObject.execute(query1)
cursorObject.execute(query2)

result1 = cursorObject.fetchall()

for x in result1:
    print(x)

dataBase.close()