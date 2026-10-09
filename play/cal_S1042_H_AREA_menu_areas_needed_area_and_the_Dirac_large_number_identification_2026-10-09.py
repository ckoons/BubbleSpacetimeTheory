#!/usr/bin/env python3
"""Cal Section 1042 (2026-10-09) — H-AREA: the menu's areas in Planck cells, the area each
census class would NEED (arithmetic on numbers already on the record: K1957 Section 1,
Elie 5877), and the identification of any nuclear-scale landing with the Eddington–Dirac
large-number coincidence. Lengths are CODATA/pinned constants (Grace's ids); the census
numbers are quoted from 5877's printed output (on disk before this file).
This is the HASH instrument: it fixes what a landing would mean before Elie multiplies.
"""
from math import log10, pi, sqrt
# constants (CODATA 2022 values as pinned in the ledger; Grace confirms ids)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
m_e = 9.1093837139e-31; m_p = 1.67262192595e-27; alpha = 1/137.035999177
lP = sqrt(hbar*G/c**3)                       # 1.616e-35 m
lam_e = hbar/(m_e*c); lam_p = hbar/(m_p*c); a0 = lam_e/alpha; r_e = alpha*lam_e
r_p = 0.84075e-15                            # const_045 (0.841 fm)
H0 = 67.4e3/3.0856775814913673e22            # Planck 2018 (as 5877 used); only for the Dirac line
# numbers already on the record (K1957 Section 1; 5877 part 1 & 2 printed lines)
N_req = 2.24e122; N_census = 1.48e83; share = {'dust': 0.75, '21cm': 0.25}
N_Hatoms = 2.054e78                           # 5877: hydrogen atoms in V_H,0

def cells(L): return (L/lP)**2
menu = [
 ("1 r_p (proton charge radius)",           r_p),
 ("2 lambda_p (proton Compton)",            lam_p),
 ("3 nuclear 1.2 A^1/3 fm, A=12",           1.2e-15*12**(1/3)),
 ("3 nuclear 1.2 A^1/3 fm, A=56",           1.2e-15*56**(1/3)),
 ("4 grain 0.01 um",                        1e-8),
 ("4 grain 0.1 um",                         1e-7),
 ("4 grain 1 um",                           1e-6),
 ("5 lambda = 21 cm",                       0.21),
 ("6 Ly-alpha 121.6 nm",                    121.6e-9),
 ("7 lambda_abs 0.6 um",                    0.6e-6),
 ("8 Bohr a0",                              a0),
 ("9 lambda_e (electron Compton)",          lam_e),
 ("10 r_e (classical electron radius)",     r_e),
 ("11 l_P (one cell; T3 as run)",           lP),
]
print("MENU: area per write in Planck cells, log10")
for name, L in menu:
    print(f"   {name:40s} L = {L:9.3e} m   log10(A/lP^2) = {log10(cells(L)):6.2f}")
print("\nNEEDED area per class if that class alone carried N_req (log10 cells):")
need = {}
for k, s in share.items():
    need[k] = N_req/(s*N_census); print(f"   {k:5s}: {log10(need[k]):6.2f}   (L_needed = {sqrt(need[k])*lP:9.3e} m)")
print("\nRows within +/-1 decade of a class's needed area (the 'landings'):")
for name, L in menu:
    for k in share:
        d = log10(cells(L)) - log10(need[k])
        if abs(d) <= 1: print(f"   {name:40s} vs {k:5s}: {d:+.2f} dec")
print("\nMenu span (rows 1-10, log10 cells):", f"{log10(cells(lam_p)):.1f} .. {log10(cells(0.21)):.1f}")
# the null: fraction of the menu's log-range (rows 1-10) within +/-1 decade of the needed band
lo, hi = log10(cells(lam_p)), log10(cells(0.21)); band = (log10(need['dust'])-1, log10(need['21cm'])+1)
p_null = (band[1]-band[0])/(hi-lo)
print(f"null: a log-uniform area on the menu's span lands in the needed +/-1 band with p = {p_null:.2f}")

print("\nTHE DIRAC IDENTIFICATION (arithmetic on the record's numbers):")
R_H = c/H0
print(f"   (R_H / r_p)^2            = 10^{log10((R_H/r_p)**2):.2f}")
print(f"   hydrogen atoms in V_H     = 10^{log10(N_Hatoms):.2f}   -> Eddington-Dirac: (R_H/r_p)^2 / N_atoms = 10^{log10((R_H/r_p)**2/N_Hatoms):.2f}")
print(f"   absorptions per H atom    = N_census/N_atoms = 10^{log10(N_census/N_Hatoms):.2f}")
print(f"   N_req / (N_census * r_p^2/lP^2) = 10^{log10(N_req/(N_census*cells(r_p))):.2f}")
print("   => a landing at the proton area is (R_H/r_p)^2 ~ N_atoms x (absorptions per atom) x O(1):")
print("      the Eddington-Dirac large-number coincidence (flatness + the proton scale), not a ledger mechanism.")
