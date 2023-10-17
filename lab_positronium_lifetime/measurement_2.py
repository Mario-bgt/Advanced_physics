from functions import *

# Now do the same for measurement 2
data1 = read_spe_file('data/me2_deltatime.Spe')
data2 = read_spe_file('data/me2_deltatime_2.Spe')
data = [x+y for x, y in zip(data1, data2)]

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_vals = channel_to_time(x_vals)

params, cov = fit_gaussian(x_vals, y_vals)
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
plt.xlabel('time (s)')
plt.ylabel('Counts')
plt.title('Gaussian fit of measurement 2')
plt.legend()
plt.savefig('plots/gaussian_fit_m2.pdf')
plt.show()

residuals = y_vals - gaussian(x_vals, *params)
sigmas = np.sqrt(y_vals)

y_error = residuals/sigmas

plt.plot(x_vals, y_error, label='Residuals')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Residuals')
plt.title('Residuals of the Gaussian fit of measurement 2')
plt.legend()
plt.savefig('plots/gaussian_fit_residuals_m2.pdf')
plt.show()
err_a0 = cov[0][0]
err_mean = cov[1][1]
err_std = cov[2][2]
print('a0: {} +- {}'.format(params[0], np.sqrt(err_a0)))
print('Mean: {} +- {}'.format(params[1], np.sqrt(err_mean)))
print('Std: {} +- {}'.format(params[2], np.sqrt(err_std)))

time_1 = 2.694793279259723e-08
err_time_1 =  1.1162952147595903e-12

# calculate the total time
total_time = 2*params[1] + params[2] - time_1
err_total_time = np.sqrt(err_mean**2 + err_std**2+ err_time_1**2)
print('Total time: {} +- {}'.format(total_time, err_total_time))
