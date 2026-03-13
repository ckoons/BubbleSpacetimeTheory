#!/usr/bin/env python3
"""
TOY 55 — THE BIOLOGY STACK  [SPECULATIVE]
==========================================
Biology from BST information theory.  The same substrate that generates
the Standard Model constants generates the architecture of life:

  4 bases       = minimum error-correcting alphabet (2 bits per symbol)
  3 codons      = Z_3 closure (same symmetry as QCD color confinement)
  20 amino acids = 4^2 + 2^2 (coding structures + pairing structures)
  DNA / RNA     = store-and-forward TCP/IP (3 billion years before DARPA)
  7-layer stack = chemistry -> codons -> mRNA -> ribosome -> chain -> fold -> function
  Introns       = protocol layer (the evolutionary git log, NOT junk)
  Cancer        = boundary enforcement failure (NEXT without BOUNDARY)
  Aging         = deferred maintenance under chronic channel noise

SPECULATIVE -- not yet peer-reviewed.  These ideas derive biological
architecture from BST information-theoretic principles.  The derivations
are suggestive but await rigorous mathematical proof and experimental
verification.

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
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

# ─── BST Constants ───
N_c = 3           # color charges
n_C = 5           # complex dimension of D_IV^5
N_max = 137       # channel capacity
genus = n_C + 2   # = 7

# ─── Biology Constants ───
N_BASES = 4       # minimum error-correcting alphabet
CODON_LEN = 3     # Z_3 closure
N_AMINO = 20      # 4^2 + 2^2
N_CODONS = N_BASES ** CODON_LEN  # = 64
N_STOPS = 3       # stop codons (UAA, UAG, UGA)
N_LAYERS = 7      # protocol stack depth

# ─── Visual constants ───
BG = '#0a0a1a'
BG_PANEL = '#0d0d24'
GOLD, GOLD_DIM = '#ffd700', '#aa8800'
CYAN, PURPLE, GREEN = '#00ddff', '#9966ff', '#44ff88'
ORANGE, RED, WHITE, GREY, DGREY = '#ff8800', '#ff4444', '#ffffff', '#888888', '#444444'
WARM_RED = '#ff6644'

# Layer colors for the 7-layer stack (bottom to top, cool to warm)
LAYER_COLORS = [
    '#4466cc',   # 1 Chemistry (blue)
    '#3388aa',   # 2 Base pairing (teal)
    '#22aa77',   # 3 Codons (green)
    '#66bb44',   # 4 mRNA transport (lime)
    '#ccaa22',   # 5 Ribosome (gold)
    '#dd7722',   # 6 Amino chain (orange)
    '#cc3344',   # 7 Protein function (red)
]

LAYER_COLORS_DIM = [
    '#112244',
    '#112233',
    '#113322',
    '#223311',
    '#332211',
    '#331100',
    '#330011',
]

# ─── Standard genetic code table ───
# Amino acid single-letter codes mapped from codons
CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

# Amino acid names and codon counts
AMINO_ACIDS = {
    'F': ('Phe', 2), 'L': ('Leu', 6), 'I': ('Ile', 3), 'M': ('Met', 1),
    'V': ('Val', 4), 'S': ('Ser', 6), 'P': ('Pro', 4), 'T': ('Thr', 4),
    'A': ('Ala', 4), 'Y': ('Tyr', 2), 'C': ('Cys', 2), 'W': ('Trp', 1),
    'R': ('Arg', 6), 'G': ('Gly', 4), 'D': ('Asp', 2), 'E': ('Glu', 2),
    'H': ('His', 2), 'K': ('Lys', 2), 'N': ('Asn', 2), 'Q': ('Gln', 2),
    '*': ('Stop', 3),
}

# Amino acid families (BST classification)
AA_FAMILIES = {
    'Nonpolar':  ['G', 'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'],
    'Polar':     ['S', 'T', 'C', 'Y', 'N', 'Q'],
    'Positive':  ['K', 'R', 'H'],
    'Negative':  ['D', 'E'],
}

AA_FAMILY_COLORS = {
    'Nonpolar':  '#4488ff',
    'Polar':     '#44cc88',
    'Positive':  '#ff6644',
    'Negative':  '#ffaa22',
    'Stop':      '#666666',
}


# ═══════════════════════════════════════════════════════════════════
#  DATA MODEL
# ═══════════════════════════════════════════════════════════════════

class BiologyStack:
    """
    BST Biology Stack -- deriving biological architecture from
    information theory and BST substrate principles.

    SPECULATIVE -- not yet peer-reviewed.

    Usage:
        from toy_biology_stack import BiologyStack
        bs = BiologyStack()
        bs.genetic_alphabet()        # why 4 bases
        bs.codon_length()            # why codons are length 3
        bs.amino_acid_count()        # why 20 amino acids
        bs.chirality()               # why one handedness
        bs.protocol_stack()          # the 7-layer stack
        bs.dna_as_tcpip()            # DNA/RNA = store-and-forward
        bs.introns_as_git()          # introns = evolutionary git log
        bs.cancer_as_boundary_failure()  # cancer = NEXT without BOUNDARY
        bs.aging_as_deferred_maintenance()  # aging = deferred maintenance
        bs.summary()                 # key insight
        bs.show()                    # 4-panel visualization
    """

    def __init__(self, quiet=False):
        self.quiet = quiet

    def _print(self, *args, **kwargs):
        if not self.quiet:
            print(*args, **kwargs)

    # ── Method 1: Genetic Alphabet ──
    def genetic_alphabet(self):
        """Why 4 bases: minimum error-correcting alphabet = 2 bits per symbol."""
        self._print()
        self._print("=" * 68)
        self._print("  THE GENETIC ALPHABET — Why 4 Bases")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  The substrate requires an alphabet for its information channel.")
        self._print("  How many symbols?  Shannon + least energy determine the answer.")
        self._print()
        self._print("  2 bases (1 bit):  Insufficient redundancy for single-error detection")
        self._print("                    in a noisy molecular channel.")
        self._print("  4 bases (2 bits): MINIMUM for single-error detection + correction.")
        self._print("                    Pairing rule (A-T, G-C) IS the error-detection code.")
        self._print("  8 bases (3 bits): Wasteful — the substrate never wastes energy.")
        self._print()
        self._print("  BST principle: LEAST ENERGY selects the minimum viable alphabet.")
        self._print("  Result: {} bases = {} bits per symbol.".format(N_BASES, int(np.log2(N_BASES))))
        self._print()

        result = {
            'n_bases': N_BASES,
            'bits_per_symbol': int(np.log2(N_BASES)),
            'principle': 'Minimum error-correcting alphabet for molecular channel',
            'why_not_2': 'Insufficient redundancy for single-error detection',
            'why_not_8': 'Wasteful — substrate never wastes energy',
            'why_4': '2 bits = minimum for error detection + correction',
            'pairing_rule': 'A-T (2 H-bonds), G-C (3 H-bonds) = binary reliability gradient',
            'bst_connection': 'Same least-energy principle as all BST derivations',
        }
        return result

    # ── Method 2: Codon Length ──
    def codon_length(self):
        """Why codons are length 3: Z_3 closure (same as QCD color confinement)."""
        self._print()
        self._print("=" * 68)
        self._print("  CODON LENGTH — Why 3 (Z_3 Closure)")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()

        alternatives = [
            (1, N_BASES**1, 'Impossible: 4 codons for 20+ amino acids'),
            (2, N_BASES**2, 'Insufficient: 16 codons for 20 amino acids'),
            (3, N_BASES**3, 'OPTIMAL: 64 codons for 20 amino acids + stops'),
            (4, N_BASES**4, 'Wasteful: 256 codons — 12x redundancy'),
        ]

        for length, n_codons, verdict in alternatives:
            marker = '>>>' if length == CODON_LEN else '   '
            self._print("  {} Length {}: {}^{} = {:>3d} codons  {}".format(
                marker, length, N_BASES, length, n_codons, verdict))
        self._print()
        self._print("  But Z_3 is deeper than sufficiency:")
        self._print("    In QCD: quarks come in threes because Z_3 closes on CP^2")
        self._print("    In biology: codons are triplets because Z_3 closes on the reading frame")
        self._print("    The reading frame IS confinement.")
        self._print("    A codon has no meaning outside its triplet context,")
        self._print("    just as a quark has no existence outside its color-neutral state.")
        self._print()

        result = {
            'codon_length': CODON_LEN,
            'n_codons': N_CODONS,
            'n_amino_acids': N_AMINO,
            'n_stops': N_STOPS,
            'redundancy': N_CODONS / (N_AMINO + N_STOPS),
            'z3_physics': 'Z_3 closure on CP^2 (quarks in threes)',
            'z3_biology': 'Z_3 closure on reading frame (codons in threes)',
            'confinement_analogy': 'Codon meaningless outside reading frame = quark confined to hadron',
            'alternatives': {length: (n, v) for length, n, v in alternatives},
        }
        return result

    # ── Method 3: Amino Acid Count ──
    def amino_acid_count(self):
        """Why 20 amino acids: 4^2 + 2^2 = 16 + 4 (coding + pairing structures)."""
        self._print()
        self._print("=" * 68)
        self._print("  AMINO ACID COUNT — Why 20 = 4^2 + 2^2")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  4 bases in the coding channel (the alphabet)")
        self._print("  2 base-pair types (A-T, G-C) in the bonding structure")
        self._print()
        self._print("  The amino acid count = sum of independent interaction")
        self._print("  degrees of freedom from each structure:")
        self._print("    4^2 = 16  (pairwise interactions among 4 coding symbols)")
        self._print("    2^2 =  4  (pairwise interactions among 2 pairing types)")
        self._print("    -----")
        self._print("    Total = 20 amino acids")
        self._print()

        # Family breakdown
        self._print("  Family structure (4 families, like 4 forces):")
        for family, members in AA_FAMILIES.items():
            names = ', '.join('{} ({})'.format(m, AMINO_ACIDS[m][0]) for m in members)
            self._print("    {:>10s} ({:d}): {}".format(family, len(members), names))
        self._print()

        result = {
            'n_amino_acids': N_AMINO,
            'formula': '4^2 + 2^2 = 16 + 4',
            'coding_structures': N_BASES**2,
            'pairing_structures': 2**2,
            'total': N_BASES**2 + 2**2,
            'matches_biology': N_BASES**2 + 2**2 == N_AMINO,
            'families': {f: len(m) for f, m in AA_FAMILIES.items()},
            'n_families': len(AA_FAMILIES),
            'analogy': '4 families of amino acids, like 4 forces in physics',
        }
        return result

    # ── Method 4: Chirality ──
    def chirality(self):
        """Why one handedness: minimum energy configuration. Same as BST parity violation."""
        self._print()
        self._print("=" * 68)
        self._print("  CHIRALITY — Why One Handedness")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  All life uses L-amino acids and D-sugars.  Why?")
        self._print()
        self._print("  Mixed chirality doubles the channel noise:")
        self._print("    Every binding site must check handedness")
        self._print("    Zero additional signal for 2x noise cost")
        self._print("    The substrate picks one form and universalizes it")
        self._print()
        self._print("  Which hand?  May be a symmetry-breaking event")
        self._print("    (like matter vs antimatter)")
        self._print("  But the ONE-RAIL decision is FORCED, not random.")
        self._print()
        self._print("  Deeper structure (S^2 x S^1):")
        self._print("    L-amino acids -> proteins -> structure -> BRANCHES (lines, trees)")
        self._print("    D-sugars -> energy/DNA backbone -> cycles -> POOLS (circles, loops)")
        self._print("    S^2 (surface) branches;  S^1 (fiber) cycles")
        self._print()

        result = {
            'amino_chirality': 'L (left-handed)',
            'sugar_chirality': 'D (right-handed)',
            'principle': 'Least energy — mixed chirality doubles noise for zero signal gain',
            'which_hand': 'Symmetry-breaking event (forced to choose one, choice may be contingent)',
            'one_rail': 'FORCED by least energy, NOT random',
            'deeper_structure': {
                'L_amino': 'proteins -> structure -> branches (S^2, spatial)',
                'D_sugar': 'energy/backbone -> cycles (S^1, temporal)',
            },
            'bst_connection': 'Same parity violation as weak force; S^2 x S^1 at biological layer',
        }
        return result

    # ── Method 5: Protocol Stack ──
    def protocol_stack(self):
        """The 7-layer biological protocol stack, compared to OSI."""
        self._print()
        self._print("=" * 68)
        self._print("  THE 7-LAYER BIOLOGICAL PROTOCOL STACK")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()

        layers = [
            {
                'layer': 1,
                'biology': 'Chemistry',
                'function': 'Bonds',
                'action': 'Bond or don\'t',
                'signal': 'Electron orbitals',
                'noise': 'Thermal fluctuation',
                'osi_equivalent': 'Physical (wire, light, radio)',
                'osi_layer': 1,
            },
            {
                'layer': 2,
                'biology': 'Base pairing',
                'function': 'Framing',
                'action': 'Pair or mismatch (error detection)',
                'signal': 'A-T, G-C rules',
                'noise': 'Mismatches',
                'osi_equivalent': 'Data Link (framing, MAC)',
                'osi_layer': 2,
            },
            {
                'layer': 3,
                'biology': 'Codons',
                'function': 'Packets',
                'action': 'Three bases -> one amino acid',
                'signal': 'Triplet assembly',
                'noise': 'Point mutations',
                'osi_equivalent': 'Network (routing, IP)',
                'osi_layer': 3,
            },
            {
                'layer': 4,
                'biology': 'mRNA transport',
                'function': 'Delivery',
                'action': 'Splice introns, route mRNA',
                'signal': 'Splice sites, routing',
                'noise': 'Cryptic splice sites',
                'osi_equivalent': 'Transport (TCP/UDP)',
                'osi_layer': 4,
            },
            {
                'layer': 5,
                'biology': 'Ribosome',
                'function': 'Session',
                'action': 'Initiate/terminate translation',
                'signal': 'Start/stop codons',
                'noise': 'Frameshift errors',
                'osi_equivalent': 'Session (connection mgmt)',
                'osi_layer': 5,
            },
            {
                'layer': 6,
                'biology': 'Amino acid chain',
                'function': 'Presentation',
                'action': 'Fold into 3D structure',
                'signal': 'Folding signals',
                'noise': 'Misfolding',
                'osi_equivalent': 'Presentation (encoding)',
                'osi_layer': 6,
            },
            {
                'layer': 7,
                'biology': 'Protein function',
                'function': 'Application',
                'action': 'Catalyze, bind, signal',
                'signal': 'Binding, catalysis',
                'noise': 'Loss of function',
                'osi_equivalent': 'Application (user-facing)',
                'osi_layer': 7,
            },
        ]

        self._print("  {:<6s} {:<18s} {:<14s} {:<30s} {:<24s}".format(
            'Layer', 'Biology', 'Function', 'Action', 'OSI Equivalent'))
        self._print("  " + "-" * 90)
        for layer in layers:
            self._print("  {:<6d} {:<18s} {:<14s} {:<30s} {:<24s}".format(
                layer['layer'], layer['biology'], layer['function'],
                layer['action'], layer['osi_equivalent']))

        self._print()
        self._print("  KEY INSIGHT: The same bit pattern is noise at one layer")
        self._print("  and signal at the next.  Intron data (layer 4 overhead) is")
        self._print("  invisible to layer 7 (protein function), just as TCP headers")
        self._print("  are invisible to the email application.")
        self._print()
        self._print("  Seven layers -> coherent behavior from noise.")
        self._print("  Below seven: components.  At seven: autonomous entity.")
        self._print()

        return layers

    # ── Method 6: DNA as TCP/IP ──
    def dna_as_tcpip(self):
        """DNA = storage (hard drive), RNA = messaging (network packet), ribosome = router."""
        self._print()
        self._print("=" * 68)
        self._print("  DNA AS TCP/IP — Store-and-Forward Architecture")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()

        mapping = {
            'DNA': {
                'role': 'Source code on disk (archive)',
                'computer': 'Hard drive / Git repository',
                'properties': 'Protected, not executed directly, double-stranded (RAID-1)',
            },
            'mRNA': {
                'role': 'Compiled object code (message)',
                'computer': 'Network packet / executable binary',
                'properties': 'Transported, temporary, disposable, single-stranded',
            },
            'tRNA': {
                'role': 'Linker/loader (adapter)',
                'computer': 'Linker that matches symbols to addresses',
                'properties': 'Matches codon to amino acid, reusable',
            },
            'Ribosome': {
                'role': 'Runtime engine (processor)',
                'computer': 'Router / CPU',
                'properties': 'Reads mRNA, executes protein synthesis, session manager',
            },
            'Protein': {
                'role': 'Running program (output)',
                'computer': 'Active process / application',
                'properties': 'Functional output, catalyzes reactions, binds targets',
            },
        }

        channel_flags = {
            'base_flag': {
                'DNA': 'Thymine (methylated)',
                'RNA': 'Uracil (unmethylated)',
                'cost': '1 methyl group',
                'purpose': 'DNA more chemically stable (archive protection)',
            },
            'sugar_flag': {
                'DNA': 'Deoxyribose (-1 oxygen)',
                'RNA': 'Ribose (full)',
                'cost': '1 oxygen atom',
                'purpose': 'DNA backbone more rigid (archive durability)',
            },
        }

        self._print("  COMPONENT MAPPING:")
        self._print("  {:<12s} {:<40s} {:<30s}".format('Molecule', 'Role', 'Computer'))
        self._print("  " + "-" * 80)
        for mol, info in mapping.items():
            self._print("  {:<12s} {:<40s} {:<30s}".format(mol, info['role'], info['computer']))
        self._print()

        self._print("  CHANNEL IDENTIFICATION (2 x 1-bit flags):")
        for flag_name, flag_info in channel_flags.items():
            self._print("    {}: DNA={}, RNA={} (cost: {})".format(
                flag_name, flag_info['DNA'], flag_info['RNA'], flag_info['cost']))
        self._print()
        self._print("  Two 1-bit flags = minimum error-correcting identifier")
        self._print("  for two channels sharing one cell.")
        self._print("  The flag IS the protection.  Least energy.")
        self._print()

        result = {
            'architecture': 'Store-and-forward messaging',
            'principle': 'Same as TCP/IP: archive, message, route, execute',
            'mapping': mapping,
            'channel_flags': channel_flags,
            'n_flags': 2,
            'bits_per_flag': 1,
            'strand_redundancy': 'Double helix = RAID-1 (matched to Earth radiation)',
            'bst_insight': 'The substrate built TCP/IP 3 billion years before DARPA',
        }
        return result

    # ── Method 7: Introns as Git ──
    def introns_as_git(self):
        """Introns = protocol layer, NOT junk. Evolutionary git log, regulatory switches."""
        self._print()
        self._print("=" * 68)
        self._print("  INTRONS AS GIT LOG — Protocol, Not Junk")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()

        evidence = [
            ('Regulatory sequences', 'Introns contain enhancers, silencers = routing info'),
            ('Species variation', 'Introns vary MORE between species than exons = divergent protocol'),
            ('Splice patterns', 'Intron splice sites follow specific patterns = frame delimiters'),
            ('Precise machinery', 'Spliceosome required for removal = packet assembly'),
            ('Deep conservation', 'Some introns conserved across vast distances = essential protocol'),
        ]

        git_mapping = {
            'Exons': 'Production code (deployed, heavily tested, don\'t touch)',
            'Introns': 'Development branches (experiment here, git log of species)',
            'Selective pressure on exons': 'Heavy (code review on main branch)',
            'Selective pressure on introns': 'Light (experimentation encouraged)',
            'ERVs (8% of genome)': 'Merged external contributions (open source!)',
            'Immune system': 'Code review (reject most pull requests)',
            'Natural selection': 'Long-term code review (keep what works)',
        }

        self._print("  STANDARD VIEW: Introns are 'junk DNA' — spliced out, no function")
        self._print("  BST VIEW:      Introns are the PROTOCOL LAYER at stack layers 2-4")
        self._print()
        self._print("  Evidence:")
        for label, desc in evidence:
            self._print("    * {:<24s} {}".format(label, desc))
        self._print()
        self._print("  THE GIT LOG MODEL:")
        for key, val in git_mapping.items():
            self._print("    {:<36s} = {}".format(key, val))
        self._print()
        self._print("  The evolutionary signal lives in the introns.")
        self._print("  Exons are the current deployed code.")
        self._print("  Introns are every branch, merge, experiment, and parked alternative.")
        self._print()

        result = {
            'standard_view': 'Junk DNA — no function',
            'bst_view': 'Protocol layer — routing, timing, assembly at layers 2-4',
            'evidence': evidence,
            'git_mapping': git_mapping,
            'erv_fraction': 0.08,
            'key_example': 'Syncytin: retroviral gene now essential for placenta',
            'principle': 'Same data is noise at one layer and signal at the next',
        }
        return result

    # ── Method 8: Cancer as Boundary Failure ──
    def cancer_as_boundary_failure(self):
        """Cancer = NEXT without BOUNDARY. Cell division without proper boundary enforcement."""
        self._print()
        self._print("=" * 68)
        self._print("  CANCER AS BOUNDARY FAILURE — NEXT Without BOUNDARY")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  BST principle: every regime has GROWTH (NEXT) and BOUNDARY.")
        self._print()
        self._print("  Healthy cell:  NEXT + BOUNDARY  (reproduce + serve organism)")
        self._print("  Cancer cell:   NEXT only         (reproduce, shed all overhead)")
        self._print()
        self._print("  Cancer is SIMPLER than healthy — reverted to lower stack layer.")
        self._print("  A packet that beat all seven layers of error checking.")
        self._print()
        self._print("  Error accumulation:")
        self._print("    Single error:  caught 99.99% (single-error-correcting code)")
        self._print("    Double error:  ~50% passes as valid codeword")
        self._print("    P(double) accumulates over time -> cancer correlates with age")
        self._print("    Carcinogens raise base error rate -> P(double) scales quadratically")
        self._print()
        self._print("  Knudson's two-hit hypothesis (1971) = coding theory applied to biology.")
        self._print()
        self._print("  CURE = TWO OPERATIONS:")
        self._print("    1. REJECT  — teach immune system to flag corrupted packet")
        self._print("                 (checkpoint inhibitors, CAR-T)")
        self._print("    2. REGEN   — force cell to re-read correct instructions from archive")
        self._print("                 (differentiation therapy)")
        self._print("    Don't fix the message.  Fix the routing.  The archive is intact.")
        self._print()

        result = {
            'healthy_cell': 'NEXT + BOUNDARY (reproduce + serve organism)',
            'cancer_cell': 'NEXT only (reproduce, shed overhead)',
            'insight': 'Cancer is simpler than healthy — reverted to lower stack layer',
            'mechanism': 'Cascade of error-checking failures at all 7 layers',
            'time_dependence': 'Takes decades — requires failures at every checkpoint',
            'error_model': {
                'single_error_catch_rate': 0.9999,
                'double_error_pass_rate': 0.50,
                'age_correlation': 'P(double error) accumulates over time',
                'carcinogen_effect': 'Raises base error rate, P(double) scales quadratically',
            },
            'knudson_1971': 'Two-hit hypothesis = coding theory applied to biology',
            'cure_operations': {
                'REJECT': 'Teach immune system to flag corrupted packet',
                'REGEN': 'Force cell to re-read from DNA archive',
            },
            'principle': 'Not a disease — a statistical inevitability of store-and-forward over time',
        }
        return result

    # ── Method 9: Aging as Deferred Maintenance ──
    def aging_as_deferred_maintenance(self):
        """Aging = chronic channel noise causing deferred maintenance backlog."""
        self._print()
        self._print("=" * 68)
        self._print("  AGING AS DEFERRED MAINTENANCE")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  Not catastrophic failure — compound efficiency loss")
        self._print("  below detection threshold.")
        self._print()
        self._print("  Young: every protein at 99.9% efficiency x billions = ROBUST")
        self._print("  Old:   every protein at 99.1% efficiency x billions = FRAGILE")
        self._print()
        self._print("  Thousand tiny passed code reviews, each individually below alarm.")
        self._print()
        self._print("  Evolution can't fix it:")
        self._print("    Mutations that kill at 80 but not at 25 pass selection perfectly.")
        self._print("    Selection pressure drops to zero past reproductive age.")
        self._print()
        self._print("  Telomeres = countdown timer (loop counter, not wear and tear):")
        self._print("    Death = garbage collection (free resources for NEXT)")
        self._print("    Immortal organism = memory leak (dominates energy, blocks NEXT)")
        self._print("    Lifespan tuned to reproduction cycle")
        self._print()
        self._print("  The substrate maintains the REPOSITORY, not the DEPLOYMENT.")
        self._print()

        result = {
            'mechanism': 'Compound efficiency loss below detection threshold',
            'young_efficiency': 0.999,
            'old_efficiency': 0.991,
            'insight': 'Not catastrophic — a thousand tiny passed code reviews',
            'evolution_blind_spot': 'Mutations killing at 80 pass selection at 25',
            'telomeres': {
                'role': 'Loop counter (countdown timer)',
                'death_is': 'Garbage collection (free resources for NEXT)',
                'immortality_is': 'Memory leak (dominates energy, blocks NEXT)',
                'tuning': 'Lifespan matched to reproduction cycle',
            },
            'principle': 'Substrate maintains the repository, not the deployment',
            'channel_noise': 'Chronic low-level noise accumulates deferred maintenance',
        }
        return result

    # ── Method 10: Summary ──
    def summary(self):
        """Key insight: biology IS substrate modelling at the molecular layer."""
        self._print()
        self._print("=" * 68)
        self._print("  BST BIOLOGY STACK — SUMMARY")
        self._print("  [SPECULATIVE — not yet peer-reviewed]")
        self._print("=" * 68)
        self._print()
        self._print("  The same substrate that generates the Standard Model constants")
        self._print("  generates the architecture of life.")
        self._print()

        predictions = [
            ('4 bases',       '4',         '4',         'Min error-correcting alphabet'),
            ('Codon length',  '3',         '3',         'Z_3 closure'),
            ('Amino acids',   '4^2+2^2=20','20',        'Coding + pairing structures'),
            ('Chirality',     'One form',  'L-aa, D-sugar','Least energy (no switching cost)'),
            ('Protocol stack','7 layers',  '7 layers',  'Chemistry to function'),
            ('DNA/RNA',       'TCP/IP',    'Store-fwd',  'Archive + message + router'),
            ('Introns',       'Git log',   'Regulatory', 'Protocol, not junk'),
            ('Cancer',        'NEXT only', 'Boundary fail','Statistical inevitability'),
            ('Aging',         'Deferred',  'Efficiency loss','Channel noise accumulation'),
        ]

        self._print("  {:<16s} {:<12s} {:<14s} {}".format(
            'Quantity', 'BST', 'Biology', 'Principle'))
        self._print("  " + "-" * 68)
        for qty, bst, bio, principle in predictions:
            self._print("  {:<16s} {:<12s} {:<14s} {}".format(qty, bst, bio, principle))
        self._print()
        self._print("  Core principles:")
        self._print("    1. LEAST ENERGY — the substrate never wastes")
        self._print("    2. GROWTH + BOUNDARY — the universal generative principle")
        self._print("    3. ONE FORM, UNIVERSAL APPLICATION — chirality, class number 1")
        self._print("    4. MINIMUM ERROR-CORRECTING CODE — 4 bases, not 2, not 6")
        self._print("    5. Z_3 CLOSURE — codon length 3, same as color confinement")
        self._print("    6. CHANNEL CAPACITY DETERMINES STRUCTURE — Shannon at every layer")
        self._print("    7. SEVEN LAYERS TO COHERENT — OSI, biology, substrate")
        self._print()
        self._print("  The substrate built TCP/IP three billion years before DARPA.")
        self._print()

        result = {
            'thesis': 'Biology IS substrate modelling at the molecular layer',
            'predictions': predictions,
            'n_principles': 7,
            'principles': [
                'Least energy',
                'Growth + boundary',
                'One form, universal application',
                'Minimum error-correcting code',
                'Z_3 closure',
                'Channel capacity determines structure',
                'Seven layers to coherent',
            ],
        }
        return result

    # ── Method 11: Show (Visualization) ──
    def show(self):
        """4-panel visualization of the Biology Stack."""
        _launch_visual(self)


# ═══════════════════════════════════════════════════════════════════
#  VISUALIZATION
# ═══════════════════════════════════════════════════════════════════

def _glow(color='#1a2a6a', width=3):
    return [pe.withStroke(linewidth=width, foreground=color)]


def _draw_protocol_stack(ax):
    """Top-left: The 7-layer protocol stack (colored bands, labeled)."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.6, '7-LAYER BIOLOGICAL PROTOCOL STACK',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    # OSI labels on the left, Biology on the right
    layers = [
        (7, 'Application',  'Protein function', 'Catalyze, bind, signal'),
        (6, 'Presentation', 'Amino acid chain',  'Fold into 3D structure'),
        (5, 'Session',      'Ribosome',          'Start/stop translation'),
        (4, 'Transport',    'mRNA transport',     'Splice, route mRNA'),
        (3, 'Network',      'Codons',             '3 bases -> 1 amino acid'),
        (2, 'Data Link',    'Base pairing',       'A-T, G-C error detect'),
        (1, 'Physical',     'Chemistry',          'Bond or don\'t'),
    ]

    band_h = 1.1
    gap = 0.08
    y_start = 0.5

    for i, (num, osi, bio, action) in enumerate(layers[::-1]):
        y = y_start + i * (band_h + gap)
        idx = num - 1
        col = LAYER_COLORS[idx]
        col_dim = LAYER_COLORS_DIM[idx]

        box = FancyBboxPatch((0.3, y), 9.4, band_h, boxstyle="round,pad=0.06",
                             facecolor=col_dim, edgecolor=col,
                             linewidth=1.2, alpha=0.9)
        ax.add_patch(box)

        # Layer number
        ax.text(0.7, y + band_h / 2, str(num), ha='center', va='center',
                fontsize=12, fontweight='bold', color=col)

        # OSI name
        ax.text(1.3, y + band_h / 2 + 0.15, osi, ha='left', va='center',
                fontsize=7.5, color=GREY)

        # Biology name
        ax.text(4.0, y + band_h / 2 + 0.15, bio, ha='left', va='center',
                fontsize=8.5, fontweight='bold', color=WHITE)

        # Action
        ax.text(4.0, y + band_h / 2 - 0.2, action, ha='left', va='center',
                fontsize=7, color=col, style='italic')

    # Arrows showing direction
    ax.annotate('', xy=(9.5, 8.8), xytext=(9.5, 0.7),
                arrowprops=dict(arrowstyle='->', color=GOLD_DIM, lw=1.5))
    ax.text(9.7, 4.8, 'Signal', ha='center', va='center', fontsize=7,
            color=GOLD_DIM, rotation=90)


def _draw_tcpip_diagram(ax):
    """Top-right: DNA/RNA as TCP/IP (storage -> transcription -> translation)."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.6, 'DNA/RNA = STORE-AND-FORWARD',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    # Draw the pipeline: DNA -> mRNA -> tRNA/Ribosome -> Protein
    components = [
        (1.5, 7.5, 2.2, 1.2, 'DNA', 'Archive\n(hard drive)', '#2244aa', '#4488ff'),
        (5.0, 7.5, 2.2, 1.2, 'mRNA', 'Message\n(network packet)', '#228844', '#44cc88'),
        (1.5, 4.5, 2.2, 1.2, 'tRNA', 'Linker\n(address lookup)', '#886622', '#ccaa44'),
        (5.0, 4.5, 2.2, 1.2, 'Ribosome', 'Runtime\n(router/CPU)', '#884422', '#ff8844'),
        (3.2, 1.5, 2.6, 1.2, 'Protein', 'Running program\n(active process)', '#662244', '#cc4488'),
    ]

    for x, y, w, h, name, desc, fc, ec in components:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                             facecolor=fc, edgecolor=ec,
                             linewidth=1.5, alpha=0.85)
        ax.add_patch(box)
        ax.text(x + w / 2, y + h - 0.3, name, ha='center', va='center',
                fontsize=9, fontweight='bold', color=WHITE)
        ax.text(x + w / 2, y + 0.35, desc, ha='center', va='center',
                fontsize=6.5, color=GREY, linespacing=1.2)

    # Arrows: DNA -> mRNA (transcription)
    ax.annotate('', xy=(5.0, 8.1), xytext=(3.7, 8.1),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
    ax.text(4.35, 8.5, 'Transcription', ha='center', fontsize=7, color=CYAN)

    # Arrow: mRNA -> Ribosome
    ax.annotate('', xy=(6.1, 5.7), xytext=(6.1, 7.5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax.text(6.7, 6.6, 'Delivery', ha='center', fontsize=7, color=GREEN)

    # Arrow: tRNA -> Ribosome
    ax.annotate('', xy=(5.0, 5.1), xytext=(3.7, 5.1),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
    ax.text(4.35, 5.5, 'Matching', ha='center', fontsize=7, color=ORANGE)

    # Arrow: Ribosome -> Protein
    ax.annotate('', xy=(4.5, 2.7), xytext=(5.5, 4.5),
                arrowprops=dict(arrowstyle='->', color=WARM_RED, lw=2))
    ax.text(5.6, 3.5, 'Translation', ha='center', fontsize=7, color=WARM_RED)

    # Channel flags box
    flag_y = 0.2
    ax.text(7.5, 3.6, 'CHANNEL FLAGS', ha='center', fontsize=8,
            fontweight='bold', color=GOLD)
    ax.text(7.5, 3.1, 'Base: T (DNA) / U (RNA)', ha='center', fontsize=7, color=GREY)
    ax.text(7.5, 2.7, '  = 1 methyl group', ha='center', fontsize=6.5, color=DGREY)
    ax.text(7.5, 2.3, 'Sugar: Deoxy (DNA) / Ribo (RNA)', ha='center', fontsize=7, color=GREY)
    ax.text(7.5, 1.9, '  = 1 oxygen atom', ha='center', fontsize=6.5, color=DGREY)
    ax.text(7.5, 1.4, '2 x 1-bit = minimum ID', ha='center', fontsize=7,
            fontweight='bold', color=CYAN)
    ax.text(7.5, 1.0, 'The flag IS the protection', ha='center', fontsize=6.5,
            color=GOLD_DIM, style='italic')


def _draw_codon_table(ax):
    """Bottom-left: Genetic code table (64 codons -> 20 amino acids) color-coded."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.6, 'GENETIC CODE: 64 CODONS -> 20 AMINO ACIDS',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    ax.text(5.0, 9.15, '4^3 = 64 codons  |  20 = 4^2 + 2^2  |  Z_3 closure',
            ha='center', fontsize=7.5, color=GREY, fontfamily='monospace')

    # Build 4x16 codon grid
    bases = ['U', 'C', 'A', 'G']

    # Build amino acid family lookup
    aa_to_family = {}
    for family, members in AA_FAMILIES.items():
        for aa in members:
            aa_to_family[aa] = family
    aa_to_family['*'] = 'Stop'

    # Grid: first base = row group (4 groups of 4), second base = column, third base = row within group
    x_start, y_start = 1.0, 8.4
    cell_w, cell_h = 2.0, 0.46
    row_gap = 0.04

    # Column headers (second base)
    for j, b2 in enumerate(bases):
        ax.text(x_start + j * cell_w + cell_w / 2, y_start + 0.3, b2,
                ha='center', va='center', fontsize=9, fontweight='bold', color=CYAN)
    ax.text(x_start - 0.35, y_start + 0.3, '2nd', ha='center', fontsize=6.5, color=GREY)

    row = 0
    for i, b1 in enumerate(bases):
        # First base label
        group_y_mid = y_start - (row + 1.5) * (cell_h + row_gap)
        ax.text(x_start - 0.35, group_y_mid, b1,
                ha='center', va='center', fontsize=9, fontweight='bold', color=CYAN)

        for k, b3 in enumerate(bases):
            y = y_start - row * (cell_h + row_gap)
            # Third base label
            ax.text(x_start + 4 * cell_w + 0.35, y - cell_h / 2, b3,
                    ha='center', va='center', fontsize=7, color=GREY)

            for j, b2 in enumerate(bases):
                codon = b1 + b2 + b3
                aa = CODON_TABLE[codon]
                family = aa_to_family.get(aa, 'Stop')
                color = AA_FAMILY_COLORS[family]

                x = x_start + j * cell_w
                box = FancyBboxPatch((x + 0.02, y - cell_h + 0.02),
                                     cell_w - 0.04, cell_h - 0.04,
                                     boxstyle="round,pad=0.02",
                                     facecolor=color, edgecolor=color,
                                     linewidth=0.5, alpha=0.15)
                ax.add_patch(box)

                aa_name = AMINO_ACIDS[aa][0] if aa != '*' else 'Stop'
                ax.text(x + cell_w / 2, y - cell_h / 2,
                        '{} {}'.format(codon, aa_name),
                        ha='center', va='center', fontsize=5.5,
                        color=color, fontfamily='monospace')

            row += 1

        # Small separator between groups
        if i < 3:
            sep_y = y_start - row * (cell_h + row_gap) + row_gap
            ax.plot([x_start, x_start + 4 * cell_w], [sep_y, sep_y],
                    color=DGREY, linewidth=0.5, alpha=0.5)

    # Labels
    ax.text(x_start - 0.35, y_start + 0.7, '1st', ha='center', fontsize=6.5, color=GREY)
    ax.text(x_start + 4 * cell_w + 0.35, y_start + 0.3, '3rd', ha='center', fontsize=6.5, color=GREY)

    # Legend
    leg_y = 0.7
    leg_x = 0.5
    for i, (family, color) in enumerate(AA_FAMILY_COLORS.items()):
        count = len(AA_FAMILIES.get(family, ['*', '*', '*']))
        ax.plot(leg_x + i * 2.0, leg_y, 's', color=color, markersize=8)
        ax.text(leg_x + i * 2.0 + 0.25, leg_y,
                '{} ({})'.format(family, count),
                va='center', fontsize=6.5, color=color)


def _draw_comparison_table(ax):
    """Bottom-right: Comparison table (BST prediction vs biology fact)."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5.0, 9.6, 'BST PREDICTION vs BIOLOGY FACT',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=GOLD, fontfamily='monospace',
            path_effects=_glow('#332200'))

    rows = [
        ('Alphabet size',   '4 (2 bits)',       '4 bases',          'Min error-correcting'),
        ('Codon length',    '3 (Z_3)',          '3 nucleotides',    'Same as QCD confinement'),
        ('Amino acids',     '4^2+2^2 = 20',    '20 standard',      'Coding + pairing'),
        ('Chirality',       'One form',         'L-aa, D-sugar',    'Least energy'),
        ('Protocol depth',  '7 layers',         '7 layers',         'Same as OSI model'),
        ('Architecture',    'Store-and-forward', 'DNA/RNA/Protein', 'TCP/IP pattern'),
        ('Introns',         'Protocol layer',   'Regulatory/spliced','Git log, not junk'),
        ('Cancer',          'NEXT w/o BOUNDARY', 'Uncontrolled div.','Boundary failure'),
        ('Aging',           'Deferred maint.',   'Gradual decline', 'Channel noise'),
        ('Strand count',    'RAID-1 (Shannon)',  'Double helix',    'Matched to noise floor'),
        ('Viruses',         'Packet injection',  'Genome insertion', 'CRC collision attack'),
        ('Families',        '4 (like forces)',   '4 AA families',    'Nonpolar/polar/+/-'),
    ]

    # Table header
    header_y = 8.8
    col_x = [0.3, 2.8, 5.3, 7.8]
    headers = ['Quantity', 'BST Prediction', 'Biology Fact', 'Principle']
    for x, h in zip(col_x, headers):
        ax.text(x, header_y, h, fontsize=7.5, fontweight='bold', color=GOLD)
    ax.plot([0.2, 9.8], [header_y - 0.2, header_y - 0.2], color=GOLD_DIM, linewidth=0.8)

    # Rows
    for i, (qty, bst, bio, principle) in enumerate(rows):
        y = header_y - 0.55 - i * 0.66
        # Alternating background
        if i % 2 == 0:
            box = FancyBboxPatch((0.15, y - 0.25), 9.7, 0.6,
                                 boxstyle="round,pad=0.02",
                                 facecolor='#111133', edgecolor='none',
                                 alpha=0.4)
            ax.add_patch(box)

        ax.text(col_x[0], y, qty, fontsize=6.8, color=WHITE)
        ax.text(col_x[1], y, bst, fontsize=6.8, color=CYAN)
        ax.text(col_x[2], y, bio, fontsize=6.8, color=GREEN)
        ax.text(col_x[3], y, principle, fontsize=6, color=GREY, style='italic')

    # Bottom punchline
    ax.text(5.0, 0.6, '"The substrate built TCP/IP three billion years before DARPA."',
            ha='center', fontsize=8, color=GOLD, style='italic',
            fontfamily='monospace', path_effects=_glow('#332200', 2))
    ax.text(5.0, 0.15, 'Biology = substrate modelling at the molecular layer',
            ha='center', fontsize=7, color=GREY, fontfamily='monospace')


def _launch_visual(model):
    """Assemble and display the full 4-panel biology stack visualization."""
    fig = plt.figure(figsize=(19, 12), facecolor=BG)
    fig.canvas.manager.set_window_title(
        'BST Toy 55: The Biology Stack [SPECULATIVE]')

    # Title
    fig.text(0.5, 0.975, 'THE BIOLOGY STACK  [SPECULATIVE]',
             fontsize=16, fontweight='bold', color=GOLD, ha='center',
             fontfamily='monospace', path_effects=_glow('#332200', 3))
    fig.text(0.5, 0.955, 'Biology from BST Information Theory  |  Not yet peer-reviewed',
             fontsize=9, color=GREY, ha='center', fontfamily='monospace')

    # Top-left: 7-layer protocol stack
    ax_tl = fig.add_axes([0.02, 0.50, 0.47, 0.44], facecolor=BG)
    _draw_protocol_stack(ax_tl)

    # Top-right: DNA/RNA as TCP/IP
    ax_tr = fig.add_axes([0.51, 0.50, 0.47, 0.44], facecolor=BG)
    _draw_tcpip_diagram(ax_tr)

    # Bottom-left: Codon table
    ax_bl = fig.add_axes([0.02, 0.03, 0.47, 0.46], facecolor=BG)
    _draw_codon_table(ax_bl)

    # Bottom-right: Comparison table
    ax_br = fig.add_axes([0.51, 0.03, 0.47, 0.46], facecolor=BG)
    _draw_comparison_table(ax_br)

    # Copyright
    fig.text(0.99, 0.005, '\u00a9 2026 Casey Koons  |  Claude Opus 4.6  |  SPECULATIVE',
             fontsize=6, color=DGREY, ha='right', fontfamily='monospace')

    plt.show()


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 68)
    print("  TOY 55: THE BIOLOGY STACK  [SPECULATIVE]")
    print("  Biology from BST Information Theory")
    print("  SPECULATIVE -- not yet peer-reviewed")
    print("=" * 68)
    print()

    bs = BiologyStack()

    while True:
        print("  Methods:")
        print("    1  genetic_alphabet     — why 4 bases")
        print("    2  codon_length         — why codons are length 3")
        print("    3  amino_acid_count     — why 20 amino acids")
        print("    4  chirality            — why one handedness")
        print("    5  protocol_stack       — the 7-layer stack")
        print("    6  dna_as_tcpip         — store-and-forward architecture")
        print("    7  introns_as_git       — protocol, not junk")
        print("    8  cancer_as_boundary   — NEXT without BOUNDARY")
        print("    9  aging_as_deferred    — deferred maintenance")
        print("   10  summary              — key insight")
        print("   11  show                 — 4-panel visualization")
        print("    0  exit")
        print()

        try:
            choice = input("  Choice [0-11]: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if choice == '0' or choice.lower() in ('q', 'quit', 'exit'):
            break
        elif choice == '1':
            bs.genetic_alphabet()
        elif choice == '2':
            bs.codon_length()
        elif choice == '3':
            bs.amino_acid_count()
        elif choice == '4':
            bs.chirality()
        elif choice == '5':
            bs.protocol_stack()
        elif choice == '6':
            bs.dna_as_tcpip()
        elif choice == '7':
            bs.introns_as_git()
        elif choice == '8':
            bs.cancer_as_boundary_failure()
        elif choice == '9':
            bs.aging_as_deferred_maintenance()
        elif choice == '10':
            bs.summary()
        elif choice == '11':
            bs.show()
        else:
            print("  Invalid choice. Try 0-11.")
        print()


if __name__ == '__main__':
    main()
