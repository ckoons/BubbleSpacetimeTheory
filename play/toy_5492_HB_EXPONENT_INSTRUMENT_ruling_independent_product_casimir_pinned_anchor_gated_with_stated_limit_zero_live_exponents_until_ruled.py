# TOY 5492 -- THE H_B EXPONENT INSTRUMENT. Elie, 2026-08-24. Ruling-independent per Grace's
# amended protocol (AUDITABLE PIN accepted -- my own outcome map killed the blind-pinner;
# every step below is arithmetic on her pinned formula or a fixture, auditable by Cal).
#
# PINNED (Grace, from the primary, verbatim-quote pin): H_B = Casimir of K = SO(5)xSO(2),
#   E(m1, m2; w) = m1(m1+3) + m2(m2+1) + w^2,  scale fixed by the R79-gated B3 form.
# ANCHOR (w-BLIND, limit stated): E(1,1;0) = 6 validates the SO(5) normalization ONLY --
#   it cannot discriminate the SO(2) term, which stands on the product-Casimir wording alone.
#   THIS GATE CLAIMS EXACTLY THAT AND NO MORE.
# RESTRICTION: *** UNDEFINED IN THE PRIMARY (Grace's finding) -- awaiting a Keeper/Cal ruling
#   on principle. ZERO LIVE EXPONENTS in this file until the ruling artifact resolves on disk.
from fractions import Fraction as F
import os
BAR="="*100
def E(m1,m2,w): return F(m1)*(F(m1)+3) + F(m2)*(F(m2)+1) + F(w)**2
print(BAR); print("TOY 5492 -- H_B exponent instrument (ruling-independent build)"); print(BAR)
print("\nGATE (w-blind anchor, limit stated):")
a=E(1,1,0)
print("  E(1,1;0) = 4 + 2 + 0 = %s  vs banked C_2 = 6 -> %s"%(a,"PASS" if a==6 else "FAIL"))
print("  *** THIS VALIDATES THE SO(5) NORMALIZATION ONLY. The SO(2) term is pinned by the")
print("      product-Casimir wording, NOT by this anchor. The gate claims no more. ***")
if a!=6: raise SystemExit("anchor failed")
print("  second normalization point, same limit: E(1,0;0) = 4 (SO(5) vector) -- consistency only.")
assert E(1,0,0)==4
def channel_min(ktypes):
    """ktypes: list of (m1, m2, w). Returns (E_min, argmin). Exact arithmetic."""
    vals=[(E(*kt),kt) for kt in ktypes]
    return min(vals)
print("\nSELF-TEST ON FIXTURES ONLY (deliberately neither candidate restriction -- zero live")
print("exponents exist before the ruling, matching Grace's zero-live-exponent pin file):")
fx1=[(0,0,7),(1,0,7)]; fx2=[(2,0,0),(1,1,3)]
for name,fx in (("fixture-1",fx1),("fixture-2",fx2)):
    m,arg=channel_min(fx)
    print("  %-10s min E = %-6s at %s"%(name,m,arg))
assert channel_min(fx1)==(F(49),(0,0,7)) and channel_min(fx2)==(F(10),(2,0,0))
print("  fixtures verified by hand-arithmetic in-line. Instrument arithmetic is exact (Fractions).")
print("\nLIVE FIRE PROTOCOL (armed, held):")
# K1824 UPDATE: the ruling EXISTS (A excluded pre-fork; B ruled as a CLASS). The live-fire
# condition therefore REFINES: not the ruling artifact, but GRACE'S C1 FUNCTIONAL having
# passed C2 (must-reproduce T2514/F375), C3 (must-reject: bulk mode not landing Shilov),
# and Cal's outcome-steering audit. The env var now names THAT artifact.
# GATE UPDATE (Keeper, post-756): C1 PASSED Cal's steering audit (no energy content -- the
# decisive fact). Live-fire now waits on: Grace's C2/C3/C3b validation artifact on disk,
# all controls green, PLUS the mode->subspace assembly sentence present. C3b (exhaustion-
# independence) was adopted as a required control before the cross.
# GATE UPDATE 2 (Grace's R95 stop, ratified): the FROZEN ASSEMBLY DEGENERATES under both
# readings -- Shilov-kernel spans are DENSE (closure = everything, E2 = global min) and
# K-type basis modes are all interior (strata spans EMPTY). The controls validated the
# FUNCTIONAL; the assembly killed the STRATIFICATION. The cross was stopped at the last
# gate BEFORE burning the one-shot on a contentless answer. Hold condition is now:
# Grace's NEW-ASSEMBLY prereg exists + Cal's audit passed + its controls green.
RULING=os.environ.get("HB_NEW_ASSEMBLY_PREREG_PASSED","")
base="/Users/cskoons/projects/github/BubbleSpacetimeTheory/"
if RULING and os.path.exists(base+RULING):
    print("  C1 functional (C2/C3+audit passed) present: %s -- SUPPLY its channels as (m1,m2,w) lists;"%RULING)
    print("  this instrument posts three exponents THEN the comparison, per protocol.")
else:
    print("  NO NEW-ASSEMBLY PREREG -- live channels REFUSED. The frozen assembly is DEFECTIVE")
    print("  (both readings degenerate: dense span / empty span -- an L2 space cannot see")
    print("  boundary strata from inside). The shot is PRESERVED, staged against whatever")
    print("  valid mode space the new prereg defines. Functional and falsifier untouched.")
    print("  Until one passes, computing anything would let the thermal reading vote on the")
    print("  operator reading -- the exact move R94 forbids. The instrument waits.")
print("\nStatus: BUILT, GATED, HELD. The hour the restriction is ruled, the blind-cross runs.")
