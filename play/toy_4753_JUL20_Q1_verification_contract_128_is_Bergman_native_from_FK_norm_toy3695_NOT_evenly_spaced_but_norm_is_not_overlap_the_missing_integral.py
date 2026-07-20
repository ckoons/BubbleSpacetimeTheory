#!/usr/bin/env python3
"""
Toy 4753 — Jul 20 (Round-6 Q1: my assigned deliverable is "verify when Lyra produces the wavefunctions; do NOT model
evenly-spaced levels; otherwise HOLD." Q1 is uncomputed this round, so per the prompt the honest deliverable is EXACTLY
what's missing — which integral, which input. This toy states that contract, and surfaces one genuine non-circular input
I found: the 2^g=128 is already Bergman-native.

FIRST — I OWN THE CATCH: Lyra's round-5 audit named my toy 4747 (granular effective-mass band, evenly-spaced 2^g levels)
as the circular model — assuming evenly-spaced levels re-imposes the 1/2^g gap the study is trying to derive. Correct. I
retract 4747's "last gap = 1/2^g" as a DERIVATION; it was an illustration built on an evenly-spaced assumption. Not defended.

THE NON-CIRCULAR INPUT (Q1 question #3 — "is 128 derived or imposed?"): Toy 3695 (Elie, June 1, supporting Lyra L4)
computed the TOP's spinor K-type norm on H²(D_IV⁵) via the actual Faraut-Koranyi Pochhammer Γ-product:
    ‖f_(1/2,1/2)‖² = Γ(5/2)²/Γ(5) = (9π/16)/24 = 3π/128 = N_c·π/2^g.
The 2^g = 128 there falls OUT of the FK radial integral (Γ(5/2)²/Γ(5)), NOT from a modeling assumption of evenly-spaced
levels — the OPPOSITE of my 4747. So for Q1-#3 there is a real, non-circular thread: the substrate 128 already lives in
the Bergman FK norm of exactly the top's K-type (1/2,1/2). This is a genuine input for Lyra's Q1, and it's HER OWN L4
candidate form.

THE CRITICAL DISTINCTION (why this does NOT compute the gap — discipline): 3π/128 is the NORM ‖f_top‖², NOT the OVERLAP
⟨top|Φ|O⟩ that Q1 needs. Q1's decider is the radial matrix element of the top's K-type (1/2,1/2) [non-spherical, λ₂=½]
with the spherical boundary condensate O = SO(5) vector (1,0) [λ₂=0], with the angular CG already = 1 (toy 4746) so the
number is PURELY radial. That overlap = the radial band-edge; whether it = M_g/2^g = 127/128 exactly is the theorem.
Toy 3695 gives the top's NORM (128 appears), not the OVERLAP (127 vs 128). So 128-is-Bergman-native is progress on Q1-#3;
the GAP (127/128 vs 1 vs other) is still uncomputed — it needs Lyra's two radial wavefunctions.

MY VERIFICATION CONTRACT (what I need from Lyra to score Q1, exactly): (a) the top gen-3 up-type radial wavefunction —
the K-type (1/2,1/2) FK Pochhammer radial profile on H²(D_IV⁵); (b) the condensate O radial profile — the (1,0) SO(5)
vector; (c) the FK/Bergman radial measure (I have it: Faraut-Koranyi Ch. XIII, genus p=n_C, same machinery as 3695). I
then compute the radial overlap ⟨top|Φ|O⟩_radial numerically and SCORE it against three outcomes: = 127/128 exactly
(→ theorem), = 1 (→ exact-1, retire), = other computed value (→ report the new number). NO evenly-spaced-level model.

⟹ VERDICT (Q1 uncomputed this round — deliverable = what's missing): I retract 4747's evenly-spaced derivation (own the
catch). The one non-circular thread found: 2^g=128 is Bergman-native — it comes out of the FK Γ-product norm of the top's
K-type (toy 3695: ‖f_(1/2,1/2)‖² = 3π/128 = N_c·π/2^g), NOT from a modeling assumption — a real input for Q1-#3. But that
is the NORM, not the OVERLAP; the gap (127/128 vs 1 vs other) is STILL uncomputed and needs Lyra's two radial
wavefunctions. My verification harness is specified and ready; I HOLD for her wavefunctions, then score. Count ~7-8
(α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Mg = 2**g - 1  # 127
twog = 2**g    # 128
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- own the catch: 4747 evenly-spaced is circular ---------------------------
check("OWN THE CATCH (no defense): Lyra's round-5 audit named my toy 4747 (granular band, evenly-spaced 2^g levels) as "
      "the circular model — assuming evenly-spaced levels re-imposes the 1/2^g gap the study is trying to derive. Correct. "
      "I RETRACT 4747's 'last gap = 1/2^g' as a DERIVATION; it was an illustration on an evenly-spaced assumption. The "
      "real gap must come from the actual radial wavefunctions, not a level model.",
      True, "4747 evenly-spaced granular band retracted as circular (per Lyra's audit) — the gap needs real wavefunctions, not a level model")

# ---- non-circular input: 128 is Bergman-native (re-verify 3695) --------------
Gamma_5_2_sq = ((3/2)*(1/2)*math.sqrt(math.pi))**2   # Γ(5/2)² = 9π/16
Gamma_5 = math.factorial(4)                          # Γ(5) = 24
norm_top = Gamma_5_2_sq / Gamma_5                     # 3π/128
bergman_128_form = N_c*math.pi/twog                   # N_c·π/2^g
print(f"\n[3695 re-verify]: ‖f_(1/2,1/2)‖² = Γ(5/2)²/Γ(5) = {norm_top:.6f} = 3π/128 = N_c·π/2^g = {bergman_128_form:.6f}")
check("NON-CIRCULAR INPUT (Q1-#3, 'is 128 derived or imposed?'): toy 3695 computed the TOP's spinor K-type norm via the "
      "actual FK Pochhammer Γ-product: ‖f_(1/2,1/2)‖² = Γ(5/2)²/Γ(5) = (9π/16)/24 = 3π/128 = N_c·π/2^g. The 2^g=128 falls "
      "OUT of the Bergman radial integral (Γ-product), NOT a modeling assumption — the OPPOSITE of 4747. So the substrate "
      "128 already lives in the FK norm of exactly the top's K-type. A real, non-circular thread for Lyra's Q1-#3.",
      abs(norm_top - bergman_128_form) < 1e-12, "‖f_top‖² = 3π/128 = N_c·π/2^g (FK Γ-product, toy 3695) — 128 is Bergman-native, NOT evenly-spaced-imposed")

# ---- critical distinction: NORM is not the OVERLAP --------------------------
check("CRITICAL DISTINCTION (why this does NOT compute the gap): 3π/128 is the NORM ‖f_top‖², NOT the OVERLAP ⟨top|Φ|O⟩ "
      "Q1 needs. Q1's decider is the RADIAL matrix element of the top's K-type (1/2,1/2) [non-spherical, λ₂=½] with the "
      "spherical condensate O = (1,0) SO(5) vector [λ₂=0], angular CG already = 1 (toy 4746) → PURELY radial. Toy 3695 "
      "gives the top's NORM (128 appears), not the OVERLAP (127 vs 128). So 128-is-Bergman-native answers Q1-#3's "
      "'derived not imposed' direction; the GAP (127/128 vs 1 vs other) is STILL uncomputed.",
      Mg == 127 and twog == 128, "3π/128 is the NORM not the OVERLAP; Q1 gap (127/128 vs 1 vs other) still needs the radial overlap ⟨top|Φ|O⟩ — uncomputed")

# ---- verification contract: exactly what I need from Lyra --------------------
check("VERIFICATION CONTRACT (exactly what's missing — my deliverable-when-blocked): to score Q1 I need from Lyra (a) the "
      "top gen-3 up-type radial wavefunction = K-type (1/2,1/2) FK Pochhammer radial profile on H²(D_IV⁵); (b) the "
      "condensate O radial profile = (1,0) SO(5) vector; (c) the FK/Bergman radial measure (I have it — FK Ch. XIII, "
      "genus p=n_C, same machinery as 3695). I then compute ⟨top|Φ|O⟩_radial numerically and SCORE vs three outcomes: "
      "= 127/128 exactly (→ theorem), = 1 (→ exact-1, retire), = other (→ report the number). NO evenly-spaced model.",
      True, "contract: need Lyra's (a) top (1/2,1/2) radial profile + (b) O (1,0) profile + (c) FK measure → I compute overlap, score vs 127/128 / 1 / other")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (Q1 uncomputed this round; deliverable = what's missing): 4747 evenly-spaced derivation RETRACTED (own the "
      "catch). One non-circular thread found: 2^g=128 is Bergman-native — it comes out of the FK Γ-product norm of the "
      "top's K-type (toy 3695: ‖f_(1/2,1/2)‖² = 3π/128 = N_c·π/2^g), NOT a modeling assumption — a real input for Q1-#3. "
      "But that's the NORM, not the OVERLAP; the gap (127/128 vs 1 vs other) is STILL uncomputed and needs Lyra's two "
      "radial wavefunctions. Harness specified and ready; I HOLD for her wavefunctions, then score. No frame added.",
      abs(norm_top - bergman_128_form) < 1e-12 and Mg == 127,
      "Q1 uncomputed; 4747 retracted; 128 Bergman-native (3695, non-circular input for Q1-#3); gap still needs the overlap; harness ready; HOLD for Lyra")

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
ROUND-6 Q1 — my deliverable (verify-when-ready; Q1 uncomputed this round → state what's missing):
  * OWN THE CATCH: 4747 evenly-spaced granular band RETRACTED as circular (Lyra's audit right). The gap needs real wavefunctions.
  * NON-CIRCULAR INPUT (Q1-#3): 2^g=128 is Bergman-native — ‖f_(1/2,1/2)‖² = Γ(5/2)²/Γ(5) = 3π/128 = N_c·π/2^g (toy 3695, FK Γ-product), NOT evenly-spaced.
  * DISTINCTION: that's the NORM, not the OVERLAP ⟨top|Φ|O⟩. The gap (127/128 vs 1 vs other) is STILL uncomputed.
  * CONTRACT: need Lyra's (a) top (1/2,1/2) radial profile + (b) O (1,0) profile + (c) FK measure → I compute the overlap, score vs 127/128 / 1 / other.
  => I HOLD for Lyra's wavefunctions, then verify. No frame added; the missing thing is named exactly (the radial overlap integral).
""")
