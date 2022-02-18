# All indexing numpy program
import data_type as np

list1 = [[-1, 2, 0, 4],
         [4, -0.5, 6, 0],
         [2.6, 0, 7, 8],
         [3, -7, 4, 2.0]]

arr = np.array(list1)
print('4th element on 2nd row: ', arr[1, 3])
print('4th element on 3nd row: ', arr[2, 3])

var = arr[:2, ::2]
var1 = arr[:3, ::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n", var)
print("Array with first 2 rows and alternate columns(0 and 2):\n", var1)
print("Array with first datatype:\n", arr.dtype, type(arr))

arr1 = arr.reshape((2, 2, 4))
print("\nOriginal array:\n", arr)
print("Reshaped array:\n", arr1)
arr2 = arr.flatten()

print("\nOriginal array:\n", arr)
print("Fattened array:\n", arr2)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp)

# boolean array indexing example using boolean condition
cond = arr > 0
var3 = arr[cond]
print("\nElements greater than 0:\n", var3)
cond = arr < 0
var3 = arr[cond]
print("\nElements less than 0:\n", var3)
