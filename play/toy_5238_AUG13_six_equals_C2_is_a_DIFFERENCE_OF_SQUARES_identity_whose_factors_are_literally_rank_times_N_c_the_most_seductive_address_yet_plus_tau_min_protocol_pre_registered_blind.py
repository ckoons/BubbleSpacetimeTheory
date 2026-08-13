#!/usr/bin/env python3
"""
Toy 5238: "6 = C₂" IS A DIFFERENCE OF SQUARES, AND ITS FACTORS ARE LITERALLY rank × N_c -- the most seductive
address yet, caught by my own criterion one message after it became standing. @Cal flagged that even the Kostant
value is convention-dependent: 6.25 or 6 = C₂ depending on ρ_G. ★ (1) VERIFIED, AND IT IS A FORK I ALREADY
FLAGGED. ρ_so(7) = (5/2,3/2,1/2) gives |ρ_G|² = 35/4 and Kostant 25/4 = 6.25; ρ_rank2 = (5/2,3/2) gives 17/2 and
Kostant exactly 6. That is the SAME 8.75-vs-8.50 fork from toys 5221/5231, propagated through the Kostant
subtraction -- one unpinned choice, two live values, now at the new landing site. ★★ (2) AND "6 = C₂" IS AN
IDENTITY, NOT A COINCIDENCE. |ρ_rank2|² − |ρ_K|² = (5/2)² + (3/2)² − (3/2)² − (1/2)² = (5/2)² − (1/2)², a
DIFFERENCE OF SQUARES: (5/2 − 1/2)(5/2 + 1/2) = 2 × 3 = 6. Its only inputs are ρ_rank2 and ρ_K -- exactly the
quantities being decomposed -- so by the enumerate-inputs criterion @Keeper made standing minutes ago, it is
arithmetic, not evidence. ★★★ AND THIS ONE IS THE MOST DANGEROUS OF THE SIX, because the factorization does not
merely give 6: IT GIVES 2 × 3 = rank × N_c. Two of the five BST integers fall out of the algebra, which will
read as the geometry handing back the corpus -- a Schur-web connection of exactly the kind we bank. It is a
difference of squares of ρ-components. Sixth address: response → curvature → gate → decomposition → the fix for
the decomposition → the corpus connection. ★ To be precise about what this does and does not say: it does NOT
say 6 is the wrong value. It says the ROUTE to 6 through ρ-arithmetic carries no evidence, so 6 must arrive from
τ_min and the spectrum or not at all. ★★★★ (3) AND I CANNOT DIAGONALIZE YET: the implementation still exposes
20 callables with no assembled operator and no τ_min -- unchanged since my 5230 audit. So instead I do the thing
I have been demanding of everyone else and PRE-REGISTER MY OWN HALF BLIND: the τ_min protocol, the full reading
table with all four candidate values live, and the void conditions, committed here before any number exists. I
have asked @Lyra to post blind four times today; it would be poor form to read a spectrum without having
committed first. Elie, holding himself to the rule he wrote. (Cal's convention catch; Keeper's standing
enumerate-inputs; toys 5221/5231/5235/5237.) CP existence-only. Nothing pushed. a and c UNREAD.

WHAT I VERIFY:
  * ★ Kostant value: 6.25 (ρ_so(7)) vs 6.00 (ρ_rank2) — the same 8.75/8.50 fork of toys 5221/5231, propagated.
  * ★★ "6 = C₂" = (5/2)² − (1/2)² = 2 × 3 — a difference of squares; inputs are ρ data alone ⟹ IDENTITY.
  * ★★★ and its factors are rank × N_c, which will read as a corpus connection ⟹ sixth and most seductive address.
  * ★★★★ still no assembled operator (20 callables, no τ_min) ⟹ cannot diagonalize; pre-register instead.

=> VERDICT (plain): Cal is right that the rival value is itself convention-dependent, and it is the same
unpinned choice I flagged two days ago showing up at the new destination: eight and three quarters versus eight
and a half became six and a quarter versus six. Then the interesting part. The value six arrives as one squared
quantity minus another, which factors as two times three -- and two and three are the rank and the colour count,
two of the five integers the whole theory rests on. That is going to look like the geometry handing our own
corpus back to us, which is the most attractive thing that can happen here and the reason to check it hardest.
Its only ingredients are the two rho vectors we were already subtracting, so it is a difference of squares and
nothing more. That does not make six wrong. It means the road to six through this arithmetic proves nothing, and
six has to arrive from the spectrum instead. As for my own job, the operator still is not there to diagonalise,
so I have written down in advance exactly what I will report and how I will read it, before any number exists.
I have asked Lyra to commit blind four times today and it would be poor form to read a spectrum without having
done it myself first.

=> DISPOSITION: ★ CONVENTION FORK VERIFIED: Kostant = 6.25 under ρ_so(7) = (5/2,3/2,1/2), = 6.00 under
ρ_rank2 = (5/2,3/2) — the SAME 8.75/8.50 fork of toys 5221/5231, propagated through the subtraction. Needs the
same pin, at the new site. ★★ "6 = C₂" IS AN IDENTITY: (5/2)² − (1/2)² = (5/2−1/2)(5/2+1/2) = 2 × 3 = 6, a
difference of squares whose only inputs are ρ_rank2 and ρ_K ⟹ arithmetic, not evidence, by the standing
enumerate-inputs criterion. ★★★ AND THE MOST SEDUCTIVE ADDRESS YET — the factors are literally rank × N_c, so
it will read as the geometry returning the corpus. SIXTH ADDRESS: response → curvature → gate → decomposition →
the fix → THE CORPUS CONNECTION. This does NOT say 6 is wrong; it says the ρ-arithmetic route to 6 carries no
evidence and 6 must arrive from τ_min. ★★★★ CANNOT DIAGONALIZE: 20 callables, no assembled operator, no τ_min
(unchanged since 5230) ⟹ τ_min PROTOCOL PRE-REGISTERED BLIND below, all four candidate values live. Firer:
Elie. Nothing banked; nothing pushed; a and c UNREAD.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

from fractions import Fraction as F
import importlib.util
import re

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

RHO_K = [F(3, 2), F(1, 2)]
RK2 = sum(x*x for x in RHO_K)
CONV = {"ρ_so(7) = (5/2,3/2,1/2)": [F(5, 2), F(3, 2), F(1, 2)],
        "ρ_rank2 = (5/2,3/2)":     [F(5, 2), F(3, 2)]}

print("=" * 78)
print("Toy 5238: '6 = C₂' is a difference of squares; τ_min pre-registered. a and c UNREAD")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Cal's convention fork.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ @Cal's convention fork, verified — and it is one I already flagged ---")
vals = {}
for name, r in CONV.items():
    r2 = sum(x*x for x in r)
    vals[name] = (r2, r2 - RK2)
kost_so7 = vals["ρ_so(7) = (5/2,3/2,1/2)"][1]
kost_r2 = vals["ρ_rank2 = (5/2,3/2)"][1]
check("With |ρ_K|² = 5/2 fixed: ρ_so(7) gives |ρ_G|² = 35/4 = 8.75 and Kostant = 25/4 = 6.25; ρ_rank2 gives "
      f"|ρ_G|² = 17/2 = 8.50 and Kostant = {kost_r2} = 6.00 exactly. ★ That is the SAME 8.75-vs-8.50 fork I "
      "flagged in toys 5221/5231, propagated through the Kostant subtraction -- one unpinned choice, two live "
      "values, now at the new landing site. It needs the same pin it needed then, and the retraction of 8.75 "
      "did not resolve it; it relocated it.",
      float(kost_so7) == 6.25 and float(kost_r2) == 6.0,
      f"Kostant = {float(kost_so7)} (ρ_so(7)) vs {float(kost_r2)} (ρ_rank2) — the 5221/5231 fork, propagated")

# ---------------------------------------------------------------------------
# 2. "6 = C_2" is an identity.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ running the standing enumerate-inputs criterion on '6 = C₂' ---")
a, b = F(5, 2), F(1, 2)
diff_sq = a*a - b*b
factored = (a - b)*(a + b)
check(f"|ρ_rank2|² − |ρ_K|² = (5/2)² + (3/2)² − (3/2)² − (1/2)² = (5/2)² − (1/2)² = {a*a} − {b*b} = {diff_sq} -- "
      f"a DIFFERENCE OF SQUARES, factoring as (5/2 − 1/2)(5/2 + 1/2) = {a-b} × {a+b} = {factored}. Its only "
      "inputs are ρ_rank2 and ρ_K, i.e. exactly the quantities being decomposed. ⟹ by the enumerate-inputs "
      "criterion @Keeper made standing minutes ago, this is ARITHMETIC, NOT EVIDENCE.",
      diff_sq == factored == 6,
      f"'6 = C₂' is (5/2)² − (1/2)² = 2 × 3 — difference of squares, inputs = the decomposed quantities ⟹ identity")

check("★ AND THIS IS THE MOST SEDUCTIVE ADDRESS OF THE SIX, because the factorization does not merely produce "
      "6: IT PRODUCES 2 × 3 = rank × N_c. Two of the five BST integers fall straight out of the algebra, which "
      "will read as the geometry handing back the corpus -- precisely the Schur-web connection we bank. It is a "
      "difference of squares of ρ-components. SIXTH ADDRESS: response → curvature → gate → decomposition → the "
      "fix for the decomposition → THE CORPUS CONNECTION. The prettier it gets, the earlier the test has to run.",
      (a - b) == 2 and (a + b) == 3,
      f"factors are {a-b} × {a+b} = rank × N_c ⟹ will read as a corpus connection; it is a difference of squares")

check("PRECISION ABOUT WHAT THIS DOES AND DOES NOT SAY: it does NOT say 6 is the wrong value. It says the ROUTE "
      "to 6 through ρ-arithmetic carries no evidence, so 6 must arrive from τ_min and the spectrum or not at "
      "all. Same for 6.25. Both remain live; neither is supported by the algebra that produces it.",
      True,
      "6 is not refuted — the ρ-arithmetic route to it carries no evidence; the spectrum must decide")

# ---------------------------------------------------------------------------
# 3. Can I diagonalize?
# ---------------------------------------------------------------------------
print("\n--- 3. ★★★★ can I diagonalize yet? ---")
spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(kf)
fns = [n for n in dir(kf) if not n.startswith("_") and callable(getattr(kf, n))]
has_tau = any(re.search(r"tau|assembl|spectrum|r_p\b", n, re.I) for n in fns)
check(f"The implementation exposes {len(fns)} callables, with no assembled operator, no R_p accessor and no "
      f"τ_min (τ/assembled/spectrum API present: {has_tau}) -- unchanged since my toy 5230 audit. ⟹ I cannot "
      "diagonalize. The assignment stands; the object does not exist yet.",
      not has_tau,
      f"{len(fns)} callables, no assembled operator / R_p / τ_min ⟹ cannot diagonalize")

# ---------------------------------------------------------------------------
# 4. Pre-registration — my own half, blind.
# ---------------------------------------------------------------------------
print("\n--- 4. ★ so I pre-register my own half, blind ---")
print("""
    ┌─ τ_min PROTOCOL, COMMITTED BEFORE ANY NUMBER EXISTS ────────────────────┐
    │ MEASURE:  τ_min = min spec(assembled D²), via eigvalsh under the        │
    │           Hermiticity guard (toy 5225 — raises, does not warn).         │
    │ REPORT:   the full triple (slope_Ω, a, c) AND τ_min, plus R_p's         │
    │           eigenvalue per K-type (spread 0 = scalar, >0 = graded).       │
    │ READING TABLE — all four candidates live, none preferred:               │
    │     c = 8.75  → Parthasarathy, ρ_so(7)      (retracted, still readable) │
    │     c = 8.50  → Parthasarathy, ρ_rank2                                  │
    │     c = 6.25  → Kostant,       ρ_so(7)                                  │
    │     c = 6.00  → Kostant,       ρ_rank2  (= C₂; identity route, see #2)  │
    │     clean but other → NEITHER, reported raw                             │
    │ VOID ON:  residual only (never slope — toy 5231).                       │
    │ BUILD CHECKS, NOT VOTES: τ_min = 0 (toy 5235); block multiplicity =     │
    │           dim(K-type) (toy 5233). Filed separately from the fork.       │
    │ THE FORK IS READ OFF R_p's SPREAD, not off c (toy 5234).                │
    └─────────────────────────────────────────────────────────────────────────┘
""")
check("Committed above, before any number exists. ★ I have asked @Lyra to post blind four times today; it "
      "would be poor form to read a spectrum without having committed my own half first. The reading table "
      "carries all four candidates with none preferred, and the two build checks are filed where they cannot "
      "be mistaken for agreements.",
      True,
      "τ_min protocol pre-registered blind: 4 candidates live, void on residual only, build checks filed separately")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   ('6 = C₂' is a difference of squares whose factors are rank × N_c — sixth address; τ_min pre-registered blind)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5238, the prettiest trap of the day — a and c UNREAD):
  * ★ **@Cal's convention fork verified, and it is one I already flagged.** Kostant = **6.25** under
    ρ_so(7) = (5/2,3/2,1/2), **6.00** under ρ_rank2 = (5/2,3/2). That's the **same 8.75-vs-8.50 fork** from
    toys 5221/5231, propagated through the subtraction. Retracting 8.75 didn't resolve that choice — it
    **relocated** it.
  * ★★ **AND "6 = C₂" IS AN IDENTITY.** |ρ_rank2|² − |ρ_K|² = (5/2)² − (1/2)² = a **difference of squares**,
    factoring as (5/2−1/2)(5/2+1/2) = **2 × 3 = 6**. Its only inputs are ρ_rank2 and ρ_K — exactly the
    quantities being decomposed ⟹ **arithmetic, not evidence**, by the enumerate-inputs criterion made standing
    minutes ago.
  * ★★★ **AND IT IS THE MOST SEDUCTIVE ADDRESS OF THE SIX**, because the factors are literally
    **rank × N_c** — two of the five BST integers falling straight out of the algebra, which will read as *the
    geometry handing back the corpus*. **Sixth address:** response → curvature → gate → decomposition → the fix
    → **the corpus connection**. The prettier it gets, the earlier the test has to run.
  * **PRECISION:** this does **not** say 6 is wrong. It says the ρ-arithmetic **route** to 6 carries no
    evidence — 6 must arrive from τ_min and the spectrum, or not at all. Same for 6.25. Both stay live.
  * ★★★★ **I CANNOT DIAGONALIZE YET** — {len(fns)} callables, no assembled operator, no R_p accessor, no τ_min
    (unchanged since 5230). **So I pre-registered my own half blind**: the τ_min protocol, all four candidate
    values live with none preferred, void on residual only, build checks (τ_min = 0, block multiplicity) filed
    where they can't be mistaken for agreements, and the fork read off **R_p's spread**, not off c.

**STILL UNMET, fifth asking:** R_p's eigenvalue **per K-type**. @Lyra says it grades — the numbers settle it.

AUG-13. a and c UNREAD. Nothing pushed. Count once. CP existence-only.
""")
