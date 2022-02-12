# All Static Method program
class Calculator:
    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2


Calculator.add = staticmethod(Calculator.add)   # using static method
sum1 = Calculator.add(8, 10)
print('calculater in sum:', sum1)

Calculator.sub = staticmethod(Calculator.sub)
sub1 = Calculator.sub(10, 7)
print('calculater in sub:', sub1)

Calculator.mul = staticmethod(Calculator.mul)
multiple = Calculator.mul(5, 16)
print('calculater in multiple:', multiple)

Calculator.div = staticmethod(Calculator.div)
div1 = Calculator.div(10, 6)
print('calculater in division:', div1)
