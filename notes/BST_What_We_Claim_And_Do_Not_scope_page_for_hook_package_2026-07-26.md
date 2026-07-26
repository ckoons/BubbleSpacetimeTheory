# What BST Claims — and Does Not

*A scope statement, meant to be read first. BST derives Standard Model physics from a single geometric object, the bounded symmetric domain D_IV⁵. This page draws the boundary between what is proved, what is matched-but-not-proved, and what is neither claimed nor solved — because the boundary is what makes the rest worth reading. Every claim below can be checked against a runnable toy in the repository; the tiers are not asserted, they are auditable.*

*(Keeper draft for the Tegmark hook package, 2026-07-26. The tiers reflect the state as of this date and are maintained honestly — including the walk-backs.)*

---

## How to read the tiers

Two axes, kept separate on purpose (this separation is itself the point):
- **Accuracy** — how close a computed value is to measurement. A precision fact.
- **Proof** — whether the closed form is *forced* by the geometry, or merely *matches*. An epistemic fact.

A row can be precise-but-unproven (matches to four digits, still a fit) or forced-but-imprecise (mechanism proved, sits at a percent). Conflating the two is the single most common way these programs mislead; we refuse to.

- **DERIVED** — mechanism proved, forced by the geometry.
- **IDENTIFIED** — the closed form matches, but the mechanism is absent or imported. An honest coincidence or a content-plug, not a derivation.
- **OPEN / NOT CLAIMED** — neither proved nor asserted.

---

## DERIVED (mechanism proved)

- **The gauge group SU(3)×SU(2)×U(1)** as three division-algebra structures of the one domain; **electric charge** as the integer weight of its complex-structure circle.
- **Parity violation (V−A)** — forced by the embedding dimension g=7 being *odd* (the volume element is central, locking internal to spacetime chirality). A sign forced by structure.
- **One fermion generation = the domain's 16-real spinor; three generations = rank+1.**
- **Color confinement in the precise sense (A): no free colored asymptotic states** — colored states have exactly zero boundary support (Schur orthogonality on the Shilov boundary), so they cannot be asymptotic. *(This is "no free quarks or gluons," not the area-law/mass-gap — see NOT CLAIMED.)*
- **Asymptotic freedom — the sign** — the geometry forces the color group non-abelian, and the sign of the running is the sign of the short-time spectral flow of one operator (the color-sector heat semigroup) on the one Hilbert space. *(The coefficient 11/3 is standard QFT, imported as a consistency check — not derived. See IDENTIFIED.)*
- **The PMNS "Pythagorean law"** g² = N_c²·n_C + rank² (49 = 45+4), forcing **sin²θ₁₃ = 1/45** and **|sin δ_PMNS| = 2/7** (magnitude).
- **θ_QCD = 0** (a symmetry-forced zero — the strong-CP problem) and **m_ν1 = 0** (the rank of an overlap operator).
- **The partition theorem**: every dimensionless SM observable is exhaustively either a functional of one proven measure (pinned), a characterized free modulus (a proven-finite set), or a scale-runner — with **color the proved line** between pinned and free. This is the flagship result, and it is a *map* of what the geometry fixes, not a claim that the SM is derived whole.
- **The uniqueness of the domain** under (3 colors, 3 generations, dim 5).

## IDENTIFIED (matches, mechanism absent or imported)

- **α⁻¹ = 137** (= N_c³·n_C + rank; a charge-count identification — the integer is forced, the 0.036 residual is not). *This is the Wyler result — α from a bounded symmetric domain — carried to a specific forced domain; we claim the identification and the lineage, not a proof of the exact value.*
- **Most mass ratios**: m_μ/m_e = (24/π²)⁶ (0.004%), m_τ/m_e = 49·71, m_p/m_e = 6π⁵ (0.002%) — striking matches, but proven *free* (the geometry demonstrably leaves the lepton values unfixed by the natural mechanism), so these are identified coincidences, not derivations.
- **The QCD β-function sign via content-plug** (11N_c − 2N_f = 21 > 0 with N_c=3, N_f=6) — BST supplies the integers; the 11/3, 2/3 coefficients are standard.
- **The mass-gap value** (proton = C₂·π⁵·m_e; 0⁺⁺ glueball ≈ n_C-scaled) — matches, but at the lattice's own few-percent precision, not sub-percent; the *value* is identified, the *existence of a gap* is not a Millennium construction.
- **Several mixing values** (sin²θ₁₂ = 3/10, sin²θ₂₃ = 4/7) and **sin²θ_W = 3/8** (a standard content result, not a BST-specific win).

## OPEN / NOT CLAIMED

- **The Clay Millennium problems are NOT solved as stated.** BST makes *attempts* on the same geometry — with a genuine structural result (the remaining problems reduce, in this frame, to one issue, mostly needing definitional sharpening) and specific advances (a Navier–Stokes approach; the observation that a mass gap requires curvature — flat scale-free space has no geometric gap). But "proof" is a referee-consensus with residual gaps, and BST's attempts sit at varying distance from it; **Yang–Mills specifically has a large gap** — the R⁴ interacting-QFT construction and the area-law mass-gap (the (B) notion) are the *core* of the problem and are not done. A per-problem, referee-calibrated ledger accompanies this; we do not claim the prizes.
- **The full Yang–Mills Lagrangian / induced dynamics** — a candidate mechanism, not derived.
- **Gravity and cosmology (Λ, G, H₀)** — real prior work exists; presented at structural/identified tier, not as the SM core.
- **Row-by-row "species" derivations** — several matched values (the down-quark ratio, the Gatto relations, the mixing numerators) are candidates awaiting a forced mechanism, honestly labeled.

---

## What makes this checkable (why "Physics is on GitHub")

Every DERIVED and IDENTIFIED row above corresponds to a runnable computation. A reviewer — or an AI in a loop — can:
- run `verify_bst.py` (50 predictions against measurement, 49/50 under 1%, the open cases shown openly, with the null-model context);
- run `toy_541_five_integers_to_everything.py` (51 quantities from 5 integers, 16/16);
- verify any single result: `toy_bst_explorer.py verify T187` (m_p/m_e = 1836.12 vs 1836.15).

The claims are not asked to be believed. They are asked to be *run*. That, and the honest tiering above, is the whole difference between this and the thing it will remind you of.

## The bottom line, honestly

BST does not prove the Standard Model, and it does not solve the Millennium problems. What it does is more specific and more checkable: it identifies a single forced geometric object and shows, at the tiers above, how much of physics is a reading of that one object — the derived core drawn exactly, the coincidences labeled as coincidences, the open frontier named. If that is what the mathematical universe looks like when made concrete, this is a first draft of it, kept in public, and runnable.

— Keeper, 2026-07-26. Draft for the hook package; audit-maintained. Companion artifacts: the hook paper (Lyra), the curated toy set (Elie), the SM tier-ledger (Grace).