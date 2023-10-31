import numpy as np

from functions import *

data = read_spe_file('data/me1_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_vals = channel_to_time(x_vals)


params, cov = fit_gaussian(x_vals, y_vals)
print(params)
# limit data to the range of the fit
upper = 9500
lower = 8000
x_vals = x_vals[lower:upper]
y_vals = y_vals[lower:upper]

# Outcomment the next 4 lines if you want it to compile fast, this does Latex label style
A=6
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.plot(x_vals, data[lower:upper], label='Measurement 1')
plt.plot(x_vals, gaussian(x_vals, *params), label='Gaussian fit')
# also plot the mean and std
plt.axvline(params[1], color='r', label='Mean', linestyle='--')
plt.axvline(params[1] + params[2], color='g', label='Mean + std', linestyle='--')
plt.grid()
plt.xlabel('Time (s) ')
plt.ylabel('Counts')
plt.title(r'\textbf{Gaussian fit of measurement 1}')
plt.legend()
plt.savefig('plots/gaussian_fit_m1.pdf')
plt.show()

gaus_fit = gaussian(x_vals, *params)
residuals = y_vals - gaus_fit
sigmas = np.sqrt(y_vals)

y_error = residuals/sigmas

plt.plot(x_vals, y_error, label='Residuals')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Residuals')
plt.title(r'\textbf{Residuals of the Gaussian fit of measurement 1}')
plt.legend()
plt.savefig('plots/gaussian_fit_residuals_m1.pdf')
plt.show()
err_a0 = cov[0][0]
err_mean = cov[1][1]
err_std = cov[2][2]
print('a0: {} +- {}'.format(params[0], np.sqrt(err_a0)))
print('Mean: {} +- {}'.format(params[1], np.sqrt(err_mean)))
print('Std: {} +- {}'.format(params[2], np.sqrt(err_std)))

# calculate the total time
total_time = params[1] + params[2]
print('Total time: {} +- {}'.format(total_time, np.sqrt(err_mean**2 + err_std**2)))
