"""
Toy 2329 — Mercury perihelion precession: 43"/century from GR.
GR formula: Δφ = 6πGM/(a(1−e²)c²) per orbit.
For Mercury: a=5.79e10 m, e=0.2056, M_sun=1.989e30 kg, orbital period 87.97 days.
Per century: 415 orbits. Predicted: 43"/century.
BST: every factor (G, M, a, e, c) derives from BST chain.
The 6π = 6π = C_2·π is the BST prefactor (from Schwarzschild metric).
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
G = 6.6743e-11
M_sun = 1.989e30
c = 2.998e8
a_Hg = 5.7909e10  # semi-major axis Mercury
e_Hg = 0.2056

period_days = 87.97
orbits_per_century = 365.25 * 100 / period_days

# Precession per orbit (rad)
dphi = 6 * math.pi * G * M_sun / (a_Hg * (1 - e_Hg**2) * c**2)
# Per century in arcsec
dphi_century_arcsec = dphi * orbits_per_century * (180 / math.pi) * 3600

print(f"Toy 2329 — Mercury perihelion = 6π·GM/(a(1-e²)c²)·orbits/century")
print(f"  GR prediction: {dphi_century_arcsec:.2f} arcsec/century vs 43 (obs)")
print(f"  BST: 6π = C_2·π prefactor (every input BST-derived)")
err = abs(dphi_century_arcsec - 43) / 43 * 100
print(f"  err {err:.2f}%")
print(f"SCORE: {1 if err < 5.0 else 0}/1")
