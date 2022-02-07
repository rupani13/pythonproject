#class Programming

#Declaring Objects
class Employee:
  def __init__(self, attendance, department, meeting, salary):
    self.attendance = attendance
    self.department = department
    self.meeting = meeting
    self.salary = salary

p1 = Employee(10,'finance', 5, 10000)

print(p1.attendance)
print(p1.department)
print(p1.meeting)
print(p1.salary)

