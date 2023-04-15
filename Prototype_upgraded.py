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
# plt.show()
plt.clf()

# PART 3 b)
from scipy.optimize import minimize
from scipy import stats


def E_out_model(theta, mc2):
    E_in = 0.6617  # MeV
    return E_in / (1 + (((E_in) / (mc2)) * (1 - np.cos(np.deg2rad(theta)))))


# theta_list = np.arange(10, 90, 10) we have a list above so i commented this one out
E_out_true = E_out_model(theta_lyst, mc2=0.510998)


# I have tried to optimize the NLL function for our 8 different mc2 values (before it was handled as if we had 1)
def NLL(params):
    mc2 = params[0:8]
    std = params[8]
    E_out_predicted = E_out_model(theta_lyst, mc2)
    NLL = -np.sum(stats.norm.logpdf(E_out_true, loc=E_out_predicted, scale=std))
    return NLL


# This is a test energy list used on our MLE model instead of the initial guess for mc2 = 0.4 we have now 8 different values
test_energy_lyst = np.array([np.random.normal(0.5, 0.05) for i in range(8)])
MLE_model = minimize(NLL, x0=np.concatenate((test_energy_lyst, np.array([0.01]))), method='Nelder-Mead')

# MLE_model = minimize(NLL, x0=np.array([0.4, 0.01]), method='Nelder-Mead')

print(MLE_model, '\n')

est_mc2 = MLE_model.x[0]
est_sigma = MLE_model.x[1]
print(f"Estimated parameter: mc^2 = {est_mc2:.6}, sigma = {est_sigma:.2}")
E_out_fit = E_out_model(theta_lyst, est_mc2)

plt.scatter(theta_lyst, E_out_true, label='data', color='r')
plt.plot(theta_lyst, E_out_fit, label='fit', color='b')
plt.xlabel(r"$\theta$", fontsize=15)
plt.ylabel(r"$E_{out}$", fontsize=15)
plt.legend()
plt.show()
plt.clf()


# here we define the pull with the formula pull = (mass_generated - allmass_generated_mean)/allmass_generated_std
def pull(x, x_lyst):
    mean = np.mean(x_lyst)
    sigma = np.std(x_lyst)
    pull = (x - mean) / sigma
    return pull


# PART 4
# for later use we define a function for which we can tune our sigma
def simulation(sigma=0.01):
    """
    :param sigma:
    :return: None
    """
    # PART 4 a)
    mass_lyst = []
    sigma_lyst = []
    for i in range(1000):
        energy_fluctuation = [np.random.normal(0, sigma) for i in range(8)]
        energy_simulated = np.add(energy_lyst, energy_fluctuation)

        # here we use the simulated energy (again 8 values) on our MLE model to get one guessed mc2 value which we add to our list
        MLE_model = minimize(NLL, x0=np.concatenate((energy_simulated, np.array([sigma]))), method='Nelder-Mead')

        est_mc2 = MLE_model.x[0]
        est_sigma = MLE_model.x[1]
        mass_lyst.append(est_mc2)
        sigma_lyst.append((est_sigma))
        print(i)  # speed test, currently it takes a while to calculate
        # mass_lyst.append(0.5 + np.random.normal(0,
        #                                        0.1))  # this is a placeholder, this has to be replaced with the calculations for the electron mass

    # PART 4 b)
    # histograms:
    plt.hist(mass_lyst, bins=25)
    plt.xlabel("mass of electron")
    plt.ylabel("Number of occurences")
    plt.title("Histogram of simulated masses with sigma " + str(sigma))
    plt.show()
    plt.clf()

    # STD of the distribution
    deviation = np.std(mass_lyst)

    # PART 4 c) #we make a list of the pull distribution and plot it
    pull_dist = [pull(mass, mass_lyst) for mass in mass_lyst]
    plt.hist(pull_dist, bins=25)
    plt.xlabel("Pull distribution")
    plt.ylabel("Number of occurences")
    plt.title("Histogram of the pull distribution with sigma " + str(sigma))
    plt.show()
    plt.clf()
    pull_mean = np.mean(pull_dist)
    pull_std = np.std(pull_dist)
    print(f"The mean of the pull distribution with sigma {sigma}: mean {pull_mean:.2f}, std {pull_std:.2f}")


# PART 4 d) (called a) in the sheet)
simulation(0.01)
simulation(0.5)
simulation(0.1)