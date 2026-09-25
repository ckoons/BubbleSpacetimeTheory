#!/usr/bin/env python3
"""
Toy 5795 — the dark-mode mass map + coldness (Elie, 2026-09-25; round 4 item 3, Lyra clump note Section 5).

MASSES (Lyra, clump note + ledgers note, 09-25): m_p/N_c = 0.313 GeV (selected, Delta = 0),
  (16/9) m_p = 1.67 GeV, (16/3) m_p = 5.00 GeV (= Lyra's ceiling).
PINS:
  m_p = 938.27208943 MeV, eV-kg 1.782661921e-36, G, hbar, c, k_B, Planck mass 2.176434e-8 kg:
      CODATA 2022, data/sources_elie_2026-09-25/nist_codata_allascii.txt
  Windows (Grace R162 Section 6): Windchime target = reduced Planck mass "~4 ug"; Carney+ gravitational
      detection needs m >~ m_Pl; asteroid window 1e17-1e23 g (Carr+2021); HSC 1e-11..1e-6 M_sun;
      EROS-2 0.6e-7..15 M_sun; OGLE 1.3e-5..860 M_sun.
  Lyman-alpha (R162 Section 5): thermal-relic-equivalent m_WDM > 5.7 keV (Irsic+2024, 95%);
      alternatives 5.3 / 4.1 / 3.1 keV run too.
  omega_c = 0.1200 (Planck 2018, 1807.06209 l.3258).
FLAGGED, NOT PINNED (each shown not to move a verdict): M_sun = 1.989e33 g (only converts window edges;
  a factor 10 either way leaves >= 30 orders of margin); T_CMB = 2.7255 K; parsec from the IAU exact
  au (149597870700 m) and pc = au*648000/pi; g*s(today) = 3.91, g*s(T_c) scanned 10.75..106.75;
  relic statistics: fermion, g = 2 internal states, Fermi-Dirac <p> = (7 pi^4 / (180 zeta3)) T.

COLDNESS MODEL (stated before numbers): the dark mode never thermalises (gravity-only). It is born at
  T_c with mean momentum p_b = x * 3.151 T_c (x = 1: thermal-size, Lyra's default). Afterwards p ∝ 1/a,
  entropy conservation gives a_c = (T0/T_c)(g*s0/g*s(T_c))^(1/3), so today
    <p0> = x * 3.151 * T0 * (g*s0/g*s(T_c))^(1/3)      — T_c itself DROPS OUT, only g*s(T_c) remains.
  The equivalent thermal relic of mass m_th that is ALL the dark matter has T_x0 fixed by
    rho_DM = m_th * (3 zeta3 / (2 pi^2)) * 2/2 ... (fermion, g=2: n = 3 zeta3 g T^3 /(4 pi^2))
  and <p_th0> = 3.151 T_x0. Same present velocity  <=>  same free streaming (both redshift as 1/a after
  birth; the dark mode is non-relativistic earlier or later only through <p0>/m).
  Lyman-alpha kills the dark mode iff <p0>/m > <p_th0>/m_th at m_th = 5.7 keV.

DIRECTION BEFORE NUMBERS:
  P1 all three masses lie below EVERY pinned window by more than 20 orders of magnitude (cosmology only).
  P2 with thermal-size birth momentum (x = 1) all three are colder than the 5.7 keV bound for EVERY
     g*s(T_c) in 10.75..106.75 -> Lyman-alpha cannot kill the thermal-birth reading at any T_c.
  P3 the killing parameter is x: the maximum allowed x (birth momentum in units of thermal) is > 100
     for m = 0.313 GeV — i.e. only a strongly non-thermal (e.g. decay-kicked) birth is killable.
  P4 (control) a 5.7 keV thermal relic run through the same code has velocity ratio exactly 1.
"""
from math import pi, log10
from fractions import Fraction

zeta3 = 1.2020569031595942
MeV_p = 938.27208943
eV_kg = 1.782661921e-36
G = 6.67430e-11; hbar = 1.054571817e-34; c = 299792458.0; kB = 1.380649e-23; eV = 1.602176634e-19
mPl_kg = 2.176434e-8
Msun_g = 1.989e33                     # FLAGGED
T0K = 2.7255                          # FLAGGED
au = 149597870700.0; pc = au*648000/pi; Mpc = 1e6*pc   # FLAGGED (IAU exact definitions)
omega_c = 0.1200
gs0 = 3.91                            # FLAGGED

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

m_p_GeV = MeV_p/1000
masses = {"m_p/3 (selected)": m_p_GeV/3, "16/9 m_p": 16/9*m_p_GeV, "16/3 m_p (ceiling)": 16/3*m_p_GeV}
def GeV_to_g(m):
    return m*1e9*eV_kg*1e3

print("Toy 5795 — dark-mode mass map + coldness\n")
print("DIRECTION: P1 >20 orders below every window; P2 thermal-birth never killed by Ly-a; P3 x_max > 100 at 0.313 GeV; P4 control = 1\n")

mPl_red_g = mPl_kg*1e3/(8*pi)**0.5
windows = {
    "Windchime target (reduced Planck mass)": (mPl_red_g, mPl_red_g),
    "Carney+ grav. detection (>~ m_Pl)": (mPl_kg*1e3, float('inf')),
    "asteroid window (Carr+2021)": (1e17, 1e23),
    "HSC M31": (1e-11*Msun_g, 1e-6*Msun_g),
    "EROS-2": (0.6e-7*Msun_g, 15*Msun_g),
    "OGLE (f<10%)": (1.3e-5*Msun_g, 860*Msun_g),
}
print("(1) mass map (grams, log10)")
for k, (lo, hi) in windows.items():
    print(f"   {k:40s} [{log10(lo):6.1f}, {'inf' if hi == float('inf') else f'{log10(hi):6.1f}'}]")
gaps = []
for name, m in masses.items():
    mg = GeV_to_g(m)
    gap = min(log10(lo) - log10(mg) for lo, _ in windows.values())
    gaps.append(gap)
    print(f"   {name:22s} m = {m:.4f} GeV = {mg:.3e} g  ->  {gap:.1f} orders below the lightest window")
check("P1 every mass > 20 orders below every pinned window (cosmology-only bin)", min(gaps) > 20)
check("M_sun flag: a factor-10 error moves no window edge within 20 orders of the masses",
      min(gaps) - 1 > 20)

print("\n(2) coldness")
# rho_DM today in kg/m^3
H100 = 100e3/Mpc
rho_c100 = 3*H100**2/(8*pi*G)
rho_DM = omega_c*rho_c100
def Tx0_eV(m_th_eV):
    # n = rho/m ; n = (3 zeta3 g /(4 pi^2)) (kT/(hbar c))^3 , g = 2
    n = rho_DM/(m_th_eV*eV_kg)
    kT = (n/(3*zeta3*2/(4*pi**2)))**(1/3)*hbar*c      # J
    return kT/eV
pfac = 7*pi**4/(180*zeta3)
T0_eV = kB*T0K/eV
def v_relic(m_th_eV):
    return pfac*Tx0_eV(m_th_eV)/m_th_eV
def v_mode(m_GeV, x, gsc):
    return x*pfac*T0_eV*(gs0/gsc)**(1/3)/(m_GeV*1e9)
print(f"   rho_DM = {rho_DM:.3e} kg/m^3 ; T0 = {T0_eV:.4e} eV ; FD <p>/T = {pfac:.4f}")
for mth in (5.7e3, 5.3e3, 4.1e3, 3.1e3):
    print(f"   thermal relic m_th = {mth/1e3:.1f} keV: T_x0 = {Tx0_eV(mth):.3e} eV (T_x0/T0 = {Tx0_eV(mth)/T0_eV:.3f}), v0 = {v_relic(mth):.3e} c")
check("P4 control: velocity ratio of a 5.7 keV relic to itself = 1",
      abs(v_relic(5.7e3)/v_relic(5.7e3) - 1) < 1e-15, can_fail=False)
vb = v_relic(5.7e3)
ok2 = True
print("   dark mode, x = 1 (thermal-size birth):")
for name, m in masses.items():
    for gsc in (10.75, 61.75, 106.75):
        r = v_mode(m, 1, gsc)/vb
        ok2 &= r < 1
        print(f"     {name:22s} g*s(T_c) = {gsc:6.2f}: v0 = {v_mode(m, 1, gsc):.3e} c, ratio to 5.7 keV bound = {r:.2e}")
check("P2 thermal-size birth is colder than the 5.7 keV bound for all masses and all g*s(T_c)", ok2)
print("   maximum birth-momentum factor x_max (Ly-a 5.7 keV edge), g*s(T_c) = 10.75 (most conservative):")
xm = {}
for name, m in masses.items():
    xm[name] = vb/v_mode(m, 1, 10.75)
    print(f"     {name:22s} x_max = {xm[name]:.3e}   (birth <p> up to {xm[name]*pfac:.2e} T_c)")
check("P3 x_max > 100 at m = 0.313 GeV", xm["m_p/3 (selected)"] > 100)
print("   Reading: T_c drops out; only a birth momentum ~x_max times thermal is killable. A decay-born mode with")
print("   p_b ~ m would need T_c < m/x_max to be dangerous — this is where Lyra's commit mechanism must say p_b.")

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
