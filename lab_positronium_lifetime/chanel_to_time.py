import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import read_spe_file, gaussian, fit_gaussian


def linear(x, m, b):
    """
    :param x: x array
    :param m: slope
    :param b: y-intercept
    :return: m*x + b
    """
    return m * x + b


def fit_linear(x, y):
    """
    :param x: x array
    :param y: y array
    :return: fit parameters
    """
    params, _ = curve_fit(linear, x, y, sigma=sigmas)
    return params, _

data = read_spe_file('data/timeconverter_0_4_8_12_16_20.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)

peaks = [8890, 10175, 11508, 12800, 14120, 15410]
mean = []
sigmas = []
time = [0, 4*10**-9, 8*10**-9, 12*10**-9, 16*10**-9, 20*10**-9]

plt.plot(x_vals, y_vals, label='Data')
plt.grid()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Raw data for the time calibration')
plt.legend()
# plt.xticks(peaks, time)
plt.savefig('plots/time_calibration_raw_data.pdf')
plt.show()



for i in peaks:
    x_data = x_vals[i-100:i+100]
    y_data = y_vals[i-100:i+100]
    params, cov = fit_gaussian(x_data, y_data)
    mean.append(params[1])
    sigmas.append(params[2])
    plt.plot(x_data, y_data, label='Measurement 1')
    plt.plot(x_data, gaussian(x_data, *params), label='Gaussian fit')
    # also plot the mean and std
    plt.axvline(params[1], color='r', label='Mean', linestyle='--')
    plt.axvline(params[1] + params[2], color='g', label='Mean + std', linestyle='--')
    plt.grid()
    plt.xlabel('Channel')
    plt.ylabel('Counts')
    plt.title('Gaussian fit of measurement peak at {} channel'.format(i))
    plt.legend()
    # plt.savefig('plots/time_calibration_gaussian_fit_{}.pdf'.format(i))
    # plt.show()
    plt.clf()




def linear(x, m, c):
    return m*x + c


time = [0, 4*10**-9, 8*10**-9, 12*10**-9, 16*10**-9, 20*10**-9]
mean = np.array(mean)
popt, _ = fit_linear(mean, time)
print(popt)
# plt.plot(mean, time, 'x', label='Data', color='black')
plt.errorbar(mean, time, xerr=sigmas, fmt='x', label='Mean', color='black')
plt.plot(mean, linear(mean, popt[0], popt[1]), label='Linear fit', color='red', linestyle='--')
plt.xlabel('Channel')
plt.ylabel('Time [s]')
plt.title('Linear fit of channel vs time')
plt.legend()
plt.grid()
plt.savefig('plots/time_calibration_linear_fit.pdf')
plt.show()


slope = popt[0]
y_intercept = popt[1]
slope_error = np.sqrt(_[0, 0])

print(fr"slope:{slope}   y intercep:{y_intercept} ")
print("Slope:", slope)
print("Error on the Slope:", slope_error)

