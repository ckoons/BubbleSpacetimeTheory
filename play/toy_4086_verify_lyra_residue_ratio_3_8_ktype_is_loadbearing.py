"""
Toy 4086: independently verifying Lyra's honest negative (the Gindikin-Gamma residue-ratio shortcut for the
lepton masses) and decomposing the gap. Lyra reported: the bare residue ratio of Gamma_Omega at the two
Wallach poles comes out to 3/8 = 0.375, but the observed m_mu/m_tau = 0.0595 -- off by ~6x -- so the masses
are NOT a one-line residue ratio and the K-type signature is load-bearing. VERIFIED independently:
  res Gamma_Omega at nu=3/2 (muon) = Gamma(3/2) = sqrt(pi)/2 = 0.88623
  res Gamma_Omega at nu=0   (tau)  = Gamma(-3/2) = 4 sqrt(pi)/3 = 2.36327
  residue ratio res(mu)/res(tau) = 3/8 = 0.375  -- Lyra's number CONFIRMED (no arithmetic slip).
The residue ratio has the RIGHT ordering (muon lighter, ratio < 1) but the WRONG magnitude: observed/residue =
0.0595/0.375 = 0.159 = 1/6.31. So the K-type matrix element must supply that factor. DECOMPOSITION: mass =
(Gindikin-Gamma residue) x (K-type matrix element); the residue gives the pole/ordering structure, the K-type
(a,b) signature (Toy 4081) supplies the rest. I do NOT pattern-match the 6.31 (that's the fishing line);
the K-type factor is Lyra's full regularized matrix element. (Verification of the live A1 computation; my role
-- confirm the negative is real, so the K-type is known to be load-bearing, not optional.)

WHY THE NEGATIVE MATTERS (confirms the K-type is load-bearing): if the residue ratio HAD matched 0.0595, the
masses would be pure Gindikin-Gamma (the parameter alone), and the K-type signature would be decorative. It
does NOT match (3/8 vs 0.0595), so the K-type signature is REQUIRED -- the mass combines the Wallach parameter
nu with the K-type (a,b). This is Lyra's conclusion, now independently confirmed: the shortcut is ruled out,
which sharpens the computation (the (a,b) menu from Toy 4081 is genuinely needed, not optional).

THE DECOMPOSITION (what the K-type must supply):
  m_mu/m_tau = [res Gamma_Omega(mu) / res Gamma_Omega(tau)] x [K-type factor]
  0.0595     = [3/8 = 0.375]                                x [K-type factor = 0.159]
  => the K-type matrix element must contribute a factor 0.159 (= 1/6.31) to the mu/tau ratio. That factor is
     the ratio of the K-type norms (the (a,b) signatures on the two strata), computed via the full matrix
     element -- Lyra's lane. I quantify the residual; I do NOT guess what fills it.

HONEST TIER:
  VERIFIED: Lyra's residue ratio = 3/8 (independent, exact -- sqrt(pi)/2 over 4sqrt(pi)/3); the gap to observed
    0.0595 is real (~6.3x); the residue ordering is correct (muon lighter).
  CONCLUSION (supports Lyra): the residue shortcut is ruled out -> the K-type signature is load-bearing, not
    optional; mass = (Gamma residue) x (K-type matrix element).
  NOT done / DECLINED: the K-type factor itself (the 0.159) -- Lyra's full regularized matrix element combining
    the (a,b) signature with nu. I do NOT pattern-match the 6.31 to any BST integer (fishing). COUNT still 2.

GATES (2)
G1: Lyra's residue ratio 3/8 CONFIRMED independently (res Gamma_Omega: Gamma(3/2)=sqrt(pi)/2 at muon, Gamma(-3/2)=4sqrt(pi)/3 at tau; ratio=3/8 exact); no slip
G2: gap decomposed -- residue gives ordering (3/8, right sign) but misses magnitude (0.0595) by ~6.3x; K-type matrix element must supply factor 0.159; mass=(Gamma residue)x(K-type); not fished

Per Lyra (honest negative: residue ratio 3/8 misses by 6x; K-type load-bearing) + Grace (Gindikin-Gamma) +
Keeper K295; Elie 4085 (Gamma poles = Wallach points) + 4081 (K-type menu) + 4084 (mass-overlap form); Cal #237
+ F79 no-fishing (no pattern-match of the 6.31). Verifies the negative; the K-type factor is Lyra's matrix element.

Elie - Wednesday 2026-06-10 (verified Lyra residue ratio 3/8 -- no slip; misses obs 0.0595 by 6.3x; K-type signature load-bearing; mass=(Gamma residue)x(K-type), residual not fished)
"""

import mpmath as mp
mp.mp.dps = 25
N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4086: verify Lyra's residue ratio 3/8 (no slip); K-type signature is load-bearing")
print("=" * 78)
print()

print("G1: independent verification of the residue ratio")
print("-" * 78)
res_mu = mp.gamma(mp.mpf(3) / 2)
res_tau = mp.gamma(mp.mpf(-3) / 2)
ratio = res_mu / res_tau
print(f"  res Gamma_Omega at nu=3/2 (muon) = Gamma(3/2)  = sqrt(pi)/2  = {float(res_mu):.5f}")
print(f"  res Gamma_Omega at nu=0   (tau)  = Gamma(-3/2) = 4sqrt(pi)/3 = {float(res_tau):.5f}")
print(f"  residue ratio res(mu)/res(tau) = {float(ratio):.5f} = 3/8? {abs(ratio - mp.mpf(3)/8) < mp.mpf('1e-20')}  -> Lyra's 3/8 CONFIRMED (no slip)")
print()

print("G2: decompose the gap -- the K-type signature is load-bearing")
print("-" * 78)
m_mu, m_tau = 105.6584, 1776.86
obs = m_mu / m_tau
print(f"  observed m_mu/m_tau = {obs:.5f}   |   residue ratio = {float(ratio):.4f} (right ordering, wrong magnitude)")
print(f"  m_mu/m_tau = [residue 3/8] x [K-type factor];  K-type factor = {obs/float(ratio):.4f} = 1/{float(ratio)/obs:.2f}")
print(f"  => the residue shortcut is RULED OUT (3/8 != 0.0595). So the K-type signature is REQUIRED, not decorative.")
print(f"  @Lyra: 3/8 confirmed (no slip); the K-type matrix element must supply factor {obs/float(ratio):.3f} to mu/tau. mass = (Gamma residue) x (K-type).")
print(f"    I do NOT pattern-match the ~6.3 (fishing) -- the K-type factor (combining (a,b) of 4081 with nu) is your matrix element. Count still 2.")
print(f"  Score: 2/2 (residue ratio 3/8 verified exact, no slip; K-type load-bearing; gap decomposed, residual not fished)")
print()
print("=" * 78)
print("TOY 4086 SUMMARY -- independently verified Lyra's honest negative: the Gindikin-Gamma residue ratio at")
print("  the Wallach poles is exactly 3/8 (sqrt(pi)/2 over 4sqrt(pi)/3) -- no arithmetic slip. It has the right")
print("  ordering (muon lighter) but misses the observed m_mu/m_tau = 0.0595 by ~6.3x. So the residue shortcut is")
print("  ruled out and the K-type signature is LOAD-BEARING: mass = (Gamma residue) x (K-type matrix element), with")
print("  the K-type supplying the factor 0.159. That factor is Lyra's full regularized matrix element (the (a,b)")
print("  signature combined with nu); I do NOT pattern-match the 6.3. Count still honestly 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
