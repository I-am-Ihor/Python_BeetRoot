#List comprehension exercise

#Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.


new_list = []
new_list_square = []
zipped = []
for i in range(1, 10 + 1):
    new_list.append(i)  
    new_list_square.append(i ** 2)

zipped.append(list(zip(new_list, new_list_square)))

print(zipped)
