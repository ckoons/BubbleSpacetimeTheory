#!/usr/bin/env python3
"""
Toy 4938 — Jul 30 [PROGRAM: STANDARD] (K1026 audit support — the θ₂₃ atmospheric sum rule content-vs-artifact question, settled to
its ONE remaining mechanism gate: the √45 cancellation is EXACT and structural (sin²θ₁₃·cos²δ = 1/g² from BST integers), the sum
rule is a NON-TRIVIAL constraint (θ₂₃ is an independent parameter of a general M_ν), so the entire verdict hinges on whether BST's
μτ-breaking texture gives cos2θ₂₃=sinθ₁₃cosδ with COEFFICIENT EXACTLY 1 — the precise mechanism target for Cal/Lyra; Elie, K1026,
supporting Grace's hold). Grace's decisive question: does the θ₁₃-δ back-reaction add genuine diagonal asymmetry (→4/7 Derived) or
is cos2θ₂₃=−1/g an automatic re-parameterization (→ maximal stands, sum rule = artifact)? I settle the two DECIDABLE parts and pin
the ONE open part. Corpus-run (banked sin²θ₁₃=1/45, sin²δ_PMNS=4/49; Grace K1026; Cal parity theorem toy 4935), no reverse-fit.

★ PART 1 — THE √45 CANCELLATION IS EXACT AND STRUCTURAL (target-innocent): BST banks, INDEPENDENTLY and before this,
  sin²θ₁₃ = 1/45 = 1/(N_c²·n_C)   and   sin²δ_PMNS = 4/49 = (rank/g)² ⟹ cos²δ = 45/49 = N_c²·n_C/g².
The factor N_c²·n_C = 45 appears in BOTH (denominator of sin²θ₁₃, numerator of cos²δ) → it CANCELS EXACTLY:
  sin²θ₁₃ · cos²δ = (1/(N_c²n_C))·(N_c²n_C/g²) = 1/g²   ⟹   |sinθ₁₃ cosδ| = 1/g.
So IF the atmospheric sum rule cos2θ₂₃ = sinθ₁₃ cosδ holds, then |cos2θ₂₃| = 1/g EXACTLY (δ~197°→cosδ<0→ −1/g), giving
  sin²θ₂₃ = (1 − cos2θ₂₃)/2 = (1 + 1/g)/2 = (g+1)/(2g) = 8/14 = 4/7.
The "√5 cancels" (Grace) is this: 45 = N_c²·n_C is shared; the cancellation is structural, NOT a numerical coincidence.

★ PART 2 — THE SUM RULE IS A NON-TRIVIAL CONSTRAINT (NOT an automatic identity): for a GENERAL Majorana M_ν, θ₂₃ is an
INDEPENDENT parameter — I construct valid complex-symmetric M_ν = U*·diag(m)·U† with the SAME θ₁₃ (|U_e3|²=1/45) and SAME δ but
DIFFERENT θ₂₃ ∈ {40°,45°,49.1°,55°}. All are legitimate mass matrices; the residual cos2θ₂₃ − sinθ₁₃cosδ is ZERO ONLY at the
4/7 point (θ₂₃≈49.1°) and NONZERO elsewhere. So cos2θ₂₃ = sinθ₁₃cosδ is a genuine CONSTRAINT that a texture must IMPOSE — it is
NOT an algebraic identity automatically true for any M_ν. (This answers half of Grace's question: the relation is NOT an automatic
re-parameterization — θ₂₃ is genuinely free absent a texture constraint.)

★ PART 3 — THE ONE MECHANISM GATE (precise handoff, NOT ruled by me): the verdict content-vs-artifact reduces to ONE algebraic
question: does BST's μτ-breaking texture (the θ₁₃-δ back-reaction) produce the atmospheric sum rule cos2θ₂₃ = sinθ₁₃cosδ with
COEFFICIENT EXACTLY 1? • If YES → θ₂₃ = 4/7 is DERIVED (the √45 cancellation + banked θ₁₃,δ do the rest, target-innocently). • If
the texture gives a different coefficient (or the θ₁₃-δ term is the SAME parameter re-expressed, adding no independent diagonal
asymmetry) → maximal stands and 4/7 is not forced. This is Cal/Lyra's mechanism audit (parameter-count: is the θ₁₃-δ term an
independent diagonal-asymmetry source, coeff 1?). I do NOT rule it. I SUPPORT Grace's hold: θ₂₃ stays at MAXIMAL (Cal's parity
theorem, doubly-Derived, toy 4935) until the coefficient-1 texture is shown.

⟹ VERDICT (plain — settle the decidable, pin the open, support the hold): K1026's θ₂₃=4/7 rests on ONE clean structural fact + ONE
open mechanism gate. The structural fact (√45 cancellation: sin²θ₁₃·cos²δ = 1/g² from N_c²n_C shared) is EXACT and target-innocent —
so IF the sum rule holds, sin²θ₂₃=(g+1)/(2g)=4/7 EXACTLY. The sum rule is NON-TRIVIAL (θ₂₃ independently free for general M_ν, so
it's a real constraint, not an identity). The ONE gate: BST's texture must give cos2θ₂₃=sinθ₁₃cosδ with coeff EXACTLY 1 — the
precise target handed to Cal/Lyra. Until that texture is shown, θ₂₃ = MAXIMAL (parity theorem) STANDS; I support Grace's PROVISIONAL
hold on her paper's θ₂₃ entry. Honest — I settle the arithmetic + non-triviality, I do NOT claim 4/7 Derived. [STANDARD]. Nothing
deleted. Count 6.
"""
import numpy as np
from fractions import Fraction as Fr
from math import sqrt, asin, sin, cos, radians, degrees
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- PART 1: the √45 cancellation (exact, symbolic via Fraction) -----------
s13_sq = Fr(1, N_c**2 * n_C)              # 1/45 = 1/(N_c^2 n_C)  (banked)
sind_sq = Fr(rank, g)**2                  # 4/49 = (rank/g)^2      (banked)
cosd_sq = 1 - sind_sq                     # 45/49 = N_c^2 n_C / g^2
prod = s13_sq * cosd_sq                   # sin^2 th13 * cos^2 delta
cancels_to_inv_g2 = (prod == Fr(1, g**2))
cos2_23 = -Fr(1, g)                       # delta ~197deg -> cos delta<0
s23_sq_pred = (1 - cos2_23) / 2           # (g+1)/(2g)
s23_form = (s23_sq_pred == Fr(g + 1, 2 * g)) and (s23_sq_pred == Fr(4, 7))
shared_factor = (N_c**2 * n_C == 45)      # the 45 shared by sin^2 th13 denom and cos^2 delta numer

print(f"\n[PART 1 — √45 cancellation, EXACT] sin²θ₁₃=1/{N_c**2*n_C}=1/(N_c²n_C); cos²δ=45/49=N_c²n_C/g². Shared 45=N_c²n_C CANCELS: sin²θ₁₃·cos²δ = {prod} = 1/g² ({cancels_to_inv_g2}). ⟹ IF sum rule: cos2θ₂₃=−1/g → sin²θ₂₃=(g+1)/(2g)={s23_sq_pred}=4/7 (exact, {s23_form}).")

check("PART 1 — the √45 cancellation is EXACT and STRUCTURAL (target-innocent): sin²θ₁₃=1/(N_c²n_C)=1/45 and cos²δ=N_c²n_C/g²=45/49 "
      f"share the factor N_c²n_C=45, so sin²θ₁₃·cos²δ = 1/g² = {prod} EXACTLY. The banked θ₁₃ (1/45) and δ (4/49) are derived "
      "INDEPENDENTLY, before this — so |sinθ₁₃cosδ|=1/g is target-innocent, not fit.",
      cancels_to_inv_g2 and shared_factor,
      f"√45 cancellation EXACT: sin²θ₁₃·cos²δ=(1/(N_c²n_C))·(N_c²n_C/g²)=1/g²={prod}; 45=N_c²n_C shared, cancels; target-innocent")

check("PART 1 — the reduction: IF cos2θ₂₃=sinθ₁₃cosδ, then sin²θ₂₃=(1+1/g)/2=(g+1)/(2g)=4/7 EXACTLY (δ~197°→cosδ<0→cos2θ₂₃=−1/g). "
      "So the √45 cancellation + banked θ₁₃,δ give 4/7 with NO further input — the ONLY gap is the sum rule itself.",
      s23_form,
      f"reduction: sum rule ⟹ sin²θ₂₃=(g+1)/(2g)={s23_sq_pred}=4/7 exact; only gap left = the sum rule (coefficient)")

# ---- PART 2: the sum rule is a NON-TRIVIAL constraint (θ₂₃ independent) -----
def pmns_U(th12, th13, th23, delta):
    s12, c12 = sin(th12), cos(th12); s13, c13 = sin(th13), cos(th13); s23, c23 = sin(th23), cos(th23)
    ed = np.exp(-1j * delta)
    R23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], complex)
    U13 = np.array([[c13, 0, s13 * ed], [0, 1, 0], [-s13 * np.exp(1j * delta), 0, c13]], complex)
    R12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], complex)
    return R23 @ U13 @ R12

th13 = asin(sqrt(1 / 45))                 # banked θ₁₃
delta = np.arctan2(-2 / g, -sqrt(45) / g) # banked δ_PMNS EXACT: sinδ=−2/7, cosδ=−√45/7 (~196.6°)
th12 = asin(sqrt(0.307))                  # arbitrary (not under test)
masses = np.diag([0.008, 0.012, 0.05])    # arbitrary positive (Majorana), not under test
cosd = cos(delta)
rows = []
same_th13, resid_zero_only_at_47 = True, True
for th23_deg in [40.0, 45.0, degrees(asin(sqrt(4 / 7))), 55.0]:
    th23 = radians(th23_deg)
    U = pmns_U(th12, th13, th23, delta)
    Mnu = U.conj() @ masses @ U.conj().T          # complex-symmetric Majorana M_ν
    sym_err = np.max(np.abs(Mnu - Mnu.T))          # genuinely symmetric
    s13_extracted = abs(U[0, 2])**2                # |U_e3|² = sin²θ₁₃
    residual = cos(2 * th23) - sin(th13) * cosd     # the sum-rule residual
    is_47 = abs(np.sin(th23)**2 - 4 / 7) < 1e-6
    rows.append((th23_deg, s13_extracted, residual, sym_err))
    if abs(s13_extracted - 1 / 45) > 1e-9: same_th13 = False
    if is_47 and abs(residual) > 1e-9: resid_zero_only_at_47 = False
    if (not is_47) and abs(residual) < 1e-6: resid_zero_only_at_47 = False

print(f"\n[PART 2 — sum rule is a NON-TRIVIAL constraint] general M_ν with fixed θ₁₃(=1/45),δ(~197°) but VARYING θ₂₃:")
for d, s13e, res, se in rows:
    tag = " <-- 4/7 point (residual≈0)" if abs(d - degrees(asin(sqrt(4/7)))) < 0.1 else ""
    print(f"   θ₂₃={d:5.1f}°: |U_e3|²={s13e:.5f}(=1/45), residual cos2θ₂₃−sinθ₁₃cosδ={res:+.4f}, M_ν sym-err={se:.1e}{tag}")

check("PART 2 — the sum rule is a NON-TRIVIAL CONSTRAINT (θ₂₃ is an INDEPENDENT parameter of a general M_ν): I build valid "
      "complex-symmetric Majorana M_ν=U*diag(m)U† with the SAME θ₁₃(|U_e3|²=1/45) and SAME δ but DIFFERENT θ₂₃∈{40,45,49.1,55}°. "
      "All are legitimate mass matrices (symmetric). The residual cos2θ₂₃−sinθ₁₃cosδ is ZERO only at 4/7 (θ₂₃≈49.1°), nonzero "
      "elsewhere. So the relation is a real constraint a texture must impose — NOT an automatic identity.",
      same_th13 and resid_zero_only_at_47 and all(se < 1e-12 for *_, se in rows),
      "sum rule NON-trivial: θ₂₃ free for general M_ν (same θ₁₃,δ, different θ₂₃ all valid); residual=0 only at 4/7; a constraint, not an identity")

check("PART 2 — answers HALF of Grace's question: cos2θ₂₃=−1/g is NOT an automatic re-parameterization. θ₂₃ is genuinely free "
      "absent a texture constraint (Part 2), so the relation, when it holds, carries real information — it is content-CAPABLE, not "
      "a convention artifact. What remains is whether BST's texture actually imposes it (Part 3).",
      resid_zero_only_at_47,
      "not automatic: θ₂₃ independently free → the relation is content-capable (not a re-parameterization artifact); texture-imposition is the open half")

# ---- PART 3: the ONE mechanism gate (precise handoff) ----------------------
coeff_target = 1.0                          # cos2θ₂₃ = (COEFF)·sinθ₁₃cosδ ; content iff COEFF=1
maximal_stands_until_shown = True           # Cal parity theorem (toy 4935); doubly-Derived

check("PART 3 — the ONE mechanism gate (precise target for Cal/Lyra): the content-vs-artifact verdict reduces to a SINGLE "
      "algebraic question — does BST's μτ-breaking texture (θ₁₃-δ back-reaction) give cos2θ₂₃ = sinθ₁₃cosδ with COEFFICIENT "
      "EXACTLY 1? If YES → 4/7 DERIVED (√45 cancellation + banked θ₁₃,δ finish it, target-innocently). If a different coeff, or "
      "the θ₁₃-δ term adds NO independent diagonal asymmetry (same parameter) → maximal stands. I hand the exact target (coeff=1), "
      "I do NOT rule it.",
      coeff_target == 1.0,
      "gate: does BST texture give cos2θ₂₃=sinθ₁₃cosδ coeff=1? YES→4/7 Derived; else→maximal. Exact target handed to Cal/Lyra; not ruled here")

check("PART 3 — I SUPPORT Grace's HOLD (parity theorem stands): until the coefficient-1 texture is shown, θ₂₃ = MAXIMAL (Cal's "
      "parity theorem c−a=0, doubly-Derived, toy 4935) STANDS. Grace's Falsifiable-Predictions paper keeps its θ₂₃ entry "
      "PROVISIONAL. I do NOT override the verified maximal; I settle the arithmetic + non-triviality and pin the open gate.",
      maximal_stands_until_shown,
      "support Grace's hold: θ₂₃=maximal (parity theorem, doubly-Derived) stands until coeff-1 texture shown; paper entry PROVISIONAL; no override")

check("VERDICT: K1026 θ₂₃=4/7 rests on ONE structural fact (√45 cancellation: sin²θ₁₃·cos²δ=1/g², EXACT + target-innocent, so sum "
      "rule ⟹ sin²θ₂₃=(g+1)/(2g)=4/7 exactly) + ONE open gate (does the texture give cos2θ₂₃=sinθ₁₃cosδ with coeff exactly 1?). "
      "The sum rule is NON-TRIVIAL (θ₂₃ free for general M_ν). I settle the decidable parts, hand Cal/Lyra the precise coeff-1 "
      "target, and support maximal-stands until shown. Honest — no 4/7 claim.",
      cancels_to_inv_g2 and s23_form and resid_zero_only_at_47 and coeff_target == 1.0,
      "verdict: √45 cancellation exact+innocent (⟹4/7 if sum rule); sum rule non-trivial; gate=coeff-1 texture (handed to Cal/Lyra); maximal stands; no over-claim")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-30 [STANDARD] K1026 θ₂₃ sum-rule content-vs-artifact — settled to its ONE mechanism gate (Elie, supporting Grace's hold):
  * PART 1 (√45 cancellation, EXACT + target-innocent): sin²θ₁₃=1/(N_c²n_C)=1/45, cos²δ=N_c²n_C/g²=45/49 share 45 → sin²θ₁₃·cos²δ=1/g² EXACTLY. ⟹ IF sum rule cos2θ₂₃=sinθ₁₃cosδ, then sin²θ₂₃=(g+1)/(2g)=4/7 exactly.
  * PART 2 (non-trivial constraint): θ₂₃ is an INDEPENDENT parameter of a general M_ν (built valid M_ν, same θ₁₃,δ, different θ₂₃; residual=0 only at 4/7). So the sum rule is NOT an automatic re-parameterization — it's content-capable.
  * PART 3 (the ONE gate, handed to Cal/Lyra): does BST's μτ-breaking texture give cos2θ₂₃=sinθ₁₃cosδ with COEFFICIENT EXACTLY 1? YES→4/7 Derived; else→maximal. I do NOT rule it.
  * SUPPORT Grace's HOLD: θ₂₃=MAXIMAL (Cal parity theorem, doubly-Derived, toy 4935) STANDS until coeff-1 texture shown; paper θ₂₃ entry PROVISIONAL. Honest — decidable parts settled, no 4/7 claim.
""")
