import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the provided LIXS spectra data
file_path = 'LiF.csv'
lixs_data = pd.read_csv(file_path)

# Cleaning column names
lixs_data.columns = lixs_data.columns.str.strip()

# Extracting data for plotting
wavelength = lixs_data['Wavelength [nm]']
intensity = lixs_data['Intensity [64 bit] LiF_1.tif']

# Finding peaks in the spectrum
peaks, properties = find_peaks(intensity, height=1000, prominence=0.1)

# Extracting peak properties for visualization
peak_wavelengths = wavelength.iloc[peaks].reset_index(drop=True)
peak_intensities = intensity.iloc[peaks].reset_index(drop=True)

# Updated assignments based on user input
custom_assigned_peaks = {
    "F VII": [9.44, 12.7],
    "Li III": [11.24, 13.41],
    "F VI": [13.88, 14.52]
}

# Plotting the spectrum alone
plt.figure(figsize=(12, 8))
plt.plot(wavelength, intensity, label="LiF Spectrum", linewidth=1.5, color="darkkhaki")

# Adjusting x-axis ticks to have steps of 1 nm
plt.xticks(ticks=range(int(wavelength.min()), int(wavelength.max()) + 1, 1))
plt.ylim(top=36000)
plt.xlim(6, 20)
plt.title("LIXS Spectrum of LiF raw", fontsize=25)
plt.xlabel("Wavelength (nm)", fontsize=15)
plt.ylabel("Intensity [64 bit]", fontsize=15)
plt.grid(True)
plt.legend(loc="upper right")
plt.savefig("LIXS_spectra_raw.jpg")
plt.show()

# Plotting the spectrum with identified peaks
plt.figure(figsize=(12, 8))
plt.plot(wavelength, intensity, label="LiF Spectrum", linewidth=1.5, color="darkkhaki")
plt.scatter(peak_wavelengths, peak_intensities, color='red', label="Identified Peaks")
plt.ylim(top=36000)
plt.xlim(6, 20)
plt.title("LIXS Spectrum of LiF with peaks", fontsize=25)
plt.xlabel("Wavelength (nm)", fontsize=15)
plt.ylabel("Intensity [64 bit]", fontsize=15)
plt.grid(True)
plt.legend()
plt.savefig("LIXS_spectra_peaks.jpg")
plt.show()

# Displaying the identified peaks' details
peak_data = pd.DataFrame({
    "Wavelength (nm)": peak_wavelengths.values,
    "Intensity": peak_intensities.values
})



# Plotting the spectrum with user-defined peak assignments
plt.figure(figsize=(12, 8))
plt.plot(wavelength, intensity, label="LiF Spectrum", linewidth=1.5, color="darkkhaki")

# Highlighting the specified peaks with labels directly on the plot
for element, positions in custom_assigned_peaks.items():
    for pos in positions:
        closest_peak_idx = (peak_wavelengths - pos).abs().idxmin()
        closest_peak_wavelength = peak_wavelengths.iloc[closest_peak_idx]
        closest_peak_intensity = peak_intensities.iloc[closest_peak_idx]
        plt.scatter(closest_peak_wavelength, closest_peak_intensity, s=100, color = 'hotpink')
        plt.text(closest_peak_wavelength, closest_peak_intensity + 1000,  # Offset label slightly above the peak
                 f"{element}",
                 fontsize=18, ha='center', color='blue')

# Adjusting x-axis ticks to have steps of 1 nm
plt.xticks(ticks=range(int(wavelength.min()), int(wavelength.max()) + 1, 1))
plt.ylim(top=36000)
plt.xlim(6, 20)
plt.title("LIXS Spectrum of LiF with Labeled Peaks", fontsize=25)
plt.xlabel("Wavelength (nm)", fontsize=15)
plt.ylabel("Intensity [64 bit]", fontsize=15)
plt.grid(True)
plt.legend(loc="upper right")
plt.savefig("LIXS_spectra.jpg")
plt.show()
