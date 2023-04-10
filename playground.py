""" I imported some sample code from chatgpt that might be useful"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

h = 6.62607015e-34  # Planck's constant (J s)
c = 299792458  # speed of light (m/s)
me = 9.10938356e-31  # mass of electron (kg)
E_in = 0.6617  # energy of incoming photon (MeV)
sigma_E = 0.01  # energy resolution of detector (MeV)
psi = np.arange(10, 90, 10) * np.pi / 180  # scattering angles (radians)


# We define the Compton scattering formula as a function:
def compton_scattering(E_in, me, c, h, psi):
    return E_in / (1 + E_in / (me * c ** 2) * (1 - np.cos(psi)))


# We use this function to calculate the expected outgoing energy of the photon for each scattering angle:
E_true_out = compton_scattering(E_in, me, c, h, psi)

# We then add a random energy resolution to each data point, using a normal distribution with mean 0 and standard
# deviation sigma_E:
E_reco_out = E_true_out + np.random.normal(0, sigma_E, size=len(psi))

# We can plot the data points to visualize the simulated experiment:
plt.errorbar(psi * 180 / np.pi, E_reco_out, yerr=sigma_E, fmt='o', label='simulated data')
plt.xlabel('Scattering angle (degrees)')
plt.ylabel('Energy of outgoing photon (MeV)')
plt.legend()
plt.show()


# Now we can perform a maximum likelihood fit to determine the measured electron mass and its uncertainty. We define
# a function to fit the data points using the curve_fit function from the scipy.optimize library:
def fit_function(psi, m_reco_e):
    return compton_scattering(E_in, m_reco_e, c, h, psi)


popt, pcov = curve_fit(fit_function, psi, E_reco_out, sigma=sigma_E)
m_reco_e = popt[0]
sigma_m_reco_e = np.sqrt(pcov[0, 0])

# Finally, we plot the result of the fit together with the simulated data points:
plt.errorbar(psi * 180 / np.pi, E_reco_out, yerr=sigma_E, fmt='o', label='simulated data')
plt.plot(psi * 180 / np.pi, fit_function(psi, m_reco_e),
         label='fit: m_reco_e = {:.3e} +/- {:.3e} kg'.format(m_reco_e, sigma_m_reco_e))
plt.xlabel('Scattering angle (degrees)')
plt.ylabel('Energy of outgoing photon (MeV)')
plt.legend()
plt.show()

# This should give you a plot with the simulated data points and the result of the fit. You can adjust the values of
# sigma_E and E_in to explore different scenarios.
