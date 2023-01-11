class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self,start, limit):
        self.start = start
        self.limit = limit
        self.counter = 0


    def __next__(self):
        if self.start < self.limit:
            self.start += 1
            self.counter += 1
            return {self.counter: self.start}
        else:
            raise StopIteration
s = SimpleIterator(1, 5)
for i in s:
    print(i)