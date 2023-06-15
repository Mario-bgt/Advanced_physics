import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import *
from tabulate import tabulate
import os


main_files = ['dw_ang20_rt900.14.Spe', 'dw_ang34_rt900.06.Spe', 'dw_ang49_rt900.14.Spe',
              'dw_ang63_rt300.18.Spe', 'dw_ang78_rt300.06.Spe', 'dw_ang92_rt300.10.Spe',
              'dw_ang107_rt900.32.Spe', 'dw_ang121_rt722.36.Spe', 'dw_ang136_rt300.82.Spe']

background_files = ['untergrund_ang20_rt60.00.Spe', 'untergrund_ang34_rt60.00.Spe', 'untergrund_ang49_rt60.00.Spe',
                    'untergrund_ang63_rt60.54.Spe', 'untergrund_ang78_rt60.66.Spe', 'untergrund_ang92_rt60.52.Spe',
                    'untergrund_ang107_rt60.00.Spe', 'untergrund_ang121_rt60.06.Spe', 'untergrund_ang136_rt60.02.Spe']


def normalize(file):
    if file[:2] == 'un':
        real_time = float(file[-9:-4])
    else:
        real_time = float(file[-10:-4])
    # read the file
    spe_file_path = 'data/' + file
    count_lyst = np.array(read_spe_file(spe_file_path))

    # normalize the counts
    count_lyst = count_lyst / real_time

    return count_lyst


def calculate_counts(main_file, background_file):
    norm_main = normalize(main_file)
    norm_back = normalize(background_file)

    # subtract the background
    tot = norm_main - norm_back

    # reduce the data to the expected range
    upper = int(keV_to_marker(1000))
    tot = tot[:upper]
    return np.sum(tot), np.sum(norm_main), np.sum(norm_back)


counts = []
counts_std = []
norm_main_l = []
norm_main_std = []
norm_back_l = []
norm_back_std = []

for i, file in enumerate(main_files):
    count, n_main, n_back = calculate_counts(file, background_files[i])
    counts.append(count)
    norm_main_l.append(n_main)
    norm_back_l.append(n_back)
    counts_std.append(np.sqrt(count))
    norm_main_std.append(np.sqrt(n_main))
    norm_back_std.append(np.sqrt(n_back))

angels = [20, 34, 49, 63, 78, 92, 107, 121, 136]
# print the data as latex table
table = np.array([angels, counts, counts_std, norm_main_l, norm_main_std, norm_back_l, norm_back_std]).T
print('angel & counts & counts std & norm main & norm main std & norm back & norm back std')
print(tabulate(table, tablefmt="latex_raw", floatfmt=".5f"))
