import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Tc = 9.77  # critical temperature (K)

def C_model(T, alpha, A_plus, A_minus, B, E):
    t = (T - Tc) / Tc
    A = np.where(t >= 0, A_plus, A_minus)
    t_safe = np.clip(np.abs(t), 1e-8, None)
    return (A / alpha) * (t_safe ** (-alpha)) + B + E * t

def main(csv_path):
    df = pd.read_csv(csv_path, comment="#", header=None, names=["T", "C"]).dropna()
    df["t"] = (df["T"] - Tc) / Tc
    mask = (np.abs(df["t"]) < 0.2) & (np.abs(df["t"]) > 1e-3)
    fit_df = df.loc[mask]

    T = fit_df["T"].values
    C = fit_df["C"].values

    p0 = [-0.10, 0.30, 0.30, 0.25, 0.0]  # [alpha, A_plus, A_minus, B, E]
    bounds = ([-0.49, 0.0, 0.0, -np.inf, -np.inf], [0.49, np.inf, np.inf, np.inf, np.inf])

    popt, pcov = curve_fit(C_model, T, C, p0=p0, bounds=bounds, maxfev=200000)
    perr = np.sqrt(np.diag(pcov))
    alpha, A_plus, A_minus, B, E = popt

    print("alpha = %.4f ± %.4f" % (alpha, perr[0]))
    print("A_plus = %.4f ± %.4f" % (A_plus, perr[1]))
    print("A_minus = %.4f ± %.4f" % (A_minus, perr[2]))
    print("B = %.4f ± %.4f" % (B, perr[3]))
    print("E = %.4f ± %.4f" % (E, perr[4]))

    T_plot = np.linspace(df["T"].min(), df["T"].max(), 1000)
    C_fit = C_model(T_plot, *popt)

    plt.figure(figsize=(7,5))
    plt.scatter(df["T"], df["C"], s=8, label="data", color="red")
    plt.plot(T_plot, C_fit, linewidth=2, label="fit", color="green")
    plt.axvline(Tc, linestyle="--", linewidth=1, label="T_c")
    plt.xlabel("T (K)")
    plt.ylabel("C (arb. u.)")
    plt.title(f"Specific heat fit (alpha ≈ {alpha:.5f})")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main("data_fig_2.txt")
