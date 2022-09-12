import random
num = int(input('Enter integer: '))
computer = random.randint(0,10)
if num == computer:
    print('Great!')
else:
    print('Try again')
