def calculate_probability(A, B, n):
    Pn = ((A / B) ** n - 1) / ((A / B) ** 100 - 1)
    return Pn

A = 51  # Initial euros for player A
B = 49  # Initial euros for player B
n = 52  # Current euros for player A to calculate p_n

pn = calculate_probability(A, B, n)
print(f"The calculated probability p_n for A = {A}, B = {B}, n = {n} is: {pn:.10f}")