import numpy as np, sys, time
exec(open('bigN.py').read().split('if __name__')[0])
rng=np.random.default_rng(303)
N=20000
print("SO(4,2)-DESCENDED BOUNDARY:  D_IV^4 -> R x S^3  (conformal Minkowski_4)")
print("run with the IDENTICAL pipeline used for the 5D case (toy 5252).")
print()
print("  geometry                    intervals  median r   IQR                median |I|")
for name,mk in [("Minkowski d=4 (calib)",lambda: make_MINK(N,4)),
                ("Minkowski d=5 (calib)",lambda: make_MINK(N,5)),
                ("BST descended (R x S^3)",lambda: make_ESU(N,3,2.0)),
                ("BST full      (R x S^4)",lambda: make_ESU(N,4,2.0))]:
    t,fut,pas,sub=mk(); rs,sz=interval_r(t,fut,pas,sub,N)
    if len(rs):
        q1,q3=np.percentile(rs,[25,75])
        print("  %-26s %4d       %.4f     [%.4f, %.4f]   %d"%(name,len(rs),np.median(rs),q1,q3,int(np.median(sz))))
    sys.stdout.flush()
print()
print("*** DISCRIMINATING-POWER CHECK -- can this test decide the DESCENT? ***")
print("  the estimator was put onto R x S^3, a 4-dimensional space, and asked its dimension.")
print("  Sweeping the sphere dimension shows the answer is DETERMINED BY THE INPUT:")
print()
print("   sphere S^n   total dim   median interval-r")
for ns in [2,3,4,5]:
    t,fut,pas,sub=make_ESU(N if ns<5 else 12000,ns,2.0)
    rs,sz=interval_r(t,fut,pas,sub,N if ns<5 else 12000,want=60)
    print("   S^%d          %d           %s"%(ns,ns+1,("%.4f"%np.median(rs)) if len(rs) else "n/a"))
    sys.stdout.flush()
print()
print("  => r tracks the sphere dimension EXACTLY, as it must. Feeding in a 4-dimensional")
print("     boundary and reading '4' tests the ESTIMATOR, not the DESCENT.")
print("  => and the restriction is exact: a totally geodesic S^3 subset S^4 has the SAME induced")
print("     metric, so the 5D light cone restricted to it IS the 4D light cone. Guaranteed, not measured.")
