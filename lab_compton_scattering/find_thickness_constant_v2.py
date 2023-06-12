import matplotlib.pyplot as plt
import numpy as np

from functions import *
import os


def mean_counts_finder(file, expected_mean, expected_range):
    # Load and process SPE file
    spe_file_path = 'data/' + file
    counts = read_spe_file(spe_file_path)
    x = marker_to_keV(np.arange(len(counts)))

    mean = np.sum(counts)
    d = float(file[1:2])
    std = np.sqrt(mean)
    return mean, d, std


# get the file names that start with d from the data folder
files = ['d0_rt120.32.Spe', 'd1_rt120.26.Spe', 'd2_rt120.22.Spe', 'd3_rt120.18.Spe', 'd4_rt120.16.Spe','d5_rt120.17.Spe']


# get the mean count and std for each file
dicken = []
means = []
stds = []

for file in files:
    mean, d, std = mean_counts_finder(file, 662, 150)
    means.append(mean)
    dicken.append(d)
    stds.append(std)


# fit the means
params = fit_exponential(dicken, means)

# Generate points for the fitted curve
x_fit = np.linspace(float(dicken[0]), float(dicken[-1]), 1000)
y_fit = exponential(x_fit, *params)

# Plot the data and the fitted curve
plt.errorbar(dicken, means, yerr=stds, fmt='b.', label='data')
# plt.plot(dicken, means, 'b.', label='data')
plt.plot(x_fit, y_fit, 'r-', label='fit')
plt.title('Mean vs Thickness')
plt.xlabel('Thickness [cm]')
plt.ylabel('Mean Counts')
plt.legend()
plt.grid()
plt.savefig('plots/mean_vs_thickness.pdf')
plt.show()


# print the fitted parameters
print('a = ' + str(params[0]))
print('b = ' + str(params[1]))

# print the means
print('means = ' + str(means))
print('stds = ' + str(stds))
print('dicken = ' + str(dicken))
