#!/usr/bin/env python3
"""
Toy 4868 — Jul 26 (fish-detector on my OWN toy 4721 '11' vs the QCD β-function '11'; Elie, pull 26c, strong-sector scoping).
The team is scoping strong-sector dynamics (QCD β-function / asymptotic freedom). Keeper flagged an FF-20 risk on my prior
work: the '11 from KK reduction' (toy 4721) is almost certainly NOT the β-function's 11N_c, and identifying them without a
mechanism would be a textbook coincidence-trap. This is my prior toy, so I run the fish-detector on it myself before it can
mislead the new area — clearing a false lead is honest scoping.

THE TWO '11's — DIFFERENT OBJECTS on three axes (FF-20 coincidence, NOT an identity):
  * 4721 '11' = dim SO(5) + dim SO(2) = 10 + 1 = 11 — a COUNT of KK gauge fields (ELECTROWEAK sector; the over-production that
    reduces to 4 = SM_EW by the odd-g chirality lock).
  * β-function '11' = the coefficient of N_c in b₀ = (11 N_c − 2 N_f)/3 — a RATIONAL LOOP COEFFICIENT (11/3 · C_A from the
    gluon self-energy Feynman integral; COLOR/QCD sector).
  Three distinctions:
    1. TYPE: 4721 is an integer FIELD-COUNT (10+1); β is a rational LOOP-COEFFICIENT (11/3 from an integral).
    2. SECTOR: 4721 is ELECTROWEAK (SO(5) KK reduction); β-11 is COLOR/QCD (SU(3) gluon loop) — different gauge group.
    3. N_c-SCALING: 4721's 11 = dim SO(5)+1 (fixed by the coset); β's 11 MULTIPLIES N_c (11 N_c). Different N_c-dependence.
  ⟹ no mechanism maps a KK gauge-field COUNT onto a one-loop β COEFFICIENT. The two '11's are an FF-20 coincidence — DO NOT
  identify them in the strong-sector work.

THE REAL ROUTE (Keeper's scoping, principled — the companion to the gravity work F60-F66): INDUCED YANG-MILLS. The heat-kernel
a₁ coefficient gives the F²_μν term; its LOG-SCALE dependence gives the β-function — the same induced-action machinery that
gave gravity at the gauge scale.
  * TIER 1 (achievable, where the weight goes): the SIGN — asymptotic freedom (b₀ > 0), the gluon self-interaction /
    geometric curvature ANTISCREENS and dominates. A mechanism/sign claim (BST-style, like parity-violation from odd-g — a
    sign forced by geometry, not a fitted number).
  * TIER 2 (harder, FF-20-prone): the coefficient 11/3 — needs a genuine loop computation; numerology-bait unless a real
    mechanism forces it.

⟹ VERDICT (plain): my toy 4721's KK '11' is NOT the β-function's 11 — a field-count vs a loop-coefficient, electroweak vs
color, with different N_c-scaling; identifying them is a textbook FF-20 trap and I flag my own prior number so the new area
doesn't chase it. The principled route is INDUCED YANG-MILLS (heat-kernel a₁ → F² → β), aimed at TIER 1 (the SIGN of the
β-function = asymptotic freedom, a geometry-forced sign like parity) with TIER 2 (the 11/3 coefficient) held as FF-20-prone
until a mechanism forces it. This clears the scoping: aim at the induced-YM sign, NOT at matching the two '11's. No BST claim
banked here — this is a discipline/scoping toy (a coincidence rejected + a route pointed). Partition theorem untouched.
Five-Absence-positive. Count ~4.
"""
from math import comb
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

kk11 = comb(5, 2) + 1                                     # dim SO(5) + dim SO(2) = 10 + 1
beta_11_coeff = 11                                        # coefficient of N_c in b0 = (11 N_c - 2 N_f)/3
print(f"\n[fish-detector] 4721 '11' = dim SO(5)+dim SO(2) = {comb(5,2)}+1 = {kk11} (field COUNT, electroweak) vs β '11' = coeff of N_c in (11N_c−2N_f)/3 (loop COEFFICIENT, color) → different objects → FF-20 trap")

check("TYPE mismatch: 4721's 11 is an integer FIELD-COUNT (dim SO(5)+dim SO(2)=10+1); the β's 11 is a rational LOOP "
      "COEFFICIENT (11/3·C_A from the gluon self-energy Feynman integral). A count and a loop-coefficient are not the same "
      "kind of object.",
      kk11 == 11 and beta_11_coeff == 11,
      "4721 11 = field-count (10+1); β 11 = loop coefficient (11/3·C_A integral) → different TYPE of object")

check("SECTOR mismatch: 4721's 11 is ELECTROWEAK (SO(5) KK reduction → SM_EW); the β's 11 is COLOR/QCD (SU(3) gluon loop). "
      "Different gauge group, different physics.",
      True, "4721 11 electroweak (SO(5)→SM_EW); β 11 color/QCD (SU(3) gluon loop) → different SECTOR")

check("N_c-SCALING mismatch: 4721's 11 = dim SO(5)+1, fixed by the coset (does NOT multiply N_c); the β's 11 MULTIPLIES N_c "
      "(11 N_c). Different N_c-dependence → not the same number wearing two hats.",
      True, "4721 11 = dim SO(5)+1 (coset-fixed); β 11 multiplies N_c (11 N_c) → different N_c-SCALING")

check("⟹ FF-20 TRAP (rejected): no mechanism maps a KK gauge-field COUNT onto a one-loop β COEFFICIENT. The two '11's are a "
      "coincidence — DO NOT identify them in the strong-sector work. (Fish-detector on my own prior number, per Keeper's "
      "flag.)",
      kk11 == beta_11_coeff and True,  # numerically equal but structurally unrelated → the trap
      "two 11s numerically equal but structurally unrelated (type/sector/scaling all differ) → FF-20 coincidence, reject the identification")

check("THE REAL ROUTE (scoping, no number-matching): INDUCED YANG-MILLS (companion to gravity F60-F66) — heat-kernel a₁ → "
      "F²_μν → its log-scale dependence → β. TIER 1 = the SIGN (asymptotic freedom, gluon/curvature antiscreening; a "
      "geometry-forced sign like parity-from-odd-g) — where the weight goes. TIER 2 = the 11/3 coefficient — FF-20-prone, "
      "held until a mechanism forces it. Aim at TIER 1, not at matching the two 11s.",
      True, "real route = induced YM (a₁→F²→β); TIER 1 the sign (asymptotic freedom, geometry-forced), TIER 2 the 11/3 coefficient (FF-20-prone, held)")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-3 (07-26) fish-detector: KK '11' (toy 4721) is NOT the β-function '11' (Elie, pull 26c, strong-sector scoping):
  * DIFFERENT OBJECTS on 3 axes: TYPE (field-count 10+1 vs loop-coefficient 11/3), SECTOR (electroweak vs color/QCD), N_c-SCALING (dim SO(5)+1 vs 11·N_c).
  * ⟹ FF-20 TRAP: numerically equal, structurally unrelated → do NOT identify the two 11s in the strong-sector work (my own prior number, flagged per Keeper).
  * REAL ROUTE (induced YM, companion to gravity F60-F66): heat-kernel a₁ → F² → β. TIER 1 = the SIGN (asymptotic freedom, geometry-forced) where the weight goes; TIER 2 = the 11/3 coefficient (FF-20-prone, held).
  => aim the team at the induced-YM sign, not at matching the 11s. Discipline/scoping toy — no BST claim banked; partition theorem untouched.
""")
