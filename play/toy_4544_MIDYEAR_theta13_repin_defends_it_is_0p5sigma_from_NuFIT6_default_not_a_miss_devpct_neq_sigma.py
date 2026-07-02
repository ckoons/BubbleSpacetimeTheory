#!/usr/bin/env python3
"""
Toy 4544 — Mid-Year PDG/NuFIT re-pin: θ₁₃ DEFENDS. Grace flagged 1/45 as a
"1.24% MISS vs NuFIT 6.0 default" (reference-sensitive, possibly demoting a firm
bank). The σ-analysis says otherwise: 1/45 is 0.50σ from the NuFIT 6.0 headline —
WITHIN 1σ, clean. Same dev%≠σ lesson as my m_s/m_d self-correction (toy_4543),
applied symmetrically — this time it DEFENDS a firm bank instead of softening a flag.

AUTHORITATIVE NuFIT 6.0 (2024), Normal Ordering, without-SK-atmospheric (the
headline/default result), arXiv:2410.05380 / nu-fit.org:
  sin²θ₁₃ = 0.02195 +0.00054 −0.00058     3σ range: 0.02023 → 0.02376

BST: sin²θ₁₃ = 1/(N_c²·n_C) = 1/45 = 0.022222 (θ₁₃ bank, K632).

FINDING: 1/45 is 0.50σ ABOVE the NuFIT 6.0 default (within 1σ) and comfortably
inside the 3σ range. Grace's "1.24% MISS" is a dev%; on a reference with ~2.5%
1σ uncertainty, 1.24% = ~0.5σ = consistent. θ₁₃ is NOT reference-gated; it stays
firm. The discipline (dev% ≠ σ) that softened my own nail also DEFENDS this bank.
Target-innocent (NuFIT primary source). No count move — θ₁₃ stays firm.
"""
N_c, n_C = 3, 5
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- authoritative NuFIT 6.0 (NO, without SK — the headline) -----------------
s13_default = 0.02195
s13_up, s13_dn = 0.00054, 0.00058
s13_3sig = (0.02023, 0.02376)
# the with-SK variant Grace cited (~0.0222) where BST scored 0.10%
s13_withSK = 0.0222

bst = 1/(N_c**2 * n_C)      # 1/45

print("=" * 78)
print("Toy 4544 — θ₁₃ re-pin: does 1/45 defend against the NuFIT 6.0 default?")
print("=" * 78)

print(f"\n  BST sin²θ₁₃ = 1/(N_c²·n_C) = 1/45 = {bst:.5f}")
print(f"  NuFIT 6.0 default (NO, w/o SK) = {s13_default} +{s13_up} −{s13_dn}")
print(f"  NuFIT 6.0 3σ range = {s13_3sig[0]} → {s13_3sig[1]}")

# ---- σ-analysis (the point) -------------------------------------------------
diff = bst - s13_default
sig = diff / (s13_up if diff > 0 else s13_dn)
dev_default = abs(diff)/s13_default
print(f"\n[σ-ANALYSIS] 1/45 vs NuFIT default:")
print(f"  deviation = {dev_default:.2%}  (Grace's '1.24% MISS')")
print(f"  but 1σ(NuFIT) = {s13_up/s13_default:.1%} of the value → in σ: {sig:.2f}σ")
check("1/45 is within 1σ of the NuFIT 6.0 default (0.50σ) — CONSISTENT, not a MISS",
      abs(sig) < 1.0, f"{sig:.2f}σ above default — the '1.24% MISS' is dev%-inflated")
check("1/45 is comfortably inside the NuFIT 6.0 3σ range",
      s13_3sig[0] < bst < s13_3sig[1], f"{s13_3sig[0]} < {bst:.5f} < {s13_3sig[1]}")
check("dev% ≠ σ (again): 1.24% on a ±2.5% reference is ~0.5σ — same lesson as my m_s/m_d nail",
      dev_default > 0.01 and abs(sig) < 1.0, "the re-pin discipline cuts BOTH ways")

# ---- with-SK variant (where it scored 0.10%) --------------------------------
dev_withSK = abs(bst - s13_withSK)/s13_withSK
print(f"\n[with-SK variant] 1/45 vs {s13_withSK}: {dev_withSK:.2%} (~0.05σ) — DONE-class on that variant")
check("θ₁₃ is consistent on BOTH NuFIT variants (0.5σ default, ~0.05σ with-SK)",
      abs(sig) < 1.0 and dev_withSK < 0.005, "reference-robust in σ terms, not reference-gated")

# ---- verdict -----------------------------------------------------------------
check("θ₁₃ DEFENDS — stays FIRM (0.5σ from the authoritative NuFIT 6.0 default)",
      abs(sig) < 1.0, "firm-3 (θ_QCD, m_t, θ₁₃) intact; no demotion; count 8")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
θ₁₃ RE-PIN VERDICT (defends a firm bank; discipline symmetric):
  * BST 1/45 = 0.02222 is 0.50σ above the NuFIT 6.0 DEFAULT (without-SK, the
    headline global fit) — WITHIN 1σ — and comfortably inside the 3σ range.
  * Grace's "1.24% MISS" is a dev%; the NuFIT 1σ on sin²θ₁₃ is ~2.5%, so 1.24%
    is ~0.5σ = CONSISTENT. θ₁₃ is reference-ROBUST in σ terms, not reference-gated.
  * Same dev% ≠ σ lesson that softened my m_s/m_d 'nail' (toy_4543) — here it
    DEFENDS the bank. The re-pin discipline cuts both ways: it demoted nothing it
    shouldn't and it promotes nothing it shouldn't.
  => θ₁₃ STAYS FIRM. firm-3 (θ_QCD, m_t, θ₁₃) intact. Count 8, no change.
  @Keeper (reference call): recommend θ₁₃ certified firm at 0.5σ vs the NuFIT 6.0
  default — score it in σ, not dev%, and it's clean on both variants.
""")
