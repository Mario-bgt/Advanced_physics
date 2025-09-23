import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

# Load the data
with open("stealme.txt") as f:
    lines = f.readlines()

data_clean = [line.strip().split(sep=",") for line in lines[1:]]
profile = [[float(row[0]), float(row[1])] for row in data_clean]
df = pd.DataFrame(profile, columns=['x', 'y'])

def exponential(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the data
popt, pcov = opt.curve_fit(exponential, df['x'], df['y'])

# Extract the parameters
a, b, c = popt
print(f"Fitted parameters: a={a}, b={b}, c={c}")

plt.figure(figsize=(10, 10))
plt.plot(df['x'], df['y'], 'o', label='Data')
plt.plot(df['x'], exponential(df['x'], *popt), 'r-', label='Fitted curve')
plt.xlabel('Momentum (nm^-1)')
plt.ylabel('Energy (meV)')
plt.title('Exponential Fit')
plt.grid()
plt.legend()
plt.show()

a_fit, b_fit, c_fit = popt  # a in meV·(nm^-2)

# Convert a from meV·nm^2 to SI: J·m^2
a_SI = a_fit * 1e-3 * (1e-18) * (1.6021e-19)  # meV -> J, nm^-2 -> m^-2

# hbar in J·s
hbar = 1.0545718e-34  # J·s

# Calculate effective mass: a = ℏ² / (2m*) => m* = ℏ² / (2a)
m_eff = hbar**2 / (8 * a_SI)

# Normalize to electron mass
m_e = 9.10938356e-31  # kg
m_eff_ratio = m_eff / m_e

print(f"Effective mass: {m_eff} kg")
print(f"Effective mass ratio: {m_eff_ratio} m_e")