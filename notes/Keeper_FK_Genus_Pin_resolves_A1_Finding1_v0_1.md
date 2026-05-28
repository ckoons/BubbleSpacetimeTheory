---
title: "Keeper FK-genus literature pin — resolves A1 Finding 1; corrects the three-genus convention to ONE genus"
author: "Keeper"
date: "2026-05-28 Thursday PM EDT"
status: "Resolves A1 K-audit Finding 1 (genus self-contradiction). DERIVATION-BACKED: FK genus of D_IV⁵ = n_C = 5 (FK = Hua; C_2=6 is the Casimir NOT a genus; g=7 is the embedding dim NOT a genus). OVERTURNS the morning three-genus convention's 'FK genus = C_2 = 6'. CONFIRM vs Faraut-Korányi/Loos primary source before locking into the PRIMARY paper — genus naming has flipped 3× today; pin it once against the book, stop relabeling from notes."
related: ["Keeper_KAudit_A1_PRIMARY_v0_3.md (Finding 1)", "A1 §1/§8.1/§8.4 genus claims", "Grace INV-5262 three-genus convention", "Lyra April-10 genus note", "Keeper_Genus_Verdict_T2442_Escalation_v0_1.md"]
---

# FK-genus pin — resolves A1 Finding 1

## The derivation (the authority — not my say-so; genus naming flipped 3× today)

Faraut-Korányi genus of an irreducible bounded symmetric domain: **p = 2 + (r−1)a + b** (b=0 for tube type).

**Type IV_n (Lie ball) is the tube domain over the Lorentz cone = the spin-factor Euclidean Jordan algebra** (dim n, rank r=2). Tube-type ⟹ b=0; the dimension relation n = 2 + a ⟹ a = n−2. So:

> **p = 2 + (r−1)a + b = 2 + (1)(n−2) + 0 = n.**

For **D_IV⁵ (n=5): FK genus p = 5 = n_C.** The Hua kernel exponent is also n (K ∝ Δ^{−n}, Δ the generic norm) — **Hua and FK agree for Type IV; there is no Hua=5/FK=6 distinction.** Standard genus table corroborates (Type IV_n: genus n; cf. I_{p,q}: p+q; III_n: n+1; V: 12; VI: 18). Cross-check: the rank-1 ball B^d has genus d+1 because its b-term is nonzero (non-tube-trivial) — confirming the b-term matters and is zero here.

## Conclusion — there is ONE genus, not three

| Quantity | Value | What it actually is |
|---|---|---|
| **genus(D_IV⁵)** | **5 = n_C** | FK genus = Hua genus = Bergman kernel exponent = complex dimension. They coincide. |
| C_2 | 6 | **quadratic Casimir** eigenvalue (T2435) — a representation quantity, **NOT a genus** |
| g | 7 | **embedding/signature dimension** p+q = n_C+rank — **NOT a genus** |

**So:**
- **A1 §8.1 ("n_C = Faraut-Korányi genus = 5") is CORRECT.**
- **A1 §1 / Route-A table / §8.4 ("FK genus = C_2 = 6") is the MISLABEL** — C_2=6 is the Casimir, not a genus.
- The morning's "three-genus convention" (Hua 5 / FK 6 / embedding 7) **overcounted**: it fixed the real g=7 confusion but introduced a spurious second "genus" (C_2=6). The accurate convention is **"ONE genus = n_C = 5 (FK=Hua); C_2=6 is the Casimir; g=7 is the embedding dimension — and neither C_2 nor g is a genus."**

## Honesty + the caveat (this corrects a same-day RATIFIED convention)

This **reverses** the correction I accepted this morning (Grace/Lyra-April "Hua=5, FK=C_2=6"). The genus name has now flipped three times in one day — me→Grace→me — which is itself the signal: **the team has been asserting genus conventions from internal notes instead of from the primary source.** My derivation (multiplicity formula + dimension consistency + standard table + Hua/FK agreement) is solid standard math, but because this (a) corrects a convention RATIFIED this morning (Grace INV-5262) and (b) goes into the Casey-PRIMARY paper, **confirm it once against Faraut-Korányi *Analysis on Symmetric Cones* (or Loos, *Bounded Symmetric Domains*) genus table before locking**. Then stop relabeling — pin it to the book and cite the book.

The convention-free anchor never moved: the **Bergman kernel exponent is n_C = 5** (Elie ν=5, MC). Everything here is about the *name* and the spurious second genus; the physics/exponent is unaffected, as are the Serre constants, mixing angles, ρ-vector, and c_FK.

## Fix for A1 (resolves Finding 1 → v0.4)

1. **§8.1**: keep "n_C = genus = 5" but say "FK genus = Hua genus = n_C = 5 (they coincide for Type IV)" — and cite the FK/Loos table.
2. **§1 + Route-A table + §8.4**: change "C_2 = 6 = Faraut-Korányi genus" → "**C_2 = 6 = quadratic Casimir (T2435) — not a genus**." Change the headline convention from "three genera" to "**one genus (n_C=5) + Casimir (C_2=6) + embedding dim (g=7)**."
3. **Grace INV-5262** (three-genus convention) → correct to the one-genus framing; re-issue as the standing convention.
4. **Route A unaffected in substance**: n_C=5 is still a named geometric invariant (the genus); C_2=6 is still a named invariant (the Casimir); g=7 still the embedding dim. Only the *word "genus"* on C_2 was wrong.

## Disposition

A1 Finding 1 **RESOLVED pending one book-confirmation** (genus = n_C = 5; FK=Hua; C_2 and g are not genera). The morning three-genus convention is **corrected to one-genus**. Routed: Keeper/Lyra confirm vs FK/Loos; Lyra fixes A1 §1/§8.1/§8.4 + the convention; Grace re-issues INV-5262. Once consistent → Cal cold-read → A1 v0.4 → Keeper final PASS.

This is the load-bearing fix for the PRIMARY paper, and it doubles as the lesson: pin domain invariants to the primary source once, then cite it — three relabel-flips in a day is three too many.

— Keeper, 2026-05-28 Thursday PM. FK genus = n_C = 5 (derivation-backed; confirm vs book); convention corrected to one genus; A1 Finding 1 resolved.

---

## FINAL PIN (value definitive; naming resolved; honest about what "pin" means in-environment)

Elie (Toy 3596, four independent methods), Cal (#157), and Grace all independently land on **genus = 5**. Convergent + my derivation. The pin is settled to the extent it can be, and I want to be exact about *how*, since the team is trusting me as "the one who won't guess from memory":

**VALUE — definitive (not a memory, a derivation from the definition).** The genus is *defined* by p = 2 + (r−1)a + b. For Type IV that's a derivation from the domain's known multiplicities (a=n−2, b=0, r=2), giving p = n = 5 — not a recalled table entry. Four independent routes agree (multiplicity formula, dimension consistency, convention-free Bergman exponent ν=5, Hua kernel). **Genus(D_IV⁵) = n_C = 5 is as pinned as a derivation gets.**

**NAMING — resolved: there is no real Hua-vs-FK distinction.** Both "Hua genus" (kernel exponent) and "Faraut-Korányi genus" (the p in p = 2+(r−1)a+b) denote the SAME single invariant = n = 5 for Type IV. The "FK genus = 6" was never a competing name — it was C_2 (the Casimir) mislabeled "genus." So: **one genus (5); C_2 = 6 is the Casimir; g = 7 is the embedding dimension; only the first is a genus.**

**HONEST LIMIT — what I cannot do in-environment.** I cannot physically open Faraut-Korányi *Analysis on Symmetric Cones* / Loos to confirm the literal tabulation. What I have is the FK genus *definition* (the formula) applied to Type IV's standard multiplicities — which is a derivation, stronger than a remembered value, but not a page-check. **Therefore my recommendation to A1 is to remove the dependence on the naming nuance entirely:**

> A1 should state the three invariants **by value and role**, citing the standard reference for the genus: *"D_IV⁵ has genus n_C = 5 (= complex dimension = Bergman-kernel exponent; Faraut-Korányi 1994 / Loos), quadratic Casimir C_2 = 6, and embedding/signature dimension g = 7 = p+q."* No "Hua vs FK" distinction (there is none); C_2 and g are NOT called genera.

Stated that way, A1 is correct, internally consistent, sourced, and **does not hinge on any contested naming** — which removes the entire class of risk that bit us today. A referee checking the genus formula gets 5; the paper claims exactly that.

**A1 Finding 1 — RESOLVED.** Genus pinned (value 5, one genus, state-by-value+role + cite). Combined with Lyra's v0.4 consistency sweep (the other three contradictions — kernel exponent 5/2, α placement, PMNS — all resolved per her report), A1's K-audit conditions are met. **Pending one step: I verify the swept v0.4 reads consistently end-to-end, then issue the final Keeper PASS** → Cal cold-read → submission-grade.

Standing convention correction (Grace re-files INV-5262): **"ONE genus (n_C=5) + Casimir (C_2=6) + embedding dim (g=7); intrinsic genus is always 5; C_2 and g are not genera."** The morning "three-genus" framing is retired.

— Keeper, 2026-05-28 Thursday PM. FK genus pin FINAL: value 5 (derivation-pinned, 4-way + team-confirmed), one genus, state-by-value+role + cite to dodge the naming nuance. A1 Finding 1 resolved; final PASS pending my read of the swept v0.4.
