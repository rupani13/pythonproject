# In File User_Define_Exception

class Error(Exception):
    pass


class TransitionError(Error):
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex
        self.msg = msg


try:
    raise (TransitionError(2, 3 * 2, "Not Allowed"))

except TransitionError as error:
    print('Exception occurred: ', error.msg)
