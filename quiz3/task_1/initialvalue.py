import sympy as sp

# Input the recurrence relation coefficients and initial conditions
recurrence_relation = input("Enter the recurrence relation (e.g., 'a[n] - 2*a[n-1] + a[n-2]'): ")
a_0 = int(input("Enter the value for a_0: "))
a_1 = int(input("Enter the value for a_1: "))

# Parse the recurrence relation
n = sp.symbols('n')
a = sp.Function('a')

# Define symbols for constants C1 and C2
C1, C2 = sp.symbols('C1 C2')

# Construct the characteristic equation by evaluating the recurrence relation at a generic n
recurrence_relation = sp.sympify(recurrence_relation.replace('a[n]', 'r**2')
                                                  .replace('a[n-1]', 'r')
                                                  .replace('a[n-2]', '1'))
char_eq = sp.expand(recurrence_relation)

# Solve for the roots of the characteristic polynomial
r = sp.symbols('r')
roots = sp.solve(char_eq, r)

# Find the general solution based on the roots
if len(roots) == 1:  # Repeated root case
    solution = (C1 + C2 * n) * roots[0]**n
else:
    solution = C1 * roots[0]**n + C2 * roots[1]**n

# Use initial conditions to solve for C1 and C2
eq1 = solution.subs(n, 0) - a_0
eq2 = solution.subs(n, 1) - a_1
constants = sp.solve([eq1, eq2], (C1, C2))

# Substitute the constants back into the solution
final_solution = solution.subs(constants)

# Print the final solution as a function of n
print("The solution for a_n as a function of n is:")
sp.pprint(final_solution)
