# TOY 5476 -- THE F638 CHAMBER INSTRUMENT. Elie, 2026-08-24. R81 assignment.
# Rubric cell: External 3 / Internal B (chirality).
#
# JOB (R81): F638's chamber formula as an executable toy, GATED BEFORE USE:
#   must-reproduce (the scalar case's known chamber) and must-reject (a deliberately wrong rho).
#   Then PRE-REGISTER which chambers give L-doublet/R-singlet BEFORE Lyra's c-values land,
#   "so the check cannot be read either way afterward."
#
# INDEPENDENCE DISCIPLINE: I do NOT copy F638's root table. I DERIVE the B3 root system from
# scratch, compute rho and Delta_n+ from the derivation, and CHECK against F638. If they
# disagree, the gate fails and nothing downstream is read. That makes the "verify the roots"
# handoff (F638 @Elie, 2026-07-22 -- never run, confirmed by grep) and the instrument ONE object.
#
# NOVELTY (R81 rule -- read the NEXT artifact): grep of play/ shows no F638 verification toy
# exists; toy 4777 is the +-4 consistency point F638 cites, not the instrument.

from fractions import Fraction as F
import itertools
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5476 -- the F638 chamber instrument. Gates first, pre-registration second,"); print("            and NO c-value is evaluated anywhere in this file."); print(BAR)

# ---------------------------------------------------------------- derive B3 from scratch
head("PART A -- DERIVE the root data (not copied from F638)")
print("  g = so(5,2), complexified = B3. Orthogonal basis (e1, e2, e3), e1 = the SO(2) direction.")
print("  B3 positive roots: {e_i} u {e_i - e_j, e_i + e_j : i < j}.")
e=[None]*4
def vec(*c): return tuple(F(x) for x in c)
pos=[]
for i in range(1,4): 
    v=[0,0,0]; v[i-1]=1; pos.append(vec(*v))
for i,j in itertools.combinations(range(1,4),2):
    v=[0,0,0]; v[i-1]=1; v[j-1]=-1; pos.append(vec(*v))
    w=[0,0,0]; w[i-1]=1; w[j-1]=1;  pos.append(vec(*w))
assert len(pos)==9, len(pos)
rho=tuple(sum(r[k] for r in pos)/F(2) for k in range(3))
print("  positive roots (9): %s"%[tuple(int(x) if x==int(x) else str(x) for x in r) for r in pos])
print("  rho = half-sum     = (%s, %s, %s)"%rho)
# compact = roots not involving e1 (SO(5) on (e2,e3)); noncompact = carry e1
compact=[r for r in pos if r[0]==0]
noncompact=[r for r in pos if r[0]!=0]
print("  compact positive (no e1): %d roots  %s"%(len(compact),[tuple(map(int,r)) for r in compact]))
print("  NONCOMPACT positive (carry e1): %d roots %s"%(len(noncompact),[tuple(map(int,r)) for r in noncompact]))

# ---------------------------------------------------------------- the formula
def pairing(lam):
    """the five noncompact pairings <lam+rho, beta>, standard orthogonal inner product"""
    lp=tuple(lam[k]+rho[k] for k in range(3))
    return sorted(sum(lp[k]*b[k] for k in range(3)) for b in noncompact)
def q_of(lam):
    """concentration degree; None if any pairing is exactly 0 (ON A WALL -- formula silent)"""
    ps=pairing(lam)
    if any(p==0 for p in ps): return None
    return sum(1 for p in ps if p<0)

# ---------------------------------------------------------------- GATES
head("PART B -- GATES. All three must pass or nothing downstream is read.")
print("  GATE 1 (structure): my derived data must MATCH F638 exactly.")
g1a = (rho==(F(5,2),F(3,2),F(1,2)))
g1b = (len(noncompact)==5)
spinor=lambda c: (F(c), F(1,2), F(1,2))
ps=pairing((F(0),F(1,2),F(1,2)))   # c=0 spinor: F638 says {1/2,3/2,5/2,7/2,9/2}
g1c = (ps==[F(1,2),F(3,2),F(5,2),F(7,2),F(9,2)])
print("     rho = (5/2,3/2,1/2)?              %s  (got (%s,%s,%s))"%("YES" if g1a else "NO",*rho))
print("     #noncompact = 5 = n_C?            %s"%("YES" if g1b else "NO"))
print("     spinor pairings at c=0 = F638's?  %s  (got %s)"%("YES" if g1c else "NO",[str(p) for p in ps]))
print("     six chambers, thresholds at c = -1/2,-3/2,-5/2,-7/2,-9/2:")
g1d=True
for c,expq in [(F(0),0),(F(-1),1),(F(-2),2),(F(-3),3),(F(-4),4),(F(-5),5)]:
    q=q_of(spinor(c)); ok=(q==expq); g1d=g1d and ok
    print("        c = %-4s -> q = %s (expect %d)  %s"%(c,q,expq,"ok" if ok else "*** NO ***"))
gate1 = g1a and g1b and g1c and g1d

print("\n  GATE 2 (must-reproduce): the SCALAR case's known chamber.")
print("     Trivial K-type lam = (c,0,0). Known answer: for c positive the space is the")
print("     holomorphic discrete series / Bergman sector -> q = 0.")
g2=True
for c in [F(1),F(3),F(1,2)]:
    q=q_of((c,F(0),F(0))); ok=(q==0); g2=g2 and ok
    print("        scalar c = %-4s -> q = %s  %s"%(c,q,"ok (holomorphic)" if ok else "*** NO ***"))
sc=pairing((F(0),F(0),F(0)))
print("     scalar thresholds (from pairings at c=0): %s -> at c = -1,-2,-5/2,-3,-4"%[str(p) for p in sc])
print("     *** NOTE THEY DIFFER FROM THE SPINOR THRESHOLDS -- the instrument DISTINGUISHES the")
print("         two K-types, which is exactly what yesterday's lesson demands. ***")

print("\n  GATE 3 (must-reject): a DELIBERATELY WRONG rho must fail to reproduce F638.")
rho_bad=(F(3,2),F(5,2),F(1,2))    # e1,e2 entries swapped
def pairing_bad(lam):
    lp=tuple(lam[k]+rho_bad[k] for k in range(3))
    return sorted(sum(lp[k]*b[k] for k in range(3)) for b in noncompact)
psb=pairing_bad((F(0),F(1,2),F(1,2)))
g3 = (psb!=[F(1,2),F(3,2),F(5,2),F(7,2),F(9,2)])
print("     wrong rho = (3/2,5/2,1/2) gives pairings %s"%[str(p) for p in psb])
print("     differs from F638's table? %s -- the gate CAN fail, so passing it means something."%("YES" if g3 else "NO"))

allg = gate1 and g2 and g3
print("\n  *** GATES: %s ***"%("ALL PASS" if allg else "FAIL -- INSTRUMENT NOT VALID, nothing below binds"))
if not allg: raise SystemExit

# ---------------------------------------------------------------- consistency with my own 4777
head("PART C -- consistency point with my own toy 4777 (July)")
print("  q=0 chamber: all 4 spinor components holomorphic -> net chirality (+1)^0 * 4 = +4.")
print("  Matches 4777's net +-4 (holomorphic projection IS chiral). Consistency, NOT a second vote --")
print("  4777 and F638 share the holomorphic-sector input. One fact, noted once.")

# ---------------------------------------------------------------- PRE-REGISTRATION
head("PART D -- ★★★ PRE-REGISTRATION. Written before ANY c-value exists. Binding.")
print("""  P1. THE INVARIANT IS RELATIVE PARITY, NOT ABSOLUTE SIGN. (-1)^q gives a sign, but WHICH
      sign is called 'left-handed' is a CONVENTION (a coordinate). The testable claim is:
         *** q(c_doublet) and q(c_singlet) have OPPOSITE PARITY, for every SM pair. ***
      The absolute L/R naming is pinned ONCE, by ONE fermion, and then FORCED for all others.
      Nobody gets to flip the convention per-fermion. One flip, applied globally, is the only
      freedom -- and it cannot rescue a wrong RELATIVE parity anywhere.

  P2. WIN CONDITION (all must hold):
      (a) every L-doublet c lands in one parity class, every R-singlet c in the other;
      (b) this holds for EVERY generation and EVERY sector supplied (quarks and leptons);
      (c) no supplied c lands ON a wall (see P4).
      PARTIAL SORTING IS A FAIL. If 11 of 12 sort and one does not, the result is FAIL with
      the count reported -- not 'mostly confirms'. (K1809 standard.)

  P3. LOSS CONDITIONS, all informative, named now:
      (i)  all fermions in one parity class        -> NO chirality split. Mechanism fails for SM.
      (ii) mixed within the doublets (or singlets) -> the c-assignment and F638 cannot both stand.
      (iii) any c ON a wall                        -> see P4.

  P4. WALLS. If a supplied c is EXACTLY a threshold (-1/2, -3/2, -5/2, -7/2, -9/2), q is
      UNDEFINED -- a vanishing pairing means the concentration theorem's hypothesis fails.
      *** THE INSTRUMENT RETURNS 'ON WALL: NO ANSWER', NEVER A CHOICE. *** This is pre-registered
      precisely because half-integer c-values are LIKELY in this corpus, and a wall must not be
      quietly rounded into whichever chamber flatters the outcome.

  P5. CIRCULARITY GUARD (Cal's gate, restated here so the instrument carries it): c-values are
      accepted ONLY with a stated derivation from quantum numbers that exist independently of
      chirality. A c derived from 'which chirality the SM has' is REFUSED as input -- the
      instrument will not run on it.

  P6. SCOPE: this instrument evaluates F638's formula. It does NOT certify the formula's
      applicability at spinor lambda beyond what F638 proved -- in particular the EHW caveat
      (R81 Section 2: everything downstream of split rank 1 is one step from primary) does not
      touch F638's own theorem, which is Schmid/HP concentration, a different citation.""")

# ---------------------------------------------------------------- the callable
head("PART E -- THE CALLABLE (for when Lyra's values arrive)")
def chirality_check(fermions):
    """fermions: list of (name, c, kind) with kind in {'L-doublet','R-singlet'}.
       Returns verdict per P1-P4. NO DEFAULTS."""
    rows=[]
    for name,c,kind in fermions:
        q=q_of(spinor(F(c)))
        rows.append((name,F(c),kind,q))
    walls=[r for r in rows if r[3] is None]
    if walls:
        return rows,"ON WALL: NO ANSWER for %s -- formula silent (P4)"%", ".join(r[0] for r in walls)
    dpar={r[3]%2 for r in rows if r[2]=='L-doublet'}
    spar={r[3]%2 for r in rows if r[2]=='R-singlet'}
    if len(dpar)>1 or len(spar)>1:
        return rows,"FAIL (P3.ii): mixed parity within a kind"
    if dpar==spar:
        return rows,"FAIL (P3.i): doublets and singlets share parity -- no chirality split"
    return rows,"WIN (P2): all doublets one parity, all singlets the other, no walls"
print("  chirality_check([(name, c, kind), ...]) defined. Demo on PLACEHOLDER inputs")
print("  (labelled as such -- these are NOT predictions, they exercise the three verdict paths):")
for demo,label in [([("dL",-1,'L-doublet'),("uR",0,'R-singlet')],"opposite chambers"),
                   ([("dL",0,'L-doublet'),("uR",1,'R-singlet')],"same chamber"),
                   [( [("dL",F(-1,2),'L-doublet'),("uR",0,'R-singlet')],"on a wall")][0]]:
    rows,v=chirality_check(demo)
    print("     %-18s -> %s"%(label,v))

head("VERDICT")
print(" (1) Root data DERIVED from scratch and it MATCHES F638 exactly: rho=(5/2,3/2,1/2),")
print("     5 noncompact roots, spinor pairings c+{1/2,3/2,5/2,7/2,9/2}, six chambers. The July")
print("     handoff 'verify the roots' is now DONE, 33 days late, as the instrument's Gate 1.")
print(" (2) Must-reproduce PASSED (scalar q=0 holomorphic) and must-reject PASSED (wrong rho")
print("     produces a different table -- the gate can fail).")
print(" (3) ★ The scalar and spinor THRESHOLDS DIFFER (-1,-2,-5/2,-3,-4 vs half-integers).")
print("     The instrument distinguishes the K-types -- yesterday's disease cannot ride through it.")
print(" (4) PRE-REGISTERED: relative parity is the invariant; partial sorting is FAIL; walls")
print("     return NO ANSWER, never a choice; circular c-values are refused as input.")
print(" (5) NO c-value evaluated. The instrument waits on Lyra, per R81.")
print("\n *** Instrument + gates + pre-registration = the R81 deliverable. Ready for values. ***")
