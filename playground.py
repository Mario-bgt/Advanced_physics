import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1  # mass (arbitrary units)
omega = 2  # angular frequency (arbitrary units)
E = 1  # total energy (arbitrary units)

# Calculate the maximum values of p and q
q_max = np.sqrt(2 * E / (m * omega**2))
p_max = np.sqrt(2 * m * E)

# Parametric equation for an ellipse in the p-q plane
theta = np.linspace(0, 2 * np.pi, 100)
q_vals = q_max * np.cos(theta)
p_vals = p_max * np.sin(theta)

# Plot the phase space diagram
plt.figure(figsize=(10, 6))
plt.plot(q_vals, p_vals, label='Energy Ellipse (Phase Space)')
plt.xlabel('Position (q) arb. units', fontsize=12)
plt.ylabel('Momentum (p) arb. units', fontsize=12)
plt.title('Phase Space Diagram of a Harmonic Oscillator', fontsize=14)
plt.legend()
plt.savefig('harmonic_oscillator_phase_space.png')
plt.show()
