from functools import wraps


def decorator(func):

    def nested_func(*args):

        print(f"{func} name is '{__name__}' and haves args {args}")

    return nested_func


@decorator
def add(x, y):

    return x + y


@decorator
def square_all(*args):

    return [arg**2 for arg in args]


print("function 'add' name is: " + add.__name__)
print("function 'square_all' name is: " + square_all.__name__)
add(4, 5)
square_all(4, 5)
