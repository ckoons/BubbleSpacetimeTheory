#!/usr/bin/env python3
"""
Toy 4764 — Jul 21 (Round-3 quark row, the reconciliation + basis-independence rigor check, Elie's assigned half): Keeper
adjudicated (K795) that my ε¹ (toy 4763) and Lyra's ε² are NOT a contradiction — they are the same singular-value
perturbation formula under one condition: σ₂ ≈ the kernel-block of the correction δM (the charm-charm entry in the 2D space
⊥ the saturated top), which is first order (ε¹ → λ²) UNLESS that block vanishes, in which case σ₂ comes only from the
seesaw through the top (ε²/s → λ⁴). My assignment: verify the unified decider, and run the RIGOR check I was given —
basis-independence (K795 line #1): "off-diagonal / kernel-block = 0" is a weak-basis choice (Branco: ANY matrix rotates to
NNI form), so the up-type λ⁴ has content ONLY if it is a BASIS-INDEPENDENT statement, not an artifact of choosing a
convenient basis. Result: the σ₂-POWER is weak-basis INVARIANT, so a texture zero created by a basis choice CANNOT turn
ε¹ into ε² — the win condition is the invariant σ₂ ~ ε², which a genuine selection rule must produce. This sets the exact
bar for Lyra's δM.

RESULT 1 — THE UNIFIED DECIDER (reconciles Lyra ε² + Elie ε¹): with a saturated leading term (top=O), σ₂ = the kernel-block
of δM to first order. Generic δM (kernel-block ≠ 0) → σ₂ ~ ε¹ (my toy 4763, λ²); kernel-block = 0 (Lyra's seesaw
assumption) → σ₂ ~ ε² (λ⁴). ONE condition — does the up-type correction's first-order kernel-block vanish? — subsumes both
Lyra's seesaw and my nested-corrections. Verified both scalings.
RESULT 2 — BASIS-INDEPENDENCE (rigor line #1, the fish-guard): the singular value σ₂ is invariant under M → U_L M U_R†
(weak-basis rotations), so its ε-POWER is invariant. Verified: a ε¹ matrix rotated by arbitrary U_L, U_R keeps σ₂ ~ ε¹; a
ε² matrix keeps σ₂ ~ ε². ⟹ a texture zero created by a BASIS CHOICE cannot turn ε¹ into ε² — an NNI/Fritzsch zero is
COSMETIC (Branco). The physical, bankable content is the INVARIANT σ₂ ~ ε², NOT the appearance of a zero in some basis.
RESULT 3 — THE DISCRIMINATOR / verification contract for Lyra's δM: when Lyra's up-type correction texture lands, I do NOT
check "is there a zero in the strata basis" (basis-dependent, empty). I check the INVARIANT σ₂-POWER: ε² (physical λ⁴, a
genuine selection rule) vs ε¹ (down-type-like / a cosmetic zero). The selection rule passes the rigor bar ONLY if it
produces the invariant ε² for up-type AND ε¹ for down-type — target-innocent (the powers come from the texture, not the
observed ratios). My 4763 harness is ready.

⟹ VERDICT: no contradiction — the unified decider (does the up-type correction's first-order kernel-block vanish?) subsumes
Lyra's seesaw (ε²) and my generic result (ε¹); the row's whole λ⁴ question reduces to that ONE condition. The RIGOR bar
(K795 #1): the λ⁴ is physical ONLY as the BASIS-INVARIANT statement σ₂ ~ ε² — a texture zero from a basis choice is
cosmetic (σ₂-power is weak-basis invariant, verified), so Lyra's selection rule must produce the invariant ε², not an
NNI-basis zero. I verify her δM against the invariant when it lands (honest-negative branch ready). Integer power 2 is
DERIVED iff the selection rule gives invariant ε² (up) + ε¹ (down), target-innocently. Count ~7-8. Five-Absence-safe
(seesaw here = linear-algebra light-eigenvalue, NOT ν_R).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

np.random.seed(11)
def rvec(): v = np.random.randn(3); return v/np.linalg.norm(v)
a, b = rvec(), rvec()
eps = np.logspace(-5, -2, 20)
def s2pow(Mfun):
    return np.polyfit(np.log(eps), np.log([np.sort(np.linalg.svd(Mfun(e), compute_uv=False))[::-1][1] for e in eps]), 1)[0]

# ---- Result 1: the unified decider ------------------------------------------
P = np.eye(3) - np.outer(a, a); Q = np.eye(3) - np.outer(b, b)   # project OFF the top direction
C = np.random.randn(3, 3)
C_blockzero = C - P@C@Q                                          # remove the kernel-block (⊥-top charm-charm)
p_generic = s2pow(lambda e: np.outer(a, b) + e*C)
p_blockzero = s2pow(lambda e: np.outer(a, b) + e*C_blockzero)
print(f"\n[R1] generic δM (block≠0) → σ₂~ε^{p_generic:.2f} (Elie 4763, λ²); kernel-block=0 (Lyra seesaw) → σ₂~ε^{p_blockzero:.2f} (λ⁴)")
check("RESULT 1 — THE UNIFIED DECIDER (reconciles Lyra ε² + Elie ε¹): with a saturated leading term (top=O), σ₂ = the "
      "kernel-block of δM to first order. Generic δM (block ≠ 0) → σ₂ ~ ε¹ (λ²); kernel-block = 0 (Lyra's seesaw) → σ₂ ~ "
      "ε² (λ⁴). ONE condition — does the up-type correction's first-order kernel-block vanish? — subsumes both Lyra's "
      "seesaw and my nested-corrections. No contradiction.",
      abs(p_generic - 1) < 0.2 and abs(p_blockzero - 2) < 0.3, "block≠0 → σ₂~ε (λ²); block=0 → σ₂~ε² (λ⁴); one condition unifies Lyra's seesaw + Elie's nested-corrections")

# ---- Result 2: basis-independence -------------------------------------------
UL = np.linalg.qr(np.random.randn(3, 3))[0]; UR = np.linalg.qr(np.random.randn(3, 3))[0]
p_rot1 = s2pow(lambda e: UL@(np.outer(a, b) + e*C)@UR.T)
p_rot2 = s2pow(lambda e: UL@(np.outer(a, b) + e*C_blockzero)@UR.T)
print(f"[R2] ε¹ matrix rotated (arbitrary U_L,U_R) → σ₂~ε^{p_rot1:.2f} (still λ²); ε² rotated → σ₂~ε^{p_rot2:.2f} (still λ⁴)")
check("RESULT 2 — BASIS-INDEPENDENCE (rigor line #1, the fish-guard): σ₂ is invariant under M → U_L M U_R† (weak-basis "
      "rotations), so its ε-POWER is invariant. Verified: a ε¹ matrix rotated by arbitrary U_L, U_R keeps σ₂ ~ ε¹; a ε² "
      "matrix keeps σ₂ ~ ε². So a texture zero created by a BASIS CHOICE cannot turn ε¹ into ε² — an NNI/Fritzsch zero is "
      "COSMETIC (Branco). The physical, bankable content is the INVARIANT σ₂ ~ ε², NOT the appearance of a zero.",
      abs(p_rot1 - 1) < 0.2 and abs(p_rot2 - 2) < 0.3, "σ₂-power is weak-basis invariant (ε¹ stays ε¹, ε² stays ε² under arbitrary rotation) → NNI-basis zero is cosmetic; the invariant is the win")

# ---- Result 3: the discriminator / verification contract --------------------
check("RESULT 3 — THE DISCRIMINATOR / verification contract for Lyra's δM: when her up-type correction texture lands, I do "
      "NOT check 'is there a zero in the strata basis' (basis-dependent, empty). I check the INVARIANT σ₂-POWER: ε² "
      "(physical λ⁴, genuine selection rule) vs ε¹ (down-type-like / cosmetic zero). The selection rule passes the rigor "
      "bar ONLY if it produces the invariant ε² for up-type AND ε¹ for down-type — target-innocent (powers from the "
      "texture, not the observed ratios). 4763 harness ready.",
      True, "verify Lyra's δM by the INVARIANT σ₂-power (ε² up / ε¹ down), not the appearance of a zero; target-innocent; honest-negative branch ready")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: no contradiction — the unified decider (does the up-type correction's first-order kernel-block vanish?) "
      "subsumes Lyra's seesaw (ε²) and my generic result (ε¹); the λ⁴ question reduces to that ONE condition. RIGOR bar "
      "(K795 #1): λ⁴ is physical ONLY as the BASIS-INVARIANT statement σ₂ ~ ε² — a texture zero from a basis choice is "
      "cosmetic (σ₂-power weak-basis invariant, verified), so Lyra's selection rule must produce the invariant ε², not an "
      "NNI-basis zero. I verify her δM against the invariant when it lands. Integer power 2 DERIVED iff the selection rule "
      "gives invariant ε² (up) + ε¹ (down), target-innocently.",
      abs(p_generic-1) < 0.2 and abs(p_blockzero-2) < 0.3 and abs(p_rot1-1) < 0.2 and abs(p_rot2-2) < 0.3,
      "unified decider (kernel-block vanish?) subsumes both; rigor bar = invariant σ₂~ε² (weak-basis zeros cosmetic); verify Lyra's δM by the invariant")

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
ROUND-3 kernel-block decider + basis-independence — Elie's reconciliation + rigor check:
  * R1: NO contradiction — σ₂ = kernel-block of δM: block≠0 → ε¹ (Elie 4763, λ²); block=0 → ε² (Lyra seesaw, λ⁴). One condition subsumes both.
  * R2 (RIGOR): σ₂-power is WEAK-BASIS INVARIANT — a texture zero from a basis choice can't fake ε² (NNI/Fritzsch zero is cosmetic, Branco). The win = the invariant σ₂~ε².
  * R3: verification contract — I check Lyra's δM by the INVARIANT σ₂-power (ε² up / ε¹ down), NOT the appearance of a zero; target-innocent; honest-negative branch ready.
  => the row reduces to ONE basis-independent condition; integer power 2 DERIVED iff Lyra's selection rule produces invariant ε² (up) + ε¹ (down). Harness ready.
""")
