from functions import *
import math

def gauss_expo_convolution(data, mu, sigma, tau, a):
    res = []
    for x in data:
        expo = np.exp((sigma**2-2*tau*x+2*mu*tau)/(2*tau**2))
        ero = math.erfc((tau*(mu-x)+sigma**2)/(np.sqrt(2)*sigma*tau))
        res.append(a * expo * ero)
    return np.array(res)

# Now do the same for measurement 2
data1 = read_spe_file('data/me2_deltatime.Spe')
data2 = read_spe_file('data/me2_deltatime_2.Spe')
data = [x+y for x, y in zip(data1, data2)]

transformed_data = []
window_size = 10

for i in range(len(data)):
    start = max(0, i - window_size)
    end = min(len(data), i + window_size + 1)
    neighbors = data[start:end]
    transformed_value = sum(neighbors)
    transformed_data.append(transformed_value)

data = transformed_data

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_vals = channel_to_time(x_vals)

inital_guess = [2.72e-08, 1.8e-10, 2e-10, 4]
params, cov = curve_fit(gauss_expo_convolution, x_vals, y_vals, p0=inital_guess)
print(params)
# Extract the fitted parameters
mu_fit, sigma_fit, decay_fit, a_fit = params
upper = 10000
lower = 8400
x_vals = x_vals[lower:upper]
y_vals = y_vals[lower:upper]

# Outcomment the next 4 lines if you want it to compile fast, this does Latex label style
A=6
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(x_vals, data[lower:upper], label='Measurement 2')
plt.plot(x_vals, gauss_expo_convolution(x_vals, *params), label='fit')
# also plot the gaussian and expo part
#plt.axvline(params[1], color='r', label='Mean')
#plt.axvline(params[1] + params[2], color='g', label='Mean + std')
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('Counts')
plt.title(r'\textbf{fit of measurement 2}')
plt.legend()
plt.savefig('plots/gaussian_fit_m2_v2.pdf')
plt.show()

residuals = y_vals - gauss_expo_convolution(x_vals, *params)
sigmas = np.sqrt(y_vals)

y_error = residuals/sigmas

plt.plot(x_vals, y_error, label='Residuals')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Residuals')
plt.title(r'\textbf{Residuals of the fit of measurement 2}')
plt.legend()
plt.savefig('plots/gaussian_fit_residuals_m2_v2.pdf')
plt.show()
err_mean = np.sqrt(np.diag(cov))[0]
err_std = np.sqrt(np.diag(cov))[1]
err_tau = np.sqrt(np.diag(cov))[2]
err_a = np.sqrt(np.diag(cov))[3]
print('Mean: {} +- {}'.format(params[0], err_mean))
print('Std: {} +- {}'.format(params[1], err_std))
print('Tau: {} +- {}'.format(params[2], err_tau))
print('A: {} +- {}'.format(params[3], err_a))



tot_time = mu_fit + sigma_fit + decay_fit
err_tot_time = np.sqrt(err_mean**2 + err_std**2 + err_tau**2)
print('Total time: {} +- {}'.format(tot_time, err_tot_time))
