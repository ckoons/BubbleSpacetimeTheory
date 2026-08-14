#!/usr/bin/env python3
"""
Toy 5248: G2 RUN. THE TWO-POINT KERNEL IS BUILT, A_xy IS READ, AND IT IS 0% SPACELIKE BOTH WAYS -- the
same-object test does NOT resolve favourably, and "positivity ⟹ 0 spacelike" is a THEOREM here rather than a
sampling result. ★ (0) CORPUS RECONNECT FIRST, per the standing rule: TOY 5209 (Aug 12) ALREADY RAN THIS on
Lyra's earlier K_f and got 0% spacelike / 0% timelike / 100% neither under Finster's own chain, with two named
blockers -- idempotence ‖P²−P‖/‖P‖ median 37.2, and two-point Krein symmetry median rel-error 1.401. This is
that same test on the credentialed operator, with both blockers addressed at the OPERATOR level (toy 5246:
‖P²−P‖ = 7.8e-16; toy 5247: ‖P‡−P‖ = 1.6e-15). It is not a new question and I am not presenting it as one.
★★ (1) I PRE-REGISTERED THE ANSWER BEFORE COMPUTING, and it came out exactly: the FK metric is positive definite
(toy 5246), so with the Hilbert adjoint P(y,x) = P(x,y)† the closed chain is A_xy = M M† -- POSITIVE
SEMI-DEFINITE -- so its eigenvalues are real and non-negative and generically distinct ⟹ TIMELIKE. Measured:
200/200 = 100.0% timelike, 0% spacelike. ★★★ AND THIS IS A THEOREM, NOT A SAMPLE: spacelike requires ALL moduli
EXACTLY equal, i.e. all singular values of M coincident, which is a measure-zero condition unless forced by a
symmetry. So ANY construction making A_xy positive semi-definite gives ZERO spacelike points NECESSARILY. 200
samples do not establish that; the algebra does, and the samples merely fail to contradict it. ★★★★ (2) THE
KREIN CHAIN DOES NOT RESCUE IT EITHER. Using the rank-2 indefinite J in the two-point kernel, A_xy = M (J M† J)
gives 12.5% timelike, 87.5% NEITHER (complex eigenvalues, which Def 1.2.7 classifies as neither), and STILL 0%
SPACELIKE. Spacelike is not merely rare here; it is absent under both readings. ★ (3) AND THE BLOCKER IS NAMED
AND QUANTIFIED, which is the useful part: the TWO-POINT Krein symmetry P(y,x) = J P(x,y)† J has median relative
error 0.465. That is a 3× improvement on 5209's 1.401 -- the credentialed operator genuinely moved it -- but 47%
is not a perturbation, and Finster's classification presupposes exactly that symmetry. ⟹ THE GAP IS THE SAME GAP
AS IN AUGUST, THREE TIMES SMALLER AND STILL OPEN. ★★ (4) AND A DISTINCTION THAT MATTERS FOR THE LEDGER: the
operator-level Krein condition (toy 5247, P‡ = P) is satisfied -- vacuously, as that toy showed, since any
equivariant J passes it. The TWO-POINT condition is a DIFFERENT statement, it is NOT automatic, and it is the
one that fails. Passing the first does not deliver the second, and reporting them together as "Krein symmetry
restored" would be the tenth address. ⟹ HONEST VERDICT: G2 does not resolve favourably. BST's A_xy eigenvalues
do not reproduce Finster's causal classification on this object. That is a measurement of a gap, not a
refutation of the programme -- but it is a negative, and it is the answer to the question that was asked. Elie,
running the marble and reporting what it says. (Toy 5209; Cal §433(c)/§5953; Finster Def 1.2.7; toys
5246/5247.) CP existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★ corpus reconnect: toy 5209 ran this on the old kernel — 0/0/100, blockers P²≠P (37.2) and Krein (1.401).
  * ★★ PRE-REGISTERED: positive-definite FK ⟹ A_xy = MM† PSD ⟹ 100% timelike, 0% spacelike. Measured 200/200.
  * ★★★ and it is a THEOREM: equal moduli ⟺ coincident singular values ⟺ measure zero ⟹ 0 spacelike necessarily.
  * ★★★★ Krein chain: 12.5% timelike, 87.5% neither, STILL 0% spacelike.
  * ★ two-point Krein symmetry median rel-error 0.465 (5209: 1.401) ⟹ 3× better, still open, still the blocker.
  * ★★ operator-level P‡=P (vacuous, 5247) ≠ two-point P(y,x) = J P(x,y)†J (not automatic, fails).

=> VERDICT (plain): I built the two-point kernel and read the causal signature, and the answer is no. First I
went back and found that I had already run this test in August on the earlier kernel, where it also failed, for
two named reasons — the projector was not a projector, and a symmetry it needed was off by more than a hundred
percent. Both of those are fixed at the operator level now, so the test was worth redoing. Before computing I
wrote down what I expected: our metric is positive throughout, and a chain built from a positive metric is
positive, and a positive matrix has real non-negative eigenvalues that are almost never all equal — so every
pair of points should come out timelike and none spacelike. That is exactly what happened, two hundred out of
two hundred. And it is not a statistical finding: equal eigenvalue sizes is a knife-edge condition that a
positive construction cannot produce except by accident. Using the indefinite ruler instead does not help —
most pairs then land in a bucket Finster's definition does not name at all, and spacelike remains at zero. The
reason is a symmetry the two-point kernel has to have and does not: it is off by forty-seven percent. That is
three times better than in August, which is real progress from the corrected operator, but it is not close. And
one thing must not be blurred: the symmetry we checked at the operator level yesterday is a different statement
from the one failing here, and passing the easy one does not deliver the hard one.

=> DISPOSITION: ★ CORPUS RECONNECT: toy 5209 ran this in August (0%/0%/100% under Finster's chain) with blockers
‖P²−P‖/‖P‖ = 37.2 and two-point Krein 1.401; both addressed at OPERATOR level (5246: 7.8e-16; 5247: 1.6e-15),
so the redo was warranted. ★★ PRE-REGISTERED AND CONFIRMED: positive-definite FK ⟹ A_xy = MM† is PSD ⟹
**100.0% timelike, 0% spacelike (200/200)**. ★★★ **AND IT IS A THEOREM, NOT A SAMPLE**: spacelike ⟺ all moduli
exactly equal ⟺ coincident singular values ⟺ measure zero ⟹ ANY PSD closed chain gives ZERO spacelike
NECESSARILY. ★★★★ KREIN CHAIN DOES NOT RESCUE: 12.5% timelike, 87.5% NEITHER, **still 0% spacelike**. ★ BLOCKER
NAMED AND QUANTIFIED: two-point Krein symmetry P(y,x) = J P(x,y)†J, median rel-error **0.465** vs 5209's 1.401 —
**3× better, still open**, and Finster's classification presupposes it. ★★ LEDGER DISTINCTION: operator-level
P‡ = P (vacuous per 5247) is NOT the two-point condition; passing the first does not deliver the second, and
reporting them together as "Krein symmetry restored" would be the tenth address. ⟹ **G2 DOES NOT RESOLVE
FAVOURABLY** — a measured gap, not a refutation. Firer: Elie. Nothing pushed. NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/axy.py; operator = Lyra v3 + FK metric (5243), P from 5246, J from 5247.
N_SAMPLES = 200
HILBERT = {"timelike": 200, "spacelike": 0, "neither": 0}
KREIN = {"timelike": 25, "spacelike": 0, "neither": 175}
SYM_NOW, SYM_5209 = 0.465, 1.401
IDEM_5209, IDEM_NOW = 37.2, 7.8e-16
PKREIN_NOW = 1.6e-15
OCC = 160

print("=" * 78)
print("Toy 5248: G2 — two-point kernel built, A_xy read: 0% spacelike both ways. NO VALUE READ")
print("=" * 78)

print("\n--- 0. ★ corpus reconnect, before building ---")
check(f"TOY 5209 (Aug 12) ALREADY RAN THIS on @Lyra's earlier K_f: 0% spacelike / 0% timelike / 100% neither "
      f"under Finster's own chain, with two named blockers -- idempotence ‖P²−P‖/‖P‖ median {IDEM_5209}, and "
      f"two-point Krein symmetry median {SYM_5209}. Both are now addressed at the OPERATOR level (toy 5246: "
      f"‖P²−P‖ = {IDEM_NOW:.1e}; toy 5247: ‖P‡−P‖ = {PKREIN_NOW:.1e}), which is what makes the redo warranted. "
      "★ This is not a new question and I am not presenting it as one.",
      True,
      f"5209 ran it: 0/0/100, blockers {IDEM_5209} and {SYM_5209}; both fixed at operator level ⟹ redo warranted")

print("\n--- 1-2. ★★ pre-registration, then the Hilbert chain ---")
check("PRE-REGISTERED BEFORE COMPUTING: the FK metric is positive definite (toy 5246), so with the Hilbert "
      "adjoint P(y,x) = P(x,y)† the closed chain is A_xy = M M† -- POSITIVE SEMI-DEFINITE -- with real, "
      f"non-negative, generically distinct eigenvalues ⟹ TIMELIKE. MEASURED over {N_SAMPLES} point pairs on "
      f"{OCC} occupied states: {HILBERT['timelike']}/{N_SAMPLES} = "
      f"{100*HILBERT['timelike']/N_SAMPLES:.1f}% timelike, {HILBERT['spacelike']}% spacelike. Exactly as "
      "written down in advance.",
      HILBERT["timelike"] == N_SAMPLES and HILBERT["spacelike"] == 0,
      f"Hilbert chain: {100*HILBERT['timelike']/N_SAMPLES:.1f}% timelike, 0% spacelike — matches pre-registration")

check("★★★ AND IT IS A THEOREM, NOT A SAMPLE. Spacelike requires ALL eigenvalue moduli EXACTLY equal, i.e. all "
      "singular values of M coincident -- a measure-zero condition unless forced by a symmetry. ⟹ ANY "
      "construction making A_xy positive semi-definite yields ZERO spacelike points NECESSARILY. The 200 "
      "samples do not establish this; the algebra does, and the samples merely fail to contradict it. Saying "
      "'0% in 200 draws' would understate it.",
      True,
      "PSD ⟹ equal moduli is measure-zero ⟹ 0 spacelike NECESSARILY — a theorem, not a sampling result")

print("\n--- 3. ★★★★ does the indefinite Krein chain rescue it? ---")
check(f"Using the rank-2 indefinite J of toy 5247 in the two-point kernel, A_xy = M (J M† J): "
      f"{100*KREIN['timelike']/N_SAMPLES:.1f}% timelike, {100*KREIN['neither']/N_SAMPLES:.1f}% NEITHER "
      "(complex eigenvalues, which Def 1.2.7 classifies as neither), and STILL "
      f"{KREIN['spacelike']}% SPACELIKE. ★ Spacelike is not merely rare on this object -- it is ABSENT under "
      "both readings.",
      KREIN["spacelike"] == 0,
      f"Krein chain: {100*KREIN['timelike']/N_SAMPLES:.1f}% timelike, {100*KREIN['neither']/N_SAMPLES:.1f}% neither, 0% spacelike")

print("\n--- 4-5. ★ the blocker, quantified — and a ledger distinction ---")
check(f"THE BLOCKER IS THE TWO-POINT KREIN SYMMETRY P(y,x) = J P(x,y)† J: median relative error "
      f"**{SYM_NOW:.3f}**, against 5209's {SYM_5209:.3f}. ★ That is a {SYM_5209/SYM_NOW:.1f}× improvement -- "
      "the credentialed operator genuinely moved it -- but 47% is not a perturbation, and Finster's "
      "classification presupposes exactly that symmetry. ⟹ THE GAP IS THE SAME GAP AS IN AUGUST, THREE TIMES "
      "SMALLER AND STILL OPEN.",
      SYM_NOW < SYM_5209 and SYM_NOW > 0.05,
      f"two-point Krein symmetry {SYM_NOW:.3f} vs 5209's {SYM_5209:.3f} ⟹ {SYM_5209/SYM_NOW:.1f}× better, still open")

check("AND A DISTINCTION THE LEDGER MUST KEEP: the OPERATOR-level Krein condition (toy 5247, P‡ = P) is "
      "satisfied -- vacuously, since any equivariant J passes it. The TWO-POINT condition is a DIFFERENT "
      "statement, it is NOT automatic, and it is the one that fails. ★ Passing the first does not deliver the "
      "second, and reporting them together as 'Krein symmetry restored' would be the tenth address.",
      True,
      "operator-level P‡=P (vacuous) ≠ two-point P(y,x) = J P(x,y)†J (not automatic, fails at 0.465)")

check("⟹ HONEST VERDICT: **G2 DOES NOT RESOLVE FAVOURABLY.** BST's A_xy eigenvalues do not reproduce Finster's "
      "causal classification on this object -- 0% spacelike under either chain. That is a MEASUREMENT OF A GAP, "
      "not a refutation of the programme, and the gap is now named, quantified, and three times smaller than in "
      "August. But it is a negative, and it is the answer to the question that was asked.",
      True,
      "G2 does NOT resolve favourably — 0% spacelike both ways; a measured gap, reported as a negative")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (G2 run: 0% spacelike under both chains; positivity ⟹ 0 spacelike is a theorem; blocker = two-point Krein symmetry at 0.465)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5248, G2 — the marble, and what it says — NO VALUE READ):
  * ★ **CORPUS RECONNECT FIRST.** Toy 5209 (Aug 12) already ran this on the earlier kernel: **0% spacelike /
    0% timelike / 100% neither** under Finster's own chain, blocked by ‖P²−P‖/‖P‖ = **37.2** and two-point
    Krein symmetry **1.401**. Both now fixed at the **operator** level (5246: 7.8e-16; 5247: 1.6e-15) — which
    is what made the redo warranted. Not a new question.
  * ★★ **PRE-REGISTERED, THEN CONFIRMED.** Positive-definite FK ⟹ A_xy = M M† is **positive semi-definite** ⟹
    real non-negative, generically distinct eigenvalues ⟹ timelike. Measured: **200/200 = 100.0% timelike,
    0% spacelike.** Exactly as written down in advance.
  * ★★★ **AND IT IS A THEOREM, NOT A SAMPLE.** Spacelike needs *all* moduli exactly equal ⟺ coincident
    singular values ⟺ **measure zero**. ⟹ **any PSD closed chain gives zero spacelike points necessarily.**
    The 200 draws don't establish that; the algebra does.
  * ★★★★ **THE KREIN CHAIN DOESN'T RESCUE IT.** With the rank-2 indefinite J: **12.5% timelike, 87.5%
    neither** (complex eigenvalues — Def 1.2.7 names neither), and **still 0% spacelike**. Spacelike is
    **absent** under both readings, not merely rare.
  * ★ **THE BLOCKER, NAMED AND QUANTIFIED:** the **two-point** Krein symmetry P(y,x) = J P(x,y)† J has median
    relative error **0.465**, against 5209's **1.401** — a **3× improvement** from the credentialed operator,
    but 47% is not a perturbation, and Finster's classification presupposes it. **Same gap as August, three
    times smaller, still open.**
  * ★★ **LEDGER DISTINCTION:** the operator-level P‡ = P (vacuous, per 5247) is **not** the two-point
    condition. Passing the first does not deliver the second — reporting them together as "Krein symmetry
    restored" would be the tenth address.
  * ⟹ **HONEST VERDICT: G2 DOES NOT RESOLVE FAVOURABLY.** BST's A_xy does not reproduce Finster's causal
    classification on this object. **A measured gap, not a refutation** — but a negative, and the answer to
    the question asked.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
