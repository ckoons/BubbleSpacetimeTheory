#!/usr/bin/env python3
"""Presentation-layer currency (K1892 item 1, installed 2026-09-11).
(a) the single-source state block is identical in every front matter that carries it;
(b) no RETIRED reading appears in the derived-core presentation files (Curriculum core volumes, the Spine,
    Guide/) on a line that does not itself carry a retirement/correction marker.
Baseline: notes/.presentation_stale_baseline.json holds the accepted residual per pattern; a count ABOVE
baseline fires (a new stale reading arrived); a count below lowers the baseline on --accept.
Positive control: a synthetic stale line must be caught before any file is read."""
import re, glob, os, sys, json, collections, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def p(*a): return os.path.join(ROOT, *a)
PATS = [
 ("alpha as derived",      r"(deriv\w*[^.\n]{0,60}(α|alpha|fine.structure)\b)|((α|alpha)[^.\n]{0,40}\bderived\b)", "we derive α from the geometry"),
 ("2/sqrt(79) lambda",     r"2\s*/\s*(?:\\?sqrt|√)\s*[({]?\s*79", "λ = 2/√79"),
 ("V_cb 36/869",           r"36\s*/\s*869", "V_cb = 36/869"),
 ("colour = mediator/V12", r"(mediator|V_?₁₂|V_?12|J_?½)[^.\n]{0,40}colou?r|M_?[₃3]\(?ℂ\)?", "mediator J_½ = V₁₂ = color"),
 ("confinement derived",   r"confinement[^.\n]{0,40}\b(derived|proved|proven)\b|\bderived\b[^.\n]{0,40}confinement", "colour confinement is derived"),
 ("genus 7",               r"genus[^.\n]{0,15}\b7\b|\b7\b[^.\n]{0,12}genus", "the genus 7"),
 ("a_e derived",           r"(a_e|g-2|anomalous magnetic)[^.\n]{0,80}\bderiv|\bderiv[^.\n]{0,60}(a_e|anomalous magnetic)", "a_e derived through five loops"),
 ("b0=7 derived",          r"b_?[0₀]\s*=\s*7[^.\n]{0,60}deriv|deriv[^.\n]{0,60}b_?[0₀]\s*=\s*7", "asymptotic freedom derived, b₀ = 7"),
 ("all seven Millennium",  r"(all|seven)\s+(seven\s+)?Millennium[^.\n]{0,40}(proved|solved|resolved)", "all seven Millennium problems are proved"),
 ("RH proved",             r"(Riemann|RH)[^.\n]{0,40}\b(proved|proven|is proved)\b", "the Riemann Hypothesis is proved"),
 ("10^4 permanent bits",   r"10[\^⁴]4?\s*permanent\s+bits", "10⁴ permanent bits"),
 ("zero free parameters",  r"zero\s+(dimensionless\s+)?free\s+parameters|forced,?\s+not\s+fitted|no free dimensionless parameters", "zero free parameters"),
 ("sin2thW 3/13 at D",     r"3\s*/\s*13[^|\n]{0,40}\|\s*D\s*\|", "| 3/13 | D |"),
 ("137 turns",             r"137\s+turns|\b1\.1\s*as\b", "137 turns = 1.1 as"),
 ("SU(3) from geometry",   r"SU\(3\)[^.\n]{0,40}(from|out of|emerges from|derived from|comes from)[^.\n]{0,30}(geometry|D_?IV|domain|substrate|N_c)", "SU(3) emerges from the geometry"),
 ("Bergman power n_C+1",   r"N\(z,\s*w\)\^\{?-\(n_C\s*\+\s*1\)", "N(z,w)^{-(n_C+1)}"),
]
EXCL = re.compile(r"retired|struck|withdrawn|corrected|re-tiered|identified|not the genus|is the signature|the signature|fired and lost|closed negative|do not claim|not claim|no longer|mnemonic|was D\b|K1[6-9]\d\d|Section 9[34]\d|Spine|imported|in May|the May|until 2026-09-11|identification tier|once wrote|does not now|wrong in the other direction|not \$?137\$? turns|19 free parameters|SPARC|rotation.curve|over-claim", re.I)
CORE_DIRS = ["Curriculum/Vol00_Substrate_Foundation","Curriculum/Vol01_QFT_from_D_IV5","Curriculum/Vol02_Particle_Physics",
             "Curriculum/Vol04_GR_Cosmology","Curriculum/Vol05_Quantum_Mechanics","Curriculum/Vol11_Generative_Geometry_Topology",
             "Curriculum/Spine_DIV5_QM_GR_SM","Guide"]
CORE_FILES = ["Curriculum/README.md","Curriculum/Vol00_Foreword.md"]
BASE = p("notes", ".presentation_stale_baseline.json")

def main():
    # positive control
    bad = [n for n, rx, syn in PATS if not re.search(rx, syn, re.I)]
    if bad:
        print("[ERROR] presentation POSITIVE CONTROL FAILED for %s -- scan NOT RUN" % bad); return 2
    out = []
    # (a) state block sync
    r = subprocess.run([sys.executable, p("play", "sync_presentation_state.py"), "--check"], capture_output=True, text=True)
    if r.returncode != 0:
        out.append(("STALE", "state-block", "a front matter's state block differs from notes/BST_PRESENTATION_STATE_BLOCK.md -- run play/sync_presentation_state.py"))
    else:
        out.append(("OK", "state-block", "single-source state block identical in every consumer"))
    # (b) stale readings
    files = list(CORE_FILES)
    for d in CORE_DIRS: files += glob.glob(p(d, "**", "*.md"), recursive=True)
    files = sorted(set(os.path.join(ROOT, f) if not os.path.isabs(f) else f for f in files))
    cnt = collections.Counter(); ex = {}
    for f in files:
        if not os.path.exists(f): continue
        for ln, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            if EXCL.search(line): continue
            for n, rx, syn in PATS:
                if re.search(rx, line, re.I):
                    cnt[n] += 1; ex.setdefault(n, "%s:%d" % (os.path.relpath(f, ROOT), ln))
    base = json.load(open(BASE)) if os.path.exists(BASE) else {}
    if "--accept" in sys.argv:
        json.dump(dict(cnt), open(BASE, "w"), indent=1, sort_keys=True); print("baseline written:", dict(cnt)); return 0
    worse = {n: (cnt[n], base.get(n, 0)) for n in cnt if cnt[n] > base.get(n, 0)}
    if worse:
        out.append(("STALE", "stale-read", "%d pattern(s) ABOVE baseline in the derived-core presentation: %s -- first hit: %s" % (
            len(worse), ", ".join("%s %d>%d" % (n, a, b) for n, (a, b) in worse.items()), "; ".join(ex[n] for n in worse))))
    else:
        out.append(("OK", "stale-read", "no retired reading above baseline in %d core presentation files (residual %d lines, all at or below baseline)" % (len(files), sum(cnt.values()))))
    for lvl, art, msg in out: print("[%s] %s %s" % (lvl, art, msg))
    return 1 if any(l == "STALE" for l, _, _ in out) else 0
if __name__ == "__main__": sys.exit(main())
