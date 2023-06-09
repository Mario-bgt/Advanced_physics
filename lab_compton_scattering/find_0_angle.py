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

    # Generate points for the fitted curve
    x_fit = np.linspace(x[0], x[-1], 1000)
    y_fit = gaussian(x_fit, *params)

    # Plot the data and the fitted curve
    plt.plot(x, counts, 'b.', label='data')
    plt.plot(x_fit, y_fit, 'r-', label='fit')
    plt.title('Angle: ' + str(angle) + ' degrees')
    plt.xlabel('Energy (keV)')
    plt.ylabel('Counts')
    plt.legend()
    plt.grid()
    plt.show()

    # return the mean and standard deviation of the fitted curve
    return params[1], params[2]


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
plt.title('Mean vs Angle')
plt.xlabel('Angle (degrees)')
plt.ylabel('Mean (keV)')
plt.legend()
plt.grid()
plt.show()

# print the fitted parameters
print('Mean: ', params[1])
print('Standard deviation: ', params[2])



