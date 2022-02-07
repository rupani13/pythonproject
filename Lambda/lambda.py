# Lambda Program

def cube(y):
    return y * y * y


obj = lambda x: x * x * x
print(obj(8), cube(10))

# In side the function using lambdq


def Power(n):
    return lambda a: a ** n


base = Power(5)
print("Now power is set to 5")
print("6 Power_of 2 = ", base(6))
base = Power(3)
print("Now power is set to 3")
print("3 power_of 2 = ", base(3))