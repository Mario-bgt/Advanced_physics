import numpy as np
from tabulate import tabulate
from sympy import symbols, diff, sqrt, latex

N_A = 6.02214076 * 10 ** 23
Z = 13


# Define the symbols
a, b, c, a_err, b_err, c_err = symbols('text{width} text{height} text{Thickness} a_err b_err c_err')

# Define the function
volume = a * b * c

# Print it in latex
latex_func = latex(volume, mul_symbol='\\cdot ')
print(f"Latex of function: {latex_func}")

# Define the variables and their errors
variables = {a: 4.82*10**(-2), b: 10.81*10**(-2), c: 0.3*10**(-2)}
errors = {a: 0.001, b: 0.001, c: 0.001}

# Calculate the partial derivatives
partial_derivatives = {var: diff(volume, var) for var in variables}

# Calculate the absolute error for each variable
absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

# Calculate the squared absolute errors and sum them
squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

# Calculate the total absolute error
total_absolute_error = sqrt(squared_errors_sum)

# Calculate the relative error
relative_error = total_absolute_error / volume.subs(variables)

# Print the results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({volume}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of volume:", volume.subs(variables))

# define symbols
R, R_err, r, r_err = symbols('R R_err r r_err')

# define function
sigma = (np.pi * R**2)/(r**2)

# Print it in latex
latex_func = latex(sigma, mul_symbol='\\cdot ')
print(f"Latex of function: {latex_func}")

# define variables and errors
variables = {R: 1.205*10**(-2), r: 0.345}
errors = {R: 10**(-4), r: 0.02}

# calculate partial derivatives
partial_derivatives = {var: diff(sigma, var) for var in variables}

# calculate absolute errors
absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

# calculate squared absolute errors and sum them
squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

# calculate total absolute error
total_absolute_error = sqrt(squared_errors_sum)

# calculate relative error
relative_error = total_absolute_error / sigma.subs(variables)

# print results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({sigma}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of sigma:", sigma.subs(variables))





