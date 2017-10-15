
def fib(max):
    a, b = 0, 1
    while a< max:
        yield a
        a, b = b, a + b
gen = fib(10)
for i in fib(10):
    print (i)


squares= (i**2 for i in range(10))
for s in squares:
    print(s)