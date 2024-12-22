def least_squares_fit(x_data, y_data):

    n = len(x_data)

    # Calculate sum of x, y, x^2, and xy
    sum_x = sum(x_data)
    sum_y = sum(y_data)
    sum_x_squared = sum(x**2 for x in x_data)
    sum_xy = sum(x * y for x, y in zip(x_data, y_data))

    # Calculate slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)

    # Calculate intercept (b)
    b = (sum_y - m * sum_x) / n

    return m, b


# Example usage:
x_data = [1, 2, 3, 4, 5]
y_data = [1, 4, 9, 16, 25]

slope, intercept = least_squares_fit(x_data, y_data)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
