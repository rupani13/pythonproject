# All Iterating numpy program
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print('array is:')
for x in arr:
    print(x)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print('array is arr1:')
for x in arr1:
    for y in x:
        print(y)
# Iterate through the array as a string
arr3 = np.array([1, 2, 3])
for x in np.nditer(arr3, flags=['buffered'], op_dtypes=['S']):
    print(x)

# using npiter
var = np.arange(12)
print(var)
var1 = var.reshape(3, 4)
print('Original array is:', var)
print('Modified array is:')
# iterating  an array
for x in np.nditer(var):
    print(x)
# Modified array in F-style order
print('Modified array in F-style order:')
for x in np.nditer(var, order='F'):
    print(x)
# iterating array values using external loop
print('Modified array is using external loop:')
for x in np.nditer(var, flags=['external_loop'], order='C'):
    print(x)
