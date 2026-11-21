# Pre-registration: boundary correction to induced G (written before any computation)
Date: 2026-11-20 ~21:00 EST. Author: Claude, at Casey's request.

Model: D = D_IV^5 (Harish-Chandra realisation) viewed as a region of its compact dual Q^5,
with Q^5's own symmetric (compact) Kaehler metric, Kaehler potential log(1 + 2|z|^2 + |z.z|^2).
Its edge {h = 0}, h = 1 - 2|z|^2 + |z.z|^2, is then at finite distance.

Heat-kernel coefficient of the Einstein-Hilbert order (Gilkey/Branson, pure Laplacian,
same for Dirichlet and Neumann at this order):  (1/6) [ INT_D tau dV + 2 INT_dD L_aa dA ].
Define rho = 2 INT_dD L_aa dA / INT_D tau dV  (dimensionless, independent of heat time and
of the overall metric scale). Induced G_eff = G_bulk / (1 + rho).

Target: the ladder m_e = 6 pi^5 alpha^12 m_Pl gives G 0.0650% too HIGH, so success needs
rho = +6.5e-4.  PASS iff 5.2e-4 <= rho <= 7.8e-4 (+-20%). Anything else, including the
right size with the wrong sign, is a FAIL, reported as such. No second definition counts.
Validation first: the same code must reproduce Gauss-Bonnet (INT tau + 2 INT L = 4 pi) on a
spherical cap in CP^1.
