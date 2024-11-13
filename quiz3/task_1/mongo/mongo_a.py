from sympy import symbols, Function

# Define symbolic variables
n = symbols('n', integer=True)
A_size = symbols('A_size', integer=True, positive=True)  # Symbolic size of set A
X_size = symbols('X_size', integer=True, positive=True)  # Symbolic size of set X

# Define symbolic functions for b_n and c_n
b = Function('b')(n)
c = Function('c')(n)

# Recurrence relations based on given rules
b_recurrence = A_size * (b.subs(n, n-1) + c.subs(n, n-1))
c_recurrence = X_size * b.subs(n, n-1)

# Print the recurrence relations
print(f"Recurrence relation for b(n): b(n) = {b_recurrence}")
print(f"Recurrence relation for c(n): c(n) = {c_recurrence}")
print("Recurrence relation for a(n): a(n) = b(n)")
