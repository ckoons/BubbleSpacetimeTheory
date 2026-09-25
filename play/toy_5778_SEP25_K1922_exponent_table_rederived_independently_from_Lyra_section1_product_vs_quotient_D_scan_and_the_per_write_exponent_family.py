#!/usr/bin/env python3
"""
Toy 5778 — K1922's exponent table, re-derived independently (Elie, 2026-09-25).

Source of inputs: Lyra, FILLING_LAW 2026-09-22, Section 1 ONLY. Keeper's script
(play/keeper_K1922_three_writes_exponent_check.py) was NOT opened before this ran.

Input list (stated first, so a difference with Keeper's is visible):
  I1  rho_DE = E_commit * N / V_H                         (Lyra S1 / S3(iv))
  I2  E_commit = k_B T ln2, T = hbar H / 2pi  -> E ∝ H    (Gibbons-Hawking; H-power is D-independent)
  I3  V_H ∝ H^-D  (Hubble ball in D spatial dimensions)
  I4  Friedmann: H^2 ∝ rho_total (power holds in any D; only the coefficient changes)
  I5  matter dilutes as a^-D, radiation as a^-(D+1)
  I6  ledger as stated: d ln N1/dt = 2H  ->  N1 ∝ a^2 at D = 3
      Two generalisations of the "2" to D dims (K1922's pair):
        G_area : N1 ∝ a^(D-1)   (the 2 is the horizon's area dimension)
        G_fixed: N1 ∝ a^2       (the 2 held fixed)
  I7  Casey's reading, two ways: PRODUCT  N_D = N1^D (one write per axis)
                                  QUOTIENT N_D = N1 / D (a unit consumes D writes)

Derived requirement: rho_DE ∝ H^(D+1) N; constant in the matter era needs
N ∝ H^-(D+1) ∝ a^(D(D+1)/2).

All arithmetic exact (Fraction). Checks can fail; score printed X/Y.
"""
from fractions import Fraction as F

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

def H_exp(D, era):
    """H ∝ a^x : x = -(matter/radiation dilution exponent)/2."""
    dil = F(D) if era == "matter" else F(D + 1)
    return -dil / 2

def required_N_exp(D, era="matter"):
    # rho_DE ∝ H^(D+1) * N constant  ->  N ∝ H^-(D+1)
    return -(D + 1) * H_exp(D, era)

def N1_exp(D, gen):
    return F(D - 1) if gen == "area" else F(2)

def supplied(D, gen, reading):
    p = N1_exp(D, gen)
    return D * p if reading == "product" else p   # quotient: constant factor 1/D drops out of d ln/dt

def rhoDE_exp(D, gen, reading, era):
    # rho_DE ∝ H^(D+1) * N
    return (D + 1) * H_exp(D, era) + supplied(D, gen, reading)

print("Toy 5778 — K1922 exponent table, independent re-derivation\n")
print("Required matter-era exponent of N (rho_DE constant):")
for D in range(1, 8):
    r = required_N_exp(D)
    print(f"  D={D}: {r}   [D(D+1)/2 = {F(D*(D+1),2)}]")
check("required exponent equals D(D+1)/2 for D=1..7",
      all(required_N_exp(D) == F(D*(D+1), 2) for D in range(1, 8)))
check("required exponent at D=3 is 6 (epsilon = 2 in d ln N/dt = 2H(1+eps))",
      required_N_exp(3) == 6 and F(6, 2) - 1 == 2)

print("\nTable: supplied exponent vs required, D = 1..10")
print("  D | req  | prod/area | prod/fixed | quot/area | quot/fixed")
match = {k: [] for k in ("product-area", "product-fixed", "quotient-area", "quotient-fixed")}
for D in range(1, 11):
    req = required_N_exp(D)
    row = []
    for reading in ("product", "quotient"):
        for gen in ("area", "fixed"):
            s = supplied(D, gen, reading)
            row.append(f"{str(s):>4}{'*' if s == req else ' '}")
            if s == req:
                match[f"{reading}-{gen}"].append(D)
    print(f"  {D:>2}| {str(req):>4} |   {row[0]}   |   {row[1]}    |   {row[2]}   |   {row[3]}")
print("  (* = matches requirement)")
for k, v in match.items():
    print(f"  {k:15s}: matches at D = {v}")

check("PRODUCT under G_area matches only at D = 3 (D=1..10)", match["product-area"] == [3])
check("PRODUCT under G_fixed matches only at D = 3 (D=1..10)", match["product-fixed"] == [3])
check("QUOTIENT matches at no D (either generalisation)",
      match["quotient-area"] == [] and match["quotient-fixed"] == [])
check("control: literal ledger at D=3 (N ∝ a^2) fails the requirement",
      supplied(3, "fixed", "quotient") != required_N_exp(3), can_fail=False)

# Analytic confirmation of 'only at D=3' for all D, not just the scan:
#   G_area : D(D-1) = D(D+1)/2  <=>  D(D-3) = 0
#   G_fixed: 2D     = D(D+1)/2  <=>  D(D-3) = 0
check("both matching conditions reduce to D(D-3)=0 (analytic, all D>=1)",
      all((D*(D-1) == F(D*(D+1), 2)) == (D == 3) and (2*D == F(D*(D+1), 2)) == (D == 3)
          for D in range(1, 200)))

print("\nAdversarial (for Cal's read 2): what 'only at D=3' is a statement about.")
print("  Product reading with per-write exponent p: need D*p = D(D+1)/2  ->  p(D) = (D+1)/2")
for D in range(1, 8):
    p = F(D + 1, 2)
    print(f"    D={D}: p = {p}   (G_area gives {D-1}, G_fixed gives 2)")
check("a product reading matches at EVERY D for p(D)=(D+1)/2; D=3 is where p=2=D-1",
      all(D * F(D + 1, 2) == required_N_exp(D) for D in range(1, 20))
      and [D for D in range(1, 20) if F(D + 1, 2) == 2] == [3]
      and [D for D in range(1, 20) if F(D + 1, 2) == D - 1] == [3])
print("  -> 'only at D=3' is about the two generalisations of the ledger's 2, not the")
print("     product mechanism alone: the mechanism fixes N = N1^D; the ledger's per-write")
print("     exponent must be (D+1)/2, and the ledger's 2 is that value only at D = 3.")

print("\nRadiation era, product reading, D = 3:")
x = rhoDE_exp(3, "area", "product", "radiation")
w = -x / 3 - 1
print(f"  rho_DE ∝ a^{x}  ->  w = {w};  fraction rho_DE/rho_rad ∝ a^{x + 4}")
check("radiation era: rho_DE ∝ a^-2, w = -1/3, fraction grows as a^2",
      x == -2 and w == F(-1, 3) and x + 4 == 2)
xm = rhoDE_exp(3, "area", "product", "matter")
check("matter era, product, D=3: rho_DE ∝ a^0 (w = -1)", xm == 0)

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; 1 control)")
