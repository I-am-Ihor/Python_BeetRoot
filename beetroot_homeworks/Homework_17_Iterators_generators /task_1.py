a = [1, 2, 3, 4, 5, 6, 7]


def with_index(itarable, start=0):
    pr = start + len(itarable)
    index = 1
    while start < pr:
        yield (start, index)
        start += 1
        index += 1


for i in with_index(a):
    print(i)
