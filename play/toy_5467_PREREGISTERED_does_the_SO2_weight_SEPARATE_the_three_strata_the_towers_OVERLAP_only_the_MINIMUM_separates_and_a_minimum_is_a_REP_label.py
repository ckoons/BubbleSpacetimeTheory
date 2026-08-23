# TOY 5467 -- R73 Section 2 assignment. Elie, 2026-08-23. Rubric cell: EXTERNAL 3.
# "Pre-register, then test -- does the SO(2) weight separate the three strata?"
# Keeper predicts NO and wants it on record BEFORE I compute. It is on record below, and so is
# a distinction I think his prediction slightly conflates. THE PRE-REGISTRATION IS WRITTEN FIRST
# AND NOTHING IN IT IS REVISED AFTER THE NUMBERS.

BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5467 -- does m_wt (the SO(2) weight) SEPARATE the three strata nu_strat?"); print(BAR)

head("PART 0 -- ★ PRE-REGISTRATION. Written before the computation. Not revised after.")
print("  KEEPER'S PREDICTION, on record: NO -- by his generalization of my A2 kill, that any")
print("  spectral label has an infinite tower 0,1,2,... and so cannot carry a 3-valued index.")
print()
print("  ★ MY PRE-REGISTERED OBJECTION TO THE QUESTION ITSELF -- filed before computing, because")
print("    if I raise it after, it is rationalization. *** HIS CONSTRAINT AND THIS TEST ARE TWO")
print("    DIFFERENT CLAIMS AND THEY CAN COME APART: ***")
print("      CLAIM A -- 'can m_wt BE the generation index?'      -> NO, and his argument settles it:")
print("                 an infinite tower cannot be a 3-valued index. I agree, no computation needed.")
print("      CLAIM B -- 'does m_wt SEPARATE the three strata?'   -> OPEN. A label can take infinitely")
print("                 many values and still take DISTINCT values on three specified objects.")
print("    Height is not an index of people, but it can still distinguish three named people.")
print("    *** SO 'NO' TO A DOES NOT GIVE 'NO' TO B, AND B IS WHAT I WAS ASKED TO TEST. ***")
print()
print("  MY PRE-REGISTERED PREDICTION ON B: the three strata will have DISTINCT LOWEST weights but")
print("  OVERLAPPING towers -- so m_wt separates the REPRESENTATIONS but NOT the MODES. If that is")
print("  what comes out, the honest verdict is a SPLIT, not a clean no.")
print("  WIN CONDITION FOR 'YES': the three weight sets are pairwise DISJOINT.")
print("  WIN CONDITION FOR 'NO' : the three weight sets OVERLAP.")

head("PART A -- the object, declared")
print("  Each stratum nu_strat carries its own Wallach representation H_{nu}. Its SO(2) weights are")
print("  the lowest weight plus the degree tower: m_wt(nu, d) = nu + d, d = 0,1,2,...")
print("  (Normalisation-carrying: the ADDITIVE OFFSET is convention, the SPACING and the RELATIVE")
print("   offsets are not. Per the standing rule I test only convention-independent statements --")
print("   disjointness and overlap are invariant under a common shift.)")

head("PART B -- THE COMPUTATION")
strata=[("electron/up-1","5/2",2.5),("muon/up-2","3/2",1.5),("tau/top","0",0.0)]
NT=8
print("   stratum        nu_strat   first %d SO(2) weights m_wt = nu + d"%NT)
towers={}
for name,lbl,nu in strata:
    t=[nu+d for d in range(NT)]
    towers[lbl]=set(t)
    print("   %-14s %-10s %s ..."%(name,lbl,", ".join(("%g"%v) for v in t)))
print()
print("   LOWEST weights:  5/2, 3/2, 0  ->  ALL DISTINCT")
print()
print("   pairwise tower intersections (first %d rungs):"%NT)
import itertools
disjoint=True
for (a,_,_),(b,_,_) in itertools.combinations(strata,2):
    la=[x for x in strata if x[0]==a][0][1]; lb=[x for x in strata if x[0]==b][0][1]
    inter=sorted(towers[la]&towers[lb])
    if inter: disjoint=False
    print("     %-14s vs %-14s : %s"%(a,b,("%d shared: %s"%(len(inter),", ".join("%g"%v for v in inter[:5]))) if inter else "DISJOINT"))

head("PART C -- VERDICT AGAINST THE PRE-REGISTERED WIN CONDITIONS")
print("  win condition for YES was: three weight sets pairwise DISJOINT.")
print("  observed: %s"%("DISJOINT" if disjoint else "*** THEY OVERLAP ***"))
print()
print("  *** ANSWER TO CLAIM B: NO. m_wt DOES NOT SEPARATE THE THREE STRATA. ***")
print("  The towers overlap: nu=3/2 contains 5/2, 7/2, ... and nu=5/2 starts at 5/2, so a mode of")
print("  weight 5/2 could sit in EITHER. Knowing m_wt does not tell you which stratum you are in.")
print()
print("  ★ BUT THE SPLIT I PRE-REGISTERED IS REAL AND IT IS THE INFORMATIVE HALF:")
print("     the LOWEST weights ARE distinct (5/2, 3/2, 0).")
print("     *** SO WHAT SEPARATES THE STRATA IS 'the lowest weight of the representation containing")
print("         the mode' -- WHICH IS NOT A PROPERTY OF THE MODE. It is a property of WHICH")
print("         REPRESENTATION YOU ARE IN. That is a REP label, and a rep label IS a support/")
print("         localization label wearing spectral clothes. ***")
print("     ⟹ KEEPER'S CONCLUSION IS CONFIRMED, AND BY A ROUTE THAT STRENGTHENS IT: the quantity")
print("       that does the separating turns out to be exactly the KIND of object he predicted the")
print("       generation label must be. The spectral candidate, pushed, becomes a support label.")

head("VERDICT")
print(" (1) CLAIM A (can m_wt BE the index): NO -- conceded without computation, his argument is enough.")
print(" (2) CLAIM B (does m_wt SEPARATE the strata): *** NO. Towers overlap; pre-registered win")
print("     condition for YES fails. ***")
print(" (3) ★ THE SPLIT: lowest weights ARE distinct, but a lowest weight is a REPRESENTATION")
print("     property, not a mode property. The only separating quantity is a rep/support label.")
print("     *** THE SPECTRAL CANDIDATE, PUSHED HARD ENOUGH, TURNS INTO THE SUPPORT LABEL. ***")
print(" (4) I raised my objection to the question BEFORE computing, and the computation did not")
print("     rescue it -- Claim B answers NO too. Reporting that plainly: my distinction was real")
print("     and it did NOT change the verdict.")
print()
print(" *** RULE 3: ONE CI -- ME. NOT FILED. Attack: (a) is m_wt(nu,d) = nu + d the right tower")
print("     for the DEGENERATE Wallach points nu = 3/2 and 0? My own 5456 says those are not")
print("     generic points -- if their towers are truncated rather than full, disjointness could")
print("     return and the answer flips. THAT IS THE ONE TO ATTACK and it is my own prior result")
print("     arguing against my own computation here. ***")
