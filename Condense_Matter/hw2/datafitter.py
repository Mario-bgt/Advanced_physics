import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

hbar = 1.0545718e-34  # Reduced Planck constant in Js
eV_to_J = 1.602176634e-19  # Conversion from eV to Joules
angstrom_to_meter = 1e-10  # Conversion from Å to meters
m_e = 9.10938356e-31  # Electron rest mass in kilograms

# Load the data from the txt file
data = np.loadtxt('arpes.txt', delimiter=',')

k_parallel = data[:, 0]  # First column: k_parallel
E_minus_Ef = data[:, 1]  # Second column: E - E_f

def parabolic_dispersion(k, a, b):
    return a * k**2 + b

params, covariance = curve_fit(parabolic_dispersion, k_parallel, E_minus_Ef)

a = params[0]
b = params[1]


# Convert the fitting parameter 'a' from eV·Å² to J·m²
a_SI = a * eV_to_J / (angstrom_to_meter**2)

# Calculate the effective mass in kilograms
m_star = hbar**2 / (2 * a_SI)
m_star_2 = hbar**2 / (2*a)

# Print the result
print(f"Fitting parameter (a): {a}")
print(f"Fitting parameter (b): {b}")
print(f"Effective mass (m*): {m_star} m_e")
print(f"Effective mass 2 (m*): {m_star_2} m_e")

# Plot the original data and the fit
k_fit = np.linspace(min(k_parallel), max(k_parallel), 100)  # Generate k values for the fitted curve
E_fit = parabolic_dispersion(k_fit, a, b)  # Calculate E values for the fitted curve

# enable latex rendering
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


plt.scatter(k_parallel, E_minus_Ef, label='Data', color='blue')  # Scatter plot of the data
plt.plot(k_fit, E_fit, label=f'Fit: a = {a:.4e}', color='red')  # Plot the fitted curve
plt.xlabel('k_{parallel} (1/Å)')
plt.ylabel('E - E_f (eV)')
plt.legend()
plt.title('Parabolic Fitting of ARPES Data')
plt.show()
