
# Declaring Objects
class Employee:
    def __init__(self, attendance, department, meeting, salary):
        self.attendance = attendance
        self.department = department
        self.meeting = meeting
        self.salary = salary


list1 = [ ]
list1.append(Employee(10, 'Developer', 5, 10000))
list1.append(Employee(12, 'Developer', 5, 10000))
for i in list1:
    print("attendance:", i.attendance)
    print("department:", i.department)
    print("meeting:", i.meeting)
    print("salary:", i.salary)

