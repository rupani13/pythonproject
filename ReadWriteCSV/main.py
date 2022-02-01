# Problem statement : write program read and write csv file from pandas

import pandas as pd

#read the csv file
print("Reading the CSV file")
df = pd.read_csv("student.csv")
print(df)

# write in the csv file
data = {
    'rollno': [7, 8],
    'name': ['sita', 'gita'],
    'subject': ['math', 'Physics'],
    'class': [10, 9]
}
df1 = pd.DataFrame(data)
df1.to_csv("./student.csv", mode='a', index=False, header=False)
print("Successfully Added the data in the CSV file")
df = pd.read_csv("student.csv")
print(df)
