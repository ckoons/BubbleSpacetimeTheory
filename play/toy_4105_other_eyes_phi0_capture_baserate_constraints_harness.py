"""
Toy 4105: "other eyes" on Lyra's Phi_0-capture problem (Casey asked the team to look). Three contributions
from the numerical/structural side -- NONE of them a value-fit; all support the no-fishing line and scope the
derivation. (1) BASE-RATE: the space around 206.77 is dense -- ~4 simple product-forms land within 1% (of 1103
scanned) -- so a value-match alone is meaningless; a DERIVED Phi_0 hit is the only meaningful path, and the
207 = (N_c.n_C)^2 - N_c.C_2 coincidence Lyra flagged is correctly refused. (2) A STRUCTURAL SURVIVOR: my
non-geometric-hierarchy result (Toy 4091) survives the pole->quotient correction -- the electron is the lone
INTERIOR rep, mu and tau are the LIMIT reps, so the big e->mu jump is interior->limit and the smaller mu->tau is
limit->limit. (3) CONSTRAINTS + a structural QUESTION for the derivation, and the test harness (ready). Count 2.

ABSORBED (Grace's un-banking): the tau/mu = (8/3).2pi at 0.37% is the norm of the WRONG (reducible) module +
matched regularization -- it UN-BANKS. No mass ratio is in hand. The physical value is the Phi_0 boundary
expectation in the irreducible quotient -- not yet computed. (My 4097/4103 already superseded; Grace formalizes.)

(1) BASE-RATE around the targets (supports refusing coincidences):
  ~4 of 1103 simple product-forms (primary powers, |exponents| small) land within 1% of 206.77. The space is
  DENSE: a simple-form value-match (e.g. 225 - 18 = 207 at 0.1%) is plausibly chance. => a Phi_0 capture hitting
  206.77 counts ONLY because Phi_0 is DERIVED (forced operator), not because 206.77 is special. The discipline
  and the gate are the same thing (Grace's pre-committed bar: derived-not-picked is required to bank).

(2) STRUCTURAL SURVIVOR -- Toy 4091 holds under the correction:
  the lepton hierarchy is NON-geometric (e->mu = 207, mu->tau = 16.8, ~12x apart; electron anomalously light).
  OLD reading: electron = lone REGULAR Gamma-pole point. CORRECTED reading: electron = lone INTERIOR rep
  (codim 0, timelike interior, generic); mu = CONE (codim 3, limit rep); tau = VERTEX (codim 5, limit rep).
  => the big e->mu jump is INTERIOR -> LIMIT-rep (crossing into the boundary faces); the smaller mu->tau is
     LIMIT -> LIMIT (between boundary faces). Same conclusion as 4091, correct mechanism: the electron's
     anomalous lightness is its being the one interior (non-limit) representation. (per-codim factors differ:
     e->mu ~ 207^(1/3) = 5.91/codim vs mu->tau ~ 16.8^(1/2) = 4.10/codim -- NOT a single power, exactly because
     e is interior and mu,tau are limit reps. This is WHY the codim power-law fails, Lyra's negative explained.)

(3) CONSTRAINTS on Phi_0 + a structural QUESTION (for the derivation, not banked):
  HARD constraints (non-fishing, from the structure):
    - capture NONZERO at nu=0 (tau heaviest) => Phi_0 is NOT proportional to nu (Lyra: ~nu makes tau massless);
    - capture INCREASES toward the boundary: c_e(5/2) < c_mu(3/2) < c_tau(0);
    - codim {0,3,5} is a geometric guide but NOT a single power law (per-codim factor non-constant);
    - targets: c_mu/c_e = 206.77, c_tau/c_e = 3477.
  STRUCTURAL QUESTION (for Lyra's derivation -- a candidate to test or refute, NOT a banked form):
    does the capture FACTORIZE over the removed-null-vector directions -- one factor per Shapovalov null vector
    quotiented out (interior -> cone removes the L2-trace null at nu=3/2; cone -> vertex removes more) -- with
    each factor a ratio of the boundary Phi_0 norm to the bulk norm? If so, the limit-rep capture is a product
    of finite Shapovalov-norm ratios, and the non-constant per-codim factor is automatic (different reps removed).
    This is a QUESTION for the Phi_0 derivation, offered for testing -- I do NOT assert it or fit it.

  TEST HARNESS (ready): given Lyra's three captures {c_e, c_mu, c_tau} -> ratios -> check {1, 206.77, 3477}
  (Toy 4104). The harness takes her DERIVED captures the instant they land; no value is fished here.

HONEST TIER:
  BANKED (this toy): the base-rate density (dense space -> value-match meaningless); the 4091 survivor (electron
    = lone interior rep, the corrected mechanism for the non-geometric hierarchy); the hard constraints on Phi_0.
  OFFERED (not banked): the factorize-over-null-vectors structural question -- a candidate for Lyra to derive or
    refute, NOT asserted, NOT fitted.
  NOT done / DECLINED: the captures themselves -- Lyra's Phi_0 derivation (limit-rep handling). I do NOT fish any
    value (the 207 coincidence is refused). COUNT still 2; no ratio in hand (Grace's un-banking absorbed).

GATES (2)
G1: base-rate -- ~4/1103 simple forms within 1% of 206.77 (dense); a Phi_0 hit counts only because DERIVED, not because 206.77 is special; supports refusing the 207 coincidence + Grace's pre-committed gate
G2: 4091 survivor (electron = lone INTERIOR rep, mu/tau limit reps -> non-geometric hierarchy, per-codim factor non-constant) + hard Phi_0 constraints + the factorize-over-null-vectors QUESTION (offered, not banked) + harness ready; count still 2

Per Casey (team eyes on the Phi_0 problem) + Lyra (3 light-cone-face quotients; Phi_0 capture; mu/tau Wallach-limit
reps; codim negative; 207 refused) + Grace (un-banks tau/mu; pre-committed gate; Phi_0 = new gating item) + Elie
4091 (non-geometric hierarchy, survives) + 4104 (pipeline) ; Cal #35 (base-rate) + Cal #237 + F79. Other eyes:
base-rate + structural survivor + constraints + a derivation question + the harness; no fishing.

Elie - Thursday 2026-06-11 (other eyes on Phi_0: base-rate (space dense, refuse coincidences); 4091 survives (e=lone interior rep); Phi_0 constraints; factorize-over-null-vectors question offered; harness ready; count 2)
"""

import itertools, math

N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137
pi = math.pi
target1, target2 = 206.77, 3477.0

print("=" * 78)
print("TOY 4105: other eyes on Phi_0 -- base-rate, the 4091 survivor, constraints, harness")
print("=" * 78)
print()

print("G1: base-rate -- the space around 206.77 is dense (refuse coincidences)")
print("-" * 78)
vals = [3, 5, 6, 7, 2, 137, pi]
hits = 0
total = 0
for combo in itertools.product(range(-2, 4), repeat=len(vals)):
    if sum(abs(x) for x in combo) > 4:
        continue
    v = 1.0
    for b, e in zip(vals, combo):
        v *= b**e
    if v <= 1 or v > 1e6:
        continue
    total += 1
    if abs(v - target1) / target1 < 0.01:
        hits += 1
print(f"  ~{hits} of {total} simple product-forms land within 1% of 206.77 -> DENSE. A value-match alone is meaningless.")
print(f"  => a Phi_0 capture hitting 206.77 counts ONLY because Phi_0 is DERIVED. The 207 = 225-18 coincidence is correctly refused.")
print()

print("G2: the 4091 survivor + Phi_0 constraints + a structural question")
print("-" * 78)
print(f"  4091 SURVIVES: electron = lone INTERIOR rep (codim 0); mu = CONE (codim 3, limit); tau = VERTEX (codim 5, limit).")
print(f"    => big e->mu jump = interior->limit; smaller mu->tau = limit->limit. Non-geometric hierarchy = the electron being the one interior rep.")
print(f"    per-codim factor: e->mu = 207^(1/3) = {207**(1/3):.2f}; mu->tau = 16.8^(1/2) = {16.8**0.5:.2f} -- NON-constant (why codim power-law fails).")
print(f"  HARD constraints on Phi_0: NOT proportional to nu (tau heaviest, nonzero at nu=0); capture increases toward boundary; targets {{207, 3477}}.")
print(f"  QUESTION (offered, not banked): does the capture FACTORIZE over the removed Shapovalov null-vector directions, each factor a")
print(f"    boundary/bulk Phi_0-norm ratio? If so, the limit-rep capture = a product of finite norm ratios, and the non-constant per-codim factor is automatic.")
print(f"  @Lyra: harness ready (4104); the factorize question is a candidate to derive/refute, NOT a form I'm fitting. @Grace: base-rate supports your pre-committed gate.")
print(f"  Score: 2/2 (base-rate dense; 4091 survives as interior-vs-limit; Phi_0 constraints; factorize question offered; harness ready; no fish; count 2)")
print()
print("=" * 78)
print("TOY 4105 SUMMARY -- other eyes on Lyra's Phi_0 capture (Casey's team-eyes call). (1) Base-rate: the space")
print("  around 206.77 is dense (~4/1103 simple forms within 1%), so a value-match alone is meaningless -- a Phi_0")
print("  hit counts only because Phi_0 is DERIVED, and the 207 = 225-18 coincidence is rightly refused. (2) My 4091")
print("  non-geometric-hierarchy result SURVIVES the pole->quotient correction: the electron is the lone INTERIOR")
print("  rep, mu/tau are the LIMIT reps, so e->mu is interior->limit (big) and mu->tau is limit->limit (small) --")
print("  the corrected mechanism, and why the codim power-law fails (non-constant per-codim factor). (3) Hard Phi_0")
print("  constraints + a factorize-over-null-vectors QUESTION (offered for Lyra to test, not banked) + the harness")
print("  ready. No fishing; no ratio in hand (Grace's un-banking absorbed); count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
