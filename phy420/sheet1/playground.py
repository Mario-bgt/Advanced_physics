import numpy as np
import matplotlib.pyplot as plt

def angle(E):
    m = 9.11e-31  # kg
    hbar = 1.05e-34  # J·s
    ev = 1.6e-19  # J/eV
    E = E * ev  # Convert energy from eV to Joules

    upper = hbar
    lower = 2.91 * (10**(-10)) * np.sqrt( 2 * m * E)
    print(upper, lower)
    ratio = upper / lower

    # Prevent out-of-domain errors
    ratio = np.clip(ratio, -1, 1)  # Ensures values are in the valid range for arccos

    return np.degrees(np.arctan(ratio))


energy = np.linspace(10, 500, 1000)  # Energy values in eV
print(energy)
angle = [angle(E) for E in energy]

plt.plot(energy, angle)
plt.xlabel('Energy (eV)')
plt.ylabel('Angle (degrees)')
plt.title('Angle vs. Energy')
plt.grid(True)
plt.savefig('angle.png')
# plt.show()
plt.clf()