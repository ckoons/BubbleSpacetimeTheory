#!/usr/bin/env python3
"""
Toy 5102: CFS object-match -- the three-way tie verified; (3,0) is the accidental non-Weyl
member that makes the triple stringent; structural spacelike shown; the DISCRIMINATING numerical
test named. (K1248; Lyra's point->mode map, Grace's E=30 discriminator.)
E / Elie -- the live gate. I fire what the delivered data supports and name exactly what the
deciding number needs, WITHOUT fabricating a pass I can't faithfully compute.

DELIVERABLES IN HAND (Lyra ~12:20 + Grace):
  * The three-way simultaneity: modes (1,3), (2,2), (3,0), all at Casimir C(a,b)=a(a+5)+b(b+3)=24
    (= conformal rho=(5/2,3/2)), H_B energy 30 = 24 + C_2. Grace's E=30 discriminator = Lyra's
    F843 commit-tie -- same object (verified).
  * Map: mode (a,b) -> highest-weight coherent state e_{(a,b)} in H^2(D_IV^5) -> F_{(a,b)} =
    -<psi|psi> under the indefinite (2,2) spin product (an indefinite 4x4 operator).
  * The test (Lyra): build F for the three modes; are all THREE PAIRS mutually SPACELIKE
    (Finster: equal-magnitude eigenvalues)? "A pairwise mechanism that misses the triple is the
    wrong operator."

WHAT I FIND:
  * TIE VERIFIED: all three at Casimir 24 (conformal rho); on the equal-energy circle |lam+rho|^2
    = 32.5. Grace = Lyra, confirmed.
  * WHY THE TRIPLE IS STRINGENT (the sharp part): {(1,3),(2,2)} are WEYL-SWAP-related (same
    coordinate multiset {3.5,4.5} in shifted e-coords), but (3,0) has multiset {1.5,5.5} -- it is
    an ACCIDENTAL degeneracy, NOT Weyl-related. So a Weyl-symmetric operator makes the PAIR
    spacelike for free but can MISS (3,0). The triple tests the accidental (3,0) -- strictly
    stronger than any pair (this is exactly Lyra's "misses the triple = wrong operator").
  * STRUCTURAL object-match: the three modes are three points on the equal-COMMIT-ENERGY circle (a
    simultaneity slice). In a causal structure whose time function IS the commit-energy (which the
    homogeneous CFS construction F(x)=g_x F(o) g_x* with H_B as the commit clock provides, per
    Lyra's map spacelike <=> equal commit-energy), three equal-energy points are mutually SPACELIKE.
    So a three-way tie -> three-way spacelike, structurally + target-innocent (the circle is the
    equal-Casimir shell, not reverse-engineered).

WHAT I DO NOT FABRICATE (the deciding number): whether Lyra's SPECIFIC F_{(a,b)} (built from the
coherent states) INDEPENDENTLY renders the accidental (3,0) mutually spacelike -- i.e. whether her
operator's causal-time really IS the commit-energy including on the non-Weyl member -- requires the
explicit (2,2) spinor matrices per mode (or the coherent-state group elements g_{(a,b)}). The
prescription is concrete; the explicit spinor data is the remaining input. A transparent demo
(below) that ENCODES energy=time confirms consistency but is NOT the discriminating test.

=> VERDICT (plain): the three-way tie is VERIFIED, and the sharp content is exposed -- (3,0) is an
accidental non-Weyl degeneracy, so the triple genuinely discriminates the operator. The STRUCTURAL
object-match (equal-energy circle -> mutually spacelike if causal-time = commit-energy) holds and is
target-innocent. The DECIDING numerical test -- does Lyra's explicit F make the non-Weyl (3,0)
spacelike to the pair? -- needs the explicit (2,2) spinor matrices, which I request precisely rather
than model. Gate advanced from "form-match" to "structural object-match + stringency exposed"; the
"is a CFS" number awaits the spinors. NOT banked.

=> DISPOSITION: fires the verifiable part (tie + Weyl analysis + structural), names the deciding
input (explicit F_{(a,b)}), refuses to fabricate the pass. Firer=Lyra(construction), checker=Elie.
Nothing banked. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

modes = [(1, 3), (2, 2), (3, 0)]
rho = np.array([2.5, 1.5])   # conformal rho = (n_C, N_c)/rank = (5/2, 3/2)
C_2 = 6

print("=" * 78)
print("Toy 5102: CFS object-match -- three-way tie verified, (3,0) accidental (K1248)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. VERIFY the tie.
# ----------------------------------------------------------------------------
print("\n--- verify the three-way tie: all at Casimir 24 (conformal rho) ---")
def casimir(a, b): return a*(a+5) + b*(b+3)
def cas_rho(a, b):
    lam = np.array([a, b]); return float((lam+rho) @ (lam+rho) - rho @ rho)
cass = [casimir(a, b) for a, b in modes]
energy = cass[0] + C_2
check("the three modes (1,3),(2,2),(3,0) are all at Casimir C(a,b)=a(a+5)+b(b+3)=24 (= conformal "
      "rho=(5/2,3/2)); H_B energy = 24 + C_2 = 30. Grace's E=30 discriminator = Lyra's F843 commit-tie",
      len(set(cass)) == 1 and cass[0] == 24 and all(abs(cas_rho(a, b) - 24) < 1e-9 for a, b in modes)
      and energy == 30,
      f"Casimirs = {cass} (all 24); |lam+rho|^2 = 32.5 (equal-energy circle); H_B energy = {energy}. "
      "Grace = Lyra, same object -- verified.")

# ----------------------------------------------------------------------------
# 2. WHY the triple is stringent: (3,0) is accidental (non-Weyl).
# ----------------------------------------------------------------------------
print("\n--- (3,0) is an ACCIDENTAL non-Weyl degeneracy -> the triple is strictly stronger ---")
def multiset(a, b): return tuple(sorted((abs(a+2.5), abs(b+1.5))))   # shifted e-coords, |.| for sign flips
ms = {m: multiset(*m) for m in modes}
pair_weyl = np.allclose(ms[(1, 3)], ms[(2, 2)])
accidental_30 = not np.allclose(ms[(3, 0)], ms[(1, 3)])
check("{(1,3),(2,2)} are WEYL-SWAP-related (same coordinate multiset {3.5,4.5} in shifted e-coords), "
      "but (3,0) has multiset {1.5,5.5} -- an ACCIDENTAL degeneracy, NOT Weyl-related. So a Weyl-"
      "symmetric operator makes the PAIR spacelike for free but can MISS (3,0). The triple tests the "
      "accidental member -> strictly stronger than any pair (Lyra: 'misses the triple = wrong operator')",
      pair_weyl and accidental_30,
      f"multisets: (1,3)->{ms[(1,3)]}, (2,2)->{ms[(2,2)]} (Weyl-swap); (3,0)->{ms[(3,0)]} (accidental). "
      "The (3,0) is the sharp discriminator -- symmetry alone does not deliver it.")

# ----------------------------------------------------------------------------
# 3. STRUCTURAL object-match: equal-energy circle -> mutually spacelike if causal-time = commit-energy.
# ----------------------------------------------------------------------------
print("\n--- structural object-match: equal-energy circle -> simultaneity -> spacelike ---")
radii2 = [float((np.array(m)+rho) @ (np.array(m)+rho)) for m in modes]
on_circle = len(set(round(r, 6) for r in radii2)) == 1
check("STRUCTURAL: the three modes are three points on the equal-COMMIT-ENERGY circle (|lam+rho|^2 = "
      "32.5, a simultaneity slice). In a causal structure whose TIME FUNCTION is the commit-energy "
      "(the homogeneous CFS construction provides this: F(x)=g_x F(o) g_x*, H_B = commit clock, Lyra's "
      "map spacelike<=>equal-energy), three equal-energy points are mutually SPACELIKE. Target-innocent",
      on_circle,
      f"all three on |lam+rho|^2 = {radii2[0]:.1f} (equal-energy circle). Equal energy = simultaneous = "
      "spacelike IF causal-time = commit-energy. The circle is the equal-Casimir shell, not reverse-engineered.")

# ----------------------------------------------------------------------------
# 4. TRANSPARENT consistency demo (flagged: encodes energy=time; NOT the discriminating test).
# ----------------------------------------------------------------------------
print("\n--- consistency demo (transparent; encodes energy=time; NOT the deciding test) ---")
# map each mode to an equal-time 4-vector (time = common energy) + spatial angle on the circle;
# build F via the validated Dirac-slash (5089) and check all pairs spacelike.
I2 = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]], dtype=complex); sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex); Z2 = np.zeros((2,2), dtype=complex)
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
g0 = blk(I2,Z2,Z2,-I2); g1 = blk(Z2,sx,-sx,Z2); g2 = blk(Z2,sy,-sy,Z2); g3 = blk(Z2,sz,-sz,Z2)
I4 = np.eye(4, dtype=complex)
def slash(v): return v[0]*g0+v[1]*g1+v[2]*g2+v[3]*g3
def sep_is_spacelike(delta, alpha, beta, tol=1e-6):
    # causal type of the SEPARATION delta = y - x (5089): A = P(x,y)P(y,x)
    S = slash(delta)
    A = (alpha*S + beta*I4) @ (np.conjugate(alpha)*S + np.conjugate(beta)*I4)
    lam = np.linalg.eigvals(A); lam = lam[np.abs(lam) > tol]
    eqmod = (np.abs(lam).max()-np.abs(lam).min()) < 1e-4*(1+np.abs(lam).max())
    return eqmod and np.any(np.abs(lam.imag) > tol)
# equal time T; spatial positions from the angle of (a+5/2, b+3/2) on the circle
T = 5.0
pts = []
for (a, b) in modes:
    ang = np.arctan2(b+1.5, a+2.5)
    pts.append(np.array([T, 2*np.cos(ang), 2*np.sin(ang), 0.0]))
alpha, beta = 1.0+0.3j, 0.7-0.2j
# causal type of each PAIR depends on the SEPARATION delta = pts[j]-pts[i] (equal time -> dt=0 -> spacelike)
pairs_spacelike = sum(sep_is_spacelike(pts[j]-pts[i], alpha, beta)
                      for i in range(3) for j in range(3) if i < j)
check("CONSISTENCY DEMO (transparent, flagged): mapping the three modes to EQUAL-TIME 4-vectors "
      "(time = common energy) + spatial angle, the Dirac-slash (2,2) F's make all 3 pairs SPACELIKE. "
      "This CONFIRMS the structural expectation but ENCODES energy=time -- it is NOT the discriminating "
      "test of Lyra's specific operator (which must yield energy=time independently, incl. on (3,0))",
      pairs_spacelike == 3,
      f"{pairs_spacelike}/3 pairs spacelike in the equal-time demo. Consistency only: I put energy=time in, "
      "so spacelike comes out. The real test is whether Lyra's F(o)+coherent-states DERIVE energy=time.")

# ----------------------------------------------------------------------------
# 5. The deciding input + verdict.
# ----------------------------------------------------------------------------
print("\n--- the deciding numerical test needs the explicit spinors; verdict ---")
check("VERDICT: tie VERIFIED + (3,0)-accidental stringency EXPOSED + structural object-match "
      "(target-innocent) shown. The DECIDING numerical test -- does Lyra's explicit F_{(a,b)} (from the "
      "coherent states) render the ACCIDENTAL non-Weyl (3,0) mutually spacelike with the pair? -- needs "
      "the explicit (2,2) spinor matrices per mode (or the g_{(a,b)}). Requested, NOT fabricated",
      True,
      "gate advanced: form-match -> structural object-match + stringency. The 'is a CFS' number awaits "
      "the explicit spinors -- especially to check the non-Weyl (3,0), which symmetry alone won't deliver. "
      "Firer=Lyra(construction), checker=Elie. NOT banked.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5102, K1248 -- CFS object-match: three-way tie, (3,0) accidental, structural):
  * TIE VERIFIED: (1,3),(2,2),(3,0) all at Casimir 24 (conformal rho=(5/2,3/2)); equal-energy circle
    |lam+rho|^2 = 32.5; H_B energy 30 = 24 + C_2. Grace's E=30 = Lyra's F843 tie -- same object.
  * (3,0) IS ACCIDENTAL: {{(1,3),(2,2)}} are Weyl-swap-related (multiset {{3.5,4.5}}); (3,0) has
    {{1.5,5.5}} -- NOT Weyl-related. So the triple is strictly stronger than any pair; a Weyl-
    symmetric operator can make the pair spacelike but MISS (3,0). Exactly Lyra's "misses the triple
    = wrong operator", now with the mechanism.
  * STRUCTURAL object-match: three points on the equal-commit-energy circle -> simultaneity slice ->
    mutually spacelike IF causal-time = commit-energy (which the homogeneous CFS construction provides).
    Target-innocent (the equal-Casimir shell).
  * CONSISTENCY DEMO (flagged, not the deciding test): equal-time mapping -> all 3 pairs spacelike; but
    it ENCODES energy=time, so it only confirms consistency.
  * DECIDING NUMERICAL TEST (the "is a CFS" number): does Lyra's explicit F_{{(a,b)}} render the
    accidental non-Weyl (3,0) mutually spacelike? -> needs the explicit (2,2) spinor matrices per mode.
    Requested precisely; NOT fabricated.

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked. Verified the tie + exposed the (3,0) stringency +
structural object-match; refused to fabricate the deciding number. Firer=Lyra, checker=Elie. Count N.
""")
