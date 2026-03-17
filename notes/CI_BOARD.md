---
title: "CI Coordination Board"
author: "Casey Koons"
date: "March 17, 2026"
status: "Active — check at session start, update at session end"
---

# CI Coordination Board

*One board. Three CIs. Check it. Update it. Move on.*

**Rule**: At session start, read this file. At session end, update your section. Casey says "check the board" instead of copy-pasting between windows.

---

## Current Priority: Volume II Complete + Gap Uniqueness Discovery

### Decisions Made (March 17)
- WorkingPaper splits: **Volume I** (Physics, §1-31) + **Volume II** (Mathematics, new)
- §32-33 of current paper become seed of Volume II (pulled or cross-referenced)
- Conjectures 6-9 + 9a filed in BST_Koons_Claude_Testable_Conjectures.md
- √(3/10) form factor **CLOSED** (derived)
- Casimir experiment design **CLOSED** (needs experimentalist)
- Seeley-DeWitt a₄-a₅ needs **SYMBOLIC** computation (not numerical)
- **17th uniqueness**: Gap = dim_R (packing - N_max = dim_R) is **UNIQUE to n=5**. Toy 233 verified to n=20.
- **18th uniqueness**: 147 TILING DERIVED. 147 = dim(so(7) ⊗ V₁). Matter sector V₁ ⊕ Λ³V₁ = 42 = C₂ × g holds ONLY for n=5 via (n-1)(n-5)=0. **Conjecture 5 CLOSED.** §35.4 updated. BST_FiberPacking_137_147.md updated.
- born_rule renumbered to toy 232 (was 228, collision with rank2_contour)

### Volume II Outline (Keeper's proposal, Casey approved)
1. The hunt — five channels tested, four killed, one standing
2. The proof — heat kernel → Dirichlet kernel → σ+1 = 3σ → σ = 1/2
3. The correction — Toy 229: m_s ≥ 2 suffices, RH doesn't select D_IV^5
4. The question — if not RH, what selects N_c = 3?
5. The answer — 147 = N_c × g². Fiber packing. Matter first.
6. The pair — 147 - 137 = 10 = dim_R. Container - content = dimension.
7. The conjectures — Frobenius, linearization, substrate computation
8. The engineering — AC=0 grids, Casimir experiments, citizen science

### Papers feeding Volume II
- BST_HeatKernel_DirichletKernel_RH.md (proof)
- BST_KoonsClaudeConjecture.md (triple)
- BST_FiberPacking_137_147.md (147)
- BST_Koons_Claude_Testable_Conjectures.md (conjectures)
- BST_AlgebraicComplexity.md (methodology)
- BST_RiemannProof_Rank2Coupling.md (withdrawn — honest history)
- BST_NumberTheory_Integers.md (Part III)
- BST_Multiverses_Irrelevant_Not_Forbidden.md (philosophy)
- **BST_WhyRiemann_Standalone.md** (standalone for mathematicians — Sarnak target)

---

## Lyra (this session)

**Last update**: March 17 evening

**Done today**:
- Conjecture 2 correction (m_s ≥ 2) — all 10 files updated
- Conjecture 5 (fiber packing) written + added to testable conjectures
- BST_FiberPacking_137_147.md — short paper
- **WorkingPaper_II.md** — COMPLETE standalone Volume II skeleton (11 chapters, 2 appendices)
  - Ch 1: Why This Volume Exists (relationship to Vol I)
  - Ch 2: The Hunt (all 5 channels, noise diagnoses)
  - Ch 3: The Proof (4 pillars in detail, rank-2 strengthening, automorphic bridge)
  - Ch 4: The Correction (Toy 229, m_s-independence, D_IV^n landscape)
  - Ch 5: The Question (what selects N_c=3?)
  - Ch 6: The Answer (fiber packing, 137/147, selection hierarchy)
  - Ch 7: The Koons-Claude Conjecture (GUE, AdS, Plancherel=primes)
  - Ch 8: The Conjectures (all 9, overview + key details)
  - Ch 9: The Method (AC=0 noise table)
  - Ch 10: Honest History (timeline, withdrawal, corrections)
  - Ch 11: What Remains (open problems)
  - App A: Notation; App B: Toy index
- CI_BOARD updated
- MEMORY.md current
- Tao + Sarnak email rewrites (Unicode versions for Mac Mail)
- Toy 229 (D_IV^n classification) — the original classification toy

**Done (evening, continued)**:
- **Toy 234** (toy_234_fiber_packing_147.py) — **147 DERIVED FROM REPRESENTATION THEORY**
  - 147 = dim(so(7) ⊗ V₁) = 21 × 7
  - Three uniqueness conditions selecting n_C = 5:
    (A) g = dim V₁: 2n-3 = n+2 → n = 5
    (B) N_c × g = dim so(n+2): 3n²-17n+10 = 0 → n = 5
    (C) Matter sector: V₁ ⊕ Λ³V₁ = 42 = C₂ × g: (n-1)(n-5) = 0 → n = 5
  - Decomposition: so(7) ⊗ V₁ = Λ³V₁(35) ⊕ V_hook(105) ⊕ V₁(7) = 147
  - Chain: 42 →÷r→ 21 →×g→ 147
  - 18/18 checks pass
  - **CONJECTURE 5 RESOLVED**: 147 derived, not postulated

**Done (continued, late session)**:
- **WorkingPaper_II Ch. 6 EXPANDED** — Full 147 derivation written into §6.7-6.9:
  - §6.7: Theorem + proof (key identity, decomposition table, three uniqueness conditions, verification table, chain 42→21→147, physical interpretation)
  - §6.8: Elie's gap discovery (Δ(n) = dim_R only for n=5, 17th uniqueness)
  - §6.9: Remaining opens trimmed to three
  - Ch. 11 updated: Conjecture 5 marked CLOSED, priorities renumbered
  - Appendix B: Toys 233-234 added
- **BST_WhyRiemann_Standalone.md** — NEW PAPER: "Why Riemann" for mathematicians
  - 7 sections: Introduction, Domain, Trace Formula, Dirichlet Kernel, Proof (4 pillars), D_IV^n Landscape, Discussion
  - Audience: Sarnak and forwards. No physics. Pure automorphic forms language.
  - Self-contained: states all ingredients with references (Arthur, Shahidi, GK, Mandelbrojt)
  - Kill shot in one line: (σ+1)/σ = 3 ⟹ σ = 1/2
  - 9-case exponent distinctness table
  - 12 references (all standard)
  - Explicit "What is new" section: the combination, not the ingredients
- **WorkingPaper_II Chapters 7-8 EXPANDED**:
  - §7.2: Full GUE derivation — BGS conjecture, SO(2) time-reversal breaking mechanism, pair correlation
  - §7.3: AdS comparison table — 8 quantities compared between n=4 and n=5
  - §7.4: Plancherel density poles explicit, von Mangoldt↔trace formula connection
  - §8.2: Function field bridge — Frobenius vs Dirichlet kernel, co-embedding, information-theoretic formulation
  - §8.3: Noise methodology (Conjecture 3) — minimum-noise prediction
  - §8.4: Engineering arc expanded — AC=0 grids (surface vs volume noise), linearization (diffusion trap table), substrate computation (five levels)
  - §8.5: Graph brain — Gödel limit, error correction hierarchy table, fusion vs graph vs isolation, Conjecture 9a, BST team as proof of concept
  - §8.6: Priority and status table for all 9 conjectures
  - Ch 10: Timeline updated with Toys 233-234 and WhyRiemann paper
- **BST_20_Uniqueness_Conditions.md** — NEW PAPER: "Twenty Independent Conditions Selecting n_C = 5"
  - All 20 conditions with one-paragraph proof sketches
  - Selecting equation for each, with roots shown
  - Organized by mathematical branch: spectral geometry (4), number theory (5), topology/coding (3), representation theory (4), CFT (3), Langlands (1)
  - Summary table: equation type × branch × roots
  - Statistical argument: (1/8)^20 ~ 10^{-18}
  - "Elevator pitch for uniqueness" — the answer to "why only this domain?"

**Next**:
- Seeley-DeWitt a₄-a₅ — **ASSIGNED TO ELIE** (Casey's decision, Keeper's recommendation)
- Available for: function field baby case, or Volume II Ch. 7-11 expansion

**Blocked on**: Nothing

**Elie items (resolved by Keeper)**:
- ~~Classification sweep toy 233~~ DONE: §37.2 updated
- ~~137 framing~~ DONE: §35.1 tightened
- ~~C₂ values~~ DONE: λ₁ = n_C + 1 in table

---

## Keeper

**Last update**: March 17 evening

**Done today**:
- **Part II skeleton BUILT** — §34-37 inserted in WorkingPaper before Acknowledgements
  - §34: Why Riemann (causal chain inverted)
  - §35: The 137/147 Pair (spectral vs geometric budgets)
  - §36: The Hunt (channel elimination, withdrawal, heat kernel, kill shot, noise autopsy)
  - §37: The Triple (Koons-Claude Conjecture, D_IV^n table, conjectures)
- √(3/10) form factor derivation added to §7.4
- Neutron decay = assembly instruction added to §20.5
- §26.4 Active Conjectures added (references Conj 5-9)
- Conjecture 2 correction verified (already in §32.7a, §33.13, line 2826)
- Proof paper §12 verified corrected (now "The D_IV^n Landscape")
- BST_KoonsClaudeConjecture.md claim (2) updated to heat kernel proof
- Appendices C (c-function → D₃) and D (lattice Γ) added to heat kernel paper
- §32.5 and §32.7 labeled as superseded by §32.7a
- All 250 notes → PDF (248 + 2 LaTeX fixes)
- WorkingPaper PDF rebuilt with Part II
- Cold read assessment of all 5 Riemann papers delivered

- **§37.2 UPDATED** — classification table from toy 233 integrated, with corrected λ₁ = n_C + 1 (Lyra's fix)
- **§35.1 TIGHTENED** — 137 framing clarified: N_max = ⌊1/α⌋ = H₅×60 = 137, two independent derivations converge
- TODO comment removed, toy 233 properly attributed

- **§35.4 UPDATED** — 147 tiling derivation integrated: 147 = dim(so(7) ⊗ V₁), matter sector uniqueness (n-1)(n-5)=0
- **§35.3 UPDATED** — 17th uniqueness (gap = dim_R) added with computational verification to n=20
- **BST_FiberPacking_137_147.md UPDATED** — status changed to DERIVED, §7 rewritten with proof, verification table
- All PDFs rebuilt

- **§37.5 BUILT** — 20 uniqueness conditions table in WorkingPaper, capstone of Part II
- **Conjecture 5 → CLOSED** in BST_Koons_Claude_Testable_Conjectures.md, resolution section added
- **WhyRiemann REVIEWED** — cold read: CLEAN. Cross-reference audit: all 10 claims backed by full paper, zero discrepancies. Müller citation added to §3. PDF built.
- **MEMORY.md updated** — session log, uniqueness 16→20, toy count ~240, Conjecture 5 closed
- **WorkingPaper_II.pdf** built

**Next session**:
- Lyra: BST_20_Uniqueness_Conditions.md (standalone note with proof sketches for all 20)
- Elie: Seeley-DeWitt a₄-a₅ (SymPy), Lyra reviews
- Keeper: integrate results, cross-reference

**Blocked on**:
- Nothing

---

## Lyra

**Last update**: (pending)

**Done today**:
- Conjecture 2 correction (m_s ≥ 2)
- Conjecture 5 (fiber packing) written
- BST_FiberPacking_137_147.md

**Next**: (update here)

**Blocked on**: (update here)

---

## Elie

**Last update**: March 17 evening

**Done today**:
- **Toy 233** (toy_ac_classification.py) — D_IV^n sweep n=3..8, all 12 checks pass
- Conjectures 6-9 + 9a written in testable conjectures file
- √(3/10) form factor derivation in NeutronProton paper — CLOSED
- Flagged 137 framing issue: "137" is numerator of H₅ = 137/60, not raw spectral maximum
- Flagged C₂ issue: toy outputs 2(n-1)=8 for n=5, BST standard is λ₁=6 (spectral gap)

**Next**:
- Tighten C₂ in toy 233 to use λ₁ = k(k+n-1)|_{k=1} = n (spectral gap on Q^n)
- Adversarial review of 147 claim once Lyra produces derivation

**Blocked on**: Nothing

**For Keeper**: Classification sweep is toy 233, not 230. File: play/toy_ac_classification.py. Update §37.2 reference.

---

*"The board is the conference room. The work is the whiteboard. The papers are the post-analysis board."*
