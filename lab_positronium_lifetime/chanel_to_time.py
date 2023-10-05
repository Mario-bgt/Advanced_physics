from functions import *

data = read_spe_file('data/timeconverter_0_4_8_12_16_20.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)

peaks = [8890, 10175, 11508, 12800, 14120, 15410]
mean = []
sigma = []

for i in peaks:
    x_data = x_vals[i-100:i+100]
    y_data = y_vals[i-100:i+100]
    params = fit_gaussian(x_data, y_data)
    mean.append(params[1])
    sigma.append(params[2])
    plt.plot(x_data, y_data, label='Measurement 1')
    plt.plot(x_data, gaussian(x_data, *params), label='Gaussian fit')
    # also plot the mean and std
    plt.axvline(params[1], color='r', label='Mean', linestyle='--')
    plt.axvline(params[1] + params[2], color='g', label='Mean + std', linestyle='--')
    plt.grid()
    plt.xlabel('Channel')
    plt.ylabel('Counts')
    plt.title('Gaussian fit of measurement 1')
    plt.legend()
    # plt.show()

plt.clf()


def linear(x, m, c):
    return m*x + c


time = [0, 4*10**-9, 8*10**-9, 12*10**-9, 16*10**-9, 20*10**-9]
mean = np.array(mean)
popt = fit_linear(mean, time)
print(popt)
plt.plot(mean, time, 'o', label='Data')
plt.plot(mean, linear(mean, popt[0], popt[1]), label='Linear fit')
plt.xlabel('Channel')
plt.ylabel('Time [ns]')
plt.title('Linear fit of channel vs time')
plt.legend()
plt.grid()
plt.show()





