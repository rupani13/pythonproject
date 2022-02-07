# single inheritance program

class Parent:
    def fun(self):
        list1 = ("Name")
        print("This function is in parent class:", list1)

class Child(Parent):
    def fun1(self):
        list2 = ("Student", "Shiva")
        print("This function is in child class:", list2)


obj = Child()
obj.fun()
obj.fun1()




