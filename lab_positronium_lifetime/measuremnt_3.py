import numpy as np

from functions import *

data = read_spe_file('data/me3_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_data = x_vals[8000:12000]
y_data = y_vals[8000:12000]
# transform x_data to time
x_data = channel_to_time(x_data)

# Define the model function as a sum of Gaussian and two exponential decay components
def model_function(x, a, mu, sigma, amp1, decay1, amp2, decay2):
    # Gaussian component
    gaussi = a * np.exp(-(x - mu)**2 / (2 * sigma**2))

    # Two exponential decay components
    exp1 = amp1 * np.exp(-x / decay1)
    exp2 = amp2 * np.exp(-x / decay2)

    # Calulate the convolved model
    conv1 = np.convolve(gaussi, exp1, mode='same')
    return np.convolve(conv1, exp2, mode='same')


# Initial guesses for the parameters
initial_guess = [200, 9000, 100, np.max(y_data)/2, (125*10**-12)*3.06159197e-03, np.max(y_data)/2, 142*10**-9]

# plot the inital guess
plt.plot(x_data, model_function(x_data, *initial_guess), 'r-', label='Initial Guess')
plt.plot(x_data, y_data, label='Data with Noise')
plt.legend()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Initial Guess')
plt.show()



# Fit the data to the model using curve_fit
params, covariance = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, mu_fit, sigma_fit, amp1_fit, decay1_fit, amp2_fit, decay2_fit = params

# Plot the original data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Data with Noise')
plt.plot(x_data, model_function(x_data, *params), 'r-', label='Fitted Curve')
# plot the intial guess
# Plot individual components (Gaussian and two exponential decays)
plt.plot(x_data, a_fit * np.exp(-(x_data - mu_fit)**2 / (2 * sigma_fit**2)), 'g--', label='Gaussian')
plt.plot(x_data, amp1_fit * np.exp(-x_data / decay1_fit), '--', label='Exponential 1')
plt.plot(x_data, amp2_fit * np.exp(-x_data / decay2_fit), '--', label='Exponential 2')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fitting Data with Gaussian Detector and Two Exponential Decays')
plt.show()

# print the initial guess
print("Initial Guess:")
print(f"A: {initial_guess[0]}")
print(f"Mu: {initial_guess[1]}")
print(f"Sigma: {initial_guess[2]}")
print(f"Exponential 1 Amplitude: {initial_guess[3]}")
print(f"Exponential 1 Decay Rate: {initial_guess[4]}")
print(f"Exponential 2 Amplitude: {initial_guess[5]}")
print(f"Exponential 2 Decay Rate: {initial_guess[6]}")


# Print the fitted parameters
print("Fitted Parameters:")
print(f"A: {a_fit}")
print(f"Mu: {mu_fit}")
print(f"Sigma: {sigma_fit}")
print(f"Exponential 1 Amplitude: {amp1_fit}")
print(f"Exponential 1 Decay Rate: {decay1_fit}")
print(f"Exponential 2 Amplitude: {amp2_fit}")
print(f"Exponential 2 Decay Rate: {decay2_fit}")
