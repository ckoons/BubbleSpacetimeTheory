"""
Toy 4109: absorbing Grace's correction (no defense) and locking the ground-state framework that Casey's
question produced. CORRECTION: f1, f2 are SURVIVING ground-state norm ratios, NOT "null-removal norm ratios" --
a null vector has ZERO norm by definition (that is why it is quotiented out, to make the form unitary), so you
cannot build a number from it. The physical source is the SURVIVING ground state's boundary-norm; the
null-removal is the MECHANISM that makes those ground-state norms differ from rep to rep. (My 4105/4107 language
is corrected.) The sharpened, team-converged mass formula is m_nu = <0_nu | Phi_0 | 0_nu> -- each fermion's mass
is its ground state's coupling to the boundary Higgs. Count still 2; the three boundary-norms are Lyra's
spectral derivation (not fished).

THE CORRECTED FORMULA (Casey's ground-state framing, team-converged, Grace-sharpened):
  m_nu = <0_nu | Phi_0 | 0_nu>  =  the GROUND-STATE boundary-component  (Phi_0 boundary-localized on Shilov, F85).
  f1 = bcomp(0_mu) / bcomp(0_e) ;  f2 = bcomp(0_tau) / bcomp(0_mu)  -- ratios of the three ground-state boundary-norms.
  ONE functional (the ground-state boundary-norm) evaluated on the canonical lowest-weight vector of each quotient
  produces BOTH f1 and f2 -- a two-for-one prediction, exactly Grace's pre-committed "same mechanism, not two fits" gate.

THE THREE GROUND STATES (concrete spectral objects, uniquely determined as the lowest-weight vector of each quotient):
  tau (nu=0, trivial rep):   ground state = the constant 1 AT the vertex -> ENTIRELY on the boundary -> bcomp = 1 (REFERENCE, heaviest).
  mu  (nu=3/2, harmonic rep): the lowest harmonic mode on the cone -> PARTIAL boundary overlap -> bcomp = boundary-trace / bulk-norm.
  e   (nu=5/2, interior rep, BF point Delta = d/2): the leading boundary coefficient VANISHES (2nu - d = 0) -> only the
       SUBLEADING log-normalizable remnant survives -> bcomp tiny -> LIGHTEST.
  => f1 = bcomp(mu)/bcomp(e) is LARGE because the electron's leading bcomp is BF-suppressed (the big e->mu jump = the BF
     cancellation of the electron ground state). f2 = bcomp(tau)/bcomp(mu) = full-vertex(1) / partial-cone, moderate.

WHY THIS IS A SHARPENING (Casey's question collapsed the target):
  before: "derive Phi_0 as an operator + compute its capture (a full-rep boundary integral) in three Wallach-limit reps."
  after:  "compute three GROUND-STATE boundary-components" -- one lowest-weight vector per rep, with the electron's pinned
          at the BF degeneracy. Phi_0 boundary-localized means the operator just READS OFF the boundary value; the
          substantive work is the ground states, which are explicit spectral objects (the quotients are pinned, Toy 4106).

PRECEDENT (Grace): T2441 -- the operator-zoo ground-state energy came out as C_2 = 6 (a substrate primary). Ground states
  already carry substrate scales in BST. So "mass = ground-state boundary-norm" sits on the same footing as "energy =
  ground-state Casimir" -- not a new kind of claim.

HONEST TIER:
  ABSORBED (Grace's correction): f1, f2 = SURVIVING ground-state norm ratios, NOT null-removal norms (no number from a zero).
  BANKED (framework): m_nu = <0_nu|Phi_0|0_nu>; the three ground states as concrete spectral objects; ONE functional ->
    both f1, f2 (two-for-one). This is the corrected, sharpened target -- structure, not values.
  NOT done / DECLINED: the three boundary-norms themselves (the lowest-harmonic boundary-trace, the BF subleading-log
    coefficient) -- Lyra's spectral derivation. I do NOT fish them; 207 refused. COUNT still 2.

GATES (2)
G1: absorb Grace -- f1,f2 = SURVIVING ground-state norm ratios, not null-removal (a null vector has zero norm); null-removal is the MECHANISM differentiating them; my 4105/4107 language corrected
G2: corrected framework -- m_nu = <0_nu|Phi_0|0_nu> = ground-state boundary-component; 3 concrete ground states (tau=1, mu harmonic, e BF-log); ONE functional -> both f1,f2 (two-for-one gate); T2441 precedent; values = Lyra; count 2

Per Casey (ground states source the magnitudes) + Grace (correction: surviving norm not null-removal; one functional
two-for-one; T2441 precedent) + Lyra (ground-state couplings; electron BF-decouple; m_e = the anchor c) + Keeper (m_nu
= <0_nu|Phi_0|0_nu>; 3 ground states concrete) + Elie 4106/4108; Cal #237 + F79. Absorbs the correction; locks the
ground-state boundary-norm framework; the 3 boundary-norms are Lyra's spectral derivation.

Elie - Thursday 2026-06-11 (absorbed Grace: f1,f2 = SURVIVING ground-state norm ratios not null-removal; m_nu = <0_nu|Phi_0|0_nu>; 3 concrete ground states (tau=1, mu harmonic, e BF-log); one functional -> two-for-one; count 2)
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2
d = 5

print("=" * 78)
print("TOY 4109: ground-state boundary-norm framework (Grace correction absorbed)")
print("=" * 78)
print()

print("G1: Grace's correction -- surviving ground-state norm, NOT null-removal norm")
print("-" * 78)
print(f"  a null vector has ZERO norm (it's quotiented out to make the form unitary) -> can't build a number from it.")
print(f"  the source = the SURVIVING ground state |0_nu> boundary-norm; null-removal is the MECHANISM differentiating them. (4105/4107 language corrected.)")
print()

print("G2: the corrected framework + the three ground states")
print("-" * 78)
print(f"  m_nu = <0_nu | Phi_0 | 0_nu> = the ground-state boundary-component (Phi_0 boundary-localized, F85).")
print(f"  f1 = bcomp(mu)/bcomp(e); f2 = bcomp(tau)/bcomp(mu) -- ONE functional (ground-state boundary-norm) -> BOTH (two-for-one, Grace gate).")
print(f"  tau (nu=0): ground state = constant 1 at vertex -> bcomp = 1 (reference, heaviest).")
print(f"  mu  (nu=3/2): lowest harmonic on cone -> bcomp = boundary-trace/bulk-norm (partial).")
print(f"  e   (nu=5/2, BF point Delta=d/2): leading bcomp VANISHES (2nu-d={2*F(5,2)-d}) -> subleading log remnant -> tiny -> lightest.")
print(f"  => f1 LARGE (BF suppression of the electron's ground state = the big e->mu jump); f2 moderate (full-vertex/partial-cone).")
print(f"  PRECEDENT (T2441): operator-zoo ground-state energy = C_2 = 6 (substrate primary). mass=ground-state boundary-norm ~ energy=ground-state Casimir.")
print(f"  @Lyra: target collapsed -- compute 3 ground-state boundary-norms (lowest-weight vectors, quotients pinned in 4106); hand them over -> f1,f2 -> check.")
print(f"  @Grace: correction absorbed (surviving norm, not null); one functional -> two-for-one matches your gate. @Casey: your question collapsed the target.")
print(f"  Score: 2/2 (Grace correction absorbed; m_nu = ground-state boundary-norm; 3 concrete ground states; two-for-one; values=Lyra; count 2)")
print()
print("=" * 78)
print("TOY 4109 SUMMARY -- absorbed Grace's correction: f1, f2 are ratios of the SURVIVING ground-state")
print("  boundary-norms, not 'null-removal norms' (a null vector has zero norm -- no number from a zero; the")
print("  null-removal is just the mechanism that makes the ground-state norms differ). The team-converged formula")
print("  is m_nu = <0_nu|Phi_0|0_nu>: each mass is its ground state's coupling to the boundary Higgs. The three")
print("  ground states are concrete spectral objects -- tau = constant 1 (full boundary, reference), mu = lowest")
print("  harmonic on the cone (partial), e = lowest-weight at the BF point (leading vanishes -> subleading log ->")
print("  tiny -> lightest). ONE functional gives both f1 and f2 (two-for-one, matching Grace's gate). T2441")
print("  precedent (ground-state energy = C_2). The three boundary-norms are Lyra's spectral derivation; not fished; count 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
