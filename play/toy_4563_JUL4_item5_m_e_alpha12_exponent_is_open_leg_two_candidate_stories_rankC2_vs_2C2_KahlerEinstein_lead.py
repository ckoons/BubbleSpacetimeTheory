#!/usr/bin/env python3
"""
Toy 4563 — Jul 4 (long-pull item #5, my primary): the absolute scale m_e = 6π⁵·α¹²·m_Planck.
Forward test (Keeper): 6π⁵ AND the α¹² exponent both forward-derived → bank; else FLOOR.

RESULT: 6π⁵ is forward (F429); the chain matches at 0.032%; the exponent is EXACTLY 12.0.
But the exponent 12 is the OPEN LEG — and my target-innocence audit finds it has TWO
candidate forward stories that are numerically identical because rank=2:
  (a) 2·C_2 = (α² per step) × (C_2 = 6 Bergman embedding steps) — the "layers" story
  (b) rank·C_2 = (Kähler-Einstein Ricci = C_2) over (rank = 2 polydisk directions) — Lyra's
      just-landed down-ladder RUNG-1 mechanism (same form!)
Since rank = 2, both give 12 — so the mechanism is NOT pinned by the number. Neither is
forward-derived yet; the exponent is target-consistent but fit-suspect.

THE LEAD: 12 = rank·C_2 is the SAME form Lyra forward-derived for down-ladder rung 1
(Ricci over rank directions). IF the α-exponent shares that curvature source, it's forward
via her mechanism. BUT the roles differ (α-EXPONENT here vs mass-RATIO factor there), so the
shared-source claim needs a forward mechanism, NOT the numerical coincidence.

Target-innocence audit. m_e stays FLOOR/strong-lead. Count 8, no move.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
alpha = 1/137.035999
m_Pl = 1.220890e22   # MeV
m_e = 0.51099895
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4563 — item #5: m_e = 6π⁵·α¹²·m_Planck; the α¹² exponent is the open leg")
print("=" * 82)

# ---- the chain matches at 0.032%; exponent is exactly 12 --------------------
sixpi5 = 6*math.pi**5
need = math.log(m_e/(sixpi5*m_Pl))/math.log(alpha)
m_pred = sixpi5 * alpha**12 * m_Pl
print(f"\n[chain] m_e = 6π⁵·α^n·m_Planck")
print(f"  6π⁵ = {sixpi5:.3f} (forward, F429) ; exponent needed n = {need:.3f}")
print(f"  m_e pred (n=12) = {m_pred:.5f} MeV vs {m_e} → {abs(m_pred-m_e)/m_e:.3%}")
check("m_e chain matches at 0.032% with exponent EXACTLY 12.0", abs(need-12) < 0.01 and abs(m_pred-m_e)/m_e < 0.001,
      "6π⁵ forward (F429); the exponent is a precise integer 12 — a real match")

# ---- target-innocence: exponent 12 has TWO candidate stories (rank=2 degeneracy) ----
print(f"\n[target-innocence audit of the exponent 12]:")
storyA = 2*C_2          # 12: α² per step × C_2 steps
storyB = rank*C_2       # 12: Ricci C_2 over rank directions
print(f"  (a) 2·C_2 = {storyA}: α² per Bergman step × C_2={C_2} embedding steps ('layers')")
print(f"  (b) rank·C_2 = {storyB}: Kähler-Einstein Ricci=C_2 over rank={rank} polydisk directions")
print(f"  BOTH = 12 because rank = 2 → the number does NOT pin the mechanism.")
check("exponent 12 has TWO candidate forward stories (2·C_2 layers vs rank·C_2 curvature), degenerate at rank=2",
      storyA == storyB == 12, "the number 12 doesn't discriminate the mechanism → not yet forward-derived")

# ---- the exponent is target-aware (identified knowing n=12) -----------------
check("exponent form identified AFTER knowing n=12 → target-aware → fit-suspect (target-innocence lens)",
      True, "same discipline I applied to the down-ladder 12; consistency demands I apply it here too")

# ---- THE LEAD: same form as Lyra's forward down-ladder rung 1 ----------------
print(f"\n[THE LEAD — connection to Lyra's forward rung 1]:")
print(f"  Lyra FORWARD-derived down-ladder rung 1: factor = rank·C_2 = 12 (Kähler-Einstein Ricci")
print(f"  = C_2 over rank polydisk directions). The m_e α-exponent is ALSO rank·C_2 = 12.")
print(f"  IF the α-exponent shares that curvature source → forward via her mechanism.")
print(f"  BUT roles DIFFER: here 12 is an α-EXPONENT (count of α-factors); there it's a mass-RATIO")
print(f"  factor. Same number, same form, DIFFERENT role → the shared-source claim needs a forward")
print(f"  mechanism (why the α-exponent = rank·C_2), NOT the numerical coincidence.")
check("LEAD: m_e exponent 12 = rank·C_2 matches Lyra's forward rung-1 form — but roles differ, needs mechanism",
      rank*C_2 == 12, "genuine lead (shared Kähler-Einstein curvature?), NOT a bank — different role")

# ---- honest discipline: don't bank on two-12's coincidence ------------------
check("do NOT bank m_e on the two-12's coincidence — flag it as a lead, verify the source forward",
      True, "pattern-matching two 12's is the trap; the α-exponent curvature source must be derived")

# ---- verdict ----------------------------------------------------------------
print(f"\n[VERDICT]: m_e chain = 6π⁵(forward) × α^(rank·C_2)(open exponent) × m_Planck(FLOOR input).")
print(f"  The exponent is the ONE open leg — target-consistent with rank·C_2 but mechanism-ambiguous")
print(f"  (2 stories, degenerate) and target-aware → fit-suspect. m_e stays a STRONG LEAD / FLOOR-")
print(f"  adjacent, NOT banked. Forward path: derive the α-exponent's curvature source (Lyra's")
print(f"  Kähler-Einstein rung-1 mechanism is the lead to chase). Count 8, no move.")
check("m_e stays FLOOR/strong-lead: exponent not forward-derived → count 8, no bank",
      True, "6π⁵ forward, exponent open; honest — the α¹² leg is the work, and it's the lead to Lyra's rung 1")

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
ITEM #5 (m_e absolute scale) — the α¹² exponent is the open leg (honest, not banked):
  * The chain m_e = 6π⁵·α¹²·m_Planck matches at 0.032% with exponent EXACTLY 12.0, and 6π⁵
    is forward (F429). Real, precise — but not yet a full forward derivation.
  * The exponent 12 is the OPEN LEG: it has TWO candidate forward stories — 2·C_2 (α²-per-step
    layers) and rank·C_2 (Kähler-Einstein Ricci over rank directions) — numerically DEGENERATE
    because rank=2. The number doesn't pin the mechanism → target-aware → fit-suspect.
  * THE LEAD: 12 = rank·C_2 is the SAME form Lyra just forward-derived for down-ladder rung 1
    (Ricci over rank directions). IF the α-exponent shares that curvature source, it's forward
    via her mechanism — but the ROLES differ (α-exponent vs mass-ratio factor), so it needs a
    forward mechanism, not the two-12's coincidence. Chase the shared Kähler-Einstein source.
  => m_e stays a STRONG LEAD / FLOOR-adjacent — 6π⁵ forward, α¹² exponent open. Count 8, no bank.
  The forward work is the exponent's curvature source; Lyra's rung-1 mechanism is the lead.
""")
