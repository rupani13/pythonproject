import pandas as pd

df = pd.read_csv("Textoutput.csv", usecols=[1, 3])

df1 = df.drop_duplicates(subset=['Image_Path', 'TEXT'])
#print(df1)
duplicate = df.duplicated(subset=['Image_Path']).any()
print(duplicate)

duplicate_in_image_path = df.duplicated(subset=['Image_Path'])
if duplicate_in_image_path.any(False):
    df3 = df.loc[~duplicate_in_image_path]
    print("Only False Value:", df3, end='\n')

for dup in duplicate_in_image_path:
    list1 = []
    df1 = list1.append(dup)
    df2 = df1.to_csv("Out.csv")
