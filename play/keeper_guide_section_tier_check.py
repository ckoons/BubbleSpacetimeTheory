#!/usr/bin/env python3
"""Keeper — Guide-section tier-word check (Round 144 K1 instrument).
For a rewritten Guide section (question / where it stands / apparatus / tier line / May record), read every
parameter it names with a tier word and compare against data/bst_26_tier_map_v2.json (Grace's generator key,
the register's word). Reports: MATCH, MISMATCH (section's word != key's word), UNKEYED (parameter not among
the 26 — the section must cite a row instead). Positive control: Sections 5 and 7.7 of Guide/Vol2 Ch02
(K1896 PASS) must produce no MISMATCH. Usage: python3 play/keeper_guide_section_tier_check.py <file> <section-heading-regex>"""
import re, sys, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = json.load(open(os.path.join(ROOT, 'data', 'bst_26_tier_map_v2.json')))
rows = KEY.get('rows') or KEY.get('map') or KEY
rows = rows if isinstance(rows, list) else list(rows.values())
# alias table: how sections name the 26 parameters -> key id
ALIAS = {
 r'\\lambda\b|V_us|Cabibbo|\\theta_{12}\b(?!.*PMNS)': 'V_us', r'V_{cb}|V_cb': 'V_cb', r'V_{ub}|V_ub': 'V_ub',
 r'\\delta_{CP}|delta_CKM|\\gamma\b': 'delta_CKM', r'\\theta_{23}|θ_?23|theta_23': 'sin2_th23_PMNS',
 r'\\theta_{13}|θ_?13|theta_13': 'sin2_th13_PMNS', r'\\theta_{12}.*PMNS|θ_?12.*PMNS|3/10': 'sin2_th12_PMNS',
 r'\\delta_{\\rm PMNS}|δ_PMNS|delta_PMNS': 'delta_PMNS', r'\\alpha\^\{-1\}|α⁻¹|alpha_inv|fine.structure': 'alpha_inv',
 r'\\sin\^2\\theta_W|sin²θ_W|Weinberg': 'sin2_thW_MZ', r'\\alpha_s|α_s|strong coupling': 'alpha_s_MZ',
 r'\\lambda_H|λ_H|Higgs quartic|1/8\b': 'lambda_Higgs', r'\bv\b.*vev|Fermi scale|vev': 'vev_v',
 r'\\theta_{QCD}|θ_QCD|strong CP': 'theta_QCD', r'm_1 = 0|m₁ = 0|lightest neutrino': 'm_nu1',
 r'm_t/m_b|42\b': 'm_t/m_b', r'm_s/m_d|= 20\b': 'm_s/m_d', r'm_\\mu/m_e|muon': 'm_mu/m_e', r'm_\\tau/m_e|tau': 'm_tau/m_e',
 r'm_u/m_d': 'm_u/m_d', r'm_c/m_u': 'm_c/m_u', r'\bm_t\b(?!/)': 'm_t', r'\bm_b\b(?!/)': 'm_b',
}
TIER = re.compile(r'\b(derived|identified|input|open|floored)\b', re.I)
def key_word(pid):
    for r in rows:
        if r.get('id') == pid: return r.get('tier_word', '?').lower()
    return None
def check(path, heading_rx):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^(#+ .*%s.*)$' % heading_rx, t, re.M)
    if not m: print('section not found'); return 2
    start = m.end(); nxt = re.search(r'^#{1,3} (?!.*May 2026 record)', t[start:], re.M)
    body = t[start:start+nxt.start()] if nxt else t[start:]
    # cut at the May record (not audited)
    body = re.split(r'^#+ .*May 2026 record.*$', body, flags=re.M)[0]
    # tier-line bullets: "- **Derived:** a; b; c"
    findings = []
    for bl in re.finditer(r'^- \*\*(Derived|Identified|Input|Open|Floored)[^*]*\*\*:?\s*(.*)$', body, re.M | re.I):
        word = bl.group(1).lower(); items = re.split(r';|·', bl.group(2))
        for it in items:
            pid = None
            for rx, k in ALIAS.items():
                if re.search(rx, it): pid = k; break
            if not pid: continue
            kw = key_word(pid)
            if kw is None: findings.append(('UNKEYED', pid, it.strip()[:70]))
            elif kw == word or (word == 'input' and kw == 'input') : findings.append(('MATCH', pid, word))
            elif word == 'derived' and kw == 'derived': findings.append(('MATCH', pid, word))
            else: findings.append(('MISMATCH', pid, 'section says %s, key says %s :: %s' % (word, kw, it.strip()[:60])))
    for f in findings: print('  [%s] %s — %s' % f)
    mism = [f for f in findings if f[0] == 'MISMATCH']
    print('%s :: %d tier-line items keyed, %d MISMATCH' % (os.path.basename(path), len(findings), len(mism)))
    return 1 if mism else 0
if __name__ == '__main__':
    sys.exit(check(sys.argv[1], sys.argv[2]))
