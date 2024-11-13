a_0 = -19 / 23

def a_n(n, a_previous):

    return (4**n - 3 * a_previous) / 5

a_1 = a_n(1, a_0)

#Display the recurrence relation and result
print(f"calculated value of a_1 is: {a_1}")