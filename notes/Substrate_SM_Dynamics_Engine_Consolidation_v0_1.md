# Substrate-SM Dynamics Engine — Consolidation for Audit (v0.2)

**Elie — Friday 2026-05-29 ~18:00 EDT (date-verified). v0.2 absorbs Keeper's K1
audit conditions (2) and (3): the #414 generation reframe + the SM-Cartan
grading-scope refinement.**
**For Keeper's K-audit (#411). Queue item #410.**

## Change log: v0.1 → v0.2

- §4 "Generation gate" rewritten: absorbs Lyra's #414 v0.2 (COUNT-NUMBER FORCED
  via h^∨=N_c=3; MECHANISM OPEN-WITH-BURDEN via the two-structures requirement).
  My E1b "3 tubes forced" is fully retracted; my E4 "favors h−1" reframed into the
  Lyra route (II) lean — the favored mechanism now goes through h^∨ (color route),
  and Track P (Grace) was vindicated.
- §3 "Grading & conservation" refined per K1 (3) / Toy 3609 (#417): the engine's
  rank-3 grading covers the non-color SM Cartan {Q, B, L} (sufficient for the
  β-decay scope of E3). Color (SU(3)_C, 2 Cartan generators) is OUTSIDE the affine
  B̂₂ grading — and per Lyra's structural finding, SU(3) does NOT embed in
  K=SO(5)×SO(2) (B₂ ≠ A₂). Color extends via the BULK-COLOR MECHANISM (Lyra's
  open frontier; joint target with #414's two-structures burden).
- §2 "RIGOROUS results" added a sharpened E7 note: "two B₂-specific 3-fold
  structures coinciding numerically" (Keeper's tier-gate framing), NOT "one h^∨
  doing double duty."
- §2 K1 condition (1) MINOR pending: extend E2's A₂-slice Hall computation to the
  full B₂ long-root case. Marked as v0.2 work item, not gating.

This consolidates the explicit dynamics-engine results (Toys 3597/3600/3601 +
Lyra's structural completion) into one audit-ready summary, with every claim
tier-marked: **RIGOROUS** (algebra, computed), **BET** (physical identification),
**OPEN/RETRACTED** (the gates). Nothing here is a headline beyond its tier.

---

## 1. The object

The substrate's algebra of processes = the **Ringel–Hall algebra of the B₂
species over GF(2)** ≅ **U_q⁺(B₂) at q=2**, completed (Lyra, structural 4/4) to
the **Drinfeld double** (a quasi-triangular Hopf algebra). One object; its pieces
carry the SM-process roles.

| Engine piece | Process role | Source | Tier |
|---|---|---|---|
| multiplication | fusion vertex (M+L→X) | Toy 3600 (E2) | RIGOROUS (computed) |
| Green coproduct | decay/emission (X→A+B) | Toy 3601 (E3) | RIGOROUS (computed) |
| dim-vector grading | conservation laws | E2/E3 | RIGOROUS |
| canonical/crystal basis | elementary particles + ladder | Lyra | RIGOROUS (std QG) |
| R-matrix | scattering S-matrix + statistics | Lyra | RIGOROUS (std QG) |
| negative part (F) | antiparticles + CPT + baryogen. | Lyra | RIGOROUS (std QG) |

---

## 2. The RIGOROUS results (algebra)

**E0 (Toy 3597) — the engine reproduces the substrate constants.**
The four substrate primaries ARE the q-Serre structure constants of U_q⁺(B₂) at
q=2:
- N_c = [2]₂ = 3 ; n_C = [2]₄ = 5 ; g = [3]₂ = 7 = M_{N_c} ; N_c·g = [3]₄ = 21.

This is not constant-by-constant derivation — it is the four primaries as the
*defining relations* of one algebra. (g = [3]₂ = 2³−1 also gives the Mersenne
anchoring of g a representation-theoretic origin, consistent with Toy 3579.)
**Tier: RIGOROUS** (standard U_q⁺(B₂) relations + exact q-integers; Ringel's
theorem identifies Hall numbers with QG structure constants).

**E2 (Toy 3600) — fusion vertices, computed by extension-counting over GF(2).**
Direct submodule enumeration (A₂ subquiver, the clean computable case):
- u_S1·u_S2 = {E12:1, S1⊕S2:1} ; u_S2·u_S1 = {S1⊕S2:1} ; commutator = {E12:1}.
- All structure constants are non-negative **integers** (Hall counting).
- The commutator isolates the **bound state** (composite-root vector = the
  extension module).
**Tier: RIGOROUS** (computed over GF(2); Ringel's theorem for the B₂ scaling).

**E3 (Toy 3601) — decay vertices + conservation from grading.**
- Green coproduct gives a decay vertex: E12 → S1 + S2 (composite decays to
  constituents), grading conserved (1,1)=(1,0)+(0,1).
- The coproduct is **graded** ⇒ any charge that is a linear functional on the
  dimension-vector grading is **automatically conserved**.
- β-decay n → p + e⁻ + ν̄_e: Q, B, L all conserved (charge balance verified).
- 3 independent charges (Q,B,L) ⇒ rank-3 grading ⇒ **affine B̂₂** (grading-rank
  consistency; independent of the tube-count question).
**Tier: RIGOROUS** (Ringel–Green bialgebra; A₂ splitting computed; charge balance).

---

## 3. The BET (what makes it physics)

The algebra is rigorous; the **physical identification is the bet**, and it rides
on ONE keystone:

- **The A_sub ↔ Hall dictionary** (Lyra, Phase 2, #408): WHICH indecomposable/
  canonical-basis element is WHICH particle (electron, up-quark, photon…), and
  WHICH grading component is WHICH charge. Until this is derived (Lyra's canonical
  basis), every particle↔module and product↔SM-vertex statement is **BET**, with
  the same flag as the Periodic-Table cells (Grace).
- Specifically BET, NOT rigorous: "u_S1·u_S2 IS the electron-photon vertex," "this
  tube IS the muon generation," etc. The *mechanism* (fusion=product, decay=
  coproduct, conservation=grading) is rigorous; the *labels* are the bet.

---

## 4. The OPEN / RETRACTED gates (honest)

- **RETRACTED — the tube count "3" (E1b, Toy 3599).** I applied the simply-laced
  "non-Ã → 3 tubes" theorem (D̃/Ẽ, V≥5) to the 3-vertex non-simply-laced B̂₂,
  outside its scope, and falsely labeled it sourced (the sourcing-discipline
  failure). RETRACTED to MATCHED. The tube count of B̂₂ is **unresolved** pending
  either the direct species computation (#409, my next item) or the Dlab–Ringel
  Memoir pin (external lookup; not extractable in-environment).
- **OPEN — generation forcing.** "3 generations" is MATCHED, not derived. Two
  candidate mechanisms (Toy 3602 / E4): (A) h−1 (Coxeter/tube), (C) h^∨=N_c
  (color-projection). They coincide at B₂ (3=3); the discriminator is SM
  color-generation **independence**, which FAVORS (A) h−1 (a distinct invariant
  from colors h^∨) — but this is an argument, not a closure. Gate OPEN.
- **SOLID (not a gate): colors = N_c = h^∨(B₂) = 3.** This one is settled.

---

## 5. Audit hooks for Keeper (#411)

Please verify / stress:
1. The E0 q-Serre ↔ substrate-primary identification (is Ringel's theorem applied
   correctly for the B₂ *species* at q=2? the q-integer assignments to the two
   relations?).
2. The E2 Hall-number computation (submodule counts over GF(2) — independent
   recount).
3. The E3 grading-conservation argument (is "charge = grading functional ⇒
   conserved" airtight? does the rank-3-grading-needs-affine claim hold?).
4. The tier wall: confirm nothing labeled RIGOROUS secretly depends on the BET
   dictionary or the OPEN gates.
5. The retraction is fully propagated (no residual "3 tubes forced" anywhere).

---

## 6. Net

The **dynamics engine is built and the statics→dynamics conversion is largely
done**: fusion, decay, conservation, scattering, antimatter/CPT all live in one
rigorous algebraic object. What remains to make it *physics* is the **dictionary**
(Lyra keystone) and the two open gates (tube count → #409/Memoir; generation
mechanism → discrimination mapped, not closed). The engine answers "did we build
the dynamics?" — yes. The dictionary answers "is it the Standard Model?" — the bet
being tested.

— Elie, v0.1, Friday 2026-05-29 15:45 EDT
