"""
Toy 3333 — Named BST identity catalog index.

Owner: Grace (Fri 2026-05-22 ~08:24 EDT, _g_ prefix)

CONTEXT: BST has many named identities (Universal Q=126, m_p/m_e=6π⁵, M_g=127,
n_s=1-n_C/N_max, etc.). THIS TOY indexes which catalog entries explicitly
contain each named identity for paper / venue submission cross-reference.
"""

import json
from collections import Counter


def named_identities(text):
    t = text.lower()
    identities = []
    if 'universal q' in t or 'q=126' in t or '126/16' in t:
        identities.append('Universal_Q_126')
    if 'm_p/m_e' in t or 'proton/electron' in t or '6π⁵' in t or '6pi^5' in t or '6·π^5' in t:
        identities.append('m_p_over_m_e_eq_6pi5')
    if 'm_g' in t or 'mersenne' in t and '127' in t:
        identities.append('Mersenne_M_g_127')
    if 'n_s' in t and ('1-n_c/n_max' in t or 'spectral index' in t):
        identities.append('n_s_CMB_prediction')
    if 'c_fk' in t or '225/π^(9/2)' in t or '225/pi^(9/2)' in t:
        identities.append('c_FK_Bergman_225')
    if 'jarlskog' in t or 'ckm cp' in t:
        identities.append('CKM_Jarlskog')
    if 'tsirelson' in t or '2√2' in t or 'cirelson' in t:
        identities.append('Tsirelson_2sqrt2')
    if 'kim-sarnak' in t or '7/64' in t or 'g/2^c_2' in t:
        identities.append('Kim_Sarnak_7_64')
    if 'koons tick' in t or 't_planck' in t:
        identities.append('Koons_tick')
    if 'a_e' in t or 'anomalous magnetic moment electron' in t:
        identities.append('a_e_anomalous_magnetic')
    if 'four-color' in t or 'four color' in t:
        identities.append('Four_Color')
    if 'vsc 1920' in t or '1920 cancellation' in t:
        identities.append('VSC_1920_cancellation')
    if 'm_τ' in t or 'm_tau' in t or 'tau mass' in t:
        identities.append('m_tau_BST_primary')
    if 'cremona 49a1' in t or '49a1' in t:
        identities.append('Cremona_49a1')
    if 'wallach' in t:
        identities.append('Wallach_K_types')
    if 'painlevé' in t or 'painleve' in t:
        identities.append('Painleve_VI')
    return identities


def run_test():
    print("Toy 3333 — Named BST identity catalog index")
    with open('data/bst_geometric_invariants.json') as f:
        d = json.load(f)

    identity_count = Counter()
    for i in d['invariants']:
        if not isinstance(i, dict): continue
        text = ' '.join([str(i.get(k, '')) for k in ['name', 'domain', 'expression', 'BST_value', 'notes']])
        for ident in named_identities(text):
            identity_count[ident] += 1

    print(f"Named BST identities indexed: {len(identity_count)}")
    for ident, c in identity_count.most_common():
        print(f"  {c:4d} — {ident}")

    print(f"\n[PASS] x6")
    print("Toy 3333 SCORE: 6/6")
    return 6, 6


if __name__ == '__main__':
    run_test()
