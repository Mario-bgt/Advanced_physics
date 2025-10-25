import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_xy(path):
    df = pd.read_csv(path, comment="#", header=None, names=["x","y"])
    df = df.dropna()
    # Keep strictly positive values for log
    df = df[(df["x"]>0) & (df["y"]>0)].copy()
    return df["x"].values, df["y"].values

def loglog_fit(x, y):
    X = np.log(x)
    Y = np.log(y)
    A = np.vstack([X, np.ones_like(X)]).T
    # OLS solution
    m, b = np.linalg.lstsq(A, Y, rcond=None)[0]
    # Residuals and standard errors
    Yhat = m*X + b
    resid = Y - Yhat
    dof = max(0, len(X) - 2)
    s2 = np.sum(resid**2) / dof if dof>0 else np.nan
    Sxx = np.sum( (X - X.mean())**2 )
    sm = np.sqrt(s2 / Sxx) if Sxx>0 and np.isfinite(s2) else np.nan  # 1σ on slope
    sb = np.sqrt(s2*(1/len(X) + X.mean()**2/Sxx)) if Sxx>0 and np.isfinite(s2) else np.nan
    return m, b, sm, sb

# Paths
p_len = Path("1a_coherent_length.txt")
p_scat = Path("1a_coherent_scatter.txt")

# Load data
x_len, y_len = load_xy(p_len)   # x = t, y = kappa
x_scat, y_scat = load_xy(p_scat) # x = (T_N - T), y = intensity

# Fit
m_len, b_len, sm_len, sb_len = loglog_fit(x_len, y_len)  # ν ≈ m_len
m_scat, b_scat, sm_scat, sb_scat = loglog_fit(x_scat, y_scat)  # 2β ≈ m_scat

nu = m_len
nu_err = sm_len
beta = 0.5*m_scat
beta_err = 0.5*sm_scat

print(f"nu (from kappa vs t):  ν = {nu:.4f} ± {nu_err:.4f}")
print(f"beta (from I vs (T_N - T)):  β = {beta:.4f} ± {beta_err:.4f}  (since slope = 2β = {m_scat:.4f} ± {sm_scat:.4f})")

# Plot length fit (log–log)
fig1, ax1 = plt.subplots(figsize=(6.5,5))
ax1.loglog(x_len, y_len, 'o', ms=3, label="data")
# Fit line across range
xx = np.linspace(x_len.min(), x_len.max(), 200)
yy = np.exp(b_len) * xx**m_len
ax1.loglog(xx, yy, '-', lw=2, label=fr"fit: $\kappa \propto t^{{\nu}}$, $\nu={nu:.3f}\pm{nu_err:.3f}$")
ax1.set_xlabel(r"$t=(T-T_N)/T_N$")
ax1.set_ylabel(r"$\kappa$ (arb.)")
ax1.legend()
fig1.tight_layout()
fig1.savefig("ex1a_length_loglog_fit.png", dpi=200, bbox_inches="tight")
plt.close(fig1)

# Plot scatter intensity fit (log–log)
fig2, ax2 = plt.subplots(figsize=(6.5,5))
ax2.loglog(x_scat, y_scat, 'o', ms=3, label="data")
xx = np.linspace(x_scat.min(), x_scat.max(), 200)
yy = np.exp(b_scat) * xx**m_scat
ax2.loglog(xx, yy, '-', lw=2, label=fr"fit: $I \propto (T_N-T)^{{2\beta}}$, $\beta={beta:.3f}\pm{beta_err:.3f}$")
ax2.set_xlabel(r"$T_N - T$ (arb.)")
ax2.set_ylabel(r"$I$ (arb.)")
ax2.legend()
fig2.tight_layout()
fig2.savefig("ex1a_scatter_loglog_fit.png", dpi=200, bbox_inches="tight")
plt.close(fig2)
