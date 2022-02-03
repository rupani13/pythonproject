# All List program

def list_print():
    list = ['23', '43', '523', '1234']
    print(list)

#Sorts the list in ascending order
def list_sorts_print():
    list = [12, 9, 7, 5, 3]
    list.sort()
    print("ascending orde in the list: ", list)

#It returns the class type of an object
def list_type_object():
    list = ['23', '43', '523', '1234']
    type(list)
    print("print type object in the list: ", list)
#Adds a single element to a list
def list_add():
    list = ['23', '43', '523', '1234']
    list.append('45')
    print("add value in the list: ", list)

#Returns the first appearance of the specified value
def list_index():
    list = [13, 11, 5, 7]
    list.index(7)
    print("Index value in the list: ", list[3])

#Adds multiple elements to a list
def list_extend():
    list = ['Apple', 'Banana', 'grapes', 'Mango']
    list.extend(['Strawberry'])
    print("extend value in the list: ", list)

#It returns an item from the list with max value
def list_max():
    list = [15, 13, 11, 9, 7, 5, 3]
    a = max(list)
    print("Mixmum value in the list: ", a)

#It returns an item from the list with mim value
def list_min():
    list = [15, 13, 11, 9, 7, 5, 3]
    a = min(list)
    print("Minimum value in the list: ", a)

#It gives the total length of the list
def list_len():
    list = ['Apple', 'Banana', 'grapes', 'Mango']
    b = len(list)
    print("Length in the list:", b)

#Converts a tuple into a list
def list_convert_tuple():
    tuple_var = (15, 13, 11, 9, 7, 5, 3)
    print("list convert tuple in the list: ", list(tuple_var))

#It removing elements from the lists
def list_remove():
    list = [15, 13, 11, 9, 7, 5, 3]
    list.remove(9)
    print(list)

#It pop method from the lists
def list_pop():
    list = [15, 13, 11, 9, 7, 5, 3]
    list.pop()
    list.pop()
    print(list)

#Slicing in list
def list_slicing():
    list = [15, 13, 11, 9, 7, 5, 3]
    list_slicing = list[2:6]
    print(list_slicing)
if __name__ == "__main__":
    list_print()
    list_sorts_print()
    list_type_object()
    list_add()
    list_index()
    list_extend()
    list_max()
    list_min()
    list_len()
    list_convert_tuple()
    list_remove()
    list_pop()
    list_slicing()