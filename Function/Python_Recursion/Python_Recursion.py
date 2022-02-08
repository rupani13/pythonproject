# Python Recursion Program


def Recursion(k):
    if (k > 0):
        result1 = k - Recursion(k-1)
        print(result1)
    else:
        result1 = 0
    return result1


print("\n\nRecursion Example Results")
Recursion(5)