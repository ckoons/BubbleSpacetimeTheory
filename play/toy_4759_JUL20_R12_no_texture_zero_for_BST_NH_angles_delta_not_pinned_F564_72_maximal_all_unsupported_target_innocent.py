#!/usr/bin/env python3
"""
Toy 4759 — Jul 20 (Round-12: build M_ν, read off δ target-innocently — Elie's half): the round's route is "m₁=0 (rank-2)
+ a TEXTURE ZERO (a vanishing entry of M_ν) predicts δ." My job: given the texture, compute δ target-innocently and see
which value (F564's ~17°, my ~72°, or the data hint −90°) BST's structure gives — NOT fitting to −π/2. I tested the route
directly with BST's banked inputs, and the honest, target-innocent result is a NEGATIVE that resolves the whole dispute:
BST's angles + NH masses admit NO single texture zero at all, so δ is NOT pinned by a texture zero — and F564's 17°, my
72°, and maximal −90° are ALL unsupported by this route (there's no zero to force any of them).

THE ROUTE (target-innocent test): M_ν = U*·diag(0, m₂e^{iφ}, m₃)·U† (Majorana, m₁=0). A texture zero (M_ν)_ab = 0 means
m₃·U*_a3 U*_b3 (call it A) + m₂e^{iφ}·U*_a2 U*_b2 (call it B) = 0, achievable iff |A(δ)| = |B(δ)| for some δ (then φ
cancels). I scanned all 6 entries over δ with the banked angles sin²θ₂₃=4/7, sin²θ₁₂=3/10, sin²θ₁₃=1/45 and NH masses
(m₁=0, m₂=√Δm²₂₁, m₃=√Δm²₃₁), target-innocently (never looking at −90°).
THE RESULT — NO TEXTURE ZERO IS ACHIEVABLE: for EVERY entry, |A(δ)| ≠ |B(δ)| for all δ (min gaps 0.0014–0.025 eV). The
m₂-term and m₃-term magnitudes never balance, because NH m₁=0 gives m₂/m₃ ≈ 0.17, too small for the U-element ratios to
match. So there is NO vanishing entry of M_ν → the "texture zero fixes δ" mechanism does NOT fire for BST.
IT'S AN NH-m₁=0 FEATURE (robustness, not a code artifact): the sanity check confirms even GENERIC angles (θ₂₃=45°,
standard θ₁₃) admit NO direct texture zero for NH m₁=0 — only IH-ish (both masses heavy) admits one (ττ). So the negative
is the NH-m₁=0 structure, verified, not special pleading and not a bug (the code finds the IH-ish zero).
THE CONSEQUENCE (resolves F564 vs 72° vs maximal): since there is NO texture zero, NONE of {F564 sinδ=2/7 → ~17°; my
μ-τ-break-min → ~72°; maximal → −90°} is FORCED by a texture zero. The mechanism the round is built on does not pin δ for
BST's NH structure. The simplest alternative also looks blocked: the m₁=0 null-eigenvector (U's first column) has NO
vanishing component (|U_e1|,|U_μ1|,|U_τ1| all > 0 for every δ), so the associated cofactor zeros don't occur either — but
the full cofactor/seesaw-texture analysis is Lyra's to build.

⟹ VERDICT (target-innocent, disciplined negative): BST's banked angles + NH m₁=0 admit NO single texture zero (verified
all 6 entries; robustness-checked as an NH-m₁=0 feature), so δ_PMNS is NOT pinned by a texture zero — and F564's 17°, my
72°, and maximal −90° are ALL unsupported by this route. The disciplined outcome: bank NO δ prediction; the real wins
(CP small = rank-1; CKM ≪ PMNS) stand clean and uncontaminated. IF BST's edge-mode/dead-cell structure imposes a
DIFFERENT constraint (a cofactor zero, a non-flavor-basis condition, or a specific m₂/m₃), Lyra specifies it and I compute
δ from that — then DUNE tests the derived δ. Until then, δ is honestly UNPREDICTED. This is the 127/128 discipline applied:
no fit to the −90° hint. Count ~7-8 (α RULED). Five-Absence-safe (CP within SM).
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# BST banked angles + NH masses (m1=0)
sin2 = dict(t12=3/10, t13=1/45, t23=4/7)
s12, s13, s23 = np.sqrt(sin2['t12']), np.sqrt(sin2['t13']), np.sqrt(sin2['t23'])
c12, c13, c23 = np.sqrt(1-sin2['t12']), np.sqrt(1-sin2['t13']), np.sqrt(1-sin2['t23'])
m2, m3 = np.sqrt(7.42e-5), np.sqrt(2.51e-3)   # eV

def U(d):
    return np.array([
     [c12*c13, s12*c13, s13*np.exp(-1j*d)],
     [-s12*c23-c12*s23*s13*np.exp(1j*d), c12*c23-s12*s23*s13*np.exp(1j*d), s23*c13],
     [ s12*s23-c12*c23*s13*np.exp(1j*d), -c12*s23-s12*c23*s13*np.exp(1j*d), c23*c13]])
labels = [(0,0,'ee'),(0,1,'eμ'),(0,2,'eτ'),(1,1,'μμ'),(1,2,'μτ'),(2,2,'ττ')]
ds = np.linspace(0, 2*np.pi, 8001)

# ---- the route: no texture zero achievable ----------------------------------
achievable, mingaps = [], {}
for a, b, name in labels:
    gp = np.array([m3*abs(U(d)[a,2]*U(d)[b,2]) - m2*abs(U(d)[a,1]*U(d)[b,1]) for d in ds])
    mingaps[name] = float(np.min(np.abs(gp)))
    if np.any(gp[:-1]*gp[1:] < 0): achievable.append(name)
print(f"\n[texture-zero scan, BST NH]: achievable positions = {achievable if achievable else 'NONE'}; min gaps (eV) = "
      + ", ".join(f'{k}:{v:.4f}' for k,v in mingaps.items()))
check("NO TEXTURE ZERO IS ACHIEVABLE (target-innocent): for EVERY entry of M_ν = U*·diag(0,m₂e^{iφ},m₃)·U†, |A(δ)| ≠ "
      "|B(δ)| for all δ (min gaps 0.0014–0.025 eV) — the m₂-term and m₃-term magnitudes never balance (NH m₁=0 gives "
      "m₂/m₃ ≈ 0.17, too small for the U-element ratios). So there is NO vanishing entry → the 'texture zero fixes δ' "
      "mechanism does NOT fire for BST's banked angles + NH masses.",
      len(achievable) == 0, "no texture zero achievable for any entry (|A|≠|B| ∀δ) → the texture-zero→δ route does not fire for BST NH")

# ---- robustness: it's an NH-m1=0 feature ------------------------------------
def any_zero(s2_12, s2_13, s2_23, mm2, mm3):
    a12,a13,a23 = np.sqrt(s2_12),np.sqrt(s2_13),np.sqrt(s2_23); b12,b13,b23 = np.sqrt(1-s2_12),np.sqrt(1-s2_13),np.sqrt(1-s2_23)
    def Uu(d): return np.array([
     [a12*b13, a12*0+ s12*0 + np.sqrt(s2_12)*b13, a13*np.exp(-1j*d)]]) if False else np.array([
     [b12*b13, a12*b13, a13*np.exp(-1j*d)],
     [-a12*b23-b12*a23*a13*np.exp(1j*d), b12*b23-a12*a23*a13*np.exp(1j*d), a23*b13],
     [ a12*a23-b12*b23*a13*np.exp(1j*d), -b12*a23-a12*b23*a13*np.exp(1j*d), b23*b13]])
    for a,b,_ in labels:
        gp=np.array([mm3*abs(Uu(d)[a,2]*Uu(d)[b,2])-mm2*abs(Uu(d)[a,1]*Uu(d)[b,1]) for d in ds])
        if np.any(gp[:-1]*gp[1:]<0): return True
    return False
nh_generic = any_zero(0.31, 0.022, 0.5, m2, m3)
ih_ish = any_zero(0.3, 1/45, 4/7, np.sqrt(2.51e-3), np.sqrt(2.51e-3+7.42e-5))
print(f"[robustness]: generic-angles NH admits a zero? {nh_generic}; IH-ish (both heavy) admits a zero? {ih_ish}")
check("ROBUSTNESS — it's an NH-m₁=0 FEATURE (not a code artifact): even GENERIC angles (θ₂₃=45°, standard θ₁₃) admit NO "
      "direct texture zero for NH m₁=0; only IH-ish (both masses heavy) admits one (ττ) — which the code DOES find. So the "
      "negative is the real NH-m₁=0 structure (m₂≪m₃), verified, not special pleading and not a bug.",
      (not nh_generic) and ih_ish, "generic NH also admits no texture zero; IH-ish admits ττ (code finds it) → the negative is a verified NH-m₁=0 feature")

# ---- consequence: 17/72/maximal all unsupported -----------------------------
# quick check: does the m1=0 null-eigenvector (U col 1) have any vanishing component?
nullvec_min = min(min(abs(U(d)[k,0]) for d in np.linspace(0,2*np.pi,361)) for k in range(3))
print(f"[cofactor quick-check]: min |U_a1| over δ (the m₁=0 null-eigenvector) = {nullvec_min:.3f} > 0 → no vanishing component")
check("CONSEQUENCE — F564 (17°), my 72°, and maximal (−90°) are ALL unsupported: since there is NO texture zero, none of "
      "them is FORCED by one. The simplest alternative also looks blocked — the m₁=0 null-eigenvector (U's first column) "
      "has NO vanishing component (min |U_a1| > 0 ∀δ), so the associated cofactor zeros don't occur either — but the full "
      "cofactor/seesaw-texture analysis is Lyra's to build. δ is NOT pinned by a simple texture zero.",
      nullvec_min > 0.05, "no texture zero → 17°/72°/−90° all unforced by it; null-eigenvector has no vanishing component (cofactor route also looks blocked) — δ unpinned")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (target-innocent, disciplined NEGATIVE): BST's banked angles + NH m₁=0 admit NO single texture zero "
      "(verified all 6 entries; robustness-checked as an NH-m₁=0 feature), so δ_PMNS is NOT pinned by a texture zero — and "
      "F564's 17°, my 72°, and maximal −90° are ALL unsupported by this route. Bank NO δ prediction; the real wins (CP "
      "small = rank-1; CKM ≪ PMNS) stand clean. IF BST's edge-mode/dead-cell imposes a DIFFERENT constraint (a cofactor "
      "zero, a non-flavor-basis condition, a specific m₂/m₃), Lyra specifies it and I compute δ — then DUNE tests the "
      "derived δ. Until then δ is honestly UNPREDICTED. The 127/128 discipline: no fit to the −90° hint.",
      len(achievable) == 0 and (not nh_generic) and ih_ish,
      "no texture zero for BST NH → δ unpinned; 17°/72°/maximal all unsupported; bank no δ; wins stay clean; awaits Lyra's actual M_ν constraint")

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
ROUND-12 build M_ν / read off δ — Elie's target-innocent test (a disciplined NEGATIVE):
  * NO texture zero achievable: BST's angles + NH m₁=0 give |A(δ)|≠|B(δ)| for all 6 entries, all δ (m₂/m₃≈0.17 too small to balance). The route doesn't fire.
  * ROBUSTNESS: generic NH also admits no texture zero; IH-ish admits ττ (code finds it) → a verified NH-m₁=0 feature, not a bug.
  * CONSEQUENCE: F564 (17°), my 72°, maximal (−90°) ALL unsupported (no zero to force them); the null-eigenvector has no vanishing component (cofactor route also looks blocked).
  => δ_PMNS is NOT pinned by a texture zero → bank NO δ prediction; CP-small=rank-1 & CKM≪PMNS stay clean; awaits Lyra's actual edge-mode constraint. No fit to −90°.
""")
