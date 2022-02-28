# In File Blit_in_Exceptio

try:
    # a = 10/2
    a = 10 / 0
    print(a)
except ArithmeticError:
    print("An arithmetic exception:")
else:
    print("Success:")

# lockup Error
try:
    a = [11, 12, 13]
    print(a[3])
except LookupError:
    print("An LookupError:")
else:
    print("Success:")
