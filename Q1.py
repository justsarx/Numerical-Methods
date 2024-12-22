import math

t_val = 1 / 3

r_val = round(t_val, 2)

abs_err = abs(t_val - r_val)

rel_err = abs_err / abs(t_val)

per_err = rel_err * 100

print("True value: ", t_val)
print("Rounded value: ", r_val)
print("Absolute error: ", abs_err)
print("Relative error: ", rel_err)
print("Percentage error: ", round(per_err, 3), "%")
