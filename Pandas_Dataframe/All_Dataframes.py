import pandas as pd

var = pd.read_csv("Employee.csv")
print(var.head())

#
list1 = pd.DataFrame({"A": [1, 5, 3, 4, 2],
                      "B": [3, 2, 4, 3, 4],
                      "C": [2, 2, 7, 3, 4],
                      "D": [4, 3, 6, 12, 7]},
                     index=["A1", "A2", "A3", "A4", "A5"])
df = pd.DataFrame({"A": [10, 11, 7, 8, 5],
                   "B": [21, 5, 32, 4, 6],
                   "C": [11, 21, 23, 7, 9],
                   "D": [1, 5, 3, 8, 6]},
                  index=["A1", "A2", "A3", "A4", "A5"])

df1 = list1.sub(df)
print(df1)
df2 = list1.add(df)
print(df2)
df3 = df.nunique(axis=1)
print(df3)
