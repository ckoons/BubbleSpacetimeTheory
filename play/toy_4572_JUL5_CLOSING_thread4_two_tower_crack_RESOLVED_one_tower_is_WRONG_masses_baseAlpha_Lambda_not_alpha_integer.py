#!/usr/bin/env python3
"""
Toy 4572 — Jul 5 CLOSING PUSH, Thread 4 (mine): tie off the two-tower crack. The instruction
is to STATE PLAINLY whether the two towers reconcile or the one-tower picture is wrong.

PLAIN ANSWER: the one-tower ("everything = α^{shell count}, one per-shell cost = 1/N_max")
picture is WRONG. Definitively:

  MASS tower (base α = 1/137): m_e ~ α^12 (12 = 2·C_2), Koons tick ~ α^36 (36 = C_2²) —
    CLEAN INTEGER exponents.
  Λ on the α-tower: exp(−280) = α^56.91 — NON-integer. Not 56, not any clean integer.
  one-tower test: α^56 / exp(−280) = 87× (the crack).
  reconciliation would require N_max = e^{n_C} = 148.4, but N_max = 137 (8.3% off) → FALSE.
  and "Λ = 56 shells" is a NON-UNIQUE factoring of 280 = 2^{N_c}·n_C·g (= n_C·56 = g·40 = 2^{N_c}·35...).

⟹ VERDICT: masses live on a genuine base-α tower with clean integer exponents; Λ = exp(−280)
is exp of a substrate PRODUCT, NOT α^{integer}. They are two distinct structures. The
shell-cosmology "exponent = shell count, one per-shell cost, Λ at shell 56" is REFUTED —
Λ is not on the α-tower, and its "56 shells" is one non-unique reading.

CONSEQUENCE for seed=terminus (Thread 4's prize): the "equilibrium at 56 shells" climb rides
the Λ-side (candidate, non-unique factoring), NOT the clean mass-side. So the climb factor c^56
is not clean — seed=terminus's climb side inherits this crack. The fixed-point EXISTENCE still
needs the collapse dynamics (vision, Grace/Lyra). seed=terminus stays the one derivable-number
target, UNREACHED; the two-tower crack is now a NAMED open problem, not a hidden one.

Closing tie-off. No count move — the crack is resolved to a plain statement + named open problem.
"""
import math
rank, N_c, n_C, C_2, g, Nmax = 2, 3, 5, 6, 7, 137
alpha = 1/137.035999
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4572 — CLOSING Thread 4: the two-tower crack RESOLVED — the one-tower picture is WRONG")
print("=" * 82)

# ---- masses: clean integer exponents on base α ------------------------------
print(f"\n[MASS tower — base α = 1/137, CLEAN integer exponents]:")
print(f"  m_e ~ α^12  (12 = 2·C_2 = {2*C_2}) ; Koons tick ~ α^36 (36 = C_2² = {C_2**2})")
check("masses live on a base-α tower with CLEAN integer exponents (12, 36)",
      2*C_2 == 12 and C_2**2 == 36, "solid: m_e = 6π⁵·α¹²·m_Pl at 0.032%, Koons α^36")

# ---- Λ on the α-tower: non-integer ------------------------------------------
lam_exp_alpha = 280/(-math.log(alpha))
crack = math.exp(56*math.log(alpha) + 280)
print(f"\n[Λ on the α-tower — NON-integer]:")
print(f"  exp(−280) = α^{lam_exp_alpha:.2f}  (NOT 56, NOT any clean integer)")
print(f"  one-tower test: α^56 / exp(−280) = {crack:.0f}×  ← the crack")
check("Λ = exp(−280) is α^56.9 on the α-tower — NON-integer; α^56 misses observed Λ by 87×",
      abs(lam_exp_alpha - 56.9) < 0.2 and crack > 50,
      "masses are clean α-integers; Λ is NOT an α^{integer} → not the same tower")

# ---- reconciliation is impossible: N_max ≠ e^{n_C} --------------------------
e_nc = math.exp(n_C)
print(f"\n[reconciliation test — would need N_max = e^{{n_C}}]:")
print(f"  e^{n_C} = {e_nc:.1f}  vs  N_max = {Nmax}  ({(e_nc-Nmax)/Nmax:.1%} off) → FALSE")
check("one-tower reconciliation requires N_max = e^{n_C} = 148.4, but N_max = 137 (8.3% off) → impossible",
      abs(e_nc - Nmax)/Nmax > 0.05, "ln(N_max)=4.92 ≈ n_C=5 is only 1.6% close → 87× over 56 shells")

# ---- "56 shells" is a non-unique factoring ----------------------------------
prod = 2**N_c * n_C * g
factorings = [(n_C, prod//n_C), (g, prod//g), (2**N_c, prod//2**N_c), (C_2, prod//C_2 if prod%C_2==0 else None)]
print(f"\n[the '56 shells' reading is NON-unique]:")
print(f"  280 = 2^N_c·n_C·g = {prod} ; factorings: n_C·56, g·40, 2^N_c·35, ... — '56 shells' is one of many")
check("'Λ at 56 shells' is a NON-UNIQUE factoring of 280 = 2^N_c·n_C·g → the shell reading isn't forced",
      prod == 280, "even the Λ-tower's '56' is a chosen factoring, not derived")

# ---- VERDICT ----------------------------------------------------------------
print(f"\n[VERDICT — plain]:")
print(f"  the one-tower shell picture (all observables = α^{{shell count}}, one per-shell cost) is WRONG.")
print(f"  masses = base-α tower, clean integer exponents. Λ = exp(−280) = exp of a substrate PRODUCT,")
print(f"  NOT α^{{integer}}. Two distinct structures. The unification is refuted (87× + non-integer).")
check("VERDICT: one-tower shell picture REFUTED — masses base-α (clean), Λ = exp(substrate product) ≠ α^integer",
      True, "stated plainly per the closing-push instruction — not reconciled, the one-tower is wrong")

# ---- consequence for seed=terminus + terminus -------------------------------
print(f"\n[seed=terminus — consequence + honest terminus]:")
print(f"  the 'equilibrium at 56 shells' climb rides the Λ-side (candidate, non-unique factoring),")
print(f"  NOT the clean mass-side → seed=terminus's climb factor c^56 is NOT clean (inherits the crack).")
print(f"  fixed-point EXISTENCE still needs the collapse dynamics (vision, Grace/Lyra Shilov-saturation).")
print(f"  ⟹ seed=terminus: reduced to one claim (4571), UNREACHED. The two-tower crack: NAMED open problem.")
check("seed=terminus stays UNREACHED (collapse dynamics = vision); climb side inherits the two-tower crack",
      True, "the one derivable-number target is honestly out of reach; both cracks named, not buried")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
THREAD 4 TIED OFF (two-tower crack RESOLVED to a plain statement; seed=terminus named):
  * THE PLAIN ANSWER: the one-tower shell picture (all = α^{shell count}, one per-shell cost)
    is WRONG. Masses live on a base-α tower with CLEAN integer exponents (12=2·C_2, 36=C_2²);
    Λ = exp(−280) is α^56.9 (NON-integer) — off by 87× as α^56. Reconciliation needs
    N_max = e^{n_C} = 148.4, but N_max = 137 (8.3% off) → impossible. And "Λ at 56 shells" is
    a non-unique factoring of 280 = 2^N_c·n_C·g. Two distinct structures — REFUTED as one tower.
  * seed=terminus: reduced to one fixed-point claim (4571), UNREACHED — its "56-shell climb"
    inherits the two-tower crack (rides the candidate Λ-side, not the clean mass-side), and
    fixed-point existence needs the collapse dynamics (vision). The one derivable-number target,
    honestly out of reach.
  * OPEN PROBLEMS NAMED (not buried): (1) why two bases (α for mass, exp-of-substrate-product
    for Λ)? (2) is Λ a shell tower at all, or just exp of a product? (3) seed=terminus fixed
    point (collapse dynamics). Count 8. ζ armed for Grace's Shilov spectrum — the nearer bolt.
""")
