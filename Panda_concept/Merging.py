# Pandas Merging, Joining, and Concatenating
import pandas as pd

# Concatenating DataFrame using
data = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi'],
        'Age': [27, 24, 22, 32],
        'Address': ['Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data, index=[1, 2, 3, 4])
df1 = pd.DataFrame(data2, index=[5, 6, 7, 8])
frames = [df, df1]
res1 = pd.concat(frames)
print(res1)
# applying concat with axes with join
res2 = pd.concat(frames, axis=1, join='inner')
print("concat with axes with join:\n", res2)
res3 = df.append(df1)
print("Using Append Function:\n", res3)
# Ignoring Index
res4 = pd.concat(frames, ignore_index=True)
print("Ignoring Index Function:\n", res4)
res5 = pd.concat(frames, keys=['x', 'y'])
print("Using Keys Function:\n", res5)

# Merge Concept
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32], }

# Define a dictionary containing employee data
data3 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df2 = pd.DataFrame(data1)
df3 = pd.DataFrame(data3)
var = pd.merge(df2, df3, on='key')
print(var)
# In merge left function using
var1 = pd.merge(df2, df3, how='left', on='key')
print("merge left function using:\n", var1)
