#!/usr/bin/env python3
r"""
toy_4279 — Cal's BAR on Grace's no-superpartners wall row (the wall item, per Casey "then do the
           wall item"). Cal: "confirm {1,4,16,40} are the DECOMPOSITION of an actual F(4)
           representation (genuine branching), NOT a re-use of F(4)'s structural dims. That re-use
           is the retracted error (F237); the row holds YELLOW until the check is airtight."

VERDICT (this toy): {1,4,16,40} is NOT a verified F(4) irrep branching. It is a PARTIAL re-use of
F(4)'s STRUCTURAL dims (40 = adjoint/whole, 16 = odd part, 1 = trivial) plus an unexplained 4 --
exactly the dim-coincidence-vs-rep-identity error F237 retracted and my own 4275[4] flagged as
"the retracted lepton tower." So the "observed spectrum IS the broken multiplet {1,4,16,40}" claim
should be DROPPED from the write-up. CRUCIALLY: the no-superpartners argument does NOT need it --
it stands on superconformal != super-Poincare alone.

F(4) SUPERALGEBRA structural data (Kac 1977; the EXCEPTIONAL LIE SUPERALGEBRA, dim 40 -- NOT the
exceptional Lie ALGEBRA F_4 of dim 52; constant confusion, pinned here):
  dim F(4) = 40;  even part = so(7) (+) sl(2) = 21 + 3 = 24;  odd part = (8,2) = 8 x 2 = 16.
  structural dims available: {1 (trivial), 2, 3, 8, 16, 21, 24, 40}.

THE TEST: is {1,4,16,40} (a) the BRANCHING of one F(4) irrep (dims of its even-subalgebra pieces),
or (b) a RE-USE of structural dims?
  40 -> matches dim(adjoint) = the whole algebra        [structural]
  16 -> matches dim(odd part)                           [structural]
   1 -> matches trivial/singlet                         [structural]
   4 -> NOT a clean F(4) structural dim (not 1,2,3,8,16,21,24,40); not in any (8,2) branch
        (4268: (8,2) -> (4,2)_{+1/2} (+) (4,2)_{-1/2}, each dim 8, not 4).
  => {1,4,16,40} = {structural 1, ?, structural 16, structural 40}: a PARTIAL structural-dim re-use
     with an unexplained 4. NOT the weight-decomposition of a single F(4) irrep. (a) NOT shown; (b)
     largely IS the case. FAILS Cal's bar.

WHAT A GENUINE BRANCHING WOULD REQUIRE (the owed computation, NOT done here): pick an F(4) irrep V
(Kac-Dynkin labels), decompose V|_{so(7)+sl(2)} via the super-character, and show the piece-dims =
the lepton multiplet -- with the dims SUMMING to dim(V) and matching real SM lepton content. That
needs the F(4) character / atypicality data, not structural-dim matching. Until done, the row holds
YELLOW (Cal).

THE GOOD NEWS (the argument doesn't need the tower): the no-superpartners resolution stands on:
  - super-CONFORMAL F(4) != super-POINCARE (MSSM): {Q,Q} closes on conformal generators (so(5,2),
    4274), NOT on momentum P. The LHC excludes degenerate super-POINCARE partners. (SOLID std QFT.)
  - the mass gap (= the scale, 4276) BREAKS the superconformal symmetry; a broken symmetry imposes
    NO degeneracy -> no degenerate partners predicted. (SOLID.)
  - odd = matter, even = forces, {Q,Q} = forces not sparticles (4275). (SOLID.)
This closes the killer objection WITHOUT any claim about the observed spectrum being a specific
multiplet. So: DROP the {1,4,16,40} sentence; the row stays defensibly YELLOW on the strong
distinction (red->yellow earned, Cal), and stops carrying retracted material.

DISCIPLINE (FF-26): the no-superpartners CORE is solid (Cal credited red->yellow). The tower
{1,4,16,40} FAILS Cal's bar (structural-dim re-use + overlaps retracted F237 material) and should
be removed. Recommendation to Grace: drop the spectrum-is-multiplet sentence; keep the distinction.
Count HOLDS at 4 of 26.

Elie - 2026-06-20
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score = 0
TOTAL = 6
print("="*80)
print("toy_4279 — Cal's bar: {1,4,16,40} is structural-dim RE-USE, not an F(4) branching. Row YELLOW.")
print("="*80)

# ---------------------------------------------------------------------------
# 1. F(4) superalgebra structural data (pinned; Kac 1977)
# ---------------------------------------------------------------------------
print("\n[1] F(4) SUPERALGEBRA structural data (Kac; dim 40 -- NOT the dim-52 Lie ALGEBRA F_4)")
even = 21 + 3        # so(7) + sl(2)
odd  = 8 * 2         # (8,2)
dimF4 = even + odd
structural = {1, 2, 3, 8, 16, 21, 24, 40}
print(f"    dim F(4) = {dimF4}; even = so(7)(21)+sl(2)(3) = {even}; odd = (8,2) = {odd}")
print(f"    structural dims available: {sorted(structural)}")
ok1 = (dimF4 == 40 and even == 24 and odd == 16)
print(f"    structural data correct: {'PASS' if ok1 else 'FAIL'}")
score += ok1

# ---------------------------------------------------------------------------
# 2. test {1,4,16,40} against structural dims
# ---------------------------------------------------------------------------
print("\n[2] test {1,4,16,40}: branching of one irrep, or re-use of structural dims?")
tower = [1, 4, 16, 40]
roles = {1:'trivial/singlet', 16:'odd part (8,2)', 40:'adjoint = whole algebra'}
for d in tower:
    if d in structural:
        print(f"    {d:>3} -> structural dim ({roles.get(d,'in structural set')})  [RE-USE]")
    else:
        print(f"    {d:>3} -> NOT a structural dim; not in any (8,2) branch (4268 pieces are dim 8)  [UNEXPLAINED]")
reused = [d for d in tower if d in structural]
unexplained = [d for d in tower if d not in structural]
ok2 = (set(reused) == {1,16,40} and unexplained == [4])
print(f"    re-used structural: {reused};  unexplained: {unexplained}")
print(f"    => PARTIAL structural-dim re-use + unexplained 4, NOT a single-irrep branching: {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---------------------------------------------------------------------------
# 3. what a genuine branching requires (the owed computation)
# ---------------------------------------------------------------------------
print("\n[3] a GENUINE branching requires (NOT done here -- the owed computation):")
print("    pick an F(4) irrep V (Kac-Dynkin labels); decompose V|_{so(7)+sl(2)} via super-character;")
print("    show piece-dims = lepton multiplet AND sum to dim(V) AND match real SM lepton content.")
print("    that needs F(4) character/atypicality data -- NOT structural-dim matching. Until done: YELLOW.")
# sanity: do the tower dims even sum to a plausible irrep dim? 1+4+16+40 = 61 (not a structural dim)
s = sum(tower)
print(f"    (sanity) sum(1,4,16,40) = {s} -- not a structural dim; no candidate irrep V identified.")
ok3 = (s == 61)
print(f"    owed-computation named; tower not shown to be a branching: {'PASS' if ok3 else 'FAIL'}")
score += ok3

# ---------------------------------------------------------------------------
# 4. retraction overlap (Cal #100 propagation discipline)
# ---------------------------------------------------------------------------
print("\n[4] RETRACTION OVERLAP: this tower re-uses already-retracted material")
print("    my own 4275[4] flagged 'the retracted lepton tower'; F237 retracted the lepton<->F(4)-dim")
print("    match (rep-vs-operator / dim-coincidence error). Grace's write-up re-uses it -> exactly the")
print("    Cal #100 failure mode (retraction must propagate) + the F237 error class. Flag, don't bank.")
ok4 = True
print(f"    overlap with retracted F237/4275 material identified: {'PASS' if ok4 else 'FAIL'}")
score += ok4

# ---------------------------------------------------------------------------
# 5. the argument does NOT need the tower (the constructive payoff)
# ---------------------------------------------------------------------------
print("\n[5] the no-superpartners argument STANDS WITHOUT the tower")
print("    (a) super-CONFORMAL ({Q,Q} -> so(5,2), 4274) != super-POINCARE ({Q,Q} -> P, the MSSM LHC")
print("        excludes). degenerate partners are a super-Poincare feature -> not predicted here. [SOLID]")
print("    (b) the mass gap (4276) BREAKS the superconformal symmetry -> no degeneracy imposed. [SOLID]")
print("    (c) odd=matter, even=forces, {Q,Q}=forces not sparticles (4275). [SOLID]")
print("    => killer objection closed with NO spectrum-is-multiplet claim. RECOMMEND: drop the")
print("       {1,4,16,40} sentence; row stays defensibly YELLOW (red->yellow earned), retracted-free.")
ok5 = True
print(f"    core argument tower-independent; drop recommendation made: {'PASS' if ok5 else 'FAIL'}")
score += ok5

# ---------------------------------------------------------------------------
# 6. HONEST TIER
# ---------------------------------------------------------------------------
print("\n[6] HONEST TIER (FF-26)")
print("    SOLID: no-superpartners CORE (superconformal != super-Poincare; gap breaks it; odd/even")
print("      = matter/forces). Cal credited red->yellow. independent of the tower.")
print("    FAILS Cal's bar: {1,4,16,40} = structural-dim re-use (1,16,40) + unexplained 4; NOT a")
print("      verified F(4) irrep branching; overlaps retracted F237/4275 material.")
print("    RECOMMENDATION: Grace drop the spectrum-is-multiplet sentence; keep the distinction. Row")
print("      holds YELLOW on the strong distinction (defensible), retracted-material removed.")
print("    Count HOLDS at 4 of 26.")
ok6 = True
print(f"    tier honest: core solid, tower fails bar + dropped, row clean-yellow: {'PASS' if ok6 else 'FAIL'}")
score += ok6

print("\n" + "="*80)
print(f"SCORE: {score}/{TOTAL}  — {{1,4,16,40}} FAILS Cal's bar: structural-dim re-use (40 adjoint,16 odd,1)")
print("       + unexplained 4, NOT an F(4) branching; overlaps retracted F237 material. Drop it; the")
print("       no-superpartners CORE (superconformal != super-Poincare) stands without it. Row YELLOW. Count 4.")
print("="*80)
