import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, sqrt, latex, ln, sin, cos
from functions import *
import os
from scipy.optimize import curve_fit
from tabulate import tabulate


def E_out_expected(theta, E_in=662):
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

background_files = ['untergrund_ang20_rt60.00.Spe', 'untergrund_ang34_rt60.00.Spe',
                    'untergrund_ang49_rt60.00.Spe',
                    'untergrund_ang63_rt60.54.Spe', 'untergrund_ang78_rt60.66.Spe', 'untergrund_ang92_rt60.52.Spe',
                    'untergrund_ang107_rt60.00.Spe', 'untergrund_ang121_rt60.06.Spe', 'untergrund_ang136_rt60.02.Spe']

first_main = ['dw_ang63_rt900.04.Spe', 'dw_ang78_rt900.04.Spe', 'dw_ang92_rt900.04.Spe']
first_background = ['untergrund_ang63_rt60_pt1.Spe', 'untergrund_ang78_rt60_pt1.Spe', 'untergrund_ang92_rt60_pt1.Spe']
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
    # Gaussian fit:
    x = np.arange(len(count_lyst))
    popt, pcov = curve_fit(gaussian, x, count_lyst, p0=[np.max(count_lyst), np.argmax(count_lyst), 1])
    ene_mean = popt[1]
    ene_mean = energy[int(ene_mean)]
    ene_std = popt[2]
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
        # plt.show()
        plt.clf()
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
    counts_mean, counts_std, energy_mean, energy_std = find_equalizer(first_main[i], first_background[i],
                                                                      E_out_expected_list[i + 3])
    counts_mean_first.append(counts_mean)
    counts_std_first.append(counts_std)
    energy_mean_first.append(energy_mean)
    energy_std_first.append(energy_std)
    counts_mean, counts_std, energy_mean, energy_std = find_equalizer(second_main[i], second_background[i],
                                                                      E_out_expected_list[i + 3])
    counts_mean_second.append(counts_mean)
    counts_std_second.append(counts_std)
    energy_mean_second.append(energy_mean)
    energy_std_second.append(energy_std)

# find the equalizer factor:
equalizer_factor = np.sqrt(
    (counts_mean_second[0] / counts_mean_first[0]) ** 2 + (counts_mean_second[1] / counts_mean_first[1]) ** 2)

print('equalizer factor: ', equalizer_factor)


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
    if ang < 60:
        count_lyst = count_lyst * equalizer_factor
    background_lyst = np.array(read_spe_file('data/' + background))
    background_real_time = time_finde(background)
    background_lyst = background_lyst / background_real_time
    if ang < 60:
        background_lyst = background_lyst * equalizer_factor
    energy = marker_to_keV(np.arange(len(count_lyst)))
    upper = int(keV_to_marker(expected_energy + 100))
    lower = int(keV_to_marker(expected_energy - 100))
    count_lyst = count_lyst[lower:upper]
    background_lyst = background_lyst[lower:upper]
    energy = energy[lower:upper]
    count_mean = np.sum(count_lyst)
    count_std = np.std(count_lyst)
    background_mean = np.sum(background_lyst)
    background_std = np.std(background_lyst)
    count_mean = abs(count_mean - background_mean)
    count_std = np.sqrt(count_std ** 2 + background_std ** 2)
    # Gaussian fit:
    x = np.arange(len(count_lyst))
    popt, pcov = curve_fit(gaussian, x, count_lyst, p0=[np.max(count_lyst), np.argmax(count_lyst), 1])
    ene_mean = popt[1]
    ene_mean = energy[int(ene_mean)]
    ene_std = popt[2]
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
    return count_mean, np.sqrt(count_mean), ene_mean, ene_std


counts_mean_lyst = []
counts_std_lyst = []
energy_mean_lyst = []
energy_std_lyst = []
for i, file in enumerate(main_files):
    counts_mean, counts_std, energy_mean, energy_std = counts_per_seconds(file, background_files[i],
                                                                          E_out_expected_list[i])
    counts_mean_lyst.append(counts_mean)
    counts_std_lyst.append(counts_std)
    energy_mean_lyst.append(energy_mean)
    energy_std_lyst.append(energy_std * 0.5)


# make a table:
print('angle & measured energy & expected energy & difference & sigma & count rate & sigma\\\\')
for i, ang in enumerate(angels):
    print(str(ang) + ' & ' + str(round(energy_mean_lyst[i], 2)) + ' & ' + str(round(E_out_expected_list[i], 2)) + ' & '
          + str(round(abs(energy_mean_lyst[i] - E_out_expected_list[i]), 2)) + ' & ' + str(round(energy_std_lyst[i], 2))
          + ' & ' + str(round(counts_mean_lyst[i], 4)) + ' & ' + str(round(counts_std_lyst[i], 5)) + ' \\\\')


energy_mean_zero = marker_to_keV(2248.046)
energy_std_zero = marker_to_keV(79.136)


# fit the count rate vs angle:
def count_rate_expected(x, a, b):
    return a * np.exp(-b * x)


popt, pcov = curve_fit(count_rate_expected, angels, counts_mean_lyst, p0=[np.max(counts_mean_lyst), 0.035])

print('a: ', popt[0], 'b: ', popt[1])

x_fit = np.linspace(0, 140, 1000)
y_fit = count_rate_expected(x_fit, *popt)


# plot the count rate vs angle
plt.errorbar(angels, counts_mean_lyst, xerr=2.62, yerr=counts_std_lyst, fmt='b.', label='measured', capsize=3,
                elinewidth=1,
                markeredgewidth=1)
plt.plot(x_fit, y_fit, 'r-', label='fit')
# plot the initial guess for the fit:
plt.plot(x_fit, count_rate_expected(x_fit, np.max(counts_mean_lyst), 0.035), 'g--', label='initial guess')
plt.title('Measured Count Rate vs Angle')
plt.xlabel('Angle [degrees]')
plt.ylabel('Count Rate [1/s]')
plt.legend()
plt.grid()
plt.savefig('plots/count_rate_vs_angle.pdf')
# plt.show()
plt.clf()

count_mean_zero = count_rate_expected(0, *popt)
count_std_zero = np.sqrt(count_mean_zero)

print('count rate at 0 degrees: ' + str(count_mean_zero) + ' +- ' + str(count_std_zero))

# add the zero degree data to the lists:
counts_mean_lyst.insert(0, count_mean_zero)
counts_std_lyst.insert(0, count_std_zero)
energy_mean_lyst.insert(0, energy_mean_zero)
energy_std_lyst.insert(0, energy_std_zero)
angels.insert(0, 0)

E_out_expected_list.insert(0, E_out_expected(0))

# for completness plot again the table:
print('angle & measured energy & expected energy & difference & sigma & count rate & sigma\\\\')
for i, ang in enumerate(angels):
    print(str(ang) + ' & ' + str(round(energy_mean_lyst[i], 2)) + ' & ' + str(round(E_out_expected_list[i], 2)) + ' & '
          + str(round(abs(energy_mean_lyst[i] - E_out_expected_list[i]), 2)) + ' & ' + str(round(energy_std_lyst[i], 2))
          + ' & ' + str(round(counts_mean_lyst[i], 4)) + ' & ' + str(round(counts_std_lyst[i], 5)) + ' \\\\')


popt, pcov = curve_fit(E_out_expected, angels, energy_mean_lyst, sigma=energy_std_lyst, absolute_sigma=True)

# plot the data:
plt.errorbar(angels, energy_mean_lyst, xerr=2.62, yerr=energy_std_lyst, fmt='b.', label='measured', capsize=3,
             elinewidth=1,
             markeredgewidth=1)
plt.plot(angels, E_out_expected_list, 'g--', label='expected')
plt.plot(angels, E_out_expected(angels, *popt), 'r-', label='fit', alpha=0.5)
plt.title('Measured and Expected Energy vs Angle')
plt.xlabel('Angle [degrees]')
plt.ylabel('Energy [keV]')
plt.legend()
plt.grid()
plt.savefig('plots/energy_vs_angle.pdf')
# plt.show()
plt.clf()


def calc_diffcross(R_sc,  R_sc_err):
    # Define the symbols
    R_scatter, R_scatter_err, v, v_err, Z, N_A, sigma_D, sigma_D_err, R_0, R_0_err, d_t, d_t_err = symbols('R_{scattered} R_scatter_err V v_err Z N_A Omega_D sigma_D_err R_gamma R_0_err d_{target} d_t_err')

    # Define the formula
    function = (R_scatter * v) / (R_0 * Z * d_t * N_A * sigma_D)

    # Print it in latex
    latex_func = latex(function, mul_symbol='\\cdot ')
    print(f"Latex of function: {latex_func}")

    # Define the variables and their errors
    variables = {R_scatter: R_sc, v: 1.56*10**(-5), Z: 13, N_A: 6.022*10**(23), sigma_D: 5*10**(-3), R_0: count_mean_zero, d_t: 0.3*10**(-2)}
    errors = {R_scatter: R_sc_err, v: 0.522*10**(-5), Z: 0, N_A: 0, sigma_D: 0.4489*10**(-3), R_0: count_std_zero, d_t: 10**(-4)}

    # Calculate the partial derivatives
    partial_derivatives = {var: diff(function, var) for var in variables}

    # Calculate the absolute error for each variable
    absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

    # Calculate the squared absolute errors and sum them
    squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

    # Calculate the total absolute error
    total_absolute_error = sqrt(squared_errors_sum)

    # Print the results
    print("Partial derivatives:")
    for var, derivative in partial_derivatives.items():
        print(f"Partial derivative of {var}")
        latex_func = latex(derivative, mul_symbol='\\cdot ')
        print(f"Latex of partial derivative: {latex_func}")

    # Print the result
    print(f"Result: {function.subs(variables)} +- {total_absolute_error}")

    return function.subs(variables), total_absolute_error

# calculate the differential cross section for each angle:
diff_cross_lyst = []
diff_cross_err_lyst = []
for i, ang in enumerate(angels):
    diff_cross, diff_cross_err = calc_diffcross(counts_mean_lyst[i], counts_std_lyst[i])
    diff_cross_lyst.append(diff_cross)
    diff_cross_err_lyst.append(diff_cross_err)

# print the table:
print('angle & diff cross & sigma\\\\')
for i, ang in enumerate(angels):
    print(str(ang) + ' & ' + str(round(diff_cross_lyst[i]*10**27, 4)) + ' & ' + str(round(diff_cross_err_lyst[i]*10**27, 5)) + ' \\\\')


def calc_kappa(ang):
    # Define the symbols
    E, E_err, m, m_err, theta, theta_err = symbols('E E_err m_e m_err theta theta_err')

    # Define the formula
    kappa = 1/(1 + (E/m)*(1 - cos(theta)))

    # Print it in latex
    latex_func = latex(kappa, mul_symbol='\\cdot ')
    print(f"Latex of function: {latex_func}")

    # Define the variables and their errors
    variables = {E: energy_mean_zero, m: 510.99895000, theta: ang}
    errors = {E: energy_std_zero, m: 15*10**(-8), theta: 0.5}

    # Calculate the partial derivatives
    partial_derivatives = {var: diff(kappa, var) for var in variables}

    # Calculate the absolute error for each variable
    absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

    # Calculate the squared absolute errors and sum them
    squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

    # Calculate the total absolute error
    total_absolute_error = sqrt(squared_errors_sum)

    # Print the results
    print("Partial derivatives:")
    for var, derivative in partial_derivatives.items():
        print(f"Partial derivative of {var}")
        latex_func = latex(derivative, mul_symbol='\\cdot ')
        print(f"Latex of partial derivative: {latex_func}")

    # Print the result
    print(f"Result: {kappa.subs(variables)} +- {total_absolute_error}")

    return kappa.subs(variables), total_absolute_error


# convert angels to radians:
angels_rad = np.deg2rad(angels)

# calculate kappa for each angle:
kappa_lyst = []
kappa_err_lyst = []
for i, ang in enumerate(angels_rad):
    kappa, kappa_err = calc_kappa(ang)
    kappa_lyst.append(kappa)
    kappa_err_lyst.append(kappa_err)

# print the table:
print('angle & kappa & sigma\\\\')
for i, ang in enumerate(angels):
    print(str(ang) + ' & ' + str(round(kappa_lyst[i], 4)) + ' & ' + str(round(kappa_err_lyst[i], 5)) + ' \\\\')


def calc_diff_cross_2(kap, kap_err, ang):
    # Define the symbols
    kappa, kappa_err, r_e, r_e_err, theta = symbols('\kappa kappa_err r_e r_e_err theta')

    # Define the formula
    diff_cross = ((r_e**2)/2)*(kappa - (kappa**2)*sin(theta)**2+kappa**3)

    # Print it in latex
    latex_func = latex(diff_cross, mul_symbol='\\cdot ')
    print(f"Latex of function: {latex_func}")

    # Define the variables and their errors
    variables = {kappa: kap, r_e: 2.8179403227*10**(-15), theta: ang}
    errors = {kappa: kap_err, r_e: 19*10**(-25), theta: 0.5}

    # Calculate the partial derivatives
    partial_derivatives = {var: diff(diff_cross, var) for var in variables}

    # Calculate the absolute error for each variable
    absolute_errors = {var: partial_derivatives[var].subs(variables) * errors[var] for var in variables}

    # Calculate the squared absolute errors and sum them
    squared_errors_sum = sum(abs_err ** 2 for abs_err in absolute_errors.values())

    # Calculate the total absolute error
    total_absolute_error = sqrt(squared_errors_sum)

    # Print the results
    print("Partial derivatives:")
    for var, derivative in partial_derivatives.items():
        print(f"Partial derivative of {var}")
        latex_func = latex(derivative, mul_symbol='\\cdot ')
        print(f"Latex of partial derivative: {latex_func}")

    # Print the result
    print(f"Result: {diff_cross.subs(variables)} +- {total_absolute_error}")

    return diff_cross.subs(variables), total_absolute_error


# calculate the differential cross section for each angle:
diff_cross_lyst_2 = []
diff_cross_err_lyst_2 = []
for i, ang in enumerate(angels_rad):
    diff_cross, diff_cross_err = calc_diff_cross_2(kappa_lyst[i], kappa_err_lyst[i], ang)
    diff_cross_lyst_2.append(diff_cross)
    diff_cross_err_lyst_2.append(diff_cross_err)

# print the table:
print('angle & diff cross & sigma\\\\')
for i, ang in enumerate(angels):
    print(str(ang) + ' & ' + str(round(diff_cross_lyst_2[i]*10**30, 4)) + ' & ' + str(round(diff_cross_err_lyst_2[i]*10**30, 5)) + ' \\\\')


y_data = np.array(diff_cross_lyst_2)*(1/((2.8179403227*10**(-15))**2))
x_data = np.array(angels)

y_data2 = np.array(diff_cross_err_lyst)*(1/((2.8179403227*10**(-15))**2))

# plot the data:
plt.plot(x_data, y_data2, label='first formula')
plt.grid()
plt.xlabel('angle [deg]')
plt.ylabel(r"$differential\: cross \:section \:[\frac{1}{r_0^2}\cdot \frac{d\sigma}{d\Omega}]$")
plt.title('Differential cross section as a function of the angle')
plt.legend()
plt.savefig('plots/diff_cross_section1.pdf')
plt.show()

# plot the data:
plt.plot(x_data, y_data, label='second formula')
plt.grid()
plt.xlabel('angle [deg]')
plt.ylabel(r"$differential\: cross \:section \:[\frac{1}{r_0^2}\cdot \frac{d\sigma}{d\Omega}]$")
plt.title('Differential cross section as a function of the angle')
plt.legend()
plt.savefig('plots/diff_cross_section2.pdf')
plt.show()


