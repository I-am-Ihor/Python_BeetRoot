num = input('Enter your phone: ')
ch = 0
for i in range(len(num)):
    ch += 1
if ch == 10:
    print('Your prone correct')
else:
    print('Your phone discorrect')