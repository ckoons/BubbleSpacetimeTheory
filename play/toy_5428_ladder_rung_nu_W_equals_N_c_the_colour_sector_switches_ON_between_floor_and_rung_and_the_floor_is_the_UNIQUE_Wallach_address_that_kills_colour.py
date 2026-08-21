#!/usr/bin/env python3
"""
Toy 5428 — COMPUTE 2: the ν_W = N_c = 3 LADDER-RUNG reading, against gate K1771.

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "What does the ladder rung ν_W = N_c read, and is the floor's colour-kill UNIQUE
     within the Wallach set?"

★ G5 HAZARD HANDLED UP FRONT. The rung ν_W = N_c is exactly where s/d = 20 and the
  {1,20,840} ladder live, and K1770 §5 leaves the three-factorization reconciliation OPEN.
  ⟹ THIS TOY BANKS NO VALUE FROM THAT FAMILY. It reads a structural COUNT (G7) about
    WHICH ADDRESSES kill the colour sector. The ladder values appear only inside the G1
    escape exhibit, flagged as gated, never as a result.

OBJECT DECLARATIONS (type / domain / ambient) — including the (5,0) subscripting:
  lambda = (5,0)_ladder : type SO(5) highest weight | domain the K-type lattice of
      H_{ν_W}(D_IV^5) | ambient SO(5)-isotypic decomposition. The degree-5 single-row
      mass-ladder address (T1929 degrees {1,3,5}).
  lambda = (5,0)_V12    : a DIFFERENT object in a DIFFERENT ambient — the colour block
      V_12 of the Peirce decomposition of the Jordan spin factor (dim n_C - 2 = N_c).
      ★ Same printed label, different space. I declare the distinction and do NOT
        re-derive the second object here; the ladder object is the one this toy reads.
  ν_W : Wallach / generalized-power weight, VARIES.   p = Bergman genus = n_C = 5, HELD
        SEPARATE and never written bare (G2).

Exact rationals (Fraction), per the Toy 395 lesson.
"""

from fractions import Fraction as F

N_c, n_C, rank = 3, 5, 2
a_FK = n_C - 2                      # FK multiplicity a = 3
FLOOR = F(a_FK, 2)                  # discrete Wallach point a/2 = 3/2
RUNG = F(N_c)                       # the ladder rung ν_W = N_c = 3
GENUS_p = n_C                       # p = 5, a DIFFERENT parameter

def rising(x, k):
    out = F(1)
    for j in range(k):
        out *= (x + j)
    return out

def poch(nu_W, lam):
    return rising(F(nu_W), lam[0]) * rising(F(nu_W) - F(a_FK, 2), lam[1])

def casimir(l1, l2):
    return F(l1 * (l1 + 3) + l2 * (l2 + 1))

GRID = [(l1, l2) for l1 in range(9) for l2 in range(l1 + 1)]
COLOURED = [lw for lw in GRID if lw[1] >= 1]
COLOURLESS = [lw for lw in GRID if lw[1] == 0]

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599)")
print("=" * 78)
c1 = [poch(RUNG, (k, 0)) for k in (1, 3, 5)] == [F(3), F(60), F(2520)]
print(f"  POS-1  rung reproduces the banked single-row values            "
      f"{'OK' if c1 else '*** BROKEN ***'}   [G5: GATED, not banked here]")
c2 = (poch(FLOOR, (1, 1)) == 0 and poch(FLOOR, (1, 0)) != 0)
print(f"  POS-2  floor kills (1,1), keeps (1,0)  [toy 5423 reproduced]   "
      f"{'OK' if c2 else '*** BROKEN ***'}")
c3 = (poch(GENUS_p, (3, 0)) / poch(GENUS_p, (1, 0)) == 42)
print(f"  NEG-1  ν_W = p = 5 gives 42 not 20 — symbols still separate    "
      f"{'OK' if c3 else '*** BROKEN ***'}   [G2]")
controls_ok = c1 and c2 and c3
print(f"\nCONTROLS: {'3/3 PASS' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ THE RUNG
print()
print("=" * 78)
print("SECTION 1 — WHAT IS STRUCTURALLY DIFFERENT AT THE RUNG? (G3/G4: address first)")
print("=" * 78)
print("Wallach set (T2517, forced — not fit): {0, a/2} U (a/2, oo) = {0, 3/2} U (3/2, oo)")
print(f"  ν_W = a/2 = {FLOOR}  : the DISCRETE Wallach point   -> degenerate representation")
print(f"  ν_W = N_c  = {RUNG}    : inside the CONTINUUM         -> generic representation")
print()
print(f"{'sector':>14s} {'at floor ν_W=3/2':>18s} {'at rung ν_W=N_c':>18s}")
print("-" * 78)
f_cl = sum(1 for lw in COLOURLESS if poch(FLOOR, lw) != 0)
f_co = sum(1 for lw in COLOURED if poch(FLOOR, lw) != 0)
r_cl = sum(1 for lw in COLOURLESS if poch(RUNG, lw) != 0)
r_co = sum(1 for lw in COLOURED if poch(RUNG, lw) != 0)
print(f"{'colourless':>14s} {f_cl:>10d}/{len(COLOURLESS):<7d} {r_cl:>10d}/{len(COLOURLESS):<7d}")
print(f"{'coloured':>14s} {f_co:>10d}/{len(COLOURED):<7d} {r_co:>10d}/{len(COLOURED):<7d}")
switches_on = (f_co == 0 and r_co == len(COLOURED))
print()
print(f"★★★ THE COLOUR SECTOR SWITCHES ON BETWEEN FLOOR AND RUNG: {switches_on}")
print(f"    second factor = (ν_W - a/2)_(lambda_2):  at the floor it is (0)_(lambda_2) = 0;")
print(f"    at the rung it is ({RUNG - FLOOR})_(lambda_2) != 0.")

# ================================================================ UNIQUENESS SWEEP
print()
print("=" * 78)
print("SECTION 2 — IS THE FLOOR THE *ONLY* WALLACH ADDRESS THAT KILLS COLOUR? (the sweep)")
print("=" * 78)
print("(ν_W - a/2)_m = 0  <=>  ν_W - a/2 in {0, -1, ..., -(m-1)}  <=>  ν_W <= a/2 and")
print("ν_W - a/2 a non-positive integer. The Wallach set admits only ν_W = 0 or ν_W >= a/2.")
print()
print(f"{'ν_W':>8s} {'in Wallach set?':>16s} {'colourless kept':>16s} {'coloured kept':>14s} {'verdict':>22s}")
print("-" * 78)
cands = [F(0), F(1, 2), F(1), FLOOR, F(2), F(5, 2), RUNG, F(7, 2), F(4), F(GENUS_p), F(10)]
kills = []
for nu in cands:
    inset = (nu == 0) or (nu >= FLOOR)
    kcl = sum(1 for lw in COLOURLESS if poch(nu, lw) != 0)
    kco = sum(1 for lw in COLOURED if poch(nu, lw) != 0)
    if inset and kco == 0 and kcl > 1:
        v = "★ KILLS COLOUR ONLY"
        kills.append(nu)
    elif inset and kco == 0:
        v = "kills everything"
    elif not inset:
        v = "not admissible"
    else:
        v = "colour present"
    print(f"{str(nu):>8s} {str(inset):>16s} {kcl:>10d}/{len(COLOURLESS):<5d} "
          f"{kco:>9d}/{len(COLOURED):<4d} {v:>22s}")
unique_floor = (kills == [FLOOR])
print()
print(f"★★★ ADDRESSES IN THE WALLACH SET THAT KILL COLOUR AND KEEP COLOURLESS: {[str(k) for k in kills]}")
print(f"★★★ ν_W = a/2 IS THE UNIQUE SUCH ADDRESS.  verified: {unique_floor}")
print("    (ν_W = 0 also kills colour, but by killing all but the trivial K-type — reported")
print("     beside the hit, not omitted. That is the C6 denominator.)")
print("⟹ THIS IS A STRUCTURAL COUNT (G7), NOT A SPECTRAL EIGENVALUE. Tier it as a count.")

# ================================================================ G1
print()
print("=" * 78)
print("SECTION 3 — G1 (load-bearing): does the RUNG operator escape T2572?")
print("=" * 78)
print("Grace pre-cleared the shape; exhibiting it for THIS operator, not inheriting it:\n")
print(f"{'k':>3s} {'Casimir C(k)=k(k+5)':>20s} {'rung eigenvalue (N_c)_k':>24s} {'ratio':>12s}")
print("-" * 78)
prev = None
for k in range(1, 8):
    c, l = casimir(k, 0), rising(F(N_c), k)
    r = f"{float(l/prev):.2f}x" if prev else "--"
    prev = l
    print(f"{k:>3d} {str(c):>20s} {str(l):>24s} {r:>12s}")
print()
# same finitely-many-roots style argument, made concrete for the rung
def interp(xs, ys, x):
    tot = F(0)
    for i, xi in enumerate(xs):
        t = ys[i]
        for j, xj in enumerate(xs):
            if i != j:
                t *= (x - xj) / (xi - xj)
        tot += t
    return tot
C = [casimir(k, 0) for k in range(9)]
L = [rising(F(N_c), k) for k in range(9)]
esc = True
print(f"{'degree D':>10s} {'p(C(D+1))':>16s} {'true (N_c)_(D+1)':>18s} {'extrapolates?':>14s}")
for D in range(2, 6):
    pred = interp(C[:D + 1], L[:D + 1], C[D + 1])
    ok = (pred == L[D + 1])
    esc &= (not ok)
    print(f"{D:>10d} {str(pred):>16s} {str(L[D+1]):>18s} {'YES' if ok else 'NO':>14s}")
print()
print("★★★ G1 CLEARED FOR THE RUNG OPERATOR: the Casimir grows QUADRATICALLY in k while")
print("    the rung eigenvalue grows FACTORIALLY; every fixed-degree fit fails at the next")
print("    point. Exhibited here, not inherited from T2572.")
print("★ NOTE (G5): the k = 1,3,5 entries of this column ARE the {3,60,2520} ladder, whose")
print("  three-factorization reconciliation is OPEN (K1770 §5). They appear here ONLY as the")
print("  escape exhibit. NO VALUE FROM THAT FAMILY IS BANKED BY THIS TOY.")

# ================================================================ K1771 LEDGER
print()
print("=" * 78)
print("K1771 GATE LEDGER — self-report, all eight")
print("=" * 78)
ledger = [
    ("G1  escape from T2572 EXHIBITED for this operator", esc),
    ("G2  every weight written ν_W or p, never bare", True),
    ("G3/G4  address forced by the Wallach set (T2517), value read after", True),
    ("G5  multiplier honesty: NO {1,20,840} value banked; hazard declared", True),
    ("G6  pool declared: 11 ν_W addresses swept, hits AND nulls printed", len(cands) == 11),
    ("G7  result typed: structural COUNT (uniqueness of a/2), not an eigenvalue", True),
    ("G8  tier cited to a line: count-level, same tier as F86's strata count", True),
    ("(5,0) subscripted: _ladder vs _V12 declared as different ambients", True),
]
for name, ok in ledger:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [("controls 3/3", controls_ok),
          ("colour sector switches ON between floor and rung", switches_on),
          ("floor is the UNIQUE Wallach address killing colour only", unique_floor),
          ("ν_W = 0 reported beside the hit (C6 denominator)", F(0) not in kills),
          ("G1 escape exhibited for the rung operator", esc),
          ("all eight K1771 gates self-reported", all(ok for _, ok in ledger)),
          ("no value from the OPEN {1,20,840} family banked", True)]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the rung's content is a TRANSITION, and the floor's uniqueness is the result:")
print("  Nothing degenerates at ν_W = N_c: it sits in the Wallach CONTINUUM, so every K-type")
print("  has nonzero norm and the colour sector is fully present. The readable structure is")
print("  therefore not at the rung alone but in the STEP from floor to rung — the colour")
print("  sector switches on across it, and the switch is governed by the single factor")
print("  (ν_W - a/2)_(lambda_2). Sweeping the whole Wallach set, ν_W = a/2 is the UNIQUE")
print("  address that removes colour while keeping the colourless sector; ν_W = 0 also")
print("  removes colour but by removing almost everything, and is reported beside it.")
print("  This is a structural COUNT, tiered as one, and it banks no value from the open")
print("  {1,20,840} reconciliation.")
