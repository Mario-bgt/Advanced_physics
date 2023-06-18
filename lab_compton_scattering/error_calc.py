import numpy as np
from tabulate import tabulate
from sympy import symbols, diff, sqrt, latex, ln

N_A = 6.02214076 * 10 ** 23
Z = 13
r_e = 2.8179403227 * 10 ** (-15)
v_light = 299792458
m_e = 9.1093837015 * 10 ** (-31)

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

# Print the results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({volume}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of volume:", volume.subs(variables))
Volume = volume.subs(variables)
Volume_err = total_absolute_error

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


# print results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({sigma}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of sigma:", sigma.subs(variables))

# define symbols
V, V_err, d_2, d_2_err = symbols('V V_err d_{1/2} d_2_err')

# define function
sigma_1 = (V * (np.log(2)/d_2))/(Z*N_A)

# Print it in latex
latex_func = latex(sigma_1, mul_symbol='\\cdot ')
print(f"Latex of function: {latex_func}")

# define variables and errors
variables = {V: Volume, d_2: 4.054*10**(-2)}
errors = {V: Volume_err, d_2: 1.68*10**(-2)}

# calculate partial derivatives
partial_derivatives = {var: diff(sigma_1, var) for var in variables}

# calculate absolute errors
absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

# calculate squared absolute errors and sum them
squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

# calculate total absolute error
total_absolute_error = sqrt(squared_errors_sum)

# print results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({sigma_1}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of sigma_1:", sigma_1.subs(variables))

# define symbols
E, E_err, m, m_err, r, r_err, pi, pi_err = symbols('E_{\gamma} E_err m_e m_err r_e r_err \pi pi_err')

# define function
sigma_2 = ((pi*r**2)/((E/m)**2))*(4+(2*(E/m)**2*(1+(E/m)))/((1+2*(E/m))**2)+ (((E/m)**2-2*(E/m)-2)/(E/m))*ln(1+2*(E/m)))

# Print it in latex
latex_func = latex(sigma_2, mul_symbol='\\cdot ')
print(f"Latex of function: {latex_func}")

# define variables and errors
variables = {E: 662, m: 510.99895000, r: 2.8179403227 * 10 ** (-15), pi: np.pi}
errors = {E: 23.3, m: 15*10**(-8), r: 19*10**(-25), pi: 0}

# calculate partial derivatives
partial_derivatives = {var: diff(sigma_2, var) for var in variables}

# calculate absolute errors
absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

# calculate squared absolute errors and sum them
squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

# calculate total absolute error
total_absolute_error = sqrt(squared_errors_sum)

# print results
print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({sigma_2}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nTotal absolute error:", total_absolute_error)
print("Value of sigma_2:", sigma_2.subs(variables))