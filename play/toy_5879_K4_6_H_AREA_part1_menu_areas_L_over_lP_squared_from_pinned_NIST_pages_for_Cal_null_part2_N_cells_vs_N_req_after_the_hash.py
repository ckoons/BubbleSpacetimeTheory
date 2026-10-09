#!/usr/bin/env python3
"""
Toy 5879 — Round K4-6, Lane B item 2: H-AREA (Elie, 2026-10-09). Prereg: Keeper K1958 (Sections 1–3, 5–7 read; Section 4 not).
  --part1 (BEFORE Cal's hash): the menu areas (L/ℓ_P)² for rows 1–11, every length read from a pinned file (Grace band K NIST
          pages, the ledger rows she confirmed, Wild's 1420.4 MHz, NIST Lyα), reduced/un-reduced Compton both printed and
          flagged (Grace 14.2: (2π)² = 1.6 decades). The span S and count n of rows 1–10 are printed for Cal's P₀. NO N_cells.
  --part2 (AFTER Cal's hash only): N_cells = Σ_class N_census,class × (A_class/ℓ_P²) from the FROZEN 5877 census vs N_req.
"""
import sys, os, re, html, json, math

here = os.path.dirname(os.path.abspath(__file__))
K = os.path.join(here, '..', 'data', 'sources_grace_2026-10-09', 'bandK')
def nist(fname):
    t = open(os.path.join(K, fname), errors='ignore').read()
    t = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
    m = re.search(r'Numerical value ([\d. ]+?)(?: x 10 (-?\d+))? ?m Standard', t)      # NIST renders "x 10 -35 m"
    assert m, fname
    v = float(m.group(1).replace(' ', '')); e = int(m.group(2)) if m.group(2) else 0
    return v * 10 ** e
lP = nist('nist_codata2022_Value_plkl.html')                 # m
a0 = nist('nist_codata2022_Value_bohrrada0.html')            # m
lam_e = nist('nist_codata2022_Value_ecomwl.html')            # h/(m_e c), un-reduced
lambar_e = nist('nist_codata2022_Value_ecomwlbar.html')      # ħ/(m_e c), reduced
lam_p = nist('nist_codata2022_Value_pcomwl.html')            # h/(m_p c), un-reduced
r_p = 0.84075e-15                                            # const_045 observed, CODATA 2022 (NIST pinned 09-29)
r_e = 2.8179e-15                                             # const_111 observed, CODATA 2022
R_inf = 10973731.569                                         # const_129 observed, m^-1
nu21 = 1420.4e6                                              # Wild 1952 Table 2 (band G), Hz
lam_Lya = 1215.6699e-10                                      # NIST ASD (band G), m
c = 299792458.0
print(f"pins read from files: ℓ_P = {lP:.6e} m, a₀ = {a0:.6e}, λ_e = {lam_e:.6e} (h/mc), ƛ_e = {lambar_e:.6e} (ħ/mc), λ_p = {lam_p:.6e} (h/m_p c)")
assert abs(lam_e / lambar_e - 2 * math.pi) < 1e-6 and abs(a0 / lambar_e * (1 / 137.035999177) - 1) < 1e-6 and abs(r_e / lambar_e * 137.035999177 - 1) < 2e-4

rows = []   # (row, label, length_m, class, flag)
rows.append((1, "proton charge radius r_p", r_p, "M-recoil: 21-cm, Lyα, LyC", "const_045"))
rows.append((2, "proton Compton ƛ_p = ħ/(m_p c) [REDUCED]", lam_p / (2 * math.pi), "M-recoil variant", "NIST h/(m_p c) ÷ 2π; un-reduced = (2π)² larger"))
rows.append((2.5, "   (un-reduced λ_p = h/(m_p c), for the flag)", lam_p, "—", "NOT in the menu count"))
for A in (12, 28, 56):
    rows.append((3, f"nuclear radius 1.2 A^(1/3) fm, A = {A}", 1.2e-15 * A ** (1 / 3), "M-recoil, binder fork B1: dust", "r₀ = 1.2 fm is a FIT (Grace 14.2)"))
for a in (0.01e-6, 0.1e-6, 1e-6):
    rows.append((4, f"grain radius {a*1e6:g} μm (MRN)", a, "M-recoil, binder fork B2: dust", "MRN 1977 (band K)"))
rows.append((5, "λ = 21 cm (c/1420.4 MHz)", c / nu21, "M-mode: 21-cm", "Wild 1952"))
rows.append((6, "λ Lyα = 121.567 nm", lam_Lya, "M-mode: Lyα", "NIST ASD"))
rows.append((6, "λ LyC = 1/R_∞ = 91.127 nm", 1 / R_inf, "M-mode: LyC", "const_129"))
for lam in (0.4e-6, 0.6e-6, 1.2e-6):
    rows.append((7, f"λ_abs = {lam*1e6:g} μm", lam, "M-mode: dust", "5877 E_abs fork"))
rows.append((8, "Bohr radius a₀", a0, "M-writer: all", "const_030 / NIST"))
rows.append((9, "electron Compton ƛ_e = ħ/(m_e c) [REDUCED]", lambar_e, "M-writer: all", "NIST ecomwlbar; un-reduced λ_e = (2π)² larger (1.6 dec)"))
rows.append((9.5, "   (un-reduced λ_e = h/(m_e c), for the flag)", lam_e, "—", "NOT in the menu count"))
rows.append((10, "classical electron radius r_e = α ƛ_e", r_e, "M-writer: all", "const_111"))
rows.append((11, "ℓ_P (one cell: the null, T3 as run)", lP, "all", "NIST plkl"))

print(f"\n{'row':>4} {'length':<48} {'L [m]':>12} {'(L/ℓ_P)²':>12} {'log10':>7}  class / flag")
areas = {}
for r, lab, L, cls, flag in rows:
    A = (L / lP) ** 2; areas[lab] = A
    print(f"{str(r):>4} {lab:<48} {L:12.4e} {A:12.3e} {math.log10(A):7.2f}  {cls} | {flag}")
menu = {lab: (L / lP) ** 2 for (r, lab, L, cls, flag) in rows if r not in (2.5, 9.5, 11)}   # (first run reused a stale loop variable; owned)
logs = sorted(math.log10(v) for v in menu.values())
S = logs[-1] - logs[0]; n = len(set(round(x, 2) for x in logs))
print(f"\n  menu rows 1–10: n = {n} distinct area values (every fork counted), span S = {S:.2f} decades (log10 from {logs[0]:.2f} to {logs[-1]:.2f}); Keeper's form P₀ = min(1, 2n/S) = {min(1, 2 * n / S):.2f} — CAL sets the numbers, this is the arithmetic of his form")
rec = {"lP": lP, "areas_in_cells": {lab: A for lab, A in areas.items()}, "menu_n": n, "menu_span_decades": S, "N_cells": None}
json.dump(rec, open(os.path.join(here, '.record_5879_menu.json'), 'w'), indent=1)
print("  written .record_5879_menu.json; N_cells NOT computed; the census file is not opened in part 1.")

if "--part2" in sys.argv:
    exec(open(os.path.join(here, ".k4_6_part2_5879.py")).read())
