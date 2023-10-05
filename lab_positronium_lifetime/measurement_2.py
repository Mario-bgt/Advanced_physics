from functions import *

# Now do the same for measurement 2
data1 = read_spe_file('data/me2_deltatime.Spe')
data2 = read_spe_file('data/me2_deltatime_2.Spe')
data = [x+y for x, y in zip(data1, data2)]

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
