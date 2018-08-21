def square(n):
    result = 1
    for i in range(n):
        result = result * n


def triangle(n):
    x = .5
    for j in range(n):
        x = x + .5
    return (n * x)


def cube(n):
    return n*n*n
