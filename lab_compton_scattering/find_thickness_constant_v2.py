import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from functions import *
import os


def mean_counts_finder(file, expected_mean, expected_range):
    # Load and process SPE file
    real_time = float(file[-10:-4])
    spe_file_path = 'data/' + file
    counts = np.array(read_spe_file(spe_file_path))
    counts = counts / real_time
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

# calculate the error of the fit
perr = np.sqrt(np.diag(params))

# calculate the error upon b
b = params[1]
b_err = perr[1]

# Generate points for the fitted curve
x_fit = np.linspace(float(dicken[0]), float(dicken[-1]), 1000)
y_fit = exponential(x_fit, *params)

# Plot the data and the fitted curve
plt.errorbar(dicken, means, yerr=stds, xerr=0.05, fmt='b.', label='measured', capsize=3, elinewidth=1,
             markeredgewidth=1)
# plt.plot(dicken, means, 'b.', label='data')
plt.plot(x_fit, y_fit, 'r-', label='fit')
plt.title('Mean vs Thickness')
plt.xlabel('Thickness [cm]')
plt.ylabel('Mean Counts per second')
plt.legend()
plt.grid()
plt.savefig('plots/mean_vs_thickness.pdf')
plt.show()


# print the fitted parameters
print('a = ' + str(params[0]))
print('b = ' + str(params[1]))
print('error a = ' + str(perr[0]))
print('error b = ' + str(perr[1]))
# print the means
print('means = ' + str(means))
print('stds = ' + str(stds))
print('dicken = ' + str(dicken))

# make a table of the data
table = np.array([means, stds, dicken]).T
print(tabulate(table, headers=['Mean counts per second', 'Std', 'Thickness'], tablefmt="latex_raw", floatfmt=".2f"))

# calculate the half thickness
half_thickness = -1*np.log(0.5)*b

# cm to m
half_thickness = half_thickness/100
half_thickness_err = -1*np.log(0.5)*b_err/100

print('half thickness = ' + str(half_thickness))
print('half thickness error = ' + str(half_thickness_err))
