# Indexing and Selecting Data with Pandas
import pandas as pd

df = pd.read_csv("Book1.csv", index_col='Number')
first = df[["Id", 'Steam']]
print("retrieving columns by indexing operator:", first)
var = df.loc[2]
print("retrieving columns by loc Method:", var)
# multiple selecting row
var1 = df.loc[[2, 3]]
print("retrieving columns by multiple loc Method:", var1)
var3 = df.loc[:, ["Name", "Id", "List"]]
print("retrieving columns by multiple loc Method:", var3)
row2 = df.iloc[3]
print("retrieving rows by iloc method:", row2)
row1 = df.iloc[[3, 4], [1, 2]]
print("retrieving two rows and two columns by iloc method:", row1)
