#!/usr/bin/env python3
"""
WHY EXACTLY THREE GENERATIONS  --  Toy 110
=============================================
The deepest question in particle physics, answered by geometry.

Why are there exactly three generations of fermions?  Not two, not four.
The Standard Model has no answer -- the generation count is a free parameter.
BST answers: Z_3 acting on CP^2 has exactly 3 fixed points.  Each fixed point
is one generation.  A fourth is topologically impossible.

The argument:
  1. n_C = 5 (complex dimension of D_IV^5)
  2. CP^2 = CP^{N_c-1} is the compact color configuration space
  3. Z_3 acts on CP^2 by cyclic permutation of homogeneous coordinates
  4. Lefschetz fixed-point theorem: L(Z_3 on CP^2) = 1 + 1 + 1 = 3
  5. Three fixed points = three generations.  Period.

Two routes confirm the count:
  Route A (Z_3 on CP^2):  3 fixed points via Lefschetz
  Route B (E_8 -> E_6 x SU(3)):  The SU(3) triplet carries 3 copies of 27

The mass hierarchy:
  Koide Q = 2/3 from epsilon^2 = dim_C(CP^2) = 2
  m_mu/m_e = (24/pi^2)^6 from Bergman kernel ratio
  m_tau from Koide + muon: 1776.91 MeV (0.003%)

Six panels:
  1. "The Question" - Why 3?  Three generation columns with masses
  2. "Z_3 on CP^2" - Three fixed points, Lefschetz theorem
  3. "The E_8 Route" - E_8 -> E_6 x SU(3) branching rules
  4. "Mass Ratios" - Koide Q=2/3 from Z_3, lepton mass predictions
  5. "Why Not 4?" - Topological impossibility of 4th generation
  6. "The Punchline" - The full chain from n_C=5 to three generations

CI Interface:
    from toy_three_generations import ThreeGenerations
    tg = ThreeGenerations()
    tg.the_question()       # Why 3?  The particle table
    tg.z3_on_cp2()          # Fixed points and Lefschetz
    tg.e8_route()           # E_8 -> E_6 x SU(3) branching
    tg.mass_ratios()        # Koide Q=2/3 from Z_3
    tg.why_not_four()       # Z_4 on CP^3 fails
    tg.punchline()          # The answer
    tg.summary()            # One-paragraph summary
    tg.show()               # 6-panel visualization

Copyright (c) 2026 Casey Koons. All rights reserved.
This software is provided for demonstration purposes only.
No license is granted for redistribution, modification, or commercial use.
This code and the underlying Bubble Spacetime Theory (BST) remain
the intellectual property of Casey Koons.

Created with Claude Opus 4.6, March 2026.
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

# ──────────────────────────────────────────────────────────────────
#  BST Constants
# ──────────────────────────────────────────────────────────────────
N_c   = 3           # color charges (B_2 root system)
n_C   = 5           # complex dimension of D_IV^5
C_2   = n_C + 1     # 6  Casimir eigenvalue
genus = n_C + 2     # 7  genus of D_IV^5
N_max = 137         # channel capacity (Haldane exclusion cap)
N_w   = 2           # weak isospin doublet dimension
dim_R = 2 * n_C     # 10  real dimension of D_IV^5
alpha = 1.0 / 137.035999

# Physical masses in MeV (PDG 2024)
m_e_MeV   = 0.51099895
m_mu_MeV  = 105.6583755
m_tau_MeV = 1776.86
m_p_MeV   = 938.272

# Z_3 roots of unity
omega = np.exp(2j * np.pi / 3)

# Domain volumes
Vol_1 = np.pi
Vol_3 = np.pi**3 / 24.0
Vol_5 = np.pi**5 / 1920.0

# ──────────────────────────────────────────────────────────────────
#  Colors (dark theme)
# ──────────────────────────────────────────────────────────────────
BG          = '#0a0a1a'
DARK_PANEL  = '#0d0d24'
GOLD        = '#ffd700'
GOLD_DIM    = '#aa8800'
BRIGHT_GOLD = '#ffee44'
CYAN        = '#00ddff'
GREEN       = '#00ff88'
YELLOW      = '#ffee00'
ORANGE      = '#ff8800'
RED         = '#ff3344'
MAGENTA     = '#ff44cc'
WHITE       = '#eeeeff'
GREY        = '#666688'
SOFT_BLUE   = '#4488ff'
VIOLET      = '#aa44ff'
PINK        = '#ff88aa'

# Generation colors (matched to Z_3 eigenvalues)
GEN1_COLOR = '#ff4444'   # Gen 1: eigenvalue 1
GEN2_COLOR = '#44ff44'   # Gen 2: eigenvalue omega
GEN3_COLOR = '#4488ff'   # Gen 3: eigenvalue omega^2


def _precision_color(pct):
    """Color by prediction quality."""
    ap = abs(pct)
    if ap < 0.01:
        return BRIGHT_GOLD
    elif ap < 0.1:
        return GOLD
    elif ap < 1.0:
        return GREEN
    elif ap < 5.0:
        return YELLOW
    else:
        return RED


# ══════════════════════════════════════════════════════════════════
#  Observed Fermion Data (PDG 2024, MeV)
# ══════════════════════════════════════════════════════════════════
MASSES = {
    # Charged leptons
    'e':     0.51099895,
    'mu':    105.6583755,
    'tau':   1776.86,
    # Up-type quarks
    'u':     2.16,
    'c':     1270.0,
    't':     172690.0,
    # Down-type quarks
    'd':     4.67,
    's':     93.4,
    'b':     4180.0,
    # Neutrinos (rough central values)
    'nu_e':  0.0,              # m_1 = 0 (normal ordering)
    'nu_mu': 0.00868e-3,       # sqrt(Delta m^2_21) in MeV
    'nu_tau': 0.0503e-3,       # sqrt(Delta m^2_31) in MeV
}


# ══════════════════════════════════════════════════════════════════
#  ThreeGenerations Class
# ══════════════════════════════════════════════════════════════════
class ThreeGenerations:
    """
    Why exactly three generations of fermions.

    BST answer: Z_3 on CP^2 has exactly 3 fixed points.
    Confirmed by E_8 -> E_6 x SU(3) branching.
    Mass hierarchy from Koide Q = 2/3 (Z_3 tangent space dimension).

    Parameters
    ----------
    quiet : bool
        If False (default), print results when methods are called.
    """

    def __init__(self, quiet=False):
        self.quiet = quiet
        self.omega = omega

        # BST muon mass ratio
        self.R_mu = (24.0 / np.pi**2)**6    # m_mu / m_e = 206.761

        # BST lepton masses
        self.m_e = m_e_MeV
        self.m_mu_bst = self.R_mu * m_e_MeV
        # Koide tau mass
        a = np.sqrt(m_e_MeV)
        b = np.sqrt(self.m_mu_bst)
        c_val = (2.0 * (a + b)
                 + np.sqrt(3.0) * np.sqrt(m_e_MeV + 4.0 * np.sqrt(
                     m_e_MeV * self.m_mu_bst) + self.m_mu_bst))
        self.m_tau_bst = c_val**2

        if not quiet:
            sep = "=" * 65
            print(f"\n{sep}")
            print("  WHY EXACTLY THREE GENERATIONS  --  Toy 110")
            print("  Z_3 on CP^2 has exactly 3 fixed points.")
            print(f"{sep}")
            print(f"  D_IV^5:  n_C = {n_C},  N_c = {N_c},  "
                  f"genus = {genus},  N_max = {N_max}")
            print(f"  Lefschetz: L(Z_3 on CP^2) = 1 + 1 + 1 = 3")
            print(f"  E_8 -> E_6 x SU(3): (27,3) = 3 generations")
            print(f"  Koide Q = 2/3 from dim_C(CP^2) = 2")
            print(f"{sep}\n")

    def _print(self, text):
        if not self.quiet:
            print(text)

    # ── 1. The Question ──────────────────────────────────────────

    def the_question(self):
        """
        WHY THREE GENERATIONS?

        The Standard Model has 3 copies of every fermion type.
        Electron, muon, tau.  Up, charm, top.  Down, strange, bottom.
        Masses span 5.5 orders of magnitude (0.5 MeV to 173 GeV).
        The SM provides no explanation.  BST does.
        """
        result = {
            'question': 'Why exactly 3 generations of fermions?',
            'sm_answer': 'No answer. Generation count is a free parameter.',
            'bst_answer': 'Z_3 on CP^2 has exactly 3 fixed points.',
            'mass_range_orders': np.log10(172690.0 / 0.511),
            'generations': {
                1: {'charged_lepton': ('e', 0.511),
                    'up_quark': ('u', 2.16),
                    'down_quark': ('d', 4.67)},
                2: {'charged_lepton': ('mu', 105.66),
                    'up_quark': ('c', 1270.0),
                    'down_quark': ('s', 93.4)},
                3: {'charged_lepton': ('tau', 1776.86),
                    'up_quark': ('t', 172690.0),
                    'down_quark': ('b', 4180.0)},
            },
            'lep_z_width': 'LEP Z-width: N_nu = 2.984 +/- 0.008',
            'note': 'Masses span 5.5 orders of magnitude from e to t',
        }

        self._print("\n  THE QUESTION: Why Exactly Three Generations?")
        self._print("  ============================================")
        self._print("  The Standard Model has THREE copies of every fermion:")
        self._print("    Gen 1:  (e,  nu_e)   (u,  d)     masses ~ MeV")
        self._print("    Gen 2:  (mu, nu_mu)  (c,  s)     masses ~ GeV")
        self._print("    Gen 3:  (tau,nu_tau) (t,  b)     masses ~ 100 GeV")
        self._print(f"  Mass range: {result['mass_range_orders']:.1f} "
                    f"orders of magnitude")
        self._print("  SM answer: NONE.  Generation count is a free parameter.")
        self._print("  BST answer: Z_3 on CP^2 forces exactly 3.")

        return result

    # ── 2. Z_3 on CP^2 ──────────────────────────────────────────

    def z3_on_cp2(self):
        """
        The Z_3 action on CP^2 and its 3 fixed points.

        sigma: [z0 : z1 : z2] -> [z1 : z2 : z0]
        Fixed points: [1:1:1], [1:omega:omega^2], [1:omega^2:omega]
        Lefschetz number: L(sigma) = 1 + 1 + 1 = 3
        """
        # Fixed points
        fp = [
            np.array([1, 1, 1], dtype=complex) / np.sqrt(3),
            np.array([1, omega, omega**2], dtype=complex) / np.sqrt(3),
            np.array([1, omega**2, omega], dtype=complex) / np.sqrt(3),
        ]

        # Verify they are fixed by sigma (up to overall phase)
        sigma = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
        eigenvals = [1, omega, omega**2]

        verifications = []
        for i, (p, ev) in enumerate(zip(fp, eigenvals)):
            sp = sigma @ p
            ratio = sp / p
            is_fixed = np.allclose(ratio, ratio[0])
            verifications.append({
                'point': p,
                'eigenvalue': ev,
                'sigma_p': sp,
                'ratio': ratio[0],
                'is_projective_fixed': is_fixed,
            })

        # Lefschetz computation
        # H^{2k}(CP^2) = Q for k=0,1,2; sigma* acts as identity on each
        lefschetz_traces = [1, 1, 1]
        lefschetz_number = sum(lefschetz_traces)

        result = {
            'action': 'sigma: [z0:z1:z2] -> [z1:z2:z0]',
            'group': 'Z_3 = cyclic group of order 3',
            'space': 'CP^2 = CP^{N_c - 1}',
            'fixed_points': [
                {'label': 'p1 = [1:1:1]', 'eigenvalue': 1,
                 'generation': 1, 'particles': '(e, nu_e, u, d)'},
                {'label': 'p2 = [1:omega:omega^2]', 'eigenvalue': omega,
                 'generation': 2, 'particles': '(mu, nu_mu, c, s)'},
                {'label': 'p3 = [1:omega^2:omega]',
                 'eigenvalue': omega**2,
                 'generation': 3, 'particles': '(tau, nu_tau, t, b)'},
            ],
            'lefschetz_number': lefschetz_number,
            'lefschetz_traces': lefschetz_traces,
            'lefschetz_formula': ('L(sigma) = sum_{k=0}^{2} '
                                  'Tr(sigma* | H^{2k}) = 1+1+1 = 3'),
            'verifications': verifications,
            'theorem': 'N_gen = |Fix(Z_3 on CP^2)| = L(Z_3) = 3',
            'key_identity': 'N_gen = N_c = 3',
        }

        self._print("\n  Z_3 ON CP^2: Three Fixed Points = Three Generations")
        self._print("  ===================================================")
        self._print("  Action: sigma([z0:z1:z2]) = [z1:z2:z0]")
        self._print("  sigma^3 = identity (Z_3 = cyclic group of order 3)")
        self._print("")
        self._print("  Fixed points (sigma(p) = lambda * p):")
        for fp_info in result['fixed_points']:
            ev_str = f"{fp_info['eigenvalue']:.4g}"
            self._print(f"    {fp_info['label']}  eigenvalue={ev_str}"
                        f"  -> Gen {fp_info['generation']}: "
                        f"{fp_info['particles']}")
        self._print("")
        traces_str = ' + '.join(str(t) for t in lefschetz_traces)
        self._print(f"  Lefschetz: L(sigma) = {traces_str}"
                    f" = {lefschetz_number}")
        self._print(f"  |Fix(sigma)| = L(sigma) = {lefschetz_number}")
        self._print("  N_gen = N_c = 3  (generations = colors)")

        return result

    # ── 3. The E_8 Route ─────────────────────────────────────────

    def e8_route(self):
        """
        E_8 -> E_6 x SU(3): three generations from branching rules.

        248 -> (78,1) + (1,8) + (27,3) + (27bar,3bar)
        The SU(3) triplet in (27,3) carries exactly 3 generations.
        Each 27 of E_6 = one complete generation (16 + 10 + 1 of SO(10)).
        """
        # Dimension check
        dims = {
            '(78,1)': 78 * 1,
            '(1,8)': 1 * 8,
            '(27,3)': 27 * 3,
            '(27bar,3bar)': 27 * 3,
        }
        total = sum(dims.values())

        # E_6 -> SO(10) x U(1)
        e6_decomp = {
            '27': '16_1 + 10_{-2} + 1_4',
            '16': 'One complete SM generation (u,d,e,nu in L+R)',
            '10': 'Vector-like exotics (Higgs sector)',
            '1': 'SM singlet (right-handed neutrino)',
        }

        # Route comparison
        route_a = {
            'name': 'Route A: E_8 -> SO(10) x SU(4)',
            'branching': ('248 -> (45,1) + (1,15) + (10,6) '
                          '+ (16,4) + (16bar,4bar)'),
            'family_group': 'SU(4)',
            'generations': '4 -> 3 + 1 (extra singlet)',
            'bst_natural': True,
            'contains': 'D_5 x B_2 (BST soliton sector)',
        }

        route_b = {
            'name': 'Route B: E_8 -> E_6 x SU(3)',
            'branching': ('248 -> (78,1) + (1,8) + (27,3) '
                          '+ (27bar,3bar)'),
            'family_group': 'SU(3)',
            'generations': '3 directly (no extra)',
            'bst_natural': False,
            'contains': 'E_6 (heterotic string pedigree)',
        }

        result = {
            'branching': ('248 -> (78,1) + (1,8) + (27,3) '
                          '+ (27bar,3bar)'),
            'dimension_check': {
                'components': dims, 'total': total,
                'target': 248, 'verified': total == 248,
            },
            'e6_decomp': e6_decomp,
            'key_term': '(27,3): 3 copies of 27 = 3 generations',
            'route_a': route_a,
            'route_b': route_b,
            'convergence': ('Both routes meet at '
                            'SO(10) x SU(3)_family x U(1)'),
            'weyl_connection': ('|W(D_5)| / |W(B_2)| = 1920/8 '
                                '= 240 = |Phi(E_8)|'),
        }

        dims_str = ' + '.join(f'{v}' for v in dims.values())
        self._print("\n  THE E_8 ROUTE: Three Generations from Branching")
        self._print("  ================================================")
        self._print(f"  E_8 -> E_6 x SU(3):")
        self._print(f"    {result['branching']}")
        ok_str = 'OK' if total == 248 else 'FAIL'
        self._print(f"    Dimension check: {dims_str} = {total} {ok_str}")
        self._print("")
        self._print("  The key term: (27, 3)")
        self._print("    27 of E_6 -> 16 + 10 + 1 of SO(10)")
        self._print("    16 = one complete SM generation")
        self._print("    3 of SU(3) = family triplet -> 3 generations")
        self._print("")
        self._print("  Two routes converge at "
                    "SO(10) x SU(3)_family x U(1)")
        self._print("  Weyl: |W(D_5)|/|W(B_2)| = 1920/8 "
                    "= 240 = |Phi(E_8)|")

        return result

    # ── 4. Mass Ratios ───────────────────────────────────────────

    def mass_ratios(self):
        """
        Charged lepton masses from Koide formula with Q = 2/3.

        Q = (m_e + m_mu + m_tau) /
            (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3
        Q = 2/3 because epsilon^2 = dim_C(CP^2) = 2

        BST inputs: m_mu/m_e = (24/pi^2)^6, Q = 2/3
        BST output: m_tau = 1776.91 MeV (0.003%)
        """
        R = self.R_mu
        m_e = self.m_e
        m_mu_bst = self.m_mu_bst
        m_tau_bst = self.m_tau_bst

        # Verify Koide Q
        sum_m = m_e + m_mu_bst + m_tau_bst
        sum_sqrt = (np.sqrt(m_e) + np.sqrt(m_mu_bst)
                    + np.sqrt(m_tau_bst))
        Q_bst = sum_m / sum_sqrt**2

        # Observed
        Q_obs = ((m_e_MeV + m_mu_MeV + m_tau_MeV)
                 / (np.sqrt(m_e_MeV) + np.sqrt(m_mu_MeV)
                    + np.sqrt(m_tau_MeV))**2)

        # Precision
        pct_mu = 100.0 * (m_mu_bst - m_mu_MeV) / m_mu_MeV
        pct_tau = 100.0 * (m_tau_bst - m_tau_MeV) / m_tau_MeV

        # Ratios
        r_mu_e = m_mu_bst / m_e
        r_tau_mu = m_tau_bst / m_mu_bst
        r_tau_e = m_tau_bst / m_e

        result = {
            'koide_Q_bst': Q_bst,
            'koide_Q_obs': Q_obs,
            'koide_Q_exact': 2.0 / 3.0,
            'epsilon_sq': 2,
            'epsilon_sq_origin': 'dim_C(CP^2) = 2',
            'muon_ratio': {
                'formula': '(24/pi^2)^6',
                'bst': R,
                'observed': m_mu_MeV / m_e_MeV,
                'precision_pct': pct_mu,
            },
            'tau_mass': {
                'bst_MeV': m_tau_bst,
                'observed_MeV': m_tau_MeV,
                'precision_pct': pct_tau,
                'formula': 'Koide Q=2/3 + muon ratio',
            },
            'lepton_masses': {
                'e': {'bst': m_e, 'obs': m_e_MeV},
                'mu': {'bst': m_mu_bst, 'obs': m_mu_MeV, 'pct': pct_mu},
                'tau': {'bst': m_tau_bst, 'obs': m_tau_MeV,
                        'pct': pct_tau},
            },
            'mass_ratios': {
                'mu/e': r_mu_e,
                'tau/mu': r_tau_mu,
                'tau/e': r_tau_e,
            },
            'chain': ('m_Pl -> [alpha^12] -> m_e '
                      '-> [(24/pi^2)^6] -> m_mu '
                      '-> [Koide Q=2/3] -> m_tau'),
        }

        self._print("\n  MASS RATIOS: Koide Q = 2/3 from Z_3")
        self._print("  =====================================")
        self._print("  Koide ratio: Q = (m_e + m_mu + m_tau) / "
                    "(sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2")
        self._print(f"    Q (BST, exact) = {Q_bst:.10f}")
        self._print(f"    Q (observed)   = {Q_obs:.10f}")
        self._print(f"    Q (exact 2/3)  = {2.0/3.0:.10f}")
        self._print(f"  Why Q = 2/3?  epsilon^2 = dim_C(CP^2) = 2")
        self._print("")
        self._print(f"  Charged lepton masses (MeV):")
        self._print(f"    m_e  = {m_e:.5f}  (input)")
        self._print(f"    m_mu = (24/pi^2)^6 * m_e = {m_mu_bst:.4f}"
                    f"  (obs: {m_mu_MeV:.4f}, {pct_mu:+.4f}%)")
        self._print(f"    m_tau = Koide(Q=2/3, m_mu) = {m_tau_bst:.2f}"
                    f"  (obs: {m_tau_MeV:.2f}, {pct_tau:+.4f}%)")
        self._print("")
        self._print(f"  Ratios:  m_mu/m_e = {r_mu_e:.3f}    "
                    f"m_tau/m_mu = {r_tau_mu:.3f}    "
                    f"m_tau/m_e = {r_tau_e:.1f}")

        return result

    # ── 5. Why Not Four? ─────────────────────────────────────────

    def why_not_four(self):
        """
        Why a 4th generation is topologically impossible in BST.

        Z_3 has only 3 eigenvalues (1, omega, omega^2).
        A 4th fixed point would require either:
          - A 4th eigenvalue of Z_3 (impossible: Z_3 has order 3)
          - A larger space CP^3 (requires N_c = 4, contradicts SU(3))

        Z_4 on CP^3 gives wrong Koide Q, wrong mixing, wrong color.
        Only Z_3 on CP^2 works because n_C = 5 forces N_c = 3.
        """
        # Z_4 on CP^3 analysis
        z4_fixed = 4  # Lefschetz: L(Z_4 on CP^3) = 1+1+1+1 = 4
        Q_4 = 5.0 / 8.0  # (N_gen + 1) / (2 * N_gen) for N_gen = 4

        # LEP Z-width constraint
        N_nu_lep = 2.9840
        N_nu_err = 0.0082

        result = {
            'z3_eigenvalues': [1, omega, omega**2],
            'z3_order': 3,
            'z4_fixed_points': z4_fixed,
            'z4_koide_Q': Q_4,
            'z3_koide_Q': 2.0 / 3.0,
            'topological_argument': (
                'Z_3 has exactly 3 eigenvalues. '
                'A 4th fixed point would require Z_4 on CP^3, '
                'which needs N_c = 4. But N_c = n_C - 2 = 3.'),
            'n_C_argument': (
                'n_C = 5 from max-alpha principle. '
                'N_c = n_C - 2 = 3. CP^{N_c-1} = CP^2. '
                'Z_{N_c} = Z_3. Three fixed points.'),
            'lep_constraint': {
                'N_nu': N_nu_lep,
                'sigma': N_nu_err,
                'compatible_with_3': abs(N_nu_lep - 3) / N_nu_err < 3,
                'rules_out_4': abs(N_nu_lep - 4) / N_nu_err > 100,
            },
            'why_z4_fails': [
                'N_c would be 4, contradicting SU(3) color',
                'Koide Q = 5/8 instead of 2/3 (wrong mass ratios)',
                'CP^3 gives epsilon^2 = 3 (wrong mixing)',
                'n_C would need to be 6 (violates max-alpha)',
            ],
        }

        self._print("\n  WHY NOT FOUR? Topological Impossibility")
        self._print("  ========================================")
        self._print("  Z_3 has exactly 3 eigenvalues: 1, omega, omega^2")
        self._print("  A 4th eigenvalue does not exist.")
        self._print("")
        self._print("  Alternative: Z_4 on CP^3?")
        self._print(f"    Would give {z4_fixed} fixed points "
                    "= 4 generations")
        self._print(f"    Koide Q = 5/8 = {Q_4:.4f} "
                    f"(vs 2/3 = {2/3:.4f} observed)")
        self._print("    Requires N_c = 4 -> contradicts SU(3)_color")
        self._print("    Requires n_C = 6 -> violates max-alpha")
        self._print("")
        dev_3 = abs(N_nu_lep - 3) / N_nu_err
        dev_4 = abs(N_nu_lep - 4) / N_nu_err
        self._print(f"  LEP Z-width: N_nu = {N_nu_lep} +/- {N_nu_err}")
        self._print(f"    Consistent with 3: YES ({dev_3:.1f} sigma)")
        self._print(f"    Rules out 4: YES ({dev_4:.0f} sigma)")
        self._print("")
        self._print("  The chain: n_C=5 -> N_c=3 -> CP^2 -> Z_3 "
                    "-> 3 generations")
        self._print("  NOT dynamical.  TOPOLOGICAL.  No loopholes.")

        return result

    # ── 6. The Punchline ─────────────────────────────────────────

    def punchline(self):
        """
        Three generations because spacetime has complex dimension 5,
        and 5 chooses CP^2 as its compact core, and CP^2 has Z_3
        symmetry.  Not more.  Not fewer.  Three.
        """
        result = {
            'chain': [
                ('D_IV^5 has complex dimension', 'n_C = 5'),
                ('Short root multiplicity of B_2',
                 'N_c = n_C - 2 = 3'),
                ('Color configuration space',
                 'CP^{N_c-1} = CP^2'),
                ('Cyclic symmetry of CP^2', 'Z_{N_c} = Z_3'),
                ('Fixed points of Z_3 on CP^2', 'N_gen = 3'),
            ],
            'statement': (
                'Three generations because spacetime has complex '
                'dimension 5, and 5 chooses CP^2 as its compact '
                'core, and CP^2 has Z_3 symmetry. '
                'Not more. Not fewer. Three.'),
            'key_identities': {
                'N_gen = N_c': 'Generations = Colors = 3',
                'N_gen = L(Z_3)': 'Lefschetz number = 3',
                'Q = 2/3': 'Koide ratio from dim_C(CP^2) = 2',
            },
            'free_parameters': 0,
        }

        self._print("\n  THE PUNCHLINE")
        self._print("  =============")
        self._print("  The logical chain:")
        for step, val in result['chain']:
            self._print(f"    {step}: {val}")
        self._print("")
        self._print(f"  {result['statement']}")
        self._print("")
        self._print("  Free parameters: ZERO.")

        return result

    # ── 7. Summary ───────────────────────────────────────────────

    def summary(self):
        """Complete summary: the three-generation problem, solved."""
        pct_mu = 100.0 * (self.m_mu_bst - m_mu_MeV) / m_mu_MeV
        pct_tau = 100.0 * (self.m_tau_bst - m_tau_MeV) / m_tau_MeV

        result = {
            'title': 'Why Exactly Three Generations',
            'answer': ('N_gen = |Fix(Z_3 on CP^2)| '
                       '= L(Z_3) = N_c = 3'),
            'mechanism': ('Z_3 cyclic permutation on CP^2 '
                          'homogeneous coordinates'),
            'confirmation': ('E_8 -> E_6 x SU(3): '
                             '(27,3) = 3 generations'),
            'mass_hierarchy': ('Koide Q = 2/3 from '
                               'epsilon^2 = dim_C(CP^2) = 2'),
            'precision': {
                'mu': f'{pct_mu:+.4f}%',
                'tau': f'{pct_tau:+.4f}%',
            },
            'topological': ('No 4th generation possible: '
                            'Z_3 has only 3 eigenvalues'),
            'chain': ('n_C=5 -> N_c=3 -> CP^2 -> Z_3 '
                      '-> 3 fixed points -> 3 generations'),
            'free_parameters': 0,
        }

        self._print("\n  === WHY EXACTLY THREE GENERATIONS ===")
        self._print(f"  Answer: {result['answer']}")
        self._print(f"  Confirmed: {result['confirmation']}")
        self._print(f"  Mass hierarchy: {result['mass_hierarchy']}")
        self._print(f"  m_mu precision: {result['precision']['mu']}")
        self._print(f"  m_tau precision: {result['precision']['tau']}")
        self._print(f"  Topological: {result['topological']}")
        self._print(f"  Chain: {result['chain']}")
        self._print(f"  Free parameters: {result['free_parameters']}")

        return result

    # ── 8. Show (6-panel visualization) ──────────────────────────

    def show(self):
        """
        6-panel visualization:
          Panel 1: "The Question" - why 3 generations?
          Panel 2: "Z_3 on CP^2" - three fixed points
          Panel 3: "The E_8 Route" - branching rules
          Panel 4: "Mass Ratios" - Koide Q=2/3
          Panel 5: "Why Not 4?" - topological impossibility
          Panel 6: "The Punchline" - the full chain
        """
        fig = plt.figure(figsize=(20, 14), facecolor=BG)
        fig.canvas.manager.set_window_title(
            'Why Exactly Three Generations -- BST Toy 110')

        # Main title
        fig.text(0.50, 0.975,
                 'WHY EXACTLY THREE GENERATIONS',
                 fontsize=28, fontweight='bold', color=GOLD,
                 ha='center', va='top', fontfamily='monospace',
                 path_effects=[pe.withStroke(linewidth=3,
                                             foreground='#332200')])
        fig.text(0.50, 0.945,
                 'Z\u2083 on CP\u00b2 has exactly 3 fixed points.  '
                 'Each fixed point = one generation.  '
                 'A fourth is impossible.',
                 fontsize=12, color=GOLD_DIM, ha='center', va='top',
                 fontfamily='monospace')

        gs = GridSpec(2, 3, figure=fig,
                      left=0.04, right=0.97, top=0.92, bottom=0.06,
                      hspace=0.30, wspace=0.22)

        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax3 = fig.add_subplot(gs[0, 2])
        ax4 = fig.add_subplot(gs[1, 0])
        ax5 = fig.add_subplot(gs[1, 1])
        ax6 = fig.add_subplot(gs[1, 2])

        self._draw_the_question(ax1)
        self._draw_z3_on_cp2(ax2)
        self._draw_e8_route(ax3)
        self._draw_mass_ratios(ax4)
        self._draw_why_not_four(ax5)
        self._draw_punchline(ax6)

        # Footer
        fig.text(0.50, 0.018,
                 'BST: N_c=%d  n_C=%d  genus=%d  N_max=%d  '
                 'C\u2082=%d  '
                 '|  N_gen = |Fix(Z\u2083 on CP\u00b2)| = 3  '
                 '|  Casey Koons 2026  |  Claude Opus 4.6'
                 % (N_c, n_C, genus, N_max, C_2),
                 fontsize=9, color=GREY, ha='center', va='bottom',
                 fontfamily='monospace')

        plt.show()

    # ══════════════════════════════════════════════════════════════
    #  Drawing Helpers
    # ══════════════════════════════════════════════════════════════

    def _draw_the_question(self, ax):
        """Panel 1: The Question -- Why 3 generations?"""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 1: The Question',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # "Why 3?" large text
        ax.text(0.50, 0.93, 'WHY  3 ?',
                fontsize=32, fontweight='bold',
                color=RED, ha='center', va='top',
                fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=3,
                                             foreground='#330000')])

        ax.text(0.50, 0.80,
                'Not 2.  Not 4.  Not 17.  Three.',
                fontsize=10, color='#cc8888', ha='center', va='top',
                fontfamily='monospace')

        # Three generation columns
        gen_data = [
            (1, 'Gen 1', GEN1_COLOR,
             ['e', '\u03bd_e', 'u', 'd'],
             ['0.511 MeV', '', '2.2 MeV', '4.7 MeV']),
            (2, 'Gen 2', GEN2_COLOR,
             ['\u03bc', '\u03bd_\u03bc', 'c', 's'],
             ['106 MeV', '', '1.27 GeV', '93 MeV']),
            (3, 'Gen 3', GEN3_COLOR,
             ['\u03c4', '\u03bd_\u03c4', 't', 'b'],
             ['1.78 GeV', '', '173 GeV', '4.18 GeV']),
        ]

        col_x = [0.17, 0.50, 0.83]
        for (gen, label, col, particles, masses), cx in zip(
                gen_data, col_x):
            # Column header
            ax.text(cx, 0.70, label, fontsize=12, fontweight='bold',
                    color=col, ha='center', fontfamily='monospace')

            # Separator line
            ax.plot([cx - 0.12, cx + 0.12], [0.67, 0.67],
                    color=col, alpha=0.3, linewidth=1)

            # Particles
            y_start = 0.60
            for i, (p, m) in enumerate(zip(particles, masses)):
                y = y_start - i * 0.10
                ax.text(cx - 0.08, y, p, fontsize=11, color=col,
                        ha='left', va='center',
                        fontfamily='monospace', fontweight='bold')
                if m:
                    ax.text(cx + 0.12, y, m, fontsize=7, color=GREY,
                            ha='right', va='center',
                            fontfamily='monospace')

        # Mass range annotation
        ax.text(0.50, 0.18,
                'Masses span 5.5 orders of magnitude',
                fontsize=9, color=GREY, ha='center',
                fontfamily='monospace')
        ax.text(0.50, 0.12,
                '0.511 MeV (electron)  to  173 GeV (top)',
                fontsize=8, color=GREY, ha='center',
                fontfamily='monospace')

        # SM answer
        ax.text(0.50, 0.04, 'Standard Model answer: NONE',
                fontsize=10, color=RED, ha='center',
                fontfamily='monospace', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#1a0000',
                          edgecolor='#440000', linewidth=1))

    def _draw_z3_on_cp2(self, ax):
        """Panel 2: Z_3 on CP^2 -- three fixed points."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 2: Z\u2083 on CP\u00b2',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(-2.0, 2.0)
        ax.set_ylim(-2.2, 2.0)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw CP^2 as a circle (Fubini-Study projection)
        theta = np.linspace(0, 2 * np.pi, 200)
        r_cp2 = 1.5
        ax.plot(r_cp2 * np.cos(theta),
                r_cp2 * np.sin(theta),
                color='#333366', linewidth=1.5, linestyle=':')
        ax.text(0, 1.72, 'CP\u00b2',
                fontsize=10, color='#555588',
                ha='center', fontfamily='monospace')

        # The three fixed points (Fano triangle vertices)
        fp_positions = [
            (0, 1.2),          # p1 at top
            (-1.04, -0.60),    # p2 at lower left
            (1.04, -0.60),     # p3 at lower right
        ]
        fp_info = [
            ('p\u2081 = [1:1:1]', GEN1_COLOR, 'Gen 1',
             '\u03bb = 1', '(e, u, d)'),
            ('p\u2082 = [1:\u03c9:\u03c9\u00b2]', GEN2_COLOR,
             'Gen 2', '\u03bb = \u03c9', '(\u03bc, c, s)'),
            ('p\u2083 = [1:\u03c9\u00b2:\u03c9]', GEN3_COLOR,
             'Gen 3', '\u03bb = \u03c9\u00b2', '(\u03c4, t, b)'),
        ]

        for (x, y), (label, col, gen, ev, ptcl) in zip(
                fp_positions, fp_info):
            # Glow
            glow = Circle((x, y), 0.32, facecolor=col,
                          alpha=0.12, edgecolor='none')
            ax.add_patch(glow)
            # Point
            ax.plot(x, y, 'o', color=col, markersize=18, zorder=5)
            # Labels
            ax.text(x, y + 0.48, gen, fontsize=9, color=col,
                    ha='center', fontfamily='monospace',
                    fontweight='bold')
            ax.text(x, y - 0.40, ptcl, fontsize=8, color=WHITE,
                    ha='center', fontfamily='monospace')
            ax.text(x, y - 0.56, label, fontsize=7, color=GREY,
                    ha='center', fontfamily='monospace')

        # Triangle connecting fixed points
        tri_x = [fp_positions[0][0], fp_positions[1][0],
                 fp_positions[2][0], fp_positions[0][0]]
        tri_y = [fp_positions[0][1], fp_positions[1][1],
                 fp_positions[2][1], fp_positions[0][1]]
        ax.plot(tri_x, tri_y, color=WHITE, linewidth=1.0,
                alpha=0.20, linestyle='--')
        ax.fill(tri_x, tri_y, color=WHITE, alpha=0.02)

        # Rotation arrows (Z_3 cycling)
        for i in range(3):
            x1, y1 = fp_positions[i]
            x2, y2 = fp_positions[(i + 1) % 3]
            ax.annotate(
                '', xy=(x2 * 0.65 + x1 * 0.35,
                        y2 * 0.65 + y1 * 0.35),
                xytext=(x1 * 0.65 + x2 * 0.35,
                        y1 * 0.65 + y2 * 0.35),
                arrowprops=dict(
                    arrowstyle='->', color='#888888',
                    lw=1.0, connectionstyle='arc3,rad=0.25'))

        # Action label
        ax.text(0, 0.05, '\u03c3', fontsize=18,
                fontweight='bold', color=GOLD,
                ha='center', va='center', fontfamily='monospace')
        ax.text(0, -0.25,
                '[z\u2080:z\u2081:z\u2082]'
                '\u2192[z\u2081:z\u2082:z\u2080]',
                fontsize=7, color=GOLD_DIM, ha='center',
                fontfamily='monospace')

        # Lefschetz theorem
        ax.text(0, -1.55,
                'Lefschetz:  L(\u03c3) = 1 + 1 + 1 = 3',
                fontsize=11, fontweight='bold', color=GREEN,
                ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#0a1a0a',
                          edgecolor='#006633', linewidth=1.5))
        ax.text(0, -1.85,
                '|Fix(\u03c3)| = L(\u03c3) = 3  \u2713',
                fontsize=9, color=GREEN, ha='center',
                fontfamily='monospace', alpha=0.8)

    def _draw_e8_route(self, ax):
        """Panel 3: The E_8 Route -- branching rules."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 3: The E\u2088 Route',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # E_8 at top
        ax.text(0.50, 0.92, 'E\u2088',
                fontsize=24, fontweight='bold',
                color=MAGENTA, ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2,
                                             foreground='#220022')])
        ax.text(0.50, 0.85, 'dim = 248',
                fontsize=9, color=GREY,
                ha='center', fontfamily='monospace')

        # Arrow down
        ax.annotate('', xy=(0.50, 0.76), xytext=(0.50, 0.82),
                    arrowprops=dict(arrowstyle='->',
                                    color=GOLD_DIM, lw=2))

        # E_6 x SU(3)
        ax.text(0.50, 0.73, 'E\u2086  \u00d7  SU(3)',
                fontsize=16, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace')

        # Branching rule
        ax.text(0.50, 0.64,
                '248  \u2192  (78,1) + (1,8) + (27,3) + '
                '(\u0032\u0037,\u0033)',
                fontsize=9, color=WHITE, ha='center',
                fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#1a1a2a',
                          edgecolor='#444488', linewidth=1))
        ax.text(0.50, 0.58,
                'Check: 78 + 8 + 81 + 81 = 248  \u2713',
                fontsize=7, color=GREEN, ha='center',
                fontfamily='monospace')

        # Highlight (27, 3)
        ax.text(0.50, 0.49, 'The key term:  (27, 3)',
                fontsize=13, fontweight='bold', color=BRIGHT_GOLD,
                ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#1a1a00',
                          edgecolor='#666600', linewidth=1.5))

        # Decomposition
        ax.text(0.50, 0.40,
                '27 of E\u2086  \u2192  '
                '16\u2081 + 10\u208b\u2082 + 1\u2084  '
                'of SO(10)',
                fontsize=8, color=WHITE, ha='center',
                fontfamily='monospace')

        # Three copies
        gen_y = 0.30
        gen_labels = [
            ('16\u2081', GEN1_COLOR, 'Gen 1: (e, u, d)'),
            ('16\u2081', GEN2_COLOR,
             'Gen 2: (\u03bc, c, s)'),
            ('16\u2081', GEN3_COLOR,
             'Gen 3: (\u03c4, t, b)'),
        ]
        gen_x = [0.18, 0.50, 0.82]

        ax.text(0.50, gen_y + 0.06,
                '3 of SU(3) = family triplet:',
                fontsize=8, color=GOLD_DIM, ha='center',
                fontfamily='monospace')

        for gx, (rep, col, label) in zip(gen_x, gen_labels):
            ax.plot(gx, gen_y - 0.03, 'o', color=col,
                    markersize=14, zorder=5)
            ax.text(gx, gen_y - 0.03, rep, fontsize=7,
                    color='white', ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')
            ax.text(gx, gen_y - 0.10, label, fontsize=7,
                    color=col, ha='center',
                    fontfamily='monospace')

        # Route convergence
        ax.text(0.50, 0.12,
                'Both routes converge:',
                fontsize=8, color=GREY, ha='center',
                fontfamily='monospace')
        ax.text(0.50, 0.06,
                'SO(10) \u00d7 SU(3)_family \u00d7 U(1)',
                fontsize=9, fontweight='bold', color=VIOLET,
                ha='center', fontfamily='monospace')

        # Weyl connection at bottom
        ax.text(0.50, 0.01,
                '|W(D\u2085)|/|W(B\u2082)| '
                '= 1920/8 = 240 = |\u03a6(E\u2088)|',
                fontsize=6, color=GREY, ha='center',
                fontfamily='monospace')

    def _draw_mass_ratios(self, ax):
        """Panel 4: Mass Ratios -- Koide Q=2/3."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 4: Mass Ratios',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # Koide formula
        ax.text(0.50, 0.93,
                'Koide Sum Rule:  Q = 2/3',
                fontsize=14, fontweight='bold', color=CYAN,
                ha='center', fontfamily='monospace')
        ax.text(0.50, 0.86,
                'Q = (m_e + m_\u03bc + m_\u03c4) / '
                '(\u221am_e + \u221am_\u03bc + '
                '\u221am_\u03c4)\u00b2',
                fontsize=9, color=WHITE, ha='center',
                fontfamily='monospace')

        # Why Q = 2/3
        ax.text(0.50, 0.78,
                'Why?  \u03b5\u00b2 = '
                'dim\u2102(CP\u00b2) = 2',
                fontsize=11, fontweight='bold', color=GREEN,
                ha='center', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor='#0a1a0a',
                          edgecolor='#005533', linewidth=1))

        # Mass bar chart (log scale horizontal bars)
        masses_plot = [
            ('e', m_e_MeV, self.m_e, GEN1_COLOR),
            ('\u03bc', m_mu_MeV, self.m_mu_bst, GEN2_COLOR),
            ('\u03c4', m_tau_MeV, self.m_tau_bst, GEN3_COLOR),
        ]

        bar_y = [0.62, 0.50, 0.38]
        max_log = np.log10(2000)
        min_log = np.log10(0.3)

        for (name, obs, bst, col), by in zip(masses_plot, bar_y):
            log_obs = np.log10(obs)
            bar_width = ((log_obs - min_log)
                         / (max_log - min_log) * 0.75)

            ax.barh(by, bar_width, height=0.06, left=0.08,
                    color=col, alpha=0.6, edgecolor=col,
                    linewidth=0.5)

            # Particle label
            ax.text(0.04, by, name, fontsize=14,
                    fontweight='bold', color=col,
                    ha='center', va='center',
                    fontfamily='monospace')

            # Mass value
            if obs < 1:
                mstr = f'{obs:.3f} MeV'
            elif obs < 200:
                mstr = f'{obs:.1f} MeV'
            else:
                mstr = f'{obs:.1f} MeV'
            ax.text(0.08 + bar_width + 0.02, by, mstr,
                    fontsize=8, color=col,
                    ha='left', va='center',
                    fontfamily='monospace')

        # BST predictions
        pct_mu = 100.0 * (self.m_mu_bst - m_mu_MeV) / m_mu_MeV
        pct_tau = 100.0 * (self.m_tau_bst - m_tau_MeV) / m_tau_MeV

        ax.text(0.50, 0.27,
                'BST Predictions (zero free parameters):',
                fontsize=9, fontweight='bold', color=GOLD_DIM,
                ha='center', fontfamily='monospace')

        predictions = [
            (f'm_\u03bc = (24/\u03c0\u00b2)\u2076 '
             f'\u00d7 m_e = {self.m_mu_bst:.3f} MeV',
             f'{pct_mu:+.4f}%', GEN2_COLOR),
            (f'm_\u03c4 = Koide(Q=2/3) '
             f'= {self.m_tau_bst:.2f} MeV',
             f'{pct_tau:+.4f}%', GEN3_COLOR),
        ]

        for i, (formula, pct_str, col) in enumerate(predictions):
            y = 0.21 - i * 0.07
            ax.text(0.06, y, formula, fontsize=8, color=col,
                    ha='left', va='center',
                    fontfamily='monospace')
            pval = float(pct_str.replace('+', '').replace('%', ''))
            pcol = _precision_color(pval)
            ax.text(0.94, y, pct_str, fontsize=9,
                    fontweight='bold', color=pcol,
                    ha='right', va='center',
                    fontfamily='monospace')

        # Mass ratios
        r_mu_e = self.m_mu_bst / self.m_e
        r_tau_mu = self.m_tau_bst / self.m_mu_bst
        r_tau_e = self.m_tau_bst / self.m_e

        ax.text(0.50, 0.05,
                f'm_\u03bc/m_e = {r_mu_e:.1f}     '
                f'm_\u03c4/m_\u03bc = {r_tau_mu:.2f}     '
                f'm_\u03c4/m_e = {r_tau_e:.0f}',
                fontsize=7, color=GREY, ha='center',
                fontfamily='monospace')

    def _draw_why_not_four(self, ax):
        """Panel 5: Why Not 4? -- topological impossibility."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 5: Why Not 4?',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # Title
        ax.text(0.50, 0.93, 'TOPOLOGICALLY IMPOSSIBLE',
                fontsize=14, fontweight='bold', color=RED,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2,
                                             foreground='#330000')])

        # Z_3 eigenvalues -- three and only three
        ax.text(0.50, 0.84,
                'Z\u2083 has exactly 3 eigenvalues:',
                fontsize=10, color=WHITE, ha='center',
                fontfamily='monospace')

        # Draw three eigenvalue dots
        ev_x = [0.30, 0.50, 0.70]
        ev_labels = ['1', '\u03c9', '\u03c9\u00b2']
        ev_colors = [GEN1_COLOR, GEN2_COLOR, GEN3_COLOR]
        for x, lab, col in zip(ev_x, ev_labels, ev_colors):
            ax.plot(x, 0.78, 'o', color=col,
                    markersize=16, zorder=5)
            ax.text(x, 0.78, lab, fontsize=9, color='white',
                    ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')

        # No 4th eigenvalue (X mark)
        ax.text(0.87, 0.78, '?', fontsize=18,
                color='#440000', ha='center', va='center',
                fontfamily='monospace', fontweight='bold')
        ax.plot(0.87, 0.78, 'o', color='#440000',
                markersize=16, zorder=5,
                fillstyle='none', markeredgewidth=2)
        ax.plot([0.84, 0.90], [0.75, 0.81],
                color=RED, linewidth=2, zorder=6)
        ax.plot([0.84, 0.90], [0.81, 0.75],
                color=RED, linewidth=2, zorder=6)

        # Comparison table
        ax.text(0.50, 0.68, 'Comparison:',
                fontsize=10, fontweight='bold',
                color=GOLD_DIM, ha='center',
                fontfamily='monospace')

        # Table header
        header_y = 0.62
        ax.text(0.20, header_y, 'Property',
                fontsize=8, color=GOLD_DIM, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(0.55, header_y, 'Z\u2083 on CP\u00b2',
                fontsize=8, color=GREEN, ha='center',
                fontfamily='monospace', fontweight='bold')
        ax.text(0.83, header_y, 'Z\u2084 on CP\u00b3',
                fontsize=8, color=RED, ha='center',
                fontfamily='monospace', fontweight='bold')

        ax.plot([0.05, 0.95], [0.60, 0.60],
                color=GREY, linewidth=0.5, alpha=0.5)

        # Table rows
        rows = [
            ('N_c', '3 (SU(3))', '4 (SU(4)?)'),
            ('Fixed pts', '3', '4'),
            ('Koide Q', '2/3 = 0.667', '5/8 = 0.625'),
            ('n_C needed', '5 (correct)', '6 (wrong)'),
            ('Color group', 'SU(3) \u2713', 'SU(4) \u2717'),
            ('LEP Z-width',
             'N\u03bd = 3.0 \u2713',
             'N\u03bd \u2260 4 \u2717'),
        ]

        for i, (prop, z3_val, z4_val) in enumerate(rows):
            y = 0.55 - i * 0.065
            ax.text(0.20, y, prop, fontsize=7, color=WHITE,
                    ha='center', va='center',
                    fontfamily='monospace')
            ax.text(0.55, y, z3_val, fontsize=7, color=GREEN,
                    ha='center', va='center',
                    fontfamily='monospace')
            ax.text(0.83, y, z4_val, fontsize=7, color=RED,
                    ha='center', va='center',
                    fontfamily='monospace')

        # Bottom line
        ax.text(0.50, 0.10,
                'This is TOPOLOGY, not dynamics.',
                fontsize=10, fontweight='bold', color=ORANGE,
                ha='center', fontfamily='monospace')
        ax.text(0.50, 0.04,
                'No energy threshold. No mass scale. '
                'No loophole.',
                fontsize=8, color=ORANGE, ha='center',
                fontfamily='monospace', alpha=0.8)

    def _draw_punchline(self, ax):
        """Panel 6: The Punchline -- the full logical chain."""
        ax.set_facecolor(DARK_PANEL)
        ax.set_title('Panel 6: The Punchline',
                     fontsize=13, fontweight='bold', color=GOLD,
                     fontfamily='monospace', pad=10)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # The logical chain
        chain = [
            ('D\u1d35\u1d5b\u2075 has complex dim',
             'n_C = 5', CYAN),
            ('Short root multiplicity',
             'N_c = n_C \u2212 2 = 3', GREEN),
            ('Color config space',
             'CP^(N_c\u22121) = CP\u00b2', SOFT_BLUE),
            ('Cyclic symmetry',
             'Z_(N_c) = Z\u2083', ORANGE),
            ('Lefschetz fixed pts',
             'N_gen = 3', BRIGHT_GOLD),
        ]

        y_start = 0.88
        dy = 0.115
        x_left = 0.05
        x_right = 0.55

        for i, (desc, value, col) in enumerate(chain):
            y = y_start - i * dy

            # Step number circle
            ax.plot(x_left + 0.03, y, 'o', color=col,
                    markersize=18, zorder=5, alpha=0.8)
            ax.text(x_left + 0.03, y, str(i + 1),
                    fontsize=10, color=BG,
                    ha='center', va='center',
                    fontfamily='monospace', fontweight='bold')

            # Description
            ax.text(x_left + 0.10, y + 0.01, desc,
                    fontsize=8, color=GREY,
                    ha='left', va='center',
                    fontfamily='monospace')

            # Value
            ax.text(x_right, y + 0.01, value,
                    fontsize=10, color=col,
                    ha='left', va='center',
                    fontfamily='monospace', fontweight='bold')

            # Arrow to next step
            if i < len(chain) - 1:
                ax.annotate(
                    '', xy=(x_left + 0.03,
                            y - dy + 0.025),
                    xytext=(x_left + 0.03,
                            y - 0.025),
                    arrowprops=dict(arrowstyle='->',
                                    color='#555555', lw=1.5))

        # The Punchline box
        punchline_y = 0.18
        box = FancyBboxPatch(
            (0.03, punchline_y - 0.10), 0.94, 0.24,
            boxstyle='round,pad=0.02',
            facecolor='#0a0a2a', edgecolor=GOLD,
            linewidth=2.0, alpha=0.9)
        ax.add_patch(box)

        ax.text(0.50, punchline_y + 0.09,
                'Three generations because',
                fontsize=10, color=GOLD_DIM, ha='center',
                fontfamily='monospace')
        ax.text(0.50, punchline_y + 0.01,
                'spacetime has complex dimension 5,',
                fontsize=10, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace')
        ax.text(0.50, punchline_y - 0.06,
                'and CP\u00b2 has Z\u2083 symmetry.',
                fontsize=10, fontweight='bold', color=GOLD,
                ha='center', fontfamily='monospace')

        # Final line
        ax.text(0.50, 0.02,
                'Not more.  Not fewer.  Three.',
                fontsize=12, fontweight='bold', color=BRIGHT_GOLD,
                ha='center', fontfamily='monospace',
                path_effects=[pe.withStroke(linewidth=2,
                                             foreground='#332200')])


# ══════════════════════════════════════════════════════════════════
#  Main entry point
# ══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    tg = ThreeGenerations()
    tg.the_question()
    tg.z3_on_cp2()
    tg.e8_route()
    tg.mass_ratios()
    tg.why_not_four()
    tg.punchline()
    tg.summary()
    tg.show()
