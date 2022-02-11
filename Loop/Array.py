# All Array Program

import array as arr
a = arr.array('b', [1, 2, 3, 4])
print("The new created array is : ")
for i in range(0, 3):
    print(a[i], end=" ")

# Accessing elements from the Array
a1 = arr.array('i', [1, 2, 3, 4, 5, 6])

print("\n Access element is: ", a1[0])
print("Access element is: ", a1[3])

# Removing Elements from the Array

arr1 = arr.array('i', [1, 2, 3, 1, 5])

print("The new created array is : ", end="")
for i in range(0, 4):
    print(arr1[i], end=" ")
print(arr1.pop(1))

# Searching element in a Array

arr2 = arr.array('i', [1, 2, 3, 1, 2, 5])

print("The new created array is : ")
for i in range(0, 6):
    print(arr2[i], end=" ")
print("\nThe index of occurrence: ", end="")
print(arr2.index(1))