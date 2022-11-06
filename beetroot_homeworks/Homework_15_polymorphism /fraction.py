class Fraction:
    def __add__(self, x, y):
        return x + y

    def __sub__(self, x, y):
        return x - y

    def __mul__(self, x, y):
        return x * y

    def __div__(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y


x = Fraction()
print(x.__add__(5, 6))
print(x.__mul__(5, 6))
print(x.__sub__(5, 6))
print(x.__div__(5, 1))
