import numpy as np
print("IS 'S^2 x U(1) = SU(2)' AN IDENTITY?  The Hopf bundle S^3 -> S^2 with U(1) fibre.")
print("If the bundle were TRIVIAL (a product), any two fibres would be parallel copies: linking 0.")
print("Compute the Gauss linking number of two Hopf fibres, stereographically projected to R^3.\n")
def fibre(z1,z2,n=4000):
    th=np.linspace(0,2*np.pi,n,endpoint=False)
    p=np.exp(1j*th)
    a=p*z1; b=p*z2
    return np.stack([a.real,a.imag,b.real,b.imag],axis=1)     # circle in S^3 subset R^4
def stereo(X,pole=np.array([0,0,0,1.0])):
    # project from the pole; require the fibres avoid it
    d=1-X@pole
    return (X-np.outer(X@pole,pole))/d[:,None]
def linking(A,B):
    dA=np.roll(A,-1,axis=0)-A; dB=np.roll(B,-1,axis=0)-B
    mA=A+dA/2; mB=B+dB/2
    R=mA[:,None,:]-mB[None,:,:]
    n=np.linalg.norm(R,axis=2)**3
    cr=np.cross(dA[:,None,:],dB[None,:,:])
    return (np.sum(R*cr,axis=2)/n).sum()/(4*np.pi)
# two fibres over DISTINCT base points of S^2
f1=fibre(1.0+0j, 0.0+0j)                       # base = north pole
f2=fibre(0.6+0j, 0.8+0j)                       # base = another point
A=stereo(f1)[:, :3]; B=stereo(f2)[:, :3]
print("  linking number of two distinct Hopf fibres = %.4f"%linking(A,B))
f3=fibre(0.8+0j, -0.6+0j)
C=stereo(f3)[:,:3]
print("  another pair                              = %.4f"%linking(A,C))
print("  and a third pair                          = %.4f"%linking(B,C))
print("\n  => LINKING = 1, not 0. THE HOPF BUNDLE IS NON-TRIVIAL: S^3 is NOT S^2 x S^1.")
print("     'S^2 x U(1) = SU(2)' is FALSE as a product. It is a non-trivial principal U(1)-bundle,")
print("     and the TWIST (linking 1 = the Hopf invariant) is the whole content.")
