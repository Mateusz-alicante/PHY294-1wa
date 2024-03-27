import numpy as np
from uncertainties import ufloat

H = 6.62607015e-34
C = 299792458
EV = 1.602176634e-19

# First calcualte expecte energies of balmer line
n = [3, 4, 5]

state_energies = np.array([-13.6 / (i ** 2) for i in n])


FINAL_ENERGY = -13.6 / 2 ** 2

# calculate spectral line energies
line_energy = np.array([state - FINAL_ENERGY for state in state_energies])

line_wavelength = np.array([H * C / (energy * EV)
                           for energy in line_energy]) * 1e9


# Define the pixel to nm conversion factor
pixel_to_nm = 0.628571

# Define the observed values in pixels and their uncertainties
observed_pixels = np.array([437.7, 485.7, 649.5])
uncertainties_pixels = np.array([5, 7, 9])

# Convert the observed values and their uncertainties to nm
observed_nm = 0.936 * observed_pixels + 30.7
uncertainties_nm = uncertainties_pixels * pixel_to_nm

# Create a uarray with the observed values and their uncertainties
observed = np.array([ufloat(n, u)
                    for n, u in zip(observed_nm, uncertainties_nm)])


for i, n in enumerate(n):
    o_val = observed[i].nominal_value
    o_dev = observed[i].std_dev
    print(f"n={n}",
          f"observed wavelength: {o_val:.2f} \pm {o_dev:.2f} nm",
          f"wavelegth = {line_wavelength[i]:.2f} nm",
          f"line energy: {line_energy[i]:.2f} ev",
          f"state energy: {state_energies[i]:.2f} ev", sep="; ")
