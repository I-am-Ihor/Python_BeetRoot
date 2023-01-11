def  in_range(start, end, step=1):
    while start < end:
        yield start
        start += step

for num in in_range(1, 10, 4):
    print(num)