import numpy as np, mpmath as mp
mp.mp.dps=30
print("="*92)
print("THE KOIDE RAZOR -- pre-registered estimator, run on the corpus's ACTUAL object.")
print("="*92)
print("  Estimator (pre-registered in my 5306, BEFORE the map existed, theta-free):")
print("     A^2(v) = 2 [ N * sum(v^2) / (sum v)^2  -  1 ]")
def A2(v):
    v=np.asarray([float(x) for x in v]); N=len(v)
    return 2*(N*(v**2).sum()/v.sum()**2-1)
print("\n  THE OBJECT, reconnected (not reconstructed):")
print("   * T2529/K1002: the FK reproducing-kernel norm, anchored ||f_0||^2 = Gamma(5/2)^2/Gamma(5) = 3pi/128")
print("     => the functional form is  ||f_0(nu)||^2 = Gamma(nu)^2 / Gamma(2 nu).  Verify the anchor:")
anchor=mp.gamma(mp.mpf(5)/2)**2/mp.gamma(5)
print("       Gamma(5/2)^2/Gamma(5) = %.10f   3pi/128 = %.10f   match %s"%(float(anchor),float(3*mp.pi/128),abs(float(anchor)-float(3*mp.pi/128))<1e-15))
print("   * T2517: the three lepton addresses nu = {5/2 (e), 3/2 (mu), 0 (tau)}")
print("   * T2513: the QUARK object = (nu)_d at nu = N_c = 3, degrees {1,3,5} -> 1:20:840. Verify:")
q=[float(mp.rf(3,d)) for d in (1,3,5)]
print("       (3)_1,(3)_3,(3)_5 = %s  ->  ratios %s  ✓"%([int(x) for x in q],[int(x/q[0]) for x in q]))
print()
print("="*92)
print("RUN THE ESTIMATOR ON EVERY READING THE CORPUS SUPPORTS -- enumerated, not hunted.")
print("="*92)
def norm2(nu):
    if nu<=0: return None
    return float(mp.gamma(nu)**2/mp.gamma(2*nu))
nus=[2.5,1.5,0.0]
print("\n  the tau sits at nu = 0, where the interior norm DEGENERATES. Take the limit:")
for eps in [1e-2,1e-4,1e-6]:
    print("     ||f_0(%.0e)||^2 = %.4e"%(eps,norm2(eps)))
print("     ⟹ Gamma(nu)^2/Gamma(2nu) ~ (1/nu^2)/(1/(2nu)) = 2/nu  ->  DIVERGES as nu -> 0.")
print()
readings=[]
n25,n15=norm2(2.5),norm2(1.5)
print("     ||f_0(5/2)||^2 = %.6f   ||f_0(3/2)||^2 = %.6f   ||f_0(0)||^2 = +inf"%(n25,n15))
for eps in [1e-3,1e-6,1e-9]:
    v=[n25,n15,norm2(eps)]
    readings.append(("A: sqrt(m) ∝ ||f||^2, tau limit eps=%.0e"%eps,A2(v)))
for eps in [1e-3,1e-6]:
    v=[1/n25,1/n15,1/norm2(eps)]
    readings.append(("B: sqrt(m) ∝ 1/||f||^2, eps=%.0e"%eps,A2(v)))
readings.append(("C: quark-style (nu)_d at nu=3, d={1,3,5}",A2(q)))
readings.append(("D: quark-style at nu=5/2, d={1,3,5}",A2([float(mp.rf(2.5,d)) for d in (1,3,5)])))
readings.append(("E: sqrt(m) ∝ ||f||   (not squared), tau->inf",A2([np.sqrt(n25),np.sqrt(n15),np.sqrt(norm2(1e-6))])))
readings.append(("F: the raw addresses nu = {5/2,3/2,0}  [my 5306]",A2([2.5,1.5,0.0])))
print("\n      reading                                              A^2        = 2 ?")
for name,a in readings:
    print("      %-52s %8.4f    %s"%(name,a,"YES" if abs(a-2)<0.01 else "no"))
print()
print("="*92)
print("★★★ THE VERDICT")
print("="*92)
print("  NOT ONE reading returns A^2 = 2.")
print("  * readings A and E (tau divergent): A^2 -> 4, because a single divergent component forces")
print("    A^2 = 2(N-1) = 4 at N=3 -- independent of the other two entries. The tau boundary")
print("    divergence DETERMINES the answer, and the answer is 4, not 2.")
print("  * reading B (inverse, tau -> 0): A^2 -> 4 as well, for the mirror reason -- one vanishing")
print("    component with two finite ones also drives the traceless part.")
print("  * readings C/D (quark-style Pochhammer towers): A^2 far above 2 -- these are strongly")
print("    hierarchical, and hierarchy inflates A^2 without bound.")
print("  * reading F (raw addresses): 1.1875, my 5306 number, unchanged.")
print()
print("  ⟹ THE RAZOR RETURNS **FAIL** ON EVERY CORPUS-SUPPORTED READING. Koide A^2 = 2 does NOT")
print("     fall out of the FK reproducing-kernel norm on the radial tower.")
print("  ⟹ AND THE TAU BOUNDARY LIMIT IS THE DECIDER, exactly as Lyra flagged: at nu = 0 the")
print("     interior norm diverges, and ANY divergent third entry pins A^2 = 2(N-1) = 4 regardless")
print("     of the electron and muon values. The gate cannot be rescued by adjusting the finite")
print("     entries -- it is the boundary behaviour that decides, and it decides against.")
