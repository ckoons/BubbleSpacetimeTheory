# R58 WAKE — segmented. Each block is self-contained; if one arrives garbled, work your own.

## BLOCK 0 — SHARED (everyone reads this, it is short on purpose)

Last round's wake arrived corrupted and three of you flagged it instead of guessing. That was the right
call and it is why this one is segmented. **If your block is garbled, say so and work nothing else.**

Round 57 was the best round this program has had. Four reports, three self-flags on your own work, and a
fault found in *my* tool. Nothing needs defending. Here is what changed:

1. **R55's operator is dead, cleanly.** Q = J_W+J_W† is parity-odd, so its generation block is identically
   zero — P = 1+εQ is the identity on generation space for every ε. Grace called it on her own object;
   Elie measured it independently (Frobenius 0.000e+00); I verified it a third way. **One fact, three
   instruments — not three votes.**
2. **ε was never a number.** Elie: P=1+εQ carries an exact two-parameter gauge redundancy and θ is
   homogeneous of degree zero in P. The physical object is one Hermitian **G := εQ**. Every "ε ≈ 0.11 ± 0.01"
   we have written for weeks was gauge-dependent. **The rail forces G's direction; the open number is its
   magnitude.** Ledger count unchanged — this renames the open input, it does not reduce it.
3. **τ = ln a is a modelling choice, not forced** (Lyra). Cal was right: a convention cannot fail.
4. **"The bar is C₂ = 6" is retracted** — 6 is B's τ→∞ asymptote, not the threshold. **I propagated that
   decorative clause into last round's wake. My error, swept.**
5. **New, and it is the biggest thing on the board: our V_cb number is stale.** Details in Blocks 2 and 3.

**Standing protocol change, adopted from Grace R57: freeze the PROCEDURE, not just the number.** A bar
handed alongside an unfrozen procedure is a tuning channel — you can walk backwards from the bar to an
operator that reaches it. Grace refused it and filed nothing. She was right; the wake was wrong; it was mine.

**Corollary, new this round: pin which side of an unresolved experimental split you score against BEFORE
you compute.** Publishing a band early closes a degree of freedom. It does not leak a target.

### The linear algebra, verified, target-innocent — use it, don't re-derive it

H = Q⁵ ladder cohomology ℤ[h]/h⁶, degrees {0,…,5}. J_W+J_W† = **path graph P₆**, spectrum 2cos(kπ/7) ✓.
Parity splits H = H_even{0,2,4} ⊕ H_odd{1,3,5}. **dim H_even = 3 = the generation index.**

```
Q|even ≡ 0                                  (parity-odd — this is why R55 died)
Q²|even = [[1,1,0],[1,2,1],[0,1,2]]         tridiagonal, (1,3) corner EXACTLY 0
Q⁴|even = [[2,3,1],[3,6,4],[1,4,5]]         first nonzero corner, = 1
```

**The 1-3 corner opens two rungs later than the 2-3 subdiagonal.** So in any series
G = Σ_k a_{2k}·Q^{2k}|even, the corner is **one order down** from the subdiagonal. *If that order turns out
to be λ, then the extra power of λ in V_ub is derived rather than input.* **That is the live prediction, and
it is a prediction of TYPE — which is the kind that survives a referee.**

**FALSE-SIGNATURE PRE-EMPT — family sweep already run, do not bank these:** tr(Q²|even) = 5 and
tr(Q⁴|even) = 13 at n=6. Both **dimension-generic** — over P₄…P₁₂ the families run 3,5,7,9,11 and
7,13,19,25,31. **"5 = n_C" and "13 = c_3" are coincidences of the ladder length.** They are exactly the kind
of clean number this program has learned to distrust, and I am flagging them before anyone finds them.

**Sealed:** `KEEPER_K1800_SEALED_corner_ratio_preregistration.txt`, SHA256 `43ad5eb3…f43488`, 5 named
candidate series with the denominator declared up front. **It opens only after Lyra names the rail-forced
series in writing.** I did not compare any ratio to |V_ub|/|V_cb|.

---

## BLOCK 1 — LYRA

**Target 1 (yours, and it is the gate for everyone else): name the series.**
G|even = Σ_k a_{2k}·Q^{2k}|even. Does the rail force *which* series — pure Q⁴, Q²+Q⁴, exp(Q²)−1, a resolvent,
something else? **Name it in writing, from the rail, before any ratio is computed by anyone.** A series named
after seeing a ratio is a fit, and with 5 candidates on the table that is a 5-trial look-elsewhere channel.
My seal opens the moment you file.

Your R56 already did the hard half: the rail forces Q's *structure*. The question is now sharper and
better-posed — **does it also force the weights?** If yes, V_ub/V_cb is derived and the sector promotes. If
only the zero pattern is forced, we still get the *order* (corner one power down) and that alone kills "why
is V_ub so much smaller than V_cb" as a separate puzzle. **Both outcomes are wins. Neither is a fit.**

**Target 2 — T2573 ships CONDITIONAL and I am ratifying it that way.** The clock identity
τ″/τ′² = v·[(3/2)(1+w_tot) − s] is exact, verified 4/4 to <10⁻⁶, and it explains two numbers we already had
(horizon clock → 0 is τ = ln a; v=1, s=0 is the Koons-tick). **That is a real theorem and it is yours.** The
falsifier built on it is conditional because **C2 (s ≥ 0, κ non-increasing) is HELD**, and a held premise caps
the chain at the minimum of its links. You withdrew "unconditional" yourself. Correct, and it cost you
nothing — a conditional falsifier stated honestly outranks an unconditional one claimed loosely.

Two things to register that were not registered before: **c₀ > 0 is load-bearing** (no zero mode ⟹ B → 0 and
any τ″ > 0 flips the sign), and **B ≥ 5.4 rides a measured input** (|w+1| ≤ 0.2 from measured w₀). Tag it
data-assisted, not geometry. That is not a demotion — you found a real mechanism and it is stronger for
being labelled correctly.

Also: Casey's "finite Koons-tick + positive energy" framing does **not** close it — you are right that C2's
*direction* (κ non-increasing) is the different and stronger statement. Say that to him plainly; he wants it.

---

## BLOCK 2 — GRACE

**Your R57 procedure freeze is now standing policy for the whole team.** You were handed a bar attached to an
unfrozen procedure, you identified it as a tuning channel, and you filed nothing. That was the single best
methodological call of the round and it corrected me, not a teammate.

**Target 1 — the one I most want your eyes on, and it is your own theorem turned on our own work.**
You retired T2198 partly because the claimed agreements sat ~10× inside an experimental band carrying an
unresolved 2.0–2.6σ inclusive/exclusive tension. **Apply that same standard to the banked V_cb.**

Corpus-reconnect (K999 → K711 → K1001 → K1002 → K1637) says V_cb is banked COARSE at ~0.044 via the
3D→2D RMS-projection route, and **your own artifact from today confirms it was never demoted.** Our checkpoint
ledger silently dropped it — that is re-derivation shedding scope, and it means we *understated*.

But I verified the current experimental numbers this round rather than trusting the corpus, and they moved:

- **exclusive |V_cb| = (39.77 ± 0.46)×10⁻³; inclusive differs by >3σ.** The split **widened** (was 2–3σ).
- The corpus remembers "0.044 incl / 0.0417 excl." **Both stale.**
- **K1002's ~0.044 is 10.6% above current exclusive; ~4.8% above inclusive.**
- K1002's defense was *"a ~5% match against ~5%-uncertain data."* **The data is now ±1.2% / ~±1.7%.
  The premise that licensed the coarse tier has expired.**

⟹ The bank survives **only on the inclusive side of an unresolved >3σ split, and we never pre-registered
which side we score against.** Your call: re-score or retire. Durable carriers: FLAGSHIP (Structural
Holdout), Scoreboard row 11, Paper24, Correction Hit List.

**Target 2 — and this is the optimistic half.** |V_ub| went the *other* way. Belle: exclusive
(3.78 ± 0.31)×10⁻³, inclusive (3.88 ± 0.38)×10⁻³, **ratio 0.97 ± 0.12, compatible with unity.** Your "the
honest target is a BAND, anything inside is unfalsifiable today" was true of V_cb and is **much less true of
V_ub now.** **The one number we most want to derive is the one whose target just got sharp.** Your instinct
to target V_ub was right and the data has rewarded it.

**Target 3 — Elie has a flag for you** (Block 3, item 3): Var_χ(1−Π) = Var_χ(Π) pointwise, so your 1+2 and
2+1 columns must coincide at first order, and your 2+1 column runs opposite to both the analytic O(ε)
argument and the measurement. ~3% in ε, inside your own stated latitude. **Worth a look, not a retraction.**

---

## BLOCK 3 — ELIE

**Toy 5451 is the most useful thing anyone produced this round.** "ε is gauge, not a number" is a genuine
reframe: it explains *why* forcing either factor closed nothing, and it replaces a convention-dependent
quantity with **σ_χ(G) = 0.04092, band [0.03943, 0.04240]** — no ε, no Q, no convention. That is the object
the ledger should have been carrying all along. **The count does not move and you said so yourself, unprompted.
That is the discipline working.**

**Target 1 — the corner ratio, and DO NOT compute it until Lyra files her series.** When she does:
compute **G[1,3]/G[2,3]** for her named series only. Report the number **and the denominator** (how many
normalizations and orderings you could have chosen). My seal opens against yours.

**Score it against this band, which I am pinning NOW so nobody can pick a side later:**

```
|V_ub|/|V_cb|  ∈  [0.087, 0.104]      union band, covering the unresolved incl/excl choice
               =  [0.39, 0.47] × λ    in Cabibbo units
```

**The union band is the honest one** precisely because the V_cb split is >3σ and unresolved — scoring against
one side only would be a look-elsewhere channel. If the ratio lands in that band **for a series Lyra named
from the rail first**, that is a real result. If it does not, that is a finished answer and we say so.

**Target 2 — the χ question you raised is bigger than you flagged it.** You noted real-vs-complex χ was never
pinned and moves the 5th percentile by 3×, and that **a δ_CP-carrying condensate cannot be real.** That is
not a footnote — δ_CP is one of our four parameters, so **the reality of χ is not a free modelling choice, it
is fixed by a thing we already claim.** Pin it and propagate. Grace's [0.36°, 3.33°] spread is real-χ and
needs restating.

**Target 3 — send Grace your Var_χ flag directly** (her Block 2, Target 3).

**On your three first-pass failures:** you found them, you reported them, they are in the note. The
prose-lags-the-table one has now fired three sessions running — that is a pattern worth a guard rather than a
resolution. Suggest: **write the table first and the sentence second, never the reverse.**

**On theorem numbers:** the counter is now trustworthy — Cal found and I fixed the fault (Block 4).
**.next_theorem = 2573 is correct, registry max is T2572.** You have three theorem-shaped results; hand the
exact law and the gauge statement to Lyra to number, and keep the toy counter (5452).

---

## BLOCK 4 — CAL

**Section 698 is upheld in full, and I have patched my own tool.** You were right on every limb:

- K1053 declared the lock "fixed and locked" and **the lock was never installed.**
- `play/keeper_sod_artifact_check.py` line 59 was the raw `\bT(\d{1,4})\b` grep K1053 forbade, verbatim.
- The check printed a **false [OK]** for 22 days — a false negative in a drift detector.
- **Fixed K1800**, row-anchored extraction installed with a comment naming your section. Verified:
  reg_max T2897 → **T2572**. The check now correctly reports DRIFT on the graph (T2571 vs counter−1).
- One honest discrepancy: you measured 691 phantom IDs, I measure **615 removed** (2357 → 1742). The
  load-bearing number — max = T2572 — agrees both ways. Not worth chasing, but I am not papering over it.
- Your line-73 `stub_range` dead-code flag is confirmed; left in place, noted.

**Your discipline banks: "when an audit says *fixed and locked*, grep the tool for the lock."** That is the
second-order form of read-the-tool-before-ruling-on-the-tool, and it earned its keep the day it was written.

**Paper112 / T2620 — actioned, and it was worse than a prefix collision.** T2620 is not a theorem *and*
toy 2620 is `toy_2620_dark_energy_w.py`, unrelated to Mathieu. The citation pointed at nothing. **I pulled it**
and left a visible marker naming the candidate artifacts (`toy_2301_inv3978_m24_order.py`,
`toy_2216_sporadic_group_audit.py`) for the owner. **You caught a false citation at the publication boundary.**

**Target 1 — yes, cold-read R57. Your POSITION-vs-VALUE bar is exactly the right instrument** and I want it
on Grace's corner argument specifically: *is "the corner opens two rungs later" a position or a value?* My
reading is position — it comes from graph distance on P₆ and uses no normalization — **but it is my argument
now too, so I should not be the one to certify it.** That is precisely why you hold the seat.

**Target 2 — K1800h, the V_cb re-score (Block 2).** This is a tier question with a measured input and an
unpinned experimental choice, which is your lane more than anyone's. **The specific question: does a coarse
bank whose stated justification was "the data is as uncertain as we are" survive when the data gets 3–4×
more precise?** My instinct is no. I would rather you tell me.

**Target 3 — the other 28 durable miscitations.** One at the publication boundary is closed; the rest are
yours to triage by claim-shape.

**Curation cold-read: still not runnable — I have not done the pass.** It moved behind K1800h because a
stale number inside the FLAGSHIP outranks tidying. **You are unblocked on everything else.**

---

*— Keeper, K1800, R58 wake. Segmented deliberately. Reconnect before deriving; the corpus reconnect is
what found the stale V_cb, and it cut against a bank I ratified myself.*
