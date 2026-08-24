# TOY 5482 -- EVIDENTIAL W2, built on Cal's PASS (section 735), HELD until Grace's artifact
# carries his four named inputs. Elie, 2026-08-24.
#
# DESIGN CONTRACT (as committed to Keeper in advance):
#  - a SEPARATE AUDITED FUNCTION. The Ylabel wrapper in toy 5480 is UNTOUCHED; this file is the
#    ONE authorized reader of Y.v for arithmetic, and says so. The 16th-collision guard stands
#    everywhere else.
#  - section-733 form: SUMS VANISH + PERTURBATION FAILS LOUDLY, both printed.
#  - REFUSES to run live without the ratified artifact's path resolving on disk (the caller
#    attests Cal's four inputs appear therein -- human-resolver pattern, stated).
#  - W2 re-entry is EVIDENTIAL, not construction-guaranteed: the mechanism that derived the
#    Y-values used NO anomaly condition (Cal 735), so these sums CAN fail and do not.
from fractions import Fraction as F
import os
BAR="="*100
CDIM={"3":3,"3bar":3,"1":1}
def evidential_W2(entries, ratified_artifact=None, fixture=False):
    """The four anomaly sums, exact. entries: (name,color,su2,Y) with Y a Fraction.
       AUDITED Y-ARITHMETIC SITE: the only place Y is summed in this program."""
    if not fixture:
        base="/Users/cskoons/projects/github/BubbleSpacetimeTheory/"
        if not (ratified_artifact and os.path.exists(base+ratified_artifact)):
            raise RuntimeError("REFUSED: evidential-W2 fires only on Grace's ratified artifact "
                               "(Cal 735's four inputs); path %r does not resolve"%ratified_artifact)
        print("ATTESTATION: caller states Cal's four inputs appear in %s"%ratified_artifact)
    else:
        print("*** FIXTURE MODE -- not a live W2 result, never quotable ***")
    s3=sum(F(e[2])*e[3] for e in entries if e[1] in ("3","3bar"))          # [SU(3)]^2 U(1)
    s2=sum(F(CDIM[e[1]])*e[3] for e in entries if e[2]==2)                 # [SU(2)]^2 U(1)
    s1=sum(F(CDIM[e[1]]*e[2])*e[3]**3 for e in entries)                    # U(1)^3
    sg=sum(F(CDIM[e[1]]*e[2])*e[3] for e in entries)                       # grav^2 U(1)
    rows=[("[SU(3)]^2 U(1)_Y",s3),("[SU(2)]^2 U(1)_Y",s2),("[U(1)_Y]^3",s1),("grav^2 U(1)_Y",sg)]
    for n,v in rows: print("   %-18s = %-8s %s"%(n,v,"VANISHES" if v==0 else "*** NONZERO ***"))
    return all(v==0 for _,v in rows)
SM=[("Q","3",2,F(1,6)),("u_c","3bar",1,F(-2,3)),("d_c","3bar",1,F(1,3)),
    ("L","1",2,F(-1,2)),("e_c","1",1,F(1))]
if __name__=="__main__":
    print(BAR); print("TOY 5482 -- evidential-W2: SELF-TESTS (live fire HELD)"); print(BAR)
    # T1: refusal without the artifact
    try: evidential_W2(SM,"notes/DOES_NOT_EXIST.md"); print("  [FAIL] T1")
    except RuntimeError as ex: print("  [PASS] T1 refusal: %s"%str(ex)[:70])
    # T2: sums vanish on the posted Y's (fixture mode, loudly labelled)
    print("  T2 sums on the posted hypercharges:")
    print("  [%s] T2 all four vanish"%("PASS" if evidential_W2(SM,fixture=True) else "FAIL"))
    # T3: perturbation fails LOUDLY -- Y_Q nudged by 1/30
    print("  T3 perturbation Y_Q -> 1/6 + 1/30:")
    P=[("Q","3",2,F(1,6)+F(1,30))]+SM[1:]
    print("  [%s] T3 perturbed spectrum FAILS all-vanish (loud)"%("PASS" if not evidential_W2(P,fixture=True) else "FAIL"))
    print(BAR)
    print("STATUS: BUILT AND HELD. Live invocation = evidential_W2(multiset, ratified_artifact=")
    print("<Grace's posted path>). Until that path resolves, this program has no W2 number.")
