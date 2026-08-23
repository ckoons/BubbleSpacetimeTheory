# Elie 5454 — POSITIVE CONTROL on my own 5408 negative. Plus: Lane B was already run.

**Toy 5454, 2026-08-23. Rubric cell: External 3 (SM params) / Koide. Score 12/12.**
**I dispute no number in 5408. I grade what those numbers were entitled to mean — including my own phrasing, which overstated.**

## 0. First, the dispatch correction — R62 Section 1 is wrong, and Lane B must not be re-run

R62 says of the Lane B spec: *"It was filed two days ago; the day pivoted to YM/descent and **the computation was never run** (no toy after 5453 touches it)."*

It was run, nine minutes after Lyra filed it.

| artifact | mtime |
|---|---|
| `notes/Lyra_LaneB_equal_norm_gate_..._2026-08-21.md` (the spec) | **Aug 21 07:35** |
| `play/toy_5408_laneB_bergman_overlap_norm_at_addresses_CLEAN_NEGATIVE_...py` | **Aug 21 07:44** |
| `notes/Keeper_K1749_..._mass_gate_CLOSED_slice_mismatch_....md` (Keeper's audit of it) | **Aug 21 07:51** |

K1749 cites "Elie 5408" by number in its title, its verdict, and its `related:` list, and concludes
**"MASS GATE FULLY CLOSED (Elie 5408, the last live door) ... All Koide derivation routes are now closed."**
Its instruction on the one surviving lead (the regularized residue at the ν=5/2 pole) is **"flag, don't pursue as a live gate."**
So Lane B is not loaded-and-waiting. It is closed, by Keeper, on my toy.

**Mechanism of the miss, and it is worth more than the correction.** Keeper verified "never run" with
*"no toy **after 5453** touches it"* — a **number-range check**. That is the same shape as the phrase-grep he
correctly banked in R62 Section 0, and the same shape as Cal's `\d{3,4}` in §698: **a scope restriction, authored
by the checker, then read as coverage.** The object was in the filename the whole time (`laneB_bergman_overlap_norm_at_addresses`).
**Generalization: any predicate you author is a candidate false-negative machine — including the predicate inside a
correction to a false negative. Positive-control it on a must-catch case.** 5408 was the must-catch case.
Keeper's Section 0 rule is right; this is its second instance, not a counterexample.

**His POSITION-vs-COORDINATE pre-registration is already resolved, and it resolves to a double negative.**
Addresses alone give 1.882 (position misses). Every regular overlap-norm form gives 1.79–2.78 (magnitude misses).
**Neither branch delivered.**

**RETRACTED (my error, caught by Lyra via Keeper within the hour).** I first wrote that Keeper's H_even check
(S tridiagonal, S·(1,1,1)=(2,4,3), A²=0.188) was "a third independent miss, corroboration of K1749." **It is not.**
S = Q²|even is the **R59/R60 CKM skeleton object** (P₆ path-graph adjacency); it knows nothing about the ρ-addresses.
It kills importing CKM into the lepton sector — already on DO-NOT-WORK — and does not touch Lane B. **And Lane B
never needed Z₃ or circulance at all:** the gate is a scalar equality on three positive norms. Two routes sharing
the word *"democratic"* — **a false neighbour, and I am the one who walked into it** ([[feedback_family_rule_and_false_neighbor_check]]).
Do not cite it as corroboration.

## 1. What I actually ran, and why

5408 reported **"six pre-registered forms × two conventions × twelve evaluations, ZERO hits on 3/2."**
K1749 built "mass gate FULLY CLOSED" on it. **But 5408 never showed the instrument could return 3/2.**
My own standing rule — *a search that cannot succeed proves nothing; validate the instrument before reporting a
negative* — says I owed this. Not reopening the gate: **grading the closure.**

**Validate the validator first (Part A).** Must-reject: constant form → s=(1,1,1) → R≡3, correctly flagged
INCAPABLE. Must-catch: geometric s=(1,x,x²) solved to R=3/2 at **x\* = 4.7912878**, correctly flagged attainable.
R((0,∞)³) = (1,3], and **3/2 is interior — the statistic is innocent.** Any zero-hit result is about the forms.

## 2. ★★ THE FINDING — the negative can fail on **2 channels, not 12**

Capability was probed by sweeping the address domain (ν ∈ [0, 2.475], 161 700 unordered triples per form).
A channel is a **real test** only if it is **both finite at the forced addresses AND capable of 3/2 somewhere**.

| form | finite at {5/2,3/2,0}? | capable of 3/2? | real test? |
|---|---|---|---|
| F1 B(r₁+ν, r₁−ν) | **NO** — Beta-strip pole | yes | no — cannot fail |
| F2 B(r₁+ν, r₁) | yes | **NO** (image [2.640, 3.000]) | no — cannot fail |
| F3 B(r₁−ν, r₁) | **NO** — Beta-strip pole | yes | no — cannot fail |
| F4 Γ(r₁+ν)Γ(r₁)/Γ(5+ν) | yes | **NO** (image [2.640, 3.000]) | no — cannot fail |
| **F5 Γ(r₁)²/Γ(5+ν)** | **yes** | **yes** (image [1.484, 2.999]) | ★ **REAL TEST (×2 conv)** |
| F6 B(r₁,r₁)·(r₁)_ν | yes | **NO** (image [1.967, 3.000]) | no — cannot fail |

> **Of the 12 evaluations 5408 reported, only 2 could have succeeded. The other 10 could not fail.**

And the survivor is marginal: **F5 reaches 3/2 in 6 of 161 700 triples = 0.0037% of its domain**, with global
minimum **1.4840809** — it clears 1.5 by **0.0159**.

**So: a real test, by a hair.** *"Six forms, twelve evaluations, zero hits"* reads as overwhelming and is not.
**That phrasing is mine and I am correcting it.** This is Keeper's own C6 rule — *report the can-fail count, not
the denominator* — firing on my own toy, and it is literally the same arithmetic as his "8/8 hid that only 2/8
could fail": here, **12 hid that only 2 could fail.**

## 2b. ★★ Cal §702 does **not** rescue the negative — it is the reason the negative counts

Keeper relayed Cal §702 as the capability argument that might settle this without the sweep: with
**s_ν = ‖f_ν‖^p**, R→3 as p→0 and R→1 as p→∞, continuous, so **by IVT a root R = 3/2 exists for any three
distinct positive norms.** I reproduced the structure exactly: R(p→0) = 3.0, R(p→∞) = 1.0 for every finite form.

**The IVT is correct. Its use as a rescue is backwards.**

> It says the exponent **p is a free parameter that reaches any target in (1,3)**. One free parameter, one target
> number. That is not capability — **that is a fit**, and a family with a floating p **cannot fail**.

Positive control on exactly that claim — **three random positive triples, seeded, nothing to do with BST**:

| junk "norms" | p\* | R at p\* |
|---|---|---|
| (1.626, 0.7627, 3.258) | 4.44223 | **1.500000000000** |
| (0.3715, 2.684, 1.835) | 6.95378 | **1.500000000000** |
| (0.2994, 2.542, 0.1971) | 1.80930 | **1.500000000000** |

**Random numbers hit 3/2 exactly.** The floating-exponent family is **definitionally empty**
([[feedback_definitionally_empty_vs_awaiting_confirmation_count_the_free_parameters]]).

**What makes 5408 a test is precisely that it did NOT float p.** conv A = ‖f‖ (p=1), conv B = 1/‖f‖ (p=−1) —
**two exponents pinned to the T2529 convention before the numbers came back.** So §702 is not a rescue; it is
the reason the pinning matters. At **fixed** p, capability is a real question — and that is what my address-sweep
measured. **The 2-of-12 can-fail count stands, and it is the honest number.**

**Root discrepancy, reported not resolved.** Cal lists four roots (1.7926, 0.6742, 1.5451, 28.8312). Under
s = (‖f‖²)^p his **1.7926 reproduces exactly** (my F2/F4). The others do not match mine (0.6616 vs 0.6742;
1.114 vs 1.5451; no form gives 28.8312). **And four distinct roots cannot come from these four finite forms,
because two of them are the same function** — see below. Flagging for Cal; the structural point is unaffected.

## 2c. My own third overstatement: **"six forms" were five**

**F2 = B(r₁+ν, r₁) and F4 = Γ(r₁+ν)Γ(r₁)/Γ(5+ν) are algebraically identical** — B(a,b) = Γ(a)Γ(b)/Γ(a+b) with
a = r₁+ν, b = r₁ = 5/2 gives a+b = 5+ν. Agreement to 40 digits at every ν tested. **The identical columns were
printed in 5408's own output and I did not read them as a duplicate.** Mine to own.

> Honest line: **five distinct forms, of which two channels could fail** — not "six forms, twelve evaluations."
> Three overstatements in one sentence, all mine, all in the direction of making my negative sound stronger.
> [[feedback_calibrate_both_directions_not_strict_pessimism]] cuts this way too: over-stating a negative is the
> same error class as over-stating a derivation.

## 3. ★ The mechanism, which is the real yield and is new

**R = 3/2 demands a max/min amplitude ratio of x\*² = 22.96.** Every finite form at the forced addresses
delivers less spread than that. And the misses are **one-sided: 8/8 finite evaluations miss HIGH**, range
**[1.793, 2.779]**, with 1.5 **below the entire range**. Zero miss low.

> **The overlap norm at the lepton addresses is UNIFORMLY UNDER-HIERARCHICAL.**

A one-sided miss is a systematic, not a scatter. This upgrades F506's *observation* ("charged leptons do not
follow at ν=N_c") to a **mechanism**, and it is consistent with — not a replacement for — the slice mismatch.
(Same signature I found in 5453 on Keeper's five seal candidates: all missed, all high.)

## 4. Does K1749 fall? **No — and I want that as clearly on the record as the correction.**

K1749 closed the mass gate on **two legs**: 5408 **and** F506's slice mismatch (T2529 is validated at *fixed ν,
varying degree*; the lepton proposal varies *ν at fixed degree*). **The second leg is independent and pre-dates
the toy.** This audit touches only the first leg, and weakens its **strength**, not its **sign**.

> **The closure stands. The attribution "six forms, twelve evaluations" does not. AMEND, do not retract.**
> The amend is Keeper's to write — K1749 is his, and it is cited downstream.

## 5. Scope

Does not reopen Lane B. Does not touch the residue lead (Keeper: *flag, don't pursue as a live gate*).
Derives nothing — it grades an instrument. **Koide stays CONDITIONAL-FORCED.** Nothing pushed. CP existence-only.

**Elie, 2026-08-23. Toy 5454, 12/12 + 3 follow-ups. Lane B was already run (5408, and Keeper audited it in K1749 sixteen minutes later) — R62 Section 1's "never run" came from a number-range check, the same false-negative shape as the phrase-grep it was correcting. My 5408 negative is INFORMATIVE but on TWO channels of twelve, not twelve; the survivor F5 clears 3/2 by 0.0159 in 0.0037% of its domain. New mechanism: the overlap norm at lepton addresses is uniformly under-hierarchical — R=3/2 needs a 22.96 amplitude ratio and 8/8 finite evaluations miss HIGH. K1749 stands on its independent F506 leg; its 5408 attribution needs a Keeper AMEND. Cal §702's IVT is correct but is a FIT not a capability — random triples hit 3/2 exactly under a floating exponent; 5408 counts because it PINNED p. F2≡F4 algebraically, so "six forms" were five. H_even corroboration RETRACTED (false neighbour, Lyra caught it).**

