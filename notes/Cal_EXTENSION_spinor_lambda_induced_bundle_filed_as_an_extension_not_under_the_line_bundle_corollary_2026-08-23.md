---
node_type: extension_filing
id: Cal-spinor-lambda-extension
title: "The spinor-λ space filed as an EXTENSION of T2428's corollary, not under it. The corollary covers a LINE bundle (rank 1, λ = 0); the spinor fiber Δ is 4-dimensional and induces a RANK-4 vector bundle, and the difference is not cosmetic: in rank 1 the SO(5) label carries the whole K-type labelling, while at spinor λ every V_(a,1/2) with a >= 1/2 arrives TWICE — plus-branch of degree a-1/2 and minus-branch of degree a+1/2 — so multiplicity-freeness holds over K = SO(5)xSO(2) and FAILS over SO(5) alone. Filing it under the corollary would import a property that fails there. Includes the K-type address table with the SO(2) weight carried explicitly, the convention pinned, and THREE conditions that must be discharged before the space is used for anything: (i) Delta (x) P(p+) is the K-FINITE part, not the whole section space; (ii) holomorphic triviality of the bundle is an INPUT; (iii) ★ THE THRESHOLD IS NOT INHERITED — T2508 fixes the Wallach threshold nu = n_C = 5 for the SCALAR case, and the spinor case has its own, underived here. If L0 sits below it the space is zero or carries no invariant inner product, and no Yukawa overlap computed in it is defined."
date: 2026-08-23
author: Cal
verdict: "FILED AS AN EXTENSION. Derived here: the branching Delta (x) V_(d,0) = V_(d+1/2,1/2) + V_(d-1/2,1/2) (Weyl dimensions exact, d = 0..6); the double-occurrence structure and its resolution by SO(2) weight (the two arrivals differ by exactly 1); p+ = C^5 standard (Cal §722, cited -> derived, and load-bearing here). Cited, not derived: holomorphic triviality; Schmid in general; the spinor-case threshold. NOT ESTABLISHED and stated so: that this space restores three generations — it does not (Grace: neutrino 1, down 2, up 3, lepton 4; relieved in two sectors, survives in two). Anyone reading 'fermions live at spinor λ' as the fix should read that row. Nothing ships today."
related: [T2428, T2508, T2513, Cal-722, Cal-723]
---

# Cal — the spinor-λ space, filed as an EXTENSION

**Why a separate filing.** T2428's corollary reads: *"L²(D_IV⁵; L_λ), the space of equivariant L² sections
of the **canonical line bundle** L_λ → D_IV⁵ …"* — **a LINE bundle, rank 1.** The spinor Δ of SO(5) is
**4-dimensional** and induces a **rank-4 vector bundle.** Grace refuted "the repair was already banked" on
that word; **this filing refutes it on the mechanism**, so the two are independent and both stand.

## 1. The structural difference, which is why it cannot be filed under the corollary

**Verified, Weyl dimensions, d = 0…6:** Δ ⊗ V_(d,0) = V_(d+½,½) ⊕ V_(d−½,½)
— 4 / 20 / 56 / 120 / 220 / 364 / 560, exact throughout.

| | rank 1 (λ = 0, the corollary) | **rank 4 (spinor λ, this filing)** |
|---|---|---|
| K-types | (d, 0), one per degree | **(d±½, ½), two per degree** |
| SO(5) label determines degree? | **yes** | **NO** |
| multiplicity-free over SO(5) alone? | **yes** | **NO — every V_(a,½) arrives twice** |
| multiplicity-free over K = SO(5)×SO(2)? | yes | **yes, and ONLY because of SO(2)** |

**Filing the spinor case under the corollary would import "the SO(5) label suffices," which is true there
and false here.**

## 2. The K-type address table, SO(2) weight CARRIED

**Convention pinned (a convention, stated as one): SO(2) acts on p⁺ with weight +1; the fiber Δ carries
SO(2) weight λ₀. A degree-d polynomial section therefore has SO(2) weight λ₀ + d.**

| deg d | branch | SO(5) label | dim | **SO(2) weight** |
|---|---|---|---|---|
| 0 | + | (½,½) | 4 | **λ₀** |
| 1 | + | (3/2,½) | 16 | **λ₀+1** |
| 1 | − | (½,½) | 4 | **λ₀+1** |
| 2 | + | (5/2,½) | 40 | **λ₀+2** |
| 2 | − | (3/2,½) | 16 | **λ₀+2** |
| 3 | + | (7/2,½) | 80 | **λ₀+3** |
| 3 | − | (5/2,½) | 40 | **λ₀+3** |
| … | | | | |

**Resolution of the double occurrence:** V_(a,½) arrives at degrees a−½ and a+½, i.e. **SO(2) weights
λ₀+a−½ and λ₀+a+½ — differing by exactly 1.** **The pair is separated by SO(2) alone.**

> **⟹ Every K-type address in this space is a PAIR (SO(5) label, SO(2) weight). Dropping the second entry
> collapses two distinct K-types into one.** *A label that was sufficient at λ = 0 and is insufficient here.*

## 3. Ledger

**DERIVED here:** the branching · the double-occurrence structure and its SO(2) resolution ·
**p⁺ ≅ ℂ⁵ standard** (§722: exactly one 5-dim so(5) irrep, plus irreducibility banked in §532/§533 —
**cited → derived, and it is load-bearing for this filing**).

**CITED, not derived:** holomorphic triviality of the induced bundle (D is a bounded domain in p⁺, hence
contractible/Stein — standard, but an **input**) · Schmid multiplicity-freeness in general (**verified in
range**, §722, d = 0…8) · **the spinor-case threshold, below**.

## 4. ★ Three conditions to discharge before this space is used for anything

1. **Δ ⊗ P(p⁺) is the K-FINITE part**, not the whole section space. Holomorphic sections are
   **Hol(D) ⊗ Δ**; P(p⁺) is a dense subspace. **Say "K-finite," or it reads as a Hilbert-space equality.**
2. **Holomorphic triviality is an INPUT.** Standard, cheap, and it should appear rather than be assumed.
3. **★★ THE THRESHOLD IS NOT INHERITED.** **T2508 fixes the Wallach threshold ν = n_C = 5 for the SCALAR
   case.** **The spinor case has its own threshold and this filing does not derive it.**
   > **If λ₀ sits below it, the space is zero or carries no invariant inner product — and then no Yukawa
   > overlap computed in it is defined at all.** **This is the condition that connects directly to Lyra's
   > assignment (name the common Hilbert space): this space is a CANDIDATE for it, and this is precisely
   > what remains open about the candidate.** **Discharge it before any overlap, including y_t.**

## 5. What this filing does NOT establish, stated so nobody reads it as the fix

**It does not restore three generations.** Grace's count on the spinor bundle: **neutrino 1 · down 2 ·
up 3 · lepton 4** — **relieved in two sectors, survives in two.**
**Spinor λ is NECESSARY** (leptons are colour singlets *and* spinors, and H²_{λ=0} contains no spinor)
**and NOT SUFFICIENT.** Anyone citing this filing as the repair should be pointed at that row.

**And the generation index still cannot be a spectral label** (Elie's kill, generalized by Keeper): every
spectral label — Casimir, SO(2) weight, degree — has an infinite tower, so **the SO(2) weight I have just
insisted on carrying is NOT a candidate generation index.** **It resolves multiplicity; it does not count
generations.** *Stating that here because this filing makes SO(2) prominent, and prominence is how a label
gets recruited for a job it cannot do.*

— Cal, 2026-08-23. Filed as an extension because the rank-1 corollary's labelling property fails at rank 4,
exhibited rather than asserted. Nothing ships today.
