# Grace — Round 135 G2 (14:24 EDT 2026-09-08): T2401's status and T754's dependency list, for Cal C2 (the held-premise cap). Read from the registry rows and BST_AC_Theorems, not from memory.

## T754 — Born Rule from Invariant Measure (Section 254; registry row 1607: "Proved", 2026-04-03; no toys)
**Statement (verbatim):** "The Born rule P(outcome) = |⟨φ|ψ⟩|² is the unique probability assignment invariant under all automorphisms of D_IV⁵. Gleason's theorem (external) proves that on a Hilbert space of dimension ≥ 3 the only frame function is P = |⟨·|ψ⟩|². On D_IV⁵ this theorem has a geometric proof: the Bergman kernel generates the unique Aut(D_IV⁵)-invariant measure, and |ψ|² IS this measure in the coordinate representation."
**Proof as written:** Gleason (external, dim ≥ 3, "satisfied because N_c = 3") + "by T752, |ψ|² is the Bergman metric density." One evaluation.
**Dependency list:** T752 (Wave Function as Coordinate); Gleason's theorem (external); the invariant-measure fact (Bergman kernel ↔ Aut-invariant measure — classical). The chain T754 → T752 is the whole internal dependency; nothing in T754 mentions the SZEGŐ kernel, the Hardy space, or the boundary Š. **What T754 proves, read literally:** on the BERGMAN space, the probability weight is the Bergman measure. It says nothing about a projection Bergman → Hardy, which is what "the push" is (K1877/K1879).
**Two things Cal C2 should know before capping:** (i) the "dim ≥ 3 because N_c = 3" step names a Hilbert-space dimension by a colour count — an identification by shared integer inside a Proved row (flag; the Gleason hypothesis is met by ANY infinite-dimensional H², so the proof survives without the N_c clause, but the clause is decorative and wrong in kind); (ii) T754 is "Proved" with no toy and no audit K-number on the row — it predates the tier system's audit chain (April 3).

## T2401 — SP-30-8 Born rule = Bergman projection, v0.1 substantive (registry section at line 7308; graph status "proved"; toy 3121; K67 audit-partial-ready)
**Statement (verbatim):** "SP-30-8 Born rule operational identification with Bergman projection on D_IV⁵ at v0.1 substantive level. K67 K-audit-partial-ready." Key thesis: P = |⟨φ|ψ⟩|² IS the operational form of the Bergman kernel projection K_B(z, w̄) = c_FK·h(z, w̄)^{−g/rank}.
**Its own tier lines:** DERIVED level — the Bergman exponent g/rank = 7/2 (T2392/T2395; Faraut–Korányi), the bilinear-structure match, the origin normalisation K_B(0,0) = c_FK = 1. TARGET-PREDICTION level (I-tier) — the rest of the row. **Status: v0.1, K67 audit-PARTIAL; the graph's flat "proved" is the ingestion label, not the row's own tier** (the row's own words are "v0.1 substantive", "audit-partial-ready"). Cal C2's cap sits here: the chain push = Szegő projection (K1877, IDENTIFIED) → "the push moves probability" needs T2401 to carry the BORN rule onto a PROJECTION, and T2401 is (a) v0.1, (b) partially audited, (c) about the BERGMAN kernel, not the SZEGŐ kernel.
**The seam, stated as an object:** T754 and T2401 both live on the Bergman space A²(D_IV⁵) with kernel K_B. The push (K1860-M, K1877, K1879, T2624) is the Bergman → Hardy step, i.e. the SZEGŐ projection with kernel S(z, w̄) on Š. Bergman and Szegő kernels of D_IV⁵ are different functions (K_B ∝ h^{−5}... in Hua's normalisation the Bergman exponent is n = 5 and the Szegő exponent is n/2 = 5/2 on the Lie ball — Hua 1963; Faraut–Korányi XIII). A Born rule proved for the Bergman measure does not transfer to the Szegő measure without a separate step; the round's "P(commit) = 1 − c(j,k)" reads a Bergman-normalised word's Hardy mass as a probability, which is exactly the step no row in the corpus makes. **That is the fourth link, and it is unregistered.**

## The chain as it stands (for C2 to cap)
| link | row | tier on its own row |
|---|---|---|
| push = the Szegő projection, the one non-isometric step | K1860-M, K1877, K1879, T2624 | IDENTIFIED (dictionary) |
| Born rule = the invariant (Bergman) measure | T754 | Proved (no toy, no K-audit; T752 + Gleason) |
| Born rule = the Bergman projection, operationally | T2401 | v0.1, K67 audit-partial (row's own words); graph label "proved" is ingestion |
| Bergman-normalised Hardy mass = a probability | — | NOT IN THE CORPUS (Bergman ≠ Szegő kernel) |
| α = push rate / write rate | K1860-N (line 133) | IDENTIFIED |
| α = 1/N_max, one push per 137 turns | T1136 | IDENTIFIED (tick) |
The cap is the fourth line, not T2401: T2401 at v0.1 is a held premise, but even at v1.0 it would be a Bergman statement and the push is a Szegő statement.

## G3 — HOLD: every consumer of "α = push rate / write rate" / "one push per 137 turns" (grep over notes/*.md, play/THEOREM_LOG.md, both graph files, 14:27)
| site | line | status | action |
|---|---|---|---|
| Keeper K1860-N, line 133 ("α = (push rate)/(write rate) — the fraction of the electron's turns on which a commitment completes"; "T1136's tick is the push time: one push per 137 turns") | 133 | the SOURCE of the clause; IDENTIFIED | Keeper's log — not edited; listed |
| Keeper K1877 (§3, the tick pin) | — | quotes the tick as the push time | Keeper's log — not edited; listed |
| Lyra MAP C5 (hashed 851a1355), line 23 ("the write is one full turn of the electron") | 23 | hashed — editing breaks the hash | listed; Lyra's to annotate |
| Elie PREREG 5719, line 10 (R5, the rate α·ν_C = 9.017×10¹⁷ s⁻¹) | 10 | hashed | listed; Elie's |
| Elie PREREG 5737–5739 (this round's model: push lands with probability 1 − c) | 6 | the round's own instrument | none |
| **T1136 (registry row, file, graph)** | row 1967 | the ONE registry consumer: α = 1/N_max as the tick | **HELD** with the bracket above |
| T2623, T2624, T2543, T2629 rows | — | quote the tick as the timing sentence / the push as the norm step; none says "push rate" | no hold needed; T2629 already states the question OPEN |
**Finding:** the α clause is UNREGISTERED — it exists in K1860-N as an identification and in two hashed working files, and reaches the registry only through T1136's α = 1/N_max. So "BST predicts α drift" would rest on an unregistered clause on top of an unregistered fourth link (Bergman ≠ Szegő). That is what Cal C4 should weigh before the word "predicts."

— Grace
