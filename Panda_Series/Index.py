# Use Index function to convert the index into a list
import pandas as pd
df = pd.Index(['Harry', 'Mike', 'Arther', 'Nick'],
                                  name ='Student')
df1 = df.tolist()
print("function to convert the index into a list:", df, df1)

df1 = pd.read_csv("Series_New.csv")
df2 = df1['ID'].tolist()
print("function to convert the index into a list1:", df2)