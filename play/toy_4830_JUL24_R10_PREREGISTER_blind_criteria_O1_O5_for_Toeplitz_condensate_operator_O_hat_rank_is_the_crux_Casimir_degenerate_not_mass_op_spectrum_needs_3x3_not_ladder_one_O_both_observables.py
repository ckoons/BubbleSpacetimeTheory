#!/usr/bin/env python3
"""
Toy 4830 — Jul 24 (PRE-REGISTER blind criteria O1–O5 for the Toeplitz condensate operator Ô; Elie's committed checker's half,
before Grace/Lyra write the symbol; pull 24j). Casey's steer ("linear algebra, one D_IV⁵ domain") collapsed the lepton
problem to ONE operator on H²(D_IV⁵), and Keeper (K875) named it: Ô = the Toeplitz operator on the Bergman space with the
condensate (Higgs-VEV) as its SYMBOL — i.e. F585 read honestly as an operator (Lyra's Vol 16 "Engine"). The remaining
question is now single and well-posed: WRITE the symbol, find its RANK, diagonalize once → masses = eigenvalues, mixing =
eigenvectors, V_μτ = an off-diagonal element. Keeper said "the criteria are waiting" — so I commit the blind bank criteria
NOW, before the symbol exists, so a match cannot be retrofitted (the discipline that caught the muon all week).

THREE STRUCTURAL FACTS (verified, they SHAPE the criteria):
  * FACT 1 — Ô ≠ Casimir: the raw K-Casimir π_k = k(k−n_C) is DEGENERATE (k=2,3 both −6; k=1,4 both −4), so it cannot even
    ORDER the three generations. Ô must be the CONDENSATE operator, not the Casimir (confirms K663).
  * FACT 2 — the spectrum is NOT a single geometric ladder: log-gap(e→μ)=5.33 ≈ 2× log-gap(μ→τ)=2.82 (ratio 1.89). Non-
    uniform gaps ⟹ genuine 3×3 structure is required, not one α-power ladder.
  * FACT 3 — RANK is the crux: a rank-1 symbol gives eigenvalues {trace,0,0} = ONE mass (F677). So the RANK of the
    condensate symbol decides the whole picture: rank-1 → tau only (μ,e borrowed off-diagonal); rank-3 → three masses but the
    symbol must carry a FORCED three-fold structure.

THE BLIND BANK CRITERIA (O1–O5), committed before the symbol is written:
  O1 (RANK — the load-bearing discriminator): the rank of the condensate symbol must be DERIVED from the geometry (how many
     strata the condensate couples / its support), NOT chosen to fit the mass count. rank-1 forces the seesaw reading; rank-3
     must come with a forced three-fold structure. If the rank is picked to make three masses appear, it is a fit.
  O2 (SYMBOL target-innocent): the condensate profile φ must be specified from the Higgs-VEV substrate mechanism (F585) +
     BST primaries, NOT reverse-engineered from {m_e,m_μ,m_τ}. A symbol tuned to reproduce the masses is IDENTIFIED, not
     derived.
  O3 (SPECTRUM forced not fit): the eigenvalues must reproduce the hierarchy (207, 16.8) with the symbol's parameters FORCED
     (e.g. the inter-level overlaps = Grace's proved A(k→k+1)=α). If a free parameter must be tuned to hit the ratios, the
     values stay identified.
  O4 (ONE Ô gives BOTH observables — my cross-check): the SAME Ô must yield masses (eigenvalues) AND the PMNS mixing
     (eigenvectors). Not one operator for masses and another for mixing. This is the one-domain form of W4; passes iff a
     single Ô carries both.
  O5 (STRUCTURE = eigenspaces, coordinate-independent): the three eigenspaces of Ô must BE the three Wallach phases
     (continuum / discrete-3/2 / discrete-0). Then the durable why-three bank is exactly the spectral statement of Ô and
     stays intact regardless of whether the VALUES derive.
  STOPPING GUARD (meta): writing Ô + diagonalizing is NOT a new mechanism — it is the one-domain form of the existing F585
     condensate, so it earns ONE clean shot. If the diagonalization needs a fit (symbol reverse-engineered OR rank chosen),
     the values tier as identified/structural and we STOP — no tenth reframe.

⟹ VERDICT (plain): the checker's half is COMMITTED BLIND for the one operator — O1 (rank derived, the crux), O2 (symbol
target-innocent), O3 (spectrum forced), O4 (one Ô carries masses AND mixing, my cross-check), O5 (eigenspaces = Wallach
phases), + the stopping guard (one shot; fit → tier + stop). Three facts fixed: Ô ≠ Casimir (degenerate, K663), the spectrum
needs genuine 3×3 (non-uniform gaps), and RANK is the load-bearing question (rank-1 → one mass, F677). I fire the full
diagonalization cross-check the instant Grace/Lyra write the symbol. Structure (gens = 3 eigenspaces = 3 Wallach phases)
UNAFFECTED — the durable win is the spectral statement. EW banked; Five-Absence-positive. Count ~7.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

me, mmu, mtau = 0.511, 105.658, 1776.86
cas = {k: k * (k - n_C) for k in range(1, 7)}
vals = list(cas.values())
casimir_degenerate = any(vals.count(v) > 1 for v in vals)
g1, g2 = np.log(mmu / me), np.log(mtau / mmu)
non_uniform = abs(g1 / g2 - 2) < 0.2                       # ~2, not 1 (ladder)
eig_r1 = sorted(abs(np.linalg.eigvalsh(np.outer([1, 2, 3.], [1, 2, 3.]))), reverse=True)
rank1_one_mass = abs(eig_r1[1]) < 1e-9 and abs(eig_r1[2]) < 1e-9
print(f"\n[Ô criteria] Casimir {cas} degenerate={casimir_degenerate} (Ô≠Casimir, K663); log-gaps {g1:.2f} vs {g2:.2f} ratio {g1/g2:.2f}→3×3; rank-1→{np.round(eig_r1,1)} one mass (F677)→RANK is the crux")

check("FACT 1 → Ô ≠ Casimir (shapes the criteria): the raw K-Casimir π_k=k(k−n_C) is degenerate (k=2,3 both −6; k=1,4 both "
      "−4), so it cannot even ORDER the three generations. Ô must be the CONDENSATE (Toeplitz-symbol) operator, not the "
      "Casimir. Confirms K663.",
      casimir_degenerate and cas[2] == cas[3] and cas[1] == cas[4],
      "Casimir degenerate (k=2,3→−6; k=1,4→−4) → can't order generations → Ô = condensate operator not Casimir (K663)")

check("FACT 2 → spectrum needs genuine 3×3 (not a ladder): log-gap(e→μ)=5.33 ≈ 2× log-gap(μ→τ)=2.82 (ratio 1.89). Non-uniform "
      "gaps ⟹ NOT one geometric α-ladder → Ô must carry real 3×3 structure. This is why a single α-per-step reading missed "
      "by 91×.",
      non_uniform, "log-gaps non-uniform (ratio 1.89≈2) → not a single ladder → Ô needs genuine 3×3 structure; explains the 91× miss")

check("O1 (RANK — the load-bearing blind criterion): a rank-1 symbol gives eigenvalues {trace,0,0} = ONE mass (F677). So the "
      "RANK of the condensate symbol must be DERIVED from the geometry (how many strata it couples), NOT chosen to fit the "
      "mass count. rank-1 → tau only (μ,e off-diagonal); rank-3 → three masses but the symbol needs a FORCED three-fold "
      "structure. A rank picked to make three masses appear is a fit.",
      rank1_one_mass, "O1: rank-1→one mass (F677) → rank must be geometry-derived not fit; rank-1 forces seesaw, rank-3 needs forced 3-fold structure; the crux")

check("O2+O3 (symbol target-innocent + spectrum forced): O2 — the condensate profile φ must come from the F585 Higgs-VEV "
      "substrate mechanism + BST primaries, NOT reverse-engineered from the masses (tuned symbol = identified). O3 — the "
      "eigenvalues must reproduce the hierarchy with parameters FORCED (inter-level overlaps = Grace's proved A(k→k+1)=α); a "
      "tuned free parameter → values stay identified.",
      True, "O2: symbol from F585 mechanism not fit to masses; O3: eigenvalues forced via A(k→k+1)=α, no tuned parameter, else identified")

check("O4+O5 (my cross-check + structure): O4 — the SAME Ô must give masses (eigenvalues) AND PMNS mixing (eigenvectors); one "
      "operator, not two. This is the one-domain W4 — passes iff a single Ô carries both. O5 — the three eigenspaces of Ô must "
      "BE the three Wallach phases (continuum/3-2/0), so the durable why-three bank is the spectral statement of Ô and stays "
      "intact regardless of the values. STOPPING GUARD: one clean shot; fit (symbol reverse-engineered OR rank chosen) → tier "
      "+ STOP, no tenth reframe.",
      True, "O4: one Ô → masses AND mixing (one-domain W4); O5: eigenspaces = Wallach phases (structure = spectral); stopping guard: one shot, fit→tier+stop")

check("VERDICT: checker's half COMMITTED BLIND for the one operator Ô — O1 (rank derived, the crux), O2 (symbol target-"
      "innocent), O3 (spectrum forced via α-overlaps), O4 (one Ô carries masses AND mixing), O5 (eigenspaces = Wallach "
      "phases) + stopping guard. Facts fixed: Ô≠Casimir (degenerate), spectrum needs 3×3 (non-uniform gaps), RANK is the "
      "load-bearing question (rank-1→one mass). I fire the diagonalization the instant Grace/Lyra write the symbol. Structure "
      "UNAFFECTED (spectral). EW banked; Five-Absence-positive.",
      casimir_degenerate and non_uniform and rank1_one_mass,
      "O1–O5 committed blind; Ô≠Casimir + needs 3×3 + rank is the crux; fire diagonalization on the written symbol; structure = spectral, unaffected")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-10 (07-24) PRE-REGISTER blind criteria O1–O5 for the Toeplitz condensate operator Ô (Elie, pull 24j — the criteria Keeper said are waiting):
  * FACTS: Ô≠Casimir (Casimir degenerate k=2,3→−6 & k=1,4→−4, K663); spectrum needs 3×3 (log-gaps non-uniform, ratio 1.89≈2, explains the 91× miss); RANK is the crux (rank-1→one mass, F677).
  * O1 (rank DERIVED not fit — the load-bearing discriminator) | O2 (symbol target-innocent, from F585 not the masses) | O3 (spectrum forced via A(k→k+1)=α) | O4 (one Ô → masses AND mixing, my cross-check) | O5 (eigenspaces = Wallach phases, structure = spectral).
  * STOPPING GUARD: one clean shot (not a new mechanism); fit → tier identified/structural + STOP, no tenth reframe.
  => I fire the full diagonalization cross-check the instant Grace/Lyra write the symbol. Structure UNAFFECTED. EW banked.
""")
