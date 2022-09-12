def test():
    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")

    try:
        return (int(number_1) ** 2) / int(number_2)

    except ValueError as a:
        print(type(a))

    except ZeroDivisionError as b:
        print(type(b))


print(test())
