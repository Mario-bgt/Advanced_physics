import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 6.62607015e-34 / (2 * np.pi)  # Joule second
m_eff = 0.3 * 9.1093837e-31  # effective mass in kg
Omega0 = 0.1  # eV
eV = 1.602176634e-19  # Joules
eta = 0.02  # small imaginary part
kb = 8.617e-5  # Boltzmann constant in eV/K
temp = 273  # Temperature

# Set up the plot style for LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 16,
    "axes.titlesize": 16,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12
})

# Energy and momentum grids
Eb = np.linspace(-0.5, 0.2, 500)  # Binding energy in eV
k = np.linspace(-0.3, 0.3, 500)  # in 1/Angstrom


def self_energy(Eb, lam, Omega0):
    re = (lam * Omega0 / 2) * np.log(np.abs((Omega0 + Eb) / (Omega0 - Eb)))
    im = (-np.pi * lam * Omega0) / 2 * (np.abs(Eb) > Omega0) + eta
    return re, im


def spectral_function(k, Eb, lam, Omega0):
    re, im = self_energy(Eb, lam, Omega0)
    k_dis = (hbar * k * 1e10) ** 2 / (2 * m_eff * eV)
    e_ferm = 1 / (1 + np.exp(Eb / (kb * temp)))
    return (1 / np.pi) * (im / ((Eb - k_dis - re) ** 2 + im ** 2)) * e_ferm


for lam in [1, 2]:
    e_re, e_im = self_energy(Eb, lam, Omega0)
    # Self-energy plot
    plt.figure()
    plt.plot(Eb, e_re, label=r"$\mathrm{Re}\,\Sigma$")
    plt.plot(Eb, e_im, label=r"$\mathrm{Im}\,\Sigma$")
    plt.xlabel(r"$E_b\ \mathrm{(eV)}$")
    plt.ylabel(r"$\Sigma(E_b)$")
    plt.title(rf"Self-energy for $\lambda = {lam}$")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"SelfEnergy_{lam}.png")
    plt.close()

    # Spectral function A(k, Eb)
    image_data = []
    for e_val in Eb:
        row = []
        for k_val in k:
            row.append(spectral_function(k_val, e_val, lam, Omega0))
        image_data.append(row)
    image_data = np.array(image_data)

    # Spectral function plot
    plt.figure()
    plt.imshow(image_data, aspect='auto', extent=[k.min(), k.max(), Eb.min(), Eb.max()],
               origin='lower', cmap='Greys')
    plt.colorbar(label=r"Intensity")
    plt.xlabel(r"$k\ (\mathrm{\AA}^{-1})$")
    plt.ylabel(r"$E_b\ \mathrm{(eV)}$")
    plt.title(rf"Spectral Function for $\lambda = {lam}$")
    plt.tight_layout()
    plt.savefig(f"SpectralFunction_{lam}.png")
    plt.close()
