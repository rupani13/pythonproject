# All NameSpace Program

globals() ['x'] = 115
globals()
print(x)

# Local And enclosing Program


def fun():
    print("Here no local variable  is present : ", locals())


# here local variables are present
def obj():
    name = "The_Book"
    print("Here local variables are present : ", locals())
    print("Before updating name is  : ", name)
    locals()['name'] = "Ramayana"
    print("after updating name is : ", name)


# driver code
fun()
obj()
