import pandas as pd

df = pd.read_csv("Textoutput.csv", usecols=[1, 3])

df1 = df.groupby('Image_Path')['TEXT'].apply(sum).rename('Path').reset_index()
print(df1)
df2 = df1.to_csv("Final_out.csv", index=False)