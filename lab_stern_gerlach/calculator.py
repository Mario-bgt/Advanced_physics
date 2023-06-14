import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sympy import symbols, diff, sqrt, latex


def calc_feld(x):
    """
    :param x: current in A
    :return: magnetic field in T, absolute error in T
    Function to calculate the magnetic field as well as the absolute error and the partial derivatives
    """
    # Define the symbols
    const, a_1, a_2, a_3, I = symbols('const a_1 a_2 a_3, I')

    # Define the function
    calc_feld = const + a_1 * I + a_2 * I ** 2 + a_3 * I ** 3

    # Print it in latex
    latex_func = latex(calc_feld, mul_symbol='\\cdot ')
    print(f"Latex of function: {latex_func}")

    # Define the variables and their errors
    variables = {const: 1.5450 * 10 ** (-2), a_1: 0.6113, a_2: 0.5146, a_3: -0.3907, I: x}
    errors = {const: 2.7819 * 10 ** (-3), a_1: 2.0927 * 10 ** (-2), a_2: 4.1541 * 10 ** (-2), a_3: 2.2721 * 10 ** (-2),
              I: 10 * 10 ** (-3)}

    # Calculate the partial derivatives
    partial_derivatives = {var: diff(calc_feld, var) for var in variables}

    # Calculate the absolute error for each variable
    absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

    # Calculate the squared absolute errors and sum them
    squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

    # Calculate the total absolute error
    total_absolute_error = sqrt(squared_errors_sum)

    # Calculate the relative error
    relative_error = total_absolute_error / calc_feld.subs(variables)

    # Print the results
    print("Partial derivatives:")
    for var, derivative in partial_derivatives.items():
        print(f"d({calc_feld}) / d{var} = {derivative} =  {derivative.subs(variables)}")
        latex_func = latex(derivative, mul_symbol='\\cdot ')
        print(f"Latex of partial derivative: {latex_func}")

    print("\nAbsolute errors:")
    for var, abs_error in absolute_errors.items():
        print(f"Absolute error for {var}: {abs_error}")

    print("\nTotal absolute error:", total_absolute_error)
    print("Relative error:", relative_error)

    return calc_feld.subs(variables), total_absolute_error, relative_error


def calc_grad(x, x_err):
    """
    :param x: magnetic field in T
    :param x_err: error of the magnetic field in T
    :return: gradient in T/m, absolute error in T/m
    Function to calculate the gradient as well as the absolute error and the partial derivatives of a magnetic field
    """
    # Define the symbols
    epsilon, a, B = symbols('epsilon a B')

    # Define the function
    calc_grad = (epsilon * B) / a

    # Print it in latex
    latex_func = latex(calc_grad, mul_symbol='\\cdot ')
    print(f"Latex of function: {latex_func}")

    # Define the variables and their errors
    variables = {epsilon: 0.953, a: 2.5 * 10 ** (-3), B: x}
    errors = {epsilon: 0.0026, a: 0.1 * 10 ** (-3), B: x_err}

    # Calculate the partial derivatives
    partial_derivatives = {var: diff(calc_grad, var) for var in variables}

    # Calculate the absolute error for each variable
    absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

    # Calculate the squared absolute errors and sum them
    squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

    # Calculate the total absolute error
    total_absolute_error = sqrt(squared_errors_sum)

    # Calculate the relative error
    relative_error = total_absolute_error / calc_grad.subs(variables)

    # Print the results
    print("Partial derivatives:")
    for var, derivative in partial_derivatives.items():
        print(f"d({calc_grad}) / d{var} = {derivative} = {derivative.subs(variables)}")
        latex_func = latex(derivative, mul_symbol='\\cdot ')
        print(f"Latex of partial derivative: {latex_func}")

    print("\nAbsolute errors:")
    for var, abs_error in absolute_errors.items():
        print(f"Absolute error for {var}: {abs_error}")

    print("\nTotal absolute error:", total_absolute_error)
    print("Relative error:", relative_error)

    return calc_grad.subs(variables), total_absolute_error, relative_error


strom = np.array([320, 410, 465, 515, 575, 622, 680, 755, 820, 880, 920, 980])
strom = strom * 10 ** (-3)
feld = []
feld_abs_err = []
feld_rel_err = []
for I in strom:
    f, abs_err, rel_err = calc_feld(I)
    feld.append(f)
    feld_abs_err.append(abs_err)
    feld_rel_err.append(rel_err)

feld = np.array(feld)
feld_abs_err = np.array(feld_abs_err)
feld_rel_err = np.array(feld_rel_err)

grad = []
grad_abs_err = []
grad_rel_err = []
for i in range(len(feld)):
    g, abs_err, rel_err = calc_grad(feld[i], feld_abs_err[i])
    grad.append(g)
    grad_abs_err.append(abs_err)
    grad_rel_err.append(rel_err)

q = [1.6152, 2.126, 2.5955, 2.9618, 3.3718, 3.5914, 3.9491, 4.4712, 4.8682, 5.1919, 5.2897, 5.6411]
q_abs_err = [0.1453, 0.1599, 0.169, 0.1745, 0.1765, 0.1888, 0.1777, 0.1743, 0.1758, 0.1856, 0.1767, 0.1831]
q = np.array(q) * 10 ** (-3)
q_abs_err = np.array(q_abs_err) * 10 ** (-3)


# Define the fit function
def fit_function(x, a, b):
    return a * x + b


sigmas = []
for i in range(len(grad_abs_err)):
    sigmas.append((grad_abs_err[i]**2 + q_abs_err[i]**2)**.5)

sigmas = np.array(sigmas, dtype='float64')
print(sigmas)

# Perform the fit
popt, pcov = curve_fit(fit_function, q, grad, sigma=sigmas, absolute_sigma=True)

# Extract the slope and its error
slope = popt[0]
slope_err = np.sqrt(pcov[0, 0])

# Generate fitted data points
fit_q = np.linspace(min(q)-0.0005, max(q)+0.0005, 100)
fit_grad = fit_function(fit_q, slope, popt[1])
steepest = fit_function(fit_q, slope + slope_err, popt[1])
shallowest = fit_function(fit_q, slope - slope_err, popt[1])

# Plot the data and fit
plt.figure(figsize=(10, 6))
plt.errorbar(q, grad, xerr=q_abs_err, yerr=grad_abs_err, fmt='.', label='Data', capsize=3, elinewidth=1,
             markeredgewidth=1)
plt.plot(fit_q, fit_grad, 'r-', label='Fit')
plt.plot(fit_q, steepest, 'g--', label='Steilster', alpha=0.5)
plt.plot(fit_q, shallowest, 'g--', label='Flachster', alpha=0.5)
plt.xlabel('q [m]')
plt.ylabel('Gradient [T/m]')
plt.title('Gradient in Abhängigkeit von q')
plt.legend()
plt.grid(True)
plt.savefig('gradient.pdf')
plt.show()

print("Fit results:")
print("slope =", slope, "+-", slope_err)
print("b =", popt[1], "+-", np.sqrt(pcov[1, 1]))

# Calculate the mean temperature
temperatures = np.array([179.8, 180.5, 181, 181.5, 181.6, 181.6, 181.6, 181.6, 181.7, 181.7, 181.7, 181.8])
temperature_err_sys = 0.2
temperatures = temperatures + 273.15

mean_temperature = np.mean(temperatures)
temperature_err_stat = np.std(temperatures) / np.sqrt(len(temperatures)-1)
temperature_err = np.sqrt(temperature_err_stat ** 2 + temperature_err_sys ** 2)

print("Mean temperature:", mean_temperature, "+-", temperature_err)

# Finally calculate the Bohr magneton
# Define the symbols
small_l, big_l, boltzmann, temp, slop = symbols('l, L, k_B, T, m')

# Define the function
calc_bohr = (2*boltzmann*temp)/(small_l*big_l*(1-big_l/(2*small_l))*slop)

# Print it for latex
latex_func = latex(calc_bohr, mul_symbol='\\cdot ')
print("Latex of function:", latex_func )

# Define the variables and their errors
variables = {small_l: 0.455, big_l: 7*10**(-2), boltzmann: 1.380649*10**(-23), temp: mean_temperature, slop: slope}
errors = {small_l: 10**(-3), big_l: 0.25*10**(-3), boltzmann: 0, temp: temperature_err, slop: slope_err}

# Calculate the partial derivatives
partial_derivatives = {var: diff(calc_bohr, var) for var in variables}

# Calculate the absolute error for each variable
absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

# Calculate the squared absolute errors and sum them
squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

# Calculate the total absolute error
total_absolute_error = sqrt(squared_errors_sum)

# Calculate the relative error
relative_error = total_absolute_error / calc_bohr.subs(variables)

# Print the results
print("\nBohr magneton:")
print("Value:", calc_bohr.subs(variables))

print("Partial derivatives:")
for var, derivative in partial_derivatives.items():
    print(f"d({calc_feld}) / d{var} = {derivative} =  {derivative.subs(variables)}")
    latex_func = latex(derivative, mul_symbol='\\cdot ')
    print(f"Latex of partial derivative: {latex_func}")

print("\nAbsolute errors:")
for var, abs_error in absolute_errors.items():
    print(f"Absolute error for {var}: {abs_error}")

print("\nTotal absolute error:", total_absolute_error)
print("Relative error:", relative_error)

# Print Latex table of the results for feld and grad
print("\nLatex table:")
print("Strom & Feld & Feld Abs. Error & Gradient & Gradient Abs. Error  \\\\")
for i in range(len(strom)):
    print(f"{strom[i]:.3f} & {feld[i]:.3f} & {feld_abs_err[i]:.4f} & {grad[i]:.3f} & {grad_abs_err[i]:.4f} \\\\")
