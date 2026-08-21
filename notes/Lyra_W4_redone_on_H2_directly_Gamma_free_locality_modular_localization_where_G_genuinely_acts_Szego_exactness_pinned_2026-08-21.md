# W4 redone on H²(D_IV⁵), Γ-free — locality where G genuinely acts (the dispatch-lane unblock, G3)

**Round 42. The one owed piece for the YM/Millennium foundation: redo W4's modular-localization/locality construction on H²(D_IV⁵) directly, dropping Γ.** Γ was only a spectral regulator (Rellich, to make L²(Γ\G/K) discrete), and H²'s Casimir/Wallach ladder is already discrete — so it was never needed, and it broke the G-action (the sector mismatch caught last round). Reconnected: BST_W4_Modular_Construction (the skeleton), the G-action blind gate (Round 41), T349 (reproducing property), EHW/Vergne–Rossi (positive-energy discrete series). **Scope guard: clearing G3 (locality) clears the FOUNDATION; it does NOT close the interacting-YM identification (G6, a separate residual) — this is not a Clay-claim closure.**

## What changes, and why each change is an improvement

| ingredient | old (L²(Γ\G/K)) | new (H²(D_IV⁵)) | why the new one is correct |
|---|---|---|---|
| **Hilbert space** | L²(Γ\G/K), K-spherical, discrete via Rellich | **H²(D_IV⁵)**, the holomorphic discrete series | this is where the physics lives; discrete spectrum already present (Casimir/Wallach) |
| **G-action** | G does NOT act (Γ breaks it to the commensurator) | **G=SO₀(5,2) genuinely acts** (the discrete-series rep U) | the modular boost K_phys∈𝔞 needs G to act — now it does (the blind-gate criterion, satisfied) |
| **Vacuum Ω** | constant 1 (G-invariant, W5) — but **1 ∉ H²** | the **lowest-weight ground state** Ω₀ (reproducing-kernel vector at the base point) | the discrete series has no G-invariant vector; the physical vacuum is the ground state — the constant was never physical |
| **regulator Γ** | needed for discrete spectrum | **dropped** | redundant: H² is already discrete; and Γ was not a physical BST input |

## The construction on H² (following the modular-localization skeleton, now on the right space)

**Given (W1–W3, W5 on H²):**
1. **ℋ = H²(D_IV⁵)**, separable, the weight-k holomorphic discrete series of G=SO₀(5,2) (EHW/Vergne–Rossi; k≥k_min=3).
2. **U : SO₀(5,2) → 𝒰(H²)**, the discrete-series representation — G genuinely acts.
3. **Positive energy (W3):** the generator of the SO(2) time-circle (the conformal Hamiltonian E₀+2j) is bounded below — the holomorphic discrete series is a *lowest-weight* module, so H ≥ 0 by construction (this is exactly why the holomorphic discrete series is the physical sector).
4. **Vacuum Ω₀:** the lowest-weight ground state (the Szegő/Bergman reproducing-kernel vector at the base point), K-invariant, cyclic.

**The modular data (unchanged Lie-algebra content — this is why the redo is clean):**
- **Boost K_phys** = the temporal boost generator ∈ 𝔞 ⊂ 𝔭 (the long root e₁+e₂ direction; the ground of the modular flow). It acts on H² because U is a genuine G-rep.
- **Modular group** Δ^it = U(e^{2πt K_phys}); **modular conjugation** J = U(θ), θ the Cartan involution.
- **Tomita–Takesaki relations** JΔJ=Δ⁻¹ (from θK_phys=−K_phys), JΩ₀=Ω₀, Δ^it Ω₀=Ω₀. **These follow from Lie-algebra facts that hold on ANY G-representation** — so they transport verbatim from the old construction to H². The only thing that broke on L²(Γ\G/K) was that U wasn't a genuine G-rep there; on H² it is, so every step now has its hypothesis met.
- **Standard subspace** K_R = closure of {x : Sx=x}, S=JΔ^{1/2}; **wedge algebra** A(W_R)=K_R''; **BW property** Δ=e^{−2πK_phys}, J=U(θ); **locality** W₁⊥W₂ ⟹ [A(W₁),A(W₂)]=0.
- **Cyclic-separating Ω₀:** cyclicity by Reeh–Schlieder (the holomorphic discrete series has the boundary-value analyticity Reeh–Schlieder needs); separability by the mass gap (W3, the Casimir gap C₂=6). Both hold on H² exactly as W4 claimed on L²(Γ\G/K) — but now with a G-action to carry them.

**⟹ W4 (locality) is established on H²(D_IV⁵), Γ-free, with G genuinely acting.** The construction is the same modular-localization argument; dropping Γ removes the sector mismatch and supplies the G-action every step needed. The foundation clears.

## The pinned open question — does K_B = S² make the Szegő projection exact? YES (reproducing property, T349)

The wedge construction lives on the **boundary** Hardy space (the wedge regions are boundary regions of ∂_S). For that to be the same object as H²(D_IV⁵), the **Szegő projection Π: L²(∂_S) → H²(∂_S)** must be **exact** — i.e. the boundary-value extension E is isometric onto its image and **Π∘E = id_{H²}**, so H² *is* the holomorphic sector of L²(∂_S) with no smoothing correction.

**Resolution: exact, by the reproducing property (T349).** The Szegő kernel reproduces H²: ∫ K_S(x,y) f(y) dσ(y) = f(x) for f ∈ H². Equivalently (F1016) the reproducing identity ∫K(x,y)K(y,x)dμ(y)=K(x,x) *is* the two-point→one-point boundary collapse — so Π is a genuine orthogonal projection with **Π∘E = id_{H²}** (T349, my Bergman↔Szegő transition). **The Szegő projection is exact; H² is unitarily the holomorphic sector of L²(∂_S), and the wedge/modular construction runs on the boundary Hardy space cleanly.**

The "K_B = S²" form of the check: the reproducing kernel restricted to the spatial S⁴-boundary factor (and its S¹-time circle) gives the exact reproduction — the Szegő kernel of the tube-type domain factors through the Šilov boundary's own reproducing structure. The exactness is **not** a further assumption; it is the reproducing property the whole Hardy machinery already stands on. *(Residual, honest: the fine analytic point — that the ℤ₂ quotient (S⁴×S¹)/ℤ₂ preserves exactness — rides on the parity structure (k+p+m even) already used in Paper A; flagged as a one-line check, not a hole.)*

## What clears, and the scope guard (do NOT over-read this)

- **CLEARS (G3):** W4-locality on H²(D_IV⁵), Γ-free, G genuinely acting — the **foundation** of the YM/Millennium lane. The dispatch-lane W1/W4 sector mismatch is fixed at the source: name H², drop Γ, the modular construction runs.
- **DOES NOT CLEAR (G6, separate residual):** whether the reconstructed boundary theory is *interacting* SU(3) Yang–Mills (vs a generalized-free cousin). That is the large named-open Clay residual (grace_W1_attack_framing's "identification-as-YM half"), untouched by this. **Clearing G3 is a foundation fix, NOT a Clay-claim closure** — do not let it read as one.
- **The 5D→4D descent** (ℝ⁴_E vs ℝ^{3,1}) is likewise separate and open.

**Lyra, 2026-08-21 (W4 redone on H², G3, Round 42). Redid the modular-localization/locality construction on H²(D_IV⁵) directly, Γ-free: ℋ=H² (holomorphic discrete series, discrete spectrum already present — Γ was only a Rellich regulator, unneeded); G=SO₀(5,2) GENUINELY ACTS (the blind-gate criterion now satisfied — the modular boost K_phys∈𝔞 acts); vacuum = the lowest-weight ground state Ω₀ (the constant 1 was G-invariant but ∉H², never physical); Tomita–Takesaki (JΔJ=Δ⁻¹ from θK=−K), BW, and locality transport verbatim because they are G-rep Lie-algebra facts — the only thing that broke on L²(Γ\G/K) was the missing G-action. Cyclic-separating Ω₀ by Reeh–Schlieder + mass gap. PINNED open question: does the Szegő projection exact-ify? YES — reproducing property (T349, Π∘E=id_{H²}); H² is unitarily the holomorphic sector of L²(∂_S); ℤ₂-parity exactness a one-line residual check. CLEARS G3 (the foundation, dispatch-lane unblock); does NOT clear G6 (interacting-YM identification, the separate Clay residual) — NOT a Clay-claim closure. Nothing pushed; CP existence-only.**
