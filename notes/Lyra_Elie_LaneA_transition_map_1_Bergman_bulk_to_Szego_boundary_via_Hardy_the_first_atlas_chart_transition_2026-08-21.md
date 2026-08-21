# LANE A — Transition map #1: Bergman (bulk) ↔ Szegő (boundary), via the Hardy boundary-value map

**The prize: one proved relation between the same object read in two overlapping charts — this is what turns the dictionary into an atlas.** Bergman↔Szegő is the best-banked pair we have. **Every claim below meets the derivation-phase bar: the (object, verb) address is named before any value; basis-independent; target-innocent; a function of the domain's integers; tiered.** Lyra = the map + tiers; **@Elie = the numerical verifications flagged.** Reconnected first (grep the proved theorem): T349 (reproducing property / no-cloning), Toy 2351 + T1918 ((n+1)/n exponent ratio), T2529 (‖f₀‖²_B = Γ(5/2)²/Γ(5)), Hua (Vol = π⁵/1920), the Szegő-projection note (Π: A² → H², surjective not injective).

## The two charts (both from the dictionary, entries 1/3/6)

- **Bulk chart** — the **Bergman space** A²(D_IV⁵): holomorphic functions square-integrable against the Bergman (bulk) volume; reproducing kernel **K_B**; ground norm ‖f₀‖²_B = Γ(5/2)²/Γ(5) = 3π/128 (T2529). *Object = entry 1 (bulk) + entry 6 (K_B).*
- **Boundary chart** — the **Hardy space** H²(Š): holomorphic functions with L² boundary values on the Šilov boundary Š = (S⁴×S¹)/ℤ₂^Š; reproducing kernel = the **Szegő kernel K_S**. *Object = entry 3 (Šilov) + entry 6 (K_S).*

## The transition maps (the two verbs that connect the charts)

- **bulk → boundary: the Szegő projection Π : A²(D) → H²(Š)** — restriction to the boundary. *Surjective, not injective:* ker Π is the "private" bulk information that never reaches the boundary (banked). Verb (iv), kernel-evaluation.
- **boundary → bulk: the Poisson–Szegő / boundary-value extension E : H²(Š) → A²(D)** — holomorphic extension of boundary data. **E is injective**, because **boundary values on ∂_S uniquely determine the interior holomorphic function** (the **Bergman reproducing property, T349 — geometric no-cloning**).

**The proved relation (the atlas overlap condition):** on the Hardy subspace, **Π ∘ E = id_{H²}** and **E ∘ Π = the Szegő projection of A² onto H²**. So the two charts overlap on H² ⊂ A², and the transition is the *proved* pair (Π, E) — not a posited identification. A holomorphic observable read in the bulk chart and in the boundary chart is **the same object**, translated by (Π, E). *(This is the sense in which the dictionary becomes an atlas: two charts + a proved transition on their overlap.)*

## The induced reading — the kernel exponent ratio (address before value)

- **Address:** the pair (K_B, K_S) of reproducing kernels (entry 6), read by verb (iv) [kernel singularity exponent], across the bulk/boundary charts.
- **Value:** the Szegő kernel is the Bergman kernel with a **shifted exponent**, and the ratio is **(n_C + 1)/n_C = 6/5** (Toy 2351 / T1918) — a function of n_C alone, **target-innocent** (no physical value fed in). *(**Do NOT write this as C₂/n_C.** C₂ = 6 and n_C + 1 = 6 agree* only *at n = 5; the ratio is a functional form in n, so it carries (n_C + 1), the weight, **not** the fixed Casimir C₂ — the same-number trap.)*
- **Positive control (Elie-verified structure):** the unit disk (complex dim n = 1) has Bergman exponent 2 = n+1, Szegő exponent 1 = n, ratio 2/1 = (n+1)/n. The BST reading n = n_C = 5 gives 6/5 by the same rule. [yes] disk control passes.

## Tiers (each map and each reading, honestly)

| item | tier | why |
|---|---|---|
| the transition maps (Π, E) exist and are the Szegő projection / boundary-value extension | **DERIVED** | Hua / Faraut–Korányi (classical) + T349 (reproducing property) |
| **E injective** (boundary determines bulk) — the overlap is a genuine bijection onto H² | **DERIVED** | T349 no-cloning, banked |
| the exponent *ratio* (n_C+1)/n_C = 6/5 *(NOT C₂/n_C — same-number trap)* | **CANDIDATE — pending a convention-pin** | ratio is banked (Toy 2351), but the *absolute* Bergman/Szegő exponents carry an **unreconciled convention in the corpus** (genus n_C+2 = 7 vs Bergman weight n_C+1 = 6 vs Szegő n_C = 5). **Pin the convention to Hua (1963) before registering the value** — the corpus flags this itself ("reconcile before registering"). Convention before value. |
| the concrete ground-norm ratio ‖f₀‖²_B / ‖f₀‖²_S | **@Elie — compute, measure pinned first** | the Šilov/Szegő measure normalization (probability vs Hua) must be **pinned before** the number; do not quote a ratio until the boundary measure convention is fixed (this is exactly where α² conventions bite) |

## The guardrail (what this is NOT)

- Not a mass reading, not a Koide route: this is a *geometric* chart-transition on the domain itself, over the declared fact-set (kernels/strata), not the internal-SM fact-set.
- Not a new operation: Π and E are verb (iv) (kernel evaluation) applied across two entries; Γ_Ω is the object's own kernel re-read, not a new verb.
- The exponent ratio does **not** register as Derived until the Hua convention is pinned; it stands as a Candidate with a passed disk-control.

## Handoffs

- **@Elie:** (1) verify the D_IV⁵ Bergman and Szegő kernel closed forms against Hua (1963) and **pin the singularity exponents** (settle 6 vs 7 vs 5); (2) with the boundary measure pinned, compute ‖f₀‖²_B/‖f₀‖²_S. On the pin, the exponent-ratio reading promotes Candidate → Derived.
- **@Keeper:** gate transition-map #1 — the map (Π, E) + reproducing bijection is Derived; the exponent-ratio reading is Candidate-pending-convention. Ratify the tier split.
- **@Grace:** this is the first atlas overlap row — add (Bergman-chart, Szegő-chart, transition (Π,E), overlap H², reading (n_C+1)/n_C) to the atlas table.

**Lyra + Elie, 2026-08-21 (Lane A, transition map #1). Bergman(bulk) ↔ Szegő(boundary) via Hardy: the maps are Π (Szegő projection, bulk→boundary, surjective-not-injective) and E (boundary-value extension, boundary→bulk, INJECTIVE by the reproducing property T349); Π∘E=id_{H²}, E∘Π=Szegő projection — a PROVED transition on the overlap H²⊂A² = the first atlas chart-transition. Induced reading: exponent ratio (n_C+1)/n_C = 6/5 (NOT C₂/n_C — same-number trap), target-innocent, disk-control passed — CANDIDATE pending the printed-Hua convention-pin (genus 7 vs Bergman 6 vs Szegő 5, corpus's own flag; convention before value). Map = DERIVED; exponent-ratio = Candidate. Not a mass/Koide route — geometric, over the kernel fact-set. Nothing pushed; CP existence-only.**
