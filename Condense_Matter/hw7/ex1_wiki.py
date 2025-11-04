# Re-run with the same plotting code (matplotlib only, single axes)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# High-symmetry points in FCC Brillouin zone (units of 2π/a)
L = np.array([0.5, 0.5, 0.5])
Gm = np.array([0.0, 0.0, 0.0])     # Γ
X  = np.array([0.0, 1.0, 0.0])     # X
K  = np.array([0.75, 0.75, 0.0])   # K

# Path: L —(Λ)— Γ —(Δ)— X —(Σ)— K —(Σ)— Γ
segments = [
    ("L", "Γ",   L,  Gm,  r"$\Lambda$"),
    ("Γ", "X",   Gm, X,   r"$\Delta$"),
    ("X", "K",   X,  K,   r"$\Sigma$"),
    ("K", "Γ",   K,  Gm,  r"$\Sigma$"),
]

def sample_segment(k1, k2, n=241, endpoint=False):
    t = np.linspace(0.0, 1.0, n, endpoint=endpoint)
    return (1 - t)[:, None] * k1 + t[:, None] * k2

def bcc_G(R=3):
    h, k, l = np.mgrid[-R:R+1, -R:R+1, -R:R+1]
    h, k, l = h.ravel(), k.ravel(), l.ravel()
    mask = ((h + k + l) % 2 == 0)
    return np.vstack([h[mask], k[mask], l[mask]]).T.astype(float)

Glist = bcc_G(R=3)

# Build k-path and quasi-arclength x-axis
kpts = []
xvals = []
tick_pos = [0.0]
tick_lab = [segments[0][0]]
seg_centers = []
seg_labels  = []

x_accum = 0.0
for a, b, k1, k2, seglab in segments:
    seg = sample_segment(k1, k2, n=241, endpoint=False)
    kpts.append(seg)
    dk = np.linalg.norm(seg[1] - seg[0])
    xs = (x_accum + np.arange(len(seg)) * dk)
    xvals.extend(xs.tolist())
    x_accum = xs[-1] + dk
    tick_pos.append(xs[-1])
    tick_lab.append(b)
    seg_centers.append(0.5 * (xs[0] + xs[-1]))
    seg_labels.append(seglab)

kpts = np.vstack(kpts)
xvals = np.array(xvals)

# Replace the K tick label with "U,K" for the middle tick
tick_lab = [tick_lab[0], tick_lab[1], tick_lab[2], "U,K", tick_lab[4]]

def smallest_bands_at_k(kvec, Glist, N):
    KG = Glist + kvec
    E = np.einsum('ij,ij->i', KG, KG)
    idx = np.argpartition(E, N)[:N]
    return np.sort(E[idx])

Nbands = 8
Emat = np.array([smallest_bands_at_k(k, Glist, Nbands) for k in kpts])

plt.figure(figsize=(9, 5), dpi=140)
for n in range(Nbands):
    plt.plot(xvals, Emat[:, n], linewidth=1.5, linestyle='-.' )

for tp in tick_pos[1:]:
    plt.axvline(tp, color='k', linewidth=0.6, alpha=0.6)

plt.xticks(tick_pos, tick_lab)
plt.ylabel(r"$E \; / \; \frac{\hbar^2}{2ma^2}$")
plt.title("Empty lattice approximation for a face‑centered cubic crystal")

y_top = np.max(Emat) * 1.04
for xc, lab in zip(seg_centers, seg_labels):
    plt.text(xc, y_top, lab, ha='center', va='bottom', fontsize=12)

plt.ylim(0, np.max(Emat)*1.08)
plt.xlim(xvals[0], xvals[-1])
plt.tight_layout()

plt.savefig("vielen_plot.jpg", bbox_inches="tight")
plt.show()
