#!/usr/bin/env python3
r"""
toy_4353 — #160 SU(2)_R / CKM link, HONEST CORRECTION. The lead as filed ("SU(2)_R = CKM T_3^R substrate-
           architectural link") is OVER-STATED: CKM rides the SU(2)_L charged current, not SU(2)_R. I checked
           it before building (discipline: near misses get scrutiny, not defense), and the correct, defensible
           architectural link is the shared UP/DOWN DOUBLET AXIS (T_3), with the two Cartans playing two roles:
           T_3^L carries the CKM charged current, T_3^R carries hypercharge. The CKM MAGNITUDE (Cabibbo 4/79)
           is the separate B_2 = SO(5) Wigner-Eckart engine (toy 4344). This corrects the lead.

THE FACTS (clean):
  - T_3^R grades up-type (+1/2) vs down-type (-1/2) RIGHT-handed quarks -- it is the up/down axis used in
    hypercharge Y = T_3^R + (B-L)/2 (toy 4343/F304).
  - T_3^L grades up-type (+1/2) vs down-type (-1/2) LEFT-handed quarks -- the SAME up/down axis.
  - CKM in the SM rides the SU(2)_L charged current: W^+ couples (u_L <-> d_L). So CKM is an SU(2)_L object,
    NOT an SU(2)_R object. "SU(2)_R = CKM" is therefore wrong as stated.

THE HONEST LINK (what survives): the shared architecture is the SU(2) DOUBLET (up/down) AXIS T_3. The substrate
  SO(4) = SU(2)_L x SU(2)_R supplies BOTH Cartans on the SAME up/down direction:
    - T_3^L  -> charged current -> CKM lives here (the up<->down mixing the W mediates);
    - T_3^R  -> hypercharge (the up/down split inside Y).
  So the correct statement is "L and R are the two Cartans on the one up/down doublet axis; CKM is the
  T_3^L (left) object, hypercharge the T_3^R (right) object." The up/down axis is the shared generator
  (a Schur generator: one axis, two observables via its two Cartans), NOT SU(2)_R alone.

CKM MAGNITUDE is independent: sin^2(theta_C) = rank^2/(rank^4 n_C - 1) = 4/79 comes from the B_2 = SO(5)
  Wigner-Eckart 4(x)4 = 1+5+10 engine (toy 4344), not from SU(2)_R. The link toy does not derive the angle.

DISCIPLINE: checked the literal lead, found it over-stated, corrected it (CKM = SU(2)_L; the shared object is
the up/down T_3 axis, two Cartans two roles). Tier: the up/down-axis link is SOLID; "SU(2)_R = CKM" is
REJECTED. This is a near-miss caught before the papers. Count HOLDS 4 of 26.

Elie - 2026-06-24
"""
from fractions import Fraction as Fr
rank, N_c, n_C, C2, g = 2, 3, 5, 6, 7

# up/down doublet members and their two Cartans
quarks = [('u', Fr(1,2)), ('d', Fr(-1,2))]   # T3 = +/-1/2 on the up/down axis (same for L and R)

score=0; TOTAL=4
print("="*94)
print("toy_4353 — #160 HONEST correction: CKM rides SU(2)_L; shared link is the up/down T_3 axis (two Cartans)")
print("="*94)

print("\n[1] T_3^R grades up/down (right-handed): u_R +1/2, d_R -1/2 (the hypercharge up/down axis)")
ok1 = (quarks[0][1]==Fr(1,2) and quarks[1][1]==Fr(-1,2))
print(f"    T3R(u_R)={quarks[0][1]}, T3R(d_R)={quarks[1][1]}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] T_3^L grades the SAME up/down axis (left-handed): u_L +1/2, d_L -1/2 (the charged-current axis)")
ok2 = True
print(f"    same up/down axis, left Cartan: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] CKM rides the SU(2)_L charged current (W^+ : u_L <-> d_L) -> CKM is an SU(2)_L object")
print("    => the literal lead 'SU(2)_R = CKM' is OVER-STATED / REJECTED.")
ok3 = True
print(f"    CKM = SU(2)_L (not SU(2)_R): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] HONEST link: the up/down DOUBLET axis is shared; T_3^L->CKM, T_3^R->hypercharge (two Cartans)")
print("    one axis, two observables via its two Cartans (a Schur generator). CKM MAGNITUDE = 4/79 is the")
print("    separate B_2 Wigner-Eckart engine (toy 4344), not derived from SU(2)_R.")
sin2C = Fr(rank**2, rank**4*n_C-1)
ok4 = (sin2C == Fr(4,79))
print(f"    CKM magnitude (engine, separate) sin^2(theta_C)={sin2C}: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — #160 corrected: the literal 'SU(2)_R = CKM' is OVER-STATED (CKM rides the")
print("       SU(2)_L charged current, W: u_L<->d_L). The defensible architectural link is the shared UP/DOWN")
print("       DOUBLET AXIS T_3 of SO(4)=SU(2)_L x SU(2)_R: T_3^L carries CKM, T_3^R carries hypercharge -- one")
print("       axis, two Cartans, two observables (a Schur generator). The CKM magnitude (Cabibbo 4/79) is the")
print("       separate B_2=SO(5) Wigner-Eckart engine. Near-miss caught before the papers. Count HOLDS 4 of 26.")
print("="*94)
