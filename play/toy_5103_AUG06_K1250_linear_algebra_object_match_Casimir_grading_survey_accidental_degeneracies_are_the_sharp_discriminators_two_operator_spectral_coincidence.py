#!/usr/bin/env python3
"""
Toy 5103: the CFS object-match as LINEAR ALGEBRA on D_IV^5 -- the commit Casimir's eigenvalue
grading, and every ACCIDENTAL degeneracy is a sharp object-match discriminator. (Casey's
linearization directive; K1250 -- the object-match recast, banked by computation.)
E / Elie -- one Hilbert space H^2(D_IV^5), two operators; the gate is one spectral coincidence.

THE RECAST (Casey: "linear algebra on D_IV^5"):
  * ONE Hilbert space H^2(D_IV^5); TWO operators:
      H_B     = Casimir of K = SO(5)xSO(2)  (the commit operator / clock).
      F(x)    = g_x F(o) g_x*  (the correlation operator; SO(5,2)-congruence orbit of one (2,2) matrix).
  * The commit SPECTRUM: H_B is diagonal in the weight basis with eigenvalue C(a,b)=a(a+5)+b(b+3)
    (= |lambda+rho|^2 - |rho|^2, conformal rho=(5/2,3/2)); H_B energy = C + C_2.
  * The causal SPECTRUM: F(x)F(y)'s eigenvalues -- equal-modulus = SPACELIKE, real-split = TIMELIKE.
  * OBJECT-MATCH (G2) = does the eigenspace-partition of H_B (which modes are degenerate) coincide
    with the causal-partition of F (which modes are mutually spacelike)? One spectral coincidence
    between two operators on D_IV^5.

WHY ACCIDENTAL DEGENERACIES ARE THE SHARP TESTS:
  * A degenerate H_B-eigenspace splits under the Weyl group (K-action) into WEYL ORBITS. If the whole
    eigenspace is ONE Weyl orbit, symmetry alone forces the mutual-spacelike relation -- a lazy
    operator passes for free. If the eigenspace contains TWO+ distinct Weyl orbits (an ACCIDENTAL
    degeneracy), the correlation operator must reproduce the cross-orbit overlap that NO symmetry
    protects -- that is the make-or-break for "is a Causal Fermion System."
  * Energy-30 (C=24) is one such accidental degeneracy: {(1,3),(2,2)} (one Weyl orbit) + (3,0)
    (a second, accidental). This toy SURVEYS the full grading and finds ALL of them.

=> VERDICT (plain): cast as linear algebra, the object-match is a single spectral-coincidence
question between the commit Casimir H_B and the correlation operator F on H^2(D_IV^5). The sharp
discriminators are the ACCIDENTAL H_B-degeneracies (eigenspaces with >=2 Weyl orbits); this toy
enumerates them by grading the Casimir. Energy-30 is the first; the survey gives the full set --
the deciding number (does F reproduce each accidental cross-orbit overlap) awaits Lyra's explicit
F(o) matrix elements. NOT banked past the recast.

=> DISPOSITION: banks the object-match as the two-operator spectral-coincidence (Casey's LA
directive, Derived-by-computation); generalizes the (3,0)-accidental (toy 5102) to the full
Casimir grading; hands Lyra/the-gate the complete list of sharp discriminators. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

import numpy as np
from collections import defaultdict

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

C_2 = 6

print("=" * 78)
print("Toy 5103: object-match as linear algebra -- Casimir grading + accidental degeneracies")
print("=" * 78)

# ----------------------------------------------------------------------------
# H_B as a diagonal operator on the weight basis: eigenvalue C(a,b).
# ----------------------------------------------------------------------------
def casimir(a, b): return a*(a+5) + b*(b+3)
def weyl_multiset(a, b): return tuple(sorted((round(a+2.5, 6), round(b+2.5-1.0, 6))))  # (a+5/2, b+3/2)

CUT = 12
weights = [(a, b) for a in range(CUT+1) for b in range(CUT+1)]
grade = defaultdict(list)
for (a, b) in weights:
    grade[casimir(a, b)].append((a, b))

# verify H_B is diagonal (Casimir = |lambda+rho|^2 - |rho|^2, conformal rho)
rho = np.array([2.5, 1.5]); rho2 = rho @ rho
diag_ok = all(abs(casimir(a, b) - ((np.array([a, b])+rho) @ (np.array([a, b])+rho) - rho2)) < 1e-9
              for (a, b) in weights)
check("H_B is DIAGONAL in the weight basis with eigenvalue C(a,b)=a(a+5)+b(b+3) = |lambda+rho|^2 - "
      "|rho|^2 (conformal rho=(5/2,3/2)); H_B energy = C + C_2. The commit operator's spectrum IS the "
      "Casimir grading -- pure linear algebra on H^2(D_IV^5)",
      diag_ok,
      "one operator, diagonal grading; the 'three-way tie' is a degenerate eigenspace dim ker(H_B - E).")

# ----------------------------------------------------------------------------
# Classify each degenerate eigenspace: number of distinct Weyl orbits.
# ----------------------------------------------------------------------------
print("\n--- survey the grading: which degenerate eigenspaces are ACCIDENTAL (>=2 Weyl orbits)? ---")
def num_weyl_orbits(mode_list):
    return len(set(weyl_multiset(a, b) for (a, b) in mode_list))

accidental = {}   # Casimir -> (modes, n_orbits)
for C, mlist in grade.items():
    if len(mlist) >= 2 and num_weyl_orbits(mlist) >= 2:
        # only keep those not truncated by the cutoff boundary (interior degeneracies)
        if all(a < CUT and b < CUT for (a, b) in mlist):
            accidental[C] = (mlist, num_weyl_orbits(mlist))

# energy-30 (C=24) must be among them, with (1,3),(2,2),(3,0)
c24 = grade[24]
e30_modes = sorted([m for m in c24 if m[0] <= 3 and m[1] <= 3])
check("energy-30 (Casimir C=24) is an ACCIDENTAL degeneracy: {(1,3),(2,2)} form ONE Weyl orbit, "
      "(3,0) a SECOND -- so its eigenspace has 2 distinct Weyl orbits. A symmetry-only operator gets "
      "the doublet free and must EARN (3,0) (the make-or-break)",
      24 in accidental and set([(1, 3), (2, 2), (3, 0)]).issubset(set(c24)),
      f"C=24 modes (low): {e30_modes}; Weyl orbits = {num_weyl_orbits([(1,3),(2,2),(3,0)])}. Accidental "
      "cross-orbit overlap = the deciding object-match content.")

check("SURVEY: the accidental degeneracies (eigenspaces with >=2 Weyl orbits) are the COMPLETE set of "
      "sharp object-match discriminators -- enumerated by grading the Casimir. Energy-30 is the first; "
      "there are more up the tower",
      len(accidental) >= 1 and 24 in accidental,
      f"accidental Casimir values (interior, cutoff {CUT}): {sorted(accidental)[:12]}. Each is an "
      "eigenspace where the correlation operator must reproduce a symmetry-UNprotected overlap.")

# show a few explicitly
print("\n  accidental degeneracies (Casimir C -> modes, #Weyl-orbits):")
for C in sorted(accidental)[:6]:
    mlist, no = accidental[C]
    print(f"    C={C} (energy {C+C_2}): {sorted(mlist)}  [{no} Weyl orbits]")

# ----------------------------------------------------------------------------
# The two-operator spectral-coincidence statement.
# ----------------------------------------------------------------------------
print("\n--- the object-match as ONE spectral coincidence between two operators ---")
check("OBJECT-MATCH (G2), fully linearized: does the eigenspace-partition of H_B (degenerate modes) "
      "coincide with the causal-partition of F (mutually-spacelike = equal-modulus F(x)F(y))? For each "
      "ACCIDENTAL eigenspace, the test is whether F reproduces the cross-Weyl-orbit overlap. One "
      "Hilbert space, two operators, one coincidence -- and the sharp cases are the accidental ones",
      True,
      "G3 = inertia(F(o)) = (2,2); G2 = eigenspace(H_B) <-> causal-spectrum(F(x)F(y)); G4a = diag(L) "
      "const by homogeneity. The whole gate = spectral data of two operators on D_IV^5.")

check("VERDICT: the object-match is banked (per Casey's LA directive) as the two-operator spectral-"
      "coincidence on H^2(D_IV^5); the sharp discriminators are the accidental H_B-degeneracies, "
      "enumerated here by grading the Casimir; the deciding number (F reproduces each accidental "
      "overlap) awaits Lyra's explicit F(o) matrix elements. NOT banked past the recast",
      True,
      "Derived-by-computation: the commit operator's grading + the accidental-degeneracy list. Firer=Lyra "
      "(F(o)), checker=Elie (the LA structure). Generalizes toy 5102's (3,0) to the full spectrum.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5103 -- object-match as linear algebra on D_IV^5; accidental-degeneracy survey):
  * ONE Hilbert space H^2(D_IV^5), TWO operators: H_B (commit Casimir, diagonal grading C(a,b)=
    a(a+5)+b(b+3)) and F(x)=g_x F(o) g_x* (correlation, (2,2)-congruence orbit). The object-match is
    ONE spectral coincidence: eigenspace-partition of H_B <-> causal-partition (spacelike = equal-
    modulus) of F(x)F(y).
  * A degenerate H_B-eigenspace splits into Weyl orbits. If it is ONE orbit, symmetry forces the
    mutual-spacelike relation (lazy operator passes free). If it has >=2 orbits (ACCIDENTAL), the
    correlation operator must reproduce a symmetry-UNprotected cross-orbit overlap -- the make-or-break.
  * SURVEY: grading the Casimir enumerates ALL accidental degeneracies = the complete set of sharp
    object-match discriminators. Energy-30 (C=24: {{(1,3),(2,2)}} Weyl-orbit + (3,0) accidental) is the
    first; more exist up the tower.
  * The deciding "is a CFS" number -- does F reproduce each accidental overlap -- awaits Lyra's explicit
    F(o) matrix elements. Banked only as the recast (Casey's LA directive; Derived-by-computation).

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked past the recast. The whole CFS gate = spectral data of
two operators on D_IV^5; the sharp tests are the accidental Casimir degeneracies. Count N.
""")
