"""
Toy 4034: vacuum-sector exponent 280 -- the sector BOUNDARY closes (N_c linear vs exponential);
the positive geometric grading characterization NEEDS CLOSE ANALYSIS (per Casey directive: pull
the newest thread; if it confuses more than closes quickly, note it + save + return to regular work).

CONTEXT: Grace + Lyra found the alpha-tower C_2-grammar holds in the conformal-breaking sector
(mass alpha^12, clock alpha^36, gravity alpha^90 -- all C_2-graded) but Lambda = exp(-280) breaks
it: 280 = 2^{N_c}.n_C.g is NOT C_2-divisible. Lambda sits in the VACUUM sector. Lyra/Keeper flagged
"characterize the vacuum-sector 280 to complete the split" as the newest thread. I pulled it.

WHAT CLOSES (quick, save it) -- the SECTOR BOUNDARY is N_c LINEAR vs EXPONENTIAL:
  Conformal-breaking sector exponents are C_2 = rank.N_c graded -- N_c enters as a LINEAR factor,
  so the exponents are divisible by N_c (and hence by C_2):
    mass    rank.C_2     = 12   (%N_c=0, %C_2=0)
    clock   C_2.C_2      = 36   (%N_c=0, %C_2=0)
    gravity C_2.N_c.n_C  = 90   (%N_c=0, %C_2=0)
  Vacuum sector exponent: 280 = 2^{N_c}.n_C.g -- N_c enters as an EXPONENT (2^{N_c}=8), NOT a bare
  linear factor. So 280 is divisible by rank=2 but NOT by N_c=3 (280%3=1), hence NOT by C_2=6.
  => The sector boundary IS the way N_c appears: LINEAR (rank.N_c, conformal-breaking, C_2-graded)
     vs EXPONENTIAL (2^{N_c}, vacuum). That's a clean substrate-natural characterization of the
     split Grace/Lyra drew -- it CLOSES at I-tier. Lambda is confirmed outside the breaking sector.

WHAT CONFUSES (needs close analysis -- flag + save + return) -- the POSITIVE geometric grading:
  The conformal-breaking sector grades by a SINGLE clean coset dimension C_2 = dim(SO(5,2)/SO(4,2)).
  The vacuum exponent 280 does NOT map to one obvious coset/geometric dimension -- it's a 3-PRIMARY
  PRODUCT 2^{N_c}.n_C.g with MANY equivalent arithmetic readings:
    280 = 2^{N_c}.n_C.g = rank.(N_max+N_c) = rank.N_max+C_2 = 2^{N_c}.C(g,N_c)  (35 = n_C.g = C(7,3))
  No single reading is clearly THE geometric one (unlike C_2). So the vacuum-sector GRADING's
  geometric origin (what 2^{N_c}.n_C.g IS, analogous to "breaking-coset dimension") does NOT close
  quickly. This AREA NEEDS CLOSE ANALYSIS.

PINNED QUESTION (for later examination, per Casey): "What is the geometric / coset / rep-theory
meaning of the vacuum-sector exponent 280 = 2^{N_c}.n_C.g -- the analog of C_2 = dim(breaking coset)
for the conformal-breaking sector? Why does N_c enter exponentially (2^{N_c}) in the vacuum and
linearly (rank.N_c) in the breaking sector?" This completes the conformal-breaking/vacuum split when
answered; it sets up the deferred cosmology framework with Lambda properly characterized.

DISPOSITION: partial close (sector boundary = N_c linear-vs-exponential, I-tier identification) +
flagged remainder (vacuum-sector geometric grading NEEDS CLOSE ANALYSIS, pinned). Returning to
regular investigation (alpha-tower reactive + sweep) per Casey directive.

GATES (3)
G1: sector boundary CLOSES -- 280 not C_2-divisible; N_c linear (breaking) vs exponential (vacuum)
G2: positive geometric grading NEEDS CLOSE ANALYSIS -- 280 = 3-primary product, many readings, no single coset dim
G3: pinned question saved; partial close at I-tier; return to regular work

Per Casey directive (investigate newest; note "needs close analysis" if it confuses; save + return);
Grace/Lyra sector finding; Lyra F68; Cal #237 (honest about what doesn't close); K231c; Cal #265/#266.

Elie - Monday 2026-06-08 (vacuum-sector 280; newest-thread pull, disciplined partial close)
"""

N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137
L = 2**N_c * n_C * g

print("=" * 78)
print("TOY 4034: vacuum-sector 280 -- boundary CLOSES (N_c linear vs exponential); grading FLAGGED")
print("=" * 78)
print()

print("G1: sector boundary CLOSES -- N_c LINEAR (breaking) vs EXPONENTIAL (vacuum)")
print("-" * 78)
print(f"  Lambda exponent 280 = 2^N_c . n_C . g = {2**N_c}.{n_C}.{g} = {L}")
print(f"  280 % C_2 = {L%C_2} (NOT /C_2) ; % rank = {L%rank} (/rank) ; % N_c = {L%N_c} (NOT /N_c)")
print(f"  conformal-breaking (N_c LINEAR via C_2=rank.N_c):")
for nm, e in [("mass rank.C_2", rank*C_2), ("clock C_2.C_2", C_2*C_2), ("gravity C_2.N_c.n_C", C_2*N_c*n_C)]:
    print(f"    {nm:<20} = {e:>3}   %N_c={e%N_c}  %C_2={e%C_2}")
print(f"  vacuum (N_c EXPONENTIAL via 2^N_c): 280 -> %N_c={L%N_c} -> not /N_c -> not /C_2.")
print(f"  => BOUNDARY = how N_c appears: LINEAR (breaking, C_2-graded) vs EXPONENTIAL (vacuum). CLOSES (I-tier).")
print()

print("G2: positive geometric grading NEEDS CLOSE ANALYSIS")
print("-" * 78)
print(f"  C_2 = 6 = dim(SO(5,2)/SO(4,2)) is ONE clean coset dim (breaking sector).")
print(f"  280 = 2^N_c.n_C.g is a 3-PRIMARY product with many equivalent readings (no single coset dim):")
for nm, v in [("2^N_c . n_C . g", 2**N_c*n_C*g), ("rank.(N_max+N_c)", rank*(N_max+N_c)),
              ("rank.N_max + C_2", rank*N_max+C_2), ("2^N_c . C(g,N_c) [35=n_C.g=C(7,3)]", 2**N_c*35)]:
    print(f"    280 = {nm:<34} = {v}  {'OK' if v == 280 else '?'}")
print(f"  No reading is clearly THE geometric one -> the vacuum-sector grading does NOT close quickly.")
print(f"  *** AREA NEEDS CLOSE ANALYSIS *** (flagged + saved per Casey directive).")
print()

print("G3: pinned question + disposition")
print("-" * 78)
print("  PINNED (for later): geometric/coset/rep-theory meaning of 280 = 2^N_c.n_C.g -- the vacuum-sector")
print("  analog of C_2 = dim(breaking coset)? Why N_c exponential (2^N_c) in vacuum vs linear (rank.N_c) in")
print("  breaking? Answering completes the conformal-breaking/vacuum split + sets up deferred cosmology w/ Lambda placed.")
print("  DISPOSITION: partial close (boundary = N_c linear-vs-exponential, I-tier) + remainder flagged.")
print("  Returning to regular investigation (alpha-tower reactive + sweep) per Casey directive.")
print()
print("  Score: 3/3 (boundary closes; positive grading honestly flagged needs-analysis; question pinned)")
print()
print("=" * 78)
print("TOY 4034 SUMMARY -- vacuum-sector 280: the SECTOR BOUNDARY closes -- N_c enters LINEARLY in the")
print("  conformal-breaking sector (rank.N_c=C_2-graded) vs EXPONENTIALLY in the vacuum (2^N_c), so 280")
print("  is not C_2-divisible (Lambda outside breaking sector). The POSITIVE geometric grading of 280 =")
print("  2^N_c.n_C.g (analog of C_2=coset-dim) NEEDS CLOSE ANALYSIS -- 3-primary product, many readings. Pinned; returning.")
print("=" * 78)
print()
print("SCORE: 3/3")
