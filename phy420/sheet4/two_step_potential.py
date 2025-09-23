import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


# Load the data
with open("two_step_potential.txt") as f:
    lines = f.readlines()


# Reprocess data correctly from the fourth line onward
data_clean = [line.strip().split() for line in lines[3:]]

# Convert to DataFrame
profile1 = [[float(row[0]), float(row[1])] for row in data_clean if row[0] != '-' or row[1] != '-']
profile2 = [[float(row[2]), float(row[3])] for row in data_clean if row[2] != '-' or row[3] != '-']
profile3 = [[float(row[4]), float(row[5])] for row in data_clean if row[4] != '-' or row[5] != '-']

df1 = pd.DataFrame(profile1, columns=['x', 'y1'])
df2 = pd.DataFrame(profile2, columns=['x', 'y2'])
df3 = pd.DataFrame(profile3, columns=['x', 'y3'])

p1_range = [(0.0, 0.03), (0.05, 0.09), (0.11, 0.16167638)]
p2_range = [(0.0, 0.04), (0.06, 0.13), (0.15, 0.19641476)]
p3_range = [(0.0, 0.04), (0.06, 0.13), (0.15, 0.20086017)]

# Function to perform linear fit on plateau regions
def fit_plateaus(df, y_col, ranges):
    fits = []
    for x_start, x_end in ranges:
        subset = df[(df['x'] >= x_start) & (df['x'] <= x_end)]
        fits.append(np.mean(subset[y_col]))
    return fits

# Fit plateaus for each profile
fits1 = fit_plateaus(df1, 'y1', p1_range)
fits2 = fit_plateaus(df2, 'y2', p2_range)
fits3 = fit_plateaus(df3, 'y3', p3_range)

def plot_fits(df, fits, ranges, label):
    for intercept, (x_start, x_end) in zip(fits, ranges):
        subset = df[(df['x'] >= x_start) & (df['x'] <= x_end)]
        y_data = np.full(len(subset), intercept)
        plt.plot(subset['x'], y_data, linestyle='--', color="red")


# Plot again to verify
plt.figure(figsize=(10, 6))
plt.plot(df1['x'], df1['y1'], label='Profile 1')
plot_fits(df1, fits1, p1_range, 'Profile 1')
plt.plot(df2['x'], df2['y2'], label='Profile 2')
plot_fits(df2, fits2, p2_range, 'Profile 2')
plt.plot(df3['x'], df3['y3'], label='Profile 3')
plot_fits(df3, fits3, p3_range, 'Profile 3')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Two Step Potential - Corrected Data")
plt.legend()
plt.grid(True)
plt.savefig("two_step_potential_corrected.png")
plt.show()


# calculate the heights
def calculate_heights(fits):
    heights = []
    for i in range(len(fits) - 1):
        height = fits[i + 1] - fits[i]
        heights.append(height)
    return heights

heights1 = calculate_heights(fits1)
heights2 = calculate_heights(fits2)
heights3 = calculate_heights(fits3)
heights = [heights1, heights2, heights3]

for i, h in enumerate(heights):
    print(f"Profile {i + 1} Heights: {h}")
mean_height_1 = np.mean([v[0] for v in heights])
std_height_1 = np.std([v[0] for v in heights])
mean_height_2 = np.mean([v[1] for v in heights])
std_height_2 = np.std([v[1] for v in heights])

print(f"Mean Height 1: {mean_height_1}, Std Height 1: {std_height_1}")
print(f"Mean Height 2: {mean_height_2}, Std Height 2: {std_height_2}")
