# Insert the data in Multiple Rows
import pyodbc

dataBase = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-HBGGD1G;'
                          'Database=Rupani Test;'
                          'Trusted_Connection=yes;')

cursor1 = dataBase.cursor()

sql = "INSERT INTO customers (customerId,CustomerName,ContactName, Address,City) VALUES (6, 'Kany', 'Peter', 'Lowstreet', 'Mumbai'),(7, 'Many', 'Sweet', 'Lowstreet', 'Mumbai')"

print("insert into ")
cursor1.execute(sql)

dataBase.commit()

print(cursor1.rowcount, "was inserted.")
dataBase.close()
