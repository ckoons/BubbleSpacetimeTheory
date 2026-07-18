# F585 — L5: CKM texture forcing. The texture is the overlap matrix between the 3 support strata; √(mass-ratio) mixing is forced because mass and mixing are the same localization width read diagonally vs off-diagonally.

**Lyra, Sat 2026-07-18. L5 (frontier → consolidation).** Forces the CKM *structure* (not new magnitudes) from the support-flag geometry. Honest split of DERIVED vs STRUCTURAL below. Grace renders on landing.

## The forcing statement
Each generation i localizes at support stratum i of rank-2 D_IV⁵ (bulk / Cartan-slice / Shilov, F86). The Yukawa comes from a **single Higgs condensate** O (rank-1 texture M_ij = O_i O_j, mixing arc). The mass matrix entries are **overlap integrals** of the localized generation wavefunctions ψ_i against the condensate:
$$ M_{ij} \;=\; \langle \psi_i \,|\, O \,|\, \psi_j\rangle. $$
- **Diagonal** M_ii = |⟨ψ_i|O⟩|² sets the **masses** — the localization width w_i at stratum i.
- **Off-diagonal** M_ij (i≠j) sets the **mixing** — the overlap *between* strata i and j.

Because both are the same Gaussian-like overlap in the same width variable, the off-diagonal is the geometric mean of the diagonals:
$$ M_{ij} \sim \sqrt{M_{ii}\,M_{jj}} \;\Rightarrow\; \theta_{ij} \sim \sqrt{m_i/m_j}. $$
This is the **Gatto–Sartori–Tonin / Fritzsch texture**, and here it is *forced*: mixing = √(mass ratio) is not fitted, it is the statement that the same localization width controls both diagonal and off-diagonal overlaps. **The texture zeros / hierarchy come from the stratum separation** (bulk–Cartan overlap ≫ Cartan–Shilov overlap ≫ bulk–Shilov), which orders |V_us| > |V_cb| > |V_ub| automatically.

## What is DERIVED vs STRUCTURAL (honest)
- **DERIVED (mechanism):** rank-1 single-condensate Yukawa → Gatto texture → mixing = √(mass ratio). The *form* is forced.
- **DERIVED (value):** **V_us = √(m_d/m_s)** — the first off-diagonal, the cleanest (adjacent strata bulk–Cartan). Matches obs.
- **STRUCTURAL (I/S):** **V_cb** — right form (√(m_s/m_b)-scale, Cartan–Shilov), magnitude sits near/just below the naive floor; the ρ-vector direction cos ψ = n_C/√(n_C²+N_c²) = 5/√34 (F384) is the geometric read but the precise coefficient is structural.
- **STRUCTURAL (S):** **V_ub** — second-neighbor overlap (bulk–Shilov), smallest, most suppressed; magnitude named weak. The *ordering* (smallest) is derived; the number is not.
- **CP phase / Jarlskog:** the single complex phase of the condensate O propagates into one physical CKM phase (parallel to the neutrino one-Majorana-phase count, F584). Structural.

## Why this "completes" L5 (clean statement, not a new number)
The frontier ask was "force the texture." The texture *is* forced — it is the overlap matrix of the 3-stratum support flag against one condensate, and √(mass ratio) is the necessary consequence of one width controlling both diagonal and off-diagonal. The remaining openness is **magnitude precision of V_cb/V_ub**, which is the same Tier-2 structural floor that limits all mass/mixing observables (Two-Tier hypothesis) — not a gap in the mechanism. Reporting the DERIVED/STRUCTURAL split honestly = completion by the "clean negative counts" standard.

## Handoffs
- **@Grace** — render on landing: CKM texture as the 3×3 stratum-overlap matrix, with the √(mass-ratio) off-diagonals and the |V_us|>|V_cb|>|V_ub| stratum-separation ordering. Pairs with the PMNS g-organized render (F564) — same overlap-matrix machinery, different flag population (neutrinos skip Shilov, F584).
- **@Cal** — the DERIVED claim is *form only* (Gatto from rank-1) + V_us; V_cb/V_ub are STRUCTURAL. Don't let a render imply the magnitudes are derived.
- **@Keeper** — bank L5 as the texture-forcing consolidation; the shared "overlap-matrix-of-the-support-flag" mechanism now covers BOTH CKM (F585) and PMNS (F564/F584) — one machine, two sectors.
