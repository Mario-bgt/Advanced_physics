import numpy as np
import matplotlib.pyplot as plt

for Vij in [0, 0.1, 0.5]:
    # Define parameters
    k = np.linspace(-2, 2, 100)  # k values in 1/Angstrom
    E = np.zeros((3, len(k)))
    V0 = 0  # Assuming V0 is 0, adjust if needed
    G0 = 0
    G1 = 1
    Gm1 = -1

    # Compute eigenvalues for each k
    for i in range(len(k)):
        H = np.array([
            [3.81 * (k[i] + G0)**2 + V0, Vij, Vij],
            [Vij, 3.81 * (k[i] + G1)**2 + V0, Vij],
            [Vij, Vij, 3.81 * (k[i] + Gm1)**2 + V0]
        ])
        E[:, i] = np.linalg.eigvalsh(H)  # Use eigvalsh for symmetric/hermitian matrices

    # Plotting
    plt.figure()
    plt.plot(k, E[0, :], 'r', linewidth=3, label=r'$E_1$')
    plt.plot(k, E[1, :], 'g', linewidth=3, label=r'$E_2$')
    plt.plot(k, E[2, :], 'b', linewidth=3, label=r'$E_3$')

    plt.xlabel(r"$k\ [\AA^{-1}]$", fontsize=16)
    plt.ylabel(r"$E\ [eV]$", fontsize=16)
    # plt.xlim([-1, 1])
    # plt.ylim([0, 2.5])
    plt.grid(True)
    plt.title(f"Vij = {Vij}", fontsize=16)
    plt.tick_params(labelsize=14, length=6, width=1)
    plt.box(True)
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"Vij_{Vij*10}.png")
    plt.clf()
