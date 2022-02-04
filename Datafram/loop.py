# All Dataframe using loop Program
#1. List using loop program

def list_value():
    list  = [10, 15, 20, 'Number', 'Name', 'Class']
    for i in list:
        print("All iterable Values:", i)

#1.Tuple using loop program
def tuple_value():
    tuple1 = (10, 15, 20, 'Number', 'Name')
    for i in tuple1:
        print("All iterable Values:", i)

#3.Sets using loop program
def sets_value():
    sets = {5, 8, 9, 11, 15}
    for i in sets:
        print("All iterable Values:", i)

#Programthe sum of all numbers stored in a list ,tuple
def list_tuple_sum():
    a = [5, 8, 9, 11, 15]
    b = 0
    for i in a:
        b = b + i
    print("All Sum Value:", b)



if __name__ == "__main__":
    list_value()
    tuple_value()
    sets_value()
    list_tuple_sum()