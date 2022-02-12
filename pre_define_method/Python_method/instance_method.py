# All Instance Method program
class Student:
    def __init__(self, name, roll_no):
        self.name = name                  # Instance variable
        self.roll_no = roll_no            # Instance Variable

    def class1(self):                      # Instance Method
        return self.name, self.roll_no


s1 = Student("Ram", 10)
print("Student name, roll_no:", s1.name, s1.roll_no)

s2 = Student("Shiv", 9)
print("Student name, roll_no:", s2.name, s2.roll_no)
