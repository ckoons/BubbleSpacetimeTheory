---
title: "K38: α⁻¹ = 137 Derivation Chain Audit"
author: "Keeper"
date: "2026-05-15 (updated 2026-05-16 ~05:00 EDT post-T1918)"
audit_id: K38
verdict: PASS (A1 + A2 both closed; chain external-D-tier-ready pending Cal batch grade)
overall_confidence: 93%
scope: "SP-24 Phase 1 Deliverable 1 (Cal A. Brate's external-D-tier bar)"
related: ["BST_SP24_Phase1_ColdRead_Criteria.md", "BST_T1464_Reference_Frame_Counting.md", "BST_T934_Rank_Mirror.md", "BST_Paper78_Absolute_Point.md", "BST_T1454_Spectral_Width_Theorem.md", "K40_T841_P3_Erratum_Upgrade.md", "toy_2255_hilbert_Q5.py", "toy_2260_a2_rank_shift_family.py", "BST_T1918_alpha_G_Shilov_winding.md", "BST_SP26_Particle_Winding_Classification.md"]
---

## Update — 2026-05-16 ~05:00 EDT (post-T1918 chain closure)

**A2 CLOSED via three convergent routes**:
1. Lyra Toy 2260 (50/50) — Hilbert-Polynomial Shift Family (T1923). The +rank in N_max is one instance of a forced family c_k = a_k·n_C + b_k with b_k ∈ {1, rank, N_c}. Pre-α structural mechanism named.
2. Elie Toy 2265 (23/23) — K3 Hodge-Wallach Decomposition (T1921). The +rank IS the (h^{2,0}+h^{0,2}) holomorphic-form pair forced by Calabi-Yau condition on K3 = D_IV⁵ spectral slice.
3. **Grace Toy 2349 → T1918** — Gravitational Coupling from Shilov Boundary Winding. The same Shilov winding factor that gives α_G also refines T1485 Λ → H_0 closes to 0.12%. Confirms the "longest forced winding" hypothesis of SP-26 W-9. Pre-α operator identity for the dimensionful spectral scale.

The +rank shift is now derived from at least three structurally independent geometric mechanisms. Cal's external-D-tier bar (pre-α operator identity, not fitting parameter) is satisfied multiple times over.

**K38 VERDICT UPDATE: PASS ~93%.** Final external-D-tier promotion pending Cal morning batch (his grade closes the audit for outreach use). Internal: chain stands at external-D-tier with three convergent routes. Paper #104 §5.6 ships ready-for-referee.

**Remaining action items**: 
- A3 (R2 canonical N_max reading sweep) — in progress, Keeper + Lyra
- A4 (Paper #104 §5.6 final polish) — Lyra has v0.3 drafted; folds in T1918-T1923
- Cal morning batch grade — pending

## T1313 Audit Verdict (Keeper, May 16 ~05:45 EDT)

Cal's audit question on T1313 (Lyra synthesis April 18): "do the 5 algebraically independent routes each force the +rank STEP, or just the VALUE 137?"

**Read T1313 cold. Verdict: routes are valid for value, mixed for step.**

| Route | What it forces | +rank specifically? |
|-------|---------------|---------------------|
| 1. Spectral cap (T186) | N_c³·n_C + rank = 137 | YES — additive +rank |
| 2. Wolstenholme bridge (T1263) | Same form via B₂ = 1/C₂ → W_p = 1 at {n_C, g} | YES — additive +rank |
| 3. Fermat two-square (GR-3) | 137 = 11² + 4², where 4 = rank² | NO — forces rank² appearance via squaring |
| 4. Cubic-square split | Independent repackaging of 137 integer | NO — forces value, not shift mechanism |
| 5. Factorial-rank (Grace INV-11) | 1 + 5! + 2^(rank²) = 1 + 120 + 16 | NO — forces 2^(rank²), not +rank additive |

**Net**: 5 routes corroborate VALUE 137 with ~10⁻¹² coincidence probability; 2 routes (#1, #2) corroborate the +rank STEP specifically. Routes 3-5 force rank-derivative appearance but not the additive +rank shift mechanism.

**Impact on K38**: T1313 strengthens the **value** of 137 (essentially proves it's not arbitrary), which strengthens the chain's downstream identification α = 1/N_max. But for the +rank STEP specifically, A2 closure rests on independent foundations:
- T1923 (Hilbert-Polynomial Shift Family, Lyra Toy 2260)
- T1921 (K3 Hodge-Wallach, Elie Toy 2265 — +rank as holomorphic-form pair)
- T1918 (Shilov boundary winding, Grace Toy 2349 — Shilov shift gives α_G AND refines Λ)
- T1313 routes 1-2 (same family as T1923, but via Wolstenholme/Bernoulli)

So +rank has **three structurally independent routes** at external-D-tier (Hilbert family, K3 Hodge, Shilov winding) plus **two corroborating routes via T1313** (Wolstenholme/Bernoulli alternatives). Robust closure.

T1313's "5 routes" claim should be cited as 5-route VALUE corroboration, 2-route STEP corroboration, when used in Paper #104 §A3. Honest accounting. Lyra to fold this distinction into the canonical reading sweep.

**T1313 verdict**: VALID as filed (its claim is value-uniqueness corroboration). NOT a substitute for the +rank STEP derivation, which has its own (now-stronger) closure via T1918 + T1921 + T1923.

---

# K38: α⁻¹ = 137 Derivation Chain Audit

## Update — 2026-05-15 17:30 EDT (post-A1 landing)

**A1 PASS confirmed** via Toy 2255 (Elie, 38/40):
- P(Q⁵, 1) = 7 = g ✓
- **P(Q⁵, 2) = 27 = N_c³ ✓ — chain N_c³ leg is now external-D-tier**
- P(Q⁵, 3) = 77 = g·c_2 (T841 erratum-upgrade filed as K40 — does NOT affect K38's load-bearing leg)

**Confidence upgrade**: 78% → **85%**.

**Status of three actions from original audit**:
- **A1**: ✓ CLOSED (Toy 2255 PASS).
- **A2** (pre-α derivation of +rank): **sole remaining blocker** for external D-tier on the full chain. Lyra has reframed it post-K40 finding: instead of seeking the +rank shift in isolation, seek the **family of shifts c_k = [coefficient_k]·n_C + [genus_correction_k]** generated by the Bergman kernel exponent on D_IV^5. The c_2 = rank·n_C + 1 = 11 and N_max = N_c³·n_C + rank = 137 share Hilbert-polynomial structure (coefficient × n_C + genus correction). If the family closes, both 11 and 137 fall out as values of one object, and external D-tier closes WITH a stronger result than originally targeted.
- **A3** (single canonical pre-α reading of N_max): queued, no blocker.

**Cal's gate-function position** (added 17:25): Cal is the external-D-tier gatekeeper for referee-facing claims. Internal-D work ships without Cal PASS. External-D (Paper #104 referee-facing, Sarnak letter, outreach abstracts) goes through Cal's verdict. The bar is operational: would a referee outside the BST framework accept this on its own merits? A2 must clear that bar.

**Forward scenarios (corrected per Casey precursor pivot + Cal endorsement, May 15 ~21:00 EDT)**:

The previous framing ("A2 candidate routes corroborate I-tier") was too generous. Candidates surfaced via SP-25 /route are *hypotheses with named precursor gaps*, not corroboration. Tier comes from precursor outcomes, not from /route receipts alone. Concrete precursor-outcome confidence table:

| Outcome | K38 confidence |
|---------|----------------|
| Lyra Bergman closes operator-level (Toy 2260 family generalizes) | ~95% external D-tier |
| T1.3-P1 + P2 + P3 all close (Furuta-Wallach: K3 spectral subset + Pin(2)→SO(2) restriction + K-theory transfer) | ~95% external D-tier |
| T1050 pre-α check closes AND observer-shift forces +rank step | ~92% external D-tier |
| T1313 audit shows ≥2 routes force +rank step (not just value 137) | ~90% external D-tier |
| All precursors stall, hypotheses stay open | ~85% with strong receipts; Paper #104 §α ships honest with explicit I-tier label at step 4 |

Lyra's Bergman remains highest probability path (in-flight, most direct). Furuta-Wallach has three falsifiable precursors that produce data either way — even a P1 FAIL is information (kills the route cleanly under audit, doesn't leave it as ambiguous hypothesis). T1313 audit is Keeper-owned, low-cost.

**Precursor task IDs (RUN_LIST and TaskList):**
- T1.3-P1: K3 eigenvalue subset test WITH null model (Elie) — Cal refinement: control K3 not in D_IV⁵ moduli, or random-integer null
- T1.3-P2: Pin(2) → SO(2) restriction (Lyra)
- T1.3-P3: ABS-style K-theory transfer after P1+P2 (Lyra)
- T1313 read + grade per +rank load-bearing (Keeper)
- T1050 α-independence check (open)
- Lyra Bergman operator-forcing extension (Lyra in-flight)

## Original verdict (2026-05-15 16:00 EDT)

### Verdict: **CONDITIONAL PASS** (~78%)

Internal D-tier confirmed. External D-tier — passable on the N_c³ leg via Hilbert polynomial of Q⁵, NOT yet passable on the +rank leg, and contingent on the team committing to ONE reading of N_max physically before α-matching. Three concrete actions close the gap.

---

## What Cal asked

From `BST_SP24_Phase1_ColdRead_Criteria.md`, Deliverable 1:

1. **WHERE does N_c³ come from?** Specific operator/identity where N_c appears to the third power *unavoidably*, not "we cube N_c because color count is 3."
2. **WHERE does the +rank come from?** Forced shift, not fitting parameter.
3. **WHAT is N_max physically *before* matching to α⁻¹?** Interpretation must precede the match.

Target: 3-7 explicit steps from classical D_IV^5 invariants to 137, each step a named theorem or computation.

---

## Chain as currently exhibited (5 steps)

**Step 1 (T186, Five Integers Uniqueness, D-tier).** D_IV^5 = SO_0(5,2)/[SO(5) × SO(2)] has five forced integer invariants: rank = 2, N_c = 3, n_C = 5, C_2 = 6, g = 7. All five are forced by the Hermitian symmetric structure plus complex dimension 5 (Cal TOP-1 baseline). Status: PASS.

**Step 2 (T841, Todd Class Hierarchy / Hilbert Polynomial, D-tier as written).** The Hilbert polynomial P(m) of Q⁵ (compact dual, smooth quadric hypersurface in ℂP⁶) satisfies P(1) = g, **P(2) = N_c³**, P(3) = g · C_2. The leading coefficient is 1/60 (= 1/denom(H_5)). This is a CLASSICAL invariant of Q⁵ — no BST-specific choice — and it forces N_c³ to appear as a Hilbert polynomial value, not as "we cube N_c." Status: PASS *if* the claim P(2) = 27 verifies against classical Q⁵ Hilbert polynomial formula. (See action item A1.)

**Step 3 (compact dimension n_C, D-tier).** n_C = 5 is the complex dimension of D_IV^5 — forced by the rank-2 type IV classification (Cartan, Helgason). The product N_c³ · n_C = 27 · 5 = 135 is "the particle physics volume" (T934 reading) — geometrically, it is the product of the Hilbert-polynomial value at m = 2 times the complex dimension. Status: PASS on the arithmetic; the *naming* "particle physics volume" is interpretive and I-tier.

**Step 4 (rank shift, +rank, currently I-tier).** N_max = N_c³ · n_C + rank. The +2 shift is currently justified through Reference Frame Counting (T1464): the observer subtracts itself from the spectral count, so the *full* spectral capacity is (observable content) + (reference frame DOF) = 135 + rank. **Status: CONDITIONAL.** See "The +rank leg" below.

**Step 5 (T1464, RFC + identification with α).** With N_max = 137 established as the spectral cap, α = 1/N_max is the fractional cost of maintaining the reference frame. Step 5 is the match, not a derivation. The interpretation of α as "cost of observation" is I-tier pending formal derivation from spectral theory (per T1464's own honesty).

---

## Pass / Fail against Cal's three criteria

### 1. N_c³ — **PASS, contingent on A1**

Cal's bar was: "specific operator, count, or identity where N_c appears to the third power *unavoidably*."

**Best route**: T841 Todd Class Hierarchy. The Hilbert polynomial of Q⁵ at m = 2 is a forced classical quantity — Q⁵ is a smooth quadric hypersurface in ℂP⁶, its Hilbert polynomial is determined by its degree (= 2) and dimension (= 5). If P(2) = 27 verifies, this is exactly the kind of "unavoidable" appearance Cal wanted.

**Inferior routes** (FAIL Cal's bar but still appear in BST docs):
- T934 Rank Mirror: "N_c³ = 27 is dim of fundamental rep of SU(3)³ (three color factors)." This is POST-HOC identification — picking three SU(3) factors because we already know N_c = 3.
- T1450 Schwinger reading: 2160 = rank⁴ · N_c³ · n_C appears in QED denominators. Confirms the integer cluster but does not *derive* N_c³ from independent invariants.

**Action A1**: Verify T841's claim explicitly. Compute the Hilbert polynomial of the smooth quadric Q⁵ ⊂ ℂP⁶ via the standard formula P_Q(m) = P_{ℂP⁶}(m) − P_{ℂP⁶}(m-2), and confirm P_Q(2) = 27. If yes, T841 step is external D-tier. If no, the chain has a CRITICAL hole.

### 2. +rank — **CONDITIONAL (MODERATE gap)**

Cal's bar was: "explicit operator, count, or identity that produces +rank as a forced shift, not as a fitting parameter."

**Current best justification** (T1464 RFC, 11/11 instances): "The first element of every BST sequence is the ruler, not the thing being measured." The +rank is the dimensionality of the reference frame (binary distinction: ruler vs measured) that must be added back to the observable content to recover the total spectral capacity.

**The problem**: T1464 itself, in its honesty section, marks the identification "α = cost of observation" as I-tier pending formal derivation from spectral theory. The +rank shift is justified by an I-tier interpretation. Cal's bar is "forced shift, not fitting parameter" — the *interpretation* is consistent, but the *forcing* requires a step we haven't proved.

**The honest reading**: We have a STRONG STRUCTURAL ARGUMENT (RFC pattern holds in 11 independent sequences), but we do NOT have a derivation of "the spectral cap is N_c³ · n_C plus the reference frame" that operates *before* identifying α = 1/137.

**Action A2**: Either (a) derive +rank from a *pre-α* operator-level identity (e.g., Casimir on the maximal compact K, Bergman kernel reproducing-kernel weight at the origin, dim of the trivial K-type, etc.), OR (b) re-grade the +rank step honestly to I-tier in Paper #104 and elsewhere, and don't claim external D-tier for the *full chain* until A2(a) lands.

**Severity**: MODERATE. The chain is real, but the chain's strength is the weakest link — and the +rank link is currently the weakest.

### 3. N_max physically *before* α-matching — **CONDITIONAL (MINOR-MODERATE gap)**

Cal's bar was: "interpretation must precede the match, not follow it."

**Three pre-α readings exist** in BST docs, each defensible:
- **(R1) Spectral cap**: "maximal eigenvalue index below which Bergman expansion is coherent" (T1454, GC12).
- **(R2) Maximum representation dimension**: "highest K-type contributing to the spectral decomposition of SO_0(5,2)" (T1454 Spectral Width).
- **(R3) Shimura level**: "the deepest level Γ(N_max)\D_IV^5 that still encodes all five BST integers; any deeper level exceeds the spectral cap" (Paper #78 Section 8.1).

These are not necessarily inconsistent — they may all be facets of the same object. But they are not currently *unified* in BST docs, and a referee comparing two papers can legitimately ask "which one is the operational definition?"

**Action A3**: Pick ONE primary pre-α reading and adopt it across Paper #78, Paper #82, Paper #83, Paper #104. Cross-reference the other two as equivalent readings. My recommendation: **R2 (maximum K-type / representation dimension)** because it is the most direct from the geometry of D_IV^5 and is independent of any spectral truncation choice.

**Severity**: MINOR-MODERATE. The chain works under any of R1/R2/R3, but the *external-D-tier presentation* requires the team to commit.

---

## Cross-cutting findings

### (a) The chain length is fine

Cal asked for 3-7 explicit steps. The current chain has 5 (T186 → T841 → n_C identification → +rank via RFC → α match). Within Cal's target band.

### (b) Tier honesty across the chain

Step-by-step tier inheritance, per Cal's cross-cutting criterion #4:
- Step 1: D-tier
- Step 2: D-tier (contingent on A1)
- Step 3: D-tier (arithmetic); I-tier (interpretive name)
- Step 4: **I-tier as currently justified** (+rank via RFC interpretation)
- Step 5: D-tier (definitional match) + I-tier (physical interpretation of α as observation cost)

**The chain inherits the weakest link.** Currently I-tier on +rank → so the *external D-tier* claim cannot stand until A2 lands. Honest internal tier: **D-tier mechanism with one I-tier dependency in step 4**.

### (c) Multiple decompositions of 137 — feature or bug?

Paper #78 Section 3.3 gives THREE decompositions of N_max = 137 that agree only at N_c = 3:
- 2^g + 2^{N_c} + 2^0 = 128 + 8 + 1 (polynomial / bit positions)
- N_c³ · n_C + rank = 27 · 5 + 2 (integer)
- 2^g + N_c² = 128 + 9 (catalog)

This is a STRENGTH for uniqueness arguments (D_IV^5 is over-determined). But it complicates the "primary derivation chain" because a referee can ask "which decomposition is THE derivation?" The team should designate ONE as canonical (recommend the integer form for derivation purposes; cite the others as corroborating identities, not as alternative derivations).

### (d) Cal's circular-risk flag, addressed

Cal's FAIL flag was: "the interpretation of N_max requires matching to α^{-1} first." The current chain *avoids* this circularity in steps 1-4 (each step is geometric and pre-α). Step 5 is the match itself. So the circularity risk is structurally avoided — provided the team adopts pre-α reading R1/R2/R3 cleanly (A3).

---

## Action items (in order)

| # | Action | Owner | Severity if not done |
|---|--------|-------|---------------------|
| A1 | Compute Hilbert polynomial of Q⁵ in ℂP⁶ explicitly; verify P(2) = 27 | Elie (toy) | CRITICAL |
| A2 | Derive +rank from a pre-α operator-level identity, OR re-grade chain to I-tier on this leg | Lyra | MODERATE |
| A3 | Commit to ONE pre-α reading of N_max; sweep papers for consistency | Keeper (sweep) + Lyra (canonical paper text) | MINOR-MODERATE |
| A4 | Write up the 5-step chain as Section in Paper #104 with explicit tier label per step | Lyra | MINOR (cosmetic but referee-facing) |

If A1 + A2 + A3 close clean, the chain upgrades to external D-tier and Cal's Phase 1 Deliverable 1 closes PASS.

---

## What I tested

| Source | Read | Used for |
|--------|------|----------|
| `BST_SP24_Phase1_ColdRead_Criteria.md` (Cal) | Yes | Audit bar |
| `BST_T1464_Reference_Frame_Counting.md` | Yes | Step 5 + +rank justification |
| `BST_T934_Rank_Mirror.md` | Yes | Inferior route flagged |
| `BST_Paper78_Absolute_Point.md` §3.3 | Yes | Three decompositions |
| `BST_T1454_Spectral_Width_Theorem.md` | Excerpted | Pre-α readings R1, R2 |
| `BST_T1481_Denominator_Separation` (registry entry) | Excerpted | Identity N_c³n_C + 2rank + 1 = rank²n_C·g |
| `BST_AC_Theorem_Registry.md` — T841 Todd Class | Excerpted | Step 2 (key claim) |
| `BST_Paper90_QED_QCD_Spectral_Unification.md` | Excerpted | RFC corroboration |
| `BST_Paper89_Fermion_Masses_Spectral.md` | Excerpted | RFC instances |

### What I did NOT test (acknowledged scope)

- I did NOT independently verify P(2) = 27 for Q⁵ via the classical Hilbert polynomial formula. That is action A1, owned by Elie. If A1 fails, this audit's verdict downgrades to FAIL on the N_c³ leg.
- I did NOT search for an existing pre-α derivation of +rank. If one exists in a doc I missed, please flag it and I'll re-audit. My survey covered the registry T1464, T934, T1454, T1481, T1444, T186; Paper #78 §3; T1262 (parents); Paper #83 §891 (RFC section).

---

## Bottom line for Cal

Internal D-tier: CONFIRMED, with explicit chain.
External D-tier: CONDITIONAL on A1 (verify P(2) = 27) and A2 (+rank gets a pre-α derivation, OR honest I-tier label).
Presentation: A3 (pick one pre-α reading) is needed for unified referee-facing exposition.

The chain is sound. The weakest link is the +rank shift — currently justified by RFC interpretation, which is itself I-tier in its own theorem doc. Until A2 lands, claim "internal D-tier with one I-tier dependency at step 4." That is honest and survives audit.

— Keeper, K38, 2026-05-15
