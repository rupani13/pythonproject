# OOPs in Overloading Program

class Name:
    def __init__(self, name):
        self.name = name

    def __add__(self, a):
        return self.name + a.name


obj1 = Name("Gora")
obj2 = Name("Shiv")
obj3 = Name("Sita")
obj4 = Name("Ram")

print("Add Obj1 & Obj2:", obj1 + obj2)
print("Add Obj3 & Obj4:", obj3 + obj4)


# Overloading Function
class A:
    def __init__(self, a):
        self.a = a

    def __get__(self, owner):
        if self.a > owner.a:
            print("Greater Than Value")
        else:
            print("Less Than Value")


obj = input('Enter the object value obj:')
obj1 = input('Enter the object value obj1:')
if obj > obj1:
    print("Greater Than Value Ob1")
else:
    print("Less Than Value Obj")
