# Pre-registration: resonance (discrete-mode) correction at alpha-ladder steps
Written before computing. 2026-11-20 ~21:50 EST.
Spectrum: scalar Laplacian on Q^5 = SO(7)/[SO(5)xSO(2)], eigenvalues p(p+5)+q(q+3) on SO(7) irreps (p,q,0);
the spherical set (all p>=q>=0, or p=q mod 2) chosen by the check a1/a0 = R/6 = 5/6 (corpus normalisation).
Resonance correction: C(t) = Z_exact(t)/Z_smooth(t) - 1, Z_smooth = heat-kernel asymptotic series (a_k fitted at
very small t, where discreteness is negligible).
Ladder steps: t_k = alpha^k, k = 1..24 (corpus eigenvalue normalisation; alpha = 1/137.036).
My prediction: |C(t_k)| < 1e-10 for every k >= 1 (discrete corrections on a compact symmetric space are
exponentially small, ~exp(-l^2/4t), l = shortest closed geodesic).
Casey's hypothesis PASSES iff C(t_12) or C(t_24) lies within +-20% of -3.25e-4 (prefactor) or -6.5e-4 (G).
A hit at any other k is reported as a look-elsewhere candidate, not a pass. Also reported: the scale t* where
|C| first reaches 3.25e-4, and whether t* is near any alpha^k.
