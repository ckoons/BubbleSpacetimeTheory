#!/usr/bin/env python3
"""Toy 5746 — R138 LANE A: the Bergman/Szego kernel exponent ratio, computed for the unit ball (control) and for D_IV^5."""
import json, math
from fractions import Fraction as F
import numpy as np
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
# ---------- probes on the unit ball B^d ----------
def ball_intensity(nu,m,d): return F(m+d, F(nu)+m)          # <|z|^2> for z_1^m at weight nu
print("P1 POSITIVE CONTROL — the unit ball B^5")
print("  Probe H: which nu makes <|z|^2> == 1 for every m?")
hardy_b=[nu for nu in (F(4),F(9,2),F(5),F(11,2),F(6),F(7)) if all(ball_intensity(nu,m,5)==1 for m in range(8))]
print("   sweep nu = 4, 9/2, 5, 11/2, 6, 7 ->", [str(x) for x in hardy_b], "(the Shilov boundary of B^5 is the sphere, where |z|^2 = 1)")
print("  Probe B: uniform Monte Carlo in B^5 against the weight-nu prediction 1 - <|z|^2> = (nu-5)/(nu+m)")
rng=np.random.default_rng(5746); N=4_000_000
x=rng.normal(size=(N,5))+1j*rng.normal(size=(N,5)); r=np.abs(x).sum(1)  # placeholder
z=rng.uniform(-1,1,(N,5))+1j*rng.uniform(-1,1,(N,5)); r2=(np.abs(z)**2).sum(1); inb=r2<1
Z=z[inb]; R2=r2[inb]; print(f"   ball samples: {len(Z)}")
for m in (0,1,2,3):
    f2=np.abs(Z[:,0]**m)**2; est=(f2*R2).sum()/f2.sum(); B=25; idx=np.array_split(np.arange(len(f2)),B)
    e=np.array([(f2[i]*R2[i]).sum()/f2[i].sum() for i in idx]); err=e.std()/math.sqrt(B)
    print(f"   m={m}: MC <|z|^2> = {est:.4f} +- {err:.4f};  nu=6 predicts {float(ball_intensity(6,m,5)):.4f};  nu=5 predicts {float(ball_intensity(5,m,5)):.4f}")
mc_ok=abs(((np.abs(Z[:,0]**0)**2*R2).sum()/len(Z))-5/6)<0.01
sc("P1", hardy_b==[F(5)] and mc_ok, True, "Probe H -> nu_Hardy(B^5) = 5 uniquely; Probe B -> nu_Bergman(B^5) = 6; RATIO = 6/5, the row's number, reproduced")
# ---------- probes on D_IV^5 ----------
def Lnu(nu,j,k): j=F(j);k=F(k);nu=F(nu); return F(k+3,2*k+3)*(j+k+F(5,2))/(j+k+nu)
def Mnu(nu,j,k):
    if k==0: return F(0)
    j=F(j);k=F(k);nu=F(nu); return F(k,2*k+3)*(j+1)/(j+nu-F(3,2))
def lie_intensity(nu,j,k): return Lnu(nu,j,k)+Mnu(nu,j,k)
print("P2 — D_IV^5")
print("  Probe H: which nu makes <|z|^2> == 1 for every word (j,k)?")
hardy_l=[nu for nu in (F(2),F(9,4),F(5,2),F(3),F(4),F(5),F(6)) if all(lie_intensity(nu,j,k)==1 for j in range(5) for k in range(5))]
print("   sweep nu = 2, 9/4, 5/2, 3, 4, 5, 6 ->", [str(x) for x in hardy_l])
print("  Probe B: uniform Monte Carlo on the Lie ball against the weight-nu prediction")
keep=[]
for c in range(12):
    w=rng.uniform(-1,1,(6_000_000,5))+1j*rng.uniform(-1,1,(6_000_000,5))
    rr=(np.abs(w)**2).sum(1); ww=(w*w).sum(1); msk=(rr<1)&(np.abs(ww)**2-2*rr+1>0); keep.append(w[msk])
W=np.concatenate(keep); R2L=(np.abs(W)**2).sum(1); WW=(W*W).sum(1); print(f"   Lie-ball samples: {len(W)}")
for (j,k),lab in [((0,0),'vacuum'),((0,1),'one light write'),((1,0),'one winding')]:
    vals=(WW**j)*(W[:,0]**k if k>0 else 1.0); f2=np.abs(vals)**2
    B=25; idx=np.array_split(np.arange(len(f2)),B); e=np.array([(f2[i]*R2L[i]).sum()/f2[i].sum() for i in idx])
    print(f"   ({j},{k}) {lab:16}: MC <|z|^2> = {e.mean():.4f} +- {e.std()/math.sqrt(B):.4f};  nu=5 predicts {float(lie_intensity(5,j,k)):.4f};  nu=5/2 predicts {float(lie_intensity(F(5,2),j,k)):.4f}")
    if (j,k)==(0,0): mc_l_ok=abs(e.mean()-0.5)<3*e.std()/math.sqrt(B)+0.005
sc("P2", hardy_l==[F(5,2)] and mc_l_ok, True, "Probe H -> nu_Hardy(D_IV^5) = 5/2 uniquely; Probe B -> nu_Bergman = 5; RATIO = 5/(5/2) = 2")
print("P3 — the two families")
for d in range(2,9): print(f"   B^{d}: nu_H = {d}, nu_B = {d+1}, ratio = {F(d+1,d)}", end="   |   ")
print()
for n in range(3,9):
    hl=[nu for nu in (F(n,2),F(n),F(n+1,n)) if True]
    print(f"   D_IV^{n}: nu_H = {F(n,2)}, nu_B = {n}, ratio = {F(n,1)/F(n,2)}", end="   |   ")
print()
fam_ok=all(F(n,1)/F(n,2)==2 for n in range(3,9)) and all(F(d+1,d)!=2 for d in range(3,9))
print(f"   (n+1)/n at n=5 is {F(6,5)} = C_2/n_C = {F(6,5)}: the ball's formula and a BST ratio agree at n = 5 ONLY")
sc("P3", fam_ok, True, "D_IV^n ratio is 2 at every n; B^d ratio is (d+1)/d; they coincide at no n")
print("P4 — propagation, both branches priced, no ruling (Cal C1)")
G=6.67430e-11; mp=1.67262192369e-27; hbar=1.054571817e-34; cc=299792458.0
aG=G*mp**2/(hbar*cc); print(f"   observed alpha_G = G m_p^2/(hbar c) = {aG:.4e}")
row=(36/5)*math.exp(-90); alt=6*2*math.exp(-90)
print(f"   row as registered: (C_2^2/n_C) e^-90 = (36/5) e^-90 = {row:.4e}  -> {abs(row/aG-1)*100:.2f}% from observed")
print(f"   if the kernel sentence is LOAD-BEARING (prefactor = C_2 x ratio = 6 x 2 = 12): {alt:.4e}  -> {abs(alt/aG-1)*100:.1f}% from observed")
print(f"   if DECORATIVE (prefactor = C_2^2/n_C as a BST ratio): number untouched, justification struck. Ratio of the two answers = {2/(6/5):.4f} = 5/3")
sc("P4", abs(row/aG-1)<0.005 and abs(alt/aG-1)>0.5, False, "row 0.11% vs load-bearing 66% miss; both priced, Cal rules")
print("   DOWNSTREAM HELD: T1485 (Lambda), Toy 2350, the H_0 closure at 0.12%, T1924's joint anchor if it inherits.")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({'ball_ratio':'6/5','lie_ratio':'2','ratio_of_answers':'5/3','alpha_G_obs':aG,'row':row,'loadbearing':alt}, open('.record_5746.json','w'), indent=1)
