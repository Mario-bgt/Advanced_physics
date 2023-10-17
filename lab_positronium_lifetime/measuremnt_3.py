from functions import *
import math


data = read_spe_file('data/me3_deltatime.Spe')

x_vals = np.arange(0, len(data), 1)
y_data = np.array(data)[8500:11000]
x_data = channel_to_time(x_vals)[8500:11000]



def gauss_expo_convolution(data, mu, sigma, tau):
    res = []
    for x in data:
        expo = np.exp((sigma**2-2*tau*x+2*mu*tau)/(2*tau**2))
        ero = math.erfc((tau*(mu-x)+sigma**2)/(np.sqrt(2)*sigma*tau))
        res.append(expo * ero)
    return np.array(res)


# Define the model function as a sum of Gaussian and two exponential decay components
def model_function(data, mu, sigma, decay1, decay2, a1, a2):
    exp1 = a1*gauss_expo_convolution(data, mu, sigma, decay1)
    exp2 = a2*gauss_expo_convolution(data, mu, sigma, decay2)
    res = exp1 + exp2
    return res


# Initial guesses for the parameters
initial_guess = [2.72e-08, 1.8e-10, 2e-09, 1e-10, 200,200]
# initial_guess = [180, 180, 180, 2.7*10**(-8), 1e-11, 1.25*10**(-10), 1.42*10**(-7)]
# plot the inital guess
plt.plot(x_data, y_data, label='Data with Noise')
plt.plot(x_data, model_function(x_data, *initial_guess), 'r--', label='Initial Guess')
plt.plot(x_data, initial_guess[5]*np.exp(-1 * ((x_data - initial_guess[0])**2) / (2 * initial_guess[1]**2)), 'g--', label='Gaussian')
plt.plot(x_data, initial_guess[4]*gauss_expo_convolution(x_data, initial_guess[0], initial_guess[1], initial_guess[2]), 'y--', label='Exponential 1')
plt.plot(x_data, initial_guess[5]*gauss_expo_convolution(x_data, initial_guess[0], initial_guess[1], initial_guess[3]), 'b--', label='Exponential 2')
plt.legend()
plt.xlabel('Channel')
plt.ylabel('Counts')
plt.title('Initial Guess')
plt.grid()
plt.show()

# Fit the data to the model using curve_fit
params, cov = curve_fit(model_function, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
mu_fit, sigma_fit, decay1_fit, decay2_fit, a1_fit, a2_fit = params




# Plot the original data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Data', s=10, color='black', marker='o', alpha=0.5)
plt.plot(x_data, model_function(x_data, *params), 'r-', label='Fitted Curve')
# Plot individual components (Gaussian and two exponential decays)
plt.fill_between(x_data, y_data, color='yellow', alpha=0.5)
plt.plot(x_data, a1_fit*gauss_expo_convolution(x_data, mu_fit,sigma_fit,decay1_fit), 'y--', label='Exponential 1')
plt.plot(x_data, a2_fit*gauss_expo_convolution(x_data, mu_fit,sigma_fit,decay2_fit), 'b--', label='Exponential 2')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Counts')
plt.title('Fitting Data with Gaussian Detector and Two Exponential Decays')
plt.grid()
plt.savefig('plots/m3_fitting_data.pdf')
plt.show()

residuals = y_data - model_function(x_data, *params)
sigmas = np.sqrt(y_data)
y_error = residuals/sigmas

plt.plot(x_data, y_error, label='Residuals')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Residuals')
plt.title('Residuals of the Gaussian fit of measurement 3')
plt.legend()
plt.savefig('plots/gaussian_fit_residuals_m3.pdf')
plt.show()

err_a1 = cov[4][4]
err_a2 = cov[5][5]
err_mu = cov[0][0]
err_sigma = cov[1][1]
err_decay1 = cov[2][2]
err_decay2 = cov[3][3]

# Print the fitted parameters
print("Fitted Parameters:")
print('a1: {} +- {}'.format(params[4], np.sqrt(err_a1)))
print('a2: {} +- {}'.format(params[5], np.sqrt(err_a2)))
print('mu: {} +- {}'.format(params[0], np.sqrt(err_mu)))
print('sigma: {} +- {}'.format(params[1], np.sqrt(err_sigma)))
print('decay1: {} +- {}'.format(params[2], np.sqrt(err_decay1)))
print('decay2: {} +- {}'.format(params[3], np.sqrt(err_decay2)))

# calculate the total time
total_time_1 = params[0] + params[1] + params[2]
total_time_2 = params[0] + params[1] + params[3]

print('Total time 1: {} +- {}'.format(total_time_1, np.sqrt(err_mu + err_sigma + err_decay1)))
print('Total time 2: {} +- {}'.format(total_time_2, np.sqrt(err_mu + err_sigma+ err_decay2)))

