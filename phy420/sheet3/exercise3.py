import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 6.582119569e-16  # eV·s
m0 = 0.51099895069e6  # ev/c^2
m_eff = 0.3 * m0
Omega0 = 0.1  # eV
eta = 0.02  # small imaginary part
kb = 8.617e-5  # Boltzmann constant in eV/K
temp = 200  # Temperature

# Energy and momentum grids
Eb = np.linspace(-0.5, 0.2, 500)  # Binding energy in eV
k = np.linspace(0, 5, 500)  # in 1/Angstrom
K, EB = np.meshgrid(k, Eb)

# epsilon_k: non-interacting electron band energy
epsilon_k = (hbar**2 * (K * 1e10)**2) / (2 * m_eff)  # in eV


def self_energy(Eb, lam, Omega0):
    Eb = np.asarray(Eb)
    re = (lam * Omega0 / 2) * np.log(np.abs((Omega0 + Eb) / (Omega0 - Eb)))
    im = -np.pi * lam * Omega0 * (np.abs(Eb) > Omega0) + eta
    return re, im


def fermi_dirac(E, T=temp):
    return 1 / (1 + np.exp(E / (kb * T)))


for lam in [1, 2]:
    Re_Sigma_1D, Im_Sigma_1D = self_energy(Eb, lam, Omega0)
    # Plot real/imaginary self-energy
    plt.figure()
    plt.plot(Eb, Re_Sigma_1D, label="Re[Σ]")
    plt.plot(Eb, Im_Sigma_1D, label="Im[Σ]")
    plt.xlabel("Eb (eV)")
    plt.ylabel("Self-energy")
    plt.title(f"Self-energy for λ={lam}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"SelfEnergy_{lam}.png")
    plt.close()

    # Compute self-energy
    Re_Sigma, Im_Sigma = self_energy(EB, lam, Omega0)
    Im_Sigma += eta  # Ensure numerical stability

    # Spectral function A(k, Eb)
    A = (1 / np.pi) * np.abs(Im_Sigma) / ((EB - epsilon_k - Re_Sigma) ** 2 + Im_Sigma ** 2)

    # Apply Fermi-Dirac distribution
    A *= fermi_dirac(EB, T=20)  # T = 20 K for finite temperature

    # Transpose A so Eb is x-axis and k is y-axis
    A_flipped = A.T  # Now A[k_index, eb_index]

    # Plot: Eb on x-axis, k on y-axis
    plt.figure(figsize=(8, 6))
    plt.imshow(
        A_flipped,
        origin='lower',
        aspect='auto',
        extent=[Eb.min(), Eb.max(), k.min(), k.max()],
        cmap='gray',
        interpolation='bilinear'
    )
    plt.colorbar(label="Spectral Intensity")
    plt.xlabel("Binding Energy $E_b$ (eV)")
    plt.ylabel("Momentum $k$ (1/Å)")
    plt.title(f"ARPES (λ = {lam}) — $A(k, E_b)$")
    plt.tight_layout()
    plt.savefig(f"ARPES_Eb_x_Lambda{lam}.png")
    plt.close()

    # Compute self-energy
    Re_Sigma, Im_Sigma = self_energy(EB, lam, Omega0)
    Im_Sigma += eta  # Ensure numerical stability

    # Spectral function A(Eb, k)
    A = (1 / np.pi) * np.abs(Im_Sigma) / ((EB - epsilon_k - Re_Sigma) ** 2 + Im_Sigma ** 2)

    # Apply Fermi-Dirac distribution
    A *= fermi_dirac(EB, T=20)  # Use a finite temperature (T = 20 K for example)

    # Create an array to store A(Eb, k) as rows (each row corresponds to a k value)
    A_matrix = np.zeros((len(k), len(Eb)))

    # Fill A_matrix with A(Eb, k)
    for i, k_val in enumerate(k):
        A_matrix[i, :] = A[:, i]  # Each row represents a momentum k, each column is Eb

    # Plot: Eb on x-axis, A(Eb, k) on y-axis, color according to k
    plt.figure(figsize=(8, 6))
    plt.imshow(
        A_matrix,
        origin='lower',
        aspect='auto',
        extent=[Eb.min(), Eb.max(), 0, A_matrix.shape[0]],  # y-axis represents A(Eb, k)
        cmap='inferno',  # Change color map to represent momentum
        interpolation='bilinear'
    )
    plt.colorbar(label="Momentum k (1/Å)")
    plt.xlabel("Binding Energy $E_b$ (eV)")
    plt.ylabel("Spectral Intensity $A(E_b, k)$")
    plt.title(f"ARPES Spectral Function $A(E_b, k)$ (λ = {lam})")
    plt.tight_layout()
    plt.savefig(f"ARPES_Spectral_Function_Lambda{lam}.png")
    plt.close()