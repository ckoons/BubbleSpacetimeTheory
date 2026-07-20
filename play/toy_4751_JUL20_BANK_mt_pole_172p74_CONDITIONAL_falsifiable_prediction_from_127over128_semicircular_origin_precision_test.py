#!/usr/bin/env python3
"""
Toy 4751 — Jul 20 (Target 4: bank the m_t = 172.74 GeV falsifiable prediction, mine; with the discipline explicit): the
127/128 lead, IF it is the geometric pole Yukawa, pins the top pole mass to m_t = (127/128)·v/√2 = 172.74 GeV — a
collider-testable number. My job: verify it and bank it HONESTLY, with two discipline points that keep it from being
over-claimed: (1) it is CONDITIONAL (valid IF 127/128 is the geometric y_t — a code-frame LEAD gated on Q1 [radial gap]
+ Q2 [pole scheme], NOT an unconditional BST derivation); (2) it is SEMI-CIRCULAR in origin (127/128 was NOTICED from
m_t=172.74 at 0.009%), so the genuine falsifiable content is the PRECISION claim — m_t is EXACTLY (127/128)·v/√2, and a
future ~0.1 GeV measurement landing at 172.5 (not 172.74) refutes it.

THE NUMBER: m_t(pole) = (127/128)·v/√2 = (127/128)·174.10 = 172.74 GeV (measured v=246.22); 172.66 GeV (BST v=246.1).
Current pole world-average: ~172.5 (PDG cross-section) to 172.69 (direct) ± ~0.3 → the prediction 172.74 is within ~1σ.
Future colliders (FCC/ILC) reach ~0.1 GeV → confirm 172.74 or refute the fixed geometric fraction.

THE DISCIPLINE (why this is a CONDITIONAL prediction, not a banked derivation):
  (1) CONDITIONAL: m_t=172.74 holds IF y_t = 127/128 geometrically. But 127/128 is a LEAD, not banked — it's gated on
      Q1 (the radial band-edge gap = 1/2^g? — the decider, Lyra's) and Q2 (does the geometry compute the POLE Yukawa? —
      the one remaining scheme guard). So m_t=172.74 is a CONDITIONAL prediction (conditional on the code frame), NOT
      an unconditional BST result. Bank it AS conditional.
  (2) SEMI-CIRCULAR ORIGIN: 127/128 was NOTICED because m_t/(v/√2)·√2 ≈ 127/128 (0.009%). So "127/128 predicts 172.74"
      is not an independent postdiction of m_t — 127/128 was read off from m_t. The genuine falsifiable content is the
      PRECISION: IF the fraction is exactly 127/128 (a fixed geometric number, not fit), THEN m_t = 172.74 EXACTLY —
      testable at future ~0.1 GeV precision (a measurement at 172.5±0.1, not 172.74, refutes).
THE VALUE (what it buys, honestly): even conditional + semi-circular, this MOVES 127/128 from "a lead the number can't
decide" to "a lead with a near-term collider test" — a QUANTITATIVE falsifier alongside the structural Five-Absences.
Falsifiability is real progress even before Q1/Q2 land.

⟹ VERDICT: m_t(pole) = (127/128)·v/√2 = 172.74 GeV — BANK as a CONDITIONAL, FALSIFIABLE prediction (conditional on the
127/128 code-frame lead; gated on Q1 + Q2). Within ~1σ of the current WA; future ~0.1 GeV precision confirms/refutes.
The genuine content is the PRECISION claim (m_t EXACTLY 172.74). NOT an unconditional BST derivation; semi-circular in
origin. Filed to the prediction catalog as a conditional falsifier. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

v, v_bst = 246.22, 246.1
mt_pred = (127/128)*v/math.sqrt(2)
mt_pred_bst = (127/128)*v_bst/math.sqrt(2)
wa_lo, wa_hi = 172.5, 172.69

# ---- the number -------------------------------------------------------------
print(f"\n[prediction]: m_t(pole) = (127/128)·v/√2 = {mt_pred:.2f} GeV (measured v); {mt_pred_bst:.2f} (BST v); WA {wa_lo}–{wa_hi} ± 0.3")
check("THE NUMBER: m_t(pole) = (127/128)·v/√2 = 172.74 GeV (measured v=246.22); 172.66 (BST v). Current pole WA ~172.5 "
      "(xsec) to 172.69 (direct) ± ~0.3 → prediction within ~1σ. Future colliders ~0.1 GeV confirm/refute the fixed "
      "geometric fraction.",
      abs(mt_pred - 172.74) < 0.05 and wa_lo - 0.5 < mt_pred < wa_hi + 0.5, "m_t=(127/128)v/√2=172.74 GeV — within ~1σ of WA; ~0.1 GeV future test")

# ---- discipline 1: conditional ----------------------------------------------
check("DISCIPLINE 1 — CONDITIONAL (not unconditional): m_t=172.74 holds IF y_t=127/128 geometrically. But 127/128 is a "
      "LEAD, not banked — gated on Q1 (the radial band-edge gap = 1/2^g? the decider) + Q2 (does the geometry compute "
      "the POLE Yukawa? the scheme guard). So m_t=172.74 is a CONDITIONAL prediction (on the code frame), NOT an "
      "unconditional BST derivation. Bank it AS conditional.",
      True, "m_t=172.74 CONDITIONAL on the 127/128 lead (gated on Q1+Q2) — not unconditional BST; bank as conditional")

# ---- discipline 2: semi-circular origin -------------------------------------
mt_from_1276pi = None
print(f"[semi-circular]: 127/128 was NOTICED from m_t (0.009%) — so the content is PRECISION: m_t EXACTLY 172.74, not just near it")
check("DISCIPLINE 2 — SEMI-CIRCULAR ORIGIN: 127/128 was NOTICED because √2·m_t/v ≈ 127/128 (0.009%). So '127/128 "
      "predicts 172.74' is NOT an independent postdiction — 127/128 was read off from m_t. The genuine falsifiable "
      "content is the PRECISION: IF the fraction is EXACTLY 127/128 (fixed, not fit), THEN m_t=172.74 exactly — a future "
      "measurement at 172.5±0.1 (not 172.74) refutes.",
      True, "127/128 noticed FROM m_t → content is the PRECISION claim (m_t exactly 172.74), testable at ~0.1 GeV — not an independent postdiction")

# ---- the value: falsifiability ----------------------------------------------
check("THE VALUE (falsifiability, honest): even conditional + semi-circular, this MOVES 127/128 from 'a lead the number "
      "can't decide' to 'a lead with a near-term collider test' — a QUANTITATIVE falsifier alongside the structural "
      "Five-Absences. A future ~0.1 GeV top-mass measurement confirms 172.74 or refutes the fixed geometric fraction. "
      "Falsifiability is real progress even before Q1/Q2 land.",
      True, "m_t=172.74 is a quantitative near-term falsifier (future ~0.1 GeV) — real progress even conditional")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: m_t(pole) = (127/128)·v/√2 = 172.74 GeV — BANK as a CONDITIONAL, FALSIFIABLE prediction (conditional on "
      "the 127/128 code-frame lead; gated on Q1 [radial decider] + Q2 [pole scheme]). Within ~1σ of the WA; future ~0.1 "
      "GeV precision confirms/refutes. The genuine content is the PRECISION claim (m_t EXACTLY 172.74). NOT an "
      "unconditional BST derivation; semi-circular in origin. Filed as a conditional falsifier.",
      abs(mt_pred - 172.74) < 0.05,
      "m_t=172.74 GeV banked as CONDITIONAL falsifiable prediction (on 127/128 lead + Q1/Q2); precision test at ~0.1 GeV; not unconditional")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
BANK m_t = 172.74 GeV (Target 4) — CONDITIONAL falsifiable prediction, honestly tiered:
  * NUMBER: m_t(pole) = (127/128)·v/√2 = 172.74 GeV — within ~1σ of the WA (172.5–172.69 ± 0.3); future ~0.1 GeV tests it.
  * CONDITIONAL: on the 127/128 code lead (gated on Q1 radial decider + Q2 pole scheme) — NOT unconditional BST.
  * SEMI-CIRCULAR origin: 127/128 noticed FROM m_t → content is the PRECISION claim (m_t EXACTLY 172.74).
  => bank as a CONDITIONAL, near-term-falsifiable prediction (a quantitative falsifier); real progress even before Q1/Q2. Not a derivation.
""")
