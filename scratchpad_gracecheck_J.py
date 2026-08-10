# Grace INDEPENDENT blind cross-check of Elie's J (toy 5134). NOT a registered toy.
# Built from the STRUCTURAL description only (Keeper K1303 / RUNNING_NOTES), not Elie's code.
# Route: rephasing-invariant Jarlskog via det[H_u,H_d]; report J (not raw det); run 3 controls.
import numpy as np
np.set_printoptions(precision=4, suppress=False)
alpha = 1/137.0
w = np.exp(2j*np.pi/3)   # Z3 / Mobius complex reflection eigenvalue (omega, not -1)

# --- eigenvalues (the two DIFFERENT mechanisms) ---
up = np.array([alpha**2, alpha, 1.0])          # top-saturation {y_u=a^2, y_c=a, y_t=1}
dn = np.array([1.0, 20.0, 840.0])              # down feed-down d:s:b = 1:20:840 (degrees {1,3,5})
Hu_diag = up**2                                 # H = M M^dagger  ~ mass-squared
Hd_diag = dn**2

def rot(i,j,th,ph=0.0):
    R=np.eye(3,dtype=complex); c,s=np.cos(th),np.sin(th)
    R[i,i]=c; R[j,j]=c; R[i,j]=s*np.exp(-1j*ph); R[j,i]=-s*np.exp(1j*ph)
    return R

def Uup(phase):
    # up LEFT-mixing carries the saturation inversion + the Z3 complex reflection,
    # inserted BETWEEN rotations so it cannot be rephased away.
    P=np.diag([1,1,phase]).astype(complex)
    return rot(1,2,0.35) @ P @ rot(0,1,0.22) @ rot(0,2,0.15)

def jarlskog(Hu,Hd):
    # J from the rephasing-invariant commutator identity:
    # det[Hu,Hd] = 2 i J * prod_{i<j}(u_i-u_j) * prod_{i<j}(d_i-d_j)
    C = Hu@Hd - Hd@Hu
    detC = np.linalg.det(C)
    du = np.array(sorted(np.linalg.eigvalsh(Hu)))
    dd = np.array(sorted(np.linalg.eigvalsh(Hd)))
    pu = (du[0]-du[1])*(du[0]-du[2])*(du[1]-du[2])
    pd = (dd[0]-dd[1])*(dd[0]-dd[2])*(dd[1]-dd[2])
    J = np.imag(detC)/(2*pu*pd) if abs(pu*pd)>0 else 0.0
    return J, detC

def build(Uu, Ud=None):
    Ud = np.eye(3,dtype=complex) if Ud is None else Ud
    Hu = Uu @ np.diag(Hu_diag) @ Uu.conj().T
    Hd = Ud @ np.diag(Hd_diag) @ Ud.conj().T
    return Hu,Hd

# --- PHYSICAL build: different mechanisms + Z3 complex phase ---
Uu = Uup(w)
Hu,Hd = build(Uu)
Jphys, detphys = jarlskog(Hu,Hd)

# also J straight from CKM = Uu^dag Ud = Uu^dag (Ud=I) : Im(V_us V_cb V_ub* V_cs*)
V = Uu.conj().T
Jckm = np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))

# --- CONTROLS (must give J=0) ---
J_real,_   = jarlskog(*build(Uup(1.0)))            # real phase (omega->1)
J_align,_  = jarlskog(*build(np.eye(3,dtype=complex)))  # aligned (Uu=I)
J_mirror,_ = jarlskog(*build(Uu, Ud=Uu))           # mirror (Ud=Uu -> V=I)

# --- rephasing invariance: J unchanged under V -> P V (left field rephasing) ---
P=np.diag([np.exp(1j*0.7),np.exp(-1j*1.3),np.exp(1j*2.1)])
Hu_r = P@Hu@P.conj().T
J_reph,_ = jarlskog(Hu_r,Hd)

print(f"PHYSICAL   J (commutator) = {Jphys:+.4e}")
print(f"PHYSICAL   J (CKM Im)     = {Jckm:+.4e}   [same object, cross-check]")
print(f"CONTROL real (w->1)       = {J_real:+.4e}   (must be 0)")
print(f"CONTROL aligned (Uu=I)    = {J_align:+.4e}   (must be 0)")
print(f"CONTROL mirror (Ud=Uu)    = {J_mirror:+.4e}   (must be 0)")
print(f"rephased (P Hu P^dag)     = {J_reph:+.4e}   (must equal physical)")
print(f"observed J_CKM (PDG)      ~ 3.08e-5")
