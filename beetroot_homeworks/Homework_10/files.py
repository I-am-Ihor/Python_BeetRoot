with open('myfile.txt', 'w') as file:
    file.write('Hello file world!\nHi')

with open('myfile.txt', 'r') as file:
    print(file.read())

    
