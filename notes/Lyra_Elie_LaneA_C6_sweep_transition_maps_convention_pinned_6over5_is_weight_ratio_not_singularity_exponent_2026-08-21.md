# LANE A under C6 — the transition-map sweep: what closes, what closes-as-projection, what doesn't

**C6 (Cal §654): report the transitions that don't close alongside the ones that do — the full sweep, not the hits.** A sweep with honest nulls is more persuasive than a handful of matches. **Headline of the bar (a method, not a check): the address is named before the value.** Every row below names its (object, verb) pair first. Reconnected/pinned first: the 2026-08-12 genus relabeling (Bergman genus = n_C = 5, Hua 1963), T1918/Toy 2351 ((n+1)/n), the discrete-series weight k = n_C+1 = 6, the λ₂>0 zero-Šilov-value (confinement engine), Harish-Chandra Plancherel.

## The convention-pin (Bergman↔Szegő) — 6/5 promotes, but as the WEIGHT ratio, not the singularity exponent

**Pinned to Hua (1963) / the 2026-08-12 relabeling — two *different* well-defined exponents:**
- **Bergman genus** (kernel *singularity* exponent) = **n_C = 5** (= dual-Coxeter h^∨(B₃)); Szegő singularity exponent = n_C − 1 = 4. **Singularity-exponent ratio = 5/4.**
- **Bergman-space discrete-series weight** k_B = **n_C + 1 = 6** (A²(D_IV⁵) = holomorphic discrete series π₆, Harish-Chandra); Hardy/Szegő weight k_S = **n_C = 5**. **Weight ratio = (n_C+1)/n_C = 6/5.**

**⇒ the banked "6/5 = Bergman/Szegő kernel exponent ratio" (T1918) is the *weight* ratio, mislabeled "kernel exponent."** Corrected (superseded-not-deleted): **6/5 is the discrete-series WEIGHT ratio k_B/k_S = (n_C+1)/n_C**; the *singularity-exponent* ratio is separately **5/4** (genus n_C=5 / n_C−1=4). **Both stay CANDIDATE — the numbers wait for Elie's read of the printed Hua (1963) page**, not this corpus-derived weight argument (reconnect to the *primary source* before promoting; the corpus label was itself wrong, so the corpus is not the authority here). **Write each ratio as its labeled pair — (n_C+1)/n_C for the weight, n_C/(n_C−1) for the singularity — never "C₂/n_C"** (C₂ = 6 and n_C+1 = 6 agree only at n = 5; same-number trap). Target-innocent (functions of n_C), disk control passed. *(Convention-before-value: the number may be right, but it promotes on the printed page, not on a corpus that mislabeled it.)*

## The C6 sweep — every candidate transition among the four decompositions, tiered

| transition (chart ↔ chart) | verb / map | closes? | tier | induced reading (address → value) |
|---|---|---|---|---|
| **Bergman(bulk) ↔ Szegő(boundary)** | Π (Szegő projection) / E (boundary-value ext.) | **YES** (Π∘E=id_{H²}, E injective by T349) | map **DERIVED**; weight-ratio & singularity-ratio **CANDIDATE** (pending printed Hua) | (K_B, K_S) → weight ratio (n_C+1)/n_C = 6/5, singularity ratio n_C/(n_C−1) = 5/4 |
| **Cartan slice ↔ K-type** (KAK) | Harish-Chandra (τ-spherical) transform | **YES** (Plancherel isomorphism) | **DERIVED** | (K-type λ) → its radial eigenvalue on A = **C₂(λ)** (Casimir ↔ radial-Laplacian eigenvalue) |
| **K-type ↔ Šilov stratum** (Korányi–Wolf) | boundary restriction | **closes as a PROJECTION with a kernel** | **DERIVED-structure** | a K-type reaches the Šilov boundary iff **λ₂ = 0**; K-types with **λ₂ > 0 have zero Šilov value** (the confinement / m₁=0 engine) — the kernel is the confined sector |
| **bulk ↔ Šilov stratum** (direct) | — | **NO** — does not close directly | (null) | must **factor through** the boundary-value map (Bergman↔Szegő); there is no direct bulk→stratum transition that isn't the composite. Reported as a null. |
| **Peirce block ↔ Cartan slice** | — | **NO clean map** — different decompositions | (null) | the Jordan frame (c₁,c₂,V₁₂) and the KAK flat A are not related by a proved transition on an overlap; a naive identification fails the property test (they coincide only at the base point). Reported as a null. |

**Two of five close, one closes-as-projection, two are honest nulls.** The nulls are the point of C6: bulk↔stratum only closes as the Bergman↔Szegő *composite* (not a new map), and Peirce↔Cartan has no proved transition (I tested the property — a shared base point is not a chart overlap — not mere existence; the new rule).

## The trace-normalization soft joint (Cal's flag) — why trace-normalization, given no unification

The answer is **separability**: the hypercharge normalization is a **trace over End_K = ℂ⊕ℍ⊕ℝ that factorizes over the census blocks**, and the **ℝ color block contributes zero** (U(ℝ) is 0-dimensional). So the trace is effectively over the **electroweak part ℂ⊕ℍ alone** — it **does not mix the color block in**, hence needs **no unification** to be well-defined. Trace-normalization is right *precisely because* the census is block-diagonal and color is separable: you normalize hypercharge by a trace that never sees color. "It's what NCG does" is replaced by "the census trace factorizes and color drops out" — a reason internal to BST's own structure, consistent with the no-unification headline.

## Tiers / C6 status

- Bergman↔Szegő: **map Derived**; the two ratios ((n_C+1)/n_C = 6/5 weight, n_C/(n_C−1) = 5/4 singularity) stay **Candidate pending printed Hua** (label corrected from "kernel exponent"; never "C₂/n_C").
- Cartan↔K-type: Derived (Casimir ↔ radial eigenvalue).
- K-type↔stratum: Derived-structure (projection; kernel = λ₂>0 confined sector).
- bulk↔stratum, Peirce↔Cartan: **honest nulls, reported** (C6).

## Handoffs

- **@Elie:** confirm the Szegő singularity exponent = n_C−1 = 4 against Hua's Cauchy–Szegő formula (settles the 5/4); confirm the Hardy weight k_S = n_C = 5. On confirmation the two ratios (6/5 weight, 5/4 singularity) both register cleanly.
- **@Keeper:** gate the label correction (T1918's "6/5 = kernel exponent ratio" → "weight ratio"; superseded-not-deleted) and the sweep tiers; ratify the two nulls as reported nulls, not gaps.
- **@Grace:** add the three closing/projecting transitions + the two nulls to the atlas table (C6 — nulls in the same table as the hits).

**Lyra + Elie, 2026-08-21 (Lane A, C6 sweep). Convention DIAGNOSED (not yet pinned to the printed page): 6/5 is the discrete-series WEIGHT ratio (k_B=n_C+1=6 / k_S=n_C=5), the singularity-exponent ratio is separately 5/4 (genus n_C=5 / 4) — BOTH stay CANDIDATE pending Elie's read of printed Hua (1963); the "kernel exponent ratio" label (T1918) corrected. Write each as its labeled pair, never "C₂/n_C" (same-number trap, agree only at n=5). Sweep of all five candidate transitions among the four decompositions: Bergman↔Szegő and Cartan↔K-type CLOSE (Derived); K-type↔stratum closes as a PROJECTION with kernel = the λ₂>0 confined sector; bulk↔stratum and Peirce↔Cartan are HONEST NULLS (reported, C6 — tested the property, not existence). Trace-normalization answered by separability: the census trace factorizes, color (ℝ) drops out, no unification needed. Address named before value throughout. Nothing pushed; CP existence-only.**
