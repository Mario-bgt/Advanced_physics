import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve
from functions import *
import math

data = read_spe_file('data/me3_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_data = channel_to_time(x_vals)
y_data = y_vals[0:14000]
x_data = x_data[0:14000]


def gauss_expo_convolution(data, mu, sigma, tau):
    res = []
    for x in data:
        expo = (1/(2*tau))*np.exp((-1 / tau) * (x - mu - (sigma ** 2) / (2 * tau)))
        ero = 1 + math.erf((x - mu - (sigma ** 2) / tau) / (np.sqrt(2) * sigma))
        res.append(expo * ero)
    return np.array(res)


# Define the model function as a sum of Gaussian and two exponential decay components
def model_function(data, mu, sigma, decay1, decay2, a2, a3):
    gauss = np.exp((-1 * (data - mu) ** 2) / (2 * sigma ** 2))
    exp1 = gauss_expo_convolution(data, mu, sigma, decay1)
    exp2 = gauss_expo_convolution(data, mu, sigma, decay2)
    res = abs(250) * gauss + a2 * exp1 + a3 * exp2
    return res


# Initial guesses for the parameters
initial_guess = [2.72e-08, 1.8e-10, 2e-09, 1e-10, 8e-8, 5e-8]
# initial_guess = [180, 180, 180, 2.7*10**(-8), 1e-11, 1.25*10**(-10), 1.42*10**(-7)]
# plot the inital guess
plt.plot(x_data[8500:11000], y_data[8500:11000], label='Data with Noise')
plt.plot(x_data[8500:11000], model_function(x_data, *initial_guess)[8500:11000], 'r--', label='Initial Guess')
plt.plot(x_data[8500:11000], 250*np.exp(-1 * ((x_data[8500:11000] - initial_guess[0])**2) / (2 * initial_guess[1]**2)), 'g--', label='Gaussian')
plt.plot(x_data[8500:11000], initial_guess[4]*gauss_expo_convolution(x_data[8500:11000], initial_guess[0], initial_guess[1], initial_guess[2]), 'y--', label='Exponential 1')
plt.plot(x_data[8500:11000], initial_guess[5]*gauss_expo_convolution(x_data[8500:11000], initial_guess[0], initial_guess[1], initial_guess[3]), 'b--', label='Exponential 2')
plt.legend()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Initial Guess')
plt.grid()
plt.show()

# Fit the data to the model using curve_fit
params, covariance = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
mu_fit, sigma_fit, decay1_fit, decay2_fit, a2_fit, a3_fit = params

# Print the fitted parameters
print("Fitted Parameters:")
print(f"A2: {a2_fit}")
print(f"A3: {a3_fit}")
print(f"mu: {mu_fit}")
print(f"sigma: {sigma_fit}")
print(f"decay1: {decay1_fit}")
print(f"decay2: {decay2_fit}")

# Plot the original data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data[8500:11000], y_data[8500:11000], label='Data')
plt.plot(x_data[8500:11000], model_function(x_data, *params)[8500:11000], 'r-', label='Fitted Curve')
# Plot individual components (Gaussian and two exponential decays)
plt.plot(x_data[8500:11000], 250*np.exp(-1*(x_data[8500:11000]-mu_fit)**2/(2*sigma_fit**2)), 'g--', label='Gaussian')
plt.plot(x_data[8500:11000], a2_fit * gauss_expo_convolution(x_data[8500:11000], mu_fit, sigma_fit, decay1_fit), 'b--',
         label='Exponential Decay 1')
plt.plot(x_data[8500:11000], a3_fit * gauss_expo_convolution(x_data[8500:11000], mu_fit, sigma_fit, decay2_fit), 'y--',
         label='Exponential Decay 2')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Counts')
plt.title('Fitting Data with Gaussian Detector and Two Exponential Decays')
plt.grid()
plt.show()
