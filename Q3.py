def f(x):
    return x**2 - 5 * x + 2


def df(x):
    return 2 * x - 5


def nr_method(x, tolerance=1e-6):
    while abs(f(x)) > tolerance:
        x = x - f(x) / df(x)
    return x


print("Approximate root:", nr_method(2))
