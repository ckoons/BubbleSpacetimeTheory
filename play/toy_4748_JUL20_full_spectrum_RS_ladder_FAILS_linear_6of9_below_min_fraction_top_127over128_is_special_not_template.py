#!/usr/bin/env python3
"""
Toy 4748 — Jul 20 (Target 1: fit the full spectrum to RS code parameters, mine; the fish-detector on the round-2
frontier): the tempting story is "the top is one codeword (127/128) → the WHOLE fermion spectrum is the RS code's
structure (generations = code layers)." My job: fit the spectrum to code parameters, target-innocent. Result — the
simple LINEAR code-fraction reading (y_f = block-length/field = n/2^g) FAILS for the light spectrum: 6 of 9 fermions
have y < 1/2^g = 0.0078 (the MINIMUM non-trivial code fraction), so they CANNOT be codeword fractions n/2^g with n≥1.
The top's 127/128 is a SPECIAL maximal-codeword case, NOT a full-spectrum template. "From one number to all" via linear
code fractions over-reaches — the steep light hierarchy (down to y_e = 3×10⁻⁶) needs a different (multiplicative/nested)
structure, which is open (Lyra's code structure to propose; I test when she does). Don't over-claim the full-spectrum RS reading.

THE TEST (y_f = √2·m_f/v vs n/2^g, all 9 fermions):
  * top:    y = 0.992 → n = 127.0 ≈ M_g = 127 ✓ (the maximal codeword — the clean special case).
  * bottom: y = 0.024 → n = 3.1 (near N_c=3, marginal).
  * τ:      y = 0.010 → n = 1.3 (not clean).
  * c,μ,s,d,u,e: y < 1/2^g = 0.0078 → n < 1 → CANNOT be code fractions with n≥1. (6 of 9.)
  ⟹ the LINEAR code-fraction reading fits only the HEAVIEST (top=127, bottom≈3); it FAILS for the light spectrum
    (6 of 9 below the minimum fraction). So the full spectrum is NOT a simple linear RS code.

THE HONEST VERDICT (fish-detector on the prettiest frontier): the "whole spectrum = RS Ladder" via LINEAR code fractions
over-reaches — the top's 127/128 is a special maximal-codeword case, not a template for all 9. The light spectrum's
steep suppression (127 → 3 → down to ~10⁻⁶·2^g) can't be n/2^g with n≥1. Whether a MULTIPLICATIVE/nested RS structure
(code LAYERS) fits the hierarchy is OPEN — that's Lyra's code-structure to propose, and I test it target-innocently when
it lands. A quick multiplicative check is inconclusive too (y_c/y_t ≈ 1/2^g at ~5%, but y_u/y_c ≠ 1/2^g), so even the
multiplicative reading isn't clean yet. So: the top codeword result stands (special, LEAD); "generations = code layers"
is NOT yet supported — don't bank it.

⟹ VERDICT: the full-spectrum-as-RS-Ladder frontier OVER-REACHES at the linear level — y_f = n/2^g fits only the heaviest
(top=M_g=127, bottom≈N_c=3); 6 of 9 fermions are below the minimum code fraction 1/2^g, so the light spectrum is NOT
linear code fractions. The top's 127/128 stays a SPECIAL maximal-codeword LEAD, not a full-spectrum template. "From one
number to all" is NOT established; the light hierarchy needs a multiplicative/nested structure that isn't yet shown to
fit (Lyra's, I test target-innocently). Don't over-claim "generations = code layers." Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
twog = 2**g
v = 246.22
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

m = {'t':172.76,'b':4.18,'tau':1.777,'c':1.27,'mu':0.1057,'s':0.0934,'u':2.16e-3,'d':4.67e-3,'e':0.511e-3}
y = {k: math.sqrt(2)*mf/v for k, mf in m.items()}
min_frac = 1/twog
below = sum(1 for yy in y.values() if yy < min_frac)

# ---- the top fits (maximal codeword) ----------------------------------------
n_top = y['t']*twog
print(f"\n[top]: y_t = {y['t']:.4f} → n = {n_top:.1f} ≈ M_g = {twog-1} (maximal codeword); min code fraction 1/2^g = {min_frac:.5f}")
check("TOP FITS (the special case): y_t = 0.992 → n = 127.0 ≈ M_g = 127 — the maximal RS codeword (block length q−1). "
      "Bottom: y_b → n ≈ 3.1 (near N_c, marginal). These heaviest fit; the question is whether the rest do.",
      abs(n_top - (twog-1)) < 1, "y_t → n=127=M_g (maximal codeword) — the clean special case; bottom marginal near N_c")

# ---- the light spectrum FAILS -----------------------------------------------
print(f"[light spectrum]: {below}/9 fermions have y < 1/2^g = {min_frac:.5f} → n < 1 → CANNOT be code fractions n/2^g")
check("LIGHT SPECTRUM FAILS (the fish): 6 of 9 fermions (c,μ,s,d,u,e) have y < 1/2^g = 0.0078 — BELOW the minimum "
      "non-trivial code fraction — so they CANNOT be codeword fractions n/2^g with n≥1 (n<1). The linear code-fraction "
      "reading fits only the heaviest (top, bottom); the light spectrum (down to y_e=3×10⁻⁶) does NOT.",
      below == 6, "6/9 fermions below 1/2^g → can't be linear code fractions → the full spectrum is NOT a simple linear RS code")

# ---- multiplicative also inconclusive ---------------------------------------
r_ct = y['c']/y['t']; r_uc = y['u']/y['c']
print(f"[multiplicative check]: y_c/y_t = {r_ct:.4f} (≈1/2^g={min_frac:.4f}? {abs(r_ct-min_frac)/min_frac*100:.0f}%); y_u/y_c = {r_uc:.4f} (≠1/2^g) → inconclusive")
check("MULTIPLICATIVE ALSO INCONCLUSIVE: a nested/multiplicative RS reading (code LAYERS) isn't clean either — y_c/y_t ≈ "
      "1/2^g at ~5%, but y_u/y_c ≠ 1/2^g. So even the multiplicative hierarchy doesn't yet fit. 'Generations = code "
      "layers' is NOT yet supported — Lyra's code-structure must propose it and I test target-innocently.",
      abs(r_ct - min_frac)/min_frac < 0.10 and abs(r_uc - min_frac)/min_frac > 0.5,
      "y_c/y_t≈1/2^g (5%) but y_u/y_c≠1/2^g → multiplicative RS not clean; 'generations=code layers' not yet supported")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the full-spectrum-as-RS-Ladder frontier OVER-REACHES at the linear level — y_f = n/2^g fits only the "
      "heaviest (top=M_g=127, bottom≈N_c=3); 6 of 9 fermions are below the minimum code fraction 1/2^g, so the light "
      "spectrum is NOT linear code fractions. The top's 127/128 stays a SPECIAL maximal-codeword LEAD, NOT a "
      "full-spectrum template. 'From one number to all' is NOT established; the light hierarchy needs a "
      "multiplicative/nested structure not yet shown to fit. Don't over-claim 'generations = code layers.'",
      below == 6 and abs(n_top - (twog-1)) < 1,
      "full-spectrum RS over-reaches (6/9 below min fraction); top=127/128 special not template; 'generations=code layers' not supported — don't bank")

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
FULL SPECTRUM AS RS LADDER (Target 1) — the fish: it OVER-REACHES at the linear level:
  * TOP fits: y_t → n=127=M_g (maximal codeword); bottom → n≈3 (near N_c, marginal).
  * LIGHT SPECTRUM FAILS: 6/9 fermions below 1/2^g=0.0078 → can't be code fractions n/2^g with n≥1.
  * MULTIPLICATIVE inconclusive: y_c/y_t≈1/2^g (5%) but y_u/y_c≠1/2^g.
  => top=127/128 is SPECIAL (maximal codeword), NOT a full-spectrum template. 'Generations=code layers' NOT supported. Don't over-claim.
""")
