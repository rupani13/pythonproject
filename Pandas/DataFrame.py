# All Pandas DataFrame Program
import pandas as pd

# 1. Creating a Pandas DataFrame

df = ['The', 'Book', 'Animal', 'Study']
fun = pd.DataFrame(df)
print("DataFrame:\n", fun)
df1 = {'Subject': ['Math', 'Physics', 'History', 'Chemistry', 'Science'],
       'Mark': [95, 90, 85, 80, 75]}
fun1 = pd.DataFrame(df1)
print("DataFrame:\n", fun1)

# 2. Dealing with Rows and Columns
var = pd.read_csv("Book1.csv")
fun2 = pd.DataFrame(var)
print("DataFrame:\n", fun2[['Name', 'Steam']])

# Row Selection
var1 = pd.read_csv("Book1.csv", index_col='Name')
fun4 = var1.loc['Ram']
print("Row Selection:\n", fun4)

# Indexing and Selecting Data
# 1. Indexing a Dataframe using indexing operator []
first = var1['Id']
print("Indexing a Dataframe using indexing operator:\n", first)

# Selecting a single row
row2 = var1.iloc[3]
print("Selecting a single row:\n", row2)

# 3. Working with Missing Data
df2 = {'Subject': ['Math', 'Physics', 'History', 'na', 'Science'],
       'Mark': [95, 90, 85, '80', 75]}
df3 = pd.DataFrame(df2)
var2 = df3.isnull()
print("Selecting a single row:\n", var2)
var3 = df3.fillna(0)
print("Selecting a single row:\n", var3)

# Dropping missing values using dropna()
var4 = df3.dropna()
print("Dropping missing values using dropna:\n", var4)

# 5. Iterating over rows and columns
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
df5 = pd.DataFrame(dict)
print(df5)