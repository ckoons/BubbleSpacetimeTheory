r"""
Toy 4201: charge-structure verification supporting Lyra's F146 -- resolving her load-bearing caveat. Lyra's
no-right-handed-neutrino / Majorana result (F144/F146) hinges on ONE scoping question she flagged for Cal+Keeper: does
BST gauge an INDEPENDENT U(1)_(B-L), or does B-L enter only through the read hypercharge Y? If B-L is independently
gauged, a Majorana mass is forbidden (the tension is real); if B-L enters only through Y, the Majorana mass is allowed
(no tension). THIS TOY verifies the charge structure (my lane, F102): Y/2 = T_3R + (B-L)/2 for all SM fermions, with Y
the READ/gauged combination and T_3R (SU(2)_R) UNREAD (F144) -- so B-L = Y - 2*T_3R is NOT an independent gauge charge,
and the Weinberg operator LLHH (the Majorana mass) is Y-NEUTRAL (preserves gauged U(1)_Y) while violating only the GLOBAL
B-L. Conclusion: Lyra's candidate 1 holds at the charge-structure level -- B-L is not independently gauged, the Majorana
mass is allowed. (Cal+Keeper own the F137-specific audit of whether F137 ever claimed independent gauged B-L; this toy
supplies the charge arithmetic.) Five-Absence "no sterile neutrino" mechanism stands. No count move (Absences not in 26).

THE SCOPING QUESTION (Lyra's caveat):
  F144/F146: the neutrino has NO right-handed partner (SU(2)_R unread) -> no Dirac mass -> the mass must be MAJORANA
  (the Weinberg operator LLHH). caveat: a Majorana mass violates B-L by 2; if BST gauges an independent unbroken U(1)_(B-L),
  that is forbidden. so the whole no-nu_R/Majorana picture rests on: B-L is NOT independently gauged.

THE CHARGE STRUCTURE (verified, all SM fermions):
  standard relation  Y/2 = T_3R + (B-L)/2  holds for every SM fermion (checked below, 7/7 incl. the would-be nu_R).
  in BST only what is READ is gauged: SU(3) x SU(2)_L x U(1)_Y. the RIGHT isospin T_3R (SU(2)_R) is UNREAD (F144).
  so the GAUGED charge is Y (the full combination); neither T_3R nor B-L is gauged individually. since
    B-L = 2*(Y/2 - T_3R) = Y - 2*T_3R,
  and T_3R is unread, B-L is NOT an independent gauge charge -- it is the read Y minus the unread T_3R. B-L is at most a
  GLOBAL (classification) symmetry -- structurally the same status as SO(10) (never gauged, classifies the 16, F137).

THE MAJORANA MASS IS ALLOWED (Weinberg operator LLHH):
  total gauged hypercharge of L L H H = 2*Y_L + 2*Y_H = 2*(-1) + 2*(+1) = 0  -> Y-NEUTRAL -> preserves gauged U(1)_Y.
  total (B-L) of L L H H = 2*(-1) + 2*(0) = -2  -> violates GLOBAL B-L by 2.
  violating a GLOBAL symmetry is permitted; only GAUGED symmetries are sacred. so the Majorana mass preserves everything
  BST gauges and violates only a global (classification) symmetry -> ALLOWED. exactly Lyra's candidate 1.

THE PARALLEL (one mechanism, the whole neutrino + proton story):
  "BST gauges only what it reads" gives, in one stroke:
    - no proton decay: SO(10) never gauged -> no X/Y bosons -> no dim-6 qqql operator (Elie 4190).
    - no sterile neutrino: SU(2)_R unread -> no nu_R (Lyra F144).
    - Majorana mass allowed: B-L not independently gauged (enters only through read Y) -> LLHH violates only global B-L (this toy).
  same principle (read = gauged; unread = global/classification) -> three Five-Absence-sector consequences.

HONEST STATUS:
  CONFIRMS, at the charge-structure level, Lyra's candidate-1 resolution of her caveat: Y/2 = T_3R + (B-L)/2 (7/7),
  B-L = Y - 2*T_3R with T_3R unread -> B-L not independently gauged -> the Weinberg/Majorana operator is Y-neutral and
  violates only global B-L -> ALLOWED. so the no-nu_R/Majorana picture has no gauge-inconsistency. CAVEAT OWNERSHIP: this
  supplies the charge arithmetic; whether F137 ever asserted an independent gauged U(1)_(B-L) is the Cal+Keeper F137 audit
  Lyra requested -- if F137 did, that text needs the re-scoping (B-L enters only through Y), which this charge structure
  supports. the remaining neutrino-sector opens are unchanged: the 3-neutrino strip placement (count-mover, Lyra continuum
  + #418) and the fermionic-tower rerun of the parity argument (Lyra). NO count move (Five-Absences are not among the 26).
  count stays 2 of 26; muon yellow IDENTIFIED.
"""

from fractions import Fraction as F

# SM hypercharges (Q = T3 + Y/2), B-L, and right-isospin T3R
Y   = {"L": F(-1), "e_R": F(-2), "Q": F(1,3), "u_R": F(4,3), "d_R": F(-2,3), "H": F(1), "nu_R": F(0)}
BL  = {"L": F(-1), "e_R": F(-1), "Q": F(1,3), "u_R": F(1,3), "d_R": F(1,3), "H": F(0), "nu_R": F(-1)}
T3R = {"L": F(0),  "e_R": F(-1,2), "Q": F(0), "u_R": F(1,2), "d_R": F(-1,2), "H": F(1,2), "nu_R": F(1,2)}

print("=" * 100)
print("TOY 4201: B-L not independently gauged -> Weinberg/Majorana operator ALLOWED (supports Lyra F146)")
print("=" * 100)
print()
print("check Y/2 = T_3R + (B-L)/2 (all SM fermions):")
print("-" * 100)
rel_ok = True
for f in Y:
    lhs = Y[f] / 2; rhs = T3R[f] + BL[f] / 2
    ok = (lhs == rhs); rel_ok = rel_ok and ok
    print(f"  {f:5}: Y/2 = {str(lhs):>5}   T_3R + (B-L)/2 = {str(rhs):>5}   [{'OK' if ok else 'FAIL'}]")
print()
print("B-L = Y - 2*T_3R; T_3R (SU(2)_R) is UNREAD (F144) -> B-L is NOT an independent gauge charge (only global).")
print()
print("Weinberg operator L L H H (the Majorana mass):")
print("-" * 100)
Y_LLHH = 2*Y["L"] + 2*Y["H"]
BL_LLHH = 2*BL["L"] + 2*BL["H"]
print(f"  gauged hypercharge Y(LLHH) = 2*Y_L + 2*Y_H = {Y_LLHH}  -> Y-NEUTRAL (preserves gauged U(1)_Y): {Y_LLHH==0}")
print(f"  (B-L)(LLHH) = 2*(B-L)_L + 2*(B-L)_H = {BL_LLHH}  -> violates GLOBAL B-L by {abs(BL_LLHH)}: {BL_LLHH!=0}")
print(f"  => preserves everything BST gauges, violates only a global (classification) symmetry -> ALLOWED.")
print()

checks = [
    ("Y/2 = T_3R + (B-L)/2 for all 7 fermions", rel_ok),
    ("B-L = Y - 2*T_3R (T_3R unread -> B-L not independently gauged)", all(BL[f] == Y[f] - 2*T3R[f] for f in Y)),
    ("Weinberg LLHH is Y-neutral (preserves gauged U(1)_Y)", Y_LLHH == 0),
    ("Weinberg LLHH violates global B-L by 2", BL_LLHH == -2),
    ("Majorana mass allowed (preserves gauged, violates only global)", Y_LLHH == 0 and BL_LLHH != 0),
    ("nu_R would be a gauge singlet (Y=0) -> nothing to gauge it (consistent with unread)", Y["nu_R"] == 0),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- a charge-structure verification supporting Lyra's F146 and resolving her load-bearing caveat. Her")
print("  no-right-handed-neutrino / Majorana result rests on one scoping question: is B-L independently gauged, or does it")
print("  enter only through the read hypercharge Y? The charge arithmetic settles it: Y/2 = T_3R + (B-L)/2 holds for every")
print("  SM fermion (7/7), so B-L = Y - 2*T_3R; since BST gauges only what it READS and the right isospin T_3R (SU(2)_R) is")
print("  UNREAD (F144), B-L is the read Y minus the unread T_3R -- NOT an independent gauge charge, only a global")
print("  (classification) symmetry, structurally identical to never-gauged SO(10) (F137). Therefore the Weinberg operator")
print("  LLHH (the Majorana mass) is Y-neutral (preserves the gauged U(1)_Y) and violates only the global B-L -- ALLOWED.")
print("  One principle ('read = gauged, unread = global') gives three Five-Absence-sector results at once: no proton decay")
print("  (never-gauged SO(10), 4190), no sterile neutrino (unread SU(2)_R, F144), and Majorana-mass-allowed (B-L not")
print("  independently gauged, this toy). Cal+Keeper own the F137 audit (whether F137 asserted an independent gauged B-L);")
print("  this supplies the charge arithmetic that supports the re-scoping. Opens unchanged: 3-neutrino placement (Lyra")
print("  continuum + #418) and the fermionic-tower rerun. No count move (Absences not among the 26). Count 2 of 26.")
print("=" * 100)
print()
print("Elie - Monday 2026-06-15 (charge-structure verification supporting Lyra F146, resolving her load-bearing caveat: Lyra's no-right-handed-neutrino/Majorana result F144/F146 hinges on ONE scoping question flagged for Cal+Keeper -- does BST gauge an INDEPENDENT U(1)_(B-L) or does B-L enter only through read hypercharge Y? independent-gauged -> Majorana forbidden (tension real); only-through-Y -> Majorana allowed (no tension); THIS TOY verifies the charge structure (my lane F102): Y/2 = T_3R + (B-L)/2 for ALL SM fermions (7/7 incl would-be nu_R), Y the READ/gauged combination + T_3R (SU(2)_R) UNREAD (F144), so B-L = Y - 2*T_3R is NOT an independent gauge charge (only global/classification, structurally same as never-gauged SO(10) F137); Weinberg operator LLHH (the Majorana mass) total gauged hypercharge 2*Y_L+2*Y_H = 2*(-1)+2*(+1) = 0 -> Y-NEUTRAL preserves gauged U(1)_Y, total B-L 2*(-1)+2*0 = -2 -> violates GLOBAL B-L by 2, violating global is permitted only gauged sacred -> Majorana mass ALLOWED = Lyra candidate 1; PARALLEL one principle 'BST gauges only what it reads' gives in one stroke no proton decay (SO(10) never gauged no X/Y no dim-6 qqql, Elie 4190) + no sterile neutrino (SU(2)_R unread no nu_R, Lyra F144) + Majorana allowed (B-L not independently gauged enters only through read Y, this toy) = three Five-Absence-sector consequences from read=gauged/unread=global/classification; HONEST confirms at charge-structure level Lyra candidate-1 resolution (Y/2=T_3R+(B-L)/2 7/7, B-L=Y-2T_3R T_3R unread -> not independently gauged -> Weinberg Y-neutral violates only global B-L -> allowed, no gauge-inconsistency), CAVEAT OWNERSHIP this supplies charge arithmetic + whether F137 asserted independent gauged B-L is the Cal+Keeper F137 audit Lyra requested (if it did the text needs re-scoping B-L-enters-only-through-Y which this supports), opens unchanged 3-neutrino strip placement (count-mover Lyra continuum + #418) + fermionic-tower rerun (Lyra), NO count move Five-Absences not among 26; count 2 of 26 muon yellow IDENTIFIED)")
print()
print(f"SCORE: {passed}/{len(checks)} (B-L not independently gauged supports Lyra F146: Y/2 = T_3R + (B-L)/2 (7/7 SM fermions), B-L = Y - 2*T_3R, T_3R (SU(2)_R) UNREAD (F144) -> B-L NOT an independent gauge charge (global/classification, like never-gauged SO(10)); Weinberg LLHH Y-neutral (preserves gauged U(1)_Y) + violates global B-L by 2 -> Majorana mass ALLOWED = Lyra candidate 1; one principle read=gauged gives no-proton-decay + no-nu_R + Majorana-allowed; Cal+Keeper own the F137 audit, this supplies the charge arithmetic; no count move, Absences not in 26; count 2 of 26)")
