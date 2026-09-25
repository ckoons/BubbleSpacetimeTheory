#!/usr/bin/env python3
"""Keeper K1922 -- exponent bookkeeping for Casey's 'three writes' reading of the filling law (2026-09-25).

Reads NOTHING from DESI. Prints no w-direction. Checks orders only (exact rationals).

Lyra's filling-law note (2026-09-22) Sections 1 and 3:
  rho_DE = E_commit * N / V_H,  E_commit ~ H,  V_H ~ H^-D  (D spatial dimensions)
  matter era: H^2 ~ a^-D   =>  rho_DE constant needs  N ~ H^-(D+1) ~ a^(D(D+1)/2)
  the ledger as stated: d ln N/dt = 2H  (N ~ a^2)  -- short by exactly a factor 3 at D = 3.

Casey (2026-09-25): 'three commitment writes make a single unit of 3D information; each write is a
single dimension of measurement.'  Two readings of 'make':
  PRODUCT  -- a 3D unit is one choice of write on each axis: N_3D = N_1^D   (the twig spreading in D)
  QUOTIENT -- a 3D unit consumes D writes:                    N_3D = N_1 / D
Two generalizations of the 1D count to D dimensions (the '2' of the ledger):
  G1: N_1 ~ a^(D-1)  (area law in D)
  G2: N_1 ~ a^2      (the 2 held fixed)
"""
from fractions import Fraction as Fr

def required(D):            # exponent of a that makes rho_DE constant in the matter era
    return Fr(D * (D + 1), 2)

def product(D, n1):         # exponent of N_3D = N_1^D
    return D * n1

def quotient(D, n1):        # exponent of N_3D = N_1 / D  (a constant factor does not move an exponent)
    return n1

fails = 0
print("D | required | PRODUCT G1 | PRODUCT G2 | QUOTIENT G1 | QUOTIENT G2")
for D in range(1, 7):
    g1, g2 = Fr(D - 1), Fr(2)
    row = [required(D), product(D, g1), product(D, g2), quotient(D, g1), quotient(D, g2)]
    marks = ["=" if x == row[0] else " " for x in row[1:]]
    print(f"{D} | {row[0]!s:>8} | " + " | ".join(f"{x!s:>9}{m}" for x, m in zip(row[1:], marks)))

# Claims under test
c1 = product(3, Fr(2)) == required(3) == 6                  # the factor three, exactly, at D = 3
c2 = [D for D in range(1, 50) if product(D, Fr(D - 1)) == required(D)] == [3]   # G1: D = 3 only (D >= 1)
c3 = [D for D in range(1, 50) if product(D, Fr(2)) == required(D)] == [3]       # G2: D = 3 only
c4 = all(quotient(D, Fr(2)) != required(D) for D in range(2, 50))               # quotient never supplies it
# radiation era at D = 3: H^2 ~ a^-4, rho_DE ~ H^4 N ~ a^(-8+6) = a^-2
c5 = (-8 + product(3, Fr(2))) == -2
# control: the ledger as stated (N ~ a^2) must FAIL the requirement at D = 3 (Lyra's K1 reproduced)
ctrl = Fr(2) != required(3)

for name, ok in [("C1 product gives exponent 6 = 3 x 2 at D=3", c1),
                 ("C2 G1 matches only at D=3", c2),
                 ("C3 G2 matches only at D=3", c3),
                 ("C4 quotient never supplies the factor", c4),
                 ("C5 radiation era: rho_DE ~ a^-2 (w=-1/3)", c5),
                 ("CONTROL literal ledger fails at D=3", ctrl)]:
    print(("PASS " if ok else "FAIL ") + name)
    fails += (not ok)
print(f"SCORE: {6 - fails}/6")
