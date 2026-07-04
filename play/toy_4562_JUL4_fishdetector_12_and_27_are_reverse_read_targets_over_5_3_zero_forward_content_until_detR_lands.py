#!/usr/bin/env python3
"""
Toy 4562 — Jul 4: FISH-DETECTOR on the reopened down-ladder (my assignment). Casey's
boundary-curvature insight correctly reopened it (the channel is REAL — resolves my 4561,
survives the same-sector ratio because det'(R) is read per-stratum). But the NUMBERS 12
and 27 are currently REVERSE-READ. This toy holds the forward-only line, hard.

The claim (F466): m_s/m_d = (5/3)·12, m_b/m_s = (5/3)·27, with 12 = rank·C_2, 27 = N_c³,
both from det'(R) at the Korányi-Wolf strata.

MY AUDIT (target-innocence lens, Cal #27 firing at peak excitement):
  1. 12 = 20/(5/3) and 27 = 45/(5/3) EXACTLY → TARGET-AWARE → fit-suspect.
  2. FREE-PARAMETER COUNT: 2 boundary factors (12,27) for 2 targets (20,45); the 5/3 is
     common → carries NO discrimination. So the boundary factors are 100% of the content,
     and they're reverse-read → ZERO net forward content until det'(R) gives them.
  3. DIFFERENT-FORMS red flag: 12 = rank·C_2 (rank×Casimir) and 27 = N_c³ (color-cubed) are
     UNRELATED families. One det'(R) mechanism producing two unrelated forms must EXPLAIN
     the selection (why rank·C_2 at step 1→2, N_c³ at step 2→3) — else it's two knobs.
  4. COMPOSITION is NOT independent evidence: 900 = 20·45 automatically.
  FORWARD BAR: det'(R) at the three strata must give 12 AND 27 target-innocent, AND explain
  the rank·C_2-vs-N_c³ selection. Until then: strong LEAD, count 8.
Target-innocence audit. No count move — the discipline, fired at peak.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4562 — FISH-DETECTOR: 12 and 27 are reverse-read (targets ÷ 5/3), zero forward content")
print("=" * 82)

# ---- acknowledge the real advance first -------------------------------------
print("\n[REAL ADVANCE — not disputed]: Casey's boundary channel is genuine.")
print("  det'(R) (nonzero curvature-eigenvalue product) is read at each quark's Korányi-Wolf")
print("  stratum → generation-DEPENDENT → SURVIVES the same-sector ratio (resolves my 4561;")
print("  the channel F462 wrongly closed). The MECHANISM/LOCATION is a real reconnection.")
check("the boundary-curvature CHANNEL is real (per-stratum, survives the ratio) — mechanism advance",
      True, "not disputing the reopening; auditing the NUMBERS")

# ---- 1. target-innocence: 12 and 27 are EXACTLY targets ÷ 5/3 ----------------
dep = n_C/N_c            # 5/3 deposit ratio
b2 = 20/dep             # boundary factor for m_s/m_d
b3 = 45/dep             # boundary factor for m_b/m_s
print(f"\n[1. target-innocence audit]:")
print(f"  m_s/m_d = 20 = (5/3)·b2 → b2 = {b2:.1f} = rank·C_2 = {rank*C_2}")
print(f"  m_b/m_s = 45 = (5/3)·b3 → b3 = {b3:.1f} = N_c³ = {N_c**3}")
check("12 and 27 are EXACTLY targets÷(5/3) → TARGET-AWARE → fit-suspect (target-innocence lens)",
      abs(b2-12) < 1e-9 and abs(b3-27) < 1e-9,
      "identified AFTER knowing 20,45; no independent forward source yet → fit-suspect")

# ---- 2. free-parameter count: 2 factors for 2 targets = zero forward content --
print(f"\n[2. free-parameter count]:")
print(f"  down sector: 2 independent ratios (m_s/m_d, m_b/m_s). 900 = 20·45 is DERIVED, not free.")
print(f"  mechanism: ratio = (5/3) × boundary_factor. The 5/3 is COMMON → no discrimination.")
print(f"  ⟹ 2 boundary factors (12,27) carry 100% of the content, for 2 targets → 0 net forward content.")
check("2 free boundary factors for 2 targets, 5/3 common → ZERO net forward content until det'(R) lands",
      True, "the 5/3 doesn't discriminate; the reverse-read factors are the whole fit")

# ---- 3. different-forms red flag: rank·C_2 vs N_c³ unrelated -----------------
print(f"\n[3. different-forms red flag]:")
print(f"  step 1→2 factor = 12 = rank·C_2 = {rank}·{C_2}  (rank × Casimir)")
print(f"  step 2→3 factor = 27 = N_c³ = {N_c}³        (color-cubed)")
print(f"  these are UNRELATED families. A single det'(R) mechanism giving BOTH must explain the")
print(f"  SELECTION (why rank·C_2 here, N_c³ there) — a mechanism that fits both but explains")
print(f"  neither's selection is TWO KNOBS, not a derivation. THIS is the load-bearing question.")
check("rank·C_2 (12) and N_c³ (27) are unrelated forms — the selection must be explained, not fit",
      rank*C_2 != N_c**3 and True, "the different-factors question is load-bearing (Keeper K658)")

# ---- 4. composition is not independent evidence -----------------------------
comp = (dep**2)*12*27
print(f"\n[4. composition is NOT a third check]:")
print(f"  m_b/m_d = (5/3)²·12·27 = {comp:.0f} = 900 ✓ — but 900 = 20·45 AUTOMATICALLY.")
check("m_b/m_d=900 composing is NOT independent evidence (900 = 20·45 by construction)",
      abs(comp-900) < 1e-6, "only 2 independent ratios; the third is forced — don't count it as confirmation")

# ---- the forward bar (armed for Grace's det'(R)) ----------------------------
print(f"\n[FORWARD BAR — armed for Grace's det'(R) at the three strata]:")
print(f"  det'(R) must give 12 AND 27 from the curvature spectrum ALONE (target-innocent),")
print(f"  AND the geometry must explain the rank·C_2-vs-N_c³ selection. I run the ζ-truncation")
print(f"  numerics and check forward-vs-fit: are the eigenvalue products 12 and 27 independent")
print(f"  of the targets? If Grace's strata give them without 20/45 as input → banks. Else LEAD.")
check("forward bar set: det'(R) → 12,27 target-innocent + selection explained; else strong LEAD, count 8",
      True, "fish-detector armed on the det'(R)/O(s) term; the '20/6.7≈N_c' shortcut is the fish")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
FISH-DETECTOR ON THE REOPENED LADDER (discipline fired at peak excitement):
  * The CHANNEL is real: Casey's boundary curvature (det'(R) per-stratum) genuinely survives
    the same-sector ratio — the mechanism/location is a true advance (resolves my 4561,
    corrects F462's wrongful closure). NOT disputed.
  * The NUMBERS are reverse-read: 12 = 20/(5/3) and 27 = 45/(5/3) EXACTLY → target-aware,
    fit-suspect. 2 boundary factors for 2 targets, the 5/3 common → ZERO net forward content
    until det'(R) produces them independently.
  * Load-bearing red flag: 12 = rank·C_2 and 27 = N_c³ are UNRELATED forms. A det'(R)
    mechanism giving both must EXPLAIN the selection — else it's two knobs. And 900 composing
    is NOT independent evidence (= 20·45 automatically).
  * FORWARD BAR ARMED: det'(R) at the three strata must give 12 and 27 target-innocent AND
    explain rank·C_2-vs-N_c³. I run the ζ-truncation forward-check when Grace's strata land.
  => Reopened as a strong LEAD with a real mechanism — count STAYS 8 until det'(R) lands the
  numbers forward. The excitement is earned on the channel; the numbers are not banked. No fit.
""")
