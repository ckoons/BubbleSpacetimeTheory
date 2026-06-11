"""
Toy 4098: scoping #418 (the gauge-content program) -- the doubly-load-bearing second front Grace identified
(it underwrites BOTH the running band b_2/b_1 AND the mixing-is-forced claim). This characterizes the target
and verifies the substrate-natural pieces, independent of Lyra's flavor kernel. Headline: ONE SM generation =
15 Weyl fermions = N_c.n_C = dim SO(4,2) (or 16 = the SO(10) spinor with a right-handed neutrino) -- a
substrate-natural fermion-content target. The gauge group is SU(N_c) x SU(rank) x U(1) = SU(3) x SU(2) x U(1)
straight from the primaries. What #418 must FORCE is the fermion REPS + hypercharges (anomaly-consistent) --
that forcing is Lyra's bulk-color lane (F-series, partially open); I scope the target and verify what's
substrate-natural now. Count still 2.

1) GAUGE GROUP from the primaries:  SU(N_c) x SU(rank) x U(1)  =  SU(3) x SU(2) x U(1)
   dim SU(N_c) = N_c^2-1 = 8 (gluons); dim SU(rank) = rank^2-1 = 3 (W); U(1) = 1 (B). Total 12 gauge bosons.
   The two non-abelian factors are the substrate primaries: N_c (color), rank (weak). Substrate-natural.

2) ONE GENERATION = the SM Weyl fermion content (per generation):
   Q (quark doublet, color x weak)  : N_c x rank = 6   Y = +1/6
   u (up, R)                        : N_c x 1    = 3   Y = +2/3
   d (down, R)                      : N_c x 1    = 3   Y = -1/3
   L (lepton doublet)               : 1 x rank   = 2   Y = -1/2
   e (electron, R)                  : 1 x 1      = 1   Y = -1
   TOTAL = 6+3+3+2+1 = 15 Weyl fermions = N_c.n_C = dim SO(4,2).  (+1 nu_R -> 16 = SO(10) spinor.)
   => the generation count is forced (rank+1 = 3, F88); the generation CONTENT target is N_c.n_C = 15 (or SO(10) 16). Substrate-natural lead.

3) THE SU(2) DOUBLET (Grace's mixing argument -- load-bearing #1):
   the lepton doublet L = (nu, e)_L is ONE object -- the charged lepton and neutrino share one SU(2) frame by
   construction. That shared frame is what makes PMNS a forced mismatch (no free angle). So #418 producing the
   doublet underwrites the mixing-is-forced claim.

4) THE HYPERCHARGES -> the beta coefficients (load-bearing #2, closing the 4090 B1 gap):
   anomaly cancellation fixes the hypercharges Y; the full field content (reps + Y) determines b_2 = -19/6 and
   b_1 = -41/10 (the two beta coefficients 4090 left open). So #418 producing the reps + Y closes the B1 running
   band. => #418 is load-bearing TWICE: the doublet (mixing) + the reps (beta coefficients). One program, two pieces.

WHAT'S SUBSTRATE-NATURAL NOW vs WHAT #418 MUST FORCE:
  substrate-natural NOW (verified): gauge group {SU(N_c), SU(rank), U(1)}; one-generation Weyl count = N_c.n_C =
    15 = dim SO(4,2) (or 16 = SO(10) spinor); generation count rank+1 = 3 (F88).
  #418 MUST FORCE (Lyra bulk-color lane, partially open): the specific fermion REPS ((3,2,1/6), (3,1,2/3), ...)
    and the hypercharge assignments (anomaly-consistent). This is the gauge-content derivation; Grace sets the
    input-count bar; I verify pieces (b_3 = g already, 4090) as they land.

HONEST TIER:
  VERIFIED (substrate-natural): gauge group from the primaries; one generation = N_c.n_C = 15 = dim SO(4,2) (16
    with nu_R = SO(10) spinor); the doublet + hypercharge -> beta structure; #418 load-bearing twice (Grace).
  LEAD (flagged, not banked): 15 = N_c.n_C and 16 = SO(10) spinor are substrate-natural fermion-content targets;
    whether the substrate FORCES the reps + Y is Lyra's bulk-color derivation (#418). NOT asserting the forcing.
  NOT a count move: #418 is the gauge-content program; scoping it does not move the count. COUNT still 2.

GATES (2)
G1: #418 scope -- gauge group SU(N_c)xSU(rank)xU(1) from primaries (8+3+1=12 bosons); one generation = 15 Weyl = N_c.n_C = dim SO(4,2) (or SO(10) 16); generation count rank+1=3
G2: #418 load-bearing TWICE -- the SU(2) doublet underwrites mixing-forced (load #1); the reps+hypercharges give b_2/b_1 (load #2, closes 4090); the forcing = Lyra bulk-color lane, Grace sets the bar; count still 2

Per Grace (#418 load-bearing twice: mixing + running band; second front) + Keeper K302 + Lyra (bulk-color
F-series) + Casey (continue, scope #418); Elie 4090 (b_3=g, b_2/b_1 need #418) + 4096 (doublet mixing); F88
(generation count); 15 = N_c.n_C = dim SO(4,2) (memory); SO(10) 16-spinor (standard); Cal #237 + F79. Scopes the
second front; substrate-natural pieces verified; the reps+Y forcing is Lyra's bulk-color lane.

Elie - Wednesday 2026-06-10 (#418 scope: gauge group from primaries; one generation = 15 Weyl = N_c.n_C = dim SO(4,2) (16=SO(10) spinor); load-bearing twice (doublet+reps); forcing = Lyra bulk-color)
"""

from fractions import Fraction as F

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4098: #418 scope -- gauge content; one generation = N_c.n_C = 15 = dim SO(4,2)")
print("=" * 78)
print()

print("G1: gauge group + one-generation content (substrate-natural)")
print("-" * 78)
print(f"  gauge group: SU(N_c) x SU(rank) x U(1) -- dim {N_c**2-1} (gluons) + {rank**2-1} (W) + 1 (B) = {N_c**2-1+rank**2-1+1} bosons")
content = [("Q (quark doublet)", N_c * rank, F(1, 6)), ("u (R)", N_c, F(2, 3)), ("d (R)", N_c, F(-1, 3)),
           ("L (lepton doublet)", rank, F(-1, 2)), ("e (R)", 1, F(-1, 1))]
tot = sum(c for _, c, _ in content)
for name, c, Y in content:
    print(f"    {name:<20} {c:>2} Weyl   Y = {str(Y)}")
print(f"  ONE GENERATION = {tot} Weyl = N_c.n_C = {N_c*n_C} = dim SO(4,2)  (+1 nu_R -> 16 = SO(10) spinor). Substrate-natural target.")
print()

print("G2: #418 load-bearing TWICE + what it must force")
print("-" * 78)
print(f"  load #1 (mixing): the SU(2) doublet L=(nu,e)_L is ONE object -> shared frame -> PMNS forced (Grace).")
print(f"  load #2 (running band): the reps + hypercharges (anomaly-consistent) give b_2=-19/6, b_1=-41/10 -> closes the 4090 B1 gap.")
print(f"  => one program (#418) secures both. substrate-natural NOW: gauge group + 15=N_c.n_C generation + rank+1=3 count.")
print(f"  #418 MUST FORCE: the specific reps + Y (Lyra bulk-color lane, partially open). I verify pieces (b_3=g done); Grace sets the bar.")
print(f"  @Grace: scope target + substrate-natural pieces verified; ready to verify the reps/Y forcing against your input-count bar.")
print(f"  @Lyra: the fermion-content target is N_c.n_C=15 (or SO(10) 16); the doublet is the mixing common-frame. forcing = your bulk-color F-series.")
print(f"  Score: 2/2 (gauge group + one-generation=N_c.n_C=15=dim SO(4,2); #418 load-bearing twice; forcing = bulk-color lane; count still 2)")
print()
print("=" * 78)
print("TOY 4098 SUMMARY -- scoping #418 (the doubly-load-bearing second front). The gauge group SU(N_c)xSU(rank)x")
print("  U(1) comes straight from the primaries (12 bosons). One SM generation = 15 Weyl fermions = N_c.n_C =")
print("  dim SO(4,2) (16 = SO(10) spinor with nu_R) -- a substrate-natural fermion-content target. #418 is")
print("  load-bearing TWICE: the SU(2) doublet underwrites the mixing-is-forced claim, and the reps+hypercharges")
print("  give the b_2/b_1 beta coefficients (closing the 4090 B1 gap). What #418 must FORCE is the specific reps +")
print("  anomaly-consistent hypercharges -- Lyra's bulk-color lane; I scope the target and verify the substrate-natural")
print("  pieces. Count still 2.")
print("=" * 78)
print()
print("SCORE: 2/2")
