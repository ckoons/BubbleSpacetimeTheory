import numpy as np
S=np.array([[1,1,0],[1,2,1],[0,1,2]],float)
P=np.linalg.matrix_power
r=lambda G: G[0,2]/G[1,2]
print("DIRECT from the matrices (no Cayley-Hamilton reduction), NON-NEGATIVE coefficients only:")
tests={ "S^3            (= pure Q^6 = Keeper's S5)": [0,0,1],
        "S^2 + S^3":                                 [0,1,1],
        "S^4            (= pure Q^8)":               [0,0,0,1],
        "S^3 + S^4 + S^5":                           [0,0,1,1,1],
        "0.01*S + S^3":                              [0.01,0,1] }
for name,a in tests.items():
    G=sum(a[k]*P(S,k+1) for k in range(len(a)))
    print(f"   {name:<42} ratio = {r(G):.4f}   > 1/4 ? {r(G)>0.25}")
print("\nKeeper's OWN seal table, reproduced from the reduction:")
for nm,(al,be) in {"S1 pure Q^4 (S^2)":(1,0),"S2 Q^2+Q^4 (S+S^2)":(1,1),"S5 pure Q^6 (S^3=5S^2-6S+1)":(5,-6)}.items():
    t = al/be if be else float('inf'); rr = al/(be+4*al)
    print(f"   {nm:<30} t={t:>8.4f}  ratio={rr:.4f}")
print("\n   -> S5 is a PURE NON-NEGATIVE series (a_6=1) with t = -0.833 < 0 and ratio 5/14 = 0.3571 > 1/4.")
print("      Keeper's own seal lists t(S5) = -0.833. The counterexample is inside the seal data.")
# reachable set under a_2k >= 0
print("\nReachable t under a_2k >= 0 (cone of the reduction directions):")
dirs=[]
for k in range(1,15):
    B=np.stack([np.eye(3).ravel(),S.ravel(),(S@S).ravel()],1)
    c,b,a=np.linalg.lstsq(B,P(S,k).ravel(),rcond=None)[0]; dirs.append((a,b))
print("   directions (alpha,beta):", [(round(a),round(b)) for a,b in dirs[:7]])
print(f"   t of directions: {[round(a/b,4) if abs(b)>1e-9 else 'inf' for a,b in dirs[:7]]}  -> limit {dirs[-1][0]/dirs[-1][1]:.6f}  (-4/7 = {-4/7:.6f})")
print("   => reachable t = [0,inf) U (-inf, -4/7]  -- the POLE at t=-1/4 is NOT in the cone.")
print(f"   => reachable ratio = [0,1/4) U (1/4, 4/9],  sup = 4/9 = {4/9:.4f}  (sweep found 0.4427)")
print("\nWhat the band needs:")
for R in (0.081,0.108):
    t=R/(1-4*R); print(f"   ratio {R} -> t={t:.4f} -> beta/alpha = {1/t:.2f}   (S must outweigh S^2 by {1/t:.1f}x)")
print("   All five candidates are S^2-heavy; none is S-dominant by ~5-8x. That is the SHAPE of the miss.")
