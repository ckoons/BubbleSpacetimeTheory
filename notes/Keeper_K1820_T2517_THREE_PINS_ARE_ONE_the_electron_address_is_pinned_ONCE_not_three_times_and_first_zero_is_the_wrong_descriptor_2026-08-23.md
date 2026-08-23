# K1820 — T2517's "pinned THREE independent ways" is ONE way. AMEND, do not retire.

**Keeper, 2026-08-23. Rubric cell: External 3 (SM params) — the row the scorecard itself calls
"still highest over-claim risk." Verdict: CONDITIONAL PASS with two corrections.**
**The VALUES are not disputed. The COUNT of independent derivations is.**

## 0. What I checked and why

Casey asked me to verify the old calculations behind the checklist. The scorecard lists in its **DERIVED**
column: *"the generation ADDRESSES ν={5/2, 3/2, 0} (T2517, **forced 3 ways**)."* Today three independent
routes (Elie lowest-weight, Cal threshold, Keeper index-type) concluded the **spinor** generation addresses
are underived — so the supporting objects of that cell needed auditing regardless of the Clerc reading.

## 1. ★ CORRECTION 1 — the three pins are one pin

Registry text: *"The electron at ν=5/2 is pinned THREE independent ways: (a) self-shadow fixed point of the
reflection ν→(n_C−ν)=5−ν; (b) first zero of the Harish-Chandra formal degree
d(ν)=(5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν); (c) ρ₁=n_C/2."*

| pin | what it delivers | independent? |
|---|---|---|
| (a) fixed point of ν → 5−ν | **p/2, TAUTOLOGICALLY** — *any* reflection x → C−x has fixed point C/2 | **NO. can-fail = 0.** It restates "the reflection is about 5." |
| (b) zero of d(ν) | **p/2** — the zero at 5/2 **IS the factor (5/2−ν) = (p/2−ν)**, by inspection | **NO** |
| (c) ρ₁ = n_C/2 | **p/2**, by definition | — |

> **ALL THREE REDUCE TO ONE FACT: 5/2 = p/2 = n_C/2.**
> **"Pinned three independent ways" is a can-fail-1 claim dressed as can-fail-3.**

This is the Schur-web shape the team spent 2026-08-23 learning to detect, sitting in a **DERIVED** cell.

## 2. ★ CORRECTION 2 — "first zero" is the wrong descriptor

d(ν) = (5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν). **Zeros sorted: 1, 2, 5/2, 3, 4.**
**5/2 is the THIRD smallest, not the first.** Readings tried: first ascending → 1; first descending → 4;
first above the Wallach threshold → 2. **None give 5/2.**

> **BUT THE NUMBER IS RIGHT AND THERE IS A GENUINE PROPERTY: 5/2 is the UNIQUE NON-INTEGER ZERO.**
> **Right number, wrong reason bolted on** — [[feedback_decorative_clauses_hide_errors_sweep_both_directions]].
> **Replace "first zero" with "the unique half-integer zero."**

## 3. ★★ WHAT SURVIVES, AND IT IS STRONGER THAN THE CORRECTION SOUNDS

The discrete Wallach set for D_IV⁵ is **{0, a/2} = {0, 3/2} — exactly two points, no freedom.**

| address | status | strength |
|---|---|---|
| **muon ν = 3/2** | **FORCED** — a discrete Wallach point (= N_c/2 = a/2; a = n−2 = N_c, one number two names) | **can-fail real:** a different discrete set moves this address |
| **tau ν = 0** | **FORCED** — the other discrete Wallach point | same |
| **electron ν = 5/2** | **the self-dual point p/2** of ν → p−ν; **on the continuous ray**, so *not* forced by the Wallach structure | **pinned ONE way, by a DIFFERENT fact** |

> **HONEST RESTATEMENT: 2 of 3 addresses are FORCED by the structure (they exhaust the discrete Wallach
> set); the third is pinned by ONE separate fact (the self-dual point). That is a good result — it is just
> not the one the scorecard states.**

**★ AND THIS IS GENUINE CORROBORATION, unlike the pins.** Elie reached the identical split this afternoon
(toy 5472) from **Wallach-component counting** — *"the structure forces 2 of 3 and leaves the third free"* —
while I reached it by **auditing the three pins**. **Different objects, different failure modes, arrived at
separately. Two CIs.**

## 4. VERDICT

**CONDITIONAL PASS. AMEND, DO NOT RETIRE** — same call Elie made on my K1749.
- **Registry T2517:** strike *"pinned THREE independent ways"* → *"pinned once, at the self-dual point
  p/2"*; strike *"first zero"* → *"the unique half-integer zero"*; keep **ALL THREE VALUES**.
- **Scorecard External 3:** the addresses stay in DERIVED **with the split stated** — two forced, one
  pinned once — **and flagged as scalar-λ objects pending the Clerc reading.**
- **Nothing retires. No value moves.**

*— Keeper, K1820. The values were right. The count was three times what it should have been.*

---

## 5. ★ AMENDMENT (same audit, no new K-number) — a THIRD wrong descriptor, found by building the root data

While gating the root-system input for the A(Δ)/C(Δ) computation I built ρ for so(5,2) explicitly and
**every gate passed**: g_C = B3 on (e1,e2,e3), e1 = the SO(2)/ν direction; compact roots = B2 on (e2,e3)
[8 roots]; **positive noncompact = 5 = dim p⁺ = n_C** ✓; **rank = 2** via the maximal strongly-orthogonal
set {(1,1,0), (1,−1,0)} ✓; **ρ = (5/2, 3/2, 1/2)** ✓.

**T2517's opening clause reads: *"the three charged-lepton generations sit at the ρ-vector components of
D_IV⁵ — electron ν=5/2, muon ν=3/2, tau ν=0."***

| address | a ρ component? |
|---|---|
| electron 5/2 | **YES** (ρ₁) |
| muon 3/2 | **YES** (ρ₂) |
| **tau 0** | **NO — ρ₃ = 1/2, not 0** |

> **TWO OF THREE. The tau is not at a ρ component.**
> **⟹ THIRD WRONG DESCRIPTOR ON THIS ONE THEOREM** — with *"pinned three independent ways"* (Section 1)
> and *"first zero"* (Section 2). **All three descriptors wrong; ALL THREE VALUES RIGHT, every time.**

**AND THE DECOMPOSITION SHOWS WHAT IS ACTUALLY TRUE, which is better:**
**ρ = ρ_n + ρ_c** with **ρ_n = (5/2, 0, 0)** — the noncompact ρ lives **purely on e1, the ν direction**, and
equals **exactly 5/2**.
> **★ THE ELECTRON SITS AT ν = ρ_n = p/2. That is a real, meaningful, single identification** — not three
> pins, and not a coordinate coincidence. It is the noncompact ρ read in the parameter it parametrises.

**And 3/2 is NOT distinguished by being ρ₂.** It carries **three names — a/2, N_c/2, ρ₂ — coinciding only
because a = n−2 = 3 = N_c in BST.** One number, three labels. **The same disease as the three pins, in the
same clause.**

### HONEST ONE-LINE REPLACEMENT FOR THE T2517 HEADLINE
> **"The electron sits at ν = ρ_n = p/2, the self-dual point of ν → p−ν. The muon and tau exhaust the two
> discrete Wallach points {a/2, 0}. Two addresses forced by the Wallach structure; one pinned by the
> noncompact ρ."**

**Shorter, true, and it says WHICH fact does WHICH job. Nothing retires. No value moves.**

**Method note, and it is the day's rule paying off immediately:** I found this **while gating inputs for a
different computation** — not by auditing T2517 again. **Enumerating the inputs of the A/C job surfaced a
defect in a theorem I had already amended once today.** [[feedback_decorative_clauses_hide_errors_sweep_both_directions]]
