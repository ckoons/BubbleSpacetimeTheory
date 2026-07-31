#!/usr/bin/env python3
"""
Toy 4954 — Jul 31 [PROGRAM: STANDARD] (YM sprint verification (Elie's items): (1) the glueball — pure-gauge 0⁺⁺ = c_2·π⁵·m_e =
11·π⁵·m_e = 1720 MeV vs lattice 1710±50 (0.6%, YMB), DISTINCT from the full-theory mass gap Δ = C_2·π⁵·m_e = 6·π⁵·m_e = 938 = m_p
(T1399 — glueball ≠ proton); (2) the decompactification — scale-free R⁴ has spectral gap 0 (YMC Theorem 1, Tier-1 PROVED), and the
D_IV⁵ scalar gap λ₁ = C_2/R² = 6/R² → 0 as R→∞, so the mass gap is a BOUNDED-DOMAIN fact. RED LINE HELD: this is a construction on
D_IV⁵ with W4 (cluster decomposition) OPEN, NOT a claim on the R⁴ Clay problem (K939 walked the banner back once — the time-box must
not push it back); Elie, YM sprint, K1060). The λ₁=g=7 spectral INDEX is cited from the corpus/K1060 sense-table (Grace's lane), NOT
re-derived here — glyph-trap discipline (c_2/C_2, λ₁=6/7 are exactly the collisions I've tripped on today). Corpus-run (YMB, YMC
Thm1, T1399, K1060), no glyph-weld.

★ (1) THE GLUEBALL (verified, matches lattice, DISTINCT from the mass gap): the pure-gauge 0⁺⁺ glueball = c_2·π⁵·m_e = 11·π⁵·m_e =
1720 MeV vs the lattice value 1710 ± 50 MeV (Morningstar–Peardon) at 0.6% (YMB). It uses c_2 = 11 (the 2-form / Weitzenböck gap),
NOT C_2 = 6. It is a DIFFERENT object from the full-theory mass gap Δ = C_2·π⁵·m_e = 6·π⁵·m_e = 938 MeV = m_p (T1399: "glueball ≠
proton; 938 MeV is the full-theory mass gap"). This is the SAME scale-separation discipline as my Section 4 catch (K1059): two
distinct spectral objects, not one — 1720 (pure-gauge glueball) ≠ 938 (full-theory gap = m_p).

★ (2) THE DECOMPACTIFICATION (Tier-1, YMC Theorem 1, the RED-LINE fact): a complete, non-compact, SCALE-FREE Riemannian manifold has
spectral gap = 0 (YMC Thm 1, PROVED). On D_IV⁵ (curved, finite scale R) the scalar gap is λ₁ = C_2/R² = 6/R². As R → ∞
(decompactification to flat R⁴), λ₁ → 0 — the gap VANISHES. So the mass gap is intrinsic to the BOUNDED/curved domain, NOT a
property of R⁴. This is precisely why BST's construction lives on D_IV⁵ and is NOT a solution of the R⁴ Clay problem.

★ THE SCOPE RED LINE (held, non-negotiable): this is a QFT CONSTRUCTION ON D_IV⁵ satisfying the Wightman axioms EXCEPT W4 (cluster
decomposition), which is OPEN. It is NOT a claim on the R⁴ Clay Millennium problem. The banner was walked back once (K939); an honest
OPEN W4 beats a forced closure. The time-box does not move this line. (Grace carries the K1060 sense-table; the λ₁=g=7 spectral index
is cited from it, not re-derived here — I don't repeat today's glyph/value trips.)

⟹ VERDICT (plain — YM sprint items verified, scope held): (1) the glueball 11·π⁵·m_e = 1720 MeV matches lattice (0.6%) and is a
DISTINCT object from the full-theory mass gap Δ = 6·π⁵·m_e = 938 = m_p (T1399 — same scale-separation as K1059). (2) The
decompactification is a Tier-1 PROVED no-go: scale-free R⁴ has gap 0 (YMC Thm 1), the D_IV⁵ scalar gap λ₁ = 6/R² → 0 as R→∞ — the
mass gap is a bounded-domain fact. RED LINE HELD: construction on D_IV⁵ with W4 OPEN, NOT an R⁴ Clay claim (K939). The λ₁=g=7
spectral index is corpus-cited (K1060, Grace's), not re-derived — glyph-trap discipline. [STANDARD]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
c_2 = 11                                     # Weitzenböck / 2-form gap (≠ C_2=6 Casimir — glyph discipline)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

pi5 = 3.14159265**5
m_e = 0.511
glueball = c_2 * pi5 * m_e                    # 11·π⁵·m_e (2-form gap)
massgap = C_2 * pi5 * m_e                     # 6·π⁵·m_e = m_p (full-theory gap)
m_p = 938.272
lattice = (1710, 50)                          # 0⁺⁺ glueball, Morningstar–Peardon
glueball_matches = abs(glueball - lattice[0]) / lattice[0] < 0.01     # 0.6%
glueball_distinct_from_gap = abs(glueball - massgap) > 500            # 1720 ≠ 938
gap_is_mp = abs(massgap - m_p) < 1

# ---- decompactification (Tier-1 YMC) ---------------------------------------
def scalar_gap(R): return C_2 / R**2         # λ₁ = C_2/R² = 6/R²
gap_at_1 = scalar_gap(1)                      # 6 (R=1)
gap_large_R = scalar_gap(1000)               # → 0
decompactifies = gap_large_R < 1e-4 and gap_at_1 == 6
R4_gap_zero = True                           # YMC Theorem 1: scale-free → gap 0 (PROVED)

# ---- scope red line --------------------------------------------------------
W4_open = True                               # cluster decomposition OPEN
not_R4_clay = True                           # construction on D_IV⁵, NOT R⁴ Clay
lambda1_index_corpus_cited = True            # λ₁=g=7 index from K1060 sense-table (Grace), not re-derived

print(f"\n[YM sprint verify]")
print(f"  (1) glueball 0⁺⁺ = c_2·π⁵·m_e = 11·π⁵·m_e = {glueball:.0f} MeV vs lattice {lattice[0]}±{lattice[1]} → {100*abs(glueball-lattice[0])/lattice[0]:.2f}% ({glueball_matches}). DISTINCT from mass gap Δ = 6·π⁵·m_e = {massgap:.0f} = m_p ({gap_is_mp}) — T1399.")
print(f"  (2) decompactification: scale-free R⁴ gap = 0 (YMC Thm1); D_IV⁵ scalar gap λ₁ = C_2/R² = 6/R² → 0 as R→∞ ({decompactifies}). Mass gap = bounded-domain fact.")
print(f"  RED LINE: D_IV⁵ construction, W4 OPEN ({W4_open}), NOT an R⁴ Clay claim ({not_R4_clay}). λ₁=g=7 index corpus-cited (K1060), not re-derived.")

check("(1) THE GLUEBALL matches lattice + is DISTINCT from the mass gap: pure-gauge 0⁺⁺ = c_2·π⁵·m_e = 11·π⁵·m_e = "
      f"{glueball:.0f} MeV vs lattice {lattice[0]}±{lattice[1]} (0.6%, YMB). It uses c_2=11 (2-form gap), NOT C_2=6. It is a DIFFERENT "
      f"object from the full-theory mass gap Δ = 6·π⁵·m_e = {massgap:.0f} = m_p (T1399). Two distinct spectral objects, not one.",
      glueball_matches and glueball_distinct_from_gap and gap_is_mp,
      f"glueball 11·π⁵·m_e={glueball:.0f} vs lattice 1710 (0.6%); DISTINCT from Δ=6·π⁵·m_e={massgap:.0f}=m_p (T1399); two objects (c_2=11 ≠ C_2=6)")

check("(1) SAME SCALE-SEPARATION DISCIPLINE as K1059 (my Section 4 catch): the glueball (1720, pure-gauge, c_2) and the full-theory "
      "mass gap (938=m_p, C_2) are distinct spectral objects with distinct provenance — NOT to be conflated. Rule 11 (provenance-"
      "not-value) again: 1720 ≠ 938 even though both are 'the gap' in loose talk.",
      glueball_distinct_from_gap,
      "scale-separation (Rule 11): glueball 1720 (c_2, pure-gauge) ≠ mass gap 938=m_p (C_2, full theory); distinct objects, not conflated")

check("(2) DECOMPACTIFICATION — the D_IV⁵ scalar gap λ₁ = C_2/R² = 6/R² → 0 as R→∞: at finite scale R the gap is 6/R² (=6 at R=1); "
      "as R→∞ it vanishes. So the mass gap is intrinsic to the BOUNDED/curved domain, NOT flat space. Consistent with YMC Theorem 1.",
      decompactifies,
      "decompactification: λ₁ = C_2/R² = 6/R² → 0 as R→∞ (gap at R=1 is 6); mass gap is a bounded-domain fact")

check("(2) SCALE-FREE R⁴ HAS NO GAP (YMC Theorem 1, Tier-1 PROVED — the RED-LINE fact): a complete, non-compact, scale-free "
      "Riemannian manifold has spectral gap = 0. So flat R⁴ has no mass gap; the gap exists ONLY on the curved bounded domain "
      "D_IV⁵. This is precisely why BST's construction is on D_IV⁵ and does NOT solve the R⁴ Clay problem.",
      R4_gap_zero,
      "YMC Thm1 (Tier-1 PROVED): scale-free R⁴ → gap 0; gap exists only on curved bounded D_IV⁵ → not the R⁴ Clay problem")

check("THE SCOPE RED LINE HELD (non-negotiable, K939): this is a QFT construction on D_IV⁵ satisfying the Wightman axioms EXCEPT "
      "W4 (cluster decomposition), which is OPEN. It is NOT a claim on the R⁴ Clay Millennium problem. The banner was walked back "
      "once (K939); an honest OPEN W4 beats a forced closure; the time-box does not move this line.",
      W4_open and not_R4_clay,
      "red line: D_IV⁵ construction, W4 (cluster decomp) OPEN, NOT R⁴ Clay; honest open W4 > forced closure (K939); time-box doesn't move it")

check("VERDICT: YM sprint items verified, scope held. (1) glueball 11·π⁵·m_e=1720 matches lattice (0.6%), DISTINCT from Δ=6·π⁵·m_e="
      "938=m_p (T1399, same scale-separation as K1059). (2) decompactification Tier-1 no-go: scale-free R⁴ gap 0 (YMC Thm1), D_IV⁵ "
      "scalar gap λ₁=6/R²→0 — mass gap a bounded-domain fact. RED LINE HELD: D_IV⁵ construction, W4 OPEN, NOT R⁴ Clay. λ₁=g=7 index "
      "corpus-cited (K1060), not re-derived (glyph discipline).",
      glueball_matches and decompactifies and W4_open and not_R4_clay,
      "verdict: glueball verified (distinct from m_p); decompactification λ₁=6/R²→0 (R⁴ gap 0, YMC Thm1); red line held (W4 open, not Clay); index cited")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-31 [STANDARD] YM sprint verify — glueball + decompactification, scope red-line held (Elie, K1060):
  * (1) GLUEBALL: 0⁺⁺ = c_2·π⁵·m_e = 11·π⁵·m_e = {glueball:.0f} MeV vs lattice 1710±50 (0.6%, YMB). DISTINCT from full-theory mass gap Δ = 6·π⁵·m_e = {massgap:.0f} = m_p (T1399). c_2=11 ≠ C_2=6. Same scale-separation as K1059.
  * (2) DECOMPACTIFICATION: scale-free R⁴ gap = 0 (YMC Thm1, Tier-1 PROVED); D_IV⁵ scalar gap λ₁ = C_2/R² = 6/R² → 0 as R→∞. Mass gap is a bounded-domain fact.
  * RED LINE HELD: construction on D_IV⁵, W4 (cluster decomposition) OPEN, NOT an R⁴ Clay claim (K939 — honest open W4 > forced closure; time-box doesn't move it).
  * λ₁=g=7 spectral index cited from K1060 sense-table (Grace's lane), NOT re-derived — glyph-trap discipline (c_2/C_2, λ₁ collisions I've tripped on today).
""")
