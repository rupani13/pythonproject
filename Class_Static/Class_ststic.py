# Using class method in static


class Employee:
    def __init__(self, name, Id, salary):
        self.name = name
        self.Id = Id
        self.salary = salary

    @staticmethod
    def fun(salary):
        return salary >= 10000


Employee1 = Employee('Mayank', 'ABC12', 9000)
Employee2 = Employee('Rohit', 'DEF24', 10000)

print(Employee1.salary)
print(Employee2.salary)

print(Employee.fun(11000))

