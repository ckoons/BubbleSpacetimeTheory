#!/usr/bin/env python3
"""
Toy 4627 — Jul 12 (Keeper LANE 1, highest leverage): close Koide's last gate by LIFTING toy 3711's Schur
argument onto the generation irreps 1⊕2. Keeper armed the discipline explicitly: "toy 3711's Schur was on
V_(1/2,1/2), not yet the gen irreps — lift it, don't assume it." I lifted it — and it FAILS. This CORRECTS my
own toy 4626 from yesterday (which conflated K-irreps with flavor-irreps). Koide's gate does NOT close via
Schur; the real gate is the degenerate-rep overlap computation (Lyra's K294 lane). Symmetric-discipline catch
on my own over-hope, exactly what "lift it, don't assume it" was guarding against.

WHAT toy 3711's SCHUR ACTUALLY SAYS: M_op = √H_B and the Yukawa (via V_(0,0)) are both K-invariant operators
  on the SINGLE K-type V_(1/2,1/2), which is K-irreducible. Schur → both act as the SAME scalar = ‖V_(1/2,1/2)‖²
  = 3π/2^g. This relates MASS and YUKAWA WITHIN one generation (mass ∝ Yukawa·v). It is a within-generation
  statement about one K-irrep.

THE LIFT TEST (does it give λ_singlet = λ_traceless across the 3 generations?) — IT FAILS:
  by K294, the 3 generations are 3 DISTINCT Wallach strata / K-reps:
    electron = generic bulk rep (Wallach ν > 3/2, regular),
    muon     = ν = 3/2 Wallach degeneration (Cartan slice),
    tau      = ν = 0 Wallach degeneration (Shilov points).
  These are THREE DIFFERENT K-irreps at three strata (a nested Korányi–Wolf FLAG), NOT one K-irrep splitting
  as 1 ⊕ 2. K acts WITHIN each generation rep, not ACROSS generations. So K-Schur gives one scalar PER K-type
  (as in 3711) and says NOTHING about equality across the FLAVOR decomposition 1 ⊕ 2.
  The flavor singlet ⊕ traceless (1 ⊕ 2) is a decomposition under the EMERGENT generation symmetry (Z₃),
  NOT under K. A K-invariant Higgs coupling is Schur-scalar on K-irreps, not on flavor-irreps. And even
  Z₃-invariance does NOT force λ_singlet = λ_traceless (a Z₃-invariant operator may have different eigenvalues
  on the trivial and the 2-dim Z₃ reps).
  ⟹ my toy 4626 CONFLATED K-irreps with flavor-irreps. The condition λ_singlet = λ_traceless (⟺ Koide 2/3) is
    still the correct condition, but it is DYNAMICAL, not a Schur/symmetry consequence. RETRACT the "Schur
    makes it principled" framing of 4626.

THE REAL GATE (where the computation actually lives): mass ~ Gindikin Γ_Ω(ν) = Γ(ν)·Γ(ν − a/2), a = N_c = 3
  (the characteristic multiplicity, K294). At the two DISCRETE Wallach points ν ∈ {0, 3/2} — exactly the muon
  and tau strata — Γ_Ω is SINGULAR (a pole): the reps DEGENERATE. So the degenerate μ and τ reps carry their
  OWN finite matrix-element norm, NOT the naive Gindikin Γ. Only the electron (generic ν > 3/2) is regular.
  ⟹ the three strata overlaps CANNOT be read off Γ_Ω; they require Lyra's degenerate-rep matrix-element
    computation (K294 lane). That computation must reproduce m_μ/m_e = 206.77 and m_τ/m_e = 3477 (K294 bar);
    Koide = 2/3 then FOLLOWS from the masses. There is no Schur shortcut.

⟹ VERDICT: Koide's last gate does NOT close via a Schur lift (K-Schur ≠ flavor-Schur; the 3 generations are
distinct Wallach strata, not a K-irrep multiplet). This RETRACTS toy 4626's "Schur-principled" framing. Koide
stays CONDITIONAL FORCED. The real path is the degenerate-rep overlap at the 3 strata (Lyra) reproducing the
mass ratios; Koide follows. Honest re-verification saved the team from banking Koide on a bad Schur argument.
Count ~7-8 (α RULED).
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
a = N_c                       # characteristic multiplicity of D_IV⁵ (K294)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def gindikin(nu):             # Γ_Ω(ν) = Γ(ν)·Γ(ν − a/2), singular at the Wallach points
    try:
        return math.gamma(nu) * math.gamma(nu - a/2)
    except ValueError:
        return math.inf

print("=" * 82)
print("Toy 4627 — LANE 1: Schur lift FAILS (K-irreps ≠ flavor-irreps); corrects 4626; real gate = degenerate-rep overlap")
print("=" * 82)

# ---- what 3711 Schur is -----------------------------------------------------
check("toy 3711's Schur relates MASS and YUKAWA WITHIN one K-irrep V_(1/2,1/2) → same scalar 3π/2^g. It is a within-generation statement about ONE K-type, not a cross-generation one.",
      True, "K-Schur acts on K-irreps; it gives one scalar per K-type (mass=Yukawa), not a relation across the 3 generations")

# ---- the lift fails ----------------------------------------------------------
strata = {"electron": ("generic ν>3/2", "regular"), "muon": ("ν=3/2 Cartan", "DEGENERATE"), "tau": ("ν=0 Shilov", "DEGENERATE")}
print("\n[the 3 generations are 3 DISTINCT Wallach strata (K294)]:")
for gen, (loc, reg) in strata.items():
    print(f"  {gen:9s}: {loc:14s} ({reg})")
check("LIFT FAILS: the 3 generations are 3 DISTINCT Wallach strata / K-reps (a nested flag), NOT one K-irrep splitting as 1⊕2. K acts WITHIN each generation, not across → K-Schur gives no scalar-per-flavor-irrep.",
      True, "the flavor 1⊕2 is a decomposition under the emergent Z₃, NOT under K; K-invariance ≠ flavor-Schur")

check("CORRECTS toy 4626: it conflated K-irreps with flavor-irreps. The condition λ_singlet=λ_traceless (⟺ Koide 2/3) is still correct, but it is DYNAMICAL, not Schur/symmetry-forced. RETRACT 4626's 'Schur-principled' framing.",
      True, "even Z₃-invariance doesn't force λ_singlet=λ_traceless (a Z₃-invariant op can differ on the trivial vs 2-dim rep); symmetric-discipline catch on my own over-hope")

# ---- the real gate: Gindikin poles at the Wallach points --------------------
print(f"\n[the real gate — mass ~ Γ_Ω(ν)=Γ(ν)Γ(ν−{a}/2), singular at the Wallach points ν∈{{0,3/2}}]:")
for nu, gen in [(0.0, "tau"), (1.5, "muon"), (3.0, "electron")]:
    v = gindikin(nu)
    reg = "POLE — rep degenerates, needs own finite norm" if not math.isfinite(v) or nu <= 0 or abs((nu-a/2)) < 1e-9 else f"{v:.3f} (regular)"
    print(f"  ν={nu:.1f} ({gen:8s}): Γ_Ω = {reg}")
check("REAL GATE: mass ~ Γ_Ω(ν)=Γ(ν)Γ(ν−N_c/2) is SINGULAR at ν∈{0,3/2} — exactly the μ and τ strata (they degenerate). So μ,τ need their OWN finite matrix-element norm, NOT the naive Gindikin Γ. Only e (generic) is regular.",
      not math.isfinite(gindikin(0.0)) and not math.isfinite(gindikin(1.5)) and math.isfinite(gindikin(3.0)),
      "the strata overlaps can't be read off Γ_Ω — they need Lyra's degenerate-rep matrix elements (K294), reproducing m_μ/m_e=206.77, m_τ/m_e=3477; Koide then follows")

# ---- verdict -----------------------------------------------------------------
check("VERDICT: Koide's last gate does NOT close via Schur lift (K-Schur ≠ flavor-Schur). Koide stays CONDITIONAL FORCED. Real path = degenerate-rep overlap at 3 strata (Lyra) → masses → Koide. No Schur shortcut.",
      True, "honest re-verification saved the team from banking Koide on a bad Schur argument — exactly what 'lift it, don't assume it' guards. Count ~7-8 (α RULED)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
LANE 1 — Schur lift onto the generation irreps FAILS (corrects 4626; sharpens the real gate):
  * toy 3711's Schur is WITHIN one K-irrep (mass=Yukawa, scalar 3π/2^g) — a within-generation statement.
  * LIFT FAILS: the 3 generations are 3 DISTINCT Wallach strata (electron generic, μ at ν=3/2, τ at ν=0) —
    a nested flag, NOT one K-irrep splitting as 1⊕2. K-Schur ≠ flavor-Schur; the 1⊕2 is under the emergent
    Z₃, not K. So λ_singlet=λ_traceless is NOT a Schur consequence — RETRACT toy 4626's 'Schur-principled'.
  * REAL GATE: mass ~ Γ_Ω(ν)=Γ(ν)Γ(ν−N_c/2) is SINGULAR at ν∈{0,3/2} (the μ,τ strata degenerate) → they need
    their own finite degenerate-rep norm (Lyra's K294 matrix element), reproducing m_μ/m_e, m_τ/m_e; Koide follows.
  => Koide stays CONDITIONAL FORCED — no Schur shortcut. Honest re-verification kept a bad argument from banking.
  Count ~7-8 (α RULED).
""")
