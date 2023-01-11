# define Python user-defined exceptions
class CustomException(Exception):
    """Base class for other exceptions"""

    pass


class ValueTooSmallError(CustomException):
    """Raised when the input value is too small"""

    pass


class ValueTooLargeError(CustomException):
    """Raised when the input value is too large"""

    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")

    except ValueTooLargeError:
        print("This value is too large, try again!")


print("Congratulations! You guessed it correctly.")
