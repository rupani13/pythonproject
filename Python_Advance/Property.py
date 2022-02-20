# Python Property Program


class fun:

    def __init__(self, value):
        self._value = value

    def getter(self):
        print('Getting value')
        return self._value

    def setter(self, value):
        print('Setting value to ' + value)
        self._value = value

    def deleter(self):
        print('Deleting value')
        del self._value
    value = property(getter, setter, deleter, )


x = fun('datetime')
print(x.value)