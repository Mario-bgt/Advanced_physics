import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
with open("height_profiles.txt") as f:
    lines = f.readlines()


# Reprocess data correctly from the fourth line onward
data_clean = [line.strip().split() for line in lines[3:]]

# Convert to DataFrame
profile1 = [[float(row[0]), float(row[1])] for row in data_clean if row[0] != '-' or row[1] != '-']
profile2 = [[float(row[2]), float(row[3])] for row in data_clean if row[2] != '-' or row[3] != '-']
profile3 = [[float(row[4]), float(row[5])] for row in data_clean if row[4] != '-' or row[5] != '-']
profile4 = [[float(row[6]), float(row[7])] for row in data_clean if row[6] != '-' or row[7] != '-']
profile5 = [[float(row[8]), float(row[9])] for row in data_clean if row[8] != '-' or row[9] != '-']
profile6 = [[float(row[10]), float(row[11])] for row in data_clean if row[10] != '-' or row[11] != '-']
profile7 = [[float(row[12]), float(row[13])] for row in data_clean if row[12] != '-' or row[13] != '-']
profile8 = [[float(row[14]), float(row[15])] for row in data_clean if row[14] != '-' or row[15] != '-']
profile9 = [[float(row[16]), float(row[17])] for row in data_clean if row[16] != '-' or row[17] != '-']
profile10 = [[float(row[18]), float(row[19])] for row in data_clean if row[18] != '-' or row[19] != '-']

df1 = pd.DataFrame(profile1, columns=['x', 'y'])
df2 = pd.DataFrame(profile2, columns=['x', 'y'])
df3 = pd.DataFrame(profile3, columns=['x', 'y'])
df4 = pd.DataFrame(profile4, columns=['x', 'y'])
df5 = pd.DataFrame(profile5, columns=['x', 'y'])
df6 = pd.DataFrame(profile6, columns=['x', 'y'])
df7 = pd.DataFrame(profile7, columns=['x', 'y'])
df8 = pd.DataFrame(profile8, columns=['x', 'y'])
df9 = pd.DataFrame(profile9, columns=['x', 'y'])
df10 = pd.DataFrame(profile10, columns=['x', 'y'])

p1_range = [(0.0, 0.024), (0.06, np.max(df1['x']))]
p2_range = [(0.0, 0.012), (0.034545268, np.max(df2['x']))]
p3_range = [(0.0, 0.015), (0.055, np.max(df3['x']))]
p4_range = [(0.0, 0.018), (0.055, np.max(df4['x']))]
p5_range = [(0.0, 0.009869093), (0.046878195, np.max(df5['x']))]
p6_range = [(0.0, 0.012), (0.04545268, np.max(df6['x']))]
p7_range = [(0.0, 0.017), (0.045, np.max(df7['x']))]
p8_range = [(0.0, 0.01), (0.04, np.max(df8['x']))]
p9_range = [(0.0, 0.017), (0.06, np.max(df9['x']))]
p10_range = [(0.0, 0.01), (0.054, np.max(df10['x']))]

def fit_height_profile(df, p1_range):
    # Fit a polynomial to the data
    background = []
    for x_start, x_end in p1_range:
        subset = df[(df['x'] >= x_start) & (df['x'] <= x_end)]
        background.append(np.mean(subset['y']))
    back = np.mean(background)
    maxi = np.max(df['y'])
    height = maxi - back
    return back, maxi, height

def plot_fits(df, fit, ranges):
    back, maxi, _ = fit
    y_data = np.full(len(df), back)
    plt.plot(df['x'], y_data, linestyle='--', color="red")
    # plot the maximum
    subset = df[(df['y'] == maxi)]
    plt.scatter(subset['x'], subset['y'], color="red")


fit1 = fit_height_profile(df1, p1_range)
fit2 = fit_height_profile(df2, p2_range)
fit3 = fit_height_profile(df3, p3_range)
fit4 = fit_height_profile(df4, p4_range)
fit5 = fit_height_profile(df5, p5_range)
fit6 = fit_height_profile(df6, p6_range)
fit7 = fit_height_profile(df7, p7_range)
fit8 = fit_height_profile(df8, p8_range)
fit9 = fit_height_profile(df9, p9_range)
fit10 = fit_height_profile(df10, p10_range)

plt.figure(figsize=(10, 6))
plt.plot(df6['x'], df6['y'], label='Profile 6')
plot_fits(df6, fit6, p6_range)
plt.plot(df7['x'], df7['y'], label='Profile 7')
plot_fits(df7, fit7, p7_range)
plt.plot(df8['x'], df8['y'], label='Profile 8')
plot_fits(df8, fit8, p8_range)
plt.plot(df9['x'], df9['y'], label='Profile 9')
plot_fits(df9, fit9, p9_range)
plt.plot(df10['x'], df10['y'], label='Profile 10')
plot_fits(df10, fit10, p10_range)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Height Profiles")
plt.legend()
plt.grid(True)
plt.show()

heights = [fit1[2], fit2[2], fit3[2], fit4[2], fit5[2], fit6[2], fit7[2], fit8[2], fit9[2], fit10[2]]
avg_height = np.mean(heights)
std_height = np.std(heights)
print(f"Average height: {avg_height:.4f}")
print(f"Standard deviation of height: {std_height:.4f}")