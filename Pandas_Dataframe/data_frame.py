# All Pandas Dataframe Program
import pandas as pd

list1 = [12, 15, 17, 18]
var = pd.DataFrame(list1)
print(var)

var1 = pd.DataFrame(list1, columns=['Name'])
print(var1)

# DataFrame from dict

list2 = {'Name_Boy': ['Tom', 'nick', 'krish', 'jack'],
         'Age': [20, 21, 19, 18]}

var2 = pd.DataFrame(list2)
print(var2)
