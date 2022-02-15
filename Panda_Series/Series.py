# All Panda Series Program
import pandas as pd

df = pd.read_csv("Series_New.csv")
df1 = df.head(5)
# print(df1)
df2 = pd.DataFrame(df)
print(df2.columns)
# converting to list
df3 = type(df["Salary"])
print("Type od function:", df3)
list1 = df2['ID'].tolist()
df4 = type(df["Salary"])
#list2 = list(df["Salary"])
print('extract the value of series and converting into the list', list1)
print("Data type before converting = {}\nData type after converting = {}".format(df3, df4))
