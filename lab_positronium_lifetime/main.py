import matplotlib.pyplot as plt

from functions import *

data = read_spe_file('data/total_spec.Spe')

x_vals = np.arange(0, len(data), 1)
y_vals = np.array(data)
x_vals = x_vals[:8000]
y_vals = y_vals[:8000]

# plot the whole spectrum
plt.plot(x_vals, y_vals, label='Total spectrum')

plt.fill_between(x_vals, y_vals, color='lightblue', alpha=0.5)
plt.annotate('511 keV', xy=(2650, 900), xytext=(2650, 1200),
             arrowprops=dict(arrowstyle='->'),
             fontsize=12)
plt.annotate('1275 keV', xy=(6550, 100), xytext=(6550, 400),
             arrowprops=dict(arrowstyle='->'),
             fontsize=12)

plt.annotate('"Compton edge"', xy=(2000, 250), xytext=(4000, 600),
             arrowprops=dict(arrowstyle='->'),
             fontsize=12)
plt.annotate('               ', xy=(6000, 50), xytext=(4000, 600),
             arrowprops=dict(arrowstyle='->'),
             fontsize=12)

plt.annotate('"Noise"', xy=(100, 1250), xytext=(1100, 1200),
             arrowprops=dict(arrowstyle='->'),
             fontsize=12)
# reduce the plotting height to 14400
plt.ylim(0, 1400)
plt.grid()
plt.xlabel('Channel, proportional to energy')
plt.ylabel('Counts')
plt.title('Total spectrum')
plt.legend()
plt.savefig('plots/total_spectrum.pdf')
plt.show()
