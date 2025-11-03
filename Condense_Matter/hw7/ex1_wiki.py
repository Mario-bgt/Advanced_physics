import numpy as np
import matplotlib.pyplot as plt

# ---- High-symmetry points (FCC BZ; k in units of 2π/a) ----
L = np.array([0.5, 0.5, 0.5])
Gm = np.array([0.0, 0.0, 0.0])   # Γ
X  = np.array([0.0, 1.0, 0.0])
K  = np.array([0.75, 0.75, 0.0])
U  = np.array([0.625, 1.0, 0.25])  # not on the main path, shown only in label

# Path per your sketch: L —(Λ)— Γ —(Δ)— X —(Σ)— K —(Σ)— Γ
segments = [
    ("L",   "Γ",   L,  Gm, "Λ"),
    ("Γ",   "X",   Gm, X,  "Δ"),
    ("X",   "K",   X,  K,  "Σ"),
    ("K",   "Γ",   K,  Gm, "Σ"),
]

def sample_segment(k1, k2, n=241, endpoint=False):
    t = np.linspace(0, 1, n, endpoint=endpoint)
    return (1-t)[:,None]*k1 + t[:,None]*k2

# ---- BCC reciprocal lattice vectors G: h+k+l even ----
def bcc_G(R=3):
    h,k,l = np.mgrid[-R:R+1, -R:R+1, -R:R+1]
    h,k,l = h.ravel(), k.ravel(), l.ravel()
    mask = ((h+k+l) % 2 == 0)
    return np.vstack((h[mask], k[mask], l[mask])).T.astype(float)

Glist = bcc_G(R=3)

# ---- Build k-path and quasi-arclength x-axis ----
kpts = []
xvals = []
tick_pos = [0.0]
tick_lab = ["L"]
seg_centers = []   # for placing Λ, Δ, Σ above segments
seg_labels  = []

x_accum = 0.0
for a,b,k1,k2,seg_lab in segments:
    seg = sample_segment(k1, k2, n=241, endpoint=False)
    kpts.append(seg)
    dk = np.linalg.norm(seg[1]-seg[0])
    xs = x_accum + np.arange(len(seg))*dk
    xvals.extend(xs.tolist())
    x_accum = xs[-1] + dk
    tick_pos.append(xs[-1])
    tick_lab.append(b)
    seg_centers.append(0.5*(xs[0] + xs[-1]))
    seg_labels.append(seg_lab)

# Replace the K tick label with "U,K" as in your picture
tick_lab = [tick_lab[0], tick_lab[1], tick_lab[2], "U,K", tick_lab[4]]

kpts = np.vstack(kpts)
xvals = np.array(xvals)

# ---- Free-electron energies: take N smallest |k+G|^2 per k ----
def smallest_bands(kvec, Glist, N=12):
    Kg = Glist + kvec
    E  = np.einsum('ij,ij->i', Kg, Kg)
    idx = np.argpartition(E, N)[:N]
    return np.sort(E[idx])

Nbands = 12
Emat = np.array([smallest_bands(k, Glist, Nbands) for k in kpts])

# ---- Plot ----
plt.figure(figsize=(5,8), dpi=140)
for n in range(Nbands):
    plt.plot(xvals, Emat[:, n], lw=1.2, color='r')

# vertical lines at point ticks (skip the first at 0)
for tp in tick_pos[1:]:
    plt.axvline(tp, color='k', lw=0.6, alpha=0.6)

# segment labels above the path (Λ, Δ, Σ, Σ)
y_top = np.max(Emat)*0.97
for xc, lab in zip(seg_centers, seg_labels):
    plt.text(xc, y_top, lab, ha='center', va='bottom', fontsize=12)

plt.xticks(tick_pos, tick_lab)
plt.ylabel(r"$E$  (arb.; $\hbar^2/2m=1$, $\mathbf{k}$ in $2\pi/a$)")
plt.title("Empty-lattice FCC bands along L–Γ–X–K–Γ (segments: Λ, Δ, Σ, Σ)")
plt.tight_layout()
plt.show()
