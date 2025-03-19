import numpy as np
import matplotlib.pyplot as plt


# Constants
k_B = 8.617e-5  # Boltzmann constant in eV/K

E = np.linspace(4, 12, 1000)

# Fermi-Dirac distribution function
def fermi_dirac(E, E_F, T):
    return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

# Temperatures in Kelvin
temperatures = [0, 500, 1000, 2000]

# Work functions
wf_LaB6 = 2.40   # Average value in eV https://doi.org/10.1016/j.vacuum.2017.06.029
ef_LaB6 = 2.68    # Approximate value in eV https://doi.org/10.1016/j.vacuum.2017.06.029
wf_W_Ir = 4.5  # Approximate value in eV https://www.researchgate.net/publication/24169123_Simulation_of_attosecond_streaking_of_electrons_emitted_from_a_tungsten_surface
ef_W_Ir = 9.6  # Approximate value in eV https://www.researchgate.net/publication/24169123_Simulation_of_attosecond_streaking_of_electrons_emitted_from_a_tungsten_surface


# Plot for lanthanum hexaborides
plt.figure(figsize=(10, 6))
for T in temperatures:
    f = fermi_dirac(E, ef_LaB6, T)
    plt.plot(E, f, label=f'T = {T} K')

plt.axvline(wf_LaB6, color='r', linestyle='--', label='LaB6 Work Function (2.40 eV)')
plt.xlabel('Energy (eV)')
plt.ylabel('Fermi-Dirac Distribution')
plt.title('Fermi-Dirac Distribution lanthanum hexaborides')
plt.legend(loc = "lower left")
plt.grid(True)

# Zoomed-in inset around work functions
ax_inset = plt.axes([0.52, 0.3, 0.35, 0.35])
for T in temperatures:
    f = fermi_dirac(E, ef_LaB6, T)
    ax_inset.plot(E, f, label=f'T = {T} K')
ax_inset.set_xlim(2.2, 2.6)
ax_inset.set_ylim(0.5, 1.1)
ax_inset.set_title('Zoomed-In View')
ax_inset.axvline(wf_LaB6, color='r', linestyle='--')

plt.savefig('fermi_dirac_la.png')
# plt.show()
plt.clf()


# Plot for tungsten-iridium
plt.figure(figsize=(10, 6))
for T in temperatures:
    f = fermi_dirac(E, ef_W_Ir, T)
    plt.plot(E, f, label=f'T = {T} K')

plt.axvline(wf_W_Ir, color='r', linestyle='--', label='W-Ir Work Function (4.50 eV)')
plt.xlabel('Energy (eV)')
plt.ylabel('Fermi-Dirac Distribution')
plt.title('Fermi-Dirac Distribution Ir-doped Tungsten')
plt.legend(loc = "lower left")
plt.grid(True)

# Zoomed-in inset around work functions
ax_inset = plt.axes([0.25, 0.35, 0.35, 0.35])
for T in temperatures:
    f = fermi_dirac(E, ef_W_Ir, T)
    ax_inset.plot(E, f, label=f'T = {T} K')
ax_inset.set_xlim(4.3, 4.7)
ax_inset.set_ylim(0.5, 1.1)
ax_inset.set_title('Zoomed-In View')
ax_inset.axvline(wf_W_Ir, color='r', linestyle='--')


plt.savefig('fermi_dirac_w.png')
# plt.show()
plt.clf()

# number of thermoelectrons
def thermoelectrons(w, T):
    return k_B*T*np.exp(-w/(k_B*T))

# mean energy of thermoelectrons
def mean_energy(w, T):
    return w + k_B*T

# variance of energy of thermoelectrons
def variance_energy(w, T):
    return (k_B*T)**2

temperature = np.linspace(0, 2000, 1000)
plt.subplot(3, 1, 1)
plt.plot(temperature, thermoelectrons(wf_LaB6, temperature))
plt.xlabel('Temperature (K)')
plt.ylabel('N')
plt.title('Number of Thermoelectrons vs. Temperature')
plt.grid(True)

plt.subplot(3, 1, 2)
y = mean_energy(wf_LaB6, temperature)
# change y[0] to 0
y[0] = 0
plt.plot(temperature, y)
plt.xlabel('Temperature (K)')
plt.ylabel('Mean')
plt.title('Mean Energy of Thermoelectrons vs. Temperature')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(temperature, variance_energy(wf_LaB6, temperature))
plt.xlabel('Temperature (K)')
plt.ylabel('Var')
plt.title('Variance of Energy of Thermoelectrons vs. Temperature')
plt.grid(True)

plt.tight_layout()
plt.savefig('thermoelectrons.png')
# plt.show()
plt.clf()

def surface_transmission(E, w):
    u = 4*np.sqrt(E*(E-w))
    l = (np.sqrt(E)+ np.sqrt(E-w))**2
    return u/l

energy = np.linspace(wf_LaB6, 7, 1000)
plt.plot(energy, surface_transmission(energy, wf_LaB6))
plt.xlabel('Energy (eV)')
plt.ylabel('Transmission')
plt.title('Surface Transmission vs. Energy')
plt.grid(True)
plt.savefig('surface_transmission.png')
# plt.show()

plt.clf()
# extra plot with fermi-dirac distribution
trans_data = surface_transmission(energy, wf_LaB6)
plt.plot(energy, trans_data, label='Surface Transmission')
fermi_data = fermi_dirac(energy, ef_LaB6, 2000)
plt.plot(energy, fermi_data, label='Fermi-Dirac Distribution')
product_data = trans_data * fermi_data
plt.plot(energy, product_data, label='Product')
plt.legend()
plt.xlabel('Energy (eV)')
plt.ylabel('Transmission')
plt.title('Surface Transmission vs. Energy at 2000 K')
plt.savefig('surface_transmission_extra.png')
# plt.show()
plt.clf()

def angle(E):
    m = 9.11e-31
    hbar = 1.05e-34
    ev = 1.6e-19
    upper = np.sqrt(2*m*E*ev)
    lower = hbar*2.91e-10
    return np.arcsin(upper/lower)

energy = np.linspace(10, 500, 1000)
plt.plot(energy, angle(energy))
plt.xlabel('Energy (eV)')
plt.ylabel('Angle')
plt.title('Angle vs. Energy')
plt.grid(True)
plt.savefig('angle.png')
# plt.show()
plt.clf()
