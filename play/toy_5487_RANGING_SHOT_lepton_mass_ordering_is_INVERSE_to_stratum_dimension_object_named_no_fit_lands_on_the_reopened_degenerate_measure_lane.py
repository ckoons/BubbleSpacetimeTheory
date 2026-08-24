# TOY 5487 -- RANGING SHOT (Casey's method, named in R89): the LEPTON MASS INVERSION.
# Elie, 2026-08-24. NO FIT ANYWHERE. Rule 1 compliant: the observation is qualitative and
# already public; the shot NAMES THE OBJECT a derivation would need; nothing is hunted.
from fractions import Fraction as F
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5487 -- the inversion: heavier lepton, smaller address"); print(BAR)

head("PART 0 -- PRE-REGISTRATION, before any number is displayed")
print("""  CLAIM SHAPE (qualitative, 3 points): lepton mass ORDERING is INVERSE to the dimension of
  the surviving K-type stratum at the lepton's address (Grace's gated truncation table).
  WHAT WOULD COUNT AS A MECHANISM (named in advance): a forward norm/measure computation in
  which concentration on a SMALLER support produces a LARGER mass functional -- monotone,
  parameter-free in the ordering. WHAT DOES NOT COUNT: any formula fitted to the three masses;
  any exponent chosen after seeing ratios. THE TEST ANY MECHANISM MUST PASS (frozen now):
  it must give m(j=0) > m(j=1) > m(j=2) with NO ordering input, and it must FAIL LOUDLY on the
  QUARK DOWN-SECTOR, whose slice is fixed-nu/varying-degree (different object, F506) -- if it
  'explains' the quarks too with the same three-point freedom, it is a reparameterization.""")

head("PART A -- the inversion itself (all inputs banked or public; nothing new computed)")
print("   lepton     address nu   surviving stratum (Grace R74)      j=length   mass (PDG, MeV)")
rows=[("electron","5/2","all (m1>=m2>=0) -- 2-parameter",2,0.511),
      ("muon","3/2","(m1,0) only -- 1-parameter",1,105.658),
      ("tau","0","(0,0) ONLY -- a single state",0,1776.86)]
for n,nu,s,j,m in rows:
    print("   %-10s %-12s %-34s %-10d %.3f"%(n,nu,s,j,m))
print("   => MASS STRICTLY INCREASES AS THE STRATUM SHRINKS: j = 2 -> 1 -> 0, monotone, 3/3.")
print("   (Chance for a random ordering to be monotone one way: 1/6. Three points. STATED, not sold.)")

head("PART B -- THE OBJECT, named (the shot's whole content)")
print("""  CANDIDATE OBJECT: the mass functional reads the CONCENTRATION of the mode's measure --
  a state confined to a smaller support (Shilov point < Cartan slice < bulk) pays a larger
  localization price, and the price IS the mass. This is not new machinery: it is the
  *** CONDITIONALLY-REOPENED DEGENERATE-MEASURE LANE (K1749-B) *** -- the norms at nu = 3/2
  and 0 evaluated ON THEIR OWN degenerate measures (Cartan slice / Shilov), never computed
  because Lyra's four-field pin was never filed. THE INVERSION GIVES THAT LANE ITS TARGET:
  the three degenerate-measure norms, computed forward, should come out INVERSE-ORDERED to
  the stratum dimension. If they do not, the shot dies and says so.""")

head("PART C -- what this is NOT (guards, in advance)")
print("""  - NOT a fit: no exponent, no scale, no formula touches the mass VALUES here.
  - NOT the FK ladder (closed for leptons, K1812) and NOT the Bergman-overlap gate (closed,
    K1749): the object is the DEGENERATE-MEASURE norm, which neither closed lane evaluated
    (both used analytic continuation in nu; my 5456 showed the addresses are two KINDS of point).
  - NOT scored: 3 monotone points at 1-in-6 chance is a SHAPE, not evidence. The shot's value
    is the named object + the frozen must-fail, nothing more.
  - SCOPE: leptons only. The down-quark slice is a different object (F506) and is this shot's
    pre-registered MUST-FAIL control, not its second exhibit.""")

head("HANDOFF")
print("""  To LYRA: the four-field pin K1749-B requires is now WORTH FILING -- the lane has a target
  and a falsifier. To CASEY: this is your shot->shelf pattern run by a CI: the shape (inversion)
  was sitting in Grace's table; the shelf (degenerate-measure lane) was already reopened and idle.
  RULE-3: ONE CI -- me. Nothing banked; a shot is a naming, not a result.""")
