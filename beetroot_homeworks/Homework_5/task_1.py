import random


new_list = []
while len(new_list) < 10:
    new_list.append(random.randint(0, 10))
print(max(new_list))
