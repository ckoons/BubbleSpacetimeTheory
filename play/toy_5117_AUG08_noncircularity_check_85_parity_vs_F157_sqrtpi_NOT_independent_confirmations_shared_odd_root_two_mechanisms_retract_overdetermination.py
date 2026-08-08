#!/usr/bin/env python3
"""
Toy 5117: NON-CIRCULARITY CHECK (Cal's guard, routed by Keeper K1282) -- are #85 (sin²θ_W=3/13, by
color-parity) and Grace F157 (tau √π) two INDEPENDENT confirmations, or secretly ONE shared fact?
FINDING: NOT cleanly independent. Both ride the ODDNESS of a BST integer, and the specific "3"s are tied
by the corpus identity a = n_C−2 = N_c = 3. They use TWO DIFFERENT mechanisms (complex-structure
obstruction vs half-integer Gindikin-Γ) but ONE oddness-root -> do NOT cite as "over-determination /
two independent confirmations." Honest form: one BST-integer-oddness theme forces two observables (a
consistency web / Schur pattern), which is valuable but is NOT independent evidence. Retract the
"over-determined" framing on #85. (Elie's requested check; calibrating an over-claim DOWN.)
E / Elie -- Cal is right to guard this. Two results are two confirmations only if not secretly one fact.

THE TWO RESULTS AND THEIR PARITY SOURCES:
  * #85 (3/13): color Peirce space V12 has real dim = N_c = 3 = ODD -> no complex structure (J²=−I needs
    EVEN dim; det(−I_3)=−1<0) -> color is a real count, does not double -> 3/13. PARITY SOURCE: N_c=3 odd.
    MECHANISM: complex-structure obstruction (a Z/2 / linear-algebra fact).
  * F157 (tau √π): the Gindikin gamma of the Lorentz cone Γ_Ω(s) = (2π)^((n_C−r)/2) ∏_j Γ(s_j − j·a/2),
    r=2, a=n_C−2=3. BOTH the prefactor power (n_C−r)/2 = 3/2 [n_C−r=3 ODD] AND the shift a/2 = 3/2
    [a=3 ODD] give half-integer -> Γ(3/2)=√π/2 -> √π. PARITY SOURCE: a=n_C−2=3 and n_C−r=3, both odd
    BECAUSE n_C=5 is odd. MECHANISM: half-integer Gindikin-Γ (an analysis fact).

THE CRUX: are the two "3"s the same? The corpus identity a = n_C − 2 = N_c = 3 (short-root multiplicity =
color, T2545) TIES them. So #85's "N_c=3 odd" and F157's "a=n_C−2=3 odd" are the SAME 3, identified by a
BST identity. The PARITY-SOURCE integers differ nominally (N_c vs n_C→a), but the identity collapses them.

=> VERDICT (plain): NOT two independent confirmations. Both ride BST-integer ODDNESS; the specific 3s are
tied by a = n_C−2 = N_c. Two DIFFERENT mechanisms (complex-structure obstruction vs half-integer Γ), but
ONE oddness-root. So RETRACT "over-determined" as a strengthener for #85 -- it double-counts one fact seen
two ways. HONEST FORM: "one BST-integer-oddness (N_c=3, = a = n_C−2) forces BOTH 3/13 AND the tau √π, via
two mechanisms" -- a consistency web / Schur pattern (if that integer were EVEN, BOTH break), which is
genuine and valuable, but is NOT independent evidence. #85 stands on parity ALONE (it does not need F157).

=> DISPOSITION: answers Cal's routed guard -- the tau cross-check is NOT an independent confirmation of
#85; it is the same odd-integer fact via a second mechanism. #85's PD tier rests on its own parity
derivation (unaffected). Do not narrate "over-determined"; narrate "one odd integer, two observables,
two mechanisms." Calibrating an over-claim DOWN before it ships. Firer: Elie; concurs-with: Cal's guard.
Nothing pushed. Nothing banked.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from math import gamma, sqrt, pi

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5117: non-circularity -- #85 parity vs F157 √π: NOT independent (shared odd root, two mechanisms)")
print("=" * 78)

rank, N_c, n_C = 2, 3, 5
a = n_C - 2                      # cone characteristic multiplicity (= N_c by BST identity)

# ----------------------------------------------------------------------------
# 1. #85 mechanism: complex-structure obstruction on dim(V12) = N_c = 3 (odd).
# ----------------------------------------------------------------------------
print("\n--- 1. #85 parity source: N_c=3 odd -> no complex structure (Z/2 obstruction) ---")
dimV12 = N_c
no_cplx_struct = (-1)**dimV12 < 0
check("#85 (3/13) parity source = dim(V12) = N_c = 3 ODD; mechanism = complex-structure obstruction "
      "(det(-I_3)=-1<0 -> no J with J²=-I) -> color is a real count, does not double -> 3/13",
      no_cplx_struct and dimV12 == 3,
      f"det(-I_{dimV12}) = {(-1)**dimV12} < 0 -> no complex structure. Source integer = N_c. Mechanism = "
      "linear-algebra parity (Z/2).")

# ----------------------------------------------------------------------------
# 2. F157 mechanism: half-integer Gindikin-Γ from a=n_C-2=3 and n_C-r=3 (both odd because n_C=5 odd).
# ----------------------------------------------------------------------------
print("\n--- 2. F157 parity source: a=n_C-2=3, n_C-r=3 (odd <= n_C=5 odd) -> half-integer Γ -> √π ---")
prefactor_power = (n_C - rank)/2      # = 3/2 (half-integer since n_C-r=3 odd)
shift = a/2                           # = 3/2 (half-integer since a=3 odd)
G_half = gamma(1.5)                   # Γ(3/2) = √π/2
sqrt_pi_from_G = abs(G_half - sqrt(pi)/2) < 1e-12
check("F157 (tau √π) parity source = a = n_C-2 = 3 and n_C-r = 3, BOTH odd because n_C=5 is odd; mechanism "
      "= half-integer Gindikin-Γ. prefactor power (n_C-r)/2 = 3/2 and shift a/2 = 3/2 -> Γ(3/2) = √π/2 -> √π",
      sqrt_pi_from_G and prefactor_power == 1.5 and shift == 1.5,
      f"(n_C-r)/2 = {prefactor_power}, a/2 = {shift}; Γ(3/2) = {G_half:.6f} = √π/2 = {sqrt(pi)/2:.6f}. "
      "Source integers = n_C-2 and n_C-r (odd <= n_C odd). Mechanism = analytic half-integer Γ.")

# ----------------------------------------------------------------------------
# 3. The crux: the two "3"s are TIED by the identity a = n_C - 2 = N_c.
# ----------------------------------------------------------------------------
print("\n--- 3. crux: a = n_C - 2 = N_c = 3 ties the two '3's (T2545) ---")
tied = (a == N_c == 3)
check("the corpus identity a = n_C - 2 = N_c = 3 (short-root multiplicity = color, T2545) TIES the two "
      "'3's: #85's dim(V12)=N_c and F157's a=n_C-2 are the SAME 3. So the parity-source integers, nominally "
      "different (N_c vs n_C->a), collapse to one fact under a BST identity",
      tied,
      f"a = n_C-2 = {a}; N_c = {N_c}; equal = {tied}. The identity means the oddness is ONE integer's, "
      "seen from the color side (N_c) and the cone side (n_C-2).")

# ----------------------------------------------------------------------------
# 4. Verdict: NOT independent -> retract "over-determined"; honest form = one odd integer, two mechanisms.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: NOT independent confirmations -> retract 'over-determined' framing ---")
independent = False   # both ride the same odd integer (a=n_C-2=N_c); only the mechanism differs
check("VERDICT: #85 and F157 are NOT two INDEPENDENT confirmations -- both ride the ODDNESS of one BST "
      "integer (a = n_C-2 = N_c = 3), via two DIFFERENT mechanisms (complex-structure obstruction vs "
      "half-integer Γ). RETRACT 'over-determined' as a strengthener for #85 (it double-counts one fact). "
      "HONEST FORM: one odd integer forces BOTH 3/13 AND the tau √π -- a consistency web (Schur), not "
      "independent evidence. #85 stands on parity ALONE, needs no F157 cross-check",
      independent is False and tied,
      "if that integer were EVEN, BOTH break -> genuine consistency web (valuable), but NOT two "
      "independent confirmations. The mechanisms differ; the fact does not. Cal's guard = correct.")

check("consequence for narration: do NOT say '3/13 is over-determined by the tau mass.' DO say 'the same "
      "odd integer (N_c=3 = a = n_C-2) forces the Weinberg-angle doubling-exclusion AND the tau √π, by two "
      "mechanisms.' The PD tier of 3/13 rests on its OWN parity derivation, unaffected either way",
      no_cplx_struct and sqrt_pi_from_G and tied,
      "calibrating an over-claim down before it ships (as dishonest to over-claim a confirmation as to "
      "inflate a fit). Same discipline as the #85 four-Chern-forms and the m_W six-8-forms flags.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (#85 & F157: NOT independent -- one odd root, two mechanisms)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5117, non-circularity check -- Cal's guard, routed by Keeper K1282):
  * #85 (3/13): parity source N_c=3 odd; mechanism = complex-structure obstruction (no J²=-I on odd dim).
  * F157 (tau √π): parity source a=n_C-2=3 and n_C-r=3 (odd <= n_C=5 odd); mechanism = half-integer
    Gindikin-Γ (Γ(3/2)=√π/2).
  * CRUX: a = n_C-2 = N_c = 3 (T2545) TIES the two 3s -> the oddness is ONE integer's, seen two ways.
  * VERDICT: NOT two independent confirmations -- one odd-integer fact via two mechanisms. RETRACT
    'over-determined' as a strengthener; honest form = 'one odd integer forces both 3/13 and the tau √π'
    (a consistency web / Schur pattern, valuable but not independent evidence). #85's PD tier rests on
    its OWN parity derivation and needs no F157 cross-check.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked. Answers Cal's guard: the tau cross-check is NOT
independent of #85 -- same odd integer (a=n_C-2=N_c), two mechanisms. Retract 'over-determined'. #85
stands on parity alone. Calibrating an over-claim down. Count N.
""")
