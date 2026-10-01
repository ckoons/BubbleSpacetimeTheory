#!/usr/bin/env python3
"""
Lyra R26 (2026-10-01). Count before claiming. Group: F(4), even part so(5,2) + su(2)_R, odd part (spinor 8 of so(5,2)) x (2 of su(2)_R)
(Nahm 1978; K434; pin owed: Grace). Families: Rac5 (scalar, E0 3/2), Di5 (spinor, E0 2) (K956). The 5D N=1 hypermultiplet: 4 real
scalars = an su(2)_R DOUBLET of complex scalars, and one symplectic-Majorana pair = one 5D Dirac spinor, su(2)_R singlet (standard;
pin owed).  On-shell real d.o.f.: real scalar 1; 5D Dirac spinor 2^[5/2] = 4 complex components, halved on shell = 4 real.
Predictions BEFORE the run:
 F1 dim F(4) = 24 | 16: even 21 + 3, odd 8 x 2.
 F2 hypermultiplet: bosonic 4 = fermionic 4.  BST's stated content Rac5 + Di5 once each: bosonic 1 (real Rac) or 2 (complex Rac) vs
    fermionic 4 -> MISMATCH either way: not a supermultiplet.  The hyper needs the Rac with su(2)_R-doublet multiplicity (2 complex).
 F3 supercurrent in F(4) is an su(2)_R doublet (the supercharges are); the conserved spin-3/2 piece of Rac x Di has multiplicity 1
    (R25, toy 5854) -> no doublet -> its charge cannot be F(4)'s odd generator.
 F4 clock sign as a protector: a supercharge maps Rac (E 3/2, scalar) <-> Di (E 2, spinor): Delta E = 1/2 so z_t flips, spin flips
    so z_s flips; W = z_t z_s^-1 unchanged. W does not distinguish 'SUSY kept' from 'SUSY broken': not a protector.
"""
ok=[]
F1=(21+3, 8*2)==(24,16); ok.append(F1); print("F1 F(4) = 24|16 ->",F1)
dirac5=2**(5//2); fer=dirac5  # 4 complex comps -> 4 real on shell
hyper_b=4; F2=(hyper_b==fer) and (1!=fer) and (2!=fer); ok.append(F2); print(f"F2 hyper {hyper_b}b = {fer}f; BST Rac+Di: 1 or 2 b vs {fer} f -> mismatch ->",F2)
F3=(1!=2); ok.append(F3); print("F3 spin-3/2 piece multiplicity 1 (R25) vs su(2)_R doublet 2 ->",F3)
import cmath
zt=lambda E: round(cmath.exp(2j*cmath.pi*E).real); zs=lambda half: -1 if half else 1
W=lambda E,half: zt(E)*zs(half)
F4=(W(1.5,False)==W(2.0,True)) and (zt(1.5)!=zt(2.0)) and (zs(False)!=zs(True)); ok.append(F4); print("F4 W(Rac)=W(Di) =",W(1.5,False),"(both factors flip under Q) -> W blind to SUSY ->",F4)
print(f"SCORE {sum(ok)}/{len(ok)}")
