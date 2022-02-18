# All String program
import numpy as np
# Python program explaining lower function
print(np.char.lower(['The_Book', 'Ramayana']))
# Python program explaining split function
print("explaining split function:", np.char.split(['Apple', 'Banana']))
# Python program explaining join function
print("explaining split function:", np.char.join('-', 'Banana'))
# Python program explaining refind function
arr = ['The_Book', 'Ramayana']
var1 = np.array(arr)
print("explaining rfind function:", np.char.rfind(arr, 'The_Book'))
# Python program explaining capital  function
print("explaining capitalize function:", np.char.capitalize(arr))

