import numpy as np
from uncertainties import ufloat

H = 6.62607015e-34
C = 299792458
EV = 1.602176634e-19

n_states = [2, 3]


state_energies = np.array([-13.6 * 2 ** 2 / (i ** 2) for i in n_states])

print(f"State Energies: {state_energies}")

delta_E = state_energies[1] - state_energies[0]
delta_L = H * C / (delta_E * EV) * 1e9

print(f"Delta E: {delta_E:.2f}")
print(f"Delta L: {delta_L:.2f}")


# Calculate values with uncertainties for table:
pixel_to_nm = 0.613839
observed_pixels = np.array([394.6, 449.4, 499.9, 581.4, 661.0, 699.1])
uncertainties_pixels = np.array([7, 5, 6, 9, 9, 8])

# Convert the observed values and their uncertainties to nm
observed_nm = 1.068 * observed_pixels - 32.7
uncertainties_nm = uncertainties_pixels * pixel_to_nm

# Create a uarray with the observed values and their uncertainties
observed = np.array([ufloat(n, u)
                    for n, u in zip(observed_nm, uncertainties_nm)])


# Print the energy values for each reference observation

for entry in observed:
    print(f"{entry.nominal_value:.2f} \pm {entry.std_dev:.2f}")


reference_wavelengths = np.array(
    [58.43339, 706.5190, 388.8648, 587.5621, 667.8151, 501.56783, 447.14802])

reference_energy = np.array(H * C / (reference_wavelengths * 10 ** -9)) / EV

for entry in reference_energy:
    print(f"{entry:.2f}")
