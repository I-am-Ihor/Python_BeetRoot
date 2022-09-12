"""
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be '+', '-' or '*') and an
arbitrary number of arguments (only numbers) as the second parameter. Then return
the sum or product of all the numbers in the arbitrary parameter.

"""


def make_operation(arithmetic_operator, *args):    # the function takes an algometric value and any number of parameters (numbers only)
    if arithmetic_operator == '+':

        return sum(num for num in args)

    if arithmetic_operator == '*':
        calculation = 1
        for num in args:
            calculation *= num

        return calculation
        
    if arithmetic_operator == '-':
        calculation = args[0] * 2
        for num in args:
            calculation -= num

        return calculation


print(make_operation())
