#!/usr/bin/env python3
"""
THE PROTON RADIUS  [EXPLORATORY]
================================
Toy 81: The proton charge radius r_p from BST geometry.

The proton is a Z_3 baryon circuit on CP^2 subset S^4 subset boundary(D_IV^5).
Its charge radius is the RMS extent of the charge distribution on the
Shilov boundary S^4 x S^1.

The "proton radius puzzle" (2010-2019) was the discrepancy between muonic
(smaller) and electronic (larger) measurements. Now largely resolved
in favor of the smaller value ~0.841 fm.

STATUS: EXPLORATORY. The proton radius has NOT been cleanly derived in BST.
This toy explores candidate geometric formulas and searches for combinations
of BST integers {N_c=3, n_C=5, g=7, C_2=6, N_max=137} that reproduce
the observed r_p = 0.8414 fm.

    from toy_proton_radius import ProtonRadius
    pr = ProtonRadius()
    pr.observed_values()              # CODATA, muonic, electronic
    pr.z3_circuit()                   # proton as Z_3 baryon on CP^2
    pr.cp2_geometry()                 # Fubini-Study metric, length scales
    pr.candidate_formulas()           # several BST geometric candidates
    pr.form_factor()                  # charge distribution from Z_3 circuit
    pr.radius_puzzle()                # muonic vs electronic: BST perspective
    pr.compton_relations()            # lambda_p, lambda_e, their ratios
    pr.integer_search()               # systematic search for r_p from BST integers
    pr.summary()                      # honest: exploratory, best candidates
    pr.show()                         # 4-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import math

# ═══════════════════════════════════════════════════════════════════
# BST CONSTANTS
# ═══════════════════════════════════════════════════════════════════

N_c = 3                # color charges (Z_3 baryon number)
n_C = 5                # complex dimension of D_IV^5
genus = n_C + 2        # = 7
C2 = n_C + 1           # = 6
N_max = 137            # channel capacity per contact

# Physical constants (CODATA 2018)
ALPHA = 1.0 / 137.035999084       # fine structure constant
M_E = 0.51099895000               # electron mass, MeV/c^2
M_P = 938.27208816                 # proton mass, MeV/c^2
HBAR_C = 197.3269804              # hbar*c, MeV*fm
MASS_RATIO = M_P / M_E            # = 1836.15267343

# Derived length scales
LAMBDA_E = HBAR_C / M_E           # electron Compton wavelength, fm (= 386.16 fm)
LAMBDA_P = HBAR_C / M_P           # proton Compton wavelength, fm (= 0.2103 fm)
A_BOHR = LAMBDA_E / ALPHA         # Bohr radius, fm (= 52917.7 fm)
R_CLASSICAL_E = ALPHA * LAMBDA_E  # classical electron radius, fm (= 2.818 fm)

# BST mass relation: m_p = 6*pi^5 * m_e
SIX_PI_FIFTH = 6.0 * math.pi**5   # = 1836.12...

# Observed proton charge radius
R_P_CODATA_2018 = 0.8414          # fm, CODATA 2018
R_P_CODATA_ERR = 0.0019           # fm
R_P_MUONIC = 0.84087              # fm, muonic hydrogen (Pohl et al. 2010, 2013)
R_P_MUONIC_ERR = 0.00039          # fm
R_P_ELECTRONIC_OLD = 0.877        # fm, older electronic H (pre-2019)
R_P_ELECTRONIC_OLD_ERR = 0.013    # fm
R_P_PRad_2019 = 0.831             # fm, PRad at JLab (2019)
R_P_PRad_ERR = 0.012              # fm


# ═══════════════════════════════════════════════════════════════════
# THE PROTON RADIUS CLASS
# ═══════════════════════════════════════════════════════════════════

class ProtonRadius:
    """
    Exploratory BST analysis of the proton charge radius.

    The proton is a Z_3 baryon circuit on CP^2.  Its charge radius
    is determined by the geometry of this circuit and the Fubini-Study
    metric on CP^2 subset S^4 subset Shilov boundary of D_IV^5.

    STATUS: EXPLORATORY -- the proton radius has not yet been cleanly
    derived from BST integers alone.  This toy catalogs candidate
    formulas and their precision against experiment.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        if not quiet:
            self._print_header()

    def _print_header(self):
        print("=" * 68)
        print("  THE PROTON RADIUS  [EXPLORATORY]")
        print("  Z_3 baryon circuit on CP^2 -- charge distribution geometry")
        print(f"  N_c={N_c} | n_C={n_C} | g={genus} | C_2={C2} | "
              f"N_max={N_max}")
        print(f"  r_p(observed) = {R_P_CODATA_2018} +/- {R_P_CODATA_ERR} fm")
        print("=" * 68)

    # --- 1. Observed Values ---

    def observed_values(self) -> dict:
        """
        Experimental measurements of the proton charge radius.
        CODATA 2018, muonic hydrogen, electronic hydrogen.
        """
        measurements = {
            'CODATA 2018':           (R_P_CODATA_2018, R_P_CODATA_ERR),
            'Muonic H (2013)':       (R_P_MUONIC, R_P_MUONIC_ERR),
            'Electronic H (older)':  (R_P_ELECTRONIC_OLD, R_P_ELECTRONIC_OLD_ERR),
            'PRad JLab (2019)':      (R_P_PRad_2019, R_P_PRad_ERR),
        }

        print()
        print("  OBSERVED PROTON CHARGE RADIUS")
        print("  " + "=" * 56)
        print()
        print(f"  {'Measurement':<24} {'r_p (fm)':<14} {'Error (fm)':<12}")
        print("  " + "-" * 50)
        for name, (val, err) in measurements.items():
            print(f"  {name:<24} {val:<14.5f} {err:<12.5f}")
        print()
        print("  The 'proton radius puzzle' (2010-2019):")
        print(f"    Muonic H:      {R_P_MUONIC:.5f} fm  (precise, smaller)")
        print(f"    Electronic H:  {R_P_ELECTRONIC_OLD:.3f} fm  (less precise, larger)")
        print(f"    Discrepancy:   {R_P_ELECTRONIC_OLD - R_P_MUONIC:.3f} fm "
              f"({(R_P_ELECTRONIC_OLD - R_P_MUONIC)/R_P_MUONIC * 100:.1f}%)")
        print()
        print("  Resolution: newer electronic measurements converge toward")
        print("  the muonic value. CODATA 2018 adopts the smaller r_p.")
        print()
        print(f"  BST target: r_p = {R_P_CODATA_2018} +/- {R_P_CODATA_ERR} fm")

        return {
            'measurements': measurements,
            'target_fm': R_P_CODATA_2018,
            'target_err': R_P_CODATA_ERR,
        }

    # --- 2. Z_3 Circuit ---

    def z3_circuit(self) -> dict:
        """
        The proton as a Z_3 baryon circuit on CP^2.
        Three quarks at the three fixed points of the Z_3 action.
        """
        omega = np.exp(2j * np.pi / 3)

        # Fixed points of Z_3 on CP^2
        fp1 = np.array([1, 1, 1], dtype=complex) / np.sqrt(3)
        fp2 = np.array([1, omega, omega**2], dtype=complex) / np.sqrt(3)
        fp3 = np.array([1, omega**2, omega], dtype=complex) / np.sqrt(3)

        # Fubini-Study distance between fixed points
        # d_FS(p, q) = arccos(|<p,q>|)
        ip12 = abs(np.vdot(fp1, fp2))
        ip13 = abs(np.vdot(fp1, fp3))
        ip23 = abs(np.vdot(fp2, fp3))

        d12 = np.arccos(np.clip(ip12, -1, 1))
        d13 = np.arccos(np.clip(ip13, -1, 1))
        d23 = np.arccos(np.clip(ip23, -1, 1))

        # Lefschetz number
        lefschetz = 3  # L(sigma) = 1 + 1 + 1 for Z_3 on CP^2

        # Circuit perimeter (in FS units)
        perimeter = d12 + d13 + d23
        # Circuit radius (circumscribed circle)
        circuit_radius = perimeter / (2 * np.pi) if perimeter > 0 else 0

        print()
        print("  Z_3 BARYON CIRCUIT ON CP^2")
        print("  " + "=" * 56)
        print()
        print("  The proton = Z_3 orbit on CP^2 = three quarks cycling.")
        print()
        print("  Fixed points of sigma: (z0,z1,z2) -> (z1,z2,z0):")
        print(f"    p1 = [1:1:1]       eigenvalue 1")
        print(f"    p2 = [1:w:w^2]     eigenvalue w = e^(2pi*i/3)")
        print(f"    p3 = [1:w^2:w]     eigenvalue w^2")
        print()
        print("  Fubini-Study distances (on CP^2, max = pi/2):")
        print(f"    d(p1,p2) = {d12:.6f} rad = {np.degrees(d12):.2f} deg")
        print(f"    d(p1,p3) = {d13:.6f} rad = {np.degrees(d13):.2f} deg")
        print(f"    d(p2,p3) = {d23:.6f} rad = {np.degrees(d23):.2f} deg")
        print()
        print(f"  Inner products: |<p_i,p_j>| = {ip12:.6f}")
        print(f"  (All equal by Z_3 symmetry)")
        print()
        print(f"  Circuit perimeter: {perimeter:.6f} rad")
        print(f"  Effective radius:  {circuit_radius:.6f} rad")
        print(f"  Lefschetz number:  L(sigma) = {lefschetz}")
        print()
        print("  The charge distribution of the proton is determined by")
        print("  the Z_3 orbit geometry on CP^2 with its Fubini-Study metric.")

        return {
            'fixed_points': [fp1, fp2, fp3],
            'distances': [d12, d13, d23],
            'inner_products': [ip12, ip13, ip23],
            'perimeter': perimeter,
            'circuit_radius': circuit_radius,
            'lefschetz': lefschetz,
        }

    # --- 3. CP^2 Geometry ---

    def cp2_geometry(self) -> dict:
        """
        Fubini-Study metric on CP^2 and natural length scales.
        The CP^2 radius R_FS sets the physical scale.
        """
        # CP^n has real dimension 2n.  CP^2 has dim_R = 4.
        # Its curvature radius in units of Fubini-Study metric is 1.
        # Physical radius: R = (some function of alpha, Compton wavelengths)

        dim_cp2 = 4       # real dimension
        chi_cp2 = 3        # Euler characteristic
        c1_cp2 = 3         # first Chern number of CP^2 (c_1 = 3h)
        vol_cp2 = 0.5      # vol(CP^2) = pi^2/2 in FS units (radius=1)

        # In BST, the Shilov boundary S^4 x S^1 contains CP^2.
        # The physical scale is set by the proton Compton wavelength.
        R_FS_phys = LAMBDA_P  # Compton wavelength as natural unit

        # The Z_3 orbit has circumradius on CP^2:
        # For equilateral triangle inscribed in a circle on CP^2,
        # the circumradius is r_circ = perimeter / (2*pi)
        omega = np.exp(2j * np.pi / 3)
        fp = np.array([1, 1, 1], dtype=complex) / np.sqrt(3)
        fq = np.array([1, omega, omega**2], dtype=complex) / np.sqrt(3)
        d_FS = np.arccos(np.clip(abs(np.vdot(fp, fq)), -1, 1))
        r_circ = 3 * d_FS / (2 * np.pi)  # circumradius of Z_3 triangle

        print()
        print("  CP^2 GEOMETRY")
        print("  " + "=" * 56)
        print()
        print(f"  dim_R(CP^2) = {dim_cp2}")
        print(f"  chi(CP^2)   = {chi_cp2}  (Euler characteristic)")
        print(f"  c_1(CP^2)   = {c1_cp2}   (first Chern number)")
        print(f"  vol(CP^2)   = pi^2/2 = {vol_cp2 * np.pi**2:.6f}  (FS metric)")
        print()
        print("  Embedding: CP^2 subset S^4 subset Shilov(D_IV^5)")
        print(f"  S^4 is the 4-sphere boundary of the 5-ball.")
        print()
        print("  Natural length scale of CP^2 in BST:")
        print(f"    lambda_p = hbar/(m_p c) = {LAMBDA_P:.6f} fm")
        print(f"    lambda_e = hbar/(m_e c) = {LAMBDA_E:.4f} fm")
        print(f"    lambda_e/lambda_p = m_p/m_e = {MASS_RATIO:.2f}")
        print(f"                      ~ 6*pi^5  = {SIX_PI_FIFTH:.2f}")
        print()
        print(f"  Z_3 triangle on CP^2:")
        print(f"    FS distance between fixed points: {d_FS:.6f} rad = pi/2")
        print(f"    FS circumradius of Z_3 triangle:  {r_circ:.6f}")
        print()
        print("  KEY OBSERVATION:")
        r_4lp = 4 * LAMBDA_P
        pct_4 = (r_4lp - R_P_CODATA_2018) / R_P_CODATA_2018 * 100
        print(f"    r_p = 4 * lambda_p = {r_4lp:.6f} fm  ({pct_4:+.4f}%)")
        print(f"    and 4 = dim_R(CP^2)!")
        print()
        print("  The charge radius equals dim_R(CP^2) times the proton")
        print("  Compton wavelength. This may be the BST formula:")
        print("    r_p = dim_R(CP^2) * hbar/(m_p c)")

        return {
            'dim_R': dim_cp2,
            'chi': chi_cp2,
            'c1': c1_cp2,
            'vol_FS': vol_cp2 * np.pi**2,
            'd_FS': d_FS,
            'r_circ': r_circ,
            'lambda_p': LAMBDA_P,
            'lambda_e': LAMBDA_E,
        }

    # --- 4. Candidate Formulas ---

    def candidate_formulas(self) -> dict:
        """
        Several BST geometric candidate formulas for r_p.
        Compared to r_p(obs) = 0.8414 fm.
        """
        target = R_P_CODATA_2018

        candidates = {}

        # --- Simple dimensional candidates ---

        # 0. r_p = 4 * lambda_p = dim_R(CP^2) * lambda_p  *** BEST ***
        r0 = 4 * LAMBDA_P
        candidates['4*lambda_p = dim_R(CP^2)*lambda_p'] = r0

        # 1. r_p = N_c * lambda_p
        r1 = N_c * LAMBDA_P
        candidates['N_c * lambda_p'] = r1

        # 2. r_p = sqrt(genus) * lambda_p
        r2 = np.sqrt(genus) * LAMBDA_P
        candidates['sqrt(g) * lambda_p'] = r2

        # 3. r_p = C_2/genus * lambda_p / alpha
        r3 = (C2 / genus) * LAMBDA_P / ALPHA
        candidates['(C_2/g) * lambda_p/alpha'] = r3

        # 4. r_p = alpha * lambda_e / (2*pi)
        r4 = ALPHA * LAMBDA_E / (2 * np.pi)
        candidates['alpha*lambda_e/(2*pi)'] = r4

        # 5. r_p = N_c * alpha * lambda_e / (2*pi)
        r5 = N_c * ALPHA * LAMBDA_E / (2 * np.pi)
        candidates['N_c*alpha*lambda_e/(2*pi)'] = r5

        # --- Z_3 circuit geometry candidates ---

        # 6. FS distance * lambda_p / alpha
        omega = np.exp(2j * np.pi / 3)
        fp = np.array([1, 1, 1], dtype=complex) / np.sqrt(3)
        fq = np.array([1, omega, omega**2], dtype=complex) / np.sqrt(3)
        d_FS = np.arccos(np.clip(abs(np.vdot(fp, fq)), -1, 1))
        r6 = d_FS * LAMBDA_P / ALPHA
        candidates['d_FS * lambda_p/alpha'] = r6

        # 7. r_p = (2/3) * FS_distance * lambda_p / alpha
        r7 = (2.0 / 3.0) * d_FS * LAMBDA_P / ALPHA
        candidates['(2/3)*d_FS*lambda_p/alpha'] = r7

        # 8. r_p = classical_e_radius * (m_e/m_p)^(1/3)
        r8 = R_CLASSICAL_E * (M_E / M_P) ** (1.0/3.0)
        candidates['r_e * (m_e/m_p)^(1/3)'] = r8

        # 9. r_p = 4 * alpha^2 * lambda_p / (N_c/n_C)
        # Motivated: alpha^2 from two EM vertices, N_c/n_C geometry
        r9 = 4 * ALPHA**2 * LAMBDA_E * (N_c / n_C)
        candidates['4*alpha^2*lambda_e*(N_c/n_C)'] = r9

        # 10. r_p = (N_c/pi) * lambda_p * sqrt(C_2)
        r10 = (N_c / np.pi) * LAMBDA_P * np.sqrt(C2)
        candidates['(N_c/pi)*lambda_p*sqrt(C_2)'] = r10

        # 11. r_p = lambda_p * (N_c + 1/alpha^(1/3))
        # Motivated: leading integer + sub-leading EM correction
        r11 = LAMBDA_P * (N_c + 1.0 / ALPHA**(1.0/3.0))
        candidates['lambda_p*(N_c+alpha^(-1/3))'] = r11

        # 12. r_p = (2/pi) * N_c * lambda_e * alpha
        r12 = (2.0 / np.pi) * N_c * LAMBDA_E * ALPHA
        candidates['(2/pi)*N_c*lambda_e*alpha'] = r12

        # 13. r_p = sqrt(N_c * n_C / (4*pi)) * lambda_p / alpha^(2/3)
        r13 = np.sqrt(N_c * n_C / (4 * np.pi)) * LAMBDA_P / ALPHA**(2.0/3.0)
        candidates['sqrt(N_c*n_C/(4pi))*lambda_p/alpha^(2/3)'] = r13

        # 14. r_p = N_c * lambda_p + alpha * lambda_p
        r14 = (N_c + ALPHA) * LAMBDA_P
        candidates['(N_c + alpha)*lambda_p'] = r14

        # 15. r_p = (4/n_C) * lambda_p / alpha
        r15 = (4.0 / n_C) * LAMBDA_P / ALPHA
        candidates['(4/n_C)*lambda_p/alpha'] = r15

        # Sort by closeness to target
        scored = []
        for name, val in candidates.items():
            if val > 0:
                pct = (val - target) / target * 100
                scored.append((name, val, pct))
        scored.sort(key=lambda x: abs(x[2]))

        print()
        print("  CANDIDATE BST FORMULAS FOR r_p")
        print("  " + "=" * 56)
        print(f"  Target: r_p = {target} fm (CODATA 2018)")
        print()
        print(f"  {'Formula':<42} {'r_p (fm)':<12} {'Error %':<10}")
        print("  " + "-" * 62)
        for name, val, pct in scored:
            marker = " <--" if abs(pct) < 5 else ""
            print(f"  {name:<42} {val:<12.6f} {pct:+8.2f}%{marker}")
        print()

        if scored:
            best_name, best_val, best_pct = scored[0]
            print(f"  BEST: {best_name}")
            print(f"        r_p = {best_val:.6f} fm  ({best_pct:+.2f}%)")
        else:
            best_name, best_val, best_pct = 'none', 0, 100

        return {
            'candidates': candidates,
            'ranked': scored,
            'best': (best_name, best_val, best_pct),
            'target': target,
        }

    # --- 5. Form Factor ---

    def form_factor(self) -> dict:
        """
        The proton electromagnetic form factor from the Z_3 charge distribution.
        G_E(q^2) is the Fourier transform of the charge density.
        """
        # For a Z_3-symmetric charge distribution on S^2 (projected from CP^2),
        # the charge density is a sum of three Gaussians at 120 deg intervals.
        #
        # In the simplest model: rho(r) = (1/r_0^3) * exp(-r/r_0)
        # gives G_E(q^2) = 1/(1 + q^2 r_0^2)^2  (dipole form factor)
        #
        # The actual QCD form factor is well described by the dipole form:
        #   G_E(Q^2) = G_D(Q^2) = 1/(1 + Q^2/0.71)^2
        # where Q^2 is in (GeV/c)^2.

        Q2_dipole = 0.71  # GeV^2 (dipole mass parameter)

        # From dipole: <r^2> = 12/Lambda^2 where Lambda^2 = Q2_dipole
        r_dipole = np.sqrt(12.0 / Q2_dipole) * HBAR_C / 1000  # convert to fm
        # (HBAR_C is in MeV*fm, Q2 is in GeV^2)
        r_dipole_fm = np.sqrt(12.0 / (Q2_dipole * 1e6)) * HBAR_C  # fm

        # Better: Lambda^2 = 0.71 GeV^2 = 710000 MeV^2
        # <r^2> = 12 * (hbar*c)^2 / Lambda^2
        r2_dipole = 12.0 * HBAR_C**2 / (Q2_dipole * 1e6)  # fm^2
        r_from_dipole = np.sqrt(r2_dipole)

        # q^2 range for plotting
        Q2 = np.linspace(0, 5, 500)  # GeV^2

        # Standard dipole
        GE_dipole = 1.0 / (1.0 + Q2 / Q2_dipole)**2

        # Z_3 modification: three-body interference
        # G_E^(Z3)(Q^2) = G_D(Q^2) * [1 + 2*cos(Q*d_12)]
        # where d_12 is the Z_3 separation scale
        # This is speculative -- exploring the pattern
        d_Z3 = R_P_CODATA_2018 / np.sqrt(N_c)  # characteristic Z_3 scale
        Q_fm = np.sqrt(Q2) * 1000 / HBAR_C  # convert to fm^-1
        GE_z3 = GE_dipole * (1.0 + 2.0 * np.cos(Q_fm * d_Z3)) / 3.0

        print()
        print("  PROTON FORM FACTOR")
        print("  " + "=" * 56)
        print()
        print("  Standard dipole form factor:")
        print("    G_E(Q^2) = 1/(1 + Q^2/0.71 GeV^2)^2")
        print()
        print(f"  Dipole mass: Lambda^2 = {Q2_dipole} GeV^2")
        print(f"  Implies <r^2> = 12*(hbar*c)^2/Lambda^2")
        print(f"         r_p = sqrt(<r^2>) = {r_from_dipole:.4f} fm")
        print()
        print("  Z_3 modification (SPECULATIVE):")
        print("    G_E^(Z3) = G_D * [1 + 2*cos(Q*d_Z3)] / 3")
        print(f"    d_Z3 = r_p/sqrt(N_c) = {d_Z3:.4f} fm")
        print("    Three quarks contribute coherently at low Q^2,")
        print("    producing interference fringes at high Q^2.")
        print()
        print("  BST interpretation:")
        print("  The dipole form factor arises because the Z_3 charge")
        print("  distribution on CP^2 is exponential in the geodesic")
        print("  distance from the Z_3 centroid.")

        return {
            'Q2': Q2,
            'GE_dipole': GE_dipole,
            'GE_z3': GE_z3,
            'Q2_dipole': Q2_dipole,
            'r_from_dipole': r_from_dipole,
            'd_Z3': d_Z3,
        }

    # --- 6. Radius Puzzle ---

    def radius_puzzle(self) -> dict:
        """
        The proton radius puzzle: muonic vs electronic measurements.
        BST perspective on why different probes might see different radii.
        """
        r_muonic = R_P_MUONIC
        r_electronic = R_P_ELECTRONIC_OLD
        discrepancy = r_electronic - r_muonic
        sigma_disc = discrepancy / R_P_ELECTRONIC_OLD_ERR  # in sigma

        # Muon mass
        m_mu = 105.6583755  # MeV
        lambda_mu = HBAR_C / m_mu  # muon Compton wavelength

        # Bohr radii
        a_bohr_e = A_BOHR  # electronic Bohr radius
        a_bohr_mu = HBAR_C / (ALPHA * m_mu)  # muonic Bohr radius

        ratio = a_bohr_e / a_bohr_mu  # = m_mu/m_e

        print()
        print("  THE PROTON RADIUS PUZZLE")
        print("  " + "=" * 56)
        print()
        print("  The puzzle (2010-2019):")
        print(f"    Muonic H:        r_p = {r_muonic:.5f} +/- {R_P_MUONIC_ERR} fm")
        print(f"    Electronic H:    r_p = {r_electronic:.3f} +/- {R_P_ELECTRONIC_OLD_ERR} fm")
        print(f"    Discrepancy:     {discrepancy:.3f} fm ({sigma_disc:.1f} sigma)")
        print()
        print("  Probe comparison:")
        print(f"    electron Compton: {LAMBDA_E:.2f} fm  >> r_p")
        print(f"    muon Compton:     {lambda_mu:.4f} fm  ~ 2*r_p")
        print(f"    proton Compton:   {LAMBDA_P:.4f} fm   < r_p")
        print()
        print(f"    e^- Bohr radius:  {a_bohr_e:.1f} fm")
        print(f"    mu^- Bohr radius: {a_bohr_mu:.2f} fm")
        print(f"    Ratio a_e/a_mu = m_mu/m_e = {ratio:.1f}")
        print()
        print("  The muon orbits ~207x closer than the electron,")
        print("  probing the charge distribution much more precisely.")
        print()
        print("  BST perspective:")
        print("    In BST, the proton is a Z_3 circuit on CP^2.")
        print("    The charge radius is a geometric property of this circuit.")
        print("    There is ONE radius -- it does not depend on the probe.")
        print("    The puzzle was experimental, not theoretical.")
        print()
        print("  Current status (2024+):")
        print("    Newer electronic measurements agree with muonic value.")
        print(f"    Best value: r_p = {R_P_CODATA_2018} +/- {R_P_CODATA_ERR} fm")

        return {
            'r_muonic': r_muonic,
            'r_electronic': r_electronic,
            'discrepancy': discrepancy,
            'sigma': sigma_disc,
            'lambda_mu': lambda_mu,
            'a_bohr_mu': a_bohr_mu,
            'probe_ratio': ratio,
        }

    # --- 7. Compton Relations ---

    def compton_relations(self) -> dict:
        """
        Proton and electron Compton wavelengths and their BST relations.
        """
        ratio = LAMBDA_E / LAMBDA_P  # = m_p/m_e

        # BST: m_p = 6*pi^5 * m_e
        bst_ratio = SIX_PI_FIFTH
        pct_mass = (bst_ratio - ratio) / ratio * 100

        # Various length ratios
        r_over_lambda_p = R_P_CODATA_2018 / LAMBDA_P
        r_over_lambda_e = R_P_CODATA_2018 / LAMBDA_E
        r_over_r_cl_e = R_P_CODATA_2018 / R_CLASSICAL_E
        r_over_bohr = R_P_CODATA_2018 / A_BOHR

        # What integer/fraction is r_p/lambda_p closest to?
        nice_fracs = [
            (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
            (1, 2), (3, 2), (5, 2), (7, 2),
            (1, 3), (2, 3), (4, 3), (5, 3), (7, 3), (8, 3),
            (1, 4), (3, 4), (5, 4), (7, 4),
            (1, 5), (2, 5), (3, 5), (4, 5), (6, 5), (7, 5),
            (1, 6), (5, 6), (7, 6),
            (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
        ]

        closest_frac = None
        closest_err = 1e10
        for p, q in nice_fracs:
            err = abs(r_over_lambda_p - p/q)
            if err < closest_err:
                closest_err = err
                closest_frac = (p, q)

        print()
        print("  COMPTON WAVELENGTH RELATIONS")
        print("  " + "=" * 56)
        print()
        print(f"  lambda_e = hbar/(m_e c) = {LAMBDA_E:.4f} fm")
        print(f"  lambda_p = hbar/(m_p c) = {LAMBDA_P:.6f} fm")
        print(f"  ratio = lambda_e/lambda_p = m_p/m_e = {ratio:.5f}")
        print()
        print(f"  BST mass relation: m_p = 6*pi^5 * m_e")
        print(f"    6*pi^5 = {bst_ratio:.5f}  ({pct_mass:+.4f}%)")
        print()
        print("  Dimensionless ratios of r_p to key length scales:")
        print(f"    r_p / lambda_p       = {r_over_lambda_p:.6f}")
        print(f"    r_p / lambda_e       = {r_over_lambda_e:.8f}")
        print(f"    r_p / r_e(classical) = {r_over_r_cl_e:.6f}")
        print(f"    r_p / a_Bohr         = {r_over_bohr:.2e}")
        print()
        print(f"  r_p / lambda_p = {r_over_lambda_p:.4f}")
        print(f"    ~ {r_over_lambda_p:.1f} proton Compton wavelengths")
        if closest_frac:
            p, q = closest_frac
            frac_val = p / q
            frac_err = (r_over_lambda_p - frac_val) / r_over_lambda_p * 100
            print(f"    Nearest simple fraction: {p}/{q} = {frac_val:.4f} "
                  f"({frac_err:+.1f}%)")
        print()
        print(f"  r_p * m_p / (hbar*c) = r_p / lambda_p = {r_over_lambda_p:.4f}")
        print(f"  This is the proton radius in natural units (hbar = c = 1).")

        return {
            'lambda_e': LAMBDA_E,
            'lambda_p': LAMBDA_P,
            'mass_ratio': ratio,
            'bst_ratio': bst_ratio,
            'r_over_lambda_p': r_over_lambda_p,
            'r_over_lambda_e': r_over_lambda_e,
            'r_over_r_cl_e': r_over_r_cl_e,
            'closest_fraction': closest_frac,
        }

    # --- 8. Integer Search ---

    def integer_search(self) -> dict:
        """
        Systematic search for r_p from combinations of BST integers.
        Tries all formulas of the form:
            r_p = (a/b) * alpha^p * lambda_p   (various a, b, p)
        """
        target = R_P_CODATA_2018

        # BST integers and small numbers to try
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 137]
        denoms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
        # alpha powers to try
        alpha_pows = [-2, -1, -2/3, -1/2, -1/3, 0, 1/3, 1/2, 2/3, 1, 2]
        # pi powers to try
        pi_pows = [-1, 0, 1]

        results = []

        for a in nums:
            for b in denoms:
                if a == b:
                    continue
                for ap in alpha_pows:
                    for pp in pi_pows:
                        val = (a / b) * ALPHA**ap * np.pi**pp * LAMBDA_P
                        if 0.1 < val < 10:  # reasonable range
                            pct = (val - target) / target * 100
                            if abs(pct) < 2.0:  # within 2%
                                label = f"({a}/{b})"
                                if ap != 0:
                                    if ap == int(ap):
                                        label += f"*alpha^{int(ap)}"
                                    else:
                                        label += f"*alpha^({ap:.2g})"
                                if pp != 0:
                                    label += f"*pi^{int(pp)}"
                                label += "*lambda_p"
                                results.append((label, val, pct, a, b, ap, pp))

        # Also try lambda_e based formulas
        for a in nums:
            for b in denoms:
                if a == b:
                    continue
                for ap in alpha_pows:
                    for pp in pi_pows:
                        val = (a / b) * ALPHA**ap * np.pi**pp * LAMBDA_E
                        if 0.1 < val < 10:
                            pct = (val - target) / target * 100
                            if abs(pct) < 2.0:
                                label = f"({a}/{b})"
                                if ap != 0:
                                    if ap == int(ap):
                                        label += f"*alpha^{int(ap)}"
                                    else:
                                        label += f"*alpha^({ap:.2g})"
                                if pp != 0:
                                    label += f"*pi^{int(pp)}"
                                label += "*lambda_e"
                                results.append((label, val, pct, a, b, ap, pp))

        # Sort by precision
        results.sort(key=lambda x: abs(x[2]))

        print()
        print("  SYSTEMATIC INTEGER SEARCH")
        print("  " + "=" * 56)
        print(f"  Target: r_p = {target} fm")
        print(f"  Search: (a/b) * alpha^p * pi^q * lambda_{{e,p}}")
        print(f"  Filter: within 2% of target")
        print()

        if results:
            print(f"  Found {len(results)} candidates within 2%:")
            print()
            n_show = min(20, len(results))
            print(f"  {'Formula':<45} {'r_p (fm)':<12} {'Error %':<10}")
            print("  " + "-" * 65)
            for label, val, pct, a, b, ap, pp in results[:n_show]:
                bst = ""
                if a in [N_c, n_C, genus, C2, N_max] or \
                   b in [N_c, n_C, genus, C2]:
                    bst = " [BST]"
                print(f"  {label:<45} {val:<12.6f} {pct:+8.4f}%{bst}")
            if len(results) > n_show:
                print(f"  ... and {len(results) - n_show} more")
        else:
            print("  No candidates found within 2% with this search grid.")

        print()
        print("  Note: the search is over simple rational multiples of")
        print("  alpha^p * lambda_p or alpha^p * lambda_e.  The true BST")
        print("  formula may involve transcendental combinations from the")
        print("  Fubini-Study metric on CP^2.")

        return {
            'results': results[:20] if results else [],
            'n_found': len(results),
            'target': target,
        }

    # --- 9. Summary ---

    def summary(self) -> dict:
        """
        Honest summary: proton radius is exploratory in BST.
        Best candidates and open questions.
        """
        # Run candidate search quietly
        candidates = {}

        # A few best candidates to highlight
        r_4lp = 4 * LAMBDA_P
        r_3lp = N_c * LAMBDA_P
        r_alpha_e = (3.0 / 10.0) * ALPHA * LAMBDA_E

        target = R_P_CODATA_2018

        highlights = [
            ('4*lambda_p = dim_R(CP^2)*lambda_p', r_4lp, (r_4lp - target)/target * 100),
            ('N_c * lambda_p',                     r_3lp, (r_3lp - target)/target * 100),
            ('(3/10)*alpha*lambda_e',             r_alpha_e, (r_alpha_e - target)/target * 100),
        ]
        highlights.sort(key=lambda x: abs(x[2]))

        r_over_lambda_p = target / LAMBDA_P

        print()
        print("  " + "=" * 56)
        print("  SUMMARY: THE PROTON RADIUS  [EXPLORATORY]")
        print("  " + "=" * 56)
        print()
        print(f"  Observed: r_p = {target} +/- {R_P_CODATA_ERR} fm")
        print(f"           = {r_over_lambda_p:.4f} * lambda_p")
        print()
        print("  The proton is a Z_3 baryon circuit on CP^2.")
        print("  Its charge radius is the RMS extent of the")
        print("  charge distribution on the Shilov boundary S^4 x S^1.")
        print()
        print("  *** KEY FINDING ***")
        print(f"    r_p = 4 * lambda_p = {4*LAMBDA_P:.6f} fm  "
              f"({(4*LAMBDA_P - target)/target * 100:+.4f}%)")
        print(f"    and 4 = dim_R(CP^2)!")
        print()
        print("  If this is the formula, then:")
        print("    r_p = dim_R(CP^2) * hbar / (m_p c)")
        print("        = dim_R(CP^2) / (6*pi^5 * m_e c / hbar)")
        print("    Pure geometry: real dimension of the space on which")
        print("    the Z_3 baryon circuit lives, times the proton Compton")
        print("    wavelength. Precision: 0.02%.")
        print()
        print("  What we KNOW from BST:")
        print(f"    - m_p = 6*pi^5 * m_e  (0.002%)")
        print(f"    - Proton = Z_3 circuit on CP^2")
        print(f"    - dim_R(CP^2) = 4")
        print(f"    - Form factor ~ dipole (exponential charge density)")
        print()
        print("  All highlighted candidates:")
        for name, val, pct in highlights:
            marker = " ***" if abs(pct) < 0.1 else ""
            print(f"    {name:<40} = {val:.4f} fm  ({pct:+.2f}%){marker}")
        print()
        print("  STATUS: The r_p = 4*lambda_p relation (0.02%) is striking")
        print("  but requires a rigorous derivation from the CP^2 charge")
        print("  distribution. Why dim_R(CP^2) and not, say, chi(CP^2)=3?")
        print()
        print("  The proton radius puzzle (muonic vs electronic)")
        print("  is resolved experimentally: both agree on ~0.841 fm.")
        print("  BST predicts ONE radius -- geometry has no probe dependence.")

        return {
            'status': 'EXPLORATORY',
            'target_fm': target,
            'r_over_lambda_p': r_over_lambda_p,
            'highlights': highlights,
        }

    # --- 10. Show (4-panel visualization) ---

    def show(self):
        """
        4-panel visualization of the proton radius in BST.
        """
        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        import matplotlib.patheffects as pe

        BG = '#0a0a1a'
        CYAN = '#00ccff'
        GOLD = '#ffd700'
        GREEN = '#44ff88'
        RED = '#ff4444'
        ORANGE = '#ff8800'
        PURPLE = '#aa66ff'
        WHITE = '#ffffff'
        GREY = '#888888'
        DGREY = '#444444'

        fig = plt.figure(figsize=(16, 11), facecolor=BG)
        fig.canvas.manager.set_window_title('Proton Radius -- BST [EXPLORATORY]')

        fig.text(0.5, 0.97, 'THE PROTON RADIUS  [EXPLORATORY]',
                 fontsize=22, fontweight='bold', color=CYAN, ha='center',
                 fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=2, foreground='#004466')])
        fig.text(0.5, 0.94,
                 f'Z_3 baryon circuit on CP^2  |  r_p = {R_P_CODATA_2018} fm  |  '
                 f'N_c={N_c}, n_C={n_C}, g={genus}',
                 fontsize=11, color='#88aacc', ha='center', fontfamily='monospace')

        # ── Panel 1: Z_3 triangle on CP^2 ──
        ax1 = fig.add_axes([0.05, 0.52, 0.42, 0.38])
        ax1.set_facecolor(BG)
        ax1.set_aspect('equal')
        ax1.set_xlim(-2.0, 2.0)
        ax1.set_ylim(-2.0, 2.0)
        ax1.set_title('Z_3 Baryon Circuit on CP^2', color='#cccccc',
                       fontsize=13, fontfamily='monospace', pad=10)

        # CP^2 boundary
        theta = np.linspace(0, 2*np.pi, 200)
        ax1.plot(1.5*np.cos(theta), 1.5*np.sin(theta),
                 color='#333366', linewidth=1, linestyle=':')
        ax1.text(0, 1.7, 'CP^2 (Fubini-Study)', fontsize=9, color='#666688',
                 ha='center', fontfamily='monospace')

        # Three fixed points
        fp_pos = [(0, 1.2), (-1.05, -0.6), (1.05, -0.6)]
        fp_colors = [RED, GREEN, '#4488ff']
        fp_labels = ['u (red)', 'd (green)', 'u (blue)']
        fp_coords = ['[1:1:1]', '[1:w:w^2]', '[1:w^2:w]']

        for (x, y), col, lab, coord in zip(fp_pos, fp_colors, fp_labels, fp_coords):
            circle = plt.Circle((x, y), 0.25, color=col, alpha=0.15)
            ax1.add_patch(circle)
            ax1.plot(x, y, 'o', color=col, markersize=16, zorder=5)
            ax1.text(x, y + 0.4, lab, fontsize=9, color=col, ha='center',
                     fontfamily='monospace', fontweight='bold')
            ax1.text(x, y - 0.35, coord, fontsize=7, color=GREY, ha='center',
                     fontfamily='monospace')

        # Triangle
        tri_x = [fp_pos[0][0], fp_pos[1][0], fp_pos[2][0], fp_pos[0][0]]
        tri_y = [fp_pos[0][1], fp_pos[1][1], fp_pos[2][1], fp_pos[0][1]]
        ax1.plot(tri_x, tri_y, color=WHITE, linewidth=1, alpha=0.3, linestyle='--')
        ax1.fill(tri_x, tri_y, color=WHITE, alpha=0.02)

        # Circumradius indicator
        cx, cy = 0.0, 0.0
        r_circ_vis = 1.2  # visual circumradius
        circ = plt.Circle((cx, cy), r_circ_vis, fill=False, color=GOLD,
                           linewidth=1, linestyle=':', alpha=0.4)
        ax1.add_patch(circ)
        ax1.annotate('', xy=(r_circ_vis, 0), xytext=(0, 0),
                      arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))
        ax1.text(r_circ_vis/2, -0.15, 'r_p', fontsize=12, color=GOLD,
                 ha='center', fontfamily='monospace', fontweight='bold')

        ax1.text(0, -1.7, f'r_p = {R_P_CODATA_2018} fm', fontsize=12,
                 color=GOLD, ha='center', fontfamily='monospace', fontweight='bold')

        for spine in ax1.spines.values():
            spine.set_color('#333366')
        ax1.tick_params(colors='#666688')

        # ── Panel 2: Candidate formulas comparison ──
        ax2 = fig.add_axes([0.55, 0.52, 0.42, 0.38])
        ax2.set_facecolor(BG)
        ax2.set_title('Candidate Formulas vs Observed', color='#cccccc',
                       fontsize=13, fontfamily='monospace', pad=10)

        target = R_P_CODATA_2018

        # Selected candidates (focused on physically interesting ones)
        cand_names = [
            '4*lambda_p = dim_R(CP^2)*lambda_p',
            '(3/10)*alpha*lambda_e',
            'N_c * lambda_p',
            'sqrt(g)*lambda_p',
            '(N_c/pi)*lambda_p*sqrt(C_2)',
        ]
        cand_vals = [
            4 * LAMBDA_P,
            (3.0/10.0) * ALPHA * LAMBDA_E,
            N_c * LAMBDA_P,
            np.sqrt(genus) * LAMBDA_P,
            (N_c/np.pi) * LAMBDA_P * np.sqrt(C2),
        ]

        # Sort by proximity
        indexed = list(enumerate(zip(cand_names, cand_vals)))
        indexed.sort(key=lambda x: abs(x[1][1] - target))

        y_positions = np.arange(len(cand_names))
        colors_bar = [GOLD, CYAN, GREEN, PURPLE, ORANGE]

        # Plot horizontal bars
        for rank, (idx, (name, val)) in enumerate(indexed):
            pct = (val - target) / target * 100
            col = colors_bar[rank]
            lw = 2.5 if abs(pct) < 0.1 else 0
            ax2.barh(rank, val, height=0.6, color=col, alpha=0.7,
                      edgecolor=col if lw > 0 else 'none', linewidth=lw)
            ax2.text(max(val, target) + 0.02, rank, f'{pct:+.2f}%',
                     fontsize=10, color=col, va='center',
                     fontfamily='monospace',
                     fontweight='bold' if abs(pct) < 0.1 else 'normal')
            ax2.text(0.02, rank + 0.32, name, fontsize=7,
                     color=WHITE, va='center', fontfamily='monospace', alpha=0.9)

        # Target line
        ax2.axvline(target, color=GOLD, linewidth=2, linestyle='--', alpha=0.8)
        ax2.text(target + 0.02, len(cand_names) - 0.3,
                 f'observed\n{target} fm', fontsize=9, color=GOLD,
                 fontfamily='monospace', va='bottom')

        ax2.set_yticks([])
        ax2.set_xlabel('r_p (fm)', color=GREY, fontfamily='monospace')
        ax2.set_xlim(0, max(max(cand_vals), target) * 1.3)
        for spine in ax2.spines.values():
            spine.set_color('#333366')
        ax2.tick_params(colors='#666688')

        # ── Panel 3: Form factor ──
        ax3 = fig.add_axes([0.05, 0.07, 0.42, 0.38])
        ax3.set_facecolor(BG)
        ax3.set_title('Proton Form Factor G_E(Q^2)', color='#cccccc',
                       fontsize=13, fontfamily='monospace', pad=10)

        Q2 = np.linspace(0, 4, 500)
        Q2_dipole = 0.71
        GE_dipole = 1.0 / (1.0 + Q2 / Q2_dipole)**2

        # Z_3 modification
        d_Z3 = R_P_CODATA_2018 / np.sqrt(N_c)
        Q_fm = np.sqrt(np.maximum(Q2, 0)) * 1000 / HBAR_C
        GE_z3 = GE_dipole * (1.0 + 2.0 * np.cos(Q_fm * d_Z3)) / 3.0

        ax3.semilogy(Q2, GE_dipole, color=CYAN, linewidth=2,
                      label='Dipole: 1/(1+Q^2/0.71)^2')
        ax3.semilogy(Q2, np.abs(GE_z3), color=ORANGE, linewidth=1.5,
                      linestyle='--', alpha=0.8,
                      label='Z_3 modification (speculative)')
        ax3.set_xlabel('Q^2 (GeV^2)', color=GREY, fontfamily='monospace')
        ax3.set_ylabel('|G_E(Q^2)|', color=GREY, fontfamily='monospace')
        ax3.set_ylim(1e-4, 1.5)
        ax3.legend(fontsize=8, loc='upper right', facecolor=BG, edgecolor='#333366',
                   labelcolor=WHITE)
        ax3.axhline(1, color=DGREY, linewidth=0.5, linestyle=':')

        # Annotate the dipole mass
        ax3.annotate(f'Lambda^2 = {Q2_dipole} GeV^2',
                      xy=(Q2_dipole, 1/(1+1)**2), xytext=(2.0, 0.3),
                      fontsize=9, color=CYAN, fontfamily='monospace',
                      arrowprops=dict(arrowstyle='->', color=CYAN, lw=1))

        for spine in ax3.spines.values():
            spine.set_color('#333366')
        ax3.tick_params(colors='#666688')

        # ── Panel 4: Length scale comparison ──
        ax4 = fig.add_axes([0.55, 0.07, 0.42, 0.38])
        ax4.set_facecolor(BG)
        ax4.set_title('Length Scales in BST', color='#cccccc',
                       fontsize=13, fontfamily='monospace', pad=10)

        # Log scale comparison of length scales
        scales = {
            'a_Bohr':        A_BOHR,
            'lambda_e':      LAMBDA_E,
            'r_e(classical)': R_CLASSICAL_E,
            'r_p (observed)': R_P_CODATA_2018,
            'lambda_p':      LAMBDA_P,
        }

        y_pos = np.arange(len(scales))
        scale_colors = ['#6688ff', CYAN, GREEN, GOLD, RED]
        scale_names = list(scales.keys())
        scale_vals = list(scales.values())

        for i, (name, val) in enumerate(scales.items()):
            ax4.barh(i, np.log10(val), height=0.6, color=scale_colors[i],
                      alpha=0.7)
            ax4.text(np.log10(val) + 0.1, i, f'{val:.4g} fm',
                     fontsize=9, color=scale_colors[i], va='center',
                     fontfamily='monospace')

        ax4.set_yticks(y_pos)
        ax4.set_yticklabels(scale_names, fontfamily='monospace', color=WHITE,
                             fontsize=9)
        ax4.set_xlabel('log10(r / fm)', color=GREY, fontfamily='monospace')

        # Mark r_p
        ax4.axvline(np.log10(R_P_CODATA_2018), color=GOLD, linewidth=1.5,
                     linestyle='--', alpha=0.5)

        # Annotate relations
        ax4.text(np.log10(R_P_CODATA_2018) - 0.3, len(scales) - 0.3,
                 'r_p = ? * lambda_p',
                 fontsize=9, color=GOLD, fontfamily='monospace',
                 fontweight='bold', alpha=0.8)

        for spine in ax4.spines.values():
            spine.set_color('#333366')
        ax4.tick_params(colors='#666688')

        # Bottom annotation
        r_bst = 4 * LAMBDA_P
        pct_bst = (r_bst - R_P_CODATA_2018) / R_P_CODATA_2018 * 100
        fig.text(0.5, 0.015,
                 f'[EXPLORATORY]  r_p = 4*lambda_p = dim_R(CP^2) * hbar/(m_p c) '
                 f'= {r_bst:.6f} fm  ({pct_bst:+.4f}%)',
                 fontsize=10, color=GOLD, ha='center', fontfamily='monospace',
                 fontweight='bold')

        plt.show(block=False)


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    pr = ProtonRadius()

    print()
    print("  What would you like to explore?")
    print("   1) Observed values -- CODATA, muonic, electronic")
    print("   2) Z_3 circuit -- proton as Z_3 baryon on CP^2")
    print("   3) CP^2 geometry -- Fubini-Study metric, length scales")
    print("   4) Candidate formulas -- BST geometric candidates")
    print("   5) Form factor -- charge distribution from Z_3 circuit")
    print("   6) Radius puzzle -- muonic vs electronic: BST perspective")
    print("   7) Compton relations -- lambda_p, lambda_e, ratios")
    print("   8) Integer search -- systematic search from BST integers")
    print("   9) Summary -- honest status and best candidates")
    print("  10) Full analysis + 4-panel visualization")
    print()

    try:
        choice = input("  Choice [1-10]: ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = '10'

    if choice == '1':
        pr.observed_values()
    elif choice == '2':
        pr.z3_circuit()
    elif choice == '3':
        pr.cp2_geometry()
    elif choice == '4':
        pr.candidate_formulas()
    elif choice == '5':
        pr.form_factor()
    elif choice == '6':
        pr.radius_puzzle()
    elif choice == '7':
        pr.compton_relations()
    elif choice == '8':
        pr.integer_search()
    elif choice == '9':
        pr.summary()
    elif choice == '10':
        pr.observed_values()
        pr.z3_circuit()
        pr.cp2_geometry()
        pr.candidate_formulas()
        pr.form_factor()
        pr.radius_puzzle()
        pr.compton_relations()
        pr.integer_search()
        pr.summary()
        try:
            pr.show()
            input("\n  Press Enter to close...")
        except Exception as e:
            print(f"  Visualization: {e}")
    else:
        pr.summary()


if __name__ == '__main__':
    main()
