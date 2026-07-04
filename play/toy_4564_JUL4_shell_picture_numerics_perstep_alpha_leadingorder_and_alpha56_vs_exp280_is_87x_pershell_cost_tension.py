#!/usr/bin/env python3
"""
Toy 4564 — Jul 4: numerical audit of Casey's shell-cosmology OPERATIONAL core (my lane).
The vision (dimensional cycling) is Level-2 internal; the operational core is checkable:
  (a) shell capacity N_max=137 → per-step α = 1/N_max (mechanism for F423)
  (b) α-tower exponents = shell counts: m_e α¹²(12), Koons α³⁶(36), Λ α⁵⁶(56)
  (c) ln(N_max) ≈ n_C reconciles α⁵⁶ with exp(−280)

HONEST AUDIT:
  (a) per-step α = 1/137 = 0.026% off α — LEADING ORDER, real mechanism-lead (F423), NOT
      exact (Casey's bar: bank only if exact). Not a bank.
  (b) exponents 12<36<56 are a CONSISTENT increasing ordering (reinterpretation of known
      α-tower exponents as shell counts) — physical reading, not a new derivation.
  (c) THE TENSION (load-bearing catch): α⁵⁶ = 10^−119.7 but exp(−280) = 10^−121.6 — they are
      87× APART. Observed Λ ~ 10^−121.6 matches exp(−280), NOT α⁵⁶. The 1.6% ln-gap
      (ln137=4.92 vs n_C=5) compounds over 56 shells to 87×. Equivalently: the per-shell
      cost is 1/137 (capacity) OR exp(−n_C)=1/148 (Λ) — 8% apart, and they can't both hold.
      So the shell picture cannot give per-step-α (1/137) AND Λ=exp(−280) with ONE per-shell cost.

Target-innocent. No count move — an honest audit of the mechanism-lead + a precise tension flag.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
alpha = 1/137.035999
Nmax = 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4564 — shell-picture numerics: per-step α (leading order) + α⁵⁶-vs-exp(−280) tension")
print("=" * 82)

# ---- (a) per-step α = 1/N_max — leading order --------------------------------
perstep = 1/Nmax
dev = abs(perstep - alpha)/alpha
print(f"\n[(a) per-step α = 1/N_max]")
print(f"  1/137 = {perstep:.7f} vs α = {alpha:.7f} → {dev:.4%} (leading order)")
check("per-step α = 1/N_max is a real MECHANISM-LEAD (F423) but LEADING-ORDER only (0.026% off)",
      dev < 0.001 and dev > 1e-4, "gives 1/137, NOT exact 137.036 → not a bank (Casey's 'bank only if exact')")

# ---- (b) exponent = shell count: consistent ordering ------------------------
tower = {"m_e/m_Pl": (12, 2*C_2), "Koons tick": (36, C_2**2), "Λ": (56, 2**N_c*g)}
print(f"\n[(b) α-tower exponents as shell counts]")
for name, (exp, form) in tower.items():
    print(f"  {name:12s}: α^{exp}  ({exp} = {['2·C_2','C_2²','2^N_c·g'][[12,36,56].index(exp)]})")
counts = [v[0] for v in tower.values()]
check("exponents 12<36<56 are a CONSISTENT increasing ordering (shell-count reinterpretation)",
      counts == sorted(counts), "physical reading of known α-tower exponents — reinterpretation, not new derivation")

# ---- (c) THE TENSION: α⁵⁶ vs exp(−280) is 87× -------------------------------
ln137 = math.log(Nmax)
a56_exp10 = 56*math.log(alpha)/math.log(10)
exp280_exp10 = -280/math.log(10)
ratio = math.exp(56*math.log(alpha) + 280)
print(f"\n[(c) THE TENSION — α⁵⁶ vs exp(−280)]")
print(f"  ln(137) = {ln137:.3f} vs n_C = {n_C}  (gap {(n_C-ln137)/n_C:.1%})")
print(f"  α⁵⁶ = 10^{a56_exp10:.2f}  ;  exp(−280) = 10^{exp280_exp10:.2f}  →  {ratio:.0f}× APART")
print(f"  observed Λ ~ 10^−121.6 matches exp(−280), NOT α⁵⁶ (10^−119.7).")
check("α⁵⁶ and exp(−280) are 87× APART — the ln137≈n_C reconciliation is LOOSE, not exact",
      ratio > 50, "the 1.6% per-shell ln-gap compounds over 56 shells to 87×")
check("observed Λ matches exp(−280), NOT the shell-count α⁵⁶ reading (which is 87× too big)",
      abs(exp280_exp10 - (-121.6)) < 0.2 and abs(a56_exp10 - (-121.6)) > 1,
      "the shell-count-via-α reading MISSES observed Λ; only exp(−280) hits it")

# ---- the per-shell-cost tension, made explicit ------------------------------
cost_capacity = 1/Nmax          # 1/137
cost_lambda = math.exp(-n_C)    # exp(-5) = 1/148.4
print(f"\n[per-shell-cost tension, explicit]:")
print(f"  capacity story → per-shell cost = 1/N_max = 1/137 = {cost_capacity:.5f}")
print(f"  Λ=exp(−280)=exp(−n_C·56) → per-shell cost = exp(−n_C) = 1/{1/cost_lambda:.1f} = {cost_lambda:.5f}")
print(f"  1/137 vs 1/148 → {abs(cost_capacity-cost_lambda)/cost_lambda:.1%} apart. CANNOT both hold.")
check("per-shell cost is 1/137 (capacity) OR exp(−n_C)=1/148 (Λ) — 8% apart, mutually inconsistent",
      abs(cost_capacity-cost_lambda)/cost_lambda > 0.05,
      "the shell picture can't give per-step-α (1/137) AND Λ=exp(−280) with one per-shell cost")

# ---- verdict ----------------------------------------------------------------
print(f"\n[VERDICT]:")
print(f"  (a) per-step α = 1/N_max: REAL mechanism-lead for F423, leading-order (0.026% off), not a bank.")
print(f"  (b) exponent = shell count: consistent ordering, a physical REINTERPRETATION of known exponents.")
print(f"  (c) Λ = α⁵⁶ reconciliation FAILS numerically: 87× off exp(−280); observed Λ picks exp(−280).")
print(f"      The per-shell cost is inconsistent (1/137 vs 1/148). This is the '1.6% gap' quantified —")
print(f"      it's 87× in Λ, a real tension, and it's exactly where the exact-α/Λ residual work lives.")
check("VERDICT: mechanism-lead real (F423), shell-count consistent, Λ=α⁵⁶ reconciliation 87× loose — count 8",
      True, "honest audit: the operational core has a real lead + a precise located tension; no bank")

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
SHELL-PICTURE NUMERICS (honest audit of the operational core):
  * (a) per-step α = 1/N_max = 1/137 is a REAL mechanism-lead for gate F423 — but LEADING
    ORDER (0.026% off α), gives 1/137 not exact 137.036. Per Casey's "bank only if exact":
    strong lead, not a bank.
  * (b) exponents 12<36<56 = a CONSISTENT increasing shell-count ordering — a physical
    reinterpretation of the known α-tower exponents, not a new derivation.
  * (c) THE TENSION (load-bearing): α⁵⁶ = 10^−119.7 but exp(−280) = 10^−121.6 — 87× APART.
    Observed Λ matches exp(−280), NOT the shell-count α⁵⁶ reading. The per-shell cost is
    1/137 (capacity) vs exp(−n_C)=1/148 (Λ) — 8% apart, mutually inconsistent. The shell
    picture cannot give per-step-α AND Λ=exp(−280) with one per-shell cost. This quantifies
    Casey's flagged "1.6% gap" as 87× in Λ — and locates exactly where the residual lives.
  => The operational core has a real F423 mechanism-lead + a precise, located tension. The
  exact-α (shell-closing boundary) and the per-shell-cost consistency are the open gates.
  Count 8, no move — mechanism-lead honest, reconciliation loose, nothing banked.
""")
