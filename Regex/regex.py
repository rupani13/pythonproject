# All Regex Program
# import regex
import re

df = "The rain in India"
# Using Search method in regex: Returns a Match object if there is a match anywhere in the string
x = re.search("Search the function:", df)
x1 = re.search("rain", df)
X = re.search("\s", df)
print("Match object if there is a match anywhere in the string:", x1, X.start())
# Using Findall method in regex: Returns a list containing all matches
x2 = re.findall("in", df)
print("list containing all matches:", x2)
# Using split method in regex: Returns a list where the string has been split at each match
x3 = re.split("\s", df)
X1 = re.split("\s", df, 2)
print("list where the string has been split at each match", x3, X1)
# Using sub method in regex: Replaces one or many matches with a string
x4 = re.sub("\s", "5", df)
x5 = re.sub("\s", "5", df, 1)
print("one or many matches with a string:", x4, x5)
# Returns string with all non-alphanumerics backslashes
x9 = re.escape(df)
print("string with all non-alphanumerics:", x9)

# start- and end-position of the first match occurrence
df1 = "The Book Name Good Value"
x6 = re.search(r"\bN\w+", df1)
print("Search in char function:", x6.span())
# Print the part of the string where there was a match in group
df1 = "The Book Name Good Value"
x7 = re.search(r"\bN\w+", df1)
print("Find the group name:", x7.group())
# Print the string passed into the function
df1 = "The Book Name Good Value"
x8 = re.search(r"\bN\w+", df1)
print("Search in string:", x8.string)
