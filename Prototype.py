import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.stats import norm, uniform


# PART 3
# PART 3 a)
def E_out_true(theta, E_in=0.6617):  # we calculate the true energy output with known theta and energy
    # the standart energy was gotten from 2.0 (Setup) and is given in MeV
    """
    :param theta:
    :param E_in:
    :return: E_out:
    """
    mc2 = 0.510998  # mass of elektron in MeV taken from wikipedia
    denominator = 1 + (E_in / mc2) * (1 - np.cos(np.deg2rad(theta)))  # we have to convert theta to radians
    E_out = E_in / denominator  # we calculate the output energy
    return E_out


theta_lyst = np.arange(10, 90, 10)
# This is our energy list with true values for the energy
energy_lyst = [E_out_true(angle) for angle in theta_lyst]
# This is our simulated resolution
energy_fluctuation = [np.random.normal(0, 0.01) for i in range(8)]
# This is our list with simulated energy
energy_simulated = np.add(energy_lyst, energy_fluctuation)
print(f"Our true energy values: {energy_lyst} \n"
      f"Our resolutions: {energy_fluctuation}\n"
      f"Our simulated energy: {energy_simulated}")

# Here we scatter plot the real energy vs the simulated energy
plt.figure()
plt.scatter(theta_lyst, energy_lyst, color="g", label="True energy")
plt.scatter(theta_lyst, energy_simulated, color="r", label="Simulated energy")
plt.xlabel("theta")
plt.ylabel("energy")
plt.legend()
plt.title("True energy vs simulated energy")
plt.show()
plt.clf()

"""
here comes part 3 b)
"""


# PART 4
# for later use we define a function for which we can tune our sigma
def simulation(sigma=0.01):
    """
    :param sigma:
    :return: None
    """
    # PART 4 a)
    mass_lyst = []
    for i in range(1000):
        energy_fluctuation = [np.random.normal(0, sigma) for i in range(8)]
        energy_simulated = np.add(energy_lyst, energy_fluctuation)
        mass_lyst.append(0.5 + np.random.normal(0,
                                                0.1))  # this is a placeholder, this has to be replaced with the calculations for the electron mass

    # PART 4 b)
    # histograms:
    plt.hist(mass_lyst, bins=25)
    plt.xlabel("mass of electron")
    plt.ylabel("number of occurences")
    plt.title("histogram of simulated masses with sigma " + str(sigma))
    plt.show()

    plt.clf()

    # STD of the distribution
    deviation = np.std(mass_lyst)

    # PART 4 c)


# PART 4 d) (called a) in the sheet)
simulation(0.01)
simulation(0.5)
simulation(0.1)
