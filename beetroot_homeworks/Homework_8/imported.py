""" Make a directory with 2 modules; make a function in one of them;
 then import this function in the other module and use that in your script of choice.

"""

from math import factorial


def my_room_area(num1, num2):
    total = num1 * num2

    return total


def main():
    print(my_room_area(int(input('Enter room length: ')), int(input("Enter room width: "))))


if __name__ == '__main__':
    main()


def factorial_number(integer):
    
    return factorial(integer)