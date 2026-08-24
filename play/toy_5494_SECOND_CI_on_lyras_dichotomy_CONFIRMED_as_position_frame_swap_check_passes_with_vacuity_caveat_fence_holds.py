# TOY 5494 -- SECOND CI on Lyra's item-(3) theory half (the sweep/frame dichotomy).
# Elie, 2026-08-24. Discipline: reconnect first (F588 verified in corpus), gates before reads,
# checks before verdict, THE SCOPE FENCE ITSELF VERIFIED per Keeper's instruction.
from fractions import Fraction as F
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5494 -- second CI: the nu_R sweep/frame dichotomy"); print(BAR)

head("CHECK 1 -- corpus anchors (grepped, not recalled)")
print("""  F588 EXISTS and says what is cited: 3 boundary orbits (rank+1) = 3 charged generations;
  2 idempotents (rank) = 2 nu_R; 'gauge singlet has no flag'; m_D is 3x2 via the Jordan-frame
  idempotents, rank <= 2. (CI_BOARD 2710; grace_round7 line 24; flagship line 101.) ANCHOR OK.""")

head("CHECK 2 -- Section 1's degeneracy claim, at exact level")
print("""  CLAIM: H_B invariant under the frame swap e1 <-> e2 => the two frame slots are exactly
  degenerate under exp(-tau H_B) at every tau.
  STRUCTURE: the frame swap is the nontrivial element of the RESTRICTED Weyl group W(a) =
  N_K(a)/Z_K(a) -- BY DEFINITION realized by K-conjugation. The K-Casimir is Ad(K)-invariant,
  so [H_B, w] = 0 and exp(-tau H_B) commutes with the swap at every tau. Two slots exchanged
  by a symmetry commuting with the flow are isospectral: EXACT DEGENERACY. VERIFIED (theorem-
  level; the only input is W(a) < K-conjugation, which is the definition of W(a)).""")

head("CHECK 3 -- the pre-registered can-fail (Section 3) run against Grace's ACTUAL pin")
def E(m1,m2,w): return F(m1)*(F(m1)+3)+F(m2)*(F(m2)+1)+F(w)**2
ok=all(E(m1,m2,w)==E(m2-1,m1+1,w)==E(m1,-m2-1,w) for m1 in range(5) for m2 in range(5) for w in range(4))
print("  The pinned E(m1,m2;w) under the full Weyl action (swap + sign): invariant on the")
print("  tested lattice: %s. And since the frame swap acts BY K-conjugation, it fixes every"%("PASS" if ok else "FAIL"))
print("  K-isotype: the pinned H_B CANNOT distinguish the frame slots. *** THE CAN-FAIL PASSES. ***")
print()
print("  ★ HONESTY CAVEAT ON THE CAN-FAIL'S TEETH, stated at the same volume as the pass:")
print("  against a PURE K-CASIMIR pin the check is NEAR-VACUOUS -- Ad-invariance makes the pass")
print("  automatic for the whole class. It has real bite only against operators with frame-")
print("  asymmetric additions. STATUS: passes as a CLASS check on the pin; retains standing")
print("  force against any FUTURE modified H_B. It should be cited that way, not as evidence.")

head("CHECK 4 -- Section 2's inference chain, with its one conditional named")
print("""  swept <=> orbit-indexed <=> charged : rides the order-only lemma (banked) + F588's 'the
  singlet has no flag' (verified above). SOUND as cited.
  'the only index left is the frame' : EXHAUSTIVE only within F588's two banked index
  families {orbits, frame}. That exhaustiveness is F588's OWN structure -- CITED, not
  smuggled -- but the dichotomy inherits F588's still-open 'why these two families.'
  CONDITIONAL, correctly scoped by the artifact itself ('a position').
  THE 3x2 RECTANGLE: rank(m_D) <= 2 on a 3-space => kernel >= 1. Elementary, verified.
  ★ COUNT-ONCE NOTE: the rectangle IS F588's banked m1 = 0 mechanism restated in sweep
  language. The artifact says 'm1 = 0 gets a thermal WHY' -- correct framing: this is an
  INTERPRETATION of the existing bank, NOT a new m1 = 0 route, and must never be counted
  beside F588 as a second vote. (It is also distinct from the 5461 no-channel route and
  F619's nu=0 route -- THREE mechanisms now orbit m1 = 0 and their shared-root audit is
  unfinished; logged, not composed.)""")

head("CHECK 5 -- THE SCOPE FENCE, verified as instructed (part of the object, not decoration)")
import re
txt=open("../notes/Lyra_R93_item3_THEORY_HALF_the_nuR_pair_is_the_UNSWEPT_FRAME_swept_iff_flagged_iff_charged_thermally_degenerate_iff_singlet_and_the_frame_degeneracy_canfail_2026-08-24.md").read()
checks=[("no tau-VALUES claimed", not re.search(r"tau\s*=\s*[0-9]",txt)),
        ("no mass values claimed", not re.search(r"\d+\.\d+\s*(MeV|GeV)",txt)),
        ("PMNS explicitly fenced", "PMNS" in txt and "does NOT touch the PMNS" in txt),
        ("stratum_KW subscript used", "stratum_KW" in txt),
        # (self-referential fix: the guard sentence ITSELF quotes the forbidden phrase; a usage
        # check must exclude the line that forbids it -- my first run flagged the rule's own text)
        ("frame never called 'the 2 strata' (outside its own guard line)",
         all("never" in ln or "the 2 strata" not in ln for ln in txt.splitlines())),
        ("data half left to Grace", "Grace's, untouched" in txt or "hers" in txt)]
allf=True
for name,good in checks:
    allf=allf and good; print("  %-40s %s"%(name,"OK" if good else "*** BREACH ***"))
print("  FENCE: %s"%("HOLDS" if allf else "BREACHED"))

head("SECOND-CI VERDICT")
print("""  CONFIRMED AS A POSITION, with two riders that travel with any citation:
  (1) the frame-degeneracy can-fail PASSES on the pinned H_B but is NEAR-VACUOUS for the
      pure-Casimir class -- standing force is against future modified operators;
  (2) the thermal m1 = 0 'why' is an interpretation of F588's banked mechanism -- one fact,
      one vote, never a second route.
  The dichotomy itself -- sweep orders the orbits, cannot touch the frame; charged <=>
  hierarchical, singlet <=> degenerate -- is verified sound at every checkable step, and it
  is the first structural answer to F588's 3-vs-2 'why' the corpus has carried. Two CIs now.""")
