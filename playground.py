import numpy as np
import matplotlib.pyplot as plt

# Constants (SI units, simplified for sketch)
e = 1.602e-19  # Elementary charge
epsilon_0 = 8.854e-12  # Vacuum permittivity
hbar = 1.055e-34  # Reduced Planck's constant
m = 9.109e-31  # Electron mass
l = 1  # Angular momentum quantum number

# Effective potential function (simplified, units normalized)
def V_eff(r, l, Z=1):
    """Effective potential for hydrogen atom."""
    coulomb_term = -Z * e**2 / (4 * np.pi * epsilon_0 * r)
    centrifugal_term = (hbar**2 * l * (l + 1)) / (2 * m * r**2)
    return coulomb_term + centrifugal_term

# Radial range for plot
r = np.linspace(0.01e-10, 5e-10, 500)  # Avoid r=0 to prevent singularity

# Energy of the bound state (example E < 0)
E = -0.8e-18  # Approximate energy of hydrogen bound state

# Compute V_eff values
V = V_eff(r, l)



# Plotting
plt.figure(figsize=(8, 6))
plt.plot(r, V, label=r"$V_{\mathrm{eff}}(r)$", color="blue")
plt.axhline(E, color="red", linestyle="--", label=r"Energy $E$")


plt.title("Effective Potential $V_{\mathrm{eff}}(r)$ for $l=1$")
plt.xlabel("Radial Distance $r$ (m)")
plt.ylabel("Potential Energy (J)")
plt.ylim(-5e-18, 5e-18)
plt.legend()
plt.grid()
plt.savefig("effective_potential.png")
plt.show()
