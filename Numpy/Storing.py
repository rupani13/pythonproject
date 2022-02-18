# All  Sorting, Searching and Counting Program
import numpy as np

arr = np.array([[12, 15], [10, 1]])
arr1 = np.sort(arr, axis=0)
print("Along first axis : \n", arr1)
arr2 = np.array([1, 2, 3, 4, 5, 6])
var = np.argsort(arr2)
print('Sorted indices of original array->', var)
var1 = np.zeros(len(var), dtype=int)
for i in range(0, len(var)):
    var1[i] = arr2[var[i]]
print('Sorted array->', var1)

# Numpy array created column
var2 = np.array([12, 15, 17, 19])
var3 = np.array([5, 13, 14, 16])
print('column var2, column var3')
for (i, j) in zip(var2, var3):
    print(i, j)

# Searching
fun = np.arange(9).reshape(3, 3)
print("\nMax element : ", np.argmax(fun))
print(("\nIndices of Max element : ", np.argmax(fun, axis=0)))
print(("\nIndices of Max element : ", np.argmax(fun, axis=1)))

fun1 = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
fun2 = np.count_nonzero(([[0, 1, 7, 0, 0], [3, 1, 0, 2, 19]]))

print("Number of nonzero values is :", fun1)
print("Number of nonzero values is :", fun2)
