# All Class Method Program
class Employee:
    def __init__(self, Name, Id, Stream):
        self.Name = Name
        self.Id = Id
        self.Stream = Stream

    def company(self):
        return self.Name, self.Id, self.Stream


E1 = Employee("Ravi", 'sab123', "Developer")
A = Employee.company(E1)
print(A)


# Using class method
class Fruit:
    name = 'Apple', "Banana"

    def sweet(var):
        print("Fruit name is:", var.name)


Fruit.sweet = classmethod(Fruit.sweet)
Fruit.sweet()





