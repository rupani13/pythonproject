# OOP in Multilevel Inheritance Program
class Grandfather:

    def __init__(self, grand_father_name):
        self.grand_father_name = grand_father_name


# Intermediate class 1
class Father(Grandfather):
    def __init__(self, father_name, grand_father_name):
        self.father_name = father_name

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grand_father_name)


# Derived class
class Son(Father):
    def __init__(self, son_name, father_name, grand_father_name):
        self.son_name = son_name

        # invoking constructor of Father class
        Father.__init__(self, father_name, grand_father_name)

    def print_name(self):
        print('Grandfather name :', self.grand_father_name)
        print("Father name :", self.father_name)
        print("Son name :", self.son_name)


#  Driver code
obj = Son('Shiva', 'Ramp', 'Mani')
print(obj.grand_father_name)
obj.print_name()
