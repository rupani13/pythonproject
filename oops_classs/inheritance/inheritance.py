# inheritance program

class School:
    def __init__(self, class1, name):
        self.class1 = class1
        self.name = name

    def class_Student(self):
        print("Student Class:", self.class1)
        print("Student Name:", self.name)

    def student1(self):
        pass


class Teacher(School):
    def student1(self):
        print("Teacher class:", self.class1)
        print("Teacher Name:", self.name)


stu = School(7, "Ram")
stu = Teacher(8, "Shiva")
# print("Student class:", stu.class_Student(), stu.student1())
stu.class_Student()
stu.student1()
