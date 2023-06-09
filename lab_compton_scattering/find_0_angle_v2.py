import matplotlib.pyplot as plt

from functions import *


def evaluator(angle, expected_mean, expected_range):
    # Load and process SPE file
    spe_file_path = 'data/nullwinkel' + str(int(angle)) + '.Spe'
    counts = read_spe_file(spe_file_path)
    x = marker_to_keV(np.arange(len(counts)))

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
    return mean, std


files = np.linspace(-6, 4, 11)
means = []
stds = []

for file in files:
    mean, std = evaluator(file, 662, 150)
    means.append(mean)
    stds.append(std)


# fit the means
params = fit_gaussian(files, means)

# Generate points for the fitted curve
x_fit = np.linspace(files[0], files[-1], 1000)
y_fit = gaussian(x_fit, *params)

# Plot the data and the fitted curve
plt.plot(files, means, 'b.', label='data')
plt.plot(x_fit, y_fit, 'r-', label='fit')
plt.title('Counts vs Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('Mean Counts')
plt.legend()
plt.grid()
plt.savefig('plots/mean_vs_angle.pdf')
plt.show()

# print the fitted parameters
print('Mean: ', params[1])
print('Standard deviation: ', params[2])

