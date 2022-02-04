# All dictionary Program


# Print the function in Dictionary
def dict_print():
    dict_var = {'No1': 1, 'No2': 2, 'No3': 3, 'No4': 4, 'No5': 5}
    print("Print the function in Dictionary:", dict_var)


# Removes all the elements from the dictionary
def dict_clear():
    dict_var = {'No1':21, 'No2':25, 'No3': 28, 'No4': 30, 'No5': 35, 'No6': 40}
    a = dict_var.clear()
    print("Remove the elements from the dictionary:", a)


# Returns a dictionary with the specified keys and value
def dict_fromkeys():
    dic = {'Fruits': 'Mango', 'Animal': 'Lion', 'Name': 'Mohan', 'Flowers': 'Rose'}
    dic_1 = 1
    b = dict.fromkeys(dic,dic_1)
    print("Returns a dictionary with the specified keys and value:", b)


# Returns a copy of the dictionary
def dict_copy():
    dict_var = {'Fruits': 'Mango', 'Animal': 'Lion', 'Name': 'Mohan', 'Flowers': 'Rose'}
    a = dict_var.copy()
    print("Returns a copy of the dictionary:", a)


# Returns a list containing a tuple for each key value pair
def dict_items():
    dic = {'FirstName': 'Mohan', 'Age': 29, 'Address': 'Agra'}
    b = dic.items()
    print("Returns a list containing a tuple for each key value pair:", b)

#Returns the value of the specified key
def dict_get():
    dict_var = {'No1': 1, 'No2': 2, 'No3': 3, 'No4': 4, 'No5': 5}
    b = dict_var.get('No5')
    print("Returns the value of the specified key:", b)

#Returns a list containing the dictionary's keys
def dict_keys():
    dict_var = {'No1': 1, 'No2': 2, 'No3': 3, 'No4': 4, 'No5': 5}
    b = dict_var.keys()
    print("Returns a list containing the dictionary's keys:", b)

#Removes the element with the specified key
def dict_pop():
    dict_var = {'No1': 1, 'No2': 2, 'No3': 3, 'No4': 4, 'No5': 5}
    b = dict_var.pop('No2')
    print("Removes the element with the specified key:", b)

#Removes the last inserted key-value pair
def dict_popitems():
    dic = {'FirstName': 'Mohan', 'Age': 29, 'Address': 'Agra'}
    b = dic.popitem()
    print("Removes the last inserted key-value pair:", b)

#Updates the dictionary with the specified key-value pairs
def dict_update():
    dic = {'FirstName': 'Mohan', 'Age': 29, 'Address': 'Agra'}
    dict_var = {'No1': 1, 'No2': 2, 'No3': 3, 'No4': 4, 'No5': 5}
    c = dic.update(dict_var)
    print("Updates the dictionary with the specified key-value pairs:", dic)

# This function returns a list of all the values available in a given dictionary
def dict_values():
    dic = {'FirstName': 'Mohan', 'Age': 29, 'Address': 'Agra'}
    c = dic.values()
    print("All the values available in a given dictionary:", c)

# Some Other Method
def dict_others():
    dic = {'FirstName': 'Mohan', 'Age': 29, 'Address': 'Agra'}
    list = [1, 2, 3, 4]
    c = type(dic)
    d = type(list)
    print("All the values available in a given dictionary:", c,d)

if __name__ == "__main__":
    dict_print()
    dict_clear()
    dict_fromkeys()
    dict_copy()
    dict_items()
    dict_get()
    dict_keys()
    dict_pop()
    dict_popitems()
    dict_update()
    dict_values()
    dict_others()
