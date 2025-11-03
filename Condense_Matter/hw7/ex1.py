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

# assemble k-points and x-axis
x = []
kpts = []
tick_pos = [0.0]   # start so labels match positions
tick_lab = ["L"]
s = 0.0

for (lab1, lab2, kfun) in segs:
    ts = np.linspace(0, 1, 120, endpoint=False)
    kseg = np.array([kfun(t) for t in ts])
    # approximate arclength spacing for a nice x-axis
    dk = np.linalg.norm(kseg[1] - kseg[0])
    x.extend(s + np.arange(len(ts)) * dk)
    s += len(ts) * dk
    kpts.append(kseg)
    tick_pos.append(s)   # end of this segment
    tick_lab.append(lab2)

x = np.array(x)
kpts = np.vstack(kpts)        # shape (N, 3)

# ---- choose a few nearby bands (reciprocal translations) ----
bands = [
    (0,0,0),
    (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1),

]

# ---- E is USED here: evaluate along the whole path for each band ----
for (nx, ny, nz) in bands:
    Evals = [E(kx, ky, kz, nx, ny, nz) for (kx, ky, kz) in kpts]
    plt.plot(x, Evals, lw=1, label=f"({nx},{ny},{nz})")

# cosmetics
for p in tick_pos[1:]:
    plt.axvline(p, color='k', lw=0.5)
plt.xticks(tick_pos, tick_lab)
plt.ylabel("E (arb. units of (2π/a)^2)")
plt.title("Folded free-electron bands along L–Γ–X–K–Γ (fcc BZ)")
# make legfend outside plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
              title="Band indices (nx,ny,nz)")
plt.tight_layout()
plt.show()
