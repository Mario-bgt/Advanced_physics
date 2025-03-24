import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad
data = np.loadtxt('Ex2-XPS-GaN.txt', delimiter=',')
x = data[:,0]
y = data[:,1]


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

def gauss_only(x):
    a, b, c  = params[:3]
    return a * np.exp(-(x - b)**2 / (2 * c**2))

# Generate more x values for a smoother fit
x_fine = np.linspace(min(energy), max(energy), 1000)

# Generate the fitted curve with the more densely spaced x values
y_fine = fit_function(x_fine, *params)

# Subtract the linear background from the intensity data
area_N = quad(gauss_only, min(energy), max(energy))[0]
intensity_corrected = intensity - (params[3] * energy + params[4])

# Plot the corrected data and the smoother fit
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity_corrected, 'bo', label="Data (-background)")
plt.plot(x_fine, y_fine - (params[3] * x_fine + params[4]), 'r-', label="Gaussian fit")

# Shade the area under the corrected curve
plt.fill_between(x_fine, y_fine - (params[3] * x_fine + params[4]), color='red', alpha=0.3, label=f'Area = {area_N:.2e}')

# Adding labels and title
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Corrected Gaussian Fit to N 1s Peak (Smoothed and Background Subtracted)')
plt.legend()
plt.grid(True)
plt.savefig('N1s_peak.png')
plt.show()

# plot Ga3s peak at 160 eV
energy = x[1061:1101]
intensity = y[1061:1101]

# fit data
params, pcov = curve_fit(fit_function, energy, intensity, p0=[42000, -160, 2, 0, 0])
print(params)

def gauss_only(x):
    a, b, c  = params[:3]
    return a * np.exp(-(x - b)**2 / (2 * c**2))

# Generate more x values for a smoother fit
x_fine = np.linspace(min(energy), max(energy), 1000)

# Generate the fitted curve with the more densely spaced x values
y_fine = fit_function(x_fine, *params)

# Subtract the linear background from the intensity data
area_Ga = quad(gauss_only, min(energy), max(energy))[0]
intensity_corrected = intensity - (params[3] * energy + params[4])

# Plot the corrected data and the smoother fit
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity_corrected, 'bo', label="Data (-background)")
plt.plot(x_fine, y_fine - (params[3] * x_fine + params[4]), 'r-', label="Gaussian fit")

# Shade the area under the corrected curve
plt.fill_between(x_fine, y_fine - (params[3] * x_fine + params[4]), color='red', alpha=0.3, label=f'Area = {area_Ga:.2e}')

# Adding labels and title
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Corrected Gaussian Fit to Ga 3s (Smoothed and Background Subtracted)')
plt.legend()
plt.grid(True)
plt.savefig('Ga3p_peak.png')
plt.show()

sigma_Ga = 0.03
sigma_N = 0.07
ratio = (area_Ga*sigma_N) / (area_N*sigma_Ga)
print(ratio)

# plot c1S peak at 285 eV
energy = x[821:841]
intensity = y[821:841]

# fit data
params, pcov = curve_fit(fit_function, energy, intensity, p0=[34000, -285, 2, 0, 0])
print(params)

def gauss_only(x):
    a, b, c  = params[:3]
    return a * np.exp(-(x - b)**2 / (2 * c**2))

# Generate more x values for a smoother fit
x_fine = np.linspace(min(energy), max(energy), 1000)

# Generate the fitted curve with the more densely spaced x values
y_fine = fit_function(x_fine, *params)

# Subtract the linear background from the intensity data
area_c = quad(gauss_only, min(energy), max(energy))[0]
intensity_corrected = intensity - (params[3] * energy + params[4])

# Plot the corrected data and the smoother fit
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity_corrected, 'bo', label="Data (-background)")
plt.plot(x_fine, y_fine - (params[3] * x_fine + params[4]), 'r-', label="Gaussian fit")

# Shade the area under the corrected curve
plt.fill_between(x_fine, y_fine - (params[3] * x_fine + params[4]), color='red', alpha=0.3, label=f'Area = {area_c:.2e}')

# Adding labels and title
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Corrected Gaussian Fit to C 1s (Smoothed and Background Subtracted)')
plt.legend()
plt.grid(True)
plt.savefig('C_1S_peak.png')
plt.show()

area_corr_c = area_c*1.00
area_corr_N = area_N*1.8
area_corr_Ga = area_Ga*1.13
tot_area = area_corr_c + area_corr_N + area_corr_Ga
perc_c = (area_corr_c / tot_area) * 100
print(perc_c)