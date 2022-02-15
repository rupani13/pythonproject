# Using All metacharacter
import re

df = "The Book . Name Good Value 1834"
var = re.search("", df)
print("One of the metachar:", var)
var1 = re.search("", df)
print("Two of the metachar:", var1)
var2 = re.compile('\d')
print("var2:", var2.findall(df))
var3 = re.compile('\d+')
print("var3:", var3.findall(df))
var4 = re.compile('\D')
print("var4:", var4.findall(df))
var5 = re.compile('\w')
print("var5:", var5.findall(df))
var6 = re.compile('\B')
print("var6:", var6.findall(df))