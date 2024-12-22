def divided_diff(x, y):
    n = len(x)
    table = [y.copy()]  # Initialize with the original y-values

    for i in range(1, n):
        new_row = []
        for j in range(n - i):
            new_row.append((table[i - 1][j + 1] - table[i - 1][j]) / (x[j + i] - x[j]))
        table.append(new_row)

    return table


# Example usage
x = [1, 2, 4, 7, 10]
y = [22, 30, 82, 106, 216]

table = divided_diff(x, y)

# Print the divided difference table
for row in table:
    print(row)
