# Pandas Dataframe.describe() method
import pandas as pd

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df[['Age', 'Address']])

# Column Addition
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
Qul = ['BA', 'MBA', 'BTech', 'MBBS']
df['Address'] = address
df['Qualification'] = Qul
print(df)
# Delete Column
df1 = pd.read_csv("Book1.csv", index_col='Number')
df2 = df1.drop(["Number", "Id"], axis=1, inplace=True)
print("Delete Column:", df2)

df3 = pd.read_csv("Book1.csv", index_col="Id")
df4 = df3.loc(["ADI23"])
print("Row:", df4)
