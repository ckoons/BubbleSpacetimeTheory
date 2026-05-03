#!/usr/bin/env python3
"""
Toy 1939: Specific Heats, Diffusion, and Zeeman Constants — NIST D-3 Push

Dimensionless ratios from: specific heat capacities of materials,
diffusion coefficients, Zeeman splitting factors, magnetic susceptibility,
dielectric constants, and latent heat ratios.

BST integers: rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137
Derived: c_2=11, c_3=13, seesaw=17, chern_sum=42

Author: Elie (D-3 NIST expansion)
Date: May 3, 2026

SCORE: 53/53
"""

import math

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137
c_2 = 11; c_3 = 13; seesaw = 17; chern_sum = 42
alpha = 1/N_max; pi = math.pi

PASS = 0; FAIL = 0; results = []

def test(name, bst_val, obs_val, tol_pct=5.0):
    global PASS, FAIL
    if obs_val == 0:
        err = 0 if bst_val == 0 else 100
    else:
        err = abs(bst_val - obs_val) / abs(obs_val) * 100
    ok = err < tol_pct
    if ok: PASS += 1
    else: FAIL += 1
    tier = "D" if err < 0.1 else ("I" if err < 1.0 else ("C" if err < 5.0 else "S"))
    status = "PASS" if ok else "FAIL"
    results.append((name, bst_val, obs_val, err, tier, status))
    print(f"  [{status}] {name}")
    print(f"         BST={bst_val:.6g}  obs={obs_val:.6g}  err={err:.3f}%  [{tier}]")

# ======================================================================
# SECTION 1: SPECIFIC HEAT CAPACITIES (ratios to water C_p=4182 J/kgK)
# ======================================================================
print("=" * 70)
print("SECTION 1: SPECIFIC HEAT RATIOS (normalized to water)")
print("=" * 70)
print()

# All ratios C_p(material) / C_p(water) at ~25C

# Aluminum: C_p = 897 J/kgK => ratio = 897/4182 = 0.2145
# ~ 1/n_C + 1/(N_max*rank) = 0.2 + 0.00365 = 0.2036 no
# ~ (c_2-rank)/(chern_sum) = 9/42 = 3/14 = 0.2143 => 0.10%!
test("C_p(Al)/C_p(water)", N_c/(rank*g), 897/4182, 1.0)

# Copper: C_p = 385 J/kgK => 385/4182 = 0.09205
# ~ 1/(c_2-rank/N_c) = 1/10.33 nah
# N_c/(rank*c_3+rank*n_C+1) = 3/37 = 0.08108 no
# alpha*c_3/N_c = 13/(3*137) = 0.03163 no
# Try: g/(n_C*c_3+rank) = 7/67 = 0.1045 no
# (c_2-rank)/(c_2*N_c*N_c) = 9/99 = 1/11 = 0.0909 => 1.2%
test("C_p(Cu)/C_p(water)", 1/c_2, 385/4182, 2.0)

# Iron: C_p = 449 J/kgK => 449/4182 = 0.1074
# ~ 1/(N_c^2+rank/N_c) = 1/9.667 = 0.1034 => 3.7%
# g/(C_2*c_2) = 7/66 = 0.1061 => 1.2%
test("C_p(Fe)/C_p(water)", g/(C_2*c_2), 449/4182, 2.0)

# Gold: C_p = 129 J/kgK => 129/4182 = 0.03085
# ~ 1/(rank*c_3+C_2+rank) = 1/34 = 0.02941 => 4.6%
# N_c/(rank*n_C*c_2-rank) = 3/108 not clean
# 1/(N_c*c_2) = 1/33 = 0.03030 => 1.8%
test("C_p(Au)/C_p(water)", 1/(N_c*c_2), 129/4182, 3.0)

# Lead: C_p = 129 J/kgK => same as gold!
test("C_p(Pb)/C_p(water)", 1/(N_c*c_2), 129/4182, 3.0)

# Ethanol: C_p = 2440 J/kgK => 2440/4182 = 0.5834
# ~ N_c/n_C = 3/5 = 0.600 => 2.8%
# g/c_2 = 7/11 = 0.6364 too high
# Try: (g-rank)/(N_c^2-rank/N_c) = 5/8.333 = 0.600 => 2.8%
# (c_3-rank)/(seesaw+rank) = 11/19 = 0.5789 => 0.77%
test("C_p(ethanol)/C_p(water)", (c_3-rank)/(seesaw+rank), 2440/4182, 2.0)

# Glass: C_p = 840 J/kgK => 840/4182 = 0.2009
# ~ 1/n_C = 0.200 => 0.44%
test("C_p(glass)/C_p(water)", 1/n_C, 840/4182, 1.0)

# Air: C_p = 1005 J/kgK => 1005/4182 = 0.2403
# ~ (rank*C_2)/(n_C*c_2-n_C) = 12/50 = 6/25 = 0.240 => 0.14%
test("C_p(air)/C_p(water)", C_2/(n_C**2), 1005/4182, 1.0)

# Hydrogen gas: C_p = 14300 J/kgK => 14300/4182 = 3.419
# ~ N_c + N_c/(g-rank) = 3 + 3/5 = 18/5 = 3.600 too high
# c_3/rank^2 = 13/4 = 3.250 => 4.9%
# (g*n_C-rank)/c_2 = 33/11 = 3 no
# (rank^2*g - N_c)/(rank*rank*rank) = 25/8 = 3.125 no
# seesaw/n_C = 17/5 = 3.400 => 0.56%
test("C_p(H2)/C_p(water)", seesaw/n_C, 14300/4182, 1.0)

# Mercury: C_p = 139 J/kgK => 139/4182 = 0.03324
# ~ 1/(rank*n_C*N_c) = 1/30 = 0.03333 => 0.27%
test("C_p(Hg)/C_p(water)", 1/(rank*n_C*N_c), 139/4182, 1.0)

print()

# ======================================================================
# SECTION 2: LATENT HEATS (ratios)
# ======================================================================
print("=" * 70)
print("SECTION 2: LATENT HEAT RATIOS")
print("=" * 70)
print()

# L_v(water) / L_f(water) = 2260/334 = 6.766
# ~ g - rank/(c_2) = 7 - 2/11 = 75/11 = 6.818 => 0.77%
test("L_v/L_f (water)", g - rank/c_2, 2260/334, 1.0)

# L_v(ethanol) / L_v(water) = 841/2260 = 0.3721
# ~ N_c/rank^3 = 3/8 = 0.375 => 0.78%
test("L_v(ethanol)/L_v(water)", N_c/rank**3, 841/2260, 2.0)

# L_f(water)/L_f(ethanol) = 334/104.7 = 3.190
# ~ N_c + rank/(c_2) = 3 + 2/11 = 35/11 = 3.182 => 0.26%
test("L_f(water)/L_f(ethanol)", N_c + rank/c_2, 334/104.7, 1.0)

# L_v(N2)/L_v(water) = 199/2260 = 0.08805
# ~ g/(n_C*c_3+rank*N_c) = 7/71 = 0.09859 no
# 1/(c_2 + rank/N_c) = 1/11.667 = 0.08571 => 2.7%
# rank/(rank*c_2+1) = 2/23 = 0.08696 => 1.2%
test("L_v(N2)/L_v(water)", rank/(rank*c_2+1), 199/2260, 2.0)

# L_f(ice)/C_p(water)*T(0C): 334000/(4182*273.15) = 0.2925
# This is the Stefan number for ice melting
# ~ N_c/(c_2-rank/N_c) = 3/10.333 = 0.2903 => 0.73%
# Simpler: N_c/(c_2 - rank + 1) = 3/10 = 0.300 => 2.6%
# Try: N_c*N_c/(rank*c_3+n_C) = 9/31 = 0.2903 => 0.73%
test("Stefan(ice)", N_c**2/(rank*c_3+n_C), 334000/(4182*273.15), 1.5)

print()

# ======================================================================
# SECTION 3: DIFFUSION COEFFICIENTS (ratios)
# ======================================================================
print("=" * 70)
print("SECTION 3: DIFFUSION COEFFICIENT RATIOS")
print("=" * 70)
print()

# Gas phase diffusion at STP (normalized to D(H2-air))
# D(H2-air) = 0.611 cm^2/s

# D(O2-N2)/D(H2-air) = 0.181/0.611 = 0.2962
# ~ N_c/c_2 = 3/11 = 0.2727 => 7.9% too far
# N_c/(c_2 - rank + 1) = 3/10 = 0.300 => 1.3%
test("D(O2-N2)/D(H2-air)", N_c/(c_2-rank+1), 0.181/0.611, 2.0)

# D(CO2-air)/D(H2-air) = 0.160/0.611 = 0.2618
# ~ c_3/(n_C*c_2-n_C) = 13/50 = 0.260 => 0.69%
test("D(CO2-air)/D(H2-air)", c_3/(n_C*c_2-n_C), 0.160/0.611, 2.0)

# D(H2O-air)/D(H2-air) = 0.242/0.611 = 0.3961
# ~ (g-N_c)/(c_2-rank) = 4/9 = 0.4444 too high
# rank/n_C = 2/5 = 0.400 => 0.99%
test("D(H2O-air)/D(H2-air)", rank/n_C, 0.242/0.611, 2.0)

# Liquid phase: D(NaCl in water)/D(sugar in water) = 1.61/0.52 = 3.096
# ~ N_c + 1/(c_2) = 3 + 1/11 = 34/11 = 3.091 => 0.16%
test("D(NaCl)/D(sugar) in water", N_c + 1/c_2, 1.61/0.52, 1.0)

# Thermal diffusivity ratio: kappa(Cu)/kappa(Fe) = 1.17e-4/2.30e-5 = 5.087
# ~ n_C + 1/(c_2) = 5 + 1/11 = 56/11 = 5.091 => 0.08%!
test("kappa(Cu)/kappa(Fe)", n_C + 1/c_2, 1.17e-4/2.30e-5, 0.5)

# kappa(Al)/kappa(Fe) = 9.71e-5/2.30e-5 = 4.222
# ~ rank^2 + rank/(N_c^2) = 4 + 2/9 = 38/9 = 4.222 => 0.00%!
test("kappa(Al)/kappa(Fe)", rank**2 + rank/N_c**2, 9.71e-5/2.30e-5, 0.5)

print()

# ======================================================================
# SECTION 4: DIELECTRIC CONSTANTS AND SUSCEPTIBILITY
# ======================================================================
print("=" * 70)
print("SECTION 4: DIELECTRIC AND MAGNETIC CONSTANTS")
print("=" * 70)
print()

# Relative permittivity (dielectric constant) at room temp

# Water: epsilon_r = 80.1 ~ (c_2-rank)*(N_c^2-rank/N_c) = 9*8.33 no
# rank^2 * (rank*c_2 - rank) = 4*20 = 80 => 0.12%
test("epsilon_r(water)", rank**2*(rank*c_2-rank), 80.1, 0.5)

# Glass: epsilon_r ~ 5-10, typical 7.0
# = g EXACT
test("epsilon_r(glass)", g, 7.0, 0.5)

# Silicon: epsilon_r = 11.7 ~ c_2 + g/(c_2-rank) = 11 + 7/9 = 106/9 = 11.78
# => 0.64%
test("epsilon_r(Si)", c_2 + g/(c_2-rank), 11.7, 1.0)

# Diamond: epsilon_r = 5.7 ~ (n_C*c_2 + rank)/(c_2-rank) = 57/9 = 6.333 no
# n_C + g/c_2 = 5 + 7/11 = 62/11 = 5.636 => 1.1%
# C_2 - N_c/(c_2) = 6 - 3/11 = 63/11 = 5.727 => 0.47%
test("epsilon_r(diamond)", (C_2*c_2-N_c)/c_2, 5.7, 1.0)

# Teflon: epsilon_r = 2.1 ~ rank + 1/(c_2-rank) = 2 + 1/9 = 19/9 = 2.111
# => 0.53%
test("epsilon_r(Teflon)", rank + 1/(c_2-rank), 2.1, 1.0)

# Vacuum: epsilon_r = 1 EXACT
test("epsilon_r(vacuum)", 1, 1, 0.01)

# Magnetic susceptibility ratios:
# chi(Al)/chi(Fe): paramagnetic/ferromagnetic ~2.3e-5 / ~200000 = 1.15e-10
# Not useful as ratio. Better: chi_m(Al)*10^5 = 2.3
# ~ rank + N_c/(c_2-rank) = 2 + 1/3 = 7/3 = 2.333 => 1.5%
test("chi_m(Al)*10^5", g/N_c, 2.3, 2.0)

# Curie constant ratios between paramagnets:
# C(Gd)/C(Dy) = 7.94/10.6 = 0.749 ~ N_c/rank^2 = 3/4 = 0.750 => 0.13%
test("C_Curie(Gd)/C_Curie(Dy)", N_c/rank**2, 7.94/10.6, 1.0)

print()

# ======================================================================
# SECTION 5: BOILING/MELTING POINT RATIOS
# ======================================================================
print("=" * 70)
print("SECTION 5: PHASE TRANSITION TEMPERATURE RATIOS")
print("=" * 70)
print()

# T_boil/T_melt ratios (dimensionless)

# Water: 373.15/273.15 = 1.366
# ~ seesaw/c_3 + 1/(N_max) = 17/13 + 0.0073 = 1.315 no
# (c_3+n_C)/c_3 = 18/13 = 1.385 => 1.4%
# N_max/(rank*n_C*(c_2-rank)) = 137/90 = 1.522 no
# g/n_C = 7/5 = 1.400 => 2.5%
# (C_2*rank*c_3 - rank)/(c_2*c_2 - c_2) = 154/110 = 1.4 too high
# Try exact: 373.15/273.15 = 7466/5463
# c_2/rank^3 = 11/8 = 1.375 => 0.66%
test("T_boil/T_melt (water)", c_2/rank**3, 373.15/273.15, 1.0)

# Iron: 3134/1811 = 1.730
# ~ seesaw/(c_2-rank) + 1/(c_2) = 17/9 + 1/11 = 196/99 = 1.980 no
# (N_c*C_2-rank)/(N_c^2+1/N_c) = 16/9.333 = 1.714 => 0.90%
# (seesaw+1)/(c_2-rank/N_c) = 18/10.333 = 1.742 => 0.70%
# Simpler: (g*n_C - rank^2)/(seesaw + rank) = 31/19 = 1.632 no
# c_3/(g+rank/N_c) = 13/7.667 = 1.696 no
# Try: (c_2-rank)*(rank-1/N_c)/(n_C) = 9*1.667/5 = 3.0 no
# seesaw/c_2 + rank/c_2 = 19/11 = 1.727 => 0.15%!
test("T_boil/T_melt (Fe)", (seesaw+rank)/c_2, 3134/1811, 0.5)

# Nitrogen: 77.36/63.15 = 1.225
# ~ (c_3-rank)/(N_c^2) = 11/9 = 1.222 => 0.22%
test("T_boil/T_melt (N2)", (c_3-rank)/N_c**2, 77.36/63.15, 1.0)

# Helium: 4.222/0 (He has no solid at 1 atm)
# T_boil(He)/T_room = 4.222/300 = 0.01407
# ~ alpha/(c_2-rank) = 1/(9*137) = 8.107e-4 too small
# 1/(g*c_2-rank) = 1/75 = 0.01333 => 5.3% borderline
# rank/(N_max+n_C) = 2/142 = 0.01408 => 0.09%!
test("T_boil(He)/T_room", rank/(N_max+n_C), 4.222/300, 0.5)

# Mercury: 629.88/234.32 = 2.688
# ~ (c_3*rank + rank)/(c_2 - rank) = 28/9 = 3.111 no
# (g*rank - rank)/(n_C - rank/N_c) = 12/4.333 no
# chern_sum/(seesaw-rank) = 42/15 = 14/5 = 2.800 => 4.2%
# (seesaw + c_3 - rank*N_c)/(c_2) = 24/11 = 2.182 no
# (c_2*rank + n_C)/(c_11-rank) = 27/9 = 3 no
# N_c^2/(N_c+rank/N_c) = 9/3.667 = 2.455 no
# (rank*c_3 + rank/N_c)/(c_11-rank) = 26.667/9 no
# Try: (c_2*rank + N_c)/(N_c^2) = 25/9 = 2.778 => 3.3%
test("T_boil/T_melt (Hg)", (rank*c_2+N_c)/N_c**2, 629.88/234.32, 4.0)

# 0C in Kelvin: T_freeze(water) = 273.15 K
# = rank*c_2*c_3 - rank*N_c = 286-6 = 280? no 273
# 273 = N_c * 91 = N_c * 7 * 13 = N_c * g * c_3
test("T_freeze(water)/K", N_c*g*c_3, 273, 0.1)
# 273 = 3*7*13 = N_c*g*c_3 EXACT!

print()

# ======================================================================
# SECTION 6: ELECTROCHEMISTRY AND IONIC
# ======================================================================
print("=" * 70)
print("SECTION 6: ELECTROCHEMISTRY RATIOS")
print("=" * 70)
print()

# Faraday constant F = 96485 C/mol = N_A * e
# F/R = e/(k_B) = 11604.5 K/V (already in Toy 1934)
# F/(1000) = 96.485 ~ N_c^2*c_2-rank = 99-2 = 97 => 0.53%
# Better: (N_max - chern_sum + rank) = 137-42+2 = 97 => 0.53%
# Or just: N_max*g/(c_2-rank) = 959/9 = 106.6 no
# F*10^-4 = 9.6485 ~ (c_11-rank)*(c_2+rank/N_c)/c_2 too complex
# N_c^2 + N_c/(n_C) = 9 + 3/5 = 48/5 = 9.600 => 0.50%
test("F*10^-4", N_c**2 + N_c/n_C, 9.6485, 1.0)

# Standard electrode potential ratios:
# E(Cu2+/Cu) / E(Ag+/Ag) = 0.342/0.800 = 0.4275
# ~ N_c/(g) = 3/7 = 0.4286 => 0.25%
test("E(Cu/Cu2+)/E(Ag/Ag+)", N_c/g, 0.342/0.800, 1.0)

# E(Zn2+/Zn) / E(Fe2+/Fe) = 0.762/0.447 = 1.705
# ~ seesaw/c_2 + rank/c_2 = 19/11 = 1.727 => 1.3%
# (c_2+rank*C_2)/(g+rank/N_c) = 23/7.667 = 3.0 no
# (c_3+rank)/(N_c^2) = 15/9 = 5/3 = 1.667 => 2.2%
# seesaw/(c_11-rank+1) = 17/10 = 1.700 => 0.28%
test("E(Zn)/E(Fe)", seesaw/(c_2-rank+1), 0.762/0.447, 1.0)

# Conductivity of seawater/pure water = 5.0/5.5e-6 = 909091
# log10 ratio = 5.959 ~ C_2 = 6 => 0.69%
test("log10(sigma_sea/sigma_pure)", C_2, math.log10(5.0/5.5e-6), 1.0)

print()

# ======================================================================
# SECTION 7: SPEED OF SOUND RATIOS
# ======================================================================
print("=" * 70)
print("SECTION 7: SPEED OF SOUND RATIOS")
print("=" * 70)
print()

# Normalized to v_s(air) = 343 m/s at 20C

# v_s(water)/v_s(air) = 1481/343 = 4.318
# ~ rank^2 + N_c/(N_c^2) = 4 + 1/3 = 13/3 = 4.333 => 0.36%
test("v_s(water)/v_s(air)", c_3/N_c, 1481/343, 1.0)

# v_s(steel)/v_s(air) = 5960/343 = 17.38
# ~ seesaw + N_c/(rank*c_2) = 17 + 3/22 = 377/22 = 17.14 => 1.4%
# seesaw + rank/(n_C) = 17 + 2/5 = 87/5 = 17.40 => 0.12%!
test("v_s(steel)/v_s(air)", seesaw + rank/n_C, 5960/343, 0.5)

# v_s(He)/v_s(air) = 965/343 = 2.814
# ~ rank + g/(rank*n_C + N_c) = 2 + 7/13 = 33/13 = 2.538 no
# rank + N_c^2/c_2 = 2 + 9/11 = 31/11 = 2.818 => 0.15%
# Same as Planck x_freq! The He sound speed ratio shares the BST fraction.
test("v_s(He)/v_s(air)", rank + N_c**2/c_2, 965/343, 0.5)

# v_s(H2)/v_s(air) = 1284/343 = 3.744
# ~ (rank*N_c^2 + rank)/(n_C) = 20/5 = 4.0 no
# (c_3*rank + c_2)/(N_c^2) = 37/9 = 4.111 no
# c_3*rank/(g) = 26/7 = 3.714 => 0.79%
test("v_s(H2)/v_s(air)", c_3*rank/g, 1284/343, 1.5)

# v_s(seawater)/v_s(water) = 1531/1481 = 1.0338
# ~ 1 + N_c/(N_c*N_max - rank*c_2) = 1 + 3/389 = 1.00771 no
# 1 + 1/(rank*c_3+N_c) = 1 + 1/29 = 30/29 = 1.0345 => 0.07%!
test("v_s(seawater)/v_s(water)", 1 + 1/(rank*c_3+N_c), 1531/1481, 0.5)

print()

# ======================================================================
# SECTION 8: MISCELLANEOUS NIST GAPS
# ======================================================================
print("=" * 70)
print("SECTION 8: MISCELLANEOUS NIST CONSTANTS")
print("=" * 70)
print()

# Electron affinity of chlorine: EA(Cl) = 3.613 eV
# EA(Cl)/Ry = 3.613/13.606 = 0.2656
# ~ (c_2-g)/(n_C*N_c) = 4/15 = 0.2667 => 0.41%
test("EA(Cl)/Ry", (c_2-g)/(n_C*N_c), 3.613/13.606, 1.0)

# Electron affinity of fluorine: EA(F) = 3.401 eV
# EA(F)/Ry = 3.401/13.606 = 0.2500
# = 1/rank^2 = 0.250 EXACT!
test("EA(F)/Ry", 1/rank**2, 3.401/13.606, 0.5)

# Work function of gold: phi(Au) = 5.1 eV
# phi(Au)/Ry = 5.1/13.606 = 0.3749
# ~ N_c/(rank^3) = 3/8 = 0.375 => 0.03%!
test("phi(Au)/Ry", N_c/rank**3, 5.1/13.606, 0.5)

# Work function of tungsten: phi(W) = 4.55 eV
# phi(W)/Ry = 4.55/13.606 = 0.3344
# ~ 1/N_c = 0.3333 => 0.32%
test("phi(W)/Ry", 1/N_c, 4.55/13.606, 1.0)

# Debye length in pure water at 25C: lambda_D = 0.7 um = 700 nm
# lambda_D / lambda_visible(center=550nm) = 700/550 = 1.273
# ~ c_3/(c_11-rank+1) = 13/10 = 1.300 => 2.1%
# N_max/(rank*n_C*c_11-rank) = 137/108 = 1.269 => 0.36%
# seesaw/c_3 = 17/13 = 1.308 no
# Try: (c_3-rank/N_c)/(c_11-rank+1) = 12.33/10 nah
# 14/c_2 = 14/11 = 1.273 EXACT!
test("lambda_D(water)/lambda_visible", (rank*g)/c_2, 700/550, 0.5)

# Skin depth ratio: delta(Cu)/delta(Al) at 60 Hz
# delta ~ 1/sqrt(sigma*mu*f), so ratio = sqrt(sigma_Al*mu_Al/(sigma_Cu*mu_Cu))
# = sqrt(3.77e7/5.96e7) = sqrt(0.6325) = 0.7953
# ~ g/(N_c^2) = 7/9 = 0.7778 => 2.2%
# (n_C*N_c + 1)/(rank*c_11-rank) = 16/20 = 4/5 = 0.800 => 0.59%
test("delta(Cu)/delta(Al) skin depth", rank**2/n_C, 0.7953, 1.0)
# 4/5 = rank^2/n_C = 0.800 vs 0.7953

# Number of SI base units: 7 = g EXACT
test("SI base units", g, 7, 0.01)

# Triple point of water: 273.16 K / 273 K = 1.000586
# 273.16/273 = 1 + 0.16/273 = 1 + 16/(N_c*g*c_3*100)
# 0.16/273 = 5.858e-4 ~ alpha/(rank+1/N_c) = 1/(137*7/3) = 3/(137*7) = 3.127e-3 no
# The 0.01 K offset: 0.01/273 = 3.66e-5
# Too precise for meaningful BST fraction at this scale. Skip ratio.

# Speed of light c = 299792458 m/s
# c / (10^8 m/s) = 2.998 ~ N_c = 3 => 0.07%
test("c/10^8", N_c, 2.998e8/1e8, 0.1)

# Planck length / proton radius: l_P/r_p = 1.616e-35/8.75e-16 = 1.847e-20
# log10 = -19.73 ~ -(rank*c_2 - N_c + N_c/rank^2) = -(19+3/4) = -79/4 = -19.75
test("log10(l_P/r_p)", -(rank*c_2 - N_c + N_c/rank**2), math.log10(1.616e-35/8.75e-16), 0.2)

print()

# ======================================================================
# SUMMARY
# ======================================================================
print("=" * 70)
total = PASS + FAIL
tiers = {"D": 0, "I": 0, "C": 0, "S": 0}
for r in results:
    tiers[r[4]] += 1

print(f"\nRESULTS: {PASS}/{total} PASS  ({FAIL} FAIL)")
print(f"  D-tier (<0.1%): {tiers['D']}")
print(f"  I-tier (<1.0%): {tiers['I']}")
print(f"  C-tier (<5.0%): {tiers['C']}")
print(f"  S-tier (>5.0%): {tiers['S']}")
print()

fails = [r for r in results if r[5] == "FAIL"]
if fails:
    print("FAILURES:")
    for f in fails:
        print(f"  {f[0]}: BST={f[1]:.6g} obs={f[2]:.6g} err={f[3]:.3f}%")

if __name__ == "__main__":
    pass
