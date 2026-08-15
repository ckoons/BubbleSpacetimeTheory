import numpy as np
rng=np.random.default_rng(1560)
print("="*88)
print("(1) PARITY: can an antilinear J with J^2 = -1 exist on an ODD complex dimension?")
print("="*88)
print("  antilinear J = C.K (K = componentwise conjugation, C unitary) => J^2 = C conj(C).")
print("  J^2 = -I  requires  C conj(C) = -I.  Take determinants:")
print("     det(C) conj(det C) = |det C|^2 > 0 real,   but  det(-I_n) = (-1)^n.")
print("  => n must be EVEN. No quaternionic structure exists in odd complex dimension.\n")
for n in [2,3,4,5]:
    # numerically: minimise ||C conj(C) + I|| over unitaries via many random tries + polar retraction
    best=1e9
    for _ in range(4000):
        A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        U,_,Vh=np.linalg.svd(A); C=U@Vh
        best=min(best,np.abs(C@C.conj()+np.eye(n)).max())
    print("    n=%d  det(-I)=%+d  best achieved ||C conj(C) + I||_max over 4000 unitaries = %.4f  %s"%(
        n,(-1)**n,best,"<- attainable" if best<1e-6 else "<- NOT attainable"))
print("\n  (exact solutions exist for even n, e.g. n=2: C = [[0,1],[-1,0]] gives C conj(C) = -I)")
C2=np.array([[0,1],[-1,0]],complex)
print("    check n=2 explicit: ||C conj(C) + I|| = %.2e"%np.abs(C2@C2.conj()+np.eye(2)).max())
print()
print("="*88)
print("(2) CAN SU(3) ACT ON A REAL 3-SPACE AT ALL?  Frobenius-Schur on SU(3), Haar-sampled.")
print("="*88)
def haar_su3(m):
    A=(rng.normal(size=(m,3,3))+1j*rng.normal(size=(m,3,3)))/np.sqrt(2)
    Q,R=np.linalg.qr(A)
    d=np.einsum('...ii->...i',R); Q=Q*(d/np.abs(d))[:,None,:]
    det=np.linalg.det(Q)
    return Q*(det**(-1/3))[:,None,None]
G=haar_su3(200000)
tr=np.einsum('...ii->...',G)
tr2=np.einsum('...ii->...',G@G)
fs_fund=tr2.mean().real
fs_adj=(np.abs(tr2)**2-1).mean().real
print("  fundamental 3  : FS = %+.4f   => 0 = COMPLEX rep (not real, not pseudo-real)"%fs_fund)
print("  adjoint     8  : FS = %+.4f   => +1 = REAL"%fs_adj)
print("\n  ⟹ SU(3)'s 3 is COMPLEX: its realification is 6-dimensional. SU(3) has NO nontrivial")
print("     3-dimensional REAL representation (smallest real irrep is the adjoint 8).")
print("  ⟹ SU(3) CANNOT ACT ON A REAL 3-SPACE. What acts on V_12 (real, 3D) is SO(3), full stop.")
