# Numpy Program
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
print(arr.shape)

dt = np.dtype('>i4')
print("Byte order is:", dt.byteorder)
print("Size is:", dt.itemsize)
print("Data type is:", dt.name)

arr1 = np.array([1.1, 2.1, 3.1])
var1 = arr1.astype(int)

print(var1)
print(var1.dtype)
dt = np.dtype([('name', np.unicode_, 16),
               ('grades', np.float64, (2,))])
x = np.array([('Sarah', (8.0, 7.0)),
              ('John', (6.0, 7.0))], dtype=dt)

print(x[1])
print("Grades of John are: ", x[1]['grades'])
print("Names are: ", x['name'])
