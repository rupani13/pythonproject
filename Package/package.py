
def fun(obj):
    if obj == 1:
        return obj
    else:
        return obj * fun(obj - 1)
