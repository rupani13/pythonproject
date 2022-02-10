# Module program


person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}


# Factorial program


def fun(obj):
    if obj == 1:
        return obj
    else:
        return obj * fun(obj - 1)
