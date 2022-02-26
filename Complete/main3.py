import pandas as pd

df = pd.read_csv("Textoutput.csv", usecols=[1, 3])

df1 = df.groupby('Image_Path')['TEXT'].apply(list).rename('Path').reset_index()
print(df1)
duplicate_in_image_path = df1.duplicated(subset=['Image_Path'])
if duplicate_in_image_path.any(False):
    df3 = df.loc[~duplicate_in_image_path]
    print("Only False Value:", df3, end='\n')
df2 = duplicate_in_image_path("Final_out.csv", index=False)
