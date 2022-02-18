# All Binary numpy program
import numpy as np

var = 9
var1 = 10
out = np.bitwise_and(var, var1)
print("Bitwise and value:", out)
out = np.bitwise_or(var, var1)
print("Bitwise or value:", out)
arr = [12, 15, 17]
arr1 = [11, 15, 21]
out2 = np.bitwise_and(arr, arr1)
print("Bitwise and value:", out2)
out3 = np.bitwise_or(arr, arr1)
print("Bitwise or value:", out3)

# Using invert function
in_num = 8
out_num = np.invert(in_num)
print("inversion of 8 : ", out_num)
in_arr = [5, 10, 15]
out_num1 = np.invert(in_arr)
print("inversion of in arr : ", out_num1)

# Using left shift
num1 = [2, 8, 15]
num2 =[3, 4, 5]     # bit shift
out_num2 = np.left_shift(num1, num2)
print("Left shift : ", out_num2)
out_num2 = np.right_shift(num1, num2)
print("Right shift : ", out_num2)
# Python program explaining binary_repr function
num1 = [2, 8, 15]
out_num3 = np.binary_repr(num1[2])
print("explaining binary_repr function : ", out_num3)