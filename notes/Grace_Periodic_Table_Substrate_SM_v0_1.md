---
title: "The Periodic Table of the Substrate Standard Model — v0.1"
author: "Grace"
date: "2026-05-29 Friday 08:38 EDT (date-verified)"
status: "v0.1 — first rendering of the 5-tuple taxonomy as a periodic table. Every cell flagged DERIVED vs ASSIGNED (Keeper discipline). The 5-tuples are hand-assigned pending Lyra's canonical Hall basis — that is what turns this from a labeling into a theorem."
purpose: "Casey-named deliverable: show how all SM particles work and are constructed from the substrate. Gaps = Five-Absence predictions (Mendeleev-style)."
---

# The Periodic Table of the Substrate Standard Model — v0.1

**Coordinate system (the 5-tuple)**: every SM fermion = (Region × σ_BF × Chirality × Charge × Winding-mode W_n).
- **Rows (periods) = W_n = generation** — count = h(B₂) − 1 = 3. *No 4th row* (chain terminates).
- **Columns (groups) = (Region × σ_BF × Charge-sublattice)** — the four fermion families.
- **Bosons** = coupling operators (the Hall-algebra *multiplication*), a separate block — they connect cells.

**Reading the flags** — D = DERIVED from substrate structure; A = ASSIGNED (hand-placed 5-tuple, awaiting Lyra's canonical basis to become derived).

## The fermion table (3 rows × 4 family-columns)

```
              CHARGED LEPTON      NEUTRINO            UP-QUARK (×N_c col)   DOWN-QUARK (×N_c col)
              Shilov/σ_BF-chg     Shilov/σ_BF-triv    Bulk/+2/3             Bulk/−1/3
              Q=−1                Q=0                                       
─────────────────────────────────────────────────────────────────────────────────────────────
GEN 1  W_0    e⁻                  ν_e                 u                     d
              m_e (scale anchor)  ~0 (σ_BF-trivial)   m_u ≈ rank²·m_e?      m_d ≈ N_c²·m_e?
              region D, 5-tuple A region D, 5-tuple A region D, mass A      region D, mass A
─────────────────────────────────────────────────────────────────────────────────────────────
GEN 2  W_1    μ⁻                  ν_μ                 c                     s
              m_μ/m_e=(24/π²)^c_2 Δm²_21 ≈ N_c·c_2    m_c/m_u≈rank²·N_c·g²  m_s/m_d ≈ 2π²
              ratio D, mech A     PREDICTED A         lead (scheme) A       INVARIANT D-ish
─────────────────────────────────────────────────────────────────────────────────────────────
GEN 3  W_2    τ⁻                  ν_τ                 t                     b
              m_τ/m_e=g²·Ogg71    (σ_BF-trivial)      m_t/m_c≈rank³·Ogg17   m_b/m_d≈g·M_g
              ratio D, mech A     PREDICTED A         lead (scheme) A       lead (scheme) A
─────────────────────────────────────────────────────────────────────────────────────────────
```

**Per-row substrate reading**: each generation is one winding-mode value W_n; the charged-lepton/neutrino pair share W_n and differ by σ_BF (parity); the quark families differ by region (Bulk) + charge-sublattice + carry N_c=3 colors. The Higgs (below) is the operator that *moves between rows* — mass generation = cross-winding-mode coupling.

## The boson block (coupling operators = Hall multiplication)

| Boson | Coupling type | Connects | Flag |
|---|---|---|---|
| **γ (photon)** | within-region σ_BF | same-region charge transitions | framework A |
| **8 gluons** | within-bulk SU(N_c) | bulk color transitions (N_c=3) | framework A |
| **W±, Z** | cross-region chiral | Bulk ↔ Shilov (β-decay) | framework A |
| **Higgs** | cross-winding-mode | row ↔ row (mass generation) | framework A |

In the Hall-algebra reading (team synthesis): multiplication = vertices, coproduct = emission/multi-particle, R-matrix = scattering, grading = conservation laws. **This block becomes derived when the full Hall algebra is built** (Lyra Phase 0) — until then, framework-assigned.

## What is DERIVED vs ASSIGNED (the integrity ledger)

**DERIVED from substrate structure:**
- Row count = 3 = h(B₂) − 1 (Coxeter; conditional on generation-forcing closing)
- N_c = 3 colors = h^∨(B₂) (dual Coxeter)
- Region split bulk/Shilov = ρ-vector (ρ₁=n_C/rank bulk, ρ₂=N_c/rank Shilov)
- Per-generation charge sum = 0 (anomaly cancellation from Bergman boundary continuity)
- Lepton mass-RATIO *forms* (T190, T2003) — derived values; the winding *mechanism* is framework
- m_s/m_d = 2π² scheme-invariant (forward)

**ASSIGNED (hand-placed, awaiting Lyra canonical Hall basis to become derived):**
- Which specific K-type ↔ which specific particle (the 5-tuple labels)
- The chirality (L/R) assignments
- The winding-mode → generation identification (matched, not forced)
- The absolute mass scale (m_e itself)
- The cross-tier quark mass-ratio forms (scheme-dependent leads)

**The v0.1 → theorem path**: Lyra's canonical basis for the full Hall algebra assigns each indecomposable module to a particle *by derivation*. When that lands, the ASSIGNED flags flip to DERIVED and the table becomes a theorem, not a labeling.

## The table's predictions (gaps = Five-Absence, Mendeleev-style)

- **No 4th row** — no 4th generation (chain terminates at h−1=3; the affine B̂₂ tube count is the test)
- **No σ_BF beyond {trivial, charged}** — no sterile neutrinos beyond the 3 σ_BF-trivial partners
- **No off-table couplings** — no GUT/proton-decay vertex, no SUSY-partner column, no extended-Higgs block
- The table is **complete and closed** — that closure IS the falsifiable content.

## Open / next

- **The decisive test (Elie E0 + the 3-tubes check)**: does the finite B₂ Hall algebra reproduce the Serre constants, and do the affine B̂₂ tubes number 3 (= generations)? If yes, the row-count and the cell-assignments become derived. If no, a clean break — also valuable.
- **Grace next**: populate exact 5-tuples per cell from Elie's Phase B K-type tables; absorb the orphaned nuclear corpus into a parallel "nuclear shell" extension of the table; keep every cell's derived/assigned flag current as Lyra's basis lands.

— Grace, Periodic Table of the Substrate SM v0.1, 2026-05-29 08:38 EDT (date-verified)
