# All Tuple program

def tuple_print():
    tuple_var = (23, 43, 523, 1234)
    print("Print the tuple value", tuple_var)

#finding the length in tuple
def tuple_length_print():
    tuple_var = (12, 9, 7, 5, 3)
    b = len(tuple_var)
    print("Length in the tuple", b)


#It returns an item from the list with max value
def tuple_max():
    tuple_var = (23, 43, 523, 1234)
    a = max(tuple_var)
    print("Mixmum value in the tuple: ", a)

#It returns an item from the list with mim value
def tuple_mim():
    tuple_var = (23, 43, 523, 1234)
    a = min(tuple_var)
    print("Minimum value in the tuple: ", a)

#Add in the tuple
def tuple_add():
    tuple_var = (20, 17, 15, 11, 9, 7, 5)
    a = sum(tuple_var)
    a = sum(tuple_var, 5)
    print("Sum in the tuple:", a)

#Returns the number of times a specified value occurs in a tuple
def tuple_count():
    tuple_var = (20, 17, 15, 11, 9, 7, 5, 9, 15)
    c = tuple.count(tuple_var, 9)
    print("count value in the tuple:", c)


#Returns enumerate object of tuple
def tuple_enumerate():
    tuple_var = (20, 17, 15, 11, 9, 7, 5, 9, 5)
    a = enumerate(tuple_var)
    print("Enumerate value in the tuple:", tuple(enumerate(tuple_var)))

#Input elements in the tuple and return a new sorted list
def tuple_sorted():
    tuple_var = (20, 17, 15, 11, 9, 7, 5)
    c = sorted(tuple_var)
    print("Sorted value in thetuple:", c)

#Convert an iterable to a tuple
def tuple_tuple():
    tuple_var = (20, 17, 15, 11, 9, 7, 5, 9, 5)
    b = tuple(tuple_var)
    print("Convert an iterable to a tuple:", b)

#creating a tuple using list
def tuple_list():
    list = [20, 17, 15, 11, 9, 7, 5]
    b = tuple(list)
    print("creating a tuple using list:", b)

# Creating a tuple mix datatype
def tuple_mixdata():
    tuple1 = (20, 15, 'Apple', 245 )
    tuple2 = (20, 17, 15, 11, 9)
    tuple3 = ('banana', 'Grapes', 20, 15, 9)
    tuple3 = (tuple1, tuple2)
    print("Creating a tuple mix datatype:", tuple3 )

#Slicing of a Tuple
def tuple_slicing():
    tuple_var = ('GEEKSFORGEEKS')
    print("Slicing of a Tuple:", tuple_var[1:])
    print("Slicing of a Tuple:", tuple_var[4:9])


if __name__ == "__main__":
    print("Tuple Data Structure")
    tuple_print()
    tuple_length_print()
    tuple_max()
    tuple_mim()
    tuple_add()
    tuple_count()
    tuple_enumerate()
    tuple_sorted()
    tuple_tuple()
    tuple_list()
    tuple_mixdata()
    tuple_slicing()
