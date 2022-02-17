# From SQL to Pandas DataFrame
import pandas as pd
import pyodbc

data = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HBGGD1G;'
                      'Database=Rupani Test;'
                      'Trusted_Connection=yes;')
df = pd.read_sql_query('SELECT * FROM test_data', data)



print("test_data:", df)
print("SQL to Pandas DataFrame type:", type(df))
