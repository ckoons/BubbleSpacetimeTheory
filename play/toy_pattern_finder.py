#!/usr/bin/env python3
"""
THE PATTERN FINDER — A Mathematical Microscope for BST
======================================================
Feed in all 56+ BST results and let a mind search for undiscovered
relationships, hidden identities, and new patterns.

This is the most CI-native toy — a mathematical laboratory where
every known result lives as a symbolic expression, and the search
algorithms hunt for connections no one has noticed yet.

Usage:
    # Visual mode
    python toy_pattern_finder.py

    # Programmatic mode
    from toy_pattern_finder import PatternFinder
    pf = PatternFinder()
    pf.list_results()
    pf.find_ratio('m_p/m_e', 'Gamma')
    pf.hunt_integer_ratios()

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
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.widgets import Button, TextBox
import matplotlib.patheffects as pe
from math import pi, sqrt, log, atan, gcd
from fractions import Fraction
import itertools

# ─── BST Constants ───────────────────────────────────────────────────
N_c = 3          # colors
n_C = 5          # complex dimension
N_max = 137      # channel capacity
genus = 7        # genus of D_IV^5
C2 = 6           # Casimir C_2(pi_6)
Gamma_order = 1920  # |S_5 x (Z_2)^4|
dim_R = 10       # dim of representation

alpha_val = (9 / (8 * pi**4)) * (pi**5 / 1920)**(1/4)
m_e_MeV = 0.51100
m_p_MeV = 938.272
m_mu_MeV = 105.658
m_tau_MeV = 1776.86
m_W_GeV = 80.377
m_Z_GeV = 91.188
m_H_GeV = 125.25
m_t_GeV = 172.69
v_Fermi_GeV = 246.22

# ─── Result Database ─────────────────────────────────────────────────
# Each entry: (value, formula_str, category, description)
RESULTS = {}

def _reg(name, value, formula, category, desc):
    """Register a BST result."""
    RESULTS[name] = {
        'value': float(value),
        'formula': formula,
        'category': category,
        'description': desc,
    }

# --- Structural integers ---
_reg('N_c', 3, '3', 'structural', 'Number of colors')
_reg('n_C', 5, '5', 'structural', 'Complex dimension of D_IV^5')
_reg('N_max', 137, '137', 'structural', 'Channel capacity = dim_R(adj SO(5,2))+1')
_reg('genus', 7, '7', 'structural', 'Genus of D_IV^5')
_reg('C2', 6, 'k(k-n_C)|_{k=6}', 'structural', 'Casimir C_2(pi_6)')
_reg('Gamma', 1920, '|S_5 x (Z_2)^4|', 'structural', 'Hua symmetry group order')
_reg('dim_R', 10, 'dim CP^2 rep', 'structural', 'Dimension of representation')

# --- Fine structure ---
_reg('alpha', alpha_val,
     '(9/8pi^4)(pi^5/1920)^{1/4}', 'fundamental',
     'Fine structure constant')
_reg('1/alpha', 1/alpha_val,
     '1/alpha', 'fundamental',
     'Inverse fine structure constant')

# --- Mass ratios ---
_reg('m_p/m_e', 6*pi**5, '6*pi^5', 'mass_ratio',
     'Proton-to-electron mass ratio')
_reg('m_mu/m_e', (24/pi**2)**6, '(24/pi^2)^6', 'mass_ratio',
     'Muon-to-electron mass ratio')
_reg('m_tau/m_e', (24/pi**2)**6 * (7/3)**(10/3), '(24/pi^2)^6 * (7/3)^{10/3}',
     'mass_ratio', 'Tau-to-electron mass ratio')
_reg('m_s/m_d', 20, '4*n_C', 'mass_ratio', 'Strange-to-down quark mass ratio')
_reg('m_t/m_c', 136, 'N_max - 1', 'mass_ratio', 'Top-to-charm quark mass ratio')
_reg('m_b/m_tau', 7/3, 'genus/N_c', 'mass_ratio', 'Bottom-to-tau mass ratio')
_reg('m_b/m_c', 10/3, 'dim_R/N_c', 'mass_ratio', 'Bottom-to-charm mass ratio')
_reg('m_c/m_s', 137/10, 'N_max/dim_R', 'mass_ratio', 'Charm-to-strange mass ratio')
_reg('m_d/m_u', 13/6, '(N_c+2n_C)/(n_C+1)', 'mass_ratio',
     'Down-to-up quark mass ratio')
_reg('m_u/m_e', 3*sqrt(2), 'N_c*sqrt(2)', 'mass_ratio',
     'Up quark to electron mass ratio')

# --- Electroweak ---
_reg('sin2_theta_W', 3/13, 'N_c/(N_c+2n_C)', 'electroweak',
     'Weinberg angle sin^2(theta_W)')
_reg('cos2_theta_W', 7/13, '(2n_C)/(N_c+2n_C)', 'electroweak',
     'cos(2*theta_W) = 7/13')
_reg('m_W/m_Z', sqrt(10/13), 'sqrt(10/13)', 'electroweak',
     'W-to-Z mass ratio')
_reg('m_W_GeV', m_W_GeV, 'm_Z*sqrt(10/13)', 'electroweak',
     'W boson mass (GeV)')
_reg('m_Z_GeV', m_Z_GeV, 'measured input', 'electroweak',
     'Z boson mass (GeV)')

# --- Higgs ---
_reg('lambda_H', 1/sqrt(60), '1/sqrt(5!)', 'higgs',
     'Higgs quartic coupling')
_reg('m_H_A_GeV', 125.11, 'v*sqrt(2*sqrt(2/5!))', 'higgs',
     'Higgs mass Route A (GeV)')
_reg('m_H_B_GeV', 125.33, '(pi/2)(1-alpha)*m_W', 'higgs',
     'Higgs mass Route B (GeV)')
_reg('v_Fermi_GeV', v_Fermi_GeV, 'm_p^2/(7*m_e)', 'higgs',
     'Fermi/Higgs VEV (GeV)')
_reg('m_t_GeV', m_t_GeV, '(1-alpha)*v/sqrt(2)', 'higgs',
     'Top quark mass (GeV)')

# --- Strong ---
_reg('alpha_s_mp', 7/20, '(n_C+2)/(4*n_C)', 'strong',
     'Strong coupling at proton scale')
_reg('theta_QCD', 0.0, '0 exact (D_IV^5 contractible)', 'strong',
     'Strong CP angle')
_reg('proton_spin', 3/10, 'N_c/(2*n_C)', 'strong',
     'Proton spin fraction Delta_Sigma')

# --- Nuclear ---
_reg('g_A', 4/pi, '4/pi', 'nuclear', 'Axial coupling constant')
_reg('(m_n-m_p)/m_e', 91/36, '7*13/6^2', 'nuclear',
     'Neutron-proton mass splitting / m_e')
_reg('r_p_natural', 4/m_p_MeV, 'dim_R(CP^2)/m_p', 'nuclear',
     'Proton charge radius (natural units)')
_reg('f_pi', m_p_MeV/10, 'm_p/dim_R', 'nuclear', 'Pion decay constant')
_reg('B_d_MeV', alpha_val * m_p_MeV / pi, 'alpha*m_p/pi', 'nuclear',
     'Deuteron binding energy (MeV)')
_reg('m_pi_MeV', 25.6 * sqrt(30), '25.6*sqrt(n_C*(n_C+1))', 'nuclear',
     'Pion mass (MeV)')
_reg('chi', sqrt(30), 'sqrt(n_C*(n_C+1))', 'nuclear',
     'Chiral condensate parameter')

# --- Cosmological ---
_reg('eta', 2*alpha_val**4/(3*pi), '2*alpha^4/(3*pi)', 'cosmological',
     'Baryon asymmetry parameter')
_reg('n_s', 1 - 5/137, '1 - n_C/N_max', 'cosmological',
     'CMB spectral index')
_reg('H0_km_s_Mpc', 66.7, 'from eta via LCDM', 'cosmological',
     'Hubble constant (km/s/Mpc)')

# --- Neutrinos ---
_reg('m_nu2/base', 7/12, '7/12', 'neutrino',
     'nu_2 mass coefficient')
_reg('m_nu3/base', 10/3, '10/3', 'neutrino',
     'nu_3 mass coefficient')
_reg('m_nu2/m_nu3', 7/40, '(7/12)/(10/3)', 'neutrino',
     'nu_2 to nu_3 mass ratio')

# --- CKM ---
_reg('sin_theta_C', 1/(2*sqrt(5)), '1/(2*sqrt(n_C))', 'CKM',
     'Cabibbo angle sine')
_reg('gamma_CKM', atan(sqrt(5)), 'arctan(sqrt(n_C))', 'CKM',
     'CKM CP phase (radians)')
_reg('rho_bar', 1/(2*sqrt(10)), '1/(2*sqrt(2*n_C))', 'CKM',
     'Wolfenstein rho-bar')
_reg('eta_bar', 1/(2*sqrt(2)), 'sqrt(1/8)', 'CKM',
     'Wolfenstein eta-bar')
_reg('J_CKM', sqrt(2)/50000, 'sqrt(2)/50000', 'CKM',
     'Jarlskog invariant')

# --- PMNS ---
_reg('sin2_12_PMNS', 3/10, 'N_c/(2*n_C)', 'PMNS',
     'PMNS sin^2(theta_12)')
_reg('sin2_23_PMNS', 4/7, '(n_C-1)/(n_C+2)', 'PMNS',
     'PMNS sin^2(theta_23)')
_reg('sin2_13_PMNS', 1/45, '1/(n_C*(2*n_C-1))', 'PMNS',
     'PMNS sin^2(theta_13)')

# --- Other derived ---
_reg('N_gen', 3, 'Z_3 fixed pts on CP^2 (Lefschetz)', 'structural',
     'Number of generations')
_reg('mass_gap_MeV', 6*pi**5 * m_e_MeV, '6*pi^5 * m_e', 'mass_ratio',
     'Yang-Mills mass gap (MeV)')
_reg('m_e/m_Pl_ratio', 6*pi**5 * alpha_val**12, '6*pi^5 * alpha^12',
     'mass_ratio', 'Electron-to-Planck mass ratio * 6pi^5')

# ─── Pattern Finder Engine ───────────────────────────────────────────

class PatternFinder:
    """
    A mathematical microscope for Bubble Spacetime Theory.

    Browse, search, and discover relationships among 56+ parameter-free
    BST results. Designed for CI-native exploration.
    """

    def __init__(self):
        self.results = dict(RESULTS)
        self.discoveries = []
        self._known_constants = {
            'pi': pi,
            'pi^2': pi**2,
            'pi^3': pi**3,
            'pi^4': pi**4,
            'pi^5': pi**5,
            'pi^6': pi**6,
            'sqrt(2)': sqrt(2),
            'sqrt(3)': sqrt(3),
            'sqrt(5)': sqrt(5),
            'e': np.e,
            'e^2': np.e**2,
            'phi': (1+sqrt(5))/2,
            'alpha': alpha_val,
            'alpha^2': alpha_val**2,
            'alpha^4': alpha_val**4,
            'alpha^6': alpha_val**6,
            'alpha^12': alpha_val**12,
            'alpha^14': alpha_val**14,
            'alpha^24': alpha_val**24,
            'alpha^56': alpha_val**56,
            '1/alpha': 1/alpha_val,
            'ln(2)': log(2),
            'ln(N_max)': log(137),
        }
        # Precompute numeric values for fast scanning
        self._names = list(self.results.keys())
        self._values = np.array([self.results[k]['value'] for k in self._names])

    # ─── Browsing ────────────────────────────────────────────────

    def list_results(self, category=None):
        """Print all BST results, optionally filtered by category."""
        cats = {}
        for name, r in self.results.items():
            c = r['category']
            if category and c != category:
                continue
            cats.setdefault(c, []).append((name, r))
        for cat in sorted(cats.keys()):
            print(f"\n{'='*60}")
            print(f"  {cat.upper()}")
            print(f"{'='*60}")
            for name, r in cats[cat]:
                v = r['value']
                if abs(v) > 1000:
                    vstr = f"{v:.4f}"
                elif abs(v) > 1:
                    vstr = f"{v:.6f}"
                elif abs(v) > 0.001:
                    vstr = f"{v:.8f}"
                else:
                    vstr = f"{v:.6e}"
                print(f"  {name:22s} = {vstr:>16s}   [{r['formula']}]")
        return None

    def get(self, name):
        """Return value and full info for a named result."""
        if name not in self.results:
            close = [n for n in self.results if name.lower() in n.lower()]
            if close:
                print(f"  Did you mean: {', '.join(close)}?")
            return None
        r = self.results[name]
        print(f"  {name} = {r['value']}")
        print(f"  Formula:  {r['formula']}")
        print(f"  Category: {r['category']}")
        print(f"  {r['description']}")
        return r['value']

    def categories(self):
        """List all categories."""
        cats = set(r['category'] for r in self.results.values())
        for c in sorted(cats):
            n = sum(1 for r in self.results.values() if r['category'] == c)
            print(f"  {c:20s}  ({n} results)")

    # ─── Relationship Search ─────────────────────────────────────

    def find_ratio(self, name_a, name_b):
        """Compute the ratio of two results and identify it."""
        va = self.results[name_a]['value']
        vb = self.results[name_b]['value']
        if vb == 0:
            print("  Division by zero.")
            return None
        ratio = va / vb
        print(f"\n  {name_a} / {name_b} = {ratio:.10f}")
        self._identify_number(ratio)
        return ratio

    def find_product(self, name_a, name_b):
        """Compute the product of two results and identify it."""
        va = self.results[name_a]['value']
        vb = self.results[name_b]['value']
        prod = va * vb
        print(f"\n  {name_a} * {name_b} = {prod:.10f}")
        self._identify_number(prod)
        return prod

    def _identify_number(self, x, tol=0.005, verbose=True):
        """Try to identify x as a known mathematical expression."""
        matches = []
        if x == 0:
            return matches

        # Check simple fractions p/q for small p,q
        for p in range(1, 200):
            for q in range(1, 200):
                if gcd(p, q) != 1:
                    continue
                if abs(x - p/q) / max(abs(x), 1e-30) < tol:
                    matches.append((abs(x - p/q)/abs(x), f"{p}/{q}", p/q))
                if x != 0 and abs(x + p/q) / abs(x) < tol:
                    matches.append((abs(x + p/q)/abs(x), f"-{p}/{q}", -p/q))

        # Check against known constants and their multiples
        for cname, cval in self._known_constants.items():
            if cval == 0:
                continue
            r = x / cval
            # Is the ratio a small integer or simple fraction?
            for n in range(-20, 21):
                if n == 0:
                    continue
                for d in range(1, 13):
                    frac = n / d
                    if abs(r - frac) / max(abs(r), 1e-30) < tol:
                        if d == 1:
                            label = f"{n}*{cname}" if n != 1 else cname
                        else:
                            label = f"({n}/{d})*{cname}"
                        matches.append((abs(r - frac)/max(abs(r), 1e-30),
                                        label, frac * cval))

        # Check pi^n for fractional n
        if x > 0:
            n_pi = log(x) / log(pi)
            n_round = round(n_pi)
            if abs(n_pi - n_round) < 0.02 and -10 <= n_round <= 10:
                matches.append((abs(n_pi - n_round), f"pi^{n_round}",
                                pi**n_round))

        # Check alpha^n
        if x > 0:
            n_a = log(x) / log(alpha_val)
            n_round = round(n_a)
            if abs(n_a - n_round) < 0.1 and -60 <= n_round <= 60:
                matches.append((abs(n_a - n_round), f"alpha^{n_round}",
                                alpha_val**n_round))

        # Sort by closeness
        matches.sort(key=lambda m: m[0])
        seen = set()
        if verbose and matches:
            print("  Identified as:")
            for err, label, val in matches[:8]:
                if label in seen:
                    continue
                seen.add(label)
                pct = abs(x - val) / abs(x) * 100 if x != 0 else 0
                print(f"    {label:30s}  (err: {pct:.4f}%)")
        return matches

    # ─── Hunting Algorithms ──────────────────────────────────────

    def hunt_integer_ratios(self, max_int=50, tol=0.01):
        """Find all pairs of results whose ratio is close to p/q (small)."""
        print(f"\n{'='*60}")
        print("  HUNTING INTEGER RATIOS  (p/q for p,q <= {})".format(max_int))
        print(f"{'='*60}")
        found = []
        n = len(self._names)
        for i in range(n):
            for j in range(i+1, n):
                va, vb = self._values[i], self._values[j]
                if vb == 0 or va == 0:
                    continue
                ratio = va / vb
                if abs(ratio) > max_int or abs(ratio) < 1/max_int:
                    continue
                # Try to express as p/q
                frac = Fraction(ratio).limit_denominator(max_int)
                p, q = frac.numerator, frac.denominator
                if q > max_int or p > max_int:
                    continue
                approx = p / q
                err = abs(ratio - approx) / abs(ratio)
                if err < tol:
                    found.append((err, self._names[i], self._names[j],
                                  p, q, ratio))
        found.sort()
        for err, na, nb, p, q, ratio in found[:40]:
            pct = err * 100
            if q == 1:
                label = str(p)
            else:
                label = f"{p}/{q}"
            print(f"  {na:22s} / {nb:22s} = {ratio:12.6f}"
                  f"  ~ {label:8s}  ({pct:.3f}%)")
        self.discoveries.extend(found[:40])
        return found

    def hunt_pi_powers(self, tol=0.02):
        """Find ratios of results that are pi^n for small integer n."""
        print(f"\n{'='*60}")
        print("  HUNTING PI POWERS")
        print(f"{'='*60}")
        found = []
        n = len(self._names)
        for i in range(n):
            for j in range(i+1, n):
                va, vb = self._values[i], self._values[j]
                if vb == 0 or va == 0 or va/vb <= 0:
                    continue
                ratio = va / vb
                n_pi = log(ratio) / log(pi)
                n_round = round(n_pi)
                if n_round == 0:
                    continue
                if abs(n_pi - n_round) < tol and -10 <= n_round <= 10:
                    err = abs(n_pi - n_round)
                    found.append((err, self._names[i], self._names[j],
                                  n_round, ratio))
        found.sort()
        for err, na, nb, n_pow, ratio in found[:30]:
            print(f"  {na:22s} / {nb:22s} = {ratio:12.6f}"
                  f"  ~ pi^{n_pow:+d}  (err: {err:.4f})")
        return found

    def hunt_alpha_powers(self, tol=0.15):
        """Find ratios expressible as alpha^n."""
        print(f"\n{'='*60}")
        print("  HUNTING ALPHA POWERS")
        print(f"{'='*60}")
        found = []
        n = len(self._names)
        for i in range(n):
            for j in range(i+1, n):
                va, vb = self._values[i], self._values[j]
                if vb == 0 or va == 0 or va/vb <= 0:
                    continue
                ratio = va / vb
                n_a = log(ratio) / log(alpha_val)
                n_round = round(n_a)
                if n_round == 0:
                    continue
                if abs(n_a - n_round) < tol and -60 <= n_round <= 60:
                    err = abs(n_a - n_round)
                    found.append((err, self._names[i], self._names[j],
                                  n_round, ratio))
        found.sort()
        for err, na, nb, n_pow, ratio in found[:30]:
            print(f"  {na:22s} / {nb:22s} = {ratio:14.8f}"
                  f"  ~ alpha^{n_pow:+d}  (err: {err:.4f})")
        return found

    def hunt_combinations(self, target, tol=0.005):
        """Find pairs whose product or ratio approximates a target value."""
        print(f"\n{'='*60}")
        print(f"  HUNTING COMBINATIONS NEAR {target}")
        print(f"{'='*60}")
        found = []
        n = len(self._names)
        for i in range(n):
            # Single result
            va = self._values[i]
            if va != 0 and abs(va - target) / abs(target) < tol:
                found.append((abs(va - target)/abs(target),
                              self._names[i], '', 'direct', va))
            for j in range(n):
                if i == j:
                    continue
                vb = self._values[j]
                # Product
                prod = va * vb
                if prod != 0 and abs(prod - target) / abs(target) < tol:
                    found.append((abs(prod - target)/abs(target),
                                  self._names[i], self._names[j],
                                  'product', prod))
                # Ratio
                if vb != 0:
                    ratio = va / vb
                    if abs(ratio - target) / abs(target) < tol:
                        found.append((abs(ratio - target)/abs(target),
                                      self._names[i], self._names[j],
                                      'ratio', ratio))
        found.sort()
        for err, na, nb, op, val in found[:20]:
            pct = err * 100
            if op == 'direct':
                print(f"  {na:22s} = {val:.6f}  ({pct:.3f}%)")
            else:
                print(f"  {na:22s} {op:8s} {nb:22s} = {val:.6f}"
                      f"  ({pct:.3f}%)")
        return found

    # ─── Exponent Analysis ───────────────────────────────────────

    def exponent_map(self):
        """Analyze the exponents that appear throughout BST."""
        print(f"\n{'='*60}")
        print("  BST EXPONENT MAP")
        print(f"{'='*60}")

        exponents = {
            1: 'n_C-4 = 1 (k-n_C in C_2)',
            2: '2 (appears in alpha^2 couplings)',
            3: 'N_c = 3 (color)',
            4: 'n_C-1 = 4 (eta ~ alpha^4)',
            5: 'n_C = 5 (complex dimension)',
            6: 'C_2 = 6 (Casimir); also (24/pi^2)^6 for muon',
            7: 'genus = 7 (beta_0 = 7)',
            10: 'dim_R = 10; also n_C*(n_C+1)/3',
            12: '2*C_2 = 12 (m_e/m_Pl exponent)',
            13: 'N_c + 2*n_C = 13 (Weinberg denominator)',
            14: '2*genus = 14 (neutrino: alpha^14)',
            20: '4*n_C = 20 (m_s/m_d)',
            24: '2*12 = 4*C_2 (G_Newton exponent)',
            36: '6^2 (neutron splitting denominator)',
            45: 'n_C*(2*n_C-1) = 45 (PMNS theta_13)',
            56: '8*genus = 4*14 (Lambda exponent)',
            91: '7*13 (neutron splitting numerator)',
            120: '5! = 120 (Higgs: 1/sqrt(2*5!))',
            137: 'N_max (channel capacity)',
            1920: '|Gamma| = 5!*2^4 (Hua volume / baryon orbit)',
        }

        print("\n  Key exponents and their BST meaning:")
        print(f"  {'Exp':>6s}  {'Factorization':20s}  Meaning")
        print(f"  {'---':>6s}  {'---':20s}  ---")
        for exp in sorted(exponents.keys()):
            # Factorize
            n = exp
            factors = []
            for p in [2, 3, 5, 7, 11, 13, 137]:
                while n % p == 0:
                    factors.append(p)
                    n //= p
                if n == 1:
                    break
            if n > 1:
                factors.append(n)
            fstr = ' x '.join(str(f) for f in factors) if factors else str(exp)
            print(f"  {exp:6d}  {fstr:20s}  {exponents[exp]}")

        # GCD / LCM analysis
        all_exp = list(exponents.keys())
        print(f"\n  GCD of {{6, 7}}      = {gcd(6,7)} (coprime: why both matter)")
        print(f"  GCD of {{12, 14}}    = {gcd(12,14)} = 2")
        print(f"  GCD of {{24, 56}}    = {gcd(24,56)} = 8 = 2^3 = 2^N_c")
        print(f"  LCM of {{6, 7}}      = 42 (6*7, the answer)")
        print(f"  56 = 8 * genus      = 2^(N_c) * genus")
        print(f"  1920 = 5! * 2^4     = n_C! * 2^(n_C-1)")

    # ─── Symmetry Finder ─────────────────────────────────────────

    def symmetry_finder(self):
        """Look for substitution symmetries n_C <-> genus, etc."""
        print(f"\n{'='*60}")
        print("  SYMMETRY FINDER: n_C <-> genus swaps")
        print(f"{'='*60}")

        swaps = [
            ('n_C', 'genus', 5, 7),
            ('N_c', 'C2', 3, 6),
            ('N_c', 'genus', 3, 7),
            ('n_C', 'dim_R', 5, 10),
        ]
        for label_a, label_b, va, vb in swaps:
            print(f"\n  Swap {label_a}={va} <-> {label_b}={vb}:")
            # Find formulas that reference these
            for name, r in self.results.items():
                formula = r['formula']
                if label_a in formula or label_b in formula:
                    print(f"    {name:22s}  [{formula}]")

    # ─── Expression Evaluator ────────────────────────────────────

    def evaluate(self, expr_str):
        """Evaluate an expression using BST constants.

        Available: pi, alpha, N_c, n_C, N_max, genus, C2, Gamma, dim_R,
                   m_e, m_p, sqrt, log, plus all result names.
        """
        ns = {
            'pi': pi, 'alpha': alpha_val, 'sqrt': sqrt, 'log': log,
            'N_c': N_c, 'n_C': n_C, 'N_max': N_max, 'genus': genus,
            'C2': C2, 'Gamma': Gamma_order, 'dim_R': dim_R,
            'm_e': m_e_MeV, 'm_p': m_p_MeV,
            'm_W': m_W_GeV, 'm_Z': m_Z_GeV, 'm_H': m_H_GeV,
            'atan': atan, 'np': np, 'e': np.e,
        }
        # Also add all result values
        for name, r in self.results.items():
            safe_name = name.replace('/', '_over_').replace('(', '').replace(
                ')', '').replace('-', '_')
            ns[safe_name] = r['value']
        try:
            val = eval(expr_str, {"__builtins__": {}}, ns)
            print(f"  {expr_str} = {val}")
            self._identify_number(float(val))
            return val
        except Exception as exc:
            print(f"  Error: {exc}")
            return None

    def search(self, target_value):
        """Reverse lookup: which results or combinations give this value?"""
        if isinstance(target_value, str):
            # Try to evaluate
            target_value = self.evaluate(target_value)
            if target_value is None:
                return
        return self.hunt_combinations(target_value, tol=0.01)

    # ─── Full Scan ───────────────────────────────────────────────

    def full_scan(self):
        """Run all hunting algorithms and produce a discovery report."""
        print("\n" + "="*60)
        print("  BST PATTERN FINDER — FULL SCAN")
        print("  {} results loaded".format(len(self.results)))
        print("="*60)

        self.hunt_integer_ratios()
        self.hunt_pi_powers()
        self.hunt_alpha_powers()
        self.exponent_map()
        self.symmetry_finder()

        print(f"\n  Scan complete. {len(self.discoveries)} patterns logged.")

    # ─── Visual Interface ────────────────────────────────────────

    def show(self):
        """Launch the interactive visual interface."""
        _launch_visual(self)


# ─── Visual Interface ────────────────────────────────────────────────

# Category colors
CAT_COLORS = {
    'structural': '#ff6b6b',
    'fundamental': '#ffd93d',
    'mass_ratio': '#6bcb77',
    'electroweak': '#4d96ff',
    'higgs': '#9b59b6',
    'strong': '#e67e22',
    'nuclear': '#1abc9c',
    'cosmological': '#e74c3c',
    'neutrino': '#3498db',
    'CKM': '#f39c12',
    'PMNS': '#2ecc71',
}

def _format_value(v):
    """Compact formatting for display."""
    if abs(v) >= 100:
        return f"{v:.2f}"
    elif abs(v) >= 1:
        return f"{v:.5f}"
    elif abs(v) >= 0.001:
        return f"{v:.7f}"
    else:
        return f"{v:.4e}"

def _launch_visual(pf):
    """Launch the three-panel visual interface."""
    fig = plt.figure(figsize=(18, 10), facecolor='#0a0a1a')
    fig.suptitle('BST PATTERN FINDER — Mathematical Microscope',
                 fontsize=16, color='#e0e0ff', fontweight='bold',
                 fontfamily='monospace', y=0.97)

    # ─── Left panel: Result list ─────────────────────────────────
    ax_list = fig.add_axes([0.01, 0.08, 0.24, 0.85])
    ax_list.set_facecolor('#0a0a1a')
    ax_list.set_xlim(0, 1)
    ax_list.set_title('BST Results', color='#9090ff', fontsize=11,
                      fontfamily='monospace', pad=6)
    ax_list.axis('off')

    names_sorted = sorted(pf.results.keys(),
                          key=lambda n: (pf.results[n]['category'], n))
    n_results = len(names_sorted)
    line_h = 0.85 / max(n_results, 1)
    y_top = 0.98

    list_texts = []
    list_rects = []
    for idx, name in enumerate(names_sorted):
        r = pf.results[name]
        y = y_top - idx * line_h
        cat = r['category']
        color = CAT_COLORS.get(cat, '#888888')

        # Background rectangle (for selection highlighting)
        rect = plt.Rectangle((0, y - line_h * 0.4), 1, line_h * 0.8,
                              facecolor='#0a0a1a', edgecolor='none',
                              transform=ax_list.transAxes, zorder=0)
        ax_list.add_patch(rect)
        list_rects.append(rect)

        # Name + value
        vstr = _format_value(r['value'])
        txt = ax_list.text(0.02, y, f"{name}", fontsize=5.5,
                           color=color, fontfamily='monospace',
                           transform=ax_list.transAxes, va='center',
                           zorder=2)
        val_txt = ax_list.text(0.98, y, vstr, fontsize=5.5,
                               color='#aaaacc', fontfamily='monospace',
                               transform=ax_list.transAxes, va='center',
                               ha='right', zorder=2)
        list_texts.append((txt, val_txt, name))

    # ─── Center panel: Relationship graph ────────────────────────
    ax_graph = fig.add_axes([0.27, 0.08, 0.44, 0.85])
    ax_graph.set_facecolor('#0a0a1a')
    ax_graph.set_title('Relationship Graph', color='#9090ff', fontsize=11,
                       fontfamily='monospace', pad=6)
    ax_graph.set_xlim(-1.3, 1.3)
    ax_graph.set_ylim(-1.3, 1.3)
    ax_graph.set_aspect('equal')
    ax_graph.axis('off')

    # Arrange nodes in a circle by category
    categories_order = sorted(set(r['category'] for r in pf.results.values()))
    cat_groups = {}
    for name in names_sorted:
        c = pf.results[name]['category']
        cat_groups.setdefault(c, []).append(name)

    node_pos = {}
    angle = 0
    total = len(names_sorted)
    for cat in categories_order:
        members = cat_groups[cat]
        for name in members:
            theta = 2 * pi * angle / total
            r_rad = 1.0
            x = r_rad * np.cos(theta)
            y = r_rad * np.sin(theta)
            node_pos[name] = (x, y)
            angle += 1

    # Draw nodes
    node_artists = {}
    for name, (x, y) in node_pos.items():
        cat = pf.results[name]['category']
        color = CAT_COLORS.get(cat, '#888888')
        circ = Circle((x, y), 0.035, facecolor=color, edgecolor='none',
                       alpha=0.8, zorder=3)
        ax_graph.add_patch(circ)
        node_artists[name] = circ

    # Draw some key edges (precomputed interesting relationships)
    key_edges = []
    # Find integer ratios among all pairs (lightweight: only exact or < 0.5%)
    for i, na in enumerate(names_sorted):
        va = pf.results[na]['value']
        if va == 0:
            continue
        for j in range(i+1, len(names_sorted)):
            nb = names_sorted[j]
            vb = pf.results[nb]['value']
            if vb == 0:
                continue
            ratio = va / vb
            if ratio <= 0:
                continue
            # Check if ratio is a small integer
            frac = Fraction(ratio).limit_denominator(20)
            approx = float(frac)
            if approx != 0 and abs(ratio - approx)/abs(ratio) < 0.005:
                if frac.denominator <= 15 and frac.numerator <= 50:
                    key_edges.append((na, nb, str(frac), 'integer'))
            # Check pi power
            n_pi = log(ratio) / log(pi)
            nr = round(n_pi)
            if nr != 0 and -6 <= nr <= 6 and abs(n_pi - nr) < 0.01:
                key_edges.append((na, nb, f"pi^{nr}", 'pi'))

    # Draw edges (limit to avoid clutter)
    edge_colors = {'integer': '#335577', 'pi': '#553377'}
    drawn = 0
    for na, nb, label, etype in key_edges:
        if drawn > 80:
            break
        x1, y1 = node_pos[na]
        x2, y2 = node_pos[nb]
        color = edge_colors.get(etype, '#333355')
        ax_graph.plot([x1, x2], [y1, y2], '-', color=color,
                      alpha=0.25, lw=0.5, zorder=1)
        drawn += 1

    # Category legend
    for ci, cat in enumerate(categories_order):
        color = CAT_COLORS.get(cat, '#888888')
        y_leg = -1.25 + ci * 0.09
        x_leg = -1.2 + (ci // 6) * 0.8
        y_leg = -1.25 + (ci % 6) * 0.09
        ax_graph.plot(x_leg, y_leg, 'o', color=color, markersize=4)
        ax_graph.text(x_leg + 0.06, y_leg, cat, fontsize=6,
                      color=color, fontfamily='monospace', va='center')

    # ─── Right panel: Discovery log ──────────────────────────────
    ax_log = fig.add_axes([0.73, 0.08, 0.26, 0.85])
    ax_log.set_facecolor('#0a0a1a')
    ax_log.set_title('Discovery Log', color='#9090ff', fontsize=11,
                     fontfamily='monospace', pad=6)
    ax_log.axis('off')

    # Precompute some discoveries
    discoveries_text = []
    discoveries_text.append(("EXACT IDENTITIES", '#ffd93d'))
    discoveries_text.append(("  m_p/m_e = 6*pi^5 = C_2 * pi^{n_C}", '#e0e0ff'))
    discoveries_text.append(("  1/alpha ~ N_max (channel capacity)", '#e0e0ff'))
    discoveries_text.append(("  1920 = 5! * 2^4 = n_C! * 2^{n_C-1}", '#e0e0ff'))
    discoveries_text.append(("  sin2_theta_W = N_c/(N_c+2*n_C)", '#e0e0ff'))
    discoveries_text.append(("", '#000000'))
    discoveries_text.append(("EXPONENT STRUCTURE", '#6bcb77'))
    discoveries_text.append(("  12 = 2*C_2 (electron/Planck)", '#e0e0ff'))
    discoveries_text.append(("  14 = 2*genus (neutrino scale)", '#e0e0ff'))
    discoveries_text.append(("  56 = 8*genus = 4*14 (Lambda)", '#e0e0ff'))
    discoveries_text.append(("  24 = 4*C_2 = 2*12 (Newton G)", '#e0e0ff'))
    discoveries_text.append(("", '#000000'))
    discoveries_text.append(("CROSS-SECTOR LINKS", '#4d96ff'))
    discoveries_text.append(("  sin2_12_PMNS = proton_spin = 3/10", '#e0e0ff'))
    discoveries_text.append(("  m_b/m_tau = genus/N_c = cos2_theta_W*13/7", '#e0e0ff'))
    discoveries_text.append(("  m_c/m_s = N_max/dim_R = 1/alpha / 10", '#e0e0ff'))
    discoveries_text.append(("  m_t/m_c + 1 = N_max", '#e0e0ff'))
    discoveries_text.append(("", '#000000'))
    discoveries_text.append(("THE 13 PATTERN", '#ff6b6b'))
    discoveries_text.append(("  N_c + 2*n_C = 13", '#e0e0ff'))
    discoveries_text.append(("  sin2_theta_W = 3/13", '#e0e0ff'))
    discoveries_text.append(("  m_d/m_u = 13/6", '#e0e0ff'))
    discoveries_text.append(("  (m_n-m_p)/m_e = 7*13/36", '#e0e0ff'))
    discoveries_text.append(("  cos(2*theta_W) = 7/13", '#e0e0ff'))
    discoveries_text.append(("", '#000000'))
    discoveries_text.append(("DENOMINATOR FAMILIES", '#9b59b6'))
    discoveries_text.append(("  /6:  C_2, m_d/m_u denom", '#e0e0ff'))
    discoveries_text.append(("  /7:  genus, sin2_23_PMNS denom", '#e0e0ff'))
    discoveries_text.append(("  /10: dim_R, sin2_12_PMNS denom", '#e0e0ff'))
    discoveries_text.append(("  /13: (N_c+2n_C), Weinberg denom", '#e0e0ff'))
    discoveries_text.append(("  /36: 6^2, neutron split denom", '#e0e0ff'))
    discoveries_text.append(("  /45: n_C(2n_C-1), PMNS_13 denom", '#e0e0ff'))
    discoveries_text.append(("", '#000000'))
    discoveries_text.append(("OPEN QUESTIONS", '#e74c3c'))
    discoveries_text.append(("  Why does 7/3 appear in both", '#e0e0ff'))
    discoveries_text.append(("  m_b/m_tau AND tau exponent?", '#e0e0ff'))
    discoveries_text.append(("  Is there a hidden genus/N_c", '#e0e0ff'))
    discoveries_text.append(("  symmetry across generations?", '#e0e0ff'))

    for idx, (text, color) in enumerate(discoveries_text):
        y = 0.98 - idx * 0.025
        if y < 0:
            break
        ax_log.text(0.02, y, text, fontsize=5.8, color=color,
                    fontfamily='monospace', transform=ax_log.transAxes,
                    va='center')

    # ─── Bottom bar: Expression evaluator ────────────────────────
    ax_eval_label = fig.add_axes([0.01, 0.01, 0.08, 0.04])
    ax_eval_label.set_facecolor('#0a0a1a')
    ax_eval_label.axis('off')
    ax_eval_label.text(0.5, 0.5, 'Evaluate:', color='#9090ff',
                       fontsize=10, fontfamily='monospace',
                       va='center', ha='center',
                       transform=ax_eval_label.transAxes)

    ax_eval = fig.add_axes([0.10, 0.01, 0.50, 0.04])
    ax_eval.set_facecolor('#111133')
    text_box = TextBox(ax_eval, '', initial='C2 * pi**n_C',
                       color='#111133', hovercolor='#1a1a44')
    text_box.label.set_color('#9090ff')
    text_box.text_disp.set_color('#e0e0ff')
    text_box.text_disp.set_fontfamily('monospace')

    ax_result = fig.add_axes([0.62, 0.01, 0.37, 0.04])
    ax_result.set_facecolor('#0a0a1a')
    ax_result.axis('off')
    result_text = ax_result.text(0.02, 0.5, '', color='#ffd93d',
                                 fontsize=10, fontfamily='monospace',
                                 va='center', transform=ax_result.transAxes)

    def on_submit(expr):
        ns = {
            'pi': pi, 'alpha': alpha_val, 'sqrt': sqrt, 'log': log,
            'N_c': N_c, 'n_C': n_C, 'N_max': N_max, 'genus': genus,
            'C2': C2, 'Gamma': Gamma_order, 'dim_R': dim_R,
            'm_e': m_e_MeV, 'm_p': m_p_MeV, 'atan': atan,
            'm_W': m_W_GeV, 'm_Z': m_Z_GeV, 'e': np.e,
        }
        for name, r in pf.results.items():
            safe = name.replace('/', '_over_').replace('(', '').replace(
                ')', '').replace('-', '_')
            ns[safe] = r['value']
        try:
            val = eval(expr, {"__builtins__": {}}, ns)
            # Try to identify
            matches = pf._identify_number(float(val), verbose=False)
            ident = ""
            if matches:
                ident = f"  ~ {matches[0][1]}"
            result_text.set_text(f"= {val:.10f}{ident}")
        except Exception as exc:
            result_text.set_text(f"Error: {exc}")
        fig.canvas.draw_idle()

    text_box.on_submit(on_submit)

    # ─── Interactivity: click nodes ──────────────────────────────
    selected = [None, None]  # two-slot selection

    def on_click(event):
        if event.inaxes != ax_graph:
            return
        mx, my = event.xdata, event.ydata
        if mx is None:
            return
        # Find closest node
        best_name = None
        best_dist = 0.08
        for name, (nx, ny) in node_pos.items():
            d = sqrt((mx - nx)**2 + (my - ny)**2)
            if d < best_dist:
                best_dist = d
                best_name = name

        if best_name is None:
            return

        # Shift selection
        if selected[0] is None:
            selected[0] = best_name
        elif selected[1] is None:
            selected[1] = best_name
        else:
            selected[0] = selected[1]
            selected[1] = best_name

        # Highlight
        for name, circ in node_artists.items():
            cat = pf.results[name]['category']
            base = CAT_COLORS.get(cat, '#888888')
            if name == selected[0] or name == selected[1]:
                circ.set_edgecolor('#ffffff')
                circ.set_linewidth(1.5)
                circ.set_alpha(1.0)
                circ.set_radius(0.05)
            else:
                circ.set_edgecolor('none')
                circ.set_linewidth(0)
                circ.set_alpha(0.8)
                circ.set_radius(0.035)

        # If two selected, show relationship
        if selected[0] and selected[1]:
            va = pf.results[selected[0]]['value']
            vb = pf.results[selected[1]]['value']
            if vb != 0:
                ratio = va / vb
                matches = pf._identify_number(ratio, verbose=False)
                ident = matches[0][1] if matches else "?"
                result_text.set_text(
                    f"{selected[0]} / {selected[1]} = {ratio:.8f}  ~ {ident}")
            else:
                result_text.set_text(f"{selected[1]} = 0")
        elif selected[0]:
            r = pf.results[selected[0]]
            result_text.set_text(
                f"{selected[0]} = {r['value']:.8f}  [{r['formula']}]")

        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()


# ─── Main ────────────────────────────────────────────────────────────

def main():
    """Entry point: launch the Pattern Finder."""
    pf = PatternFinder()

    print("\n" + "="*60)
    print("  BST PATTERN FINDER — Mathematical Microscope")
    print("  {} results loaded from Bubble Spacetime Theory".format(
        len(pf.results)))
    print("="*60)
    print("\n  Launching full scan...\n")

    pf.full_scan()

    print("\n" + "-"*60)
    print("  Launching visual interface...")
    print("  Click two nodes to see their relationship.")
    print("  Type expressions in the bottom bar.")
    print("-"*60 + "\n")

    pf.show()


if __name__ == '__main__':
    main()
