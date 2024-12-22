def lagrange_interpolation(x_data, y_data, x):
    n = len(x_data)
    y = 0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        y += term

    return y


# Example usage:
x_data = [0, 1, 4, 6]
y_data = [1, -1, 1, -1]
x = int(input("Enter the value of x: "))

interpolated_y = lagrange_interpolation(x_data, y_data, x)
print(f"Interpolated y-value at x = {x}: {interpolated_y}")
