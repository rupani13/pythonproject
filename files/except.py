# Try Except in Python

#def divide(x, y):
def add(X, Y):
    try:
        # Floor Division
        #result = x // y
        result1 = X + Y
        print("The divide value:", result1)
    except ZeroDivisionError:
        print("The value dividing by zero ")


#divide(8, 10)
add(2, 5)
#print("The value:", result)
