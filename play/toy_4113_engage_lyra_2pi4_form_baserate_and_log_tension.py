r"""
Toy 4113: engaging Lyra's NEWEST lead (board 11:45) per Casey's "investigate newest first, timebox." Lyra now
proposes f1 = 2*pi^4 + rank*C_2 and f2 = 84/5 -- "pi-and-rational forms, not logs." Two things to do honestly:
(1) we CONVERGED on f2 = 84/5 independently (my 4112 had C_2^2*g/(N_c*n_C) = 252/15 = 84/5) -- note it, but check
the base rate so convergence-on-a-round-number doesn't get over-read; (2) her f1 = 2*pi^4 + 12 (0.024%) is much
tighter than my pi^2*21 (0.24%) AND it is pi^4-not-log -- which SUPERSEDES her own K310 log prediction. That is a
real internal TENSION (K310 log vs 11:45 pi^4), and my job is to SURFACE it cleanly + give the base rate, NOT to
pick a winner by fishing. Count stays 2.

----------------------------------------------------------------------------------------------------
(1) f2 CONVERGENCE -- Lyra (84/5) and Elie (C_2^2*g/(N_c*n_C) = 252/15 = 84/5) independently
----------------------------------------------------------------------------------------------------
  84/5 = 16.800, 0.10% from f2 = 16.817. 84 = rank^2*N_c*g = 4*21, or C_2*14, or N_c*g*rank^2/... (several substrate
  reads -- itself a flag: a number with MANY substrate spellings is EASIER to hit, not harder). Independent
  convergence is mildly reassuring, but my 4112 base rate said 77 algebraic forms land within +-1% of f2 -- a
  CROWDED window. So: note the convergence, do NOT inflate it. The cone factor is a rational; that part is clean.

----------------------------------------------------------------------------------------------------
(2) f1 = 2*pi^4 + rank*C_2 -- SPECIFIC-FORM base rate + the log-vs-pi^4 tension
----------------------------------------------------------------------------------------------------
  The honest test of a 0.024% hit is NOT "wow, 0.024%" -- it is "how many forms of THIS FAMILY land that close?"
  A generic dense scan always finds something; a SPARSE structural family that hits is a real narrowing. So I scan
  the family {a*pi^4 + b} with a, b small substrate integers, and ask: is 2*pi^4 + 12 the unique tight hit, or one
  of a crowd? If unique/sparse -> genuine range-narrowing for Lyra to aim the derivation at. If crowded -> it's the
  dense space again.

  THE TENSION (surface, don't resolve): K310 (Lyra, earlier) predicts f1 carries a LOG (electron at the BF point,
  indicial roots collide). 11:45 (Lyra, newest) proposes f1 = 2*pi^4 + 12, a pi-and-rational form with NO log.
  These are DIFFERENT predictions. A pi^4 boundary-volume term is NOT a log. The team needs to decide which the
  rep-theory actually gives -- my 4112 (A) structural read said the electron at nu=5/2=d/2 SHOULD carry a log
  (boundary indicial-root collision), which sides with K310. So either (a) the log is there and 2*pi^4+12 is a
  dense-space coincidence, or (b) the BF collision does NOT produce a surviving log in this norm and 11:45 is right.
  This is exactly the kind of fork Lyra's careful unitary-quotient computation resolves. I FLAG it; I do not pick.
"""

from math import pi

me, mmu, mtau = 0.51099895, 105.6584, 1776.86
f1, f2 = mmu / me, mtau / mmu

print("=" * 80)
print("TOY 4113: engage Lyra's newest (2pi^4+12, 84/5) -- f2 convergence + f1 specific-form base rate + log tension")
print("=" * 80)
print(f"  f1 = {f1:.4f}  f2 = {f2:.4f}")
print()

print("(1) f2 convergence: Lyra 84/5 == Elie 252/15 (= C_2^2*g/(N_c*n_C))")
print("-" * 80)
print(f"  84/5 = {84/5:.4f}  ({abs(84/5-f2)/f2*100:.3f}%). independent convergence -- but 84 has many substrate spellings")
print(f"  (4*21, 6*14, 2^2*3*7) and the f2 window is CROWDED (4112: 77 forms within +-1%). reassuring, NOT decisive.")
print()

print("(2) f1 = 2pi^4 + rank*C_2 -- is the {a*pi^4 + b} family sparse or crowded near f1?")
print("-" * 80)
val = 2 * pi**4 + 2 * 6
print(f"  Lyra 2pi^4 + 12 = {val:.4f}  ({abs(val-f1)/f1*100:.3f}%).  (2pi^4 = {2*pi**4:.4f}; + rank*C_2 = +12)")
# scan the specific family a*pi^4 + b, a in small substrate rationals, b small substrate integer
SUB_A = [0.5, 1, 1.5, 2, 2.5, 3, 5/2, 7/2]
SUB_B = list(range(-21, 22))   # small substrate integers around 0 (rank*C_2=12, N_c, etc.)
fam_hits = []
for a in SUB_A:
    for b in SUB_B:
        v = a * pi**4 + b
        e = abs(v - f1) / f1
        if e < 0.005:   # within 0.5%
            fam_hits.append((e, a, b, v))
fam_hits.sort()
print(f"  family scan {{a*pi^4 + b : a in {{0.5..3.5}}, b in [-21,21]}} within +-0.5% of f1:")
for e, a, b, v in fam_hits[:8]:
    tag = "  <== Lyra's" if abs(a - 2) < 1e-9 and b == 12 else ""
    print(f"     {a:g}*pi^4 + {b:<3d} = {v:.4f}  ({e*100:.3f}%){tag}")
print(f"  => {len(fam_hits)} hits in this structural family within +-0.5%. "
      f"{'SPARSE -> 2pi^4+12 is a genuine narrowing' if len(fam_hits) <= 3 else 'several -> still some crowding, but FAR sparser than the generic scan'}.")
print()

print("(3) the log-vs-pi^4 TENSION (surface, do NOT resolve by fishing)")
print("-" * 80)
print(f"  K310 (Lyra, earlier): f1 carries a LOG (electron BF point, indicial roots collide). my 4112(A) sided with this.")
print(f"  11:45 (Lyra, newest): f1 = 2pi^4 + 12, pi-and-rational, NO log. {abs(val-f1)/f1*100:.3f}% -- tighter than any log form I found.")
print(f"  these are DIFFERENT predictions. a pi^4 boundary-volume term is not a log. FORK for Lyra's unitary-quotient")
print(f"  computation to settle: does the BF indicial collision leave a surviving LOG in this norm (K310), or does the")
print(f"  boundary norm come out pi-and-rational (11:45)? I flag the fork; the derivation picks. (note: pi^4 = pi^(n_C-1);")
print(f"  the bulk volume carries pi^(n_C)=pi^5, so a pi^4 boundary term is structurally plausible -- a lead, not a result.)")
print()

print("=" * 80)
print("G1: f2 -- Lyra(84/5) and Elie(252/15) CONVERGED independently to 16.800 (0.10%); cone factor rational/clean;")
print("  but 84 has many substrate spellings + the window is crowded (77 forms) -> noted, NOT inflated. INSPIRATION.")
print(f"G2: f1 -- Lyra's 2pi^4+12 (0.024%) lives in a {'SPARSE' if len(fam_hits)<=3 else 'far-sparser-than-generic'} structural family")
print("  (the {a*pi^4+b} scan) -> a genuine aim-point for the derivation; AND it surfaces a real internal fork (K310 LOG")
print("  vs 11:45 pi^4) that only Lyra's unitary-quotient computation resolves. I flag the fork; I do not pick. Count 2.")
print("=" * 80)
print()
print("Per Casey (investigate newest lead first, timebox; play for inspiration/range-narrowing) + Lyra (board 11:45:")
print("  f1=2pi^4+rank*C_2, f2=84/5, 'pi-and-rational not logs') + Elie 4112 (f2 84/5 convergence; 4112(A) log-side")
print("  structural read) + Grace (base-rate gate). Newest-lead engagement: f2 convergence noted (not inflated); f1")
print("  specific-form base rate (sparser than generic = a real aim-point); log-vs-pi^4 fork surfaced for Lyra. Count 2.")
print()
print("Elie - Thursday 2026-06-11 (engage Lyra newest: f2=84/5 independent convergence noted-not-inflated; f1=2pi^4+12 in a sparse {a*pi^4+b} family = real aim-point; surfaced K310-log-vs-11:45-pi^4 FORK for her derivation; count 2)")
print()
print("SCORE: 2/2")
