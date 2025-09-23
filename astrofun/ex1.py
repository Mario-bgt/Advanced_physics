# Re-run the plotting code after kernel reset

import numpy as np
import matplotlib.pyplot as plt

Omega_m0 = 0.30
Omega_rel0 = 8e-5
Omega_L0 = 1.0 - Omega_m0 - Omega_rel0

a = np.logspace(-4, np.log10(2.0), 400)

rho_m = Omega_m0 * a**(-3)
rho_rel = Omega_rel0 * a**(-4)
rho_L = Omega_L0 * np.ones_like(a)

plt.figure(figsize=(8,5))
plt.loglog(a, rho_m, label=r"matter ($\propto a^{-3}$)")
plt.loglog(a, rho_rel, label=r"relativistic ($\propto a^{-4}$)")
plt.loglog(a, rho_L, label=r"flat (const)")

plt.xlabel("Scale factor  a")
plt.ylabel(r"Density  $\rho_i(a)/\rho_{c0}$")
plt.title("Component densities vs scale factor (flat universe)")
plt.grid(True, which="both")
plt.legend()

out_path = "densities_loglog.png"
plt.savefig(out_path, bbox_inches="tight", dpi=150)
plt.show()

