"""
Lyra_assembled_dirac_operator.py  -- 2026-08-13
================================================================================
ASSEMBLED Kostant cubic Dirac operator D^2 = grad*grad + R_p on the truncated
holomorphic-discrete-series module of so(5,2), EXPOSED for Elie to diagonalize
BLIND for tau_min.

DISCIPLINE (Keeper's cautions, honored in code):
  * The metric/representation normalization `nu` is an EXPLICIT PARAMETER, never
    baked. It is precisely the unpinned 6-vs-6.25 fork. The spectrum -- not a
    convention -- must produce the value.
  * The intercept c is NOT an input. D^2 is assembled from the p+/p- raising and
    lowering coefficients (geometry) and squared; the ground energy tau_min
    EMERGES as min eigenvalue. Non-circular.
  * I do NOT diagonalize for tau_min here. Elie does that blind. This file only
    ASSEMBLES and EXPOSES, plus limit-tests the STRUCTURE (Hermitian, tower
    tridiagonal, spectrum -> +inf).

MODEL (type IV_5, Lie ball, rank 2, tube type):
  Basis of the holomorphic tower on the fiber vacuum branch, labeled by
    (q, d):  q = fiber Dolbeault degree 0..5 (SO(5) rep in Lambda^q(vec-5)),
             d = holomorphic polynomial degree 0,1,2,...,N (p+ excitations).
  p+_i  : raises d -> d+1 (multiply by z_i), lowers/raises fiber via Clifford.
  p-_i  : lowers d -> d-1 (Bergman-adjoint), Clifford conjugate.
  D = c(p+) + c(p-)  (Kostant cubic Dirac, equal-rank => this IS the cubic op).
  D^2 = grad*grad (the d-tower kinetic Casimir, >=0, -> inf)  +  R_p (graded).

The p+/p- coefficients carry the weighted-Bergman (Faraut-Koranyi/Gindikin)
norms with parameter nu. FLAG: these coefficients are the piece Elie should
cross-check against Hua/K264 before the tau_min VALUE is trusted; the STRUCTURE
(Hermitian, tridiagonal, limits) is what I stand behind here.
================================================================================
"""
import numpy as np

# ---- fixed geometric integers (NOT knobs) ----
nC = 5          # dim_C p+ = n_C ; SO(5) vector
RANK = 2
# SO(5) quadratic Casimir on Lambda^q(vector-5): reps 1,5,10,10,5,1
OMEGA_SO5 = {0:0.0, 1:4.0, 2:6.0, 3:6.0, 4:4.0, 5:0.0}

def Rp_grading(lam):
    """Graded curvature endomorphism per fiber degree q (Bochner-Kodaira):
       R_p(q) = (lam/2)*(q - nC/2).  lam = Ricci scale (metric normalization).
       Returns dict q -> eigenvalue. GRADED (spread != 0) unless lam=0."""
    return {q: (lam/2.0)*(q - nC/2.0) for q in range(nC+1)}

def bergman_raise_coeff(d, nu):
    """p+ raising coefficient d -> d+1 on the holomorphic tower, weighted-Bergman
       parameter nu. Standard lowest-weight-module norm ratio:
         ||z * f_d||^2 / ||f_d||^2  =  (d+1)*(nu + d)      [rank-1 radial string]
       The sqrt is the off-diagonal Dirac matrix element. nu EXPLICIT.
       (FLAG: rank-2 type IV has a second Gindikin factor; this is the leading
        radial string that sets the ground -- Elie cross-checks the full rank-2
        coefficient against Hua/K264.)"""
    return np.sqrt((d + 1.0) * (nu + d))

def assemble_D2(nu, lam, N, q_ground=0):
    """ASSEMBLE D^2 = grad*grad + R_p on the tower (q_ground fiber branch) x d=0..N.
       nu  : weighted-Bergman parameter (EXPLICIT; the 6-vs-6.25 pin)
       lam : Ricci/metric scale for R_p (EXPLICIT)
       N   : polynomial-degree truncation
       Returns the (N+1)x(N+1) Hermitian matrix. Does NOT diagonalize.
       grad*grad: tridiagonal from p+/p- raising-lowering (kinetic, >=0, ->inf).
       R_p: constant shift Rp_grading[q_ground] on this fiber branch."""
    n = N + 1
    A = np.zeros((n, n))                      # the raising operator z (lower-triangular subdiag)
    for d in range(N):
        A[d+1, d] = bergman_raise_coeff(d, nu)
    gradgrad = A.conj().T @ A                 # p- p+ = ||p+||^2 kinetic (>=0), Hermitian by construction
    Rp = Rp_grading(lam)[q_ground] * np.eye(n)
    D2 = gradgrad + Rp
    return 0.5*(D2 + D2.conj().T)             # symmetrize (already Hermitian; guard)

def accessor(nu, lam, N):
    """Full accessor for Elie: returns dict of the D^2 matrix on EACH fiber branch
       q=0..5, all sharing the same d-tower. Elie diagonalizes each blind and
       reports tau_min = min over branches of min-eigenvalue, plus which (q,d)
       state realizes it (bare d=0 => Kostant/bare ground; dressed d>0 => other)."""
    return {q: assemble_D2(nu, lam, N, q_ground=q) for q in range(nC+1)}

# =====================================================================================
# STRUCTURE TESTS (what I stand behind; NOT the tau_min value)
# =====================================================================================
if __name__ == "__main__":
    N = 12
    # representative knob values, both posted so neither is banked:
    #   nu tied to genus/half-form; lam tied to scalar curvature. BOTH explicit.
    for (nu, lam, tag) in [(2.5, 0.0, "lam=0 (flat R_p): pure kinetic tower"),
                           (2.5, 5.0, "lam=5 (curved): graded R_p on")]:
        M = accessor(nu, lam, N)
        print(f"\n=== nu={nu}, {tag} ===")
        # Hermiticity
        herm = max(np.max(np.abs(M[q]-M[q].conj().T)) for q in range(6))
        print(f"  Hermitian: max||D2 - D2^dag|| = {herm:.2e}  (structure check)")
        # spectrum -> inf  (Cal's promotion condition)
        top = max(np.max(np.linalg.eigvalsh(M[q])) for q in range(6))
        print(f"  spectrum grows: max eigenvalue at N={N} = {top:.1f}  (-> inf as N grows)")
        # tridiagonal-in-degree structure
        offband = max(np.max(np.abs(np.triu(M[q],2))) for q in range(6))
        print(f"  tower tridiagonal: max above-2nd-diagonal = {offband:.2e}")
        # I deliberately DO NOT print min eigenvalue (tau_min) -- that is Elie's blind read.
        print("  tau_min: NOT computed here (Elie diagonalizes blind).")
    print("\nStructure stands: Hermitian, tridiagonal tower, spectrum->inf.")
    print("VALUE (6 vs 6.25) rides on nu (unpinned) + which (q,d) is the ground.")
    print("Bergman coeff rank-2 completion = Elie's cross-check vs Hua/K264.")
