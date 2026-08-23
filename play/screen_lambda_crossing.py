#!/usr/bin/env python3
"""Screen for the lambda-crossing defect: a file that places a FERMIONIC object in a
SCALAR / lambda=0 space while also carrying a HALF-INTEGER K-type address.

Origin: grace_lepton_norm_convention_pin_2026-08-18 said "leptons | full SCALAR
Bergman space H^2(D_IV^5)" on line 45 and sent the muon run to "the Kostant-Dirac
image (3/2, 1/2)" nine lines later.  (3/2,1/2) is a spinor K-type -- second row 1/2 --
so the computation was in the spinor bundle and only the prose said scalar.  The
crossing was detectable INSIDE one file.

★ THE REJECT ARM IS THE POINT (Keeper's condition).  Co-occurrence cannot tell a file
that CONFLATES the two spaces from one that CONTRASTS them.  A file that correctly
distinguishes H^2_{lambda=0} from H^2_{lambda} must NOT score as a defect, or the screen
reports discussion as disease.  Report k-of-N-of-which-m-are-real, never the denominator.

Grace, 2026-08-23.
"""
import os, re, sys

FERMION = re.compile(r'\b(fermion|lepton|quark|electron|muon|tau|neutrino|spinor)s?\b', re.I)
# an explicit claim of scalar-ness / lambda=0, not a mere mention of H^2
SCALARCLAIM = re.compile(
    r'(scalar\s+(Bergman|Hardy|holomorphic)|'
    r'ordinary\s+holomorphic\s+function|'
    r'holomorphic\s+functions?\s+on\s+D_IV|'
    r'full\s+scalar)', re.I)
# a half-integer K-type address: (a/2, b/2) or (3/2, 1/2) style
HALFINT = re.compile(r'\(\s*\d+\s*/\s*2\s*,\s*(?:\d+\s*/\s*2|½)\s*\)|\(\s*\d+/2\s*,\s*½\s*\)')
# ★ THE REJECT ARM: the file makes the distinction explicitly
DISTINGUISHES = re.compile(
    r'(H[²2]_\{?\\?lambda|H[²2]_\{?λ|lambda\s*=\s*0|λ\s*=\s*0|'
    r'spinor\s+bundle|induced\s+bundle|H[²2]_f|'
    r'rank-?4\s+vector\s+bundle|not\s+scalar)', re.I)

def scan(root):
    hits, rejected, considered = [], [], 0
    for dp, _, names in os.walk(os.path.join(root, 'notes')):
        for nm in names:
            if not nm.endswith('.md'):
                continue
            p = os.path.join(dp, nm)
            try:
                t = open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            if not HALFINT.search(t):
                continue                      # denominator: files with a K-type address
            considered += 1
            if not (FERMION.search(t) and SCALARCLAIM.search(t)):
                continue
            rel = os.path.relpath(p, root)
            if DISTINGUISHES.search(t):
                rejected.append(rel)          # discusses both, correctly -- NOT a defect
            else:
                hits.append(rel)
    return hits, rejected, considered

def main(root):
    hits, rejected, considered = scan(root)
    joined = ' '.join(hits + rejected)

    # controls, copied from the corpus
    must_catch = 'grace_lepton_norm_convention_pin_2026-08-18'   # the origin defect
    caught = any(must_catch in h for h in hits + rejected)
    # after its correction the SAME file distinguishes -> must land in the REJECT arm
    correctly_rejected = any(must_catch in r for r in rejected)

    print(f"files carrying a half-integer K-type address (denominator): {considered}")
    print(f"FLAGGED for screening: {len(hits)}   |   rejected by the contrast arm: {len(rejected)}")
    print(f"\nCONTROLS")
    print(f"  must-catch  origin file is seen at all      : {'PASS' if caught else 'FAIL'}")
    print(f"  must-reject same file, once CORRECTED, is   : "
          f"{'PASS (in reject arm)' if correctly_rejected else 'FAIL (still flagged)'}")
    if not caught:
        print("\nINSTRUMENT NOT VALIDATED — origin defect invisible. Read refused.")
        return 1
    print(f"\nFLAGGED (screen these BY THE OBJECT — co-occurrence is not conflation):")
    for h in hits:
        print(f"   {h}")
    print(f"\nHONEST LABEL: {len(hits)} candidates for screening out of {considered} "
          f"files with a K-type address, of which UNKNOWN are real until read.")
    print("Do not quote the denominator as a defect rate.")
    return 0

if __name__ == '__main__':
    sys.exit(main(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
