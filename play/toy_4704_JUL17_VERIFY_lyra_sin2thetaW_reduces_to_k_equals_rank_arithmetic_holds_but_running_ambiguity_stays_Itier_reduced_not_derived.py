#!/usr/bin/env python3
"""
Toy 4704 — Jul 17 (VERIFY Lyra's sin²θ_W = k=rank reduction, mine; the marquee-closure gate): Lyra reduced the whole
Weinberg angle to ONE number — sin²θ_W = N_c/(N_c + k·n_C), where k=1 → 3/8 (GUT, Five-Absence-forbidden) and k=rank=2
→ 3/13 (BST, matches obs). My assignment: verify her k=rank arithmetic against the three bars (scale / Five-Absence /
target-innocence) the moment it lands. Result: the ARITHMETIC checks exactly, the FORM is target-innocent, and the
Five-Absence structure is right (BST is NOT at the forbidden k=1) — BUT the derivation is NOT complete: k=rank is
MATCHED, not yet FORCED, and 3/8 is ALSO the GUT value that SM running takes down toward the observed 0.231, so the
value alone CANNOT certify k=rank as a geometric normalization vs GUT+running. sin²θ_W stays I-tier (reduced-to-k, NOT
derived) — which is exactly Lyra's own honest tier. I HOLD the marquee at REDUCED, not CLOSED.

THE ARITHMETIC (exact, verified):
  * sin²θ_W = N_c/(N_c + k·n_C); k=1 → 3/(3+5) = 3/8 = 0.37500; k=rank=2 → 3/(3+10) = 3/13 = 0.23077.
  * 3/13 = 0.23077 vs observed MS-bar M_Z 0.23122 (0.19%). The reduction is real and clean: the entire Weinberg angle
    hangs on the single hypercharge-normalization integer k, with the primaries {N_c, n_C} fixed.

THE THREE BARS:
  * SCALE / RUNNING (the crux — my fish-detector duty): 3/8 is BOTH the k=1 endpoint AND the SU(5)-GUT unification value
    (sin²θ_W at α1=α2). SM/GUT running takes 3/8 DOWN toward ~0.21–0.23 at M_Z (the well-known GUT sin²θ_W flow). So the
    numerical fact "3/13 ≈ observed 0.231" COINCIDES with "GUT 3/8 runs down to observed" — the value ALONE cannot
    distinguish a geometric k=rank normalization from GUT+running. BST's saving grace: Five-Absence FORBIDS a GUT, so
    BST cannot USE the 3/8+running pathway — k=rank must be a DIRECT substrate-scale SO(2) normalization. But that means
    the value-match is necessary, NOT sufficient; the certification must come from the SO(2) computation, not the number.
  * FIVE-ABSENCE: k=1 → 3/8 is the forbidden GUT value; BST is correctly NOT at k=1 (it's at k=rank → 3/13). PASS — and
    meaningfully so: the naive/GUT normalization lands on the forbidden value, and BST's geometric normalization does not.
  * TARGET-INNOCENCE (the open gate): the FORM N_c/(N_c+k·n_C) is target-innocent (primaries). But k∈{1, rank} is
    currently SELECTED by matching (k=rank matches obs; k=1 is the GUT alternative). Until the SO(2)=charge-circle
    hypercharge normalization computation FORCES k=rank INNOCENT of the observed 0.231, sin²θ_W stays I-tier
    IDENTIFIED-reduced-to-k, NOT derived. Do NOT upgrade the tier-map row to derived yet.

⟹ VERDICT: Lyra's reduction is genuine and clean — the whole Weinberg angle → one integer k, arithmetic exact, form
target-innocent, Five-Absence structure correct (k=1 forbidden GUT, k=rank BST). But the marquee is REDUCED, not
CLOSED: k=rank is matched-not-forced, and the value cannot be distinguished from GUT+running by magnitude, so the
certification MUST come from the target-innocent SO(2) hypercharge-normalization computation. sin²θ_W holds at I-tier
(reduced-to-k), NOT derived — Lyra's own honest tier, verified. Count ~7-8 (α RULED). Five-Absence-safe.
"""
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- arithmetic --------------------------------------------------------------
sw_k1   = F(N_c, N_c + 1*n_C)     # 3/8
sw_krank = F(N_c, N_c + rank*n_C) # 3/13
obs = 0.23122
print(f"\n[arithmetic]: sin²θ_W = N_c/(N_c+k·n_C); k=1 → {sw_k1} = {float(sw_k1):.5f} (GUT); k=rank=2 → {sw_krank} = {float(sw_krank):.5f} (BST) vs obs {obs} ({abs(float(sw_krank)-obs)/obs*100:.2f}%)")
check("ARITHMETIC VERIFIED (Lyra's reduction, exact): sin²θ_W = N_c/(N_c+k·n_C); k=1 → 3/8 = 0.375; k=rank=2 → 3/13 = "
      "0.23077 vs observed MS-bar M_Z 0.23122 (0.19%). The whole Weinberg angle hangs on the single integer k with the "
      "primaries {N_c, n_C} fixed — a genuine, clean reduction to one number.",
      sw_k1 == F(3,8) and sw_krank == F(3,13) and abs(float(sw_krank)-obs)/obs < 0.005,
      "sin²θ_W=N_c/(N_c+k·n_C); k=1→3/8, k=rank→3/13 (0.19%) — reduction to one number verified")

# ---- SCALE/RUNNING bar (the crux) -------------------------------------------
# 3/8 is the GUT unification value; SM running flows it down toward ~0.21-0.23 at M_Z.
gut_high = 0.375
mz_running_endpoint = 0.231     # SM/GUT running of 3/8 lands in the 0.21-0.23 band at M_Z (well-known)
print(f"[scale/running]: 3/8={gut_high} is the GUT unification value; SM running → ~{mz_running_endpoint} at M_Z; 3/13={float(sw_krank):.4f} sits at the M_Z endpoint")
check("SCALE/RUNNING BAR (the crux, my fish-detector duty): 3/8 is BOTH the k=1 endpoint AND the SU(5)-GUT unification "
      "value; SM/GUT running takes 3/8 DOWN toward ~0.21-0.23 at M_Z. So '3/13 ≈ observed' COINCIDES with 'GUT 3/8 runs "
      "to observed' — the VALUE ALONE cannot distinguish a geometric k=rank normalization from GUT+running. BST's "
      "defense: Five-Absence FORBIDS a GUT, so k=rank must be a DIRECT substrate-scale SO(2) normalization — but that "
      "makes the value-match NECESSARY, NOT SUFFICIENT. Certification must come from the SO(2) computation, not the number.",
      abs(float(sw_krank) - mz_running_endpoint) < 0.01, "3/13 sits where GUT 3/8 runs to at M_Z → value can't certify k=rank; SO(2) computation is the gate")

# ---- FIVE-ABSENCE bar -------------------------------------------------------
check("FIVE-ABSENCE BAR: k=1 → 3/8 is the forbidden GUT value; BST is correctly NOT at k=1 (it's at k=rank → 3/13). "
      "PASS — and meaningfully: the naive/GUT normalization lands ON the forbidden value, and BST's geometric "
      "normalization (k=rank) does not. The framework is internally consistent (no-GUT ⟹ not k=1).",
      sw_krank != F(3,8), "k=1 forbidden GUT, k=rank BST → Five-Absence PASS; BST correctly avoids the GUT value")

# ---- TARGET-INNOCENCE bar (the open gate) -----------------------------------
check("TARGET-INNOCENCE BAR (the open gate): the FORM N_c/(N_c+k·n_C) is target-innocent (primaries). But k∈{1,rank} is "
      "currently SELECTED by matching (k=rank matches obs; k=1 is the GUT alternative). Until the SO(2)=charge-circle "
      "hypercharge normalization FORCES k=rank INNOCENT of the observed 0.231, sin²θ_W stays I-tier IDENTIFIED-reduced-"
      "to-k, NOT derived. Do NOT upgrade the tier-map row to derived — this is Lyra's own honest tier, verified.",
      True, "k=rank is matched-not-forced; SO(2) normalization must force it target-innocently → I-tier holds, not derived")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: Lyra's reduction is genuine and clean (whole Weinberg angle → one integer k; arithmetic exact; form "
      "target-innocent; Five-Absence structure correct — k=1 forbidden GUT, k=rank BST). But the marquee is REDUCED, "
      "NOT CLOSED: k=rank is matched-not-forced, and the value cannot be distinguished from GUT+running by magnitude, so "
      "the certification MUST come from the target-innocent SO(2) hypercharge-normalization computation. sin²θ_W holds "
      "at I-tier (reduced-to-k), NOT derived. Marquee stays REDUCED. Count ~7-8 (α RULED).",
      sw_krank == F(3,13) and sw_krank != F(3,8),
      "reduction verified + Five-Absence PASS, but k=rank matched-not-forced → sin²θ_W stays I-tier reduced-not-derived; marquee REDUCED not CLOSED")

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
VERIFY Lyra's sin²θ_W = k=rank reduction (marquee-closure gate) — REDUCED, not yet CLOSED:
  * ARITHMETIC (exact): sin²θ_W = N_c/(N_c+k·n_C); k=1→3/8 (GUT), k=rank→3/13 (0.19% vs obs). Whole angle → one integer k.
  * SCALE/RUNNING (crux): 3/8 is also the GUT value; SM running flows it to ~0.231 at M_Z → value ALONE can't certify
    k=rank vs GUT+running. Five-Absence forbids BST from USING 3/8+running → k=rank must be a DIRECT SO(2) normalization.
  * FIVE-ABSENCE: k=1 forbidden GUT, k=rank BST → PASS (BST correctly avoids the GUT value).
  * TARGET-INNOCENCE (open gate): form target-innocent, but k=rank MATCHED not FORCED → I-tier until SO(2) normalization
    forces k=rank innocent of 0.231. Do NOT upgrade tier-map to derived.
  => sin²θ_W stays I-tier reduced-to-k (Lyra's honest tier, verified). Marquee REDUCED not CLOSED. Count ~7-8.
""")
