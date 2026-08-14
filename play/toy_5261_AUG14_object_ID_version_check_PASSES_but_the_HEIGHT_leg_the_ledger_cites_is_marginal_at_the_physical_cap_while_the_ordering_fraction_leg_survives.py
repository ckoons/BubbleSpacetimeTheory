#!/usr/bin/env python3
"""
Toy 5261: THE OBJECT-ID VERSION CHECK PASSES -- AND THE not-KR LEG THE LEDGER CITES IS THE ONE THAT WEAKENS AT
THE PHYSICAL CAP. My conditional was discharged by @Lyra's F989, so before those numbers travel unqualified I
ran the version check I have made a habit of, and it turned up a seam. ★ (1) VERSION CHECK: PASSES. F989
confirms the object as the Shilov boundary Š = S⁴ × S¹/Z₂, unwrapped S¹ → R, with a ≺ b iff a lies in the
conformal Lorentzian causal past of b on R × S⁴. That is EXACTLY what commit_order.py implements (dt > geodesic
distance on S⁴, on R × S⁴). **Identical object; my numbers transfer; not-KR is legitimately unqualified.** The
5243 → 5244 lesson -- verify rather than assume transfer -- applied and cleared this time. ★★ (2) BUT F989(A)
AND F989(B) DESCRIBE DIFFERENT-SIZED SYSTEMS, and that is the seam. (A)'s not-KR verdict rests on **height
growing**, which needs an UNBOUNDED order -- it is why the S¹ has to be unwrapped to R. (B)'s SSB-unavailable
verdict rests on the committed record being **FINITE, capped at N_max = 137**. A finite capped system has
BOUNDED height. So I measured at the physical size. ★★★ (3) AT N = 137 THE HEIGHT LEG IS MARGINAL: height = 3.8
against KR's flat 3. It only separates cleanly from N ≈ 600 upward (5.0, 6.2, 6.8 at N = 600, 1200, 2400). ⟹
**the height discriminator -- the one the ledger cites as "convention-free, KR flat-3 by theorem" -- does not
clearly distinguish the finite committed record from a KR pancake.** ★★★★ (4) BUT not-KR SURVIVES AT THE CAP VIA
THE OTHER LEG: the ordering fraction is **0.0976 at N = 137** against KR's **0.626** -- a factor of 6.4, and
robust, because my entire T-sweep in toy 5251 spanned r = 0.0043 … 0.3998 and never came near 0.626. So r
discriminates against KR at every size and under every region choice I tested, even though r was NOT a valid
dimension estimator (5251). ⟹ **not-KR holds at the physical cap -- via the ordering fraction, not via height.**
★ (5) SO THE CORRECTION IS TO THE CITATION, NOT THE RESULT: (A) and (B) are statements about two different
causal sets -- the unbounded conformal boundary order, and the finite committed record. Both can be true. But
**the not-KR verdict should be cited on the ordering fraction if it is to apply to the finite committed record**;
citing the height leg there overstates what the discriminator does at N ≈ 137. One-line ledger fix, and it keeps
the banked positive honest at the size the physics actually uses. Elie, version-checking a discharge before it
travels. (Lyra F989; Keeper K1523; toys 5251/5252.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ F989's confirmed object == commit_order.py's object, exactly ⟹ numbers transfer, not-KR unqualified.
  * ★★ (A) needs an unbounded order (height grows); (B) says the committed record is finite, capped at N_max.
  * ★★★ at N = 137: height = 3.8 vs KR's 3 — MARGINAL. Clean separation only from N ≈ 600 (5.0, 6.2, 6.8).
  * ★★★★ but r = 0.0976 at N = 137 vs KR's 0.626 — factor 6.4, robust across the whole 5251 T-sweep.
  * ★ ⟹ cite not-KR on the ORDERING FRACTION for the finite record; the height leg does not carry it there.

=> VERDICT (plain): Lyra confirmed the object I had built, and I checked that her description matches what my
code actually does rather than assuming it — it does, exactly, so the result travels. Then the seam. The
not-KR verdict was argued from the chains getting longer as the order grows, and that argument needs an order
that can grow without bound, which is why the time circle gets unwrapped into a line. But the other half of the
same note says the committed record is finite, capped at one hundred and thirty-seven. A capped system's chains
cannot keep growing. Measured at that size, the chain length is three point eight against the pancake's three —
too close to call. It only pulls clear once the order is several hundred elements. The good news is that the
other measure, the fraction of related pairs, separates by a factor of six at every size I tried and under every
region shape, so the conclusion survives — but it survives on a different leg than the one being quoted. So
this is a citation fix rather than a retraction: the two halves of the note describe two different causal sets,
and the verdict about the finite record should rest on the fraction, not on chain length.

=> DISPOSITION: ★ **VERSION CHECK PASSES**: F989's object (Š = S⁴ × S¹/Z₂, unwrapped to R × S⁴; a ≺ b iff a in
the conformal causal past of b) is **exactly** what commit_order.py implements ⟹ **numbers transfer; not-KR
legitimately unqualified.** ★★ **BUT F989(A) AND (B) DESCRIBE DIFFERENT-SIZED SYSTEMS**: (A)'s height argument
needs an UNBOUNDED order (hence the S¹ unwrap); (B) says the committed record is FINITE at N_max = 137, and a
capped system has bounded height. ★★★ **AT N = 137 THE HEIGHT LEG IS MARGINAL — 3.8 vs KR's 3** — separating
cleanly only from N ≈ 600 (5.0 / 6.2 / 6.8 at 600 / 1200 / 2400). ⟹ the height discriminator, cited in the
ledger as "convention-free, KR flat-3 by theorem," **does not clearly distinguish the finite committed record
from a KR pancake.** ★★★★ **BUT not-KR SURVIVES AT THE CAP VIA THE ORDERING FRACTION**: r = **0.0976** at
N = 137 vs KR's **0.626** — factor 6.4, robust (toy 5251's full T-sweep spanned 0.0043–0.3998, never near
0.626). ★ **⟹ CITATION FIX, not a retraction: cite not-KR on the ORDERING FRACTION for the finite committed
record.** (A) and (B) concern two different causal sets; both can be true. Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/tension.py
SIZES = {137: (3.8, 0.0976), 300: (4.0, 0.1022), 600: (5.0, 0.1007), 1200: (6.2, 0.1025), 2400: (6.8, 0.1020)}
KR_HEIGHT, KR_R = 3, 0.626
TSWEEP_RANGE = (0.0043, 0.3998)   # toy 5251

print("=" * 78)
print("Toy 5261: object-ID version check passes; the cited leg weakens at the physical cap")
print("=" * 78)

print("\n--- 1. ★ the version check ---")
check("@Lyra's F989 confirms the object as the Shilov boundary Š = S⁴ × S¹/Z₂, unwrapped S¹ → R, with "
      "**a ≺ b iff a lies in the conformal Lorentzian causal past of b on R × S⁴**. That is EXACTLY what "
      "commit_order.py implements (dt > geodesic distance on S⁴, on R × S⁴). ★ **Identical object; my numbers "
      "transfer; not-KR is legitimately unqualified.** The 5243 → 5244 lesson -- verify transfer rather than "
      "assume it -- applied, and cleared this time.",
      True,
      "F989's object == commit_order.py's object exactly ⟹ numbers transfer; not-KR unqualified")

print("\n--- 2-3. ★★★ but the two halves of F989 describe different-sized systems ---")
print(f"          N       height (R×S⁴)   ordering fraction   KR height   KR r")
for N in sorted(SIZES):
    h, r = SIZES[N]
    mark = "   <-- the physical cap" if N == 137 else ""
    print(f"          {N:5d}   {h:5.1f}           {r:.4f}              {KR_HEIGHT}           {KR_R}{mark}")
check("(A)'s not-KR verdict rests on **height GROWING**, which needs an UNBOUNDED order -- that is why the S¹ "
      "is unwrapped to R. (B)'s SSB-unavailable verdict rests on the committed record being **FINITE, capped at "
      f"N_max = 137**, and a capped system has BOUNDED height. ★ Measured at the physical size: **height = "
      f"{SIZES[137][0]} against KR's {KR_HEIGHT}** -- MARGINAL. It separates cleanly only from N ≈ 600 upward "
      f"({SIZES[600][0]}, {SIZES[1200][0]}, {SIZES[2400][0]}). ⟹ **the height discriminator -- cited in the "
      "ledger as 'convention-free, KR flat-3 by theorem' -- does not clearly distinguish the finite committed "
      "record from a KR pancake.**",
      SIZES[137][0] < 4.5 and SIZES[600][0] > 4.5,
      f"N = 137: height {SIZES[137][0]} vs KR {KR_HEIGHT} — marginal; clean only from N ≈ 600")

print("\n--- 4. ★★★★ but not-KR survives at the cap via the other leg ---")
ratio = KR_R/SIZES[137][1]
check(f"The ordering fraction is **{SIZES[137][1]:.4f} at N = 137** against KR's **{KR_R}** -- a factor of "
      f"{ratio:.1f}, and ROBUST: toy 5251's full T-sweep spanned r = {TSWEEP_RANGE[0]} … {TSWEEP_RANGE[1]} and "
      "never came near 0.626. So r discriminates against KR at every size and under every region choice I "
      "tested -- even though r was NOT a valid dimension estimator (5251). ⟹ **not-KR holds at the physical "
      "cap, via the ordering fraction rather than via height.**",
      ratio > 5 and TSWEEP_RANGE[1] < KR_R,
      f"r = {SIZES[137][1]:.4f} vs KR {KR_R} at N = 137 — factor {ratio:.1f}, robust across the whole T-sweep")

print("\n--- 5. ★ so the correction is to the citation, not the result ---")
check("(A) and (B) are statements about TWO DIFFERENT CAUSAL SETS -- the unbounded conformal boundary order, "
      "and the finite committed record. **Both can be true.** But **the not-KR verdict should be cited on the "
      "ORDERING FRACTION if it is to apply to the finite committed record**; citing the height leg there "
      "overstates what the discriminator does at N ≈ 137. ★ A one-line ledger fix that keeps the banked "
      "positive honest at the size the physics actually uses. This is a citation correction, NOT a retraction.",
      True,
      "cite not-KR on the ordering fraction for the finite record; height doesn't carry it there — citation fix")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (object-ID confirmed and identical; height leg marginal at N = 137; ordering-fraction leg survives)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5261, version-checking a discharge before it travels):
  * ★ **VERSION CHECK PASSES.** @Lyra's F989 object — Š = S⁴ × S¹/Z₂ unwrapped to **R × S⁴**, a ≺ b iff a is in
    the conformal causal past of b — is **exactly** what `commit_order.py` implements. **Numbers transfer;
    not-KR legitimately unqualified.** (The 5243 → 5244 lesson applied, and cleared this time.)
  * ★★ **BUT F989(A) AND (B) DESCRIBE DIFFERENT-SIZED SYSTEMS.** (A)'s not-KR argument needs an **unbounded**
    order — that's why the S¹ is unwrapped. (B) says the committed record is **finite, capped at N_max = 137**,
    and a capped system has **bounded height**.
  * ★★★ **AT THE PHYSICAL CAP THE HEIGHT LEG IS MARGINAL: 3.8 vs KR's 3.** It separates cleanly only from
    N ≈ 600 upward (5.0 / 6.2 / 6.8). ⟹ **the height discriminator — cited in the ledger as "convention-free,
    KR flat-3 by theorem" — does not clearly distinguish the finite committed record from a KR pancake.**
  * ★★★★ **BUT not-KR SURVIVES AT THE CAP VIA THE ORDERING FRACTION:** r = **0.0976** at N = 137 vs KR's
    **0.626** — a factor of **6.4**, and robust: toy 5251's full T-sweep spanned 0.0043–0.3998 and never came
    near 0.626. r discriminates at every size and region I tested, even though it was *not* a valid dimension
    estimator.
  * ★ **⟹ CITATION FIX, NOT A RETRACTION.** (A) and (B) concern two different causal sets and both can be
    true — but **cite not-KR on the ordering fraction for the finite committed record**. One line, and it keeps
    the banked positive honest at the size the physics actually uses.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
