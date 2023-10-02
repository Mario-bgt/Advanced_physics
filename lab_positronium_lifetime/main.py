import matplotlib.pyplot as plt

from functions import *

data = read_spe_file('data/me1_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)

params = fit_gaussian(x_vals, y_vals)
print(params)
# limit data to the range of the fit
upper = 9500
lower = 8000
x_vals = x_vals[lower:upper]
y_vals = y_vals[lower:upper]


plt.plot(x_vals, data[lower:upper], label='Measurement 1')
plt.plot(x_vals, gaussian(x_vals, *params), label='Gaussian fit')
# also plot the mean and std
plt.axvline(params[1], color='r', label='Mean')
plt.axvline(params[1] + params[2], color='g', label='Mean + std')
plt.grid()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Gaussian fit of measurement 1')
plt.legend()
plt.savefig('plots/gaussian_fit_m1.pdf')
plt.show()

# Now do the same for measurement 2
data = read_spe_file('data/me2_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)

params = fit_gaussian(x_vals, y_vals)
print(params)
# limit data to the range of the fit
upper = 10000
lower = 8400
x_vals = x_vals[lower:upper]
y_vals = y_vals[lower:upper]


plt.plot(x_vals, data[lower:upper], label='Measurement 2')
plt.plot(x_vals, gaussian(x_vals, *params), label='Gaussian fit')
# also plot the mean and std
plt.axvline(params[1], color='r', label='Mean')
plt.axvline(params[1] + params[2], color='g', label='Mean + std')
plt.grid()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Gaussian fit of measurement 2')
plt.legend()
plt.savefig('plots/gaussian_fit_m2.pdf')
plt.show()
