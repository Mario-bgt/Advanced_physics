import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.optimize import curve_fit

path = Path("data_fig_3.txt")
df = pd.read_csv(path, comment="#", header=None, names=["T", "invchi"]).dropna()
df = df.drop_duplicates(subset=["T","invchi"]).sort_values("T").reset_index(drop=True)

def model(T, Tc, A, gamma):
    x = np.clip(T - Tc, 1e-9, None)
    return A * (x ** gamma)

Tc_guess = 53.0
A_guess = 1.0
gamma_guess = 1.3
p0 = [Tc_guess, A_guess, gamma_guess]
bounds = ([50.0, 0.0, 0.1], [56.0, np.inf, 3.0])

# fit only near-Tc region to avoid far non-critical tail; choose T>~52.8 K
df_fit = df[df["T"] > 52.8].copy()
T = df_fit["T"].values
Y = df_fit["invchi"].values


popt, pcov = curve_fit(model, T, Y, p0=p0, bounds=bounds, maxfev=200000)
perr = np.sqrt(np.diag(pcov))


Tc_fit, A_fit, gamma_fit = popt

print("Best-fit parameters (±1σ where available):")
print(f"Tc     = {Tc_fit:.4f} K  ± {perr[0]}")
print(f"A      = {A_fit:.6g}    ± {perr[1]}")
print(f"gamma  = {gamma_fit:.4f}   ± {perr[2]}")

# Make plots
T_plot = np.linspace(df["T"].min(), df["T"].max(), 500)
Y_plot = model(T_plot, *popt)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df["T"], df["invchi"], s=8, label="data", color="blue")
ax.plot(T_plot, Y_plot, linewidth=2, label="fit", color="orange")
ax.axvline(Tc_fit, linestyle="--", linewidth=1, label="Tc fit")
ax.set_xlabel("T (K)")
ax.set_ylabel("Inverse susceptibility 1/χ (arb. u.)")
ax.set_title(f"Inverse susceptibility fit (γ ≈ {gamma_fit:.4f})")
ax.legend()
plt.tight_layout()
plt.savefig("fig_3.png", dpi=300)
plt.show()
