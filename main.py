import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, curve_fit
from scipy.stats import norm, gaussian_kde
#hello
# set a seed
np.random.seed(42)

# make a list of angles from 10 to 90 degrees with a step of 10 degrees
# theta_list = np.arange(0, 370, 10) # try that one out and look at the plots and results!
theta_list = np.arange(10, 90, 10)

# define a function that calculates the energy output with fluctuations
def E_out_fluctuated(mc2, theta):
    """
    :param theta: angle in degrees
    :param mc2: mass of the electron in MeV
    :return: energy in MeV
    """
    E_in = 0.6617
    denominator = 1 + (E_in / mc2) * (1 - np.cos(np.deg2rad(theta)))
    E_out = E_in / denominator
    return E_out


# calculate the true energy for each angle in the list
mc2_wiki = 0.510998
energy_calculated = [E_out_fluctuated(mc2_wiki, angle) for angle in theta_list]

# create a list with fluctuations in energy
energy_fluctuation = np.random.normal(0, 0.01, size=len(theta_list))

# add the fluctuations to the true energy
energy_simulated = np.add(energy_calculated, energy_fluctuation)

# plot the true energy, the fluctuations and the simulated energy
plt.figure()
plt.scatter(theta_list, energy_calculated, color="g", label="True energy", alpha=0.5)
plt.scatter(theta_list, energy_simulated, color="r", label="Simulated energy", alpha=0.5)
plt.xlabel(r"$\theta$", fontsize=15)
plt.ylabel(r"$E_{out}$", fontsize=15)
plt.legend()
plt.grid()
plt.title("True energy vs simulated energy", fontsize=14, fontstyle='italic')
# plt.show()
plt.savefig("True_energy_vs_simulated_energy.png")
plt.clf()


# define the negative log-likelihood function
def neg_log_likelihood(params, energy_simulated, scale):
    mc2 = params
    energy_calculated = E_out_fluctuated(mc2, theta_list)
    log_likelihood = np.sum(norm.logpdf(energy_simulated, loc=energy_calculated, scale=scale))
    return -log_likelihood


# set the scale for testing to 0.01
scale = 0.01

# perform the maximum likelihood fit
result = minimize(neg_log_likelihood, x0=np.array([0.5]), args=(energy_simulated, scale))

# retrieve the value of mc2
mc2 = result.x[0]

print(result)

# print the value of mc2
print("The value of mc2 is:", mc2)

# plot the negative log-likelihood function
plt.figure()
plt.scatter(theta_list, energy_calculated, label='data', color='r')
plt.plot(theta_list, E_out_fluctuated(mc2, theta_list), label='fit', color='b')
plt.xlabel(r"$\theta$", fontsize=15)
plt.ylabel(r"$E_{out}$", fontsize=15)
plt.legend()
plt.grid()
plt.title("Negative log likelihood fit", fontsize=14, fontstyle='italic')
# plt.show()
plt.savefig("E_out_fit.png")
plt.clf()


def pull(rec_quant, gen_quant):
    """
    :param rec_quant: reconstructed quantity
    :param gen_quant: generated quantity
    :return: pull
    """
    nominator = [val - gen_quant for val in rec_quant]
    return nominator / np.std(rec_quant)


# define a function to simulate the maximum likelihood 1000 times for different values of sigma
def simulate_likelihood(sigma):
    # set the number of iterations
    n_iter = 1000

    # initialize an empty list to collect the results
    mc2_list = []
    scale = sigma
    # repeat the simulation n_iter times
    for i in range(n_iter):
        # create a list with fluctuations in energy
        energy_fluctuation = np.random.normal(0, sigma, size=len(theta_list))
        # calculate the true energy for each angle in the list
        energy_calculated = [E_out_fluctuated(mc2_wiki, angle) for angle in theta_list]
        # add the fluctuations to the true energy
        energy_simulated = np.add(energy_calculated, energy_fluctuation)
        # perform the maximum likelihood fit
        result = minimize(neg_log_likelihood, np.array([0.5]), args=(energy_simulated, scale))
        # retrieve the value of mc2
        mc2 = result.x[0]
        # add the result to the list
        mc2_list.append(mc2)
    # delete the outliers
    # mc2_list = [val for val in mc2_list if -1 < val < 1]
    # print the mean and the standard deviation of the mc2 values
    print("The sigma is:", sigma)
    print("The mean of the mc2 values is:", np.mean(mc2_list))
    print("The standard deviation of the mc2 values is:", np.std(mc2_list))
    # plot the results as a histograms
    plt.figure(figsize=(8, 6))  # adjust the figure size if needed
    plt.hist(mc2_list, bins=30, color='navy', alpha=0.8, density=True)  # set color and transparency
    plt.axvline(np.mean(mc2_list), color='red', linestyle='--')  # add a line for the mean value
    plt.xlabel("mc2", fontsize=12)  # adjust font size and style
    plt.ylabel("frequency", fontsize=12)
    plt.title("Histogram of mc2 values with sigma = " + str(sigma), fontsize=14, fontstyle='italic')
    plt.grid(axis='y')  # only show gridlines on the y-axis
    plt.savefig("Histogram_of_mc2_values_sigma_" + str(sigma) + ".png", dpi=300)  # increase dpi for higher quality
    plt.clf()

    # calculate the pull
    pull_list = pull(mc2_list, 0.510998)
    # delete the outliers
    # pull_list = [val for val in pull_list if val < 4]
    # print the mean and the standard deviation of the pull
    print("The mean of the pull is:", np.mean(pull_list))
    print("The standard deviation of the pull is:", np.std(pull_list))
    # plot the pull as a histogram
    plt.figure()
    plt.hist(pull_list, bins=30, color='navy', alpha=0.8) # set color and transparency
    plt.axvline(np.mean(pull_list), color='red', linestyle='--')  # add a line for the mean value
    plt.xlabel("pull", fontsize=12)  # adjust font size and style
    plt.ylabel("frequency", fontsize=12)
    plt.grid(axis='y')
    plt.title("Histogram of pull values with sigma = " + str(sigma), fontsize=14, fontstyle='italic')
    # plt.show()
    plt.savefig("Histogram_of_pull_values_sigma"+str(sigma)+".png", dpi=300)
    plt.clf()


simulate_likelihood(0.01)
simulate_likelihood(0.05)
simulate_likelihood(0.1)
