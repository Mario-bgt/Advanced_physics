import matplotlib.pyplot as plt

from functions import *


def evaluator(filename, expected_mean, expected_range):
    # Load and process SPE file
    spe_file_path = 'data/' + filename
    counts = read_spe_file(spe_file_path)
    x = np.arange(len(counts))

    lower_lim = int(keV_to_marker(expected_mean - expected_range))
    upper_lim = int(keV_to_marker(expected_mean + expected_range))

    # restrict the data to the said points
    counts = counts[lower_lim:upper_lim]
    x = x[lower_lim:upper_lim]
    std = np.sqrt(counts)
    # Fit Gaussian curve to the data
    params = fit_gaussian(x, counts)

    # Generate points for the fitted curve
    x_fit = np.linspace(x[0], x[-1], 1000)
    y_fit = gaussian(x_fit, *params)

    # Plot the original data and fitted curve
    plt.plot(x, counts, label='Original Data')
    plt.plot(x_fit, y_fit, label='Fitted Gaussian')
    plt.title('Gaussian Fit')
    plt.xlabel('channel')
    plt.ylabel('Counts')
    plt.legend()
    plt.grid()
    plt.savefig('plots/' + str(expected_mean) + '_gaussian_fit_calibration.pdf')
    plt.show()

    # print the mean and standard deviation of the fitted curve
    print('Mean: ', params[1])
    print('Standard Deviation: ', params[2])

    # return the mean and standard deviation of the fitted curve
    return params[1], params[2], std


e_peak = evaluator('eichung_2_NA22_90s.Spe', 511, 100)
NA_peak = evaluator('eichung_2_NA22_90s.Spe', 1274, 150)
Cs_peak = evaluator('nullwinkel-1.Spe', 662, 150)

# fit the means
params = fit_linear([e_peak[0], NA_peak[0], Cs_peak[0]], [511, 1274, 662])

# Generate points for the fitted curve
x_fit = np.linspace(0, 4500, 1000)
y_fit = linear(x_fit, *params)

# Plot the data and the fitted curve
plt.plot([e_peak[0], NA_peak[0], Cs_peak[0]], [511, 1274, 662], 'bx', label='data')
plt.plot(x_fit, y_fit, 'r-', label='fit', alpha=0.5)
plt.title('Mean vs Energy')
plt.xlabel('channel')
plt.ylabel('Mean (keV)')
plt.legend()
plt.grid()
plt.savefig('plots/mean_vs_energy_calibration.pdf')
plt.show()

# The function describing the calibration curve is:
print('Calibration Curve: '+ str(params[0]) + 'x + ' + str(params[1]))

# make a table
print('Energy [keV] & Mean [channel] & Standard Deviation [channel] \\\\')
print('511 & ' + str(e_peak[0]) + ' & ' + str(e_peak[1]) + ' \\\\')
print('662 & ' + str(Cs_peak[0]) + ' & ' + str(Cs_peak[1]) + ' \\\\')
print('1274 & ' + str(NA_peak[0]) + ' & ' + str(NA_peak[1]) + ' \\\\')

