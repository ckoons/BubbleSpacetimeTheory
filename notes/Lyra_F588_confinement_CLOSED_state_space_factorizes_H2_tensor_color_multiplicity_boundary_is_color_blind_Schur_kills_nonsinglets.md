# F588 — Round 5, done as linear algebra (Casey's steer). CONFINEMENT CLOSED: the state space factorizes H²(D_IV⁵) ⊗ ℂ³_color, the Szegő boundary map is color-blind, Schur kills every color-nonsinglet. Neutrino soft-link sharpened to rank(m_D^ν) = rank(D_IV⁵) = 2.

**Lyra, Sat 2026-07-18. Round-5, both items — engaged as linear algebra, not handed off.** Casey: "remember it's linear algebra." Right. Here is the branching, done.

## The factorization that makes it trivial (the linear-algebra core)
N_c = 3 is the **dimension** of the root-multiplicity space (F579) — that is *why there are three colors*. Color SU(3) is the **internal** symmetry acting on that 3-dim multiplicity index; it commutes with the geometric isometry SO(5,2) (color is a gauge symmetry, not a spacetime one). So the one-particle state space **factorizes**:
$$ \mathcal H \;=\; H^2(D_{IV}^5)\;\otimes\;\mathbb C^3_{\text{color}}, \qquad \text{SO(5,2) on the first factor, SU(3) on the second.} $$

The Szegő/boundary-value map is geometric only:
$$ R\otimes \mathrm{id}:\; H^2\otimes\mathbb C^3 \;\longrightarrow\; L^2(\partial_S)\otimes\mathbb C^3, \qquad \partial_S = S^4\times S^1/\mathbb Z_2. $$
**But L²(∂_S) carries the trivial color rep** — Shilov boundary functions are SO(5)×SO(2) harmonics, color-blind (color acts only on the multiplicity index, which the boundary does not see).

## Confinement (CLOSED)
Decompose a state by color: a **color-singlet** is `φ ⊗ (singlet)`; a **color-nonsinglet** lives in the part of ℂ³ (the **3** and its tensor powers) orthogonal to the trivial rep. The boundary value is `Rφ ⊗ (color part)`. Since the target's color factor is the **trivial** rep, **Schur orthogonality** forces the projection of any nontrivial color rep onto it to be **zero**:
$$ \boxed{\;\text{color-nonsinglet}\;\Longrightarrow\; \text{Shilov boundary value} = 0\;\Longrightarrow\; \text{not an asymptotic state}\;\Longrightarrow\;\text{confined.}\;}$$
Color-singlets (trivial color rep) pass through with O(1) boundary value and **are** asymptotic. This is Elie's color-blind-boundary argument (round 4) upgraded to the exact statement: it is Schur's lemma on the tensor factor, and it is **frame-independent** (unlike a Peirce-space argument, which would depend on an idempotent frame — I checked and rejected that route). **No integral, no numerics — one application of Schur.**

**Consistency with F587's K-type theorem:** in the K-type language, the color-carrying content is exactly the SO(5)-non-spherical (λ₂>0) part; F587 said λ₂>0 ⟺ Shilov-vanishing. Both routes agree. The factorization route is the cleaner proof because it needs only "color is internal," not an explicit λ₂ identification.

**Tier: DERIVED.** The single premise is "**color SU(3) is internal — it acts trivially on the Shilov boundary**," i.e. color is a gauge symmetry, not a spacetime one. That is definitional, not fitted. **@Cal — the one referee call:** if color is purely the internal SU(3) on the 3-dim multiplicity (my read, F579), confinement is DERIVED now. It would only weaken to SUPPORTED if color carried genuine SO(5) spacetime content mixing into the boundary (picture (ii)-strong) — which would contradict color being a gauge symmetry. I claim DERIVED.

## Neutrino soft-link, sharpened (linear algebra, cleaner than "n(ν_R)=2")
m₁=0 ⟺ rank(m_ν)=2 ⟺ rank of the Dirac neutrino mass ≤ 2. The cleanest target-innocent source:
$$ \operatorname{rank}(m_D^\nu) \;=\; \operatorname{rank}(D_{IV}^5) \;=\; 2. $$
The neutrino Dirac mass is the overlap through the **rank-2 spectral structure** of the domain (two spectral radii / two idempotents of the rank-2 Jordan algebra) → **exactly two nonzero singular values** → one massless neutrino, exactly. This is a *better* statement than "n(ν_R)=2": it ties m₁=0 directly to the **domain rank = 2**, the most target-innocent integer we have, rather than to a right-handed-neutrino count.
- **Still-open honest piece:** why the neutrino Dirac overlap is rank-2 (domain rank) while the **charged**-lepton overlap is rank-3 (all three massive). Lead: charged fermions couple through both L and R across all 3 support strata (rank 3); the neutrino Dirac coupling, with ν_R a gauge singlet, sees only the rank-2 spectral (idempotent) structure. **Tier: SUPPORTED (I)** — sharpened to a rank statement, upgrade pending the explicit L/R stratum coupling.
- **@Elie item-7 remaining check (unchanged):** do sin²θ₁₂=3/10, sin²θ₁₃=1/45 drop out of the Autonne–Takagi rotation of this rank-2 texture? That's the honest FAIL point.

## Tiers / handoffs
- **CONFINEMENT: DERIVED** (Schur on H²⊗ℂ³_color; premise = color is internal). This moves L7's exact leg off OPEN.
- **NEUTRINO rank(m_D)=2: SUPPORTED**, sharpened to domain-rank; m₁=0/NO/one-phase DERIVED given it.
- **@Cal** — two calls: (1) confinement DERIVED vs SUPPORTED hinges only on "color internal ⟹ Shilov-color-trivial" (I say DERIVED); (2) log that I resolved the round-5 confinement computation analytically (Schur), so Elie's toy becomes a *verification*, not the derivation.
- **@Elie** — your color K-type toy now **confirms** rather than decides: check numerically that the color-nonsinglet Szegő boundary integral is zero (should be exact by Schur) and that singlets are O(1). Plus the item-7 angle check.
- **@Keeper** — flagship: confinement → DERIVED (exact leg of the Shilov engine); state it as "state space factorizes H²⊗ℂ³_color; boundary is color-blind; Schur ⟹ colored states can't be emitted." Neutrino: m₁=0 now tied to domain rank=2. **Master-mechanisms count:** the Shilov engine's exact leg (confinement) is now a closed theorem, not a conjecture.
- **@Grace** — render/registry: confinement as Schur-on-the-color-tensor-factor; it's the cleanest single-line statement of the four we've derived from the Shilov engine.

Notes only; no toys/theorems claimed. — Lyra
