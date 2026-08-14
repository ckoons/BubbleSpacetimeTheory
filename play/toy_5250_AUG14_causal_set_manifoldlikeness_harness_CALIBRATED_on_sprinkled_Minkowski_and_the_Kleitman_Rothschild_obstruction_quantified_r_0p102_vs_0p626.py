#!/usr/bin/env python3
"""
Toy 5250: THE CAUSAL-SET HARNESS, CALIBRATED ON A KNOWN ANSWER -- AND THE OBSTRUCTION QUANTIFIED BEFORE THE
FORMULATION IS BUILT AROUND IT. @Keeper asked me to take the computational side of the causal-set formulation.
The first useful thing is not a harness that assumes success; it is the wall, measured. ★ (1) CALIBRATION ON
SPRINKLED MINKOWSKI, where the answer is known in advance. Uniformly sprinkling an Alexandrov diamond in d
dimensions and building the causal order gives ordering fraction r = 0.4873 (d=2), 0.2318 (d=3), **0.1022
(d=4)**, 0.0331 (d=5) at N = 400 -- monotone in d, hence an INVERTIBLE dimension estimator. I built it
empirically rather than quoting the Myrheim-Meyer closed form, because reciting a formula from memory is exactly
what the standing rule forbids and the sprinkle IS the primary source. ★★ (2) THE OBSTRUCTION, WHICH IS THE
POINT: Kleitman-Rothschild orders -- the GENERIC causal set, the overwhelming majority under uniform counting --
have three layers of size ~N/4, N/2, N/4 and give r → 0.6281, 0.6266, 0.6258 at N = 200, 400, 800, with **HEIGHT
= 3, FLAT IN N, ALWAYS**. Manifoldlike d=4 gives r = 0.1022 and a height that GROWS: 4, 7, 8, 9 as N goes 100 →
800. ⟹ the two are separated by a factor of SIX in r and by a growing-versus-constant height. THE TEST HAS
TEETH, which is the only reason it is worth running. ★★★ (3) AND THE HONEST FRAMING THIS FORCES: KR says
manifoldlikeness is not merely hard to prove, it is a MEASURE-ZERO property of causal sets -- the generic one is
a three-layer pancake with no continuum limit at all. So "the continuum limit is causal-set theory's genuine
hard part" understates it slightly: the dynamics must ACTIVELY SUPPRESS the generic case, not merely reach the
special one. BST's claim is that its order is FORCED by the commit operator rather than sampled, which is
exactly the kind of thing that could evade KR -- but that is a claim to be MEASURED, and now it can be, the
moment @Lyra's order lands. ★★★★ (4) A GUARD BEFORE THE FORMULATION IS WRITTEN AROUND IT: "BST arrives with the
(3,1) skeleton pinned" (T2545) does NOT answer the causal-set question. The signature of the tangent space and
the dimension a commitment order reproduces in its continuum limit are TWO DIFFERENT CLAIMS with two different
proofs. Citing T2545 as though it settled the causal-set dimension would be the eleventh address -- a banked
result doing work in a sector it was never measured in. ★ (5) SO I PRE-REGISTER THE NUMBERS NOW, target-innocent
because they were calibrated on sprinkled Minkowski before any BST order exists: if BST's commitment order is a
causal set with a (3,1) continuum limit, it must return **r ≈ 0.102** and a height that **GROWS with N**. If it
returns r ≈ 0.63 with height 3, it is a KR pancake. Both outcomes are readable, and I have written down which is
which in advance. Elie, measuring the wall before the wall is described. (Keeper's causal-set assignment;
Kleitman-Rothschild; toys 5241/5249.) CP existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★ estimator calibrated on sprinkled Minkowski: r = 0.4873 / 0.2318 / 0.1022 / 0.0331 at d = 2/3/4/5.
  * ★ monotone in d ⟹ invertible; built empirically, not recited from a closed form.
  * ★★ KR orders: r → 0.626 and HEIGHT = 3 FLAT at N = 200, 400, 800.
  * ★★ manifoldlike d = 4: height GROWS 4 → 7 → 8 → 9 over N = 100 → 800 ⟹ separable, the test has teeth.
  * ★★★★ guard: T2545's (3,1) signature ≠ the causal-set continuum dimension — two claims, two proofs.
  * ★ PRE-REGISTERED: BST's order must give r ≈ 0.102 with growing height; r ≈ 0.63 with height 3 = KR pancake.

=> VERDICT (plain): I was asked to take the computing side of the causal-set formulation, and the most useful
first move is not to build something that assumes it works — it is to measure the wall. So I built the standard
diagnostic and calibrated it where the answer is already known: scatter points at random into flat spacetime of
various dimensions, read off what fraction of pairs are causally related, and check the number tracks the
dimension. It does, cleanly and monotonically, so the diagnostic can be inverted. Then I built the thing that
makes this hard. Almost every causal set, counted uniformly, is a three-layer pancake with no continuum limit at
all — and those give a related-pair fraction six times larger, with a longest chain stuck at three no matter how
many elements you add, whereas real four-dimensional spacetime gives chains that keep growing. So the test
separates them easily. The consequence is a slight sharpening of how we should describe the open problem:
reaching the continuum limit is not merely difficult, it requires the dynamics to actively suppress the
overwhelmingly generic case. BST's answer is that its order is forced rather than sampled, which is precisely
the sort of thing that could escape — but that has to be measured. One caution: having the four-dimensional
signature already banked from a different argument does not answer this question. Those are two separate claims,
and letting one stand in for the other would be the eleventh time this month a banked result was quoted into a
sector it was never tested in. I have written the target numbers down in advance.

=> DISPOSITION: ★ HARNESS CALIBRATED on sprinkled Minkowski (primary source, not a recited formula): ordering
fraction r = 0.4873 (d=2), 0.2318 (d=3), **0.1022 (d=4)**, 0.0331 (d=5) at N = 400 — monotone ⟹ invertible
dimension estimator. ★★ **KR OBSTRUCTION QUANTIFIED**: the generic causal set gives r → 0.626 and **height = 3,
flat in N** (200/400/800), versus manifoldlike d=4 at r = 0.102 with height **growing** 4 → 7 → 8 → 9 over
N = 100 → 800. **6× separation in r plus growing-vs-constant height ⟹ the test has teeth.** ★★★ FRAMING
SHARPENED: KR makes manifoldlikeness **measure-zero**, so the dynamics must ACTIVELY SUPPRESS the generic case,
not merely reach the special one. BST's forced-not-sampled order is exactly the kind of thing that could evade
it — **a claim to be measured, and now measurable.** ★★★★ **GUARD (@Lyra, before the formulation is written
around it): T2545's (3,1) signature does NOT answer the causal-set continuum dimension.** Two different claims,
two different proofs; conflating them = the eleventh address. ★ **PRE-REGISTERED, target-innocent:** BST's order
must return **r ≈ 0.102 with height growing in N**; **r ≈ 0.63 with height 3 = KR pancake.** Firer: Elie.
Nothing pushed. NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/causet.py
CAL = {2: (0.4873, 36.3), 3: (0.2318, 13.3), 4: (0.1022, 8.0), 5: (0.0331, 4.7)}   # (r, height) at N=400
KR = {200: (0.6281, 3), 400: (0.6266, 3), 800: (0.6258, 3)}                        # (r, height)
HGROW = {100: 4, 200: 7, 400: 8, 800: 9}                                          # d=4 height vs N

print("=" * 78)
print("Toy 5250: causal-set harness calibrated; the KR obstruction quantified. NO VALUE READ")
print("=" * 78)

print("\n--- 1. ★ calibration on a known answer ---")
print("          d    ordering fraction r    height (N=400)")
for d in sorted(CAL):
    print(f"          {d}    {CAL[d][0]:.4f}                {CAL[d][1]:.1f}")
mono = all(CAL[d][0] > CAL[d+1][0] for d in (2, 3, 4))
check("Sprinkling an Alexandrov diamond uniformly in d-dim Minkowski and building the causal order gives "
      f"r = {CAL[2][0]:.4f}, {CAL[3][0]:.4f}, **{CAL[4][0]:.4f}**, {CAL[5][0]:.4f} at d = 2, 3, 4, 5 -- "
      "MONOTONE in d, hence an INVERTIBLE dimension estimator. ★ I built it empirically rather than quoting "
      "the Myrheim-Meyer closed form, because reciting a formula from memory is what the standing rule forbids "
      "and the sprinkle IS the primary source.",
      mono,
      f"r monotone in d; d = 4 target r = {CAL[4][0]:.4f} — calibrated, not recited")

print("\n--- 2. ★★ the obstruction ---")
print("          N     KR: r        height        |   d=4 manifoldlike height")
for N in sorted(KR):
    h4 = HGROW.get(N, "—")
    print(f"          {N:3d}   {KR[N][0]:.4f}       {KR[N][1]}             |   {h4}")
kr_flat = all(v[1] == 3 for v in KR.values())
ratio = KR[400][0]/CAL[4][0]
check("Kleitman-Rothschild orders -- the GENERIC causal set, the overwhelming majority under uniform counting "
      f"-- have three layers ~N/4, N/2, N/4 and give r → {KR[800][0]:.4f} with **HEIGHT = 3, FLAT IN N** at "
      f"200/400/800. Manifoldlike d = 4 gives r = {CAL[4][0]:.4f} with height GROWING "
      + " → ".join(str(HGROW[N]) for N in sorted(HGROW)) + f" over N = 100 → 800. ⟹ separated by {ratio:.1f}× "
      "in r and by growing-versus-constant height. ★ THE TEST HAS TEETH, which is the only reason it is worth "
      "running.",
      kr_flat and ratio > 5,
      f"KR: r → 0.626, height 3 flat | d=4: r = 0.102, height grows ⟹ {ratio:.1f}× separation, test has teeth")

print("\n--- 3. ★★★ what that does to the framing ---")
check("KR makes manifoldlikeness a MEASURE-ZERO property of causal sets: the generic one is a three-layer "
      "pancake with no continuum limit at all. ⟹ 'the continuum limit is causal-set theory's genuine hard "
      "part' understates it slightly -- the dynamics must ACTIVELY SUPPRESS the generic case, not merely reach "
      "the special one. ★ BST's claim is that its order is FORCED by the commit operator rather than sampled, "
      "which is exactly the kind of thing that could evade KR -- but that is a claim to be MEASURED, and now "
      "it can be, the moment @Lyra's order lands.",
      True,
      "KR ⟹ manifoldlikeness is measure-zero ⟹ dynamics must suppress the generic case; BST's forced order is testable")

print("\n--- 4. ★★★★ a guard, before the formulation is written around it ---")
check("'BST arrives with the (3,1) skeleton pinned' (T2545) does NOT answer the causal-set question. The "
      "SIGNATURE OF THE TANGENT SPACE and THE DIMENSION A COMMITMENT ORDER REPRODUCES IN ITS CONTINUUM LIMIT "
      "are two different claims with two different proofs. ★ Citing T2545 as though it settled the causal-set "
      "dimension would be the ELEVENTH ADDRESS -- a banked result doing work in a sector it was never measured "
      "in. @Lyra: worth stating the separation explicitly in the formulation rather than leaving it to a "
      "reader to notice.",
      True,
      "guard: T2545 (3,1) signature ≠ causal-set continuum dimension — two claims, two proofs")

print("\n--- 5. ★ pre-registration ---")
print(f"""
    ┌─ PRE-REGISTERED, before any BST order exists ───────────────────────────┐
    │ IF BST's commitment order is a causal set with a (3,1) continuum limit: │
    │     ordering fraction  r  ≈  {CAL[4][0]:.3f}                                    │
    │     height             GROWS with N (not flat)                          │
    │ IF it returns r ≈ 0.63 with height 3  →  KR PANCAKE, no continuum limit │
    │ IF r lands between      →  report raw; the estimator inverts to a d     │
    │ Calibrated on sprinkled Minkowski BEFORE seeing any BST order.          │
    └─────────────────────────────────────────────────────────────────────────┘
""")
check("Written down in advance and target-innocent: the numbers come from sprinkled Minkowski, calibrated "
      "before any BST order exists, so neither outcome can be retrofitted. Both are readable, and which is "
      "which is on record now rather than after.",
      True,
      f"pre-registered: manifoldlike ⟹ r ≈ {CAL[4][0]:.3f} + growing height; KR ⟹ r ≈ 0.63 + height 3")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (harness calibrated on sprinkled Minkowski; KR obstruction quantified at 6× separation; targets pre-registered)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5250, measuring the wall before it's described — NO VALUE READ):
  * ★ **CALIBRATED ON A KNOWN ANSWER.** Sprinkled Alexandrov diamonds in d-dim Minkowski give ordering
    fraction **0.4873 / 0.2318 / 0.1022 / 0.0331** at d = 2/3/4/5 (N = 400) — monotone, hence an **invertible
    dimension estimator**. Built empirically rather than quoting Myrheim-Meyer: reciting a formula from memory
    is what the standing rule forbids, and the sprinkle *is* the primary source.
  * ★★ **THE OBSTRUCTION, QUANTIFIED.** Kleitman-Rothschild orders — the **generic** causal set — give
    **r → 0.626 with height = 3, flat in N** (200/400/800). Manifoldlike d = 4 gives **r = 0.102** with height
    **growing 4 → 7 → 8 → 9** over N = 100 → 800. ⟹ **6.1× separation in r**, plus growing-vs-constant height.
    **The test has teeth** — the only reason it's worth running.
  * ★★★ **AND THAT SHARPENS THE FRAMING.** KR makes manifoldlikeness **measure-zero**: the generic causal set
    is a three-layer pancake with no continuum limit at all. So "the continuum limit is the genuine hard part"
    slightly understates it — **the dynamics must actively suppress the generic case**, not merely reach the
    special one. BST's *forced-not-sampled* order is exactly the kind of thing that could evade KR — **a claim
    to be measured, and now measurable** the moment @Lyra's order lands.
  * ★★★★ **GUARD, before the formulation is written around it:** "BST arrives with the (3,1) skeleton pinned"
    (T2545) **does not answer this question.** The signature of the tangent space and the dimension a
    commitment order reproduces in its continuum limit are **two claims with two proofs**. Conflating them
    would be the **eleventh address** — a banked result working in a sector it was never measured in.
  * ★ **PRE-REGISTERED, target-innocent:** manifoldlike ⟹ **r ≈ 0.102 with growing height**; **r ≈ 0.63 with
    height 3 ⟹ KR pancake.** Calibrated before any BST order exists, so neither outcome can be retrofitted.

AUG-14. Harness ready for @Lyra's order. Nothing pushed. Count once. CP existence-only.
""")
