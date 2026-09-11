#!/usr/bin/env python3
"""Toy 5752 — R142 E1: (i) genus of D_IV^5 from (r,a,b) and the Bergman-kernel exponent as a POSTED number (two instruments, ball + D_IV^n controls);
(ii) Lecture 3's branching table and 3/7 read from the 5747 RECORD (subprocess), machine-compared to the lecture's sentence;
(iii) Lecture 1's Lie-ball inequalities vs the corpus definition (T2328) by sampling. Prereg: notes/Elie_PREREG_5752_* (8e64aa70)."""
import re, math, subprocess, sys, json, glob
from fractions import Fraction as F
import numpy as np
score=[]; cf=[]
def sc(nm, ok, c, d=""): score.append(ok); cf.append(c); print(f"  [{'HIT' if ok else 'MISS'}] {nm}{'' if c else ' (control)'}  {d}")
rng=np.random.default_rng(5752)
print("="*100); print("(i) GENUS AND THE BERGMAN-KERNEL EXPONENT"); print("="*100)
def genus(r,a,b): return (r-1)*a+b+2
r,a,b=2,3,0; n=5
print(f"  genus(r,a,b) = (r-1)a + b + 2 at (2,3,0) = {genus(r,a,b)}")
print(f"  integers previously quoted for this slot: n_C + 1 = {n+1};  g = n_C + rank = {n+2};  the BALL B^5's exponent d+1 = {5+1}")
print(f"  type IV family: genus(2, n-2, 0) = n for n = 3..8 -> {[genus(2,m-2,0) for m in range(3,9)]}")
sc("P1", genus(2,3,0)==5 and genus(2,3,0)!=n+1, False, "genus = 5 by the formula; 6 is the ball's number (d+1 at d=5), not this domain's")
print("  Convention: K(z,z) = (1/V) N(z,z)^(-p), N(z,z) = 1 - 2|z|^2 + |z.z|^2 (Hua). Real ray t e1: N = (1-t^2)^2. Isotropic ray t(e1+i e2)/sqrt2: N = 1 - 2t^2.")
# ---------- samplers ----------
def ball_points(d, N):            # uniform in the unit ball of C^d = R^{2d}
    g=rng.normal(size=(N,2*d)); g/=np.linalg.norm(g,axis=1)[:,None]; rr=rng.uniform(size=N)**(1.0/(2*d))
    x=g*rr[:,None]; return x[:,:d]+1j*x[:,d:]
def lie_points(d, N):             # uniform in D_IV^d, by rejection from the unit ball (acceptance 2^{1-d})
    z=ball_points(d,N); r2=(np.abs(z)**2).sum(1); zz=(z*z).sum(1)
    return z[(1-2*r2+np.abs(zz)**2>0)]
def batches(sampler, d, N, B):
    out=[sampler(d,N) for _ in range(B)]; return out
def mean_err(vals):               # vals: list of per-batch means
    v=np.array(vals); return v.mean(), v.std(ddof=1)/math.sqrt(len(v))
print("\n  INSTRUMENT A — the degree-1 cell: p = (order of N on the real ray)^-1 * V/||z_1||^2 = d/(ord * <|z|^2>_D); ord = 2 on D_IV^n (rank 2), 1 on B^d (rank 1)")
resA={}
for lab,sampler,d,ordr,pred,B,N in [("D_IV^5",lie_points,5,2,5,15,4_000_000),("D_IV^4",lie_points,4,2,4,8,2_000_000),("D_IV^6",lie_points,6,2,6,15,4_000_000),
                                    ("B^5",ball_points,5,1,6,8,1_000_000),("B^4",ball_points,4,1,5,8,1_000_000)]:
    pts=batches(sampler,d,N,B); tot=sum(len(p) for p in pts)
    m2=[(np.abs(p)**2).sum(1).mean() for p in pts]; mu,err=mean_err(m2)
    p_hat=d/(ordr*mu); p_err=p_hat*err/mu
    resA[lab]=(p_hat,p_err,pred,pts)
    print(f"   {lab:7}: samples {tot:9d}  <|z|^2>_D = {mu:.5f} +- {err:.5f}   p_hat = {p_hat:.4f} +- {p_err:.4f}   (genus/ball prediction {pred}; |p_hat - {pred}| = {abs(p_hat-pred)/p_err:.1f} sigma; from {pred+1 if 'D_IV' in lab else pred-1}: {abs(p_hat-(pred+1 if 'D_IV' in lab else pred-1))/p_err:.1f} sigma)")
ph,pe,_,ptsL=resA["D_IV^5"]
sc("P2", abs(ph-5)<3*pe and abs(ph-6)>5*pe, True, f"D_IV^5 exponent by the degree-1 cell = {ph:.4f} +- {pe:.4f}: 5 within 3 sigma, 6 excluded at {abs(ph-6)/pe:.0f} sigma")
print("\n  INSTRUMENT B — the reproducing property: (1/V) int_D |N(z,w0)|^(-2p) dV = N(w0,w0)^(-p) holds iff p is the exponent")
def N_of(z,w):  # Hua's norm function N(z,w) = 1 - 2 z.w~ + (z.z)(w~.w~)
    return 1-2*(z*np.conj(w)).sum(1)+(z*z).sum(1)*(np.conj(w)*np.conj(w)).sum()
def N_ball(z,w): return 1-(z*np.conj(w)).sum(1)
resB={}
for lab,pts,Nf,rays,ps in [("D_IV^5",ptsL,N_of,{"real ray 0.4 e1":np.array([0.4,0,0,0,0],complex),"isotropic ray 0.4(e1+ie2)/sqrt2":np.array([0.4/math.sqrt(2),0.4j/math.sqrt(2),0,0,0])},[F(4),F(9,2),F(5),F(11,2),F(6),F(7)]),
                            ("B^5",resA["B^5"][3],N_ball,{"ray 0.4 e1":np.array([0.4,0,0,0,0],complex)},[F(5),F(6),F(7)])]:
    for rname,w0 in rays.items():
        Nww=float(np.real(Nf(w0[None,:],w0)[0]))
        line=[]
        for p in ps:
            vals=[np.abs(Nf(P,w0))**(-2*float(p)) for P in pts]; mu,err=mean_err([v.mean() for v in vals])
            ratio=mu/Nww**(-float(p)); rerr=err/Nww**(-float(p)); resB[(lab,rname,p)]=(ratio,rerr)
            line.append(f"p={str(p):4}: {ratio:.4f}+-{rerr:.4f} ({abs(ratio-1)/rerr:5.1f}s)")
        print(f"   {lab} {rname:32} N(w0,w0) = {Nww:.4f} |  "+"  ".join(line))
okB=all(abs(resB[("D_IV^5",r,F(5))][0]-1)<3*resB[("D_IV^5",r,F(5))][1] and abs(resB[("D_IV^5",r,F(6))][0]-1)>5*resB[("D_IV^5",r,F(6))][1] for r in ["real ray 0.4 e1","isotropic ray 0.4(e1+ie2)/sqrt2"])
sc("P3", okB, True, "reproducing property holds at p = 5 on both rays (within 3 sigma) and fails at p = 6 (> 5 sigma) on both")
okC=all(abs(resA[l][0]-resA[l][2])<3*resA[l][1] for l in ["B^5","B^4","D_IV^4","D_IV^6"]) and abs(resB[("B^5","ray 0.4 e1",F(6))][0]-1)<3*resB[("B^5","ray 0.4 e1",F(6))][1] and abs(resB[("B^5","ray 0.4 e1",F(5))][0]-1)>5*resB[("B^5","ray 0.4 e1",F(5))][1]
sc("P4", okC, False, f"controls: B^5 -> 6 (both instruments), B^4 -> 5, D_IV^4 -> 4, D_IV^6 -> 6 — the instrument reads the genus, and 6 is the ball's")
print(f"\n  POSTED NUMBER: Bergman-kernel exponent of D_IV^5 = 5 (closed form (r-1)a+b+2 at (2,3,0)); measured {ph:.3f} +- {pe:.3f} (instrument A) and reproducing-property ratio at p = 5: "
      +", ".join(f"{resB[('D_IV^5',r,F(5))][0]:.4f}+-{resB[('D_IV^5',r,F(5))][1]:.4f}" for r in ["real ray 0.4 e1","isotropic ray 0.4(e1+ie2)/sqrt2"])+f". The old '6 = n_C + 1' is B^5's exponent (measured {resA['B^5'][0]:.3f}).")
print("\n"+"="*100); print("(ii) LECTURE 3's BRANCHING TABLE AND 3/7 FROM THE 5747 RECORD"); print("="*100)
src=glob.glob("toy_5747_*.py")[0]; out=subprocess.run([sys.executable,src],capture_output=True,text=True).stdout
rec_tab={int(k):(F(L),F(M)) for k,L,M in re.findall(r"k=(\d) zonal : light = (\S+) \(=.*?matter = (\S+) \(",out)}
rec_def={(int(j),int(k)):F(dv) for j,k,dv in re.findall(r"\((\d),(\d)\): Sum_u.*?deficit = (\S+) ",out)}
m37=re.search(r"P\(state = \(1,1\) after three writes\) = (.+?) = (\S+) = ",out); rec_chain=m37.group(1); rec_37=F(m37.group(2))
rec_json=json.load(open(".record_5747.json"))
print(f"   5747 re-run SCORE line: {[l for l in out.splitlines() if l.startswith('SCORE')][0]}")
print(f"   record table k=0..5: {[(k,str(L),str(M)) for k,(L,M) in sorted(rec_tab.items())]}")
print(f"   record chain: {rec_chain} = {rec_37};  .record_5747.json three_write = {rec_json['three_write']}")
print(f"   record Bergman deficits: {[(jk,str(v)) for jk,v in rec_def.items()]}")
lec=open("../Curriculum/Spine_DIV5_QM_GR_SM/Lecture_03_Quantum_Mechanics.md").read()
mf=re.search(r"\$\(k\+3\)/\(2k\+3\)\$ and \$k/\(2k\+3\)\$",lec); mc=re.search(r"\$(1/5 \+ \(4/5\)\(2/7\)) = (3/7)\$",lec); md=re.search(r"by exactly \$(\S+)\$, \$(\S+)\$, \$(\S+)\$",lec)
print(f"   lecture formulas found: {bool(mf)}; lecture chain: '{mc.group(1)} = {mc.group(2)}'; lecture deficits: {md.groups()}")
lec_tab={k:(F(k+3,2*k+3),F(k,2*k+3)) for k in range(6)}
lec_chain=F(1,5)+F(4,5)*F(2,7); lec_37=F(mc.group(2)); lec_def=[F(x) for x in md.groups()]
ok_tab=(rec_tab==lec_tab); ok_chain=(rec_37==F(3,7)==lec_37==lec_chain and F(rec_json['three_write'])==F(3,7)); ok_def=(lec_def==[rec_def[(0,0)],rec_def[(0,1)],rec_def[(1,1)]])
print(f"   table match k=0..5: {ok_tab};  chain 1/5 + (4/5)(2/7) = 3/7 match: {ok_chain};  deficits 1/2, 10/21, 25/63 at (0,0),(0,1),(1,1): {ok_def}")
sc("P5", bool(mf) and ok_tab and ok_chain and ok_def, True, "Lecture 3's table, chain and deficit list are the 5747 record's, fraction for fraction")
print("\n"+"="*100); print("(iii) LECTURE 1's LIE-BALL INEQUALITIES vs THE CORPUS DEFINITION (T2328)"); print("="*100)
print("   L (Lecture 1): |z.z| < 1  and  1 - 2|z|^2 + |z.z|^2 > 0")
print("   C (T2328)    : |z|^2 < 1  and  1 - 2|z|^2 + |z.z|^2 > 0")
print("   H (Lie norm) : |z|^2 + sqrt(|z|^4 - |z.z|^2) < 1")
print("   proof sketch: |z.z| <= |z|^2 (Cauchy-Schwarz) so C => L; if |z|^2 >= 1 and |z.z| < 1 then 1 - 2|z|^2 + |z.z|^2 < 2 - 2|z|^2 <= 0, so L => C.")
cnt={k:0 for k in ["L","C","H","Q","S","LdC","LdH","Q-C","S-C","total"]}
def tally(z):
    r2=(np.abs(z)**2).sum(1); zz=(z*z).sum(1); azz=np.abs(zz); q=1-2*r2+azz**2
    L=(azz<1)&(q>0); C=(r2<1)&(q>0); H=(r2+np.sqrt(np.maximum(r2**2-azz**2,0))<1); Q=q>0; S=azz<1
    cnt["L"]+=int(L.sum()); cnt["C"]+=int(C.sum()); cnt["H"]+=int(H.sum()); cnt["Q"]+=int(Q.sum()); cnt["S"]+=int(S.sum())
    cnt["LdC"]+=int((L^C).sum()); cnt["LdH"]+=int((L^H).sum()); cnt["Q-C"]+=int((Q&~C).sum()); cnt["S-C"]+=int((S&~C).sum()); cnt["total"]+=len(z)
for _ in range(15):
    x=rng.uniform(-1,1,(4_000_000,10)); tally(x[:,:5]+1j*x[:,5:])
print(f"   cube [-1,1]^10, {cnt['total']:,} points: |L| = {cnt['L']:,}  |C| = {cnt['C']:,}  |H| = {cnt['H']:,}   L^C = {cnt['LdC']}  L^H = {cnt['LdH']}   Q\\C = {cnt['Q-C']:,}  S\\C = {cnt['S-C']:,}")
print(f"   volume check: |C|/total * 2^10 = {cnt['C']/cnt['total']*1024:.4f} vs pi^5/(2^4 5!) = {math.pi**5/(16*120):.4f}")
cube=dict(cnt)
for k in cnt: cnt[k]=0
for _ in range(10):   # thin shell 0.9 <= |z| <= 1.1, where the two definitions could only differ
    g=rng.normal(size=(1_000_000,10)); g/=np.linalg.norm(g,axis=1)[:,None]; rr=(0.9**10+rng.uniform(size=1_000_000)*(1.1**10-0.9**10))**0.1
    x=g*rr[:,None]; tally(x[:,:5]+1j*x[:,5:])
print(f"   shell 0.9<=|z|<=1.1, {cnt['total']:,} points: |L| = {cnt['L']:,}  |C| = {cnt['C']:,}  |H| = {cnt['H']:,}   L^C = {cnt['LdC']}  L^H = {cnt['LdH']}   Q\\C = {cnt['Q-C']:,}  S\\C = {cnt['S-C']:,}")
sc("P6", cube["LdC"]==0 and cube["LdH"]==0 and cnt["LdC"]==0 and cnt["LdH"]==0 and cube["C"]>0, True, "Lecture 1's set = T2328's set = the Lie-norm set on every sampled point (cube and boundary shell)")
sc("P7", cube["Q-C"]>0 and cube["S-C"]>0, False, "each clause is load-bearing: the quartic alone admits an outer component, |z.z|<1 alone admits |z|>=1")
t=rng.uniform(0,2*math.pi,100_000); x=rng.normal(size=(100_000,5)); x/=np.linalg.norm(x,axis=1)[:,None]; zs=np.exp(1j*t)[:,None]*x
r2=(np.abs(zs)**2).sum(1); azz=np.abs((zs*zs).sum(1)); q=1-2*r2+azz**2
print(f"   Shilov points e^(it) x, x in S^4: max |(|z.z| - 1)| = {np.abs(azz-1).max():.2e}, max |N(z,z)| = {np.abs(q).max():.2e}, max ||z|^2 - 1| = {np.abs(r2-1).max():.2e}")
sc("P8", np.abs(azz-1).max()<1e-12 and np.abs(q).max()<1e-12, False, "both clauses sit at their boundary values on the Shilov boundary")
print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s,c in zip(score,cf) if c and s)}/{sum(cf)} can-fail hit")
json.dump({"genus":5,"p_hat_DIV5":[ph,pe],"ratio_p5":{r:resB[('D_IV^5',r,F(5))] for r in ["real ray 0.4 e1","isotropic ray 0.4(e1+ie2)/sqrt2"]},"table_5747":{k:[str(L),str(M)] for k,(L,M) in rec_tab.items()},"three_write":str(rec_37),"cube":cube,"shell":cnt},open(".record_5752.json","w"),indent=1,default=str)
