# Global Variable

list1 = []


def fun():
    global list1
    list2 = "The_Book"
    list1.append(list2)


fun()
print("List yhe value:", list1)
