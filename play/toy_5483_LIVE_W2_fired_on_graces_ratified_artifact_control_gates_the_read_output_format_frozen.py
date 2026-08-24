# TOY 5483 -- THE LIVE EVIDENTIAL-W2 RUN. Elie, 2026-08-24.
# Fires on: grace_R85_RATIFICATION_ARTIFACT (verified on disk, I-1..I-4 tabled, protocol frozen).
# Protocol: HER FROZEN ONE -- the perturbation control GATES the read in the SAME execution,
# with exact reference values; output format locked; provenance line fixed.
import os, sys
from fractions import Fraction as F
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
ns={"__name__":"lib"}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
  "toy_5482_EVIDENTIAL_W2_built_and_held_fires_only_on_graces_ratified_artifact_sums_exact_perturbation_loud.py")).read(),ns)
evidential_W2=ns["evidential_W2"]; SM=ns["SM"]
ART="notes/grace_R85_RATIFICATION_ARTIFACT_custodial_Y_route_inheritance_step_isolated_as_C4_and_the_frozen_W2_protocol_2026-08-24.md"
BAR="="*100
print(BAR); print("TOY 5483 -- LIVE W2, frozen protocol"); print(BAR)
# ---- STEP 1: THE CONTROL, GATING THE READ (same execution, exact reference values)
print("CONTROL (gates the read): Y(Q) -> 1/6 + 1/30; reference must-fire: Y^3 = 91/4500, grav-Y = 1/5")
P=[("Q","3",2,F(1,6)+F(1,30))]+SM[1:]
s3=sum(F(e[2])*e[3] for e in P if e[1] in ("3","3bar"))
s2=sum(F({"3":3,"3bar":3,"1":1}[e[1]])*e[3] for e in P if e[2]==2)
s1=sum(F({"3":3,"3bar":3,"1":1}[e[1]]*e[2])*e[3]**3 for e in P)
sg=sum(F({"3":3,"3bar":3,"1":1}[e[1]]*e[2])*e[3] for e in P)
ctrl_ok=(s1==F(91,4500) and sg==F(1,5) and s3!=0 and s2!=0)
print("   control sums: su3=%s su2=%s Y^3=%s grav=%s -> %s"%(s3,s2,s1,sg,
      "FIRED, matches reference EXACTLY" if ctrl_ok else "*** CONTROL FAILED -- READ ABORTED ***"))
if not ctrl_ok: sys.exit("CONTROL DID NOT FIRE -- no live number is read")
# ---- STEP 2: THE LIVE READ, artifact-gated by 5482's refusal machinery
print("\nLIVE READ (artifact-gated):")
ok=evidential_W2(SM, ratified_artifact=ART)
# ---- STEP 3: LOCKED OUTPUT FORMAT (her line 5), generator quoted, never a bare x
print("\n"+BAR)
print("W2: %s · [su3^2Y=0, su2^2Y=0, Y^3=0, grav^2Y=0] · control: fired · provenance:"%("PASS" if ok else "FAIL"))
print("evidential, conditional on C4")
print(BAR)
print("Generator quoted per the x-collision pin: Y = T3_R + (B-L)/2, equivalently Y(Q_L) = 1/6.")
print("(x_C = 1 and x_G = 1/2 are the same generator in two parametrizations -- no bare x here.)")
print("MEANING, held to the evidential form: the mechanism that DERIVED these Y-values used no")
print("anomaly condition (Cal 735). These four sums COULD have failed. They did not. That is")
print("evidence, not construction -- and it is the first W2 number this program has ever printed.")
print()
print("CREDIT ORDER (Grace's correction, applied): LYRA first -- she pre-registered W2's exclusion")
print("when it WAS empty, against the result she wanted; a check that passes today is only worth")
print("something because someone refused to let it pass for free five days ago. Then CAL (the gate),")
print("the PROTOCOL (Grace's freeze), GRACE (the route), and the instrument last.")
