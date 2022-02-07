# Python Exception Handling programing

def fun(a):
    global b
    if a < 4:
    #if a > 4:
        b = a / (a - 3)
        print("Value of b = ", b)


try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")
