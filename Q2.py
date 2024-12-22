def f(x):
    return x**3 - 4 * x - 9


def bisection_method(a, b, tolerance=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if f(c) == 0.0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# Find an interval where the function changes sign
ivals = [f(i) for i in range(1, 11)]
for i in range(len(ivals) - 1):
    if ivals[i] * ivals[i + 1] < 0:
        a = i + 1
        b = i + 2
        break

# Apply the bisection method
root = bisection_method(a, b)
print("Approximate root:", root)
