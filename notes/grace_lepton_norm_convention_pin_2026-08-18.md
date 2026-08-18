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
| **leptons** | singlet (T2527) | full **scalar** Bergman space H²(D_IV⁵) | **genus p = n_C = 5** | Γ(n_C)=Γ(5)=**24** (muon's (24/π²)⁶); electron anchor ‖f₀‖²=Γ(5/2)²/Γ(5)=**3π/128** EXACT |
| **quarks** | triplet (T2521) | **V₁₂⊗ℂ = ℂ³** color bundle | **Wallach thresh. ν = N_c = 3** | (N_c)_k ladder (3)₁:(3)₃:(3)₅ = **1:20:840** (d:s:b, T2513) |

**Why the fork is forced (pull, not fit):**
- **Color singlet ⟹ scalar section** of the trivial color bundle = an ordinary holomorphic function on D_IV⁵ ⟹ its norm is the full Bergman norm at the **genus weight p = n_C = 5** (Hua). A lepton is not moduli-free.
- **Color triplet ⟹ section of the V₁₂ color bundle** ⟹ confined → interior lowest rung = the FK **Wallach/TIR threshold ν = N_c = a = 3** (T2513, the FK object's forced singular point).

**This resolves T2513's open gate (b)** ("colorless leptons unforced → moduli"): leptons carry the genus-5 weight, forced by Hua's genus + the color-singlet ⟹ scalar-section structure — not a chosen modulus.

**⟹ Elie's muon run (one short computation):** genus-**5** (n_C) Bergman weight, on the Kostant-Dirac image **(3/2,½)** (off the ν=3/2 edge), partition coordinates, read m_μ/m_e (target (24/π²)⁶ = Γ(5)-driven; falsifier has teeth — m_μ/m_e is a known number).
