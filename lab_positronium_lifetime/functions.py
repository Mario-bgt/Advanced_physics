import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def gaussian(x, A, mu, sigma):
    """
    :param x: x array
    :param A: max value
    :param mu: mean
    :param sigma: std
    :return: A*exp(-(x-mu)**2/(2*sigma**2))*1/(sigma*sqrt(2*pi))
    """
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2)) * 1 / (sigma * np.sqrt(2 * np.pi))


# Define the exponential decay function
def exponential(x, A, tau):
    """
    :param x: x array
    :param A: max value
    :param tau: decay constant
    :return: A*exp(-x/tau)
    """
    return A * np.exp(-x / tau)


# Define the function to fit the Gaussian curve to the data
def fit_gaussian(x, y):
    """
    :param x: x array
    :param y: y array
    :return: fit parameters
    """
    p0 = [np.max(y), np.mean(x), np.std(x)]  # Initial guess for parameters
    params, _ = curve_fit(gaussian, x, y, p0=p0)
    return params

def read_spe_file(file_path):
    """
    :param file_path: path to the SPE file
    :return: array of counts
    """
    counts = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file.readlines()[12:]):
            counts.append(float(line.strip()))
            if line_num == 16383:  # Stop reading at line 16396
                break
    return counts

def fit_exponential(x, y):
    """
    :param x: x array
    :param y: y array
    :return: fit parameters
    """
    p0 = [np.max(y), 1]  # Initial guess for parameters
    params, _ = curve_fit(exponential, x, y, p0=p0)
    return params