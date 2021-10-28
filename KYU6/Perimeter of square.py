def fibonacci(n):
    # a = [0, 1]
    # for i in range(n):
    #     a.append(a[i]+a[i+1])
    # b = (i for i in range(n) if i % 2 == 0)
    s = [0, 1]
    s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(n)]

    return s


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def perimeter(n):
    return(sum(fib(n+2))*4)


perimeter(5)
