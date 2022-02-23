# Dublicate not remove just adjust in csv file using pandas

import pandas as pd

var1 = pd.set_option("display.max_row", 74)
var2 = pd.set_option("display.max_column", 6)
fun = pd.read_csv("Textoutput.csv")
print(fun)
print("Duplicate:", fun.duplicated(subset=['Image_Path']))
print(fun.duplicated().sum())
print("duplicate here", fun['Image_Path'].duplicated().sum())  # how to many duplicate here
print("Remove duplicate:", fun[fun.duplicated('Image_Path')])
fun.sort_values('Image_Path', inplace=True)
df = fun.drop_duplicates(subset='TEXT', keep=False, inplace=True)
fun.pop(['Image_Path'])

print(df)
