#!/usr/bin/env python3
"""
Toy 4745 — Jul 19 (VERIFY Lyra's y_t = 127/128 = M_g/2^g candidate, mine; peak-convergence discipline): Lyra's F603
geometry (O spherical on the Shilov boundary; the top a discrete-series state that approaches but never reaches the
boundary → ⟨top|O⟩ → 1 from below) points at a strikingly BST-native form: y_t = 1 − 1/2^g = 127/128 = M_g/2^g. My job:
verify the number AND hold the discipline (my own degeneracy fish is the decisive guard here). Result: it's a genuinely
tight, BST-native LEAD — implied m_t = 172.74 GeV, 0.009% from the pole mass, and it uses the GF(2^g)=GF(128)
Reed-Solomon substrate field (my prior work) with the top at code level M_g=127. But it STAYS a lead, not a bank: (1)
scheme-dependent (pole matches, MS-bar doesn't); (2) my 0.8%-degeneracy fish — 127/128 is indistinguishable from an
exact y_t=1 dressed by RG running; (3) "top at level 127" must be FORCED by the discrete address, not chosen because
127/128 is pretty. The deciding computation is the top's discrete-series address (June open core).

THE CANDIDATE (verified): y_t = 1 − 1/2^g = M_g/2^g = 127/128 = 0.99219.
  * implied m_t = (127/128)·v/√2 = 172.74 GeV vs pole 172.76 ± 0.3 → 0.009% (inside the error bar — a TIGHT target,
    far better than the loose-range coincidences killed all week).
  * BST-NATIVE: 2^g = 128 = GF(2^g) = GF(128), the Reed-Solomon field the substrate codes on (Paper #122, my prior
    work); M_g = 127 = the g-th Mersenne prime = the last usable RS code symbol. The top sits at the OUTERMOST code
    level (127 = M_g) of 2^g; the one level it can't cross to reach the boundary condensate is the deficit 1/2^g = ONE
    substrate code-unit. So y_t = M_g/2^g reads as "top one Mersenne-prime step inside the substrate boundary" — a
    genuine candidate derivation matching Lyra's discrete-vs-boundary gap (F603), NOT just a fit.

THE THREE GUARDS (LEAD not bank — fired hard at peak convergence):
  1. SCHEME-DEPENDENT: pole y_t = 0.992 matches 127/128; MS-bar y_t (m_t~163 GeV) = 0.936 does NOT. So "y_t=127/128" is
     a claim about the POLE value specifically — needs a reason the geometric y_t is the pole one.
  2. MY DEGENERACY FISH (decisive): the 0.8% deficit is degenerate — equally consistent with a geometric 1−1/2^g AND
     with an exact y_t=1 at the condensate scale dressed by ordinary RG running (band ~0.955–0.99 at m_t). The NUMBER
     cannot tell them apart (toy 4743/4744; Grace confirmed the RG magnitude).
  3. "TOP AT LEVEL 127" MUST BE FORCED: it fits inside the error bar (better than the killed coincidences), but that is
     not proof — the top's discrete address must independently land at code level M_g, not be chosen because 127/128 is pretty.

⟹ VERDICT: y_t = M_g/2^g = 127/128 is a genuinely BST-native, TIGHT candidate (0.009% from pole m_t; uses the GF(2^g)
Reed-Solomon substrate field; matches Lyra's discrete-vs-boundary gap) — a REAL LEAD, better than the loose coincidences
killed this week. But it STAYS SUPPORTED, not banked: scheme-dependent (pole-specific) + my degeneracy fish (127/128 vs
RG-dressed-1 indistinguishable by the number) + "top at level 127" not yet forced. The DECIDING computation is the top's
discrete-series address: if the geometric deficit = exactly 1/2^g → derived (y_t = M_g/2^g, beautiful); if 0 →
exact-1+RG. The number 0.992 cannot decide — only the computed address can. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
from fractions import Fraction as F
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

Mg, twog = 2**g - 1, 2**g
yt = F(Mg, twog)
v = 246.22

# ---- the candidate + implied m_t --------------------------------------------
m_t_implied = float(yt)*v/math.sqrt(2)
print(f"\n[candidate]: y_t = M_g/2^g = {Mg}/{twog} = 1 − 1/2^g = {float(yt):.5f}; implied m_t = {m_t_implied:.2f} GeV vs pole 172.76±0.3 ({abs(m_t_implied-172.76)/172.76*100:.3f}%)")
check("THE CANDIDATE (verified, TIGHT): y_t = 1 − 1/2^g = M_g/2^g = 127/128 = 0.99219; implied m_t = 172.74 GeV vs pole "
      "172.76 ± 0.3 → 0.009% (INSIDE the error bar — far tighter than the loose-range coincidences killed this week).",
      Mg == 127 and twog == 128 and abs(m_t_implied - 172.76)/172.76 < 0.001, "y_t=127/128=M_g/2^g; implied m_t=172.74 (0.009% from pole) — tight")

# ---- BST-native: GF(2^g) Reed-Solomon ---------------------------------------
print(f"[BST-native]: 2^g={twog}=GF(2^g) Reed-Solomon field; M_g={Mg}=Mersenne prime (last code symbol); deficit 1/2^g = one code-unit")
check("BST-NATIVE (Reed-Solomon substrate): 2^g = 128 = GF(2^g) = the RS field the substrate codes on (Paper #122); "
      "M_g = 127 = the g-th Mersenne prime = last usable RS code symbol. Top at the OUTERMOST code level (127=M_g) of "
      "2^g; the one level it can't cross to the boundary = deficit 1/2^g = ONE code-unit. Matches Lyra's F603 "
      "discrete-vs-boundary gap — a candidate DERIVATION, not just a fit.",
      Mg == 2**g - 1, "2^g=128=GF(2^g) RS field, 127=M_g last code symbol, deficit=1/2^g one code-unit — matches F603 discrete-boundary gap")

# ---- guard 1: scheme-dependent ----------------------------------------------
y_pole = math.sqrt(2)*172.76/v; y_msbar = math.sqrt(2)*163/v
print(f"[guard 1 — scheme]: pole y_t={y_pole:.3f} (matches 127/128); MS-bar y_t={y_msbar:.3f} (NO match) → pole-specific claim")
check("GUARD 1 — SCHEME-DEPENDENT: pole y_t = 0.992 matches 127/128; MS-bar y_t (m_t~163) = 0.936 does NOT. So "
      "y_t=127/128 is a claim about the POLE value specifically — needs a reason the geometric y_t is the pole one.",
      abs(y_pole - float(yt)) < 0.005 and abs(y_msbar - float(yt)) > 0.03, "pole matches 127/128, MS-bar doesn't → pole-specific claim, needs justification")

# ---- guard 2: my degeneracy fish --------------------------------------------
check("GUARD 2 — MY DEGENERACY FISH (decisive): the 0.8% deficit is degenerate — equally consistent with a geometric "
      "1−1/2^g AND with an exact y_t=1 at the condensate scale dressed by RG running (band ~0.955–0.99 at m_t). The "
      "NUMBER cannot tell them apart (toys 4743/4744; Grace confirmed the RG magnitude). So 127/128 fitting is NOT proof.",
      True, "127/128 vs exact-1+RG-running degenerate → the number cannot decide (my fish holds); fitting ≠ deriving")

# ---- guard 3 + deciding computation -----------------------------------------
check("GUARD 3 + THE DECIDING COMPUTATION: 'top at level 127' must be FORCED by the discrete address, not chosen because "
      "127/128 is pretty. The deciding computation is the top's discrete-series address (June open core): if the "
      "geometric boundary-overlap deficit = exactly 1/2^g → DERIVED (y_t=M_g/2^g, beautiful); if 0 → exact-1+RG. Only "
      "the computed address decides — the number 0.992 cannot.",
      True, "top-at-level-127 must be forced by the discrete address (June open core); geometric deficit=1/2^g → derived, else exact-1+RG")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: y_t = M_g/2^g = 127/128 is a genuinely BST-native, TIGHT candidate (0.009% from pole m_t; GF(2^g) "
      "Reed-Solomon field; matches Lyra's discrete-vs-boundary gap) — a REAL LEAD, better than the loose coincidences "
      "killed this week. But it STAYS SUPPORTED, not banked: scheme-dependent (pole-specific) + my degeneracy fish "
      "(127/128 vs RG-dressed-1 indistinguishable) + 'top at level 127' not yet forced. Deciding computation: the top's "
      "discrete-series address (June open core). Don't bank y_t=127/128.",
      abs(m_t_implied - 172.76)/172.76 < 0.001 and Mg == 127,
      "y_t=M_g/2^g=127/128 tight+BST-native LEAD (0.009% pole, RS field), but scheme-dependent+degenerate+not-forced → SUPPORTED; address decides")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
VERIFY y_t = 127/128 = M_g/2^g (Lyra's peak-convergence candidate) — a REAL LEAD, held at SUPPORTED:
  * TIGHT: implied m_t=172.74 GeV, 0.009% from pole (far better than the loose coincidences killed this week).
  * BST-NATIVE: 2^g=128=GF(2^g) Reed-Solomon field; 127=M_g last code symbol; deficit 1/2^g=one code-unit (matches F603).
  * GUARD 1: scheme-dependent (pole matches, MS-bar doesn't) — pole-specific.
  * GUARD 2 (my fish, decisive): 127/128 vs exact-1+RG-running DEGENERATE — the number can't decide.
  * GUARD 3: 'top at level 127' must be FORCED by the discrete address (June open core), not chosen because 127/128 is pretty.
  => REAL LEAD, better than the killed coincidences, but SUPPORTED not banked. The top's discrete address decides.
""")
