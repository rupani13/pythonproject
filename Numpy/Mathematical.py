# All Mathematical program
import numpy as np
# Trigonometric Functions
import math

arr = [0, math.pi / 2, np.pi / 3, np.pi]
print("Input array : \n", arr)

Sin = np.sin(arr)
print("\nSine values : \n", Sin)
cos = np.sin(arr)
print("\ncos values : \n", cos)
deg = np.degrees(arr)
print("\ndegree values :", deg)
reg = np.rad2deg(arr)
print("\ndegree values :", reg)

# Hyperbolic Functions
tab = np.tanh(arr)
print("\ntanh values :", tab)
# Functions for Rounding
var = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
rou = np.around(var)
print("\nRounded values : \n", rou)
roun = np.round_(var, decimals=1)
print("\nRounded values roun : \n", roun)
ro = np.fix(var)
print("\nFix values : \n", ro)
# Exponents and logarithms Functions
var1 = [11, 13, 15, 2*6]
var2 = [5, 19, 17, 21]
out = np.exp(var1)
print("Exponents and logarithms Functions : ", out)
out1 = np.log(var1)
print("Exponents and logarithms Functions log : ", out1)
out2 = np.logaddexp(var1, var2)
print("Exponents and logarithms Functions logadd : ", out2)

# Complex number Function
list1 = [1+1j, 0j]
fun = np.isreal(list1)
print("Complex number Function:",fun)
com = 3+5j
fun1 = np.conj(com)
print("Complex number Function fun:", fun1)