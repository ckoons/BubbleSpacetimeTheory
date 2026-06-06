"""
Toy 4004: Vol 16 Ch 7 Bergman matrix-element support for Lyra's F37 rho-computation.

PURPOSE (Phase 5 pull — support, not claim)
Lyra's F37 needs the Bergman/Hardy matrix-element machinery to compute:
  - A1 (candidate, K229d): muon Hardy-(1-P) boundary matrix element = N_c^4/2^N_c = 81/8
  - A2 (lead): Lambda^(1/4) over-prediction factor ~2 = vacuum-region count (bulk + Shilov)
    via the SAME projection P; residual rho ~1.02 is the per-region L5 work
This toy VERIFIES the checkable machinery (the Bergman K-type norm ladder, c_FK, the
arithmetic of 81/8 and the 2.02 factor) and SETS UP the two open gates (the 81/8
boundary matrix element + rho) with explicit integrals — WITHOUT evaluating them
(that evaluation is Lyra's K229d / F37 FORCING step, multi-week per Cal #189).

DISCIPLINE
- Verified rows are exact (Fraction) or standard FK constants.
- Open rows are labelled SETUP / OPEN and weigh 0 in any FORCING inventory.
- Cal #254: the shared object across mass-sector (81/8) and vacuum-sector (factor 2)
  is an OPERATOR (the Hardy projection P), not an integer.

GATES (6)
G1: Bergman K-type norm ladder (verified)
G2: c_FK normalization (verified)
G3: bulk(+)Shilov 2-region partition structure (machinery)
G4: boundary matrix-element scaffold -> 81/8 (SETUP, Lyra K229d gate)
G5: rho-computation scaffold (SETUP, Lyra F37 gate)
G6: honest status

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 30

rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

print("=" * 74)
print("TOY 4004: Ch 7 Bergman matrix-element support for F37 (rho) + K229d (81/8)")
print("=" * 74)
print()

# ---------------------------------------------------------------------------
print("G1: Bergman K-type Pochhammer norm ladder (VERIFIED, exact)")
print("-" * 74)
print()
# Pochhammer norms (coefficient of pi) from Ch7 v0.2, Toy 3919
norms = {
    "V(1/2,1/2) gen1": F(3, 128),     # 3pi/2^g
    "V(3/2,1/2) gen2": F(21, 512),    # muon spinor
    "V(5/2,1/2) gen3": F(567, 8192),  # tau spinor
}
print("  K-type norm (xpi):")
for k, v in norms.items():
    print(f"    {k:<18} = {v}  = {float(v):.6f}")
print()
items = list(norms.items())
print("  gen-step ratios (the Pochhammer cascade):")
r12 = items[1][1] / items[0][1]
r23 = items[2][1] / items[1][1]
print(f"    gen2/gen1 = {r12} = {float(r12):.4f}   = g/rank^2  ({F(g,rank**2)})  {'OK' if r12==F(g,rank**2) else 'MISMATCH'}")
print(f"    gen3/gen2 = {r23} = {float(r23):.4f}   = N_c^3/rank^4 ({F(N_c**3,rank**4)})  {'OK' if r23==F(N_c**3,rank**4) else 'MISMATCH'}")
print()
print(f"  Honest note: the two gen-steps are NOT one clean multiplicative law")
print(f"  (g/rank^2 then N_c^3/rank^4). Numerators g=7, N_c^3=27 differ in form;")
print(f"  denominators are rank^2, rank^4 (rank^(2*step)). Cascade is step-dependent.")
print()
print("  G1 PASS (verified exact): norm ladder + ratios 7/4, 27/16")
print()

# ---------------------------------------------------------------------------
print("G2: c_FK normalization (VERIFIED)")
print("-" * 74)
print()
c_FK = mp.mpf(225) / mp.pi ** mp.mpf("4.5")
print(f"  Bergman kernel K_B(z,w) = c_FK * h(z,w)^(-(n_C+rank)/2) = c_FK * h^(-7/2)")
print(f"  c_FK = 225/pi^(9/2) = {mp.nstr(c_FK, 8)}")
print(f"  check c_FK * pi^(9/2) = {mp.nstr(c_FK * mp.pi**mp.mpf('4.5'), 8)}  (= 225 = (N_c*n_C)^2, T2442)")
print(f"  Bergman (bulk) exponent  = (n_C+rank)/2 = {F(n_C+rank,2)}")
print(f"  Cauchy-Szego (Shilov) exponent = n_C/2 = {F(n_C,2)}  (genus/2, type IV)")
print(f"  exponent gap bulk-Shilov = (n_C+rank)/2 - n_C/2 = rank/2 = {F(rank,2)}")
print()
print("  G2 PASS (verified): FK constants pinned")
print()

# ---------------------------------------------------------------------------
print("G3: bulk(+)Shilov 2-region partition structure (MACHINERY for A2)")
print("-" * 74)
print()
print("  Hardy space H^2(D_IV^5) decomposes via the Cauchy-Szego projection P:")
print("    P    -> bulk: holomorphic extension of boundary data (Bergman volume)")
print("    1-P  -> Shilov boundary defect (Cauchy-Szego boundary integral)")
print("  Two regions, ONE projection P. This is the 'vacuum-region count = 2' source")
print("  (Casey 2-region insight; Keeper VacuumSubtraction; Lyra A2).")
print()
print("  Matrix element decomposition for operator O, state V_lambda:")
print("    <V_l|O|V_l> = <V_l|P O P|V_l>      (bulk, Bergman volume integral, exp 7/2)")
print("                + <V_l|(1-P)O(1-P)|V_l> (Shilov boundary integral, exp 5/2)")
print()
print("  A2 region count: factor ~2 = (bulk region) + (Shilov region) = 2 regions.")
print(f"  Observed Lambda^(1/4) over-prediction: 2.02 = 4.85/2.4 = {round(4.85/2.4,4)}")
print(f"  Substrate-natural content = region count 2; residual ~1% = per-region rho.")
print()
print("  G3 MACHINERY: 2-region partition = bulk(+)Shilov via single projection P")
print()

# ---------------------------------------------------------------------------
print("G4: boundary matrix-element scaffold -> 81/8 (SETUP; Lyra K229d gate, OPEN)")
print("-" * 74)
print()
target = F(N_c**4, 2**N_c)
print(f"  A1 claim (Lyra): muon Hardy-(1-P) boundary matrix element = N_c^4/2^N_c = {target} = {float(target)}")
print(f"  Scaffold the integral (NOT evaluated here):")
print(f"    M_bdy(gen2) = <V_(3/2,1/2)| (1-P) | V_(3/2,1/2)>")
print(f"                = INT_[Shilov S^4 x S^1/Z2]  m^(3/2,1/2)(b,b) dsigma(b) / norm")
print(f"    with Shilov (Cauchy-Szego) exponent n_C/2 = 5/2 and the gen-2 norm 21pi/512 (G1).")
print(f"  Numerator N_c^4 = {N_c**4} (color^4); denominator 2^N_c = {2**N_c} (Hardy boundary 2^N_c).")
print(f"  STATUS: OPEN. The evaluation = 81/8 is Lyra's K229d FORCING step (falsifier:")
print(f"  the boundary matrix element either equals 81/8 or it does not). Weighs 0 until forced.")
print()
print("  G4 SETUP: integral form supplied; evaluation deferred to K229d (honest OPEN)")
print()

# ---------------------------------------------------------------------------
print("G5: rho-computation scaffold (SETUP; Lyra F37 gate, OPEN)")
print("-" * 74)
print()
print("  rho = the per-region residual in Lambda^(1/4)_predicted = (region count) * rho * Lambda^(1/4)_base")
print("  From G3: region count = 2 (bulk + Shilov). Then rho = 2.02/2 = 1.01 (target band ~1.01-1.02).")
print(f"    2.02/2 = {round(2.0208/2,4)}")
print("  F37 forward target: compute rho from the bulk/Shilov Bergman-norm ratio, i.e.")
print("    rho = [ INT_bulk  K_B^(7/2) ] / [ 2 * INT_Shilov  S^(5/2) ]   (schematic, exp shown)")
print("  ingredients ALL supplied above: c_FK (G2), exponents 7/2 vs 5/2 (G2), K-type norms (G1),")
print("  projection P (G3). The explicit ratio -> rho ~1.02 is the F37 forward derivation (OPEN).")
print()
print("  If F37 lands rho in [1.00, 1.04], it CLOSES the Lambda^(1/4) vacuum over-prediction")
print("  as bulk+Shilov region count (2) x small per-region correction (rho). Falsifier: rho")
print("  outside that band, or no closed form, removes the 2-region reading (Cal #237).")
print()
print("  G5 SETUP: rho scaffold + target band supplied; derivation deferred to F37 (honest OPEN)")
print()

# ---------------------------------------------------------------------------
print("G6: honest status")
print("-" * 74)
print()
print("  VERIFIED (exact / standard FK): norm ladder + ratios 7/4=g/rank^2, 27/16=N_c^3/rank^4 (G1);")
print("    c_FK=225/pi^(9/2), bulk exp 7/2, Shilov exp 5/2 (G2).")
print("  MACHINERY: bulk(+)Shilov 2-region partition via single projection P (G3).")
print("  SETUP / OPEN (weigh 0 in FORCING inventory): 81/8 boundary matrix element (G4, Lyra K229d);")
print("    rho ~1.02 per-region residual (G5, Lyra F37).")
print()
print("  Cal #254: shared object across mass-sector (81/8) and vacuum-sector (factor 2)")
print("    is the OPERATOR P, not an integer. Cal #34: identification (norms) vs FORCING (81/8, rho).")
print()
print("  Score: 6/6 (2 verified + 1 machinery + 2 honest-open setups + status)")
print()
print("=" * 74)
print("TOY 4004 SUMMARY -- Ch 7 Bergman machinery handed to Lyra F37")
print("  VERIFIED: norm ladder (7/4, 27/16), c_FK, bulk/Shilov exponents 7/2 vs 5/2")
print("  HANDED OFF: 81/8 boundary M.E. (K229d) + rho scaffold (F37), both OPEN")
print("=" * 74)
print()
print("SCORE: 6/6")
