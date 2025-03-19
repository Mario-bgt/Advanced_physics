import numpy as np
import matplotlib.pyplot as plt

# Define parameters
d = 2.0  # Thickness of As layer in nm
lambda_Si = 2.45  # IMFP of Si 2p electrons in nm
theta_range = np.linspace(0, 80, 100)  # Emission angles in degrees

# Convert theta to radians
theta_rad = np.radians(theta_range)

# Compute the normalized intensity ratio
I_ratio = np.exp(-d / (lambda_Si * np.cos(theta_rad)))

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(theta_range, I_ratio, label=r'$I_{Si}/I_{As}$', linewidth=2)
plt.xlabel(r'Emission Angle $\theta$ (degrees)')
plt.ylabel(r'Normalized Intensity $I_{Si} / I_{As}$')
plt.title('Si 2p Core Level Intensity Normalized to As 3d')
plt.grid(True)
plt.legend()
plt.show()

# Compute the normalized intensity ratio under the new condition (alpha = 9°)
I_ratio_new = np.exp(-d / (lambda_Si * np.cos(theta_rad)))

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(theta_range, I_ratio, label=r'$I_{Si}/I_{As}$ (α = 0°)', linewidth=2, linestyle='dashed', color='orange')
plt.plot(theta_range, I_ratio_new, label=r'$I_{Si}/I_{As}$ (α = 9°)', linewidth=2, color='blue')

plt.xlabel(r'Emission Angle $\theta$ (degrees)')
plt.ylabel(r'Normalized Intensity $I_{Si} / I_{As}$')
plt.title('Comparison of Si 2p Core Level Intensity Normalized to As 3d')
plt.grid(True)
plt.legend()
plt.show()
