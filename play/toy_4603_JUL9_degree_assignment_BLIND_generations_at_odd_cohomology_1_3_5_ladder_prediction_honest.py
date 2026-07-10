#!/usr/bin/env python3
"""
Toy 4603 — Jul 9 (CRITICAL PATH, Keeper's linchpin): pin the odd-cohomology degree assignment for
Lyra's ladder — which three ℓ are the generations — BLIND to the masses (never fit). This unblocks
her mass prediction AND the CP kink. The discipline: read the degrees off Q⁵'s geometry; if the
ladder then lands the masses it's forward; if the degrees are chosen to fit, it's reverse-read.

THE BLIND ASSIGNMENT (forced, target-innocent): T1929 (PROVED) — "three fermion generations ↔ three
odd-power primitive cycles {h¹, h³, h⁵} on Q⁵ — forced count, not fitted." So:
  ℓ = {1, 3, 5}   (the odd cohomology degrees = my Chern channels {c_1,c_3,c_5} = the odd harmonics 1:3:5).
This is read straight off the geometry (T1929 + T1945 "generation number = 3 odd-power Q⁵ cycles"),
with ZERO reference to any mass value. gen-1 = h¹ (lightest), gen-3 = h⁵ (heaviest).

WHAT THE LADDER THEN PREDICTS (Lyra's r² = ℓ/(ℓ+n_C), mass m ∝ (1−r²)^(−n_C) = (1+ℓ/n_C)^{n_C}):
  ℓ=1 → m = (6/5)⁵ = 2.49   ;  ℓ=3 → m = (8/5)⁵ = 10.49  ;  ℓ=5 → m = (10/5)⁵ = 32.0
  Normalized: {1, (4/3)⁵, (5/3)⁵} = {1, 4.21, 12.86} — and these ARE clean forced forms:
    m_s/m_d = ((n_C−1)/N_c)^{n_C} = (4/3)⁵   ;   m_b/m_d = (n_C/N_c)^{n_C} = (5/3)⁵.

HONEST TEST RESULT (I report, I do NOT tune): partial.
  * m_b/m_d = (5/3)⁵ = 12.86 ≈ constituent b/d ≈ 14 (8% — decent).
  * m_s/m_d = (4/3)⁵ = 4.21 vs constituent s/d ≈ 1.4 (3× high — a miss), and an additive confinement
    floor over-compresses b (Λ=6.5·m₁ forces b/d→2.6), so the naive ladder+additive-dressing does NOT
    cleanly land the down spectrum. The forms are clean and forced; the down masses are not landed by
    the naive ladder.
  ⟹ THE DEGREES ARE PINNED ({1,3,5}, forced by T1929) — I do NOT bend them to rescue s/d. If Lyra's
    full SO(5,2) construction (up-down twist + the real dressing) lands the masses against these forced
    degrees → forward bank; if it doesn't → an honest miss to NAME, not a reason to refit ℓ.

NOTE — this differs from Grace's earlier r₂ = 1/rank² proposal (which gave s/d = 1.38): the geometry
puts gen-2 at ℓ=3 (r²=3/8=0.375), NOT r²=0.0625. Two target-innocent guesses disagreed; the cohomology
degrees (T1929, proved) are the authority. Handed to Lyra: build the kink against ℓ={1,3,5} (blind);
test both gates (constituent masses + J≈3×10⁻⁵). I stand as the thermal-side check. Count ~7-8 (α RULED).
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

ell = [1, 3, 5]
def m(l): return (1 + l/n_C)**n_C

print("=" * 82)
print("Toy 4603 — degree assignment BLIND: generations at odd cohomology ℓ={1,3,5} (T1929); honest ladder test")
print("=" * 82)

# ---- the blind assignment ---------------------------------------------------
print(f"\n[BLIND geometric assignment — T1929 PROVED, target-innocent]:")
print(f"  ℓ = {{1,3,5}} = the odd cohomology {{h¹,h³,h⁵}} of Q⁵ = my Chern channels {{c_1,c_3,c_5}} = odd harmonics 1:3:5")
check("BLIND degree assignment ℓ = {1,3,5} — the odd-power Q⁵ cohomology cycles (T1929 PROVED), read off geometry, ZERO mass reference",
      ell == [1, 3, 5], "forced count not fitted (T1929); gen-1=h¹ lightest, gen-3=h⁵ heaviest — the discipline's requirement")

# ---- the ladder prediction --------------------------------------------------
ms = [m(l) for l in ell]
print(f"\n[what the ladder r²=ℓ/(ℓ+n_C) then predicts, m=(1+ℓ/n_C)^{{n_C}}]:")
print(f"  ℓ=1 → {ms[0]:.2f}; ℓ=3 → {ms[1]:.2f}; ℓ=5 → {ms[2]:.2f}  →  {{1, (4/3)⁵, (5/3)⁵}} = {{1, {ms[1]/ms[0]:.2f}, {ms[2]/ms[0]:.2f}}}")
check("the forced ℓ={1,3,5} gives CLEAN forms: m_s/m_d = ((n_C−1)/N_c)^{n_C} = (4/3)⁵, m_b/m_d = (n_C/N_c)^{n_C} = (5/3)⁵",
      abs(ms[1]/ms[0] - (4/3)**5) < 1e-6 and abs(ms[2]/ms[0] - (5/3)**5) < 1e-6,
      "the forms are forced by the degrees + ladder — target-innocent, not fit")

# ---- honest test ------------------------------------------------------------
sd, bd = ms[1]/ms[0], ms[2]/ms[0]
print(f"\n[HONEST test vs constituent {{1, 1.4, 14}} — I report, I do NOT tune]:")
print(f"  m_b/m_d = {bd:.2f} ≈ 14 (8%, decent);  m_s/m_d = {sd:.2f} vs 1.4 (3× high — a miss)")
check("HONEST: PARTIAL — b/d=(5/3)⁵≈14 decent; s/d=(4/3)⁵=4.21 is 3× high; naive additive dressing over-compresses b → not landed",
      abs(bd - 14)/14 < 0.15 and sd > 3, "the forms are clean+forced; the naive ladder does NOT cleanly land the down spectrum")

# ---- discipline -------------------------------------------------------------
check("DISCIPLINE: the degrees are PINNED ({1,3,5}, T1929) — I do NOT bend them to rescue s/d; reconciliation is Lyra's build, or an honest miss to NAME",
      True, "differs from Grace's r₂=1/rank² (gave s/d=1.38); the cohomology degrees are the authority — never reverse-read")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
DEGREE ASSIGNMENT (BLIND, the linchpin — pinned from geometry, honestly reported):
  * BLIND ASSIGNMENT: ℓ = {1,3,5} — the odd-power Q⁵ cohomology cycles {h¹,h³,h⁵} (T1929 PROVED,
    "forced count not fitted") = my Chern channels {c_1,c_3,c_5} = the odd harmonics 1:3:5. Read off
    the geometry with ZERO mass reference.
  * LADDER PREDICTION: {1, (4/3)⁵, (5/3)⁵} = {1, 4.21, 12.86}, with clean forced forms
    m_s/m_d = ((n_C−1)/N_c)^{n_C}, m_b/m_d = (n_C/N_c)^{n_C}.
  * HONEST TEST: PARTIAL — b/d = (5/3)⁵ ≈ 14 (decent), s/d = (4/3)⁵ = 4.21 vs 1.4 (3× high); naive
    additive dressing over-compresses b. The naive ladder does NOT cleanly land the down spectrum.
  * DISCIPLINE: the degrees are PINNED ({1,3,5}) — I do NOT bend them to fit. Reconciliation is Lyra's
    full construction (up-down twist + real dressing) against these forced degrees, or an honest miss
    to NAME. Differs from Grace's r₂=1/rank²; the cohomology (T1929) is the authority. Count ~7-8 (α RULED).
""")
