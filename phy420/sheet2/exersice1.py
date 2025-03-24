import numpy as np
import matplotlib.pyplot as plt


def intensity(theta):
    alpha = 90 - 54.7 + theta
    d = 400*(10**-9)*np.sin(np.radians(alpha))
    lamba = 2.45*(10**-9)*np.cos(np.radians(theta))
    x_i = [0.5*10**-9, 1*10**-9, 1.5*10**-9, 2*10**-9]
    epxsum = np.sum([np.exp(-x*(1/d + 1/lamba)) for x in x_i])
    upper = d*lamba
    lower =  (d + lamba)*epxsum
    return upper/lower

thetas = np.linspace(0, 80, 100)
intensities = intensity(thetas)*9**11

plt.plot(thetas, intensities, label='Intensity')
plt.xlabel('Theta (degrees)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Intensity vs Theta with fixed gamma')
plt.legend()
plt.grid(True)
plt.savefig('intensity_vs_theta.png')
plt.show()


def asymmetr_factor(gamma):
    B_si = 1.21
    B_Ga = 1.18
    upper = 1 + (1/2)*B_si*((3/2)*(np.sin(np.radians(gamma)))**2 - 1)
    lower = 1 + (1/2)*B_Ga*((3/2)*(np.sin(np.radians(gamma)))**2 - 1)
    return upper/lower


def intensity2(theta):
    alpha = 9
    gamma = 81 + theta
    asym_fact = asymmetr_factor(gamma)
    d = 400*(10**-9)*np.sin(np.radians(alpha))
    lamba = 2.45*(10**-9)*np.cos(np.radians(theta))
    x_i = [0.5*10**-9, 1*10**-9, 1.5*10**-9, 2*10**-9]
    epxsum = np.sum([np.exp(-x*(1/d + 1/lamba)) for x in x_i])
    upper = d*lamba*asym_fact
    lower =  (d + lamba)*epxsum
    return upper/lower

intensities2 = intensity2(thetas)*9**11
plt.plot(thetas, intensities, label='Intensity with gamma fix')
plt.plot(thetas, intensities2, label='Intensity with alpha fix')
plt.xlabel('Theta (degrees)')
plt.ylabel('Intensity (arbitrary units)')
plt.title('Intensity vs Theta with fixed alpha')
plt.legend()
plt.grid(True)
plt.savefig('intensity_vs_theta2.png')
plt.show()