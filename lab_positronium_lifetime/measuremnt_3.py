import matplotlib.pyplot as plt
from scipy.signal import convolve
from functions import *
import math

data = read_spe_file('data/me3_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_data = channel_to_time(x_vals)
y_data = y_vals[0:14000]
x_data = x_data[0:14000]


# Define the model function as a sum of Gaussian and two exponential decay components
def model_function(datas, a1, a2, a3, mu, sigma, decay1, decay2):
    res = []
    for x in datas:
        # Gaussian component
        gaussi = a1 * np.exp(-(x - mu)**2 / (2 * sigma**2))

        first1 = a2 * np.exp((-1 / decay1)*(x-mu-(sigma**2)/decay1))
        second1 = 1 + math.erf((x-mu-sigma**2/decay1)/(np.sqrt(2)*sigma))

        first2 = a3 * np.exp((-1 / decay1) * (x - mu - (sigma ** 2) / decay2))
        second2 = 1 + math.erf((x - mu - sigma ** 2 / decay2) / (np.sqrt(2) * sigma))

        result = gaussi+first1*second1+first2*second2
        res.append(result)
    return res


# Initial guesses for the parameters
initial_guess = [150, 150, 150, 2.7*10**(-8), 1e-10, 1.25*10**(-10), 1.42*10**(-7)]
# initial_guess = [180, 180, 180, 2.7*10**(-8), 1e-11, 1.25*10**(-10), 1.42*10**(-7)]
# plot the inital guess
plt.plot(x_data[8500:11000], y_data[8500:11000], label='Data with Noise')
plt.plot(x_data[8500:11000], model_function(x_data, *initial_guess)[8500:11000], 'r-', label='Initial Guess')
plt.legend()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Initial Guess')
plt.grid()
plt.show()


# Fit the data to the model using curve_fit
params, covariance = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a1_fit, a2_fit, a3_fit, mu_fit, sigma_fit, decay1_fit, decay2_fit = params

# Print the fitted parameters
print("Fitted Parameters:")
print(f"A1: {a1_fit}")
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
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Counts')
plt.title('Fitting Data with Gaussian Detector and Two Exponential Decays')
plt.grid()
plt.show()
