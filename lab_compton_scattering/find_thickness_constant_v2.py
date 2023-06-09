from functions import *
import os


def mean_counts_finder(file, expected_mean, expected_range):
    # Load and process SPE file
    spe_file_path = 'data/' + file
    counts = read_spe_file(spe_file_path)
    x = marker_to_keV(np.arange(len(counts)))

    mean = np.sum(counts)
    d = float(file[1:2])


    return mean, d


# get the file names that start with d from the data folder
files = os.listdir('data')
files = [file for file in files if file.startswith('d')]


# get the mean count and std for each file
dicken = []
means = []

for file in files:
    mean, d = mean_counts_finder(file, 662, 150)
    means.append(mean)
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
plt.show()


# print the fitted parameters
print('a = ' + str(params[0]))
print('b = ' + str(params[1]))

