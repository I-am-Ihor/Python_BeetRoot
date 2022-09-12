text = input('Enter text: ')
if len(text) > 1:
    print(text[0], text[1], text[-1], text[-2], sep='')
else:
    print('Emply result')