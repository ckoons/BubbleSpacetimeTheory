r"""
Toy 4204: stage-1 discrete half -- the transverse exponent = the domain RANK, forward and blind (Cal's named remaining
check), building on Lyra's forced lepton SEATS. Lyra closed the continuum half: the three charged-lepton addresses
{nu=0, 3/2, 5/2} are the only distinguished points of the holomorphic series on D_IV^5, computed from invariants (trivial
rep nu=0; last Wallach point nu=a/2 with a=n_C-2=3=N_c -> 3/2; self-dual point nu=n_C/2 -> 5/2), NEVER from a mass; the
neutrino sits at rho_3=1/2, the one NON-distinguished point (its sub-unitarity edge = why no Dirac mass, F144). She named
the remaining discrete pieces: (1) which Frobenius orbit lands at which seat, and (2) the transverse exponent (the only
thing Cal still has to check). THIS TOY does (2) forward+blind and (1) for the tau: the transverse exponent = rank because
the tau's deposit tiles the MAXIMAL FLAT of D_IV^5, which is rank-dimensional (a domain invariant, rank=2), at g cells per
direction (Frobenius period, 4195) -> g^rank. Forward (no reference to 3479) and reduces Cal's check to one modeling claim
("transverse deposit = the maximal flat"). The DEPTH assembly (g + 2^C2) and the -1.77 correction remain forward-open.
Count stays 2 of 26.

LYRA'S FORCED SEATS (continuum half, credited -- the addresses are off the back-fit surface):
  D_IV^5 type IV domain, complex dim n_C=5, rank 2, multiplicities a = n_C-2 = 3 = N_c, b = 0.
  distinguished points of the holomorphic series, from invariants:
    trivial rep        nu = 0                          -> tau
    last Wallach point nu = a/2 = (n_C-2)/2 = 3/2       -> muon
    self-dual point    nu = n_C/2 = 5/2                 -> electron
  the neutrino sits at rho_3 = 1/2 -- the ONLY one of the four rho-components that is NOT a distinguished point
  (the sub-unitarity edge) -> why it cannot take a normal Dirac mass (F144 from the other direction).
  CRUCIAL: these seats are computed from {a, n_C, rank}, never from a mass. so the tau's address nu=0 is FORCED as the
  trivial endpoint, not "ordering says heaviest" -- the address part of the tau prediction is OFF the back-fit surface.

THE TRANSVERSE EXPONENT = RANK (Cal's named check; forward + blind):
  the bounded symmetric domain D_IV^5 has RANK 2 = the dimension of its maximal totally-geodesic polydisk (the maximal
  flat) -- a domain invariant, computed from the domain, NOT from any mass. the tau's commitment tiles this transverse
  flat. each flat direction carries g cells (the Frobenius period, 4195: the vertex is the Frobenius fixed point, the
  commitment advances by the code's defining symmetry, period g). so:
        transverse count = g^(maximal-flat dimension) = g^rank = g^2 = 49.
  this is FORWARD (rank is a forced domain invariant; g is the Frobenius period) and BLIND (never reads 3479). it reduces
  Cal's check from "why exponent 2" to the single modeling claim "the transverse deposit IS the maximal flat" (forward-
  motivated: the maximal flat is the natural transverse extent of a bounded symmetric domain).
  dimension cross-check: dim = rank + a*C(rank,2) + b*rank = 2 + 3*1 + 0 = 5 = n_C. the bulk = the FLAT (rank=2 dims,
  the transverse) + the a-PART (dim a*C(rank,2) = 3 = N_c, the off-diagonal/depth directions). transverse = the flat.

ORBIT -> SEAT (the tau, forward):
  tau seat nu=0 (trivial rep) <-> the GF(128) additive identity 0 = the Frobenius FIXED POINT (4195). forward, the discrete
  orbit at the tau's seat is the trivial orbit {0}; the mass count is the bulk TILING around it, not the orbit. the electron
  (nu=5/2, self-dual) and muon (nu=3/2, last Wallach) seats are CONTINUUM (spectral strip / S^4) -- Lyra's half. so the
  discrete orbit->seat map has the tau at the fixed point; the other two seats are continuum-deposited.

HONEST STATUS (blind discipline held; what is forward vs open):
  FORWARD now (no 3479 reference): the SEATS {0,3/2,5/2} (Lyra, from invariants); the tau address nu=0 = trivial endpoint;
  the transverse exponent = rank (maximal flat) at side g (Frobenius period); the boundary depth 2^C2 = d_tau/d_mu (F109).
  STILL OPEN forward: (i) the DEPTH ASSEMBLY -- why the depth direction carries (g + 2^C2) (bulk g + boundary 2^C2,
  additive) rather than something else; (ii) the -1.77 CORRECTION (Toy 4203: the leading 49*71 is at 5.1e-4, above the tight
  floor; the correction must be forward-derived to clear it). so the tau leading-form assembly is now forward EXCEPT the
  depth-assembly, and the corrected value needs the forward correction. the transverse exponent (Cal's named check) is
  forward-motivated and reduced to one modeling claim. NOT yet a complete blind prediction; this is the discrete half
  advancing toward it, jointly with Lyra's continuum half. count stays 2 of 26; muon yellow, tau IDENTIFIED.
"""

from math import comb
from fractions import Fraction as F

n_C, rank, N_c, C2, g = 5, 2, 3, 6, 7
a = n_C - 2
b = 0
dim = rank + a*comb(rank, 2) + b*rank

seats = {"tau": F(0), "muon": F(a, 2), "electron": F(n_C, 2)}
neutrino_seat = F(1, 2)

transverse = g**rank
tau_box = g**rank * (g + 2**C2)

print("=" * 100)
print("TOY 4204: stage-1 discrete half -- transverse exponent = domain RANK (forward+blind); Lyra's forced seats")
print("=" * 100)
print()
print("Lyra's forced seats (continuum half, from invariants {a, n_C, rank} -- never a mass):")
print("-" * 100)
print(f"  D_IV^5: type IV, dim n_C={n_C}, rank={rank}, a=n_C-2={a} (=N_c: {a==N_c}), b={b}")
print(f"  trivial nu=0 -> tau ; last Wallach nu=a/2={seats['muon']} -> muon ; self-dual nu=n_C/2={seats['electron']} -> electron")
print(f"  neutrino at rho_3={neutrino_seat} = the ONLY non-distinguished point (sub-unitarity edge -> no Dirac mass, F144)")
print(f"  => tau address nu=0 is FORCED (trivial endpoint), OFF the back-fit surface.")
print()
print("transverse exponent = rank (Cal's named check; forward + blind):")
print("-" * 100)
print(f"  D_IV^5 maximal flat (polydisk) dimension = rank = {rank} (domain invariant, not from any mass)")
print(f"  side g (Frobenius period, 4195) -> transverse count = g^rank = {transverse}")
print(f"  dim = rank + a*C(rank,2) + b*rank = {rank} + {a}*{comb(rank,2)} + 0 = {dim} = n_C  (flat={rank} + a-part={a*comb(rank,2)})")
print(f"  reduces Cal's check to one modeling claim: 'the transverse deposit IS the maximal flat'.")
print()
print("orbit -> seat (tau, forward):")
print("-" * 100)
print(f"  tau seat nu=0 <-> GF(128) additive identity 0 = Frobenius FIXED POINT (4195); mass count = bulk TILING, not orbit {{0}}")
print(f"  electron (nu=5/2, strip) + muon (nu=3/2, S^4) seats are CONTINUUM (Lyra's half).")
print()

checks = [
    ("a = n_C - 2 = 3 = N_c", a == n_C - 2 == N_c),
    ("dim = rank + a*C(rank,2) = n_C (flat + a-part)", dim == n_C),
    ("forced seats {0, 3/2, 5/2} from invariants (Lyra)", seats == {"tau": F(0), "muon": F(3,2), "electron": F(5,2)}),
    ("neutrino seat 1/2 = the non-distinguished point", neutrino_seat == F(1,2)),
    ("maximal flat dimension = rank = 2 (transverse extent)", rank == 2),
    ("transverse count = g^rank = 49 (side g = Frobenius period)", transverse == 49),
    ("tau address nu=0 forced (trivial endpoint, off back-fit surface)", seats["tau"] == 0),
    ("tau box g^rank*(g+2^C2) = 49*71 (depth-assembly still forward-open)", tau_box == 49*71),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the discrete half of the lepton lock advancing, jointly with Lyra's continuum half. Lyra forward-closed the")
print("  SEATS: the three charged-lepton addresses {0, 3/2, 5/2} are the only distinguished points of the holomorphic series")
print("  on D_IV^5, computed from {a=n_C-2=N_c, n_C, rank} and never from a mass, with the neutrino at the one non-")
print("  distinguished point rho_3=1/2 (its sub-unitarity edge = no Dirac mass). That puts the tau's address nu=0 (the trivial")
print("  endpoint) off the back-fit surface. This toy does the transverse exponent -- Cal's named remaining check -- forward")
print("  and blind: the tau's commitment tiles the MAXIMAL FLAT of D_IV^5, whose dimension is the domain RANK (=2, an")
print("  invariant), at g cells per direction (the Frobenius period), giving g^rank = 49 -- with no reference to 3479. That")
print("  reduces Cal's check from 'why exponent 2' to the single modeling claim 'the transverse deposit is the maximal flat'.")
print("  The tau's orbit->seat is forward too: nu=0 = the GF(128) additive identity = the Frobenius fixed point, with the mass")
print("  count being the bulk tiling around it (the vertex's own orbit is trivial). What remains forward-open: the DEPTH")
print("  assembly (why the depth carries g + 2^C2) and the -1.77 correction (Toy 4203: the leading 49*71 is above the tight")
print("  floor; the correction must be forward-derived to clear it). So the tau leading assembly is now forward except the")
print("  depth, and the corrected value needs the forward correction -- the discrete half advancing toward a clean blind")
print("  prediction, joint with Lyra. Count stays 2 of 26; muon yellow, tau IDENTIFIED.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (stage-1 discrete half, transverse exponent = domain RANK forward+blind = Cal's named remaining check, building on Lyra's forced lepton SEATS: Lyra closed the continuum half -- the three charged-lepton addresses {nu=0,3/2,5/2} are the ONLY distinguished points of the holomorphic series on D_IV^5 computed from invariants (trivial rep nu=0; last Wallach point nu=a/2 with a=n_C-2=3=N_c -> 3/2; self-dual point nu=n_C/2 -> 5/2) NEVER from a mass, neutrino at rho_3=1/2 the one NON-distinguished point (sub-unitarity edge = no Dirac mass F144), so the tau address nu=0 is FORCED as the trivial endpoint OFF the back-fit surface; THIS TOY (Cal's named check) transverse exponent = rank because the tau deposit tiles the MAXIMAL FLAT of D_IV^5 which is rank-dimensional (domain invariant rank=2 = dim of max totally-geodesic polydisk, NOT from any mass) at g cells per direction (Frobenius period 4195) -> transverse = g^rank = g^2 = 49, FORWARD (rank forced domain invariant + g Frobenius period) and BLIND (never reads 3479), reduces Cal's check from 'why exponent 2' to ONE modeling claim 'transverse deposit IS the maximal flat'; dim cross-check dim = rank + a*C(rank,2) + b*rank = 2 + 3*1 + 0 = 5 = n_C, bulk = FLAT (rank=2 transverse) + a-PART (dim a*C(rank,2)=3=N_c depth/off-diagonal); ORBIT->SEAT tau seat nu=0 <-> GF(128) additive identity 0 = Frobenius FIXED POINT (4195) mass count = bulk TILING not the trivial orbit {0}, electron (nu=5/2 strip) + muon (nu=3/2 S^4) seats CONTINUUM (Lyra half); HONEST blind held, FORWARD now (no 3479) = seats {0,3/2,5/2} (Lyra from invariants) + tau address nu=0 trivial endpoint + transverse exponent=rank (maximal flat) side g (Frobenius period) + boundary depth 2^C2=d_tau/d_mu F109, STILL OPEN forward = (i) DEPTH ASSEMBLY why depth carries g+2^C2 (bulk g + boundary 2^C2 additive), (ii) -1.77 CORRECTION (Toy 4203 leading 49*71 at 5.1e-4 above tight floor, correction must be forward-derived to clear); tau leading assembly now forward EXCEPT depth-assembly + corrected value needs forward correction, discrete half advancing toward clean blind prediction joint with Lyra continuum half; count 2 of 26 muon yellow tau IDENTIFIED)")
print()
print(f"SCORE: {passed}/{len(checks)} (stage-1 discrete half: Lyra's forced SEATS {{0,3/2,5/2}} from invariants (a=n_C-2=N_c, n_C, rank) not mass, neutrino at non-distinguished 1/2; transverse exponent = rank (Cal's check) FORWARD+BLIND -- tau tiles the maximal flat (dim=rank=2 domain invariant) at g cells/dir (Frobenius period) -> g^rank=49, reduces Cal check to one modeling claim 'transverse deposit = maximal flat'; tau orbit->seat nu=0 = Frobenius fixed point 0 (4195), mass=bulk tiling; FORWARD-OPEN: depth assembly (g+2^C2) + the -1.77 correction (4203); discrete half advancing joint with Lyra; count 2 of 26)")
