import pandas as pd

df = pd.read_csv("Textoutput.csv")

duplicate_in_image_path = df.duplicated(subset=['Image_Path'])
if duplicate_in_image_path.any():
    print(df.loc[~duplicate_in_image_path], end='\n')

df1 = pd.DataFrame(duplicate_in_image_path)
df1.to_csv("student.csv", mode='a', index=False, header=False)