import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Load the data
with open("periodicity_moire.txt") as f:
    lines = f.readlines()


# Reprocess data correctly from the fourth line onward
data_clean = [line.strip().split() for line in lines[3:]]

horizontal = [[float(row[0]), float(row[1])] for row in data_clean if row[0] != '-' or row[1] != '-']
vertical = [[float(row[2]), float(row[3])] for row in data_clean if row[2] != '-' or row[3] != '-']

df_horizontal = pd.DataFrame(horizontal, columns=['x', 'y'])
df_vertical = pd.DataFrame(vertical, columns=['x', 'y'])

# Find peaks in both signals
peaks_horiz, _ = find_peaks(df_horizontal['y'])
peaks_vert, _ = find_peaks(df_vertical['y'])

# Compute peak x-positions and periodicities (differences)
periods_horiz = np.diff(df_horizontal['x'].iloc[peaks_horiz])
periods_vert = np.diff(df_vertical['x'].iloc[peaks_vert])

# Average periodicities
avg_period_horiz = periods_horiz.mean()
avg_period_vert = periods_vert.mean()

# Result summary
periodicity_results = pd.DataFrame({
    "Direction": ["Horizontal (Fast Scan)", "Vertical (Slow Scan)"],
    "Average Periodicity (nm)": [avg_period_horiz, avg_period_vert],
    "Number of Periods Detected": [len(periods_horiz), len(periods_vert)]
})

print("Periodicity Results:")
print(periodicity_results)


plt.figure(figsize=(12, 6))
plt.plot(df_horizontal['x'], df_horizontal['y'], label="Horizontal (Fast Scan)")
plt.plot(df_vertical['x'], df_vertical['y'], label="Vertical (Slow Scan)")
plt.plot(df_horizontal['x'].iloc[peaks_horiz], df_horizontal['y'].iloc[peaks_horiz], 'ko', label="Peaks (Horizontal)")
plt.plot(df_vertical['x'].iloc[peaks_vert], df_vertical['y'].iloc[peaks_vert], 'bo', label="Peaks (Vertical)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphene Moiré Profiles")
plt.legend()
plt.grid(True)
plt.show()