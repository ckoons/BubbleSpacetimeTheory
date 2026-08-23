# The two conventions that block the mass tower — PINNED (Grace half of Lyra+Grace, K1679)
*2026-08-18. The muon (1,1) has "zero FK norm at ν=3/2" — this pins as a Wallach-edge degeneration, not a coordinate bug. Don't compute norms on the bulk formula at a reduction point.*

## The FK norm formula (primary source)
T2562 states the Kostant Dirac is self-adjoint in **G_λ ∝ 1/(ν)_λ**, with the type-IV FK generalized Pochhammer
> **(ν)_λ = (ν)_{λ₁} · (ν − a/2)_{λ₂},   a = n_C − 2 = N_c = 3,   a/2 = 3/2.**

(Faraut–Korányi, *Analysis on Symmetric Cones*, Ch. VII — the Gindikin gamma / generalized Pochhammer of a type-IV cone, indexed by a **partition** λ = (λ₁ ≥ λ₂ ≥ 0).)

## Pin 1 — PARTITION, not Dynkin
The Pochhammer is indexed by **partition row-lengths** λ₁, λ₂ (each row length feeds one rising-factorial factor). So **"(1,1)" is the partition (1,1)** → (ν)₁·(ν−3/2)₁ = ν(ν−3/2). Reading (1,1) as **Dynkin labels** points at a *different* SO(5) irrep (Dynkin (1,1) = the 16, vs partition (1,1) = the 10) and gives the wrong norm. **Every K-type label fed to (ν)_λ must be in partition coordinates.** This is the collision that has bitten us repeatedly this week (the "(1,0)" vector-vs-spinor collision was the same class).

## Pin 2 — the muon IS at ν = 3/2 (and that is a reduction point, not a mistake)
- **ν = 3/2 confirmed** from the primary strata pin: T2517 (charged-lepton addresses ν = {5/2, 3/2, 0} = {n_C/2, N_c/2, 0}); muon = N_c/2 = 3/2.
- **T2554:** ν=3/2 = the **Wallach EDGE** = (r−1)a/2 = rank-1 Korányi–Wolf orbit = **the last discrete point before the continuous spectrum.** T2528: muon ν=3/2 → support-orbit rank **ℓ=1**.

## The resolution — the zero is the edge, use the degenerate-module norm
At ν=3/2 the second factor **(ν − 3/2)_{λ₂} = 0 for any λ₂ ≥ 1** — the a/2 = 3/2 shift lands the second Pochhammer *exactly on its reduction point*. So the "zero FK norm" is the **Wallach-edge degeneration**, not a coordinate error, and the generic **bulk** formula (ν)_λ is simply the *wrong norm* at an edge module.

| lepton | ν | stratum (KW) | ℓ (T2528) | norm to use |
|---|---|---|---|---|
| electron | 5/2 | bulk (Wallach continuum) | 2 | **generic FK (ν)_λ** — well-defined |
| muon | 3/2 | **edge** (rank-1 orbit) | 1 | **degenerate-module (Wallach-point) norm** — NOT the bulk (ν)_λ |
| tau | 0 | vertex (Shilov) | 0 | **ℓ=0 boundary-measure norm** (bulk Γ(0)=∞ pole, T2528) |

**Only the electron sits on the generic Pochhammer.** The muon and tau are at reduction points; their norms are the reduced unitary structures of the degenerate modules.

## Instruction for the rung run (unblocks Elie)
1. All K-type labels in **partition** coordinates before touching (ν)_λ.
2. Do **not** plug (1,1), ν=3/2 into the bulk (ν)_λ — that 0 is the artifact of the bulk formula at the edge.
3. Compute the muon on the **Kostant-Dirac image (1,1) → (3/2,½)** (the spinor tensor shifts the label *off* the reduction point — this is exactly why Casey pinned the muon as (1,1)→(3/2,½)), or equivalently on the rank-1 degenerate-module norm.
4. Then the (k,m) rung selection + norms is one short computation on a **well-defined** coordinate.

*(Lyra owns the other half — the tensor↔spinor translator / Kostant-Dirac shift that carries (1,1)→(3/2,½) explicitly, and the (k,m) rung selection. This note pins only the FK-norm coordinate.)*

---

## Addendum (K1680) — THE BERGMAN WEIGHT FORK: genus-5 leptons vs Wallach-3 quarks (pulled, not fit)
The one number that opens the mass tower is the **weight** the FK norm carries. It is a real fork, forced by color:

**Bergman genus of D_IV⁵:** p = (r−1)a + b + 2 = (n_C−2) + 2 = **n_C = 5** (Hua 1963 — a fixed fact of the domain, not a fit).

| sector | color | lives in | **weight** | primary signature |
|---|---|---|---|---|
| **leptons** | singlet (T2527) | ⚠ **CORRECTED 2026-08-23 — was "full scalar Bergman space H²(D_IV⁵)"; that is H²_{λ=0} and a lepton cannot live there.** See the correction block at the foot of this file. | **genus p = n_C = 5** | Γ(n_C)=Γ(5)=**24** (muon's (24/π²)⁶); electron anchor ‖f₀‖²=Γ(5/2)²/Γ(5)=**3π/128** EXACT |
| **quarks** | triplet (T2521) | **V₁₂⊗ℂ = ℂ³** color bundle | **Wallach thresh. ν = N_c = 3** | (N_c)_k ladder (3)₁:(3)₃:(3)₅ = **1:20:840** (d:s:b, T2513) |

**Why the fork is forced (pull, not fit):**
- ⚠ **STEP BROKEN 2026-08-23.** ~~Color singlet ⟹ scalar section of the trivial color bundle = an ordinary holomorphic function on D_IV⁵ ⟹ its norm is the full Bergman norm at the genus weight p = n_C = 5 (Hua).~~ **The inference conflates two senses of "scalar": trivial in the COLOR factor, and trivial as a K-type. Color-singlet forces the first and says NOTHING about the second.** A lepton is a color singlet **and a spinor**; it lives in **H²_{λ=Δ}**, not H²_{λ=0}. *(H²_{λ=0} carries only K-types (k_harm, 0) — integer, one nonzero row — so it contains no spinor at all.)*
- **Color triplet ⟹ section of the V₁₂ color bundle** ⟹ confined → interior lowest rung = the FK **Wallach/TIR threshold ν = N_c = a = 3** (T2513, the FK object's forced singular point).

⚠ **THIS RESOLUTION IS WITHDRAWN AS STATED.** It rested on the broken step above. **T2513's gate (b) is OPEN again** unless the genus-5 weight is re-derived for the spinor bundle. **The NUMBER is not retired — only its reason is.** *(Standing rule: when the reason is wrong, do not assume the number is wrong too; re-derive before replacing.)*

**⟹ Elie's muon run (one short computation):** genus-**5** (n_C) Bergman weight, on the Kostant-Dirac image **(3/2,½)** (off the ν=3/2 edge), partition coordinates, read m_μ/m_e (target (24/π²)⁶ = Γ(5)-driven; falsifier has teeth — m_μ/m_e is a known number).


---

## ⚠ CORRECTION BLOCK — 2026-08-23 (Grace, own file, own error)

**Flagged in R72's by-the-object sweep as a real λ-crossing, and it is mine.**

### The error
Line 45 placed leptons in the *"full **scalar** Bergman space H²(D_IV⁵)"*. **"Scalar" was doing two jobs in one word:** *trivial in the color factor* (which color-singlet does force) and *trivial as a K-type* (which it does not). **H²_{λ=0} carries only K-types (k_harm, 0) — integer, one nonzero row — and therefore contains no spinor.** A lepton is a color singlet **and a spinor**, so it lives in **H²_{λ=Δ}**.

### ★ And this file already knew — it contradicted itself on 08-18
Its own last line sends Elie's muon run to *"the Kostant–Dirac image **(3/2, ½)**."*

> **(3/2, 1/2) is a SPINOR K-type** — second row 1/2, half-integer in both rows. It is exactly Δ ⊗ V_(1,0) = V_(3/2,1/2) ⊕ V_(1/2,1/2) from the R71 decomposition.
> **So the computation was always in the spinor bundle and only the prose said scalar.** The crossing sat inside one file, five lines apart, for five days, and I wrote both lines.

### What survives, and what does not
- **SURVIVES:** color singlet ⟹ trivial *color* bundle · the quark row (triplet ⟹ V₁₂ bundle, Wallach threshold ν_strat = N_c = 3) is untouched — it never claimed scalarity · the computational target **(3/2, ½)**, which is now *confirmed* as the right kind of object rather than accidental.
- **DOES NOT:** the inference from color-singlet to *ordinary holomorphic function* · the T2513 gate (b) resolution as stated.
- **NOT RETIRED:** the genus **p = n_C = 5** weight and Γ(5) = 24. **Their justification is broken; the values are untested either way.** Re-deriving the weight for **H²_{λ=Δ}** is the open item — the SO(2) weight of the bundle shifts the measure weight, and I have not computed which way.

*Correction filed by the author. — Grace, R72*
