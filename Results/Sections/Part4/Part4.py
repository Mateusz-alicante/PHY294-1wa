import numpy as np

data = [
    "551.2 nm +/- 6 pix  : 4.620",
    "580.6 nm +/- 9 pix : 4.566",
    "748.8 nm +/- 9 pix : 36.634",
    "751.5 nm +/- 9 pix : 52.601",
    "757.6 nm +/- 6 pix : 11.434",
    "760.0 nm +/- 6 pix : 13.071",
    "776.6 nm +/- 8 pix : 7.550",
    "800.1 nm +/- 12 pix : 28.883",
    "803.3 nm +/- 12 pix : 37.835",
    "811.2 nm +/- 7 pix : 12.049",
    "819.3 nm +/- 10 pix : 20.245",
    "822.5 nm +/- 10 pix : 17.873"
]
intensities = [

]

PIX_TO_NM = 0.62256809

wavelengths = []
uncertainties = []
intensity = []

for line in data:
    parts = line.split()
    wavelengths.append(float(parts[0]))
    uncertainties.append(int(parts[3]) * PIX_TO_NM)
    intensity.append(float(parts[6]))

intensity = np.array(intensity) / max(intensity)

for w, u, i in zip(wavelengths, uncertainties, intensity):
    print(f"{w:.2f} nm +/- {u:.2f} nm ; relative intensity {i:.3f}")
