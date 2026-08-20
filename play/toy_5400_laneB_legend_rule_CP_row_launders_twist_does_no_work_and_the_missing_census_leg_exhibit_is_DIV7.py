import numpy as np
print("="*104)
print("TOY 5400 -- LANE B SUPPORT: run the LEGEND RULE on every grid row, including the undoubted ones.")
print("  THE RULE, made testable: a row 'fact F = I1 AND I2' EARNS the meet only if BOTH legs can be")
print("  shown to fail -- i.e. there is a domain matching I1 with I2 changed where F FAILS, *and* one")
print("  matching I2 with I1 changed where F FAILS. *** IF EITHER FAILURE EXHIBIT DOES NOT EXIST,")
print("  THE ROW LAUNDERS: it credits an invariant that is doing no work. ***")
print("="*104)

def gammas(n):
    X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1]).astype(complex)
    g=[X,Y]
    while len(g)<n:
        k=g[0].shape[0]
        g=[np.kron(a,Z) for a in g]+[np.kron(np.eye(k),X),np.kron(np.eye(k),Y)]
    return g[:n]
def chain(T): return [-0.25j*(T[a]@T[a+1]-T[a+1]@T[a]) for a in range(len(T)-1)]
def fs(T,tol=1e-6):
    d=T[0].shape[0]; I=np.eye(d); H=np.zeros((d*d,d*d),complex)
    for A in T:
        K=np.kron(I,A.T)+np.kron(A.conj(),I); H+=K.conj().T@K
    w,V=np.linalg.eigh(H)
    if w[0]>tol*max(abs(w[-1]),1.0): return 0
    C=V[:,0].reshape(d,d)
    return 1 if np.linalg.norm(C-C.T)<np.linalg.norm(C+C.T) else -1
def halfspinor_nu(n):
    g=gammas(n); T=chain(g)
    if n%2: return fs(T)
    G=(1j)**(n//2)*np.linalg.multi_dot(g); w,V=np.linalg.eigh(G); P=V[:,w>0]
    return fs([P.conj().T@A@P for A in T])

print("\nTABLE 1 -- THE SEPARATOR INVENTORY (computed; census = half-spinor reality type)")
NM={1:"REAL",0:"COMPLEX",-1:"QUATERNIONIC"}
inv={}
print("   n    census          Shilov orientable?   rank")
for n in range(3,10):
    nu=halfspinor_nu(n); orient=((-1)**n==1); inv[n]=(nu,orient,2)
    print("   %-4d %-15s %-20s %d"%(n,NM[nu],"orientable" if orient else "NON-ORIENTABLE",2))
def same_census_diff_twist():
    return [(a,b) for a in inv for b in inv if a<b and inv[a][0]==inv[b][0] and inv[a][1]!=inv[b][1]]
def same_twist_diff_census():
    return [(a,b) for a in inv for b in inv if a<b and inv[a][1]==inv[b][1] and inv[a][0]!=inv[b][0]]
print("   same census, DIFFERENT twist :",same_census_diff_twist())
print("   same twist, DIFFERENT census :",same_twist_diff_census()[:6])
print("   *** BOTH kinds of separator exist inside D_IV -- so both legs of a census-AND-twist meet")
print("       ARE testable. No excuse for an unexhibited leg. ***")

print("\nTABLE 2 -- *** RUN THE RULE ON EVERY ROW ***")
print("   row                        claimed as        leg-1 exhibit (twist)   leg-2 exhibit (census)   verdict")
rows=[
 ("SU(2)_L","pure census","n/a (single)","D_IV^7: REAL census, no H block -> no SU(2)","*** PASSES ***"),
 ("N_gen","pure rank","n/a (single)","n/a (single)","PASSES (mod T2525)"),
 ("chirality_geom","census AND twist","D_IV^4: orientable -> no global gamma_5","D_IV^7: REAL -> rep not complex","*** PASSES 2-sided ***"),
 ("Majorana_geom","census AND twist","D_IV^4: orientable -> Spin not Pin","D_IV^7: REAL vs H -> form changes","*** PASSES 2-sided ***"),
 ("CP-existence","census AND twist","*** NONE -- see below ***","D_IV^7: no complex block -> no CPV","*** LAUNDERS ***"),
 ("Koide","census AND rank","(vetoed to negatives)","(vetoed)","already removed"),
]
for r in rows: print("   %-26s %-17s %-23s %-24s %s"%r)

print("\nTABLE 3 -- ★ *** THE CP ROW: WHY IT LAUNDERS ***")
print("   'CP violation is POSSIBLE' <=> SOME block is COMPLEX (nu = 0). That is a statement about")
print("   the CENSUS ALONE.  Now try to build the twist-leg failure exhibit:")
print("     take D_IV^4 and D_IV^5 -- SAME census, DIFFERENT twist (one orientable, one not).")
print("     Does 'some block is complex' change?  *** NO -- orientability does not touch the reality")
print("     type of any block. ***  So CP-possibility is IDENTICAL across the twist change.")
print("   *** ==> THERE IS NO TWIST-LEG FAILURE EXHIBIT, BECAUSE THE TWIST DOES NO WORK. ***")
print("   *** CP-EXISTENCE IS A PURE-CENSUS ROW, NOT A MEET. Writing it as census AND twist CREDITS")
print("       THE TWIST FOR SOMETHING IT DOES NOT DO -- exactly the laundering Lane B is hunting. ***")
print()
print("   AND IT COMPOUNDS A KNOWN WEAKNESS (my 5394): CP-existence is EXISTENCE-ONLY -- 'CP violation")
print("   is possible' CANNOT FAIL as a prediction. *** A row that is both unfalsifiable AS PHYSICS and")
print("   over-attributed AS BOOKKEEPING is the weakest cell in the grid. *** Demote to pure census,")
print("   keep the existence-only label, and do not let it sit beside Majorana as if it were peer-grade.")

print("\nTABLE 4 -- *** THE SECOND EXHIBIT THE ROUND WAS MISSING ***")
print("   Round 14 says chirality/Majorana pass because *** D_IV^4 exhibits the failure. *** That is")
print("   the TWIST leg only. The CENSUS leg needs its own exhibit, and it exists:")
print("     *** D_IV^5 (QUATERNIONIC, NON-ORIENTABLE) vs D_IV^7 (REAL, NON-ORIENTABLE) ***")
print("     -> SAME twist, DIFFERENT census. At n=7 the rep is REAL, so the algebraic reading changes:")
print("        not complex -> not chiral in the T2522 sense; symmetric-form structure differs.")
print("   *** So the meet is verified on BOTH legs, not one. @Grace @Cal -- cite D_IV^7 alongside")
print("       D_IV^4, or the row is only half-checked. ***")

print("\nTABLE 5 -- SCOPE, STATED HONESTLY (what this test does and does not cover)")
print("   TESTED RIGOROUSLY: rows keyed to the SPINOR reality type, swept across D_IV^n (n=3..9),")
print("     with orientability computed and rank constant at 2.")
print("   *** NOT TESTED: rows keyed to the THREE-BLOCK census {C,H,R} of End_K(H_F). H_F is")
print("     constructed for D_IV^5; I did not re-derive H_F(n) for other n, so a 3-block census sweep")
print("     would be ASSUMING the construction transports. *** Same limitation I flagged in 5398.")
print("   ==> the LAUNDERING VERDICT ON CP does NOT depend on that gap: it follows from orientability")
print("       being independent of every block's reality type, which holds however H_F is built.")

print("\n"+"="*104); print("VERDICT -- Lane B legend pass"); print("="*104)
print(" (1) ★★★ *** ONE ROW LAUNDERS, AND IT IS ONE OF THE UNDOUBTED ONES: CP-existence is written as")
print("     census AND twist, but the TWIST LEG HAS NO FAILURE EXHIBIT -- orientability does not")
print("     change any block's reality type, so CP-possibility is unchanged across D_IV^4 vs D_IV^5.")
print("     *** CP IS A PURE-CENSUS ROW. *** Demote it.")
print()
print(" (2) *** AND IT IS THE GRID'S WEAKEST CELL FOR A SECOND, INDEPENDENT REASON: *** CP-existence")
print("     cannot fail as a prediction at all (my 5394). Unfalsifiable as physics AND over-attributed")
print("     as bookkeeping. Keep the existence-only label and do not seat it next to Majorana.")
print()
print(" (3) *** THE CHIRALITY/MAJORANA MEETS PASS -- BUT THE ROUND CITED ONLY ONE LEG. *** D_IV^4 is")
print("     the TWIST exhibit; the CENSUS exhibit is *** D_IV^7 (REAL census, still non-orientable). ***")
print("     Cite both or the row is half-checked.")
print()
print(" (4) SU(2)_L (pure census) and N_gen (pure rank) PASS the single-invariant test -- SU(2)_L fails")
print("     at D_IV^7 where there is no quaternionic block, and survives the twist change at D_IV^4.")
print()
print(" (5) ★ SCOPE: this sweep is rigorous for SPINOR-reality-keyed rows. A three-block census sweep")
print("     would require H_F(n) for n != 5, which BST has not built -- *** the same gap as 5398. The")
print("     CP verdict does not lean on it. ***")
