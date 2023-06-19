import matplotlib.pyplot as plt
import numpy as np

from functions import *
import os
from scipy.optimize import curve_fit
from tabulate import tabulate

def E_out_expected(theta, E_in=674.942):
    """
    :param theta: angle in degrees
    :param E_in: incident energy in keV
    :return: energy in MeV
    """
    mc2 = 510.998  # mass of the electron in keV from wikipedia
    denominator = 1 + (E_in / mc2) * (1 - np.cos(np.deg2rad(theta)))
    E_out = E_in / denominator
    return E_out


angels = [20, 34, 49, 63, 78, 92, 107, 121, 136]

E_out_expected_list = [E_out_expected(angel) for angel in angels]

main_files = ['dw_ang20_rt900.14.Spe', 'dw_ang34_rt900.06.Spe', 'dw_ang49_rt900.14.Spe',
              'dw_ang63_rt300.18.Spe', 'dw_ang78_rt300.06.Spe', 'dw_ang92_rt300.10.Spe',
              'dw_ang107_rt900.32.Spe', 'dw_ang121_rt722.36.Spe', 'dw_ang136_rt300.82.Spe']

background_files = ['untergrund_ang20_rt60.00.Spe', 'untergrund_ang34_rt60.00.Spe', 'untergrund_ang49_rt60.00.Spe',
                    'untergrund_ang63_rt60.54.Spe', 'untergrund_ang78_rt60.66.Spe', 'untergrund_ang92_rt60.52.Spe',
                    'untergrund_ang107_rt60.00.Spe', 'untergrund_ang121_rt60.06.Spe', 'untergrund_ang136_rt60.02.Spe']

first_main = ['dw_ang63_rt900.04.Spe', 'dw_ang78_rt900.04.Spe', 'dw_ang92_rt900.04.Spe']
first_background = ['untergrund_ang63_rt60_pt1.Spe', 'untergrund_ang78_rt60_pt1.Spe', 'untergrund_ang92_rt60_pt1.Spe' ]
second_main = ['dw_ang63_rt300.18.Spe', 'dw_ang78_rt300.06.Spe', 'dw_ang92_rt300.10.Spe']
second_background = ['untergrund_ang63_rt60.54.Spe', 'untergrund_ang78_rt60.66.Spe', 'untergrund_ang92_rt60.52.Spe']

# plot the data of first_main vs second_main:
for i in range(len(first_main)):
    spe_file_path = 'data/' + first_main[i]
    count_lyst_first = np.array(read_spe_file(spe_file_path))
    real_time_first = float(first_main[i][-10:-4])
    count_lyst_first = count_lyst_first / real_time_first
    count_lyst_first = count_lyst_first[:int(keV_to_marker(1000))]
    plt.plot(count_lyst_first, label='first measurement', alpha=0.5)
    spe_file_path = 'data/' + second_main[i]
    count_lyst_second = np.array(read_spe_file(spe_file_path))
    real_time_second = float(second_main[i][-10:-4])
    count_lyst_second = count_lyst_second / real_time_second
    ang = first_main[i].split('_')[1].split('ang')[1]
    count_lyst_second = count_lyst_second[:int(keV_to_marker(1000))]
    plt.plot(count_lyst_second, label='second measurement', alpha=0.5)
    plt.title('Comparison of the first and second measurement of the angle ' + ang + '°')
    plt.xlabel('channel')
    plt.ylabel('counts per second')
    plt.legend()
    plt.savefig('plots/first_vs_second_' + ang + '.pdf')
    # plt.show()
    plt.clf()


def time_finde(file):
    if file in first_main or file in main_files:
        return float(file[-10:-4])
    elif file in background_files:
        return float(file[-9:-4])
    elif file in first_background:
        return 60.0


def find_equalizer(file, background, expected_energy, figure=False):
    """
    :param file: the file to be read
    :param background: the background file
    :return: the counts per seconds, the energy and the standard deviation
    """
    count_lyst = np.array(read_spe_file('data/' + file))
    real_time = time_finde(file)
    count_lyst = count_lyst / real_time
    background_lyst = np.array(read_spe_file('data/' + background))
    background_real_time = time_finde(background)
    background_lyst = background_lyst / background_real_time
    energy = marker_to_keV(np.arange(len(count_lyst)))
    upper = int(keV_to_marker(expected_energy + 100))
    lower = int(keV_to_marker(expected_energy - 100))
    count_lyst = count_lyst[lower:upper]
    background_lyst = background_lyst[lower:upper]
    energy = energy[lower:upper]
    count_mean = np.mean(count_lyst)
    count_std = np.std(count_lyst)
    background_mean = np.mean(background_lyst)
    background_std = np.std(background_lyst)
    count_mean = count_mean - background_mean
    count_std = np.sqrt(count_std ** 2 + background_std ** 2)
    print('counts mean: ', count_mean)
    print('counts std: ', count_std)
    # Gaussian fit:
    x = np.arange(len(count_lyst))
    popt, pcov = curve_fit(gaussian, x, count_lyst, p0=[np.max(count_lyst), np.argmax(count_lyst), 1])
    ene_mean = popt[1]
    ene_mean = energy[int(ene_mean)]
    ene_std = popt[2]
    print('energy expected: ', expected_energy)
    print('energy mean: ', ene_mean)
    print('energy std: ', marker_to_keV(ene_std))
    if figure:
        # plot the data:
        plt.plot(energy, count_lyst, label='data')
        plt.plot(energy, background_lyst, label='background', alpha=0.5)
        plt.plot(energy, gaussian(x, *popt), label='fit')
        plt.title('Gaussian fit of the data')
        plt.xlabel('energy in keV')
        plt.ylabel('counts per second')
        plt.legend()
        # plt.savefig('plots/gaussian_fit_' + file.split('_')[1].split('ang')[1] + '.pdf')
        plt.show()
    return count_mean, count_std, ene_mean, ene_std


counts_mean_first = []
counts_std_first = []
energy_mean_first = []
energy_std_first = []
counts_mean_second = []
counts_std_second = []
energy_mean_second = []
energy_std_second = []


for i in [0, 1]:
    counts_mean, counts_std, energy_mean, energy_std = find_equalizer(first_main[i], first_background[i], E_out_expected_list[i + 3])
    counts_mean_first.append(counts_mean)
    counts_std_first.append(counts_std)
    energy_mean_first.append(energy_mean)
    energy_std_first.append(energy_std)
    counts_mean, counts_std, energy_mean, energy_std = find_equalizer(second_main[i], second_background[i], E_out_expected_list[i + 3])
    counts_mean_second.append(counts_mean)
    counts_std_second.append(counts_std)
    energy_mean_second.append(energy_mean)
    energy_std_second.append(energy_std)

# find the equalizer factor:
equalizer_factor = np.sqrt((counts_mean_second[0] / counts_mean_first[0])**2+(counts_mean_second[1] / counts_mean_first[1])**2)


def counts_per_seconds(file, background, expected_energy, figure=False):
    """
    :param file: the file to be read
    :param background: the background file
    :return: the counts per seconds, the energy and the standard deviation
    """
    # check at witch postion in the list the file is:
    ang = angels[main_files.index(file)]
    count_lyst = np.array(read_spe_file('data/' + file))
    real_time = time_finde(file)
    count_lyst = count_lyst / real_time
    background_lyst = np.array(read_spe_file('data/' + background))
    background_real_time = time_finde(background)
    background_lyst = background_lyst / background_real_time
    energy = marker_to_keV(np.arange(len(count_lyst)))
    upper = int(keV_to_marker(expected_energy + 100))
    lower = int(keV_to_marker(expected_energy - 100))
    count_lyst = count_lyst[lower:upper]
    background_lyst = background_lyst[lower:upper]
    energy = energy[lower:upper]
    count_mean = np.mean(count_lyst)
    count_std = np.std(count_lyst)
    background_mean = np.mean(background_lyst)
    background_std = np.std(background_lyst)
    count_mean = count_mean - background_mean
    count_std = np.sqrt(count_std ** 2 + background_std ** 2)
    if ang < 60:
        count_mean = count_mean * equalizer_factor
        count_std = count_std * equalizer_factor
    print('counts mean: ', counts_mean)
    print('counts std: ', counts_std)
    # Gaussian fit:
    x = np.arange(len(count_lyst))
    popt, pcov = curve_fit(gaussian, x, count_lyst, p0=[np.max(count_lyst), np.argmax(count_lyst), 1])
    ene_mean = popt[1]
    ene_mean = energy[int(ene_mean)]
    ene_std = popt[2]
    print('energy expected: ', expected_energy)
    print('energy mean: ', ene_mean)
    print('energy std: ', marker_to_keV(ene_std))
    if figure:
        # plot the data:
        plt.plot(energy, count_lyst, label='data')
        plt.plot(energy, background_lyst, label='background', alpha=0.5)
        plt.plot(energy, gaussian(x, *popt), label='fit')
        plt.title('Gaussian fit of the data')
        plt.xlabel('energy in keV')
        plt.ylabel('counts per second')
        plt.legend()
        # plt.savefig('plots/gaussian_fit_' + file.split('_')[1].split('ang')[1] + '.pdf')
        plt.show()
    return count_mean, count_std, ene_mean, ene_std


counts_mean_lyst = []
counts_std_lyst = []
energy_mean_lyst = []
energy_std_lyst = []
for i, file in enumerate(main_files):
    counts_mean, counts_std, energy_mean, energy_std = counts_per_seconds(file, background_files[i], E_out_expected_list[i])
    counts_mean_lyst.append(counts_mean)
    counts_std_lyst.append(counts_std)
    energy_mean_lyst.append(energy_mean)
    energy_std_lyst.append(energy_std)

# plot the data:
plt.errorbar(angels, energy_mean_lyst, yerr=counts_std_lyst, fmt='o', label='data')
plt.title('Counts per second')
plt.xlabel('energy in keV')
plt.ylabel('counts per second')
plt.legend()
plt.savefig('plots/counts_per_second.pdf')
plt.show()


