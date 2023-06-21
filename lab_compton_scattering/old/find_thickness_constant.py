import matplotlib.pyplot as plt

from functions import *
import os


def mean_counts_finder(file, expected_mean, expected_range):
    # Load and process SPE file
    spe_file_path = 'data/' + file
    counts = read_spe_file(spe_file_path)
    x = marker_to_keV(np.arange(len(counts)))

    d = float(file[1:2])

    lower_lim = int(keV_to_marker(expected_mean - expected_range))
    upper_lim = int(keV_to_marker(expected_mean + expected_range))

    # restrict the data to the said points
    counts = counts[lower_lim:upper_lim]
    x = x[lower_lim:upper_lim]

    # Fit Gaussian curve to the data
    params = fit_gaussian(x, counts)

    # return the mean and standard deviation of the fitted curve
    interval_mid = params[1]
    interval_width = params[2]
    interval = np.where((x > interval_mid - interval_width) & (x < interval_mid + interval_width))
    lower_lim = interval[0][0]
    upper_lim = interval[0][-1]

    # find the mean of the counts in the interval
    mean = np.mean(counts[lower_lim:upper_lim])
    std = np.std(counts[lower_lim:upper_lim])

    # return the mean and std of the counts
    return mean, std, d


# get the file names that start with d from the data folder
files = ['d0_rt120.32.Spe', 'd1_rt120.26.Spe', 'd2_rt120.22.Spe', 'd3_rt120.18.Spe', 'd4_rt120.16.Spe','d5_rt120.17.Spe']

# get the mean count and std for each file
dicken = []
means = []
stds = []
for file in files:
    mean, std, d = mean_counts_finder(file, 662, 150)
    means.append(mean)
    stds.append(std)
    dicken.append(d)


# fit the means
params = fit_exponential(dicken, means)

# Generate points for the fitted curve
x_fit = np.linspace(float(dicken[0]), float(dicken[-1]), 1000)
y_fit = exponential(x_fit, *params)

# Plot the data and the fitted curve
plt.plot(dicken, means, 'b.', label='data')
plt.plot(x_fit, y_fit, 'r-', label='fit')
plt.title('Mean vs Thickness')
plt.xlabel('Thickness [cm]')
plt.ylabel('Mean Counts')
plt.legend()
plt.grid()
plt.savefig('plots/mean_vs_thickness.pdf')
plt.show()


# print the fitted parameters
print('N_0 = ' + str(params[0]) + ' counts')
print('tau = ' + str(params[1]) + ' cm')

# estimate the goodness of fit
residuals = np.array(means) - exponential(np.array(dicken), *params)
chi_squared = np.sum(residuals ** 2 / exponential(np.array(dicken), *params))
print('chi_squared = ' + str(chi_squared))
print('chi_squared / dof = ' + str(chi_squared / (len(dicken) - len(params))))

god = goodness_of_fit(np.array(dicken), np.array(means), exponential, params)
print('Goodness of fit = ' + str(god))
