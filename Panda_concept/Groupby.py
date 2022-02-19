# All Group By Program
import pandas as pd

data = {'Name': ['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age': [27, 24, 22, 32,
                33, 36, 27, 32],
        'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                    'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd',
                          'B.Tech', 'B.com', 'Msc', 'MA']}

df = pd.DataFrame(data)
print("The value in data:\n", df)
var = df.groupby('Age')
for name, group in var:
    print(name)
    print(group)
    print()
print(var.sum())
print(var.groups)
