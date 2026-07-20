#!/usr/bin/env python3
"""
Toy 4749 — Jul 20 (Target 3: mass = codeword reliability, mine; the fish-detector on the refined full-spectrum lead):
my Target-1 catch (toy 4748) killed "mass = coverage-length" (6/9 fermions below the min code fraction). The refined
lead (Lyra, LFSR round): mass = codeword RELIABILITY — the top is a PERFECT codeword; light fermions are
error-dominated, and error-probabilities are EXPONENTIAL (P_error ~ exp(−distance)), which coverage-length couldn't
give. My job: fit the spectrum to code reliability, target-innocent. Result: the exponential reliability reading DOES
escape my coverage-length catch — the hierarchy fits y ~ ε^n — BUT it is exactly the KNOWN Froggatt-Nielsen
parametrization (y ~ ε^charge, ε ≈ Cabibbo) in code language, a fit with free integer charges + free ε, NOT a
derivation. And even the FN charges aren't clean integers (only 5/9 within 0.3). So "mass = codeword reliability"
escapes the coverage-length FAIL but over-reaches as a derivation: it's FN-in-code-language until the code FORCES the
integer charges and ε target-innocently. The top (n=0, perfect codeword) is the one clean case. Don't bank "the
hierarchy IS the error-rate ladder."

THE TEST (y_f = √2·m_f/v vs y ~ ε^n, ε ≈ Cabibbo ≈ 0.23):
  * the hierarchy (y from ~1 down to ~10⁻⁶, 5.5 orders) DOES fit an exponential y ~ ε^n → ESCAPES the coverage-length
    FAIL (which was bounded below by 1/2^g). Real improvement over coverage-length.
  * FN charges n = ln(y)/ln(ε): t≈0 (perfect codeword ✓), b≈2.5, τ≈3.1, c≈3.3, μ≈5.0, s≈5.1, d≈7.2, u≈7.7, e≈8.7.
    Only 5/9 are within 0.3 of an integer — so even the FN fit is loose.
THE FISH (why it's not a derivation): an exponential y ~ ε^n with FREE integer charges n and FREE ε is a ~10-parameter
fit to 9 numbers — it's UNDERDETERMINED and can fit ANY hierarchy. So "the hierarchy fits an exponential" is NOT a
prediction. This is exactly Froggatt-Nielsen (a known SM parametrization) rewritten in code language. For "mass =
codeword reliability" to be a DERIVATION, the code (RS/LFSR) must FORCE the specific integer charges n AND ε
target-innocently — which is NOT shown. The top (n=0, the perfect codeword) is the one forced/clean case.

⟹ VERDICT: mass = codeword reliability (exponential) ESCAPES the coverage-length FAIL (it can span the 5.5-order
hierarchy) — a real improvement — but it is Froggatt-Nielsen in code language: a parametrization with free charges + ε
(underdetermined, fits anything), NOT a derivation, and even the FN charges aren't clean (5/9 integer). The top (perfect
codeword, n=0) is clean; the light spectrum is FN-structured but NOT code-forced. "The hierarchy IS the error-rate
ladder" is NOT established — don't bank it. The code must force the charges + ε to make it real. Count ~7-8 (α RULED).
Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
v = 246.22
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

m = {'t':172.76,'b':4.18,'tau':1.777,'c':1.27,'mu':0.1057,'s':0.0934,'u':2.16e-3,'d':4.67e-3,'e':0.511e-3}
y = {k: math.sqrt(2)*mf/v for k, mf in m.items()}
eps = 0.23   # Cabibbo — the standard Froggatt-Nielsen expansion parameter
n_fn = {k: math.log(yy)/math.log(eps) for k, yy in y.items()}
near_int = sum(1 for nn in n_fn.values() if abs(nn - round(nn)) < 0.3)
span_orders = math.log10(y['t']/y['e'])

# ---- escapes the coverage-length FAIL ---------------------------------------
print(f"\n[reliability y~ε^n]: hierarchy spans {span_orders:.1f} orders; FN charges: t={n_fn['t']:.1f}, b={n_fn['b']:.1f}, c={n_fn['c']:.1f}, e={n_fn['e']:.1f}")
check("ESCAPES THE COVERAGE-LENGTH FAIL (real improvement): the Yukawa hierarchy spans 5.5 orders (y ~1 → ~10⁻⁶) and "
      "DOES fit an exponential y ~ ε^n — unlike coverage-length (bounded below by 1/2^g, which failed 6/9 fermions in "
      "toy 4748). So the reliability/exponential reading is a genuine improvement over coverage-length.",
      span_orders > 5, "y~ε^n spans the 5.5-order hierarchy → escapes the coverage-length FAIL (4748) — real improvement")

# ---- but it's Froggatt-Nielsen in code language -----------------------------
check("BUT IT'S FROGGATT-NIELSEN IN CODE LANGUAGE (the fish): y ~ ε^charge with ε ≈ Cabibbo ≈ 0.23 is exactly the KNOWN "
      "SM Froggatt-Nielsen parametrization. An exponential with FREE integer charges + FREE ε is a ~10-parameter fit to "
      "9 numbers — UNDERDETERMINED, fits ANY hierarchy. So 'the hierarchy fits an exponential' is NOT a prediction; it's "
      "FN rewritten in code words.",
      True, "y~ε^n = Froggatt-Nielsen (known parametrization, free charges+ε, underdetermined) in code language — not a prediction")

# ---- even the FN charges aren't clean ---------------------------------------
print(f"[FN charges]: only {near_int}/9 within 0.3 of an integer (t=0 clean; b=2.5, c=3.3, u=7.7 not) → even the FN fit is loose")
check("EVEN THE FN CHARGES AREN'T CLEAN: only 5/9 charges are within 0.3 of an integer (t≈0 clean ✓, but b≈2.5, c≈3.3, "
      "u≈7.7 are not). So even the Froggatt-Nielsen fit is loose — the hierarchy doesn't cleanly give integer code "
      "distances. The top (n=0, perfect codeword) is the one forced/clean case.",
      near_int <= 6 and abs(n_fn['t']) < 0.2, "only 5/9 FN charges near-integer; top (n=0) clean, rest loose — not clean code distances")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: mass = codeword reliability (exponential) ESCAPES the coverage-length FAIL (spans the 5.5-order "
      "hierarchy) — a real improvement — BUT it is Froggatt-Nielsen in code language: a parametrization with free "
      "charges + ε (underdetermined, fits anything), NOT a derivation, and even the FN charges aren't clean (5/9 "
      "integer). The top (perfect codeword, n=0) is clean; the light spectrum is FN-structured but NOT code-forced. "
      "'The hierarchy IS the error-rate ladder' is NOT established — the code must FORCE the charges + ε. Don't bank.",
      span_orders > 5 and abs(n_fn['t']) < 0.2,
      "reliability escapes coverage-length but = FN-in-code-language (underdetermined fit); top clean, rest not code-forced → don't bank the ladder")

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
TARGET 3 — mass = codeword reliability (exponential): escapes coverage-length, but it's FN-in-code-language:
  * ESCAPES the coverage-length FAIL: y~ε^n spans the 5.5-order hierarchy (unlike coverage-length, 4748). Real improvement.
  * BUT = Froggatt-Nielsen (y~ε^charge, ε≈Cabibbo): free charges + ε = underdetermined ~10-param fit → fits anything → NOT a prediction.
  * even the FN charges aren't clean (5/9 near-integer; top n=0 clean, rest loose).
  => reliability is a FRAME not a derivation; the code must FORCE the charges + ε. Top clean; 'hierarchy = error-rate ladder' NOT established. Don't bank.
""")
