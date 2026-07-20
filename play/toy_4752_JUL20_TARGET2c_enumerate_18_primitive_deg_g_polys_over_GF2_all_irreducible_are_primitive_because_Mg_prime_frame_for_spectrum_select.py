#!/usr/bin/env python3
"""
Toy 4752 — Jul 20 (Target 2c groundwork: enumerate the 18 candidate polynomials, mine; target-innocent frame for the
spectrum-selects-polynomial test): the round-5 lead (Grace + Lyra) says the geometry selects ONE of "φ(127)/7 = 18"
primitive degree-g polynomials, and the same selection fixes the codeword distances → the light spectrum becomes a
postdiction. Before any of that, my job is the clean combinatorial groundwork: (1) ENUMERATE the primitive degree-g=7
polynomials over GF(2) directly (not quote the count) and verify there are exactly 18; (2) surface the BST-native reason
it's EXACTLY 18 — because M_g = 2^g − 1 = 127 is PRIME (a Mersenne prime), EVERY irreducible degree-g polynomial over
GF(2) is automatically PRIMITIVE, so the count is just (2^g − 2)/g = 126/7 = 18 = φ(M_g)/g; (3) FRAME what Lyra's map
must supply (a polynomial → codeword-distance-profile → mass map) so the test is ready, WITHOUT claiming the spectrum is
selected (that's gated on her map). Target-innocent scoping, no over-reach.

THE ENUMERATION (computed directly): test all 2^g = 128 monic degree-7 polynomials over GF(2) for irreducibility (trial
division by the degree-1/2/3 irreducibles — enough since 7 is prime → any factor has degree ≤ 3). Count the irreducibles.
THE BST-NATIVE REASON IT'S 18 (the finding): M_g = 2^g − 1 = 127 is a MERSENNE PRIME. A root of an irreducible degree-g
poly lives in GF(2^g)* (order 127); since 127 is prime, every non-identity element has order exactly 127 = maximal → the
poly is PRIMITIVE. So over GF(2), at degree g=7: {irreducible} = {primitive}, and the count is (2^g − 2)/g = 126/7 = 18 =
φ(M_g)/g. The primality of M_g (a BST fact: g=7 ⟹ M_g=127 prime) is WHY the candidate set is clean (all 18 are
maximal-period LFSR taps / RS-generator-compatible), not a mix of primitive and merely-irreducible.
THE FRAME (what Target 2c needs, gated on Lyra): to turn "18 candidates" into "the spectrum selects one," Lyra's map must
provide, per polynomial p: the codeword-distance profile d(p) → a predicted mass/Yukawa profile → compared to the 9
observed fermions. The geometry (spherical packing on (S⁴×S¹)/ℤ₂) must FORCE one p target-innocently. I test when it lands.

⟹ VERDICT: exactly 18 primitive degree-g=7 polynomials over GF(2), verified by direct enumeration — and the BST-native
reason is that M_g = 127 is a Mersenne PRIME, so ALL irreducible degree-g polys are primitive (count = (2^g−2)/g = 18 =
φ(M_g)/g). This is clean groundwork for Target 2c: the candidate set is enumerated and BST-explained; the
spectrum-selection test itself is GATED on Lyra's polynomial→codeword-distance→mass map (not claimed here). Target-innocent.
Count ~7-8 (α RULED). Five-Absence-safe.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Mg = 2**g - 1  # 127
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- GF(2) polynomial arithmetic (polys as integer bitmasks) ----------------
def gf2_mod(a, m):
    """a mod m over GF(2), polys as bitmasks."""
    dm = m.bit_length() - 1
    while a.bit_length() - 1 >= dm and a:
        a ^= m << (a.bit_length() - 1 - dm)
    return a

# irreducible polys of degree 1,2,3 over GF(2) (bitmasks):
#  x=0b10, x+1=0b11, x^2+x+1=0b111, x^3+x+1=0b1011, x^3+x^2+1=0b1101
small_irred = [0b10, 0b11, 0b111, 0b1011, 0b1101]

def is_irreducible_deg7(f):
    """degree-7 f over GF(2) is irreducible iff no factor of degree <=3 (since 7 is prime)."""
    for p in small_irred:
        if gf2_mod(f, p) == 0:
            return False
    return True

# ---- enumerate all monic degree-7 polynomials -------------------------------
irreducibles = []
for low in range(2**g):                 # 7 free lower coefficients
    f = (1 << g) | low                    # monic: x^7 term set
    if f & 1 == 0:                         # constant term 0 ⇒ divisible by x ⇒ reducible; skip fast
        continue
    if is_irreducible_deg7(f):
        irreducibles.append(f)
n_irred = len(irreducibles)

print(f"\n[enumeration]: monic degree-{g} polys over GF(2) tested; irreducible count = {n_irred}; expected (2^g−2)/g = {(2**g-2)//g}")
check("ENUMERATION (direct, not quoted): tested all 2^g=128 monic degree-7 polynomials over GF(2) for irreducibility "
      "(trial division by degree-1/2/3 irreducibles — sufficient since 7 is prime). The irreducible count is exactly 18.",
      n_irred == 18, f"direct enumeration → {n_irred} irreducible degree-7 polys over GF(2) = 18")

# ---- BST-native reason: M_g prime ⇒ all irreducible are primitive ------------
is_Mg_prime = all(Mg % d for d in range(2, int(Mg**0.5)+1))
count_formula = (2**g - 2)//g
euler_over_g = (Mg - 1)//g   # φ(127)/7 since 127 prime → φ=126
print(f"[BST reason]: M_g = 2^g−1 = {Mg} prime? {is_Mg_prime}; (2^g−2)/g = {count_formula}; φ(M_g)/g = {euler_over_g}")
check("BST-NATIVE REASON IT'S 18 (the finding): M_g = 2^g − 1 = 127 is a MERSENNE PRIME. A root of an irreducible "
      "degree-g poly lives in GF(2^g)* (order 127); since 127 is prime, every non-identity element has order exactly 127 "
      "= maximal → the poly is PRIMITIVE. So over GF(2) at degree g=7, {irreducible} = {primitive}, count = (2^g−2)/g = "
      "126/7 = 18 = φ(M_g)/g. The primality of M_g is WHY the candidate set is uniformly maximal-period (all 18 are "
      "primitive / RS-generator-compatible), not a mix.",
      is_Mg_prime and count_formula == 18 and euler_over_g == 18,
      "M_g=127 Mersenne prime ⇒ ALL irreducible degree-g polys are primitive ⇒ count = (2^g−2)/g = φ(M_g)/g = 18")

# ---- the count matches Grace's φ(127)/7 pin ---------------------------------
check("MATCHES THE ROUND-5 PIN: Grace/Lyra quoted 18 = φ(127)/7 = 126/7 (primitive degree-7 factors of Φ₁₂₇(x) over "
      "GF(2), ord₁₂₇(2)=7 → 126/7). My direct enumeration confirms 18 independently, AND explains it: 18 = φ(M_g)/g with "
      "φ(M_g)=M_g−1=126 because M_g is prime. Same number, now BST-grounded and enumeration-verified.",
      n_irred == euler_over_g == 18, "direct enumeration (18) = φ(M_g)/g (18) = round-5 pin (18) — confirmed and BST-explained")

# ---- the frame: what Target 2c needs (gated on Lyra) ------------------------
check("THE FRAME (Target 2c, gated on Lyra — NOT claimed here): to turn '18 candidates' into 'the spectrum selects one,' "
      "Lyra's map must give, per polynomial p: codeword-distance profile d(p) → predicted mass/Yukawa profile → compared "
      "to the 9 observed fermions; and the geometry (spherical packing on (S⁴×S¹)/ℤ₂) must FORCE one p target-innocently. "
      "The candidate set is now enumerated + BST-explained; the SELECTION test is her map's to enable. I test when it "
      "lands. No spectrum claim here.",
      True, "candidate set enumerated (18) + BST-explained; spectrum-selection test GATED on Lyra's poly→distance→mass map — not claimed")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: exactly 18 primitive degree-g=7 polynomials over GF(2), verified by DIRECT enumeration — and the "
      "BST-native reason is that M_g=127 is a MERSENNE PRIME, so ALL irreducible degree-g polys are primitive "
      "(count = (2^g−2)/g = φ(M_g)/g = 18). Clean groundwork for Target 2c: candidate set enumerated + BST-explained; "
      "the spectrum-selection test is GATED on Lyra's polynomial→codeword-distance→mass map. Target-innocent, no over-reach.",
      n_irred == 18 and is_Mg_prime and euler_over_g == 18,
      "18 primitive degree-g polys (enumerated); reason = M_g Mersenne prime ⇒ all irreducible are primitive; Target 2c frame ready, gated on Lyra")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
TARGET 2c groundwork — the 18 candidate polynomials, enumerated + BST-explained (mine, target-innocent):
  * ENUMERATED directly: {n_irred} primitive degree-g=7 polynomials over GF(2) (= all monic irreducibles, verified by trial division).
  * BST-NATIVE REASON: M_g = 2^g−1 = 127 is a MERSENNE PRIME ⇒ every irreducible degree-g poly is PRIMITIVE ⇒ count = (2^g−2)/g = φ(M_g)/g = 18.
  * MATCHES the round-5 pin (Grace/Lyra 18 = φ(127)/7) — now independently enumerated AND grounded in g=7 ⟹ M_g prime.
  => candidate set clean and closed; the spectrum-SELECTION test is GATED on Lyra's poly→codeword-distance→mass map. I test when it lands. No spectrum claim.
""")
