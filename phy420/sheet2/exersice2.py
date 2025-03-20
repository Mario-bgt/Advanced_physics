import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('Ex2-XPS-GaN.txt', delimiter=',')
x = data[:,0]
y = data[:,1]

print(x[0], y[0])

def gauss(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

def background(x, a, b):
    return a * x + b

def fit_function(x, a, b, c, d, e):
    return gauss(x, a, b, c) + background(x, d, e)

# plot data
plt.plot(x, y, 'ro', label='data', markersize=3)
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (a.u.)')
plt.legend()
plt.grid(True)
plt.savefig('data.png')
plt.show()

# plot N1s peak at 397.5 eV
energy = x[590:620]
intensity = y[590:620]

# fit data
params, pcov = curve_fit(fit_function, energy, intensity, p0=[180000, -397.5, 2, 0, 0])
print(params)

# Generate more x values for a smoother fit
x_fine = np.linspace(min(energy), max(energy), 1000)

# Generate the fitted curve with the more densely spaced x values
y_fine = fit_function(x_fine, *params)

# Subtract the linear background from the intensity data
intensity_corrected = intensity - (params[3] * energy + params[4])

# Plot the corrected data and the smoother fit
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity_corrected, 'bo', label="Data (-background)")
plt.plot(x_fine, y_fine - (params[3] * x_fine + params[4]), 'r-', label="Gaussian fit")

# Shade the area under the corrected curve
area = np.sum(y_fine - (params[3] * x_fine + params[4])) * (x_fine[1] - x_fine[0])
plt.fill_between(x_fine, y_fine - (params[3] * x_fine + params[4]), color='red', alpha=0.3, label=f'Area = {area:.2e}')

# Adding labels and title
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Corrected Gaussian Fit to N 1s Peak (Smoothed and Background Subtracted)')
plt.legend()
plt.grid(True)
plt.savefig('N1s_peak.png')
plt.show()

# plot Ga3p peak at 105 eV
energy = x[1171:1221]
intensity = y[1171:1221]

# fit data
params, pcov = curve_fit(fit_function, energy, intensity, p0=[111000, -105, 2, 0, 0])
print(params)

# Generate more x values for a smoother fit
x_fine = np.linspace(min(energy), max(energy), 1000)

# Generate the fitted curve with the more densely spaced x values
y_fine = fit_function(x_fine, *params)

# Subtract the linear background from the intensity data
intensity_corrected = intensity - (params[3] * energy + params[4])

# Plot the corrected data and the smoother fit
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity_corrected, 'bo', label="Data (-background)")
plt.plot(x_fine, y_fine - (params[3] * x_fine + params[4]), 'r-', label="Gaussian fit")

# Shade the area under the corrected curve
area = np.sum(y_fine - (params[3] * x_fine + params[4])) * (x_fine[1] - x_fine[0])
plt.fill_between(x_fine, y_fine - (params[3] * x_fine + params[4]), color='red', alpha=0.3, label=f'Area = {area:.2e}')

# Adding labels and title
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Corrected Gaussian Fit to Ga 3p (Smoothed and Background Subtracted)')
plt.legend()
plt.grid(True)
plt.savefig('Ga3p_peak.png')
plt.show()
