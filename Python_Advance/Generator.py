# All Generator Program
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(3)   # Create a generator object
print("Using for in loop")
for i in fib(3):
    print(i)