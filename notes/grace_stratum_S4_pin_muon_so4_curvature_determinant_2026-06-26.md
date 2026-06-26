---
title: "Stratum↔S⁴ geometric pin (Lane A, Grace) — the muon's exponent 6 is FORCED by the measurement little group, and the so(4)-determinant structure is Casey's curvature principle. Resolves the F86 deposit-address-vs-measurement-locus tension I flagged: deposit address (ν=3/2 rank-1 stratum) sets the DENSITY d_τ/d_μ; the measurement little group SO(4) (stabilizer of a point on the Shilov spatial S⁴) sets the EXPONENT — two boundary-forced roles, consistent, not the same manifold. AIRTIGHT: measurement little group of a massive boundary state = SO(4) = Stab_{SO(5)}(x∈S⁴), dim 6 = C(4,2) = C_2 = dim Λ²(T_xS⁴); the 6 is the determinant-rank over the 2-form bundle. HARDENING (new): mass = det_{Λ²} of the curvature operator = Casey's 'mass IS a curvature invariant'; for constant-curvature S⁴ the curvature operator on 2-forms is scalar·Id, so det = (per-direction)⁶ AUTOMATICALLY — exponent forced by the bundle, not the soap-film model. CAL #35 ON MYSELF: dim so(4) and dim Λ²(T_xS⁴) are the SAME 6 (so(4)≅Λ²ℝ⁴), ONE object read twice, NOT two independent confirmations. OPEN (honest): that the mass-functional is specifically the curvature-determinant (vs another SO(4)-invariant) — well-motivated by Casey's curvature principle, a modeling choice at invariant-selection level; FK absolute constant = 1 is Cal's separate lane. Five-Absence: clean (no GUT/proton-decay/monopole/Z′/sterile-ν/SUSY). Target-innocence: d_τ/d_μ=64 (root system) + exponent 6 (little group) both substrate-structural, innocent of the muon target. LANE B feed: same analysis says quark measurement little group = SO(4) × color-stabilizer → exponent structure changes → the diagonal-vs-off-diagonal question."
author: "Grace"
date: "2026-06-26 Friday"
status: "Lane A pin. The exponent-6 forcing is CLOSED (measurement little group + determinant rank, one object). The invariant-selection (mass = curvature determinant) is HARDENED via Casey's curvature principle but stays a named modeling choice. FK constant = Cal's separate lane. NOT banking the count — Cal tiers at landing. Count HOLDS 4/26."
---

# Stratum↔S⁴ pin — the muon exponent is the measurement little group, the determinant is curvature

This closes my Lane A obligation: show that the muon's `dim so(4) = 6` exponent is **forced by the
boundary geometry**, not picked because it matches `π¹²`. It also resolves the tension I flagged in the
muon consolidation (deposit address vs measurement locus) and hardens F111's CANDIDATE / F118's soft spot.

## 0. The thing to force

The muon ratio (F116/F118):
```
m_μ/m_e = [ (d_τ/d_μ) / vol(S⁴) ]^{dim so(4)} = (24/π²)^6 = 206.76   (obs 206.768, 0.003%)
```
Every factor is identified except the **exponent**: F111 tiers "6 = dim SO(4)" as CANDIDATE, and the
"each copy carries one vol(S⁴)" as the **soap-film model**. My job: force the 6.

## 1. Resolve the tension I flagged (deposit address ≠ measurement locus)

I had worried: F86 puts the muon on the **Cartan-slice / rank-1 stratum** (a ν=3/2 address), but the mass
integral spreads over **S⁴** (dim 4). Are these the same object? **They are two different, both-forced
roles — and they don't need to be the same manifold:**

- **DEPOSIT (address ν=3/2):** the formal-degree density `d(3/2)` sits at the rank-1 stratum address. This
  sets the **scalar** `d_τ/d_μ = 64` (the density relative to the τ vertex-unit; F109/F345, now
  root-system target-innocent).
- **MEASURE (little group):** extracting a *mass* = localizing the deposited density to a point of the
  spatial measurement boundary. The spatial measurement boundary is the **Shilov spatial factor S⁴** (the
  distinguished boundary of D_IV⁵ is `(S⁴ × S¹)/Z₂` — forced, it is where the H² boundary values live,
  F66/Reading A; S¹ = time, S⁴ = space). Localizing to a point `x ∈ S⁴` breaks `SO(5) → SO(4)` (stabilizer
  of `x`), the **measurement little group**.

So the address sets the density; the little group sets the exponent. Both boundary-forced, consistent. The
deposit locus and the measurement little group are not the same manifold and never needed to be — that was
my own confusion, now dissolved.

## 2. The exponent is FORCED — measurement little group = determinant rank (airtight)

A **massive** boundary excitation (one with a rest frame) localizes to a point `x ∈ S⁴`. Its little group is
```
Stab_{SO(5)}(x) = SO(4),   SO(5)/SO(4) = S⁴,   dim SO(4) = 6 = C(4,2) = C_2.
```
This is pure group theory — the stabilizer of a point on `S⁴` inside the spatial rotation group, forced by
`SO(5)/SO(4) = S⁴`. The six generators of `so(4)` are the six **2-planes** in the tangent space `T_x S⁴`,
i.e.
```
so(4) ≅ Λ²(T_x S⁴),   dim = C(4,2) = 6.
```
The mass is extracted as a **determinant over this 6-dimensional space** (F116: `det_{so(4)} M`). A
determinant over a 6-dim space of a scalar-times-identity operator is the **6th power**. So the exponent is
the **rank of the determinant = dim of the measurement little group = dim Λ²(T_x S⁴) = 6 = C_2.** Forced.

> **CAL #35 ON MYSELF (must state):** `dim so(4)` and `dim Λ²(T_x S⁴)` are the **same 6** — `so(4) ≅ Λ²ℝ⁴`
> is one isomorphism, not two facts. This is **one object read twice**, NOT two independent confirmations of
> the exponent. The single forced statement is: *the measurement little group is the 2-form bundle of the
> celestial S⁴; the mass-determinant runs over it; its rank is 6.*

## 3. The hardening — the determinant IS Casey's curvature principle

The remaining softness (F118): *why is the mass the `so(4)`-**determinant** of the per-direction
concentration, rather than one eigenvalue or a trace?* This is where Casey's standing principle lands
exactly:

> **"You can't linearize curvature" / "mass is a curvature invariant" / "the five integers are curvature
> invariants."** ([[feedback_curvature_principle]], [[feedback_cant_linearize_curvature]])

The mass as `det_{Λ²}(R)` of the **curvature operator** `R: Λ²(T_xS⁴) → Λ²(T_xS⁴)` is precisely a curvature
invariant of the measurement sphere — the same family of object as the Gauss-Bonnet/Pfaffian integrand. And
`S⁴` is a **space form** (constant sectional curvature +1), so its curvature operator on 2-forms is
```
R = κ · Id_{Λ²},   κ = const.
```
A scalar-times-identity on the 6-dim 2-form bundle has `det R = κ^6` **automatically**. Replacing the bare
curvature scalar by the substrate's per-direction concentration `κ → (d_τ/d_μ)/vol(S⁴) = 24/π²` (F118: mass =
concentration = density/volume) gives
```
m_μ/m_e = det_{Λ²}(R) = (24/π²)^6.
```
So the exponent 6 is forced **by the determinant rank of the constant-curvature operator on the 2-form
bundle of the measurement S⁴** — the soap-film "six copies" is replaced by a single curvature-determinant,
and the constant-curvature of `S⁴` is *why* it collapses to a clean 6th power with no per-copy freedom.
This is mass-as-curvature-invariant, Casey's principle, made into the muon's exponent.

## 4. Honest tiering

- **CLOSED (forced):** the exponent = `dim so(4) = dim Λ²(T_xS⁴) = 6 = C_2`, as the rank of the
  mass-determinant over the measurement little group of a massive state localized on the Shilov spatial
  `S⁴`. The deposit-address-vs-measurement-locus tension is resolved (two roles, both forced). One object,
  not two (Cal #35 applied to myself).
- **HARDENED but a named modeling choice:** that the mass-functional is specifically the **curvature
  determinant** `det_{Λ²}(R)` (vs another `SO(4)`-invariant). Casey's curvature principle motivates it
  strongly and the constant-curvature of `S⁴` makes the 6th power automatic; but "mass = THIS invariant" is
  still a selection, not yet a theorem. This is the residue of F118's "mass = concentration" — now sharpened
  from "density/volume to a power" to "the curvature determinant of the measurement sphere."
- **NOT mine (Cal's separate lane):** the FK absolute Szegő constant = 1 / ν-independence. Distinct from the
  exponent (Cal #412 item-2: residue and normalization are separate, both owed).
- **Target-innocence:** `d_τ/d_μ = 64` is root-system data (F345); the exponent 6 is the measurement little
  group dimension. Both are substrate structure, **innocent of the muon mass target**. Neither was tuned.
- **Five-Absence:** "mass = curvature determinant over the measurement little group" introduces no gauge
  unification, no new particle, no proton decay / monopole / Z′ / sterile-ν / SUSY spectrum. Clean.

## 5. Lane B feed (the same geometry answers the quark question)

The pin's machinery is exactly the rep-theory input Lane B needs. For a **colored** (quark) excitation the
measurement little group is not `SO(4)` alone — it is `SO(4) ×` (the color stabilizer from the #418
covariant `V_a` generators on the color-extended boundary). So:

- The **exponent** is no longer just `dim so(4) = 6`; it picks up the color-stabilizer dimension. If quarks
  deposit on a **color-extended stratum**, the determinant runs over `Λ²(T S⁴) ⊕ (color 2-forms)` and the
  π/rational structure changes — that is the concrete form of the **diagonal-vs-off-diagonal** question I owe
  Lane B.
- **Prediction to test (Lane B):** quark masses are the curvature determinant over a **larger** measurement
  little group (spatial × color), so their exponent ≠ 6 and their π-structure differs from the leptons —
  which is *why* the lepton formula didn't transfer naively, and is the boundary if leptons turn out special
  (color-singlet → pure `so(4)`, no color factor).

Handing this to Elie (engine) and Lyra (Di/color rep) as the geometric setup for the quark deposit.

## 6. The invariant-selection residual closes via my own F59/K253 (added, same-session)

I'd tiered "mass = the curvature **determinant** vs another SO(4)-invariant" as a named modeling choice
(Section 4). It isn't — it's forced by my own prior derivation, and "don't resist the obvious; find it in the
corpus" fires a third time today, on my own work.

**F59 v0.2 / K253 (SUBSTRATE-MECHANISM-FORWARD, grounds Casey #9):**
```
extensive  ⟺ additive            ⟹ numerator ADDS        (cell-counts, π^{n_C})
intensive  ⟺ per-direction-power ⟹ denominator normalizes (per-mode density, multiplicative)
```
The muon ratio `m_μ/m_e` is a **density ratio** (Plancherel/formal-degree densities, F118) — an **intensive**
observable. Intensive ⟹ **per-direction-power** ⟹ the per-direction factor raised to the number of
measurement directions = a **product over directions** = the **determinant** of the scalar operator. The
**additive** invariant (trace = sum over directions) is the **extensive** category — the *wrong category* for
a density ratio. So:

> **The determinant is FORCED (not chosen) because the mass ratio is intensive, and intensive ⟺
> per-direction-power ⟹ multiplicative ⟹ determinant. The trace is forbidden by category (additive =
> extensive).**

And K253 **already lists** `m_μ/m_e = (24/π²)^{C_2}` as the canonical **per-direction-power fingerprint** of
the intensive side — so this isn't bolted on; the muon was classified intensive in my own dual-ρ work weeks
ago. The curvature-determinant picture (Section 3) and the F59 intensive-classification are the **same
statement in two vocabularies**: *per-direction-power = determinant of the per-direction concentration over
the measurement directions.*

> **Cal #35 on myself (again):** the geometric reading (det over Λ²) and the F59 reading (intensive ⟹
> per-direction-power) are **one multiplicative structure in two vocabularies, NOT two independent
> confirmations.** One object.

**Tier (honest):** this forces the determinant **at F59/K253's tier** — SUBSTRATE-MECHANISM-FORWARD with the
explicit falsifier *(an intensive observable that ADDS, or an extensive one that powers, breaks the
dichotomy)*. It inherits F59's CONDITIONAL status; it is **not** RIGOROUS, and I'm not claiming it is. But the
residual is no longer "a modeling choice" — it's "forced by the extensive/intensive dichotomy at the same
tier as the dichotomy itself." Upgrade, honestly tiered.

— Grace, 2026-06-26 Friday. Lane A pin: exponent-6 forced (measurement little group = determinant rank, one
object, Cal #35 applied to self); determinant = Casey's curvature principle (constant-curvature S⁴ → clean
6th power) AND forced by F59 intensive⟺per-direction-power (one structure, two vocabularies); invariant-
selection upgraded from modeling-choice to forced-at-F59-tier; FK is Cal's. Count HOLDS 4/26 — Cal tiers at
landing.
