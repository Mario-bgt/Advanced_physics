from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

# ---- band energy (units: (2π/a)^2 since ħ²/2m = 1) ----
def E(kx, ky, kz, nx, ny, nz):
    # free-electron parabola repeated in k by integer shifts (band indices)
    return (kx + nx)**2 + (ky + ny)**2 + (kz + nz)**2

# ---- k-path (in units of 2π/a) ----
segs = [
    ("L", "Γ", lambda t: (0.5*(1-t), 0.5*(1-t), 0.5*(1-t))),      # L→Γ
    ("Γ", "X", lambda t: (0.0,         t,         0.0       )),   # Γ→X
    ("X", "K", lambda t: (0.75*t,      1-0.25*t,  0.0       )),   # X→K
    ("K", "Γ", lambda t: (0.75*(1-t),  0.75*(1-t), 0.0      )),   # K→Γ
]

t_arr = np.linspace(0, 1, 100)

k_path = []
for p1, p2, func in segs:
    for t in t_arr:
        k_path.append(func(t))

bands = [
    (0, 0, 0),  # 1st band
    (1, 0, 0),  # 2nd band
    (1, 1, 0),  # 3rd band
    (1, 1, 1),  # 4th band
    (-1, 0, 0),  # 2nd band
    (-1, -1, 0),  # 3rd band
    (-1, -1, -1),  # 4th band
]


E_path = {band: [] for band in bands}
for kx, ky, kz in k_path:
    for band in bands:
        nx, ny, nz = band
        E_path[band].append(E(kx, ky, kz, nx, ny, nz))
E_path = {band: np.array(energies) for band, energies in E_path.items()}
# ---- plot ----
plt.figure(figsize=(8, 6))
x_ticks = []
x_labels = []
x_pos = 0
for p1, p2, func in segs:
    x_ticks.append(x_pos)
    x_labels.append(p1)
    x_pos += len(t_arr)
x_ticks.append(x_pos)
x_labels.append(p2)
plt.xticks(x_ticks, x_labels)
for band, energies in E_path.items():
    plt.plot(range(len(k_path)), energies, label=f"Band {band}")
plt.xlabel("k-path")
plt.ylabel("Energy (units of (2π/a)²)")
plt.title("Free Electron Band Structure along High-Symmetry k-Path")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()