import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Define the model function as a sum of Gaussian and two exponential decay components
def model_function(x, a, mu, sigma, amp1, decay1, amp2, decay2):
    # Gaussian component
    gaussian = a * np.exp(-(x - mu)**2 / (2 * sigma**2))

    # Two exponential decay components
    exp1 = amp1 * np.exp(-x / decay1)
    exp2 = amp2 * np.exp(-x / decay2)

    # Calulate the convolved model
    g_fft = np.fft.fft(gaussian)
    e1_fft = np.fft.fft(exp1)
    e2_fft = np.fft.fft(exp2)
    return np.fft.ifft(g_fft * e1_fft * e2_fft).real


# Generate synthetic data for testing
np.random.seed(0)
x_data = np.linspace(0, 10, 100)
y_true = (
    1.0 * np.exp(-(x_data - 3)**2 / (2 * 0.5**2)) +
    0.5 * np.exp(-x_data / 5) +
    0.8 * np.exp(-x_data / 5)
)
y_noise = 0.05 * np.random.normal(size=x_data.shape)
y_data = y_true + y_noise

# Initial guesses for the parameters
initial_guess = [1.0, 3.0, 0.5, 0.5, 2.0, 0.5, 0.2]

# Fit the data to the model using curve_fit
params, covariance = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, mu_fit, sigma_fit, amp1_fit, decay1_fit, amp2_fit, decay2_fit = params

# Plot the original data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Data with Noise')
plt.plot(x_data, model_function(x_data, *params), 'r-', label='Fitted Curve')

# Plot individual components (Gaussian and two exponential decays)
plt.plot(x_data, a_fit * np.exp(-(x_data - mu_fit)**2 / (2 * sigma_fit**2)), 'g--', label='Gaussian')
plt.plot(x_data, amp1_fit * np.exp(-x_data / decay1_fit), '--', label='Exponential 1')
plt.plot(x_data, amp2_fit * np.exp(-x_data / decay2_fit), '--', label='Exponential 2')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Fitting Data with Gaussian Detector and Two Exponential Decays')
plt.show()

# Print the fitted parameters
print("Fitted Parameters:")
print(f"A: {a_fit}")
print(f"Mu: {mu_fit}")
print(f"Sigma: {sigma_fit}")
print(f"Exponential 1 Amplitude: {amp1_fit}")
print(f"Exponential 1 Decay Rate: {decay1_fit}")
print(f"Exponential 2 Amplitude: {amp2_fit}")
print(f"Exponential 2 Decay Rate: {decay2_fit}")
