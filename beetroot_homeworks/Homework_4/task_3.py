import random


new_list = ['h', 'e', 'l', 'l', 'o']
l = len(new_list)
for i in range(l):
    print(*random.sample(new_list, l))
    