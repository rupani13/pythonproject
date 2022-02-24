import pandas as pd

df = pd.read_csv("Textoutput.csv", usecols=[1, 3])

duplicate_in_image_path = df.duplicated(subset=['Image_Path'])
if duplicate_in_image_path.any():
    print(df.loc[~duplicate_in_image_path], end='\n')



