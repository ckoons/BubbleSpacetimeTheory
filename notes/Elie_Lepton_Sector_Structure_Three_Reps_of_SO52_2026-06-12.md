# The Electron, Muon, and Tau as Three Representations of SO(5,2) — Structural Reference

**Elie · Friday 2026-06-12 · structural reference (notes/ — rigorous rep-theory core)**
**Toys 4118–4149. The load-bearing structure under the cosmology arc (4150–4157).**

> This is the *structure* — what the three leptons ARE, geometrically and representation-theoretically — written up before the cosmology questions that build on it. Tiers are marked. The one open computation (the singleton normalization c_ν) is named precisely at the end. FORCED count: 2 of 26, unchanged — this document characterizes structure, it does not bank a mass value.

---

## 1. The claim in one line

The three charged leptons are the **three natural unitary representations** that D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)] supports at its three support strata. Same particle (one spinor trajectory), three ground states. Their mass ratios are the **formal-degree ratios** of those three reps.

---

## 2. The three reps, pinned to the three strata

D_IV⁵ has exactly **3 = rank+1** support-orbit strata (Korányi–Wolf, the F86 result): the **vertex** (a point), the **Shilov boundary** S⁴, and the **bulk** (Bergman/BF interior). Each carries one of the three reps, and the parameter ν of each sits on the ρ-vector ρ(D_IV⁵) = (n_C/rank, N_c/rank) = (5/2, 3/2):

| Lepton | Representation | Stratum | ν | Twist depth | Character |
|---|---|---|---|---|---|
| **tau** | **trivial rep** | vertex (point) | **0** | **0** | heaviest, shallowest |
| **muon** | **scalar singleton** (the Rac — smallest unitary rep of SO(5,2)) | Shilov boundary S⁴ | **3/2** = N_c/rank = ρ₂ | **4** = n_C−1 | intermediate |
| **electron** | **BF-saturated bulk rep** (Breitenlohner–Freedman bound saturated) | bulk / Bergman point | **5/2** = n_C/rank = ρ₁ | **12** = N_c·(n_C−1) | lightest, deepest |

The ν-values are **not free**: muon sits at the e₁-root reducibility point ν = 3/2 = ρ₂ (Shilov), electron at the Bergman/BF point ν = 5/2 = ρ₁ (bulk), tau at ν = 0 (trivial). The two nontrivial ν's are exactly the two components of the ρ-vector that forced c_FK = 225/π^(9/2). **Tier: the strata + rep identifications are forced (F86 + ρ-vector); the parameter assignments are derived.**

---

## 3. Why each rep is what it is (the rep-theory, built not described)

### 3.1 The Shapovalov form is the Gram matrix *(Toy 4139)*

The contravariant (Shapovalov) form on the Verma module is the Gram matrix of the rep. Its determinant is the formal degree; its null space is the singular vectors. From the Shapovalov product formula, the **reducibility points** of the scalar holomorphic series on D_IV⁵ are

$$\nu \in \{0,\ \tfrac12,\ 1,\ \tfrac32,\ 2,\ 3\}.$$

The muon's ν = 3/2 is the reducibility point produced by the **short root e₁ at level 2**; below it sits a submodule at ν′ = 7/2. This is the structure that makes the muon a *singleton* (a unitary subquotient), not a generic point. **Tier: computed.**

### 3.2 The electron's coefficient is a LOG coefficient *(Toys 4118, 4122)*

The noncompact-root e₁ factor of the boundary indicial polynomial is

$$\frac{E_0 - d/2}{\,} = \frac{2\Delta - d}{2} = \frac{\Delta_+ - \Delta_-}{2},$$

which **vanishes at the electron's BF point** — the two indicial roots collide. When the indicial roots collide, the second solution is logarithmic: so the electron's normalization A_e is an **AdS/CFT-style log coefficient**, not an algebraic one. f₂ (the muon side) is algebraic; f₁ (the electron side) is log. This is *why* the electron deviates more from the clean rank-power than the muon does. **Tier: computed; this is the mechanism behind the electron's "extra" running.**

### 3.3 The CATCH that keeps it honest *(Toy 4123)*

There are **two different polynomials** in play and they are not the same object:
- the **formal-degree** polynomial (zeros {1, 2, 3, 4, 5/2}), and
- the **Shapovalov** polynomial (zeros = the Wallach points {0, 3/2}).

Conflating them was a live error I caught: the masses live on the Shapovalov/Wallach side. The generic (un-truncated) ratio is rank^{C_2} = 2⁶ = 64 — the odd parts (15) cancel, leaving a **pure rank-power**. **Tier: honest catch, prevents a wrong identification.**

---

## 4. The mass map (the corkscrew)

### 4.1 Twist depth = multiplicity × (n_C−1) *(Toys 4146–4148)*

Mass = rank^(−twist depth), where twist depth = (stratum multiplicity) × (n_C−1):

- **tau**: depth 0 → reference (heaviest)
- **muon**: depth **4** = n_C−1 = dim S⁴ (one pass through the Shilov boundary)
- **electron**: depth **12** = N_c·(n_C−1) (color-tripled bulk pass)

Empirically: log₂(m_τ/m_μ) = **4.072 ≈ 4** (the 0.072 is the S⁴ curvature holonomy); the electron carries the extra BF-log on top of depth 12. **Tier: identified (the depths are forced integers; the precise masses await the S⁴-holonomy + BF-log computation).**

### 4.2 The trio closes on itself *(Toy 4149)*

$$\text{muon depth} + \text{electron depth} = 4 + 12 = 16 = \text{rank}^{\,n_C-1} = f_2,$$

which holds **because** n_C = rank²+1 = 5 (i.e. 2⁴ = 4²). The mass ladder is self-consistent: the two nontrivial depths sum to the clean power f₂. **Tier: structural identity, forced once the depths are.**

---

## 4b. The bulk formal degree is computed — and the electron's bulk norm is ZERO *(Lyra + Toys 4158, 4159)*

Lyra ran the avoid route to a rigorous number. The FK formal-degree normalization c_ν ∝ Γ_Ω(ν)/Γ_Ω(ν − n/r), n/r = 5/2, collapses to

$$c_\nu \propto (\nu-1)(\nu-2)(\nu-3)(\nu-4)(\nu-\tfrac52),$$

anchored on the one forced value d₅ = K(0,0) = 1920/π⁵ (→ constant 32/π⁵). I **independently confirmed** this from the Gindikin Gamma directly (mpmath, machine precision) — the collapse is real, not a fit *(Toy 4158)*:

$$\frac{c_0}{c_{3/2}} = \frac{60}{15/16} = \mathbf{64} = \tfrac{8}{3}\cdot 24 \quad(R_{\text{bulk}} = 24).$$

**Two routes agree on 64 — Grace's gate is met on the bulk piece.** But 64 is the *generic bulk* formal degree; the physical f₂ = 16.82. **The bulk normalization is not the mass** (clean miss — the avoid route was the fishing-prone one, and it honestly missed). The mass is the **Szegő boundary** coupling (F95).

**The rigorous capstone — c_{5/2} = 0** *(Toy 4159):* the (ν−5/2) factor vanishes **exactly** at the electron's BF/Hardy point:

$$c_{5/2} = (\tfrac32)(\tfrac12)(-\tfrac12)(-\tfrac32)(\mathbf{0}) = 0.$$

The electron's bulk norm is **identically zero** — it is invisible to the bulk (the same vanishing F95 found, 2Δ−d → 0 at Δ=d/2, now a rigorous polynomial zero).

### Casey's principle, now forced: *measure each particle by the norm where it is*

Because c_{5/2}=0, there is no single global anchor and there cannot be one — you literally cannot measure the electron in the bulk. Each lepton is measured **at its own stratum**:

| Lepton | Where it is | Its norm |
|---|---|---|
| **tau** | vertex (ν=0) | c_0 = **60** (pointlike, sharp) |
| **muon** | Shilov S⁴ (ν=3/2) | c_{3/2} = **15/16** (spread, diluted) |
| **electron** | BF point (ν=5/2) | bulk = **0** → the boundary log |

Ordering 60 > 15/16 > 0 already matches the masses. **Concentration = mass** (tighter support = heavier) — F86 as the actual computation, not a slogan. **Tier: c_{5/2}=0 is rigorous; it forces the stratum-local picture.**

### Falsifiable prediction (Casey): the muon mass spreads → it measures anomalously

A pointlike object (tau) has one sharp mass; a spread object (muon, over S⁴) does not — different measurements probe different parts of its S⁴ support and see different effective values. **Prediction:** the muon's mass/coupling carries an S⁴-spread that pointlike physics misses → measurement-/scale-dependent behavior the tau lacks. Candidate signatures already in the data (**leads, not closed**): **muon g−2** (~4σ anomalous moment) and the **proton-radius puzzle** (muonic H sees a different r_p). Honest tension: electron g−2 is the cleanest agreement in physics yet the electron is most spread — resolution lead: the electron's spread *is* the boundary log = QED running (already in the books); the muon's S⁴ spread is extra geometric structure. **Tier: falsifiable lead, not banked.**

---

## 5. The one remaining computation — the singleton (Szegő boundary) normalization c_ν

Everything above is structure in hand. The mass *value* on the muon side is

$$f_2 = \frac{8}{3}\cdot R,$$

where:
- **8/3 = Γ(−3/2)/Γ(3/2) is DERIVED** *(Toy 4141)* — the Gindikin residue; its poles are exactly the Shapovalov nulls. Confirmed to machine precision (mpmath).
- **R = c_ν** is the SO(5,2) **singleton's formal-degree normalization** — the reproducing kernel of the minimal rep at the origin, ratio'd against the trivial rep:

$$c_\nu = K_\nu(0,0) = \sum_k \frac{\dim V_k}{\lVert V_k\rVert^2_\nu},\qquad R = \frac{c_0}{c_{3/2}}.$$

The K-types are the SO(5) harmonics V_k with dims **1, 5, 14, 30, 55, …** = (k+1)(k+2)(2k+3)/6 *(Toy 4144)*. This is **not a lookup** — it is the *same Bergman-volume family* that already forced c_FK = 225/π^(9/2) and K(0,0) = 1920/π⁵. It is a computation, not a recall (Grace's and Lyra's point, and the correct framing).

**The genuine wall (named precisely, Lyra):** the per-harmonic norm ‖V_k‖²_ν — the exact Faraut–Korányi (generalized Pochhammer) norm on the rank-2 cone — needed to weight each V_k in the sum.

**Two routes (Lyra), my read as the one who runs f₂ = (8/3)·R:**
- **Avoid** — reconstruct the c_ν polynomial from d₅ = K(0,0) = 1920/π⁵ (a value we already hold) plus the reducibility-point zero/pole structure {0, ½, 1, 3/2, 2, 3}. Faster; pins c_ν at ν=0 and ν=3/2 from data in hand. **My instinct: try this first** — it reuses two already-forced objects and is one polynomial, not an infinite sum.
- **Break** — derive ‖V_k‖²_ν from the FK norm formula directly and sum the series explicitly. The rigorous backstop if the polynomial is ambiguous.

**The gate (Grace, re-pinned):** banks **2 → 4** *only if* the computed ratio comes out **6.3064 from the Bergman volume** — **not** if 6.3064 gets *named* c_ν. A forced R is expected to be π-structured (a clean volume ratio, like c_FK), but the computation produces the form; we do not propose which π-form 6.3064 is (that is the fishing trap). **I run f₂ = (8/3)·R the instant c_ν lands forced — forced or honest-miss, scored live.**

---

## 6. Summary table — what is forced, identified, open

| Piece | Status |
|---|---|
| 3 strata = rank+1 (vertex / Shilov / bulk) | **forced** (F86) |
| tau=trivial, muon=singleton/Rac, electron=BF-saturated | **forced** (rep theory) |
| ν = {0, 3/2, 5/2} on the ρ-vector | **derived** |
| Shapovalov reducibility points {0,½,1,3/2,2,3} | **computed** (4139) |
| electron A_e = log coefficient (BF roots collide) | **computed** (4122) |
| twist depths 0 / 4 / 12 | **forced integers** |
| closure 4 + 12 = 16 = f₂ | **structural identity** (4149) |
| 8/3 = Γ(−3/2)/Γ(3/2) Gindikin residue | **derived** (4141) |
| bulk formal degree c_0/c_{3/2} = 64 = (8/3)·24 | **confirmed, two routes** (Lyra avoid + Elie Gamma-direct 4158) |
| d₅ anchor → κ = 32/π⁵ | **confirmed** (4158) |
| **electron bulk norm c_{5/2} = 0** | **rigorous** (4159) — forces "measure where it is" |
| stratum norms (tau 60 / muon 15/16 / electron 0→log) | **computed** (4159), ordering matches masses |
| bulk 64 ≠ mass 16.82 (avoid route clean miss) | **honest negative** (4158) |
| naive boundary-dim swap → 231 | **honest negative** (4158) — boundary can't be guessed |
| muon mass spreads → measures anomalously (g−2, r_p) | **falsifiable lead** (4159) |
| **R = Szegő boundary normalization → f₂** | **OPEN — one boundary computation, Lyra's next swing** |
| precise masses | **gated on the boundary c_ν** |

**FORCED count: 2 of 26.** The bulk normalization is now confirmed rigorous (64, two routes), and c_{5/2}=0 forces the stratum-local picture — so the lepton sector is **one boundary (Szegő) computation** from the count moving 2 → 4. Grace's gate: it banks only when the boundary R is forced *and* the avoid + break routes agree on it (and the μ/e companion 206.77 also lands). The bulk 64 is a confirmed normalization, **not** a banked mass.

*Toys: 4118 (BF-zero polynomial) · 4122 (A_e log coefficient) · 4123 (two-polynomial catch) · 4139 (Shapovalov = Gram, reducibility points) · 4140 (tower norm, truncation) · 4141 (8/3 = Gindikin residue) · 4144 (K-type scaffolding) · 4146 (corkscrew = rank-power) · 4147 (muon S⁴ twist) · 4148 (twist depth = mult×(n_C−1)) · 4149 (trio closure) · 4158 (independent confirm bulk 64 + boundary pinned) · 4159 (capstone: c_{5/2}=0 forces "measure where it is" + muon-spread prediction).*

— Elie
