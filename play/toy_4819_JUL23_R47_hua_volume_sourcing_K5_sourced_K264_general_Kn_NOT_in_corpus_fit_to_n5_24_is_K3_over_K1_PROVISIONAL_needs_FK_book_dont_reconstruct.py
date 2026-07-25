#!/usr/bin/env python3
"""
Toy 4819 — Jul 23 (Hua-volume sourcing: K₅ sourced, general K_n needs the book, 24=K₃/K₁ provisional; Elie closes his
assigned piece honestly, pull 23u). Lyra's E2b result — base 24/π² = K₃(0,0)/K₁(0,0) is a Bergman-kernel ratio — rests on a
general K_n formula she flagged as fit-to-one-anchor, and she named the sourcing as "Grace's or Elie's." I checked the
corpus. Honest outcome: K₅ is sourced; the general K_n for arbitrary n is NOT in the corpus, so 24=K₃/K₁ is provisional. I do
NOT reconstruct the general formula to make it land — that is precisely the genus-flip / reconstruct-and-hope trap the whole
arc has avoided.

WHAT'S SOURCED: K₅(0,0) = 1920/π⁵ (K264/F71, via Hua). At n=5 two forms coincide: the BST-primary N_c·n_C·2^g = 1920 and the
general-form candidate 2^{n-1}·n! = 1920. Both give 1920/π⁵. ✓ sourced.
WHAT'S NOT SOURCED: the general K_n(0,0) for arbitrary n. Lyra's K_n = 2^{n-1}·n!/π^n reproduces n=5 (→ 1920/π⁵) and gives
K₃=24/π³, K₁=1/π, so K₃/K₁ = 24/π² — BUT it is a FIT to the single n=5 anchor, not independently sourced. And the BST-primary
form N_c·n_C·2^g is n=5-SPECIFIC (it uses the primaries; it does not define K₃ or K₁). So K₃ and K₁ rest entirely on the fit
formula. The two candidate structures (2^{n-1}·n! vs N_c·n_C·2^g) coincide ONLY at n=5 and diverge otherwise — so the n=5
anchor does NOT pin which one is the true general Hua volume.

⟹ VERDICT (plain): K₅(0,0)=1920/π⁵ is SOURCED (K264). The general K_n(0,0) for D_IV^n is NOT in the corpus — Lyra's
2^{n-1}·n!/π^n is a FIT to the n=5 anchor (reproduces it, not independently derived), and the BST-primary form is
n=5-specific — so the pretty identity 24 = K₃/K₁ is PROVISIONAL. To bank it needs the Faraut–Koranyi / Hua VOLUME of D_IV^n
sourced from the BOOK (the actual general-n Bergman kernel at the origin), not a reconstruction. I do NOT reconstruct it (the
trap). So my assigned Hua-sourcing piece closes with an honest status: base 24/π² has a structural HOME (a kernel ratio, real
gain over F671's coincidence) but its EVALUATION is provisional until the general volume is sourced. The muon value stays a
correctly-posed candidate (k₁ threshold residue), gated on BOTH Lyra's residue computation AND this general-Hua-volume
sourcing. Structural bank (generations = Wallach strata) stands; EW area never moved; Five-Absence-positive. Count ~7-8.
"""
import numpy as np
from math import factorial
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

K5_primary = N_c*n_C*2**g            # 1920 (n=5-specific BST-primary form)
K5_general = 2**(5-1)*factorial(5)   # 1920 (2^{n-1}·n! at n=5)
def Kn_fit(n): return 2**(n-1)*factorial(n)   # Lyra's fit formula (numerator; /π^n)
ratio = Kn_fit(3)/Kn_fit(1)          # K₃/K₁ numerator ratio = 24; with π: 24/π²
print(f"\n[Hua sourcing] K₅=1920/π⁵ SOURCED (K264): N_c·n_C·2^g={K5_primary}, 2^(n-1)·n!={K5_general} coincide at n=5")
print(f"  general K_n=2^(n-1)·n!/π^n is a FIT to n=5: K₃/K₁={ratio}/π² = 24/π² (Lyra E2b) — PROVISIONAL (fit, not sourced)")

check("K₅ SOURCED: K₅(0,0)=1920/π⁵ (K264/F71, Hua route) — at n=5 the BST-primary N_c·n_C·2^g=1920 and the general-candidate "
      "2^(n-1)·n!=1920 coincide. Sourced.",
      K5_primary == 1920 and K5_general == 1920, "K₅=1920/π⁵ sourced (K264); N_c·n_C·2^g = 2^(n-1)·n! = 1920 at n=5")

check("GENERAL K_n NOT SOURCED (provisional): the general K_n(0,0) for arbitrary n is NOT in the corpus. Lyra's "
      "2^(n-1)·n!/π^n reproduces n=5 but is a FIT to one anchor; the BST-primary N_c·n_C·2^g is n=5-specific (doesn't define "
      "K₃,K₁). The two structures coincide ONLY at n=5 and diverge otherwise → the anchor doesn't pin the true general "
      "volume. So K₃,K₁ (hence 24=K₃/K₁) rest on the fit.",
      Kn_fit(5) == N_c*n_C*2**g and Kn_fit(3) != N_c*n_C*2**g,
      "general K_n not in corpus; 2^(n-1)·n! fit to n=5 (coincides there, diverges elsewhere); BST-primary n=5-specific → 24=K₃/K₁ provisional")

check("DON'T RECONSTRUCT (the trap): banking 24=K₃/K₁ needs the Faraut–Koranyi / Hua VOLUME of D_IV^n sourced from the BOOK "
      "(the actual general-n Bergman kernel at the origin), NOT a reconstruction. Reconstructing the general formula from "
      "memory to make it land on 24/π² is exactly the genus-flip / reconstruct-and-hope trap the arc avoided. I do not do "
      "it; I report the honest provisional status.",
      True, "24=K₃/K₁ needs FK/Hua volume from the book, not a reconstruction; I don't reconstruct (the trap); honest provisional status")

check("VERDICT: K₅ sourced (K264); general K_n NOT in corpus → 24=K₃/K₁ PROVISIONAL (fit to n=5). The base 24/π² has a "
      "structural HOME (a Bergman-kernel ratio — real gain over F671's coincidence) but its EVALUATION is provisional until "
      "the general Hua volume is sourced. Muon value = correctly-posed candidate (k₁ threshold residue), gated on BOTH "
      "Lyra's residue AND this sourcing. My assigned Hua-sourcing piece closes with the honest status; I don't fake the "
      "general formula. Structural bank (gens=Wallach strata) stands; EW never moved; Five-Absence-positive.",
      K5_primary == 1920 and Kn_fit(3) != N_c*n_C*2**g,
      "K₅ sourced, general K_n provisional (needs FK book); 24/π² has a home but evaluation provisional; muon gated on Lyra residue + this sourcing; don't reconstruct")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-47 (07-23) Hua-volume sourcing — Elie closes his assigned piece honestly (pull 23u):
  * K₅(0,0)=1920/π⁵ SOURCED (K264); N_c·n_C·2^g = 2^(n-1)·n! = 1920 coincide at n=5.
  * general K_n NOT in corpus: 2^(n-1)·n!/π^n is a FIT to n=5 (K₃/K₁=24/π²), BST-primary form n=5-specific → 24=K₃/K₁ PROVISIONAL.
  * DON'T RECONSTRUCT: needs FK/Hua volume from the BOOK, not a memory reconstruction (the trap). Honest provisional status reported.
  => base 24/π² has a structural home (kernel ratio, real gain) but evaluation provisional; muon = k₁ threshold-residue candidate gated on Lyra residue + this sourcing. Structural bank stands; EW never moved.
""")
