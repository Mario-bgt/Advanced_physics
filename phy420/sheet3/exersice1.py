import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
from sympy.abc import alpha

# Define data path and file names
data_path = Path("data/")
file_names = [
    "ARPES_517eV_theta.txt",
    "ARPES_517eV_eb.txt",
    "ARPES_517eV_data.txt",
    "ARPES_815eV_theta.txt",
    "ARPES_815eV_eb.txt",
    "ARPES_815eV_data.txt",
    "ARPES_1159eV_theta.txt",
    "ARPES_1159eV_eb.txt",
    "ARPES_1159eV_data.txt"
]

dfs = []
labels = ['517eV', '815eV', '1159eV']

for i in range(3):
    raw_tht = np.loadtxt(data_path / file_names[3 * i], delimiter=",")
    raw_eb = np.loadtxt(data_path / file_names[3 * i + 1], delimiter=",")
    data_array = np.loadtxt(data_path / file_names[3 * i + 2], delimiter=",")
    raw_tht = np.ravel(raw_tht)
    raw_eb = np.ravel(raw_eb)
    df = pd.DataFrame(data_array, index=raw_eb, columns=raw_tht)
    df.index.name = "Eb"
    df.columns.name = "theta"
    dfs.append(df)

data_517 = dfs[0]
data_815 = dfs[1]
data_1159 = dfs[2]

print(data_517.head())
print(data_517.info())
Eb_correction = [-0.54, -1.15, -2.4]
theto_corr = [0.16, 0.34, 0.38]
"""
for i, df in enumerate(dfs):
    mask = df > 15000
    qualifying_eb = df.index[mask.any(axis=1)]
    if not qualifying_eb.empty:
        max_eb = qualifying_eb.max()
        eb_row = df.loc[max_eb]
        qualifying_theta = eb_row[eb_row > 15000].index.tolist()
        print(f"Dataset {labels[i]}: max E_b where intensity > 40000 = {max_eb:.4f} eV")
    else:
        max_eb = 0
        qualifying_theta = []
        print(f"Dataset {labels[i]}: No intensity > 40000 found. Setting correction to 0.")

    print(f"Qualifying theta values: {qualifying_theta}")
    theto_corr.append(qualifying_theta)
    Eb_correction.append(max_eb)

print(f"Correction values: {Eb_correction}")
"""

for i in range(3):
    df = dfs[i].copy()
    corrected_index = df.index - Eb_correction[i]
    df.index = corrected_index
    df.index.name = "Eb (corrected)"
    dfs[i] = df  # overwrite with corrected version

for i, df in enumerate(dfs):
    plt.figure(figsize=(8, 6))
    plt.imshow(
        df.values,
        aspect='auto',
        origin='lower',
        extent=[
            df.columns.min(), df.columns.max(),  # theta range (x-axis)
            df.index.min(), df.index.max()  # Eb range (y-axis)
        ],
        cmap='hot',
    )

    plt.colorbar(label="Intensity")
    plt.xlabel(r"$\theta$", fontsize=12)
    plt.ylabel(r"$E_b$ [eV]", fontsize=12)
    # Plot overlay points
    plt.plot(theto_corr[i], 0, 'o', markersize=4, color='cyan', label='fit point', alpha=0.4)
    plt.title(f"ARPES {labels[i]}", fontsize=18)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(False)
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"ARPES_{labels[i]}.png", dpi=600)
    plt.clf()

energies = [517, 815, 1159]
for i in range(3):
    df = dfs[i].copy()
    corrected_columns = (df.columns - theto_corr[i])
    corrected_columns = 0.5124*np.sqrt(energies[i])*np.sin(np.deg2rad(corrected_columns))
    df.columns = corrected_columns
    df.columns.name = "theta (corrected)"
    dfs[i] = df  # overwrite with corrected version

for i, df in enumerate(dfs):
    plt.figure(figsize=(8, 6))
    plt.imshow(
        df.values,
        aspect='auto',
        origin='lower',
        extent=[
            df.columns.min(), df.columns.max(),  # theta range (x-axis)
            df.index.min(), df.index.max()  # Eb range (y-axis)
        ],
        cmap='hot',
    )

    plt.colorbar(label="Intensity")
    plt.xlabel(r"$k_x\: [\AA{}^{-1}]$ ", fontsize=12)
    plt.ylabel(r"$E_b$ [eV]", fontsize=12)
    plt.title(f"ARPES {labels[i]} with correction", fontsize=18)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(False)
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"ARPES_{labels[i]}_corr.png", dpi=600)
    plt.clf()

k_z = []
for en in energies:
    k_z.append(0.5124*np.sqrt(en+14.5))
print(k_z)
