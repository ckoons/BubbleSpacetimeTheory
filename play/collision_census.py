#!/usr/bin/env python3
"""COLLISION CENSUS — measure name-overload across the corpus BY BINDINGS, not by anecdote.

A collision = one name carrying multiple distinct objects (the week's disease: 23 confirmed
in three days, every one caught only after the name was load-bearing).  This instrument
measures a PROXY: for each candidate name, harvest its explicit bindings ("X = <rhs>") and
glosses, cluster the right-hand sides, and report the DEGREE (distinct binding clusters).

HONESTY CONTRACT
- The proxy is stated: distinct normalized bindings.  Extraction is NOT a ruling; every
  degree is a CANDIDATE until read by the object (retirement-record discipline).
- Controls are corpus-sourced (the week's confirmed collisions) and GATE the read:
  if the must-catch median degree fails to exceed the must-reject median, the instrument
  has no discriminating power and NO prediction is published.
- Scope stated, not silent: single-letter latin symbols are EXCLUDED (binding noise
  drowns signal); the census covers greek letters, multi-char symbols, and named phrases.
Grace, 2026-08-24 — own-time work, Casey-authorized.
"""
import os, re, sys, json, collections

NOTES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notes')

# ---- candidate names (curated; scope stated in the docstring) ----
NAMES = ['ν','λ','ρ','μ','σ','χ','ε','θ','δ','ω','Δ','Σ','Ω','Γ',
         'E₀','w₀','m_wt','k_harm','ν_strat','m_Q','c_chir','c_conv','C₂','C_2','N_c','n_C',
         'N_max','J₀','V₁₂','H²','L_λ','T³_R','B−L','y_t','J_CKM',
         'Wallach threshold','Wallach set','self-shadow','Peirce','genus','democratic',
         'singular point','the ruler','scalar Bergman','formal degree','custodial',
         'commit','the identity','spin factor','isotropy','first zero','Hardy point']

# ---- controls, corpus-sourced (confirmed this week) ----
MUST_CATCH  = ['ν','Wallach threshold','self-shadow','Peirce','genus','C₂','H²','E₀','scalar Bergman','isotropy']
MUST_REJECT = ['N_max','J_CKM','y_t','Hardy point']   # believed single-object; risk noted

BIND = re.compile(r'(?:^|[\s(|])(%s)\s*(?:=|:=|≡|—\s*the|\bis the\b|\bdenotes\b)\s*([^.|,;\n]{3,70})')

def norm(rhs):
    r = rhs.strip().lower()
    r = re.sub(r'[*_`$\\{}()]', '', r)
    r = re.sub(r'\s+', ' ', r)
    r = re.sub(r'[0-9.]+%', '', r)
    return r[:48]

def cluster(bindings):
    """crude dedup: normalized-prefix clustering."""
    seen = []
    for b in bindings:
        if not any(b[:20] == s[:20] or (len(b) > 8 and (b in s or s in b)) for s in seen):
            seen.append(b)
    return seen

def main():
    texts = {}
    for fn in os.listdir(NOTES):
        if fn.endswith('.md'):
            try:
                texts[fn] = open(os.path.join(NOTES, fn), encoding='utf-8', errors='replace').read()
            except OSError:
                pass
    census = {}
    for name in NAMES:
        pat = re.compile(r'(?:^|[\s(|>])' + re.escape(name) +
                         r'\s*(?:=|≡|—\s*the|\bis the\b|\bdenotes\b)\s*([^.|,;\n]{3,70})', re.M)
        binds, files = [], set()
        for fn, t in texts.items():
            hits = pat.findall(t)
            if hits:
                files.add(fn)
                binds += [norm(h) for h in hits]
        cl = cluster(sorted(set(binds)))
        census[name] = {'degree': len(cl), 'n_files': len(files),
                        'clusters': cl[:6], 'load': len(files) * max(1, len(cl))}
    # ---- gate ----
    med = lambda xs: sorted(xs)[len(xs)//2] if xs else 0
    mc = [census[n]['degree'] for n in MUST_CATCH if n in census]
    mr = [census[n]['degree'] for n in MUST_REJECT if n in census]
    print(f"GATE  must-catch degrees {mc} (median {med(mc)})  |  must-reject {mr} (median {med(mr)})")
    ok = med(mc) > med(mr)
    print(f"GATE  discriminating power: {'PASS' if ok else 'FAIL — NO PREDICTION PUBLISHED'}\n")
    ranked = sorted(census.items(), key=lambda kv: -kv[1]['load'])
    print(f"{'name':22s} {'deg':>4} {'files':>6} {'load':>6}   sample clusters")
    for n, d in ranked[:24]:
        print(f"{n:22s} {d['degree']:>4} {d['n_files']:>6} {d['load']:>6}   {d['clusters'][:2]}")
    json.dump(census, open(os.path.join(NOTES, '..', 'data', 'collision_census.json'), 'w'),
              indent=1, ensure_ascii=False)
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())

# ---- v0.2: BLINDNESS CHECK AT FILING (requirement created by the R92 scoring correction) ----
def blindness_check(predicted_names, filer_same_day_files, notes_dir=NOTES):
    """A prediction is CONTAMINATED if its name co-occurs with collision-markers in the
    filer's OWN same-day artifacts. Mere occurrence is not contamination (that would flag
    everything); the criterion is a collision-in-progress on the predicted name."""
    MARKERS = re.compile(r'two objects|TWO OBJECTS|collision|same name|different object|'
                         r'conflat|two inclusion orders|overload', re.I)
    verdicts = {}
    for name in predicted_names:
        hits = []
        for fn in filer_same_day_files:
            path = os.path.join(notes_dir, fn)
            if not os.path.exists(path):
                continue
            t = open(path, encoding='utf-8', errors='replace').read()
            for m in re.finditer(re.escape(name), t):
                window = t[max(0, m.start()-200):m.start()+200]
                if MARKERS.search(window):
                    hits.append(fn)
                    break
        verdicts[name] = ('CONTAMINATED — collision-in-progress in filer\'s own same-day artifact: '
                          + hits[0]) if hits else 'CLEAN'
    return verdicts
