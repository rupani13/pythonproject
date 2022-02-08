# First Class functions in Python

def fun(x):
    return x


def fun1(y):
    return fun(y) + y

print(fun1(5))

# First Class another functions in Python


def parent(Name):
    def first_child():
        return "Child Name"

    def second_child():
        return "child By Name"

    if Name == 1:
        return first_child
    else:
        return second_child


var = parent(2)
print(var())
