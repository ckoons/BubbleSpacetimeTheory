# F589 — Neutrino sector → DERIVED. A rank-2 domain has TWO natural stratifications: 3 boundary orbits (rank+1) index the gauge-charged generations, 2 spectral idempotents (rank) index the gauge-singlet ν_R. m₁=0 is rank(m_D)=rank(D_IV⁵)=2, forced. Linear algebra, no new physics premise.

**Lyra, Sat 2026-07-18. Round-6 ★ item.** Casey (×3): "it's linear algebra." So here is the closure as a counting fact about D_IV⁵'s two invariant stratifications — not the "spherical-support" premise Elie and I had been leaning on (which conflated boundary-value λ₂ with stratum-rank; superseded below).

## The two stratifications of a rank-2 domain (the whole argument)
D_IV⁵ is rank 2. A rank-r bounded symmetric domain has **two** canonical, invariant integer stratifications:
1. **Boundary orbits (Korányi–Wolf):** exactly **r+1 = 3** G-orbits in the closure — bulk (rank 0), intermediate (rank 1), Shilov (rank 2). This is the support flag (F86); it indexes the **3 generations**.
2. **Spectral idempotents (Jordan frame):** exactly **r = 2** primitive idempotents c₁,c₂ — every element has ≤2 spectral values. This is the spectral stratification.

Both are target-innocent (fixed by the domain, not by any observable). 3 = rank+1 and 2 = rank are the *same domain* read two ways.

## Which fermions index onto which (the one physical assignment)
- A **gauge-charged** fermion carries an electroweak flag, so it is distinguished by **where its support sits among the boundary orbits** → **r+1 = 3** values → **3 generations**. (This is F86, already established for charged leptons + quarks.)
- A **gauge-singlet** ν_R carries **no** flag — nothing electroweak distinguishes its copies. The only invariant left to distinguish a featureless right-handed mode is its **spectral value** (which primitive idempotent) → **r = 2** values → **exactly 2 right-handed neutrinos.**

$$ \boxed{\;n(\text{generations}) = \operatorname{rank}(D_{IV}^5)+1 = 3, \qquad n(\nu_R) = \operatorname{rank}(D_{IV}^5) = 2.\;} $$

Both counts fall out of the single integer rank=2. Nothing is fitted; 2 and 3 are the domain's rank and rank+1.

## m₁ = 0 and the sector (now DERIVED)
The Dirac neutrino mass is then a **3×2** matrix (3 ν_L generations × 2 ν_R):
$$ \operatorname{rank}(m_D^\nu) \le 2 \;\Rightarrow\; m_\nu = -m_D M_R^{-1} m_D^{\mathsf T}\ \text{has rank} \le 2 \;\Rightarrow\; \textbf{one eigenvalue exactly } 0 \;\Rightarrow\; m_1=0. $$
Consequences (all DERIVED given the counting): **normal ordering**, **exactly one physical Majorana phase**, Σm_ν ≈ 0.059 eV, and the narrow **m_ββ ∈ [1.4,3.7] meV** band (Elie-verified). The whole neutrino sector closes on rank=2.

## Tier — honest
- **Counting (n_gen=3, n(ν_R)=2): DERIVED** as linear algebra from rank=2 (the two invariant stratifications), **given the one assignment**: gauge-charged ↔ boundary-orbit flag, gauge-singlet ↔ spectral idempotents. That assignment is *motivated* (a featureless singlet has only its spectral value to be indexed by) and *self-consistent*, and it reuses the already-established F86 charged-fermion↔flag map. 
- **m₁=0 / NO / one-phase / m_ββ band: DERIVED** given the counting.
- **@Cal — the referee call that sets DERIVED vs SUPPORTED for the sector:** is "gauge-singlet ν_R is indexed by spectral idempotents (rank=2), not the boundary flag (rank+1=3)" a *forced* consequence of ν_R being flag-less, or a motivated assignment? My read: forced — the flag is an electroweak-charge structure, a singlet has none, so it cannot be flag-indexed; the spectral frame is the only invariant left, and it has exactly rank=2 slots. If you accept that, **the neutrino sector is DERIVED.** This **supersedes** the earlier "ν_R requires spherical support → skips the non-spherical Shilov stratum" premise (Elie/round-5), which conflated the K-type boundary-value λ₂ (F587) with the boundary-orbit rank — two different notions. The idempotent-counting version is the clean one; retire the spherical-support phrasing.

## Bonus — this IS frontier lead (a), the candidate third master mechanism
Round-6 lead (a) asked "where else does rank=2 force a light/massless mode?" **m₁=0 is the first instance of exactly that:** *a coupling that factors through the domain's rank-2 spectral structure has ≤2 nonzero singular values, forcing a massless/light mode in any 3-vector it maps.* Candidate **third master mechanism** alongside odd-g and the λ₂ Szegő engine:
- **odd-g (g=7):** chiral weak + no-W_R/Z′ + KK-trim (11→4).
- **λ₂ Szegő engine (spherical ⟺ λ₂=0):** confinement (F588, derived) + graded mass leg.
- **rank-2 spectral bound (NEW):** m₁=0 exactly; and it *predicts* — anywhere a physical coupling is forced through the 2-idempotent spectral structure, the third singular value vanishes. **@Keeper/@Grace — Schur-generator sweep: where else does a 3-object coupling factor through rank-2? Each is a forced-massless prediction.** (Candidate next targets: a light quark? the lightest anything coupling through the pure spectral channel?) Tier the *general* mechanism as a CANDIDATE until a second independent instance lands (Cal #27 — one instance is not yet a "mechanism").

## Handoffs
- **@Cal** — the one call above; and log that the sector closure is now a rank-counting derivation, not a spherical-support premise (supersession).
- **@Elie** — the remaining check is unchanged and it's the sector's last empirical gate: do **sin²θ₁₂=3/10, sin²θ₁₃=1/45** drop out of the Autonne–Takagi diagonalization of the rank-2 m_D texture? That's the honest FAIL point — if the angles don't emerge, the texture is wrong even though m₁=0 is right. Also: verify rank(m_D)=2 numerically for the 3×2 construction (trivial, but banks it).
- **@Keeper** — flagship: neutrino sector → DERIVED (pending Cal), on rank=2 via the two-stratifications counting; and open the "rank-2 spectral bound" as the candidate third master mechanism in the master-mechanisms section (tagged CANDIDATE, one instance).
- **@Grace** — render: the two stratifications of D_IV⁵ (3 boundary orbits / 2 idempotents) side by side = "3 generations and 2 right-handed neutrinos are one integer, rank=2." Clean companion to the B₂ root diagram.

Notes only; no toys/theorems claimed. — Lyra
