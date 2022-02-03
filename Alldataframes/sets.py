# All Sets program

def sets_print():
    sets_var = set([23, 43, 523, 1234])
    string = "Apple"
    sets_var1 = set(string)
    print("Print the sets value:", sets_var)
    print("Print the string value:", sets_var1)

#finding the add in sets
def sets_add():
    sets = {12, 11, 10}
    sets.add("9")
    print("add in the sets:", sets)

#Removes all the elements from the set
def sets_removes():
    sets = {12, 11, 10}
    sets.clear()
    print("clear in the sets:", sets)

#Returns a copy of the set
def sets_copy():
    sets = {12, 11, 10}
    sets.copy()
    print("copy in the sets:", sets)

#Returns a set containing the difference between two or more sets
def sets_difference():
    sets1 = {12, 11, 10}
    sets2 = {13, 12,11}
    c = sets1.difference(sets2)
    print("difference in the sets:", c)

#Removes the items in this set that are also included in another, specified set
def sets_difference_update():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 12, 11, 9}
    c = sets1.difference_update(sets2)
    print("difference_updating in the sets:", sets2)

#Remove the specified item
def sets_discard():
    sets = {12, 11, 10, 5}
    c = sets.discard(12)
    print("discard in the sets:", sets)

#Returns a set, that is the intersection of two or more sets
def sets_intersection():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 12, 11, 9}
    c = sets1.intersection(sets2)
    print("intersection in the sets:", c)

#Removes the items in this set that are not present in other, specified set(s)
def sets_intersection_update():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 12, 11, 9}
    c = sets1.intersection_update(sets2)
    print("intersection in the sets:", sets2)

#Returns whether two sets have a intersection or not
def sets_intersection_update():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 6, 8, 9}
    c = sets1.isdisjoint(sets2)
    print("intersection in the sets:", c)

#Removes an element from the set
def sets_pop():
    sets1 = {12, 11, 10}
    c = sets1.pop()
    print("Removes an element from the set:", c)

#Removes the specified element
def sets_remove():
    sets1 = {12, 11, 10}
    c = sets1.remove(12)
    print("Removes the specified element:", sets1)

#Returns a set with the symmetric differences of two sets
def sets_symmetric():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 6, 8, 9}
    c = sets1.symmetric_difference(sets2)
    print("Returns a set with the symmetric differences of two sets:", c)

#Return a set containing the union of sets
def sets_union():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 6, 8, 9, 10}
    c = sets1.union(sets2)
    print("Return a set containing the union of sets:", c)

#Update the set with another set, or any other iterable
def sets_update():
    sets1 = {12, 11, 10, 5}
    sets2 = {13, 6, 8, 9,11}
    c = sets1.update(sets2)
    print("Update the set with another set, or any other iterable:", sets1)

if __name__ == "__main__":
    sets_print()
    sets_add()
    sets_removes()
    sets_copy()
    sets_difference()
    sets_difference_update()
    sets_discard()
    sets_intersection()
    sets_intersection_update()
    sets_pop()
    sets_remove()
    sets_symmetric()
    sets_union()
    sets_update()
