#!/usr/bin/env python3
"""Round 153 (K1908 §4): the redshift-channel intrinsic column. r145_eb_lib.py is frozen at 4ce873ce (Cal §972) and is not edited; new fit code lives here.
Model: counts D_i = f_i b + w_i a;  redshift moments (lib convention R from <z'>_c = m + R·n_c, so an observer boost gives R = −g b)
R_k = −g_k b + ζ_k a,  ζ_k = Σ_i p_i w_i (z̃_i − z̄) over the window's bins (p_i = N_i/N weighted, z̃_i the bin median, z̄ = Σ p_i z̃_i) — Keeper K1908 (1).
Unknowns (b, a): four... six numbers, no new parameter."""
import hashlib, numpy as np
def v151_hash(): return hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]
def zeta_from_table(N_w,w,zmed):
    N_w=np.asarray(N_w,float); w=np.asarray(w,float); zmed=np.asarray(zmed,float); p=N_w/N_w.sum(); zbar=float(p@zmed); return float((p*w*(zmed-zbar)).sum()),zbar
def joint_two_channel_zeta(Ds,Cs,fs,w,Rs,CRs,gs,zetas):
    """ONE shared b and ONE intrinsic a: D_i = f_i b + w_i a;  R_k = −g_k b + ζ_k a  (⇔ −R_k = g_k b − ζ_k a)."""
    G=np.zeros((6,6)); r=np.zeros(6)
    for D,C,f,wi in zip(Ds,Cs,fs,w):
        W=np.linalg.inv(C); J=np.hstack([f*np.eye(3),wi*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@D
    for R,CR,g,z in zip(Rs,CRs,gs,zetas):
        W=np.linalg.inv(CR); J=np.hstack([g*np.eye(3),-z*np.eye(3)]); G+=J.T@W@J; r+=J.T@W@(-R)
    p=np.linalg.solve(G,r); return p[:3],p[3:],np.linalg.inv(G)
