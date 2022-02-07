# Declaring Objects
class Number:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sum(self):
        sum1 = self.x+self.y+self.z
        print("Number to sum value:", sum1)

    def multiple(self):
        Multiple1 = self.x*self.y*self.z
        print("Number to multiple value:", Multiple1)

list1 = []
list1.append(Number(10, 9, 5))
list1.append(Number(12, 10, 8))
for i in list1:
    i.sum()
    i.multiple()

