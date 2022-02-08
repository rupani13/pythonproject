# Pyton Function

# Create A Function

def create():
    print("The_Book")


create()

# Multiple Value Using Function


def multiple(a, b):
  mul = a * b
  return (mul, a)


mul, a = multiple(5, 10)

print("Print The Sum Value:", mul)