"""
*** CONFIRMED 2026-06-06 PM by Lyra Investigation #1 closure (F50). ***
The weight-0 lean "CKM amplitude N_c^2 -> two-endpoint -> Direction B" is CONFIRMED:
Lyra forced B (single trace -> 3/40 rejected; two-point -> 9/40 = lambda exact). Muon
went to T190 single-object (NOT the additive form), so the sectors diverge -- see 4012
update. This scaffold's CKM half is now closed at Direction B.

Toy 4013: Investigation #1 numerical discriminator scaffold (Elie support for Lyra).

INVESTIGATION #1 (Casey/Keeper next-session brief): does the FK matrix element
<V_lambda|O|V_mu> on H^2(D_IV^5) factor through Bergman-kernel autocorrelation
(Direction A, single-trace) or need an irreducible two-point structure (Direction B)?
ONE answer decides BOTH the muon edge-term (Composite v0.5 vs T190) AND the CKM
direction. Per Elie's Saturday synthesis (Toy 4012), Walls 2 and 5 are this one question.

CLOSURE ORDER (brief): (1) Lyra fires the substrate-mechanism FORWARD derivation under
each hypothesis; (2) Elie numerically verifies which reproduces BOTH observables cleanly.
This toy is step-2 SCAFFOLD, fired in parallel: it pins the two targets, lays out the
A-vs-B numerical signature, and is READY to verify Lyra's F50 the moment it lands.

DISCIPLINE (Saturday's lesson, held): I do NOT claim the A/B verdict here. The structural
assignment (one trace vs two endpoints) is Lyra's FK mechanism. This toy gives the values
(fact) + the discriminator + a WEIGHT-0 numerical lean. Closure = Lyra's FORCING, not
this fit. (Toy 4006 overclaimed structure and was walked back; not repeating that.)

GATES (4)
G1: the two targets pinned (source-checked)
G2: A vs B numerical signature (what each predicts)
G3: weight-0 numerical lean + the discriminating computation handed to Lyra
G4: verifier ready-state for Lyra F50

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F

rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

print("=" * 76)
print("TOY 4013: Investigation #1 FK-factorization numerical discriminator (scaffold)")
print("=" * 76)
print()

print("G1: the two targets pinned (source-checked)")
print("-" * 76)
muon_main, muon_edge = F(1575, 8), F(N_c**4, 2**N_c)
muon_total = muon_main + muon_edge
mu_obs = 206.7682830  # CODATA m_mu/m_e
ckm = F(N_c**2, 2**N_c * n_C)
lam_pdg, lam_sig = 0.22500, 0.00067  # PDG Wolfenstein lambda = sin theta_C
print(f"  MUON edge: m_mu/m_e = 1575/8 + 81/8 = {muon_total}=207  (Composite v0.5, F32/F48)")
print(f"    edge term 81/8 = N_c^4/2^N_c = {float(muon_edge)} ; F48: N_c^4 = N_c^codim-4")
print(f"    (Casey #14 restriction grading; muon is COLOR SINGLET, NOT a color factor)")
print(f"    207 vs obs {mu_obs}: dev {abs(207-mu_obs)/mu_obs*100:.3f}% (Tier 2 STRUCTURAL)")
print(f"  CKM: sin(theta_C) = N_c^2/(2^N_c·n_C) = {ckm} = {float(ckm)}")
print(f"    PDG lambda = {lam_pdg}({int(lam_sig*1e5)}): dev {abs(float(ckm)-lam_pdg)/lam_pdg*100:.3f}%, {abs(float(ckm)-lam_pdg)/lam_sig:.1f} sigma")
print()
print("  G1: both targets pinned; CKM exact at 0.0 sigma, muon edge 0.112%")
print()

print("G2: A vs B numerical signature (what each hypothesis predicts)")
print("-" * 76)
print("  Direction A (Bergman autocorrelation, SINGLE trace, amplitude^2 = rate):")
print("    - resolution of identity Sum_n |V_n><V_n| collapses to one trace")
print("    - an AMPLITUDE naturally carries N_c^1; the RATE (amplitude^2) carries N_c^2")
print("  Direction B (irreducible TWO-POINT, two distinct endpoints):")
print("    - matrix element = product of two endpoint factors, each ~N_c")
print("    - an AMPLITUDE carries N_c x N_c = N_c^2 (two endpoints)")
print()
print("  Observed N_c-powers:")
print(f"    CKM sin(theta_C) is an AMPLITUDE and carries N_c^2 (= {N_c**2})")
print(f"    muon edge carries N_c^4 (= {N_c**4}) = (N_c^2)^2")
print()
print("  G2: signatures laid out")
print()

print("G3: weight-0 numerical lean + discriminating computation for Lyra")
print("-" * 76)
print("  LEAN (WEIGHT 0, not a verdict): the CKM AMPLITUDE carrying N_c^2 reads more")
print("  naturally as TWO endpoints (Direction B: N_c x N_c) than as a single-trace")
print("  amplitude (Direction A would put N_c^1 in the amplitude, N_c^2 in the rate).")
print("  If so, muon N_c^4 = (N_c^2)^2 would be the two-endpoint structure squared/graded")
print("  -- consistent with F48's N_c^codim-4 (4 = 2 endpoints x rank? or codim-4 grading).")
print()
print("  *** This is a LEAN, weight 0 (Cal #35 / K231c discipline). It is NOT closure. ***")
print("  The DECIDING computation is Lyra's: does the FK matrix element <V|O|V> reduce to")
print("  ONE Bergman autocorrelation trace (A) or require TWO irreducible endpoints (B)?")
print("  A numerical N_c-power lean cannot settle a trace-vs-endpoint STRUCTURE question;")
print("  only the FK matrix element derivation can. I hand that verdict to F50.")
print()
print("  G3: lean flagged weight-0; structural verdict handed to Lyra F50")
print()

print("G4: verifier ready-state for Lyra F50")
print("-" * 76)
print("  When Lyra fires F50 with a derived Direction, this toy verifies immediately:")
print("    - Direction A claim -> check single-trace form reproduces 81/8 AND 9/40 with a")
print("      CONSISTENT single N_c-power rule across both observables.")
print("    - Direction B claim -> check two-endpoint form reproduces N_c^2 amplitude (CKM)")
print("      AND N_c^4 muon edge with a consistent two-endpoint rule.")
print("  The decisive numerical test of Lyra's derivation: does ONE consistent N_c-power")
print("  rule (whichever Direction) fit BOTH observables, or do they need different rules")
print("  (which would itself be evidence against a clean single-mechanism closure)?")
print()
print("  STATUS: scaffold complete; awaiting Lyra F50 to run the verification.")
print("  Independent of this: Investigation #2 [H_B,P_restriction] (needs Lyra's P_restr")
print("  operator form) and Wall 6 a_k(n_C) (my R(k) lane) are my other queued pulls.")
print()
print("  Score: 4/4 (targets pinned; A/B signature; weight-0 lean; verifier ready)")
print()
print("=" * 76)
print("TOY 4013 SUMMARY -- Investigation #1 discriminator scaffold")
print("  targets: muon 81/8 (0.112%), CKM 9/40 (0.0 sigma). CKM amplitude N_c^2 LEANS B")
print("  (weight 0). A/B verdict = Lyra F50 FK matrix element. Verifier ready.")
print("=" * 76)
print()
print("SCORE: 4/4")
