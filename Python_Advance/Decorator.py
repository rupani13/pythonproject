# All Python Decorators Program
#  Passing the function as an argument
def Adder(x):
    def adder(y):
        return x + y

    return adder


add_1 = Adder(25)

print(add_1(15))


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")
        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))
