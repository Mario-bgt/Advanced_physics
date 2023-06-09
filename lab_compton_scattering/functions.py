import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# define marker to keV conversion
def marker_to_keV(marker):
    markdiv = 15999 / 4803.46
    return marker / markdiv


# define keV to marker conversion
def keV_to_marker(keV):
    markdiv = 15999 / 4803.46
    return keV * markdiv


# Define the Gaussian function
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))


# Define the exponential decay function
def exponential(x, A, tau):
    return A * np.exp(-x / tau)


# Define the function to fit the Gaussian curve to the data
def fit_gaussian(x, y):
    p0 = [np.max(y), np.mean(x), np.std(x)]  # Initial guess for parameters
    params, _ = curve_fit(gaussian, x, y, p0=p0)
    return params


# define the function to fit the exponential decay curve to the data
def fit_exponential(x, y):
    p0 = [np.max(y), 1]  # Initial guess for parameters
    params, _ = curve_fit(exponential, x, y, p0=p0)
    return params

# define a function to fit a linear curve to the data
def fit_linear(x, y):
    params = np.polyfit(x, y, 1)
    return params

# define a linear function
def linear(x, m, c):
    return m * x + c

# Read SPE file and extract counts
def read_spe_file(file_path):
    counts = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file.readlines()[12:]):
            counts.append(float(line.strip()))
            if line_num == 16383:  # Stop reading at line 16396
                break
    return counts


# Define a godness of fit function
def goodness_of_fit(x, y, func, params):
    y_fit = func(x, *params)
    return np.sum((y - y_fit)**2)
