# Python Function All Program

# Python Function With Argument


def fun(x):
    if x % 2 == 0:
        print("The value even:")
    else:
        print("The value odd:")


fun(5)


# Function expects 2 arguments
def fun(L1, L2):
    print(L1, "", L2)


fun("Email", "Book")


# Function Arbitrary Argument

def fun(*subject):
    print("The Subject:", subject[1])


fun("Math", "Physics", "History", "Social_science")


# Function Keywords Argument


def function(child3, child2, child1):
    print("The middle child is " + child2)


function(child1="Emil", child2="Tobias", child3="Linus")


# Function Arbitrary Keyword Arguments


def function(**child3):
    print("The child is " + child3['child1'])


function(child1="Emil", child2="Tobias")


# Function Arbitrary Keyword Arguments


def Fun(x, y):
    print("The value of x: ", x)
    print("The value of y: ", y)


Fun(20, 21)


def Fun(City="Newyork"):
    print("I am From:"  + City)


Fun("Mumbai")
Fun("LosAngeles")
Fun()

# Function List as an Argument


def function(list1):
    for x in list1:
        print("Print the all List:", x)


list1 = [1, 13, 17, 'The_Book']
function(list1)

# Function in Return Value

def value(x):
    return 2*x


print("Print the value:", value(5))

