# All Mathematical program
import numpy as np


list1 = [[6, 1, 1],
         [4, -2, 5],
         [2, 8, 7]]
arr = np.array(list1)
print("Rank of A:", np.linalg.matrix_rank(arr))
print("\nTrace of A:", np.trace(arr))
print("\nDeterminant of A:", np.linalg.det(arr))
print("\nInverse of A:\n", np.linalg.inv(arr))
print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(arr, 2))
# Vector Algebra
vector1 = 2 + 3j
vector2 = 4 + 5j
product = np.dot(vector1, vector2)
print("Dot Product  : ", product)
pro = np.vdot(vector1, vector2)
print("VDot conjugate of vector  : ", pro)
