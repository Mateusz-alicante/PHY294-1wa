import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit
import numpy as np


def chi_squared(expected, obtained, std_dev, degrees_freedom, n_measurments=0):

    if not n_measurments:
        n_measurments = len(expected)

    chi_squared = sum(((expected - obtained) / std_dev) ** 2)
    print(f"Chi squared: {chi_squared}")
    reduced_chi_squared = chi_squared / (n_measurments - degrees_freedom)
    print(f"Reduced chi squared: {reduced_chi_squared}")


real = np.array([404.6565, 407.7837, 435.8328, 546.0735, 576.9598, 579.0663])

# Define the pixel to nm conversion factor
pixel_to_nm = 0.89585666

# Define the observed values in pixels and their uncertainties
observed_pixels = np.array([409.4, 412.6, 439, 541.4, 570.9, 573.3])
uncertainties_pixels = np.array([4, 4, 4, 5, 7, 7])

# Convert the observed values and their uncertainties to nm
observed_nm = observed_pixels * pixel_to_nm
uncertainties_nm = uncertainties_pixels * pixel_to_nm

# add errors to observed data
ERROR = 0.05

# Create a uarray with the observed values and their uncertainties
observed = np.array([ufloat(n, max(u, ERROR))
                    for n, u in zip(observed_nm, uncertainties_nm)])


# calculate energies:
H = 6.62607015e-34
C = 299792458
EV = 1.602176634e-19

real_energies = np.array(
    [H * C / (real[i] * 1e-9) / EV for i in range(len(real))])
observed_energies = np.array([H * C / (observed[i] * 1e-9) / EV
                              for i in range(len(observed))])

observed_energies_val = [val.nominal_value for val in observed_energies]

print("Plotting energies")

# Create linear plots of expected vs observed wavelengths with uncertainty
plt.errorbar(real_energies, observed_energies_val,
             yerr=[val.std_dev for val in observed_energies], fmt='o', label="Observed Energies")

plt.xlabel("Real Energies (eV)")
plt.ylabel("Observed Energies (eV)")
plt.title("Observed vs Real Energies")

# Add line of best fit


def fit_function(x, a, b):
    return a * x + b


a_fit, cov = curve_fit(fit_function, real_energies, observed_energies_val)
slope = a_fit[0]
intercept = a_fit[1]
slope_std = np.sqrt(cov[0, 0])
x = np.linspace(min(real_energies), max(real_energies), 100)
y = x * slope + intercept

print(f"line: {slope} ± {slope_std} x + {intercept} ± {np.sqrt(cov[1, 1])}")

chi_squared(real_energies * slope, observed_energies_val,
            np.std(observed_energies_val), 2)

plt.plot(x, y, label="y = {:.3f}x + {:.3f}".format(slope, intercept))
plt.legend()
plt.savefig("Results/Sections/Part1/Part1_energy_observed_vs_expected.png")

plt.clf()
# Compute residuals
residuals = observed_energies_val - (real_energies * slope + intercept)
plt.figure()
plt.errorbar(real_energies, residuals,
             yerr=[val.std_dev for val in observed_energies], fmt='o')

plt.axhline(0, color='black', lw=0.5)

plt.xlabel("Real Energies (eV)")
plt.ylabel("Residuals (eV)")
plt.title("Residuals of observed vs real energies")
plt.savefig(
    "Results/Sections/Part1/Part1_energy_observed_vs_expected_residuals.png")

plt.clf()
# Now do the same but for wavelengths:
print("plotting wavelengths: ==============")

observed_wavelengths_val = [val.nominal_value for val in observed]

# Create linear plots of expected vs observed wavelengths with uncertainty
plt.errorbar(real, observed_wavelengths_val,
             yerr=[val.std_dev for val in observed], fmt='o', label="Observed Wavelengths")

plt.xlabel("Real Wavelengths (nm)")
plt.ylabel("Observed Wavelengths (nm)")
plt.title("Observed vs Real Wavelengths")

# Add line of best fit


def fit_function(x, a, b):
    return a * x + b


a_fit, cov = curve_fit(fit_function, real, observed_wavelengths_val)
slope = a_fit[0]
intercept = a_fit[1]
slope_std = np.sqrt(cov[0, 0])
x = np.linspace(min(real), max(real), 100)
y = x * slope + intercept

print(f"line: {slope} ± {slope_std} x + {intercept} ± {np.sqrt(cov[1, 1])}")

chi_squared(real * slope, observed_wavelengths_val,
            np.std(observed_wavelengths_val), 2)

plt.plot(x, y, label="y = {:.3f}x + {:.3f}".format(slope, intercept))
plt.legend()
plt.savefig("Results/Sections/Part1/Part1_wavelength_observed_vs_expected.png")
plt.clf()
# Compute residuals
residuals = observed_wavelengths_val - (real * slope + intercept)
plt.figure()
plt.errorbar(real, residuals,
             yerr=[val.std_dev for val in observed], fmt='o')

plt.axhline(0, color='black', lw=0.5)

plt.xlabel("Real Wavelengths (nm)")
plt.ylabel("Residuals (nm)")
plt.title("Residuals of observed vs real wavelengths")

plt.savefig(
    "Results/Sections/Part1/Part1_wavelength_observed_vs_expected_residuals.png")
plt.clf()
