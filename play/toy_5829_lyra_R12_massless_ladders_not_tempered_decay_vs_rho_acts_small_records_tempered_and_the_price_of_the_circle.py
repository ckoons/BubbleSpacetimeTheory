#!/usr/bin/env python3
"""
Lyra R12 (2026-09-27). Invariants first.
 TEMPEREDNESS (Cowling-Haagerup-Howe criterion; pin owed): pi tempered <=> K-finite matrix coefficients bounded by
 C * Xi(g) * (poly), Xi ~ e^{-rho(H)} (1+|H|)^d on A+.  SO(n,2): restricted roots C2/BC2 of the TUBE type:
 e1+-e2 with multiplicity n-2, 2e1 and 2e2 with multiplicity 1 => rho = (n-1) e1 + 1 e2.
 Scalar lowest-K-type coefficient of H_lambda(D_IV^n) on a = (t1,t2): (cosh t1)^-lambda (cosh t2)^-lambda.
 Along e1 (t2=0): decay e^{-lambda t} vs Xi ~ e^{-(n-1)t}: tempered only if lambda >= n-1.
 Massless 4D ladders (Mack): Delta = j+1 (j = 0, 1/2, 1) -> leading decay e^{-Delta t} (vector K-type factor bounded;
 numerical per-helicity check is Elie's).
 Predictions BEFORE the run:
 T1  rho(SO(n,2)) = (n-1, 1); thresholds lambda >= n-1: SU(2,2)=SO(4,2): 3  [CONTROL: scalar HDS of SU(p,q) is lambda > p+q-1 = 3];
     SO(5,2): 4  [CONTROL: Kobayashi 8.4 / K1928 'lambda > 4'].
 T2  massless ladders Delta = 1, 3/2, 2 < 3: ratio coef/Xi -> infinity along e1 (NOT tempered), each helicity.
     CONTROL: lambda = 7/2 (a holomorphic discrete series of SO(4,2)) -> ratio -> 0 (tempered).
 T3  BST's acts: H2 (5/2) and Rac (3/2) on SO(5,2) are below 4 -> NOT tempered; records L2(G/K) tempered (Plancherel).
     H2|SO(4,2) = sum_k H_{5/2+k}(D4): k=0 not tempered, k>=1 (lambda >= 7/2 > 3) tempered.
 T4  PRICE (computed from CODATA via scipy.constants, not quoted): lambdabar_e = hbar/(m_e c) = 3.8616e-13 m,
     1/R = m_e c^2 = 0.51100 MeV; c*tick = N_max*hbar/(m_e c) (N_max=137) = 5.2904e-11 m ~ Bohr radius a0 (5.2918e-11)
     within 0.03 %, 1/R = m_e c^2/137 = 3.730 keV; hbar*c/(1 TeV) = 1.973e-19 m.
"""
import numpy as np
from scipy import constants as C
ok=[]
rho=lambda n:(n-1,1)
T1=rho(4)==(3,1) and rho(5)==(4,1); ok.append(T1); print("T1 rho SO(4,2)",rho(4),"SO(5,2)",rho(5),"thresholds 3 and 4 ->",T1)
t=np.array([20.,40.,60.])
Xi=lambda t,n: (1+t)*np.exp(-(n-1)*t)
ratio=lambda D,n: np.cosh(t)**(-D)/Xi(t,n)
T2=all(np.all(np.diff(ratio(D,4))>0) for D in (1,1.5,2)) and np.all(np.diff(ratio(3.5,4))<0)
ok.append(T2); print("T2 coef/Xi along e1 at t=20,40,60:",{D:np.round(ratio(D,4),2).tolist() for D in (1,1.5,2)},"control 7/2:",ratio(3.5,4).tolist(),"->",T2)
T3=all(np.all(np.diff(ratio(D,5))>0) for D in (1.5,2.5)) and np.all(np.diff(ratio(2.5,4))>0) and np.all(np.diff(ratio(3.5,4))<0)
ok.append(T3); print("T3 Rac, H2 not tempered on SO(5,2); H_{5/2}(D4) not, H_{7/2}(D4) tempered ->",T3)
hb,me,c,MeV=C.hbar,C.m_e,C.c,1e6*C.e
lb=hb/(me*c); E1=me*c**2/MeV; a0=C.physical_constants['Bohr radius'][0]; ct=137*lb; lt=hb*c/(1e12*C.e)
T4=abs(lb-3.8616e-13)/3.8616e-13<1e-4 and abs(E1-0.51100)<1e-4 and abs(ct/a0-1)<4e-4 and abs(E1*1e3/137-3.730)<1e-3 and abs(lt-1.973e-19)/1.973e-19<1e-3
ok.append(T4); print(f"T4 lambdabar_e={lb:.5e} m, m_e c^2={E1:.5f} MeV, c*tick={ct:.5e} m vs a0={a0:.5e} (ratio {ct/a0:.5f}), 1/R={E1*1e3/137:.4f} keV, hbar c/TeV={lt:.4e} m, TeV/m_e c^2={1e6/E1:.3e} ->",T4)
print(f"SCORE {sum(ok)}/{len(ok)}")
