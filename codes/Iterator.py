
class Fib:
    def __init__(self, maxi):
        self.max = maxi

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in Fib(21):
    print(i)


class CustomRange:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        number = self.current
        if self.current > self.max - 1:
            raise StopIteration
        self.current += 1
        return number

for i in CustomRange(10):
    print(i)