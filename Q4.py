def difference_table(fx: list):
    for i in range(len(fx) - 1):
        if i == 0:
            dfx = [fx[i + 1] - fx[i]]
        else:
            dfx.append(fx[i + 1] - fx[i])
    return dfx


x = [0, 1, 2, 3, 4, 5]
fx = [3, 12, 81, 200, 100, 8]

diffrences = [fx]

for i in range(len(fx) - 1):
    diffrences.append(difference_table(diffrences[-1]))

for table in diffrences:
    print(table)
