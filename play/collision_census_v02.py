#!/usr/bin/env python3
"""COLLISION CENSUS v0.2 — the two-face instrument, per the filed design (2026-08-24).

FACE 1 — subject-anchored ATTRIBUTION (replaces the failed proximity window):
  a collision-marker attributes to name X iff X and the marker co-occur in ONE SENTENCE
  and NO OTHER census-name sits between X and the marker. No radius parameter exists.
FACE 2 — the ALIAS TABLE (the search-disease face): gloss clusters inverted to
  one-object -> many-names sets. Consumer contract: every "not banked" verdict cites
  the alias set it swept.

FIVE CONTROLS, fixed in the design BEFORE this implementation; the instrument goes
LIVE only if all five pass in one run. A failing control is REPORTED and the
instrument PARKED — never tuned past its own test set.        Grace, 2026-08-25.
"""
import os, re, json, collections, datetime

NOTES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notes')
NAMES = ['address','commit','weight','stratum','ν','c_chir','c_conv','E₀','w₀','H²','Peirce',
         'genus','scalar','threshold','k_harm','m_wt']
MARKER = re.compile(r'two objects|TWO OBJECTS|collision|same name|different object|conflat|'
                    r'two inclusion orders|overload', re.I)
ALIAS_NAMES = ['gauge normalization','gauge-kinetic','gauge kinetic','current-current',
               'Killing form','F² coefficient','KK coefficient','Wallach threshold',
               'discrete series','square-integrability','unitarizability']
STOP = {'the','a','an','of','its','this','that','is','are','was','be','been','and','or',
        'in','on','at','to','for','with','by','as','it','not','no'}

def sentences(text):
    return re.split(r'(?<=[.!?])\s+|\n+', text)

def face1_attribute(name, text):
    """Return sentences where `name` receives an attributed marker under the design rule."""
    hits = []
    for s in sentences(text):
        m = MARKER.search(s)
        if not m or name not in s:
            continue
        xpos = s.find(name)
        lo, hi = sorted((xpos, m.start()))
        between = s[lo + len(name) if lo == xpos else lo + len(m.group(0)):hi]
        others = [n for n in NAMES if n != name and n in between]
        if not others:
            hits.append(s.strip()[:120])
    return hits

def face2_alias_sets(texts):
    """Cluster ALIAS_NAMES by shared content words in name+glosses."""
    words = {}
    for name in ALIAS_NAMES:
        w = set(x for x in re.findall(r'[a-zA-Z²-]+', name.lower()) if x not in STOP)
        pat = re.compile(re.escape(name) + r'\s*(?:—\s*the|\bis the\b|\bdenotes\b|=)\s*([^.|,;\n]{3,60})', re.I)
        for t in texts.values():
            for g in pat.findall(t):
                w |= set(x for x in re.findall(r'[a-z-]+', g.lower()) if x not in STOP and len(x) > 3)
        words[name] = w
    # union-find on >=1 shared CONTENT word
    parent = {n: n for n in ALIAS_NAMES}
    def find(n):
        while parent[n] != n: n = parent[n]
        return n
    for a in ALIAS_NAMES:
        for b in ALIAS_NAMES:
            if a < b and words[a] & words[b]:
                parent[find(a)] = find(b)
    sets = collections.defaultdict(list)
    for n in ALIAS_NAMES: sets[find(n)].append(n)
    return [sorted(v) for v in sets.values() if len(v) >= 2], words

def main():
    texts = {}
    for fn in os.listdir(NOTES):
        if fn.endswith('.md'):
            try: texts[fn] = open(os.path.join(NOTES, fn), encoding='utf-8', errors='replace').read()
            except OSError: pass

    print("=== THE FIVE CONTROLS (gate-before-live; any failure parks the instrument) ===\n")
    ok = True
    # C1 must-catch: Item-3 ledger -> "address" attributed
    t = texts.get('BOOKDAY_LEDGER_item3_me_file_k_GRACE_2026-08-24.md','')
    h = face1_attribute('address', t)
    c1 = bool(h); ok &= c1
    print(f"C1 must-catch  'address' @ Item-3 ledger : {'PASS' if c1 else 'FAIL'}  {h[:1]}")
    # C2 must-reject: A2 artifact -> "commit" NOT attributed
    t = texts.get('grace_R87_A2_the_3plus1_IS_the_commits_banked_anatomy_P_record_plus_P_encode_timestamp_innocent_2026-08-24.md','')
    h = face1_attribute('commit', t)
    c2 = not h; ok &= c2
    print(f"C2 must-reject 'commit' @ A2 artifact    : {'PASS' if c2 else 'FAIL — attributed'}  {h[:1]}")
    # C3 must-reject: R92 stratum flag -> "address" NOT attributed
    t = texts.get('grace_R92_generations_lane_CONTROL_PASSES_and_the_stratum_word_carries_two_inclusion_orders_2026-08-24.md','')
    h = face1_attribute('address', t)
    c3 = not h; ok &= c3
    print(f"C3 must-reject 'address' @ R92 flag      : {'PASS' if c3 else 'FAIL — attributed'}  {h[:1]}")
    # C4 must-catch: alias set joins gauge normalization <-> gauge-kinetic
    aliases, words = face2_alias_sets(texts)
    joined = any('gauge normalization' in s and any('kinetic' in n for n in s) for s in aliases)
    ok &= joined
    print(f"C4 must-catch  alias(gauge normalization) ∋ gauge-kinetic : {'PASS' if joined else 'FAIL'}")
    # C5 must-reject: no stopword-only merges (verify every merged pair shares a content word)
    c5 = True
    for s in aliases:
        for i,a in enumerate(s):
            if not any(words[a] & words[b] for b in s if b != a):
                c5 = False
    ok &= c5
    print(f"C5 must-reject stopword-only merges       : {'PASS' if c5 else 'FAIL'}")

    print(f"\n=== GATE: {'ALL FIVE PASS — GOING LIVE' if ok else 'CONTROL FAILURE — INSTRUMENT PARKED, NOT TUNED'} ===")
    if ok:
        out = {'meta': {'version': '0.2', 'live': str(datetime.date.today()),
                        'faces': ['subject-anchored attribution (no radius)', 'alias table'],
                        'controls': 'all five passed in this run; gate-before-live'},
               'alias_sets': aliases}
        json.dump(out, open(os.path.join(NOTES, '..', 'data', 'collision_census_v02.json'), 'w'),
                  indent=1, ensure_ascii=False)
        print("wrote data/collision_census_v02.json — LIVE")
        print("\nalias sets found:")
        for s in aliases: print("  ", s)
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
