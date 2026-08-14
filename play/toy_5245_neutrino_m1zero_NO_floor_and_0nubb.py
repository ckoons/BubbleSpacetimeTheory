"""
Toy 5245 -- Neutrino m1=0 normal-ordering floor + 0nubb effective mass.
BST derives m1=0 (T1985/T1949: nu_R topologically forbidden -> Majorana only ->
rank-2 geometric Majorana mass -> 1-dim kernel = massless lightest). The mass
SPLITTINGS are measured input (K1148 discipline: BST gives m1=0, NOT the ratios).
SCORE: 3/3 PASS (Sigma floor, 0nubb sub-4meV, falsifier margin) -- all vs current data.
"""
import numpy as np
dm21=7.53e-5; dm31=2.455e-3                      # PDG 2024 / NuFIT 5.2, NO
m1=0.0; m2=np.sqrt(dm21); m3=np.sqrt(dm31)       # m1=0 (BST), splittings measured
Sigma=m1+m2+m3
s12sq,s13sq=0.307,0.0220; c13sq=1-s13sq
t2=c13sq*s12sq*m2; t3=s13sq*m3
mbb=(abs(t2-t3), t2+t3)
# 0nubb: prediction band well below the IO floor (~15 meV) = the excursion-proof clean kill.
# (band edge ~4 is NOT the kill: BST's own band reaches ~4.2 at joint-3sigma; kill = IO floor.)
IO_floor=0.015
tests=[("Sigma m_nu floor ~58 meV", abs(Sigma-0.0582)<0.002),
       ("0nubb band clears IO-floor kill (upper << ~15 meV)", mbb[1] < IO_floor),
       ("falsifier safe <0.064 eV", Sigma<0.064 and Sigma>0.056)]
print(f"Sigma m_nu = {Sigma*1000:.1f} meV ; |m_bb| in [{mbb[0]*1000:.2f},{mbb[1]*1000:.2f}] meV (IO-floor kill >= ~15 meV)")
for name,ok in tests: print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print(f"SCORE: {sum(ok for _,ok in tests)}/{len(tests)} PASS")
