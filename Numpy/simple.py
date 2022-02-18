# Simple program in numpy using list
import data_type as np

list1 = [12, 15, 17, 20]
arr = np.array(list1)
print("print the list in array:", arr)
print("Value the list type of array:", type(arr))
print("Value the list type of array:", arr.shape)
print("Value the list type of array:", arr.size)
print("Value the list type of array:", arr.dtype)
print(np.__version__)

# Simple program in numpy using tuple
tup = (12, 15, 17, 20)
arr1 = np.array(tup)
print("print the tuple in array:", arr1)
print("print the tuple in array:", arr1.dtype)
print("print the tuple in array:", arr1.shape)
print("print the tuple in array:", arr1.size)
print("print the tuple in array dimension:", arr1.ndim)


# Simple program in numpy using dictionary
dis = {'Name': 'Soni', 'Age': 25}
arr2 = np.array(dis)
print("print the tuple in array:", arr2)


# using another array

list2 = [[1, 2, 4], [5, 8, 7]]
var2 = np.array(list2)
arr3 = np.zeros((2, 2))
print("An array initialized with all zeros:\n", arr3)
# Create a constant value array of complex type
arr4 = np.full((2, 2), 3, dtype='complex')
print("An array initialized complex values:\n", arr4)
# Create an array with random values
arr5 = np.random.random((2, 2))
print("An array initialized random values:\n", arr5)
# Create a sequence of 10 values in range 0 to 5
var3 = np.linspace(0, 5, 10)
print("An array initialized range:\n", arr5)
