# Python Closure
# Nested functions in Python
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Datetime')

# Python Closures
