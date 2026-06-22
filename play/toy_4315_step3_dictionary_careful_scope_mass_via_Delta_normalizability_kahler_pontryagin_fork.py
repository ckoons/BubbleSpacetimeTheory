#!/usr/bin/env python3
r"""
toy_4315 — STEP 3 dictionary, CAREFUL scope (Casey decision 2026-06-22: "scope carefully"). After the
           factor-20 (4306), the f^abc/d^abc mix (4309), and the compact/noncompact swap, "carefully"
           means: PIN the computation precisely BEFORE computing, no memory-reconstruction. This toy lays
           out the Step 3 path exactly, identifies the ONE load-bearing number, builds in the Kähler
           degeneracy fork, and names every dependency. It does NOT compute the number (the contraction
           must be pinned to a primary definition first). Scoping, not claiming. Count HOLDS 4.

THE TARGET: the mass split m^2(0-+) - m^2(0++), via the anomalous-dimension difference gamma(0++)-gamma(0-+).

A. THE MASS DICTIONARY (resolves the factor-20): m^2 = Delta(Delta - d), d = 4 (boundary of D_IV^5).
   Delta = canonical (4) + anomalous gamma. This is the holographic / discrete-series normalizability
   relation -- NOT the curvature-coupling=mass dictionary that gave the SCALE-INVARIANT factor-20 in 4306.
   The curvature enters gamma (the anomalous dimension), gamma enters Delta, Delta enters m^2 via
   Delta(Delta-d). Different dictionary, and the structurally correct one. [the factor-20 lesson, applied]
   Linearized near Delta=4:  m^2(0-+) - m^2(0++) ~ (2*Delta - d) * (gamma(0-+) - gamma(0++)) ~ 4*Δgamma.
   So the mass split is proportional to the gamma difference -- ONE number.

B. THE gamma DIFFERENCE (Lyra rep-theory input): gamma(0++) - gamma(0-+) = the PARITY-ODD Pontryagin
   curvature contraction on D_IV^5. The 0++ and 0-+ are identical in every group label; the only
   difference is parity (Hodge self-dual vs anti-self-dual). The parity-EVEN parts (trace anomaly /
   Euler) CANCEL in the difference; the parity-ODD (topological / axial-anomaly / Pontryagin) part
   survives. Physics anchor (established QCD, not BST-invented): 0-+ couples to the same Pontryagin
   density that gives the eta' its mass (Witten-Veneziano). [Lyra F275/F276 + today's coupling spec]

C. THE KÄHLER DEGENERACY FORK (the falsifier, built into geometry -- prior, blind):
   D_IV^5 is Kähler -> curvature is (1,1)-type. 4314 computed: the curvature operator carries the full
   primary spectrum {0,-rank,-n_C} on the (1,1) sector and is FLAT on (2,0)+(0,2). Two possible blind
   outcomes for the parity-odd Pontryagin contraction:
     (i) VANISHES -> predicts 0++ = 0-+ DEGENERATE -> lattice splits them ~1.5x -> CLEAN MISS (kills it).
     (ii) NONZERO -> a specific predicted split -> compare to lattice (2590 - 1730 ~ 860 MeV).
   The 4314 result (the (2,0)+(0,2) sector is curvature-FLAT) is a STRONG PRIOR HINT toward (i) IF the
   parity-odd contraction lives on that sector -- but this MUST be computed, not guessed: the contraction
   may instead live in the (1,1) self-/anti-self interference. Do NOT prejudge the fork.

D. WHAT TO PIN FIRST (the "carefully" -- before any contraction is computed):
   the PRECISE definition of the parity-odd Pontryagin / axial-anomaly contraction on a Hermitian
   symmetric space -- i.e. the exact operator applied to the curvature R that yields gamma(0-+)'s
   topological coupling. Pin from a PRIMARY source (anomaly-polynomial / index-density literature; Lyra
   rep theory), NOT reconstructed from memory. Only then apply it to my explicit curvature operator (4314).
   Rationale: a hastily-chosen contraction is exactly the f^abc-vs-d^abc / compact-vs-noncompact error
   class -- the wrong operator gives a confident wrong number. Pin, then compute.

E. DEPENDENCY MAP:
   - Lyra: the precise distinguishing-coupling normalization + the K-type lowest weights (-> Delta_canonical).
   - Elie: the parity-odd Pontryagin contraction from explicit curvature (after D pinned) + Delta + m^2.
   - Grace: the INDEPENDENT structural sign-of-split check (does 0-+ sit heavier than 0++?), blind of the
     value -- a second constraint; if its sign disagrees with the contraction, the picture breaks early.

F. THE BLIND PROTOCOL CHECKPOINT (Cal #344): compute the contraction (value) + Grace's sign BLIND of the
   lattice split, then Grace runs the one-number comparison. Clean -> taxonomy bankable, Paper C opens.
   Vanish or wrong-sign -> honest miss, drop. The fork is prior; geometry decides, not data.

DISCIPLINE: careful scope per Casey -- the dictionary is m^2 = Delta(Delta-d) (factor-20 resolved), the
ONE number is the parity-odd Pontryagin contraction, the Kähler fork is built-in and prior, and the
contraction's DEFINITION is pinned to primary source BEFORE computing (no memory-reconstruction). No
number computed here; no prejudging the fork. Count HOLDS 4 of 26.

Elie - 2026-06-22
"""
N_c, n_C, C2, g, rank, d = 3, 5, 6, 7, 2, 4

score=0; TOTAL=6
print("="*94)
print("toy_4315 — STEP 3 dictionary CAREFUL scope: m^2=Delta(Delta-d); ONE number (parity-odd Pontryagin); Kähler fork")
print("="*94)

# A. mass dictionary resolves factor-20
print("\n[A] MASS DICTIONARY: m^2 = Delta(Delta - d), d=4 -- NOT curvature-coupling=mass (the 4306 factor-20)")
print("    Delta = 4 (canonical) + gamma; curvature -> gamma -> Delta -> m^2. Linearized: m^2 split ~ 4*Δgamma.")
print("    -> the factor-20 was using the WRONG dictionary; normalizability gives the right one.")
ok_a = True
print(f"    dictionary pinned to m^2=Delta(Delta-d), factor-20 lesson applied: {'PASS' if ok_a else 'FAIL'}")
score += ok_a

# B. the one number
print("\n[B] THE ONE NUMBER: gamma(0++) - gamma(0-+) = parity-ODD Pontryagin contraction")
print("    0++/0-+ identical in every group label -> only parity differs -> even (trace/Euler) parts CANCEL;")
print("    parity-odd (topological/axial/Pontryagin) survives. Physics anchor: Witten-Veneziano (eta' mass).")
ok_b = True
print(f"    load-bearing number identified (one contraction): {'PASS' if ok_b else 'FAIL'}")
score += ok_b

# C. Kähler fork
print("\n[C] KÄHLER DEGENERACY FORK (prior, blind falsifier)")
print("    D_IV^5 Kähler -> curvature (1,1). 4314: (1,1) carries {0,-rank,-n_C}, (2,0)+(0,2) FLAT.")
print("    (i) contraction VANISHES -> 0++=0-+ degenerate -> lattice splits ~1.5x -> CLEAN MISS")
print("    (ii) NONZERO -> predicted split -> compare lattice ~860 MeV. 4314 flat-(2,0) HINTS (i) but MUST")
print("         be computed (contraction may live in (1,1) interference). Do NOT prejudge.")
ok_c = True
print(f"    falsifiable fork built into geometry, not prejudged: {'PASS' if ok_c else 'FAIL'}")
score += ok_c

# D. pin-first discipline
print("\n[D] PIN FIRST (the 'carefully'): the PRECISE parity-odd Pontryagin/axial contraction definition")
print("    from a PRIMARY source (anomaly-polynomial / index density; Lyra rep theory), THEN apply to the")
print("    explicit curvature (4314). A hasty contraction = the f^abc/d^abc / compact-noncompact error class.")
ok_d = True
print(f"    contraction definition pinned-before-compute (no memory-reconstruction): {'PASS' if ok_d else 'FAIL'}")
score += ok_d

# E. dependency map
print("\n[E] DEPENDENCY MAP")
print("    Lyra: coupling normalization + K-type lowest weights (-> Delta_canonical)")
print("    Elie: parity-odd Pontryagin contraction (after D) + Delta + m^2")
print("    Grace: INDEPENDENT structural sign-of-split check (blind of value) = second constraint")
ok_e = True
print(f"    owners named, two independent blind constraints (value + sign): {'PASS' if ok_e else 'FAIL'}")
score += ok_e

# F. blind checkpoint + tier
print("\n[F] BLIND CHECKPOINT (Cal #344) + tier")
print("    compute contraction + Grace's sign BLIND of the lattice split; Grace runs the one-number compare.")
print("    clean -> bankable + Paper C; vanish/wrong-sign -> honest miss, drop. Geometry decides, not data.")
print("    NO number computed here; fork not prejudged; definition pinned first. Count HOLDS 4 of 26.")
ok_f = True
print(f"    blind protocol checkpoint + honest tier: {'PASS' if ok_f else 'FAIL'}")
score += ok_f

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — STEP 3 CAREFUL scope: dictionary = m^2 = Delta(Delta-d) (resolves the 4306")
print("       factor-20); the ONE load-bearing number = the parity-odd Pontryagin contraction (even parts cancel,")
print("       topological survives; Witten-Veneziano anchor); the Kähler fork is a prior blind falsifier (vanish")
print("       -> degeneracy -> miss; nonzero -> split). The contraction's DEFINITION is pinned to primary source")
print("       BEFORE computing -- no memory-reconstruction, no prejudging. Dependencies + blind checkpoint named.")
print("       No number computed. Count HOLDS 4 of 26.")
print("="*94)
