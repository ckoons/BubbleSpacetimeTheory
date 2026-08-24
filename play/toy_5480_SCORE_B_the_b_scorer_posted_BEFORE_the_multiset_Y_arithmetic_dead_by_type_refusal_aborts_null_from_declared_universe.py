# TOY 5480 -- score_b, POSTED BEFORE Lyra's multiset lands (Keeper's request, so his blind
# six-check audit runs on code, not on my intentions). Elie, 2026-08-24.
#
# THE SIX BLIND CHECKS (Keeper, pre-registered before reading this file) AND WHERE EACH IS MET:
#  1 provenance = RESOLVABLE REFERENCE      -> require_provenance(): needs a T/F/K-number or a
#                                              notes/ filename; the bare word "banked" REFUSED.
#  2 W2 exclusion: Y sum-use dead, label-use alive
#                                           -> class Ylabel supports ONLY ==, unary -, hash;
#                                              +, *, abs, comparisons RAISE. Dead by WRAPPER +
#                                              REVIEW (the .v escape exists for W1/null internals;
#                                              audit verified no path sums Y) -- per Keeper A5,
#                                              not "impossible by type".
#  3 W1 conjugation is WHOLE-rep            -> conj(): color 3<->3bar AND Y -> -Y together
#                                              (SU(2) dims self-conjugate). Vector-like input
#                                              must FAIL W1 -- self-tested below.
#  4 refusal ABORTS, never filters          -> any bad entry raises RefusedInput; no code path
#                                              scores a remainder. Self-tested below.
#  5 nu^c separate BOTH directions          -> kind='nu_c' entries: excluded from the 5-count
#                                              AND excluded from extras-against. Self-tested.
#  6 null denominator from DECLARED universe-> null_p() computed from input's own universe
#                                              field; nothing hardcoded; printed beside k.

from fractions import Fraction as F
import re, math

class RefusedInput(Exception): pass

class Ylabel:
    """Hypercharge as a LABEL. Equality, negation, hash only. Arithmetic is DEAD (check 2)."""
    __slots__=("v",)
    def __init__(self,v): self.v=F(v)
    def __eq__(self,o): return isinstance(o,Ylabel) and self.v==o.v
    def __neg__(self): return Ylabel(-self.v)
    def __hash__(self): return hash(self.v)
    def __repr__(self): return "Y(%s)"%self.v
    def _dead(self,*a): raise RefusedInput("W2 EXCLUDED: anomaly arithmetic on Y is dead, not dormant")
    __add__=__radd__=__mul__=__rmul__=__sub__=__pow__=__abs__=__lt__=__le__=__gt__=__ge__=_dead

# A4 RESOLVED (idle-time add per clearance): form check + EXISTENCE check. An ID must occur in
# the registry or the notes tree; a notes/ path must exist on disk. Human-resolver caveat retired.
PROV=re.compile(r"\b([TFK]\d{2,4}|notes/[\w\-.]+\.md)\b")
import os,glob
_NOTES_DIR="/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes"
_CORPUS=None
def _corpus():
    global _CORPUS
    if _CORPUS is None:
        reg=os.path.join(_NOTES_DIR,"BST_AC_Theorem_Registry.md")
        txt=open(reg,encoding="utf-8",errors="replace").read() if os.path.exists(reg) else ""
        names=" ".join(os.path.basename(f) for f in glob.glob(_NOTES_DIR+"/*.md"))
        _CORPUS=txt+" "+names
    return _CORPUS
def _resolves(tok):
    if tok.startswith("notes/"):
        return os.path.exists(os.path.join(os.path.dirname(_NOTES_DIR),tok))
    return tok in _corpus()
def require_provenance(e):
    p=e.get("provenance","")
    m=PROV.search(p)
    if not m:
        raise RefusedInput("REFUSED '%s': provenance %r is not a resolvable reference (check 1)"
                           %(e.get("name","?"),p))
    if not _resolves(m.group(1)):
        raise RefusedInput("REFUSED '%s': provenance %r is well-formed but DOES NOT RESOLVE "
                           "in the registry or notes tree (A4)"%(e.get("name","?"),p))

CBAR={"3":"3bar","3bar":"3","1":"1"}
def conj(r):   # check 3: WHOLE rep
    return (CBAR[r[0]], r[1], -r[2])

SM_TARGET={ "Q_L":("3",2,Ylabel(F(1,6))), "u_c":("3bar",1,Ylabel(F(-2,3))),
            "d_c":("3bar",1,Ylabel(F(1,3))), "L_L":("1",2,Ylabel(F(-1,2))),
            "e_c":("1",1,Ylabel(F(1))) }
NU_C=("1",1,Ylabel(F(0)))

def score_b(entries, universe):
    # ---- validate EVERYTHING first; one bad entry aborts the run (check 4)
    for e in entries: require_provenance(e)
    reps=[]; nu_cs=[]
    for e in entries:
        r=(e["color"],e["su2"],Ylabel(e["Y"]))
        # SIXTEENTH-COLLISION FIX (Keeper audit): siphon ONLY when label AND content agree.
        # A label claiming nu_c over non-nu_c content is a smuggling path -> ABORT (check 4).
        if e.get("kind")=="nu_c" and r!=NU_C:
            raise RefusedInput("REFUSED '%s': kind='nu_c' but content %s is not (1,1,Y=0) -- "
                               "a label may not do work content should do"%(e["name"],(r[0],r[1],r[2])))
        (nu_cs if (e.get("kind")=="nu_c" and r==NU_C) else reps).append((e["name"],r))
    # ---- W1: complexity of the WHOLE multiset (check 3)
    ms=sorted((r[0],r[1],r[2].v) for _,r in reps)
    msc=sorted((conj(r)[0],conj(r)[1],conj(r)[2].v) for _,r in reps)
    W1 = (ms!=msc)
    # ---- W3: k-of-5 content match, Y as LABEL only (check 2 alive-side).
    # CAL'S WORDING FIX (R85): match "equals the SM list UP TO OVERALL CONJUGATION of the
    # multiset". Two frames scored -- DIRECT, and WHOLLY-CONJUGATED input -- best frame
    # reported WITH its name. Frames never mix per-leg, so a MIXED class cannot harvest
    # the free bit: it scores partial in BOTH frames.
    def _match(pool0):
        pool=list(pool0); hits={}
        for name,tgt in SM_TARGET.items():
            if tgt in pool: pool.remove(tgt); hits[name]=True
            else: hits[name]=False
        return hits,len(pool)
    direct=[r for _,r in reps]
    conjug=[conj(r) for r in direct]
    hd,ed=_match(direct); hc,ec=_match(conjug)
    if sum(hc.values())>sum(hd.values()):
        hits,extras,frame=hc,ec,"OVERALL-CONJUGATION (stated)"
    else:
        hits,extras,frame=hd,ed,"direct"
    k=sum(hits.values())                              # nu_c already siphoned (check 5)
    # ---- null from the DECLARED universe (check 6)
    U=len(set((u["color"],u["su2"],F(u["Y"])) for u in universe))
    p=F(1,U); null_k=float(math.comb(5,k))*float(p)**k*float(1-p)**(5-k) if U>1 else float("nan")
    return dict(W1=W1,k=k,hits=hits,extras=extras,frame=frame,nu_c_count=len(nu_cs),
                universe_size=U,null_at_k=null_k)

# ================= SELF-TESTS, one per blind check =================
if __name__=="__main__":
    P="T2527"; mk=lambda n,c,s,y,**kw: dict(name=n,color=c,su2=s,Y=y,provenance=P,**kw)
    UNI=[dict(color=c,su2=s,Y=y) for c in ("3","3bar","1") for s in (1,2)
         for y in (F(1,6),F(-2,3),F(1,3),F(-1,2),F(1),F(0))]
    SM=[mk("Q_L","3",2,F(1,6)),mk("u_c","3bar",1,F(-2,3)),mk("d_c","3bar",1,F(1,3)),
        mk("L_L","1",2,F(-1,2)),mk("e_c","1",1,F(1))]
    ok=lambda b,msg: print("  [%s] %s"%("PASS" if b else "FAIL",msg))
    print("SELF-TESTS against Keeper's six blind checks:")
    # 1 must-reject: provenance 'banked'
    try: score_b([dict(name="X",color="1",su2=1,Y=0,provenance="banked")],UNI); ok(False,"check1")
    except RefusedInput as ex: ok("resolvable" in str(ex),"check 1: bare 'banked' refused: %s"%ex)
    # 2 must-catch: W3 distinguishes u_c(-2/3) from d_c(+1/3).
    # NOTE (fixture bug, self-caught): a NAME-swap of Y between u_c and d_c leaves the MULTISET
    # unchanged -- matching is content-based and name-blind, so that test was a tautology.
    # The real must-catch: BREAK u_c's Y (+2/3 instead of -2/3) -> it must NOT match.
    sw=[mk("Q_L","3",2,F(1,6)),mk("u_c","3bar",1,F(2,3)),mk("d_c","3bar",1,F(1,3)),
        mk("L_L","1",2,F(-1,2)),mk("e_c","1",1,F(1))]
    r=score_b(sw,UNI); ok(r["k"]==4 and not r["hits"]["u_c"] and r["extras"]==1,
        "check 2a: u_c with wrong Y NOT matched, counts against (k=%d, extras=%d)"%(r["k"],r["extras"]))
    try: Ylabel(1)+Ylabel(2); ok(False,"check2b")
    except RefusedInput as ex: ok(True,"check 2b: Y addition raises -- anomaly path dead by wrapper + review (A5)")
    # 3 must-reject: vector-like multiset fails W1
    vl=SM+[mk(n+"bar",CBAR[c["color"]],c["su2"],-F(c["Y"])) for n,c in
           zip(["Q","u","d","L","e"],SM)]
    r=score_b(vl,UNI); ok(r["W1"]==False,"check 3: deliberately vector-like multiset -> W1 FAILS")
    r=score_b(SM,UNI); ok(r["W1"]==True,"check 3b: SM alone is complex -> W1 passes")
    # 4 must-catch: one bad entry kills the WHOLE run
    try:
        score_b(SM+[dict(name="rogue",color="1",su2=1,Y=0,provenance="banked")],UNI)
        ok(False,"check4")
    except RefusedInput as ex: ok(True,"check 4: one bad entry aborts entire run (%s)"%str(ex)[:40])
    # A4 must-reject: well-formed but nonexistent ID refused
    try:
        score_b([dict(name="ghost",color="1",su2=1,Y=0,provenance="T9999")],UNI); ok(False,"A4")
    except RefusedInput as ex: ok("DOES NOT RESOLVE" in str(ex),"A4: well-formed T9999 refused (existence checked)")
    # 5c SIXTEENTH must-reject: colored entry claiming kind='nu_c' must ABORT, not siphon
    try:
        score_b(SM+[mk("smuggle","3",2,F(1,6),kind="nu_c")],UNI); ok(False,"check 5c")
    except RefusedInput as ex: ok("label may not do work" in str(ex),
        "check 5c (16th): colored doublet claiming nu_c ABORTS the run: %s"%str(ex)[:60])
    # 5d strictness both ways: unlabeled (1,1,0) content is NOT siphoned -> counts as extra
    r=score_b(SM+[mk("bare_singlet","1",1,F(0))],UNI)
    ok(r["nu_c_count"]==0 and r["extras"]==1,
       "check 5d: undeclared (1,1,0) content NOT silently siphoned (extras=%d, nu_c=%d)"%(r["extras"],r["nu_c_count"]))
    # R85 W3-conjugation must-catch: WHOLLY conjugated SM passes WITH the frame stated
    csm=[mk(n+"_c*",CBAR[e["color"]],e["su2"],-F(e["Y"])) for n,e in zip("QudLe",SM)]
    r=score_b(csm,UNI)
    ok(r["k"]==5 and "CONJUG" in r["frame"],
       "R85a: fully conjugated SM -> k=5 in frame '%s' -- pass-with-conjugation-stated"%r["frame"])
    # R85 must-reject: a MIXED class must still fail (partial in BOTH frames, no free bit)
    mx=list(SM); e=mx[1]; mx[1]=mk("u_mixed",CBAR[e["color"]],e["su2"],-F(e["Y"]))
    r=score_b(mx,UNI)
    ok(r["k"]==4 and r["extras"]==1 and r["frame"]=="direct",
       "R85b: mixed class -> k=%d frame=%s -- still fails, no frame-mixing"%(r["k"],r["frame"]))
    # 5 nu_c both directions
    r=score_b(SM+[mk("nu_c","1",1,F(0),kind="nu_c")],UNI)
    ok(r["k"]==5 and r["extras"]==0 and r["nu_c_count"]==1,
       "check 5: nu_c neither in the 5-count nor an extra-against (k=%d extras=%d nu_c=%d)"
       %(r["k"],r["extras"],r["nu_c_count"]))
    # 6 null from declared universe
    # (fixture bug, self-caught: universe is 3 colors x 2 su2 x 6 Y = 36, not 18)
    ok(r["universe_size"]==36 and 0<r["null_at_k"]<1,
       "check 6: null computed from DECLARED universe |U|=%d, p(k=5|chance)=%.2e -- not hardcoded"
       %(r["universe_size"],r["null_at_k"]))
    print("\nk-of-5 report format: k=%d of 5 [%s], extras-against=%d, W1(complex)=%s, null@k=%.1e"
          %(r["k"],",".join(n for n,h in r["hits"].items() if h),r["extras"],r["W1"],r["null_at_k"]))
    print("NOTE: the SM rows above are TEST FIXTURES exercising the scorer -- NOT Lyra's input.")
    print("The live run waits for her multiset with provenance lines. This file is the audit target.")
