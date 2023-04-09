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


# Function to simulate a measurement given an angle of scattering and a true outgoing energy
def simulate_measurement(theta, E_true):
    E_reco = E_true + np.random.normal(loc=0, scale=sigma_E)
    return E_reco


# Simulate 1000 measurements for angles ranging from 10 to 80 degrees
angles = np.arange(10, 90, 1)
measurements = []
for i in range(1000):
    E_true_values = [E_true(theta) for theta in angles]
    measurements.append([simulate_measurement(theta, E_true) for theta, E_true in zip(angles, E_true_values)])

# Convert measurements to numpy array
measurements = np.array(measurements)


# Fit the measurements to obtain the measured electron mass
def fit_func(theta, m):
    return E_true(theta) * (1 + m*(1-np.cos(np.radians(theta)))/E_in)


mean_values = np.mean(measurements, axis=0)
popt, pcov = curve_fit(fit_func, angles, mean_values/E_in)

m_reco = popt[0]
m_reco_err = np.sqrt(np.diag(pcov))[0]
print("Measured electron mass: {:.3f} +/- {:.3f} MeV/c^2".format(m_reco, m_reco_err))

# Histogram of m_reco values
plt.hist(measurements[:,0]/E_in, bins=20)
plt.axvline(x=m_reco, color='red', label="Measured mass")
plt.xlabel("Measured electron mass (MeV/c^2)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Pull distribution
pull = (measurements[:, 0]/E_in - m_reco) / m_reco_err
plt.hist(pull, bins=20)
plt.axvline(x=np.mean(pull), color='red', label="Mean = {:.3f}".format(np.mean(pull)))
plt.axvline(x=np.std(pull), color='green', label="Standard deviation = {:.3f}".format(np.std(pull)))
plt.xlabel("Pull")
plt.ylabel("Frequency")
plt.legend()
plt.show()
