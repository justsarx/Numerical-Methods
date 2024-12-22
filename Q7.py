import math


def f(x):
    return 1 / (1 + x**2)


def simpsons_1_3(a, b, n):

    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule.")

    h = (b - a) / n
    x = a
    sum_even = 0
    sum_odd = 0

    for i in range(1, n, 2):
        x += h
        sum_odd += f(x)

    for i in range(2, n, 2):
        x += h
        sum_even += f(x)

    integral = (h / 3) * (f(a) + 4 * sum_odd + 2 * sum_even + f(b))
    return integral


def simpsons_3_8(a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")

    h = (b - a) / n
    x = a
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    for i in range(1, n, 3):
        x += h
        sum_1 += f(x)

    for i in range(2, n, 3):
        x += h
        sum_2 += f(x)

    for i in range(3, n, 3):
        x += h
        sum_3 += f(x)

    integral = (3 * h / 8) * (f(a) + 3 * sum_1 + 3 * sum_2 + 2 * sum_3 + f(b))
    return integral


# Example usage
a = 0
b = 1

result_1_3 = simpsons_1_3(a, b, 10)
result_3_8 = simpsons_3_8(a, b, 9)

print(f"Simpson's 1/3 rule: {result_1_3}")
print(f"Simpson's 3/8 rule: {result_3_8}")
