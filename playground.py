import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants
m_e = 0.5109989461  # MeV/c^2, mass of electron
E_in = 100  # MeV, incoming photon energy
sigma_E = 0.01  # MeV, energy resolution of detector

# Function to calculate true outgoing energy of photon given angle of scattering
def E_true(theta):
    return E_in/(1 + (E_in/m_e)*(1-np.cos(np.radians(theta))))

# Simulate measurements with energy resolution
theta = np.arange(10, 90, 10)
E_true_vals = E_true(theta)
E_meas_vals = np.random.normal(loc=E_true_vals, scale=sigma_E)

# Define likelihood function to fit
def likelihood(theta, m_e):
    E_meas = np.random.normal(loc=E_true(theta), scale=sigma_E)
    return np.sum((E_meas - E_meas_vals)**2)

# Perform maximum likelihood fit
initial_guess = 0.5*m_e
result = curve_fit(likelihood, theta, E_meas_vals, p0=initial_guess)
m_reco_e, m_reco_e_err = result[0][0], np.sqrt(result[1][0][0])

# Plot results
plt.errorbar(theta, E_meas_vals, yerr=sigma_E, fmt='o', label='Measured')
plt.plot(theta, E_true_vals, label='True')
plt.plot(theta, E_true(theta), label='Fitted')
plt.legend()
plt.xlabel('Scattering angle (degrees)')
plt.ylabel('Photon energy (MeV)')
plt.title('Compton scattering simulation and fit')
plt.show()

# Print results
print(f"Measured electron mass: {m_reco_e:.6f} +/- {m_reco_e_err:.6f} MeV/c^2")
