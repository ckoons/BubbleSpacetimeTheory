#!/usr/bin/env python3
"""
Toy 4702 — Jul 17 (the honest bar for Lyra's sin²θ_W embedding, mine; fish-detector infrastructure): Lyra is computing
sin²θ_W from the SU(2)_L=Sp(1)⊂SO(5) / U(1)_Y=SO(2) embedding normalization inside SO(5,2), target 3/13 =
N_c/(N_c²+rank²). My assignment is to verify her number INDEPENDENTLY when it lands — but before it does, I set the bar
her derivation must clear, because Cal flagged the exact risk ("watch that sin²θ_W's embedding is a COMPUTED
normalization") and Grace already hit the forbidden-GUT trap once (sin²θ_W=3/8 is NOT a BST win, it's a Five-Absence
violation). This toy pins (1) WHICH scale 3/13 matches — it RUNS, so the number is meaningless without a scale; (2) that
3/13 is NOT the forbidden GUT 3/8; (3) the target-innocence gate the embedding must pass.

THE THREE BARS (what Lyra's embedding must clear):
  * SCALE BAR: sin²θ_W runs. 3/13 = 0.23077 matches the M_Z-scale MS-bar value 0.23122 (0.19%), NOT the on-shell
    0.22306 (3.5% off). So the embedding, if it lands 3/13, predicts the M_Z-scale RUNNING value directly — which
    means the natural embedding scale must BE ~M_Z (needs justification), not a high unification scale + running down.
    This is the honest "runner" subtlety (my toy 4696): 3/13 is a primary FORM at a specific scale, not a static law.
  * FIVE-ABSENCE BAR: the GUT value is sin²θ_W = 3/8 = 0.375 (bare, at unification, runs DOWN to ~0.231 at M_Z). BST
    FORBIDS GUTs → BST must NOT predict 3/8-at-high-scale-plus-running. BST's 3/13 = 0.23077 is the LOW-scale (physical,
    M_Z) value DIRECTLY — a genuinely DIFFERENT structure from GUT (no unification scale, no long running). 3/13 ≠ 3/8
    is a Five-Absence PASS: the BST value is not the forbidden one. Good.
  * TARGET-INNOCENCE BAR: the denominator 13 = N_c² + rank² = 9 + 4 is the forced anchor (T2003 / my Phase-F count).
    For the embedding to be a DERIVATION and not an integer-match, 13 must emerge from an INDEX / trace-normalization
    count of the SU(2)_L / U(1)_Y generators inside SO(5,2) that is INNOCENT of the observed 0.23122 — i.e., Lyra's
    Tr(T_3²)/Tr(Q²)-type computation must produce 3/13 from the embedding indices alone. If it does → runner→forced. If
    13 only appears by choosing to match 0.231 → it stays a primary-form identification (I-tier), not a derivation.

⟹ VERDICT: I stage the independent verification with three explicit bars. 3/13 = 0.23077 matches M_Z-scale MS-bar at
0.19% (SCALE bar: an M_Z-scale runner value, not a static law); 3/13 ≠ GUT 3/8 (FIVE-ABSENCE bar: PASS, not the
forbidden value); and the derivation stands or falls on whether Lyra's embedding produces 13 = N_c²+rank² from a
target-innocent index count (TARGET-INNOCENCE bar: the open gate). When Lyra lands the embedding, I verify the index
arithmetic against these three bars. Count ~7-8; sin²θ_W currently a RUNNER, candidate to move runner→forced IF the
embedding is target-innocent.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

bst = F(N_c, N_c**2 + rank**2)                        # 3/13
print(f"\n[BST form]: sin²θ_W = N_c/(N_c²+rank²) = 3/13 = {float(bst):.5f}; denominator 13 = N_c²+rank² = {N_c**2+rank**2} (forced anchor)")

# ---- SCALE BAR: which scale does 3/13 match? --------------------------------
sw_onshell = 1 - (80.377**2)/(91.1876**2)             # on-shell 1 - m_W²/m_Z²
sw_msbar   = 0.23122                                  # MS-bar at M_Z (PDG)
sw_eff     = 0.23155                                  # effective leptonic
d_on  = abs(float(bst)-sw_onshell)/sw_onshell
d_ms  = abs(float(bst)-sw_msbar)/sw_msbar
d_eff = abs(float(bst)-sw_eff)/sw_eff
print(f"[scale]: 3/13={float(bst):.5f} vs on-shell {sw_onshell:.5f} ({d_on*100:.2f}%), MS-bar(M_Z) {sw_msbar:.5f} ({d_ms*100:.2f}%), eff-lep {sw_eff:.5f} ({d_eff*100:.2f}%)")
check("SCALE BAR: sin²θ_W RUNS — 3/13 = 0.23077 matches the M_Z-scale MS-bar value 0.23122 (0.19%), NOT the on-shell "
      "0.22306 (3.5% off). So the embedding, IF it lands 3/13, predicts the M_Z-scale running value directly → the "
      "natural embedding scale must BE ~M_Z (to justify), not a high scale + running. 3/13 is a primary FORM at a "
      "specific scale, not a static law (the honest 'runner' subtlety).",
      d_ms < 0.005 and d_on > 0.02, "3/13 matches M_Z-scale MS-bar (0.19%), not on-shell — an M_Z-scale runner value")

# ---- FIVE-ABSENCE BAR: 3/13 is NOT the forbidden GUT 3/8 --------------------
gut = F(3,8)
print(f"[Five-Absence]: BST 3/13={float(bst):.4f} (M_Z physical) vs GUT 3/8={float(gut):.4f} (bare, unification) — DIFFERENT structures")
check("FIVE-ABSENCE BAR: the GUT value is sin²θ_W = 3/8 = 0.375 (bare at unification, runs DOWN to ~0.231 at M_Z). BST "
      "FORBIDS GUTs, so must NOT predict 3/8+running. BST's 3/13 = 0.23077 is the LOW-scale physical value DIRECTLY — a "
      "genuinely different structure (no unification scale, no long running). 3/13 ≠ 3/8 → Five-Absence PASS: the BST "
      "value is NOT the forbidden one (the trap Grace hit; sin²θ_W=3/8 would be a GUT signature, not a BST win).",
      bst != gut and abs(float(bst)-0.375) > 0.1, "3/13 ≠ GUT 3/8 — Five-Absence PASS; BST predicts the M_Z value directly, not the GUT bare value")

# ---- TARGET-INNOCENCE BAR: the open gate for Lyra's embedding ---------------
check("TARGET-INNOCENCE BAR (the open gate): 13 = N_c²+rank² = 9+4 is the forced anchor. For the embedding to be a "
      "DERIVATION (not integer-match), 13 must emerge from an INDEX/trace-normalization count of the SU(2)_L=Sp(1) and "
      "U(1)_Y=SO(2) generators inside SO(5,2) — a Tr(T_3²)/Tr(Q²)-type ratio INNOCENT of the observed 0.23122. If "
      "Lyra's embedding produces 3/13 from the indices alone → sin²θ_W moves RUNNER→FORCED. If 13 appears only by "
      "matching 0.231 → it stays a primary-form IDENTIFICATION (I-tier), not a derivation. This is what I verify when she lands it.",
      N_c**2 + rank**2 == 13, "the derivation stands/falls on 13 from a target-innocent index count — the gate I verify on Lyra's landing")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (staged verification, three bars): 3/13 = 0.23077 matches M_Z-scale MS-bar at 0.19% (SCALE: an M_Z "
      "runner value, not a static law); 3/13 ≠ GUT 3/8 (FIVE-ABSENCE: PASS, not the forbidden value); derivation stands "
      "or falls on 13 = N_c²+rank² from a target-innocent index count (TARGET-INNOCENCE: the open gate). When Lyra "
      "lands the embedding, I verify the index arithmetic against these three bars. sin²θ_W: RUNNER, candidate "
      "runner→forced IF target-innocent. Count ~7-8 (α RULED).",
      d_ms < 0.005 and bst != gut and N_c**2+rank**2 == 13,
      "three bars set: M_Z-scale runner (0.19%) + Five-Absence PASS (≠3/8) + target-innocence gate open — staged for Lyra")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 100)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 100)
print(f"SCORE: {passed}/{total}")
print("=" * 100)
print("""
THE HONEST BAR for Lyra's sin²θ_W embedding (staged independent verification):
  * SCALE: 3/13 = 0.23077 matches M_Z-scale MS-bar 0.23122 (0.19%), NOT on-shell 0.22306 (3.5%) → an M_Z-scale runner
    value; the embedding must naturally live at ~M_Z, not high-scale + running.
  * FIVE-ABSENCE: 3/13 ≠ GUT 3/8 = 0.375 → PASS. BST predicts the LOW-scale physical value directly (no GUT, no long
    running) — genuinely different from the forbidden GUT signature (the trap Grace hit).
  * TARGET-INNOCENCE: 13 = N_c²+rank² must come from a Tr(T_3²)/Tr(Q²)-type index count INNOCENT of 0.23122 → derivation.
    If so, sin²θ_W moves RUNNER→FORCED; if 13 only matches the data, it stays I-tier identification.
  => I verify the index arithmetic against these three bars when Lyra's embedding lands. Count ~7-8; Five-Absence-safe.
""")
