def fib(n):
    a = 0
    b = 1
    while(n > 0):
        print(a)
        c = a + b
        a = b
        b = c
        n-=1

fib(10)

