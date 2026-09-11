#!/usr/bin/env python3
"""Keeper consumer-match scan: retired/re-tiered readings vs the presentation layer (Curriculum/, Guide/).
Each pattern = a STALE CLAIM FORM with the ruling that retired it. Positive control: a synthetic line per pattern must hit."""
import re,glob,os,sys,collections
ROOT='/Users/cskoons/projects/github/BubbleSpacetimeTheory'
PATS=[
 ("alpha DERIVED (K1816 08-23: IDENTIFIED 08-11, do-not-cite-externally)", r"(deriv\w*[^.\n]{0,60}(α|alpha|fine.structure|137)\b)|((α|alpha)[^.\n]{0,40}\bderived\b)", "we derive α⁻¹ = 137"),
 ("Wyler / 137.036 volume reading (K1826 closed negative)", r"137\.036|Wyler", "Wyler's α"),
 ("2/sqrt(79) lambda (retired; 1/√20 banked T2530)", r"2\s*/\s*(?:\\?sqrt|√)\s*[({]?\s*79", "λ = 2/√79"),
 ("V_cb ~0.044 / 36/869 (VALUE RETIRED K1002→08-22)", r"36\s*/\s*869|0\.044\d*\b", "V_cb = 0.044"),
 ("colour = mediator / V12 / M3(C) (T2543 clause struck 09-09; T2567)", r"(mediator|V_?₁₂|V_?12|J_?½|J_?1/2)[^.\n]{0,40}colou?r|colou?r[^.\n]{0,40}(mediator|V_?₁₂|V_?12)|M[_₃3]\(?ℂ\)?|M_3\(C\)", "mediator J_½ = V₁₂ = color"),
 ("confinement DERIVED unscoped (K1782 08-22: withdrawn as derived; (A1) only)", r"confinement[^.\n]{0,40}\b(derived|proved|proven)\b|\b(derive|derived|proved?)\b[^.\n]{0,40}confinement", "colour confinement is derived"),
 ("genus 7 / Bergman exponent 7 (09-09: genus 5; 7 is a definition)", r"genus[^.\n]{0,15}\b7\b|\b7\b[^.\n]{0,12}genus|exponent[^.\n]{0,12}\b7/2\b[^.\n]{0,20}derived", "the genus 7"),
 ("a_e derived through loops / Selberg terms (K1872 09-07: Petermann–Sommerfield closed form, IDENTIFIED)", r"(a_e|g-2|anomalous magnetic)[^.\n]{0,80}(deriv|Selberg|five loops|0\.026)|(deriv|Selberg)[^.\n]{0,60}(a_e|anomalous magnetic)", "a_e derived through five loops"),
 ("asymptotic freedom b0=7 DERIVED (K1875 09-07: IDENTIFIED with g)", r"(b_?[0₀]\s*=\s*7|asymptotic freedom)[^.\n]{0,60}deriv|deriv[^.\n]{0,60}(asymptotic freedom|b_?[0₀]\s*=\s*7)", "asymptotic freedom derived, b₀ = 7"),
 ("all seven Millennium proved (K939/K940)", r"(all|seven)\s+(seven\s+)?Millennium[^.\n]{0,40}(proved|solved|resolved)|Millennium[^.\n]{0,20}(all seven|7/7)", "all seven Millennium problems are proved"),
 ("RH / Riemann proved or claimed (K21 retracted; K1876 closed as ATTEMPT)", r"(Riemann|RH)[^.\n]{0,40}\b(proved|proven|proof complete|is proved)\b", "the Riemann Hypothesis is proved"),
 ("10^4 permanent bits T1292 (refuted 09-08)", r"10[\^⁴]4?\s*(permanent\s+)?bits|T1292", "10⁴ permanent bits"),
 ("uniqueness FORCED / zero free parameters (Cal §946 09-09: fit with one measured input)", r"(zero\s+(dimensionless\s+)?free\s+parameters|forced,?\s+not\s+fitted|geometry\s+is\s+forced|strong.uniqueness)", "zero free parameters"),
 ("sin²θ_W = 3/13 (retired near miss)", r"3\s*/\s*13", "sin²θ_W = 3/13"),
 ("Koons tick 1.1 as / 137 turns (2π slip; tick = 0.1765 as)", r"1\.1\s*as\b|137\s+turns", "137 turns = 1.1 as"),
 ("98.4% proved (default field, K1802)", r"98\.4\s*%", "98.4% proved"),
 ("SU(3)/colour from geometry (K1724, K1782)", r"SU\(3\)[^.\n]{0,40}(from|out of|emerges from|derived from)[^.\n]{0,30}(geometry|D_?IV|domain|substrate)", "SU(3) emerges from the geometry"),
 ("pentadactyly/biology FORCED (Axis C overclaim, 08-22)", r"(pentadactyl|five fingers|digits)[^.\n]{0,40}forced|forced[^.\n]{0,40}(pentadactyl|five fingers)", "pentadactyly is forced"),
 ("ln 137 (normalisation unit only, K1873)", r"ln\s*\(?137\)?", "ln 137 held"),
 ("Bergman exponent 7/2 DERIVED (relabel; genus 5)", r"7/2[^.\n]{0,30}derived|Bergman exponent[^.\n]{0,20}7/2", "Bergman exponent 7/2 DERIVED"),
]
# positive control
bad=[n for n,rx,syn in PATS if not re.search(rx,syn,re.I)]
print("POSITIVE CONTROL:", "PASS" if not bad else "FAIL "+str(bad))
if bad: sys.exit(1)
files=sorted(glob.glob(ROOT+'/Curriculum/**/*.md',recursive=True)+glob.glob(ROOT+'/Guide/**/*.md',recursive=True))
tot=collections.Counter(); per=collections.defaultdict(collections.Counter); ex={}
for f in files:
    t=open(f,encoding='utf-8',errors='replace').read()
    rel=os.path.relpath(f,ROOT)
    for n,rx,syn in PATS:
        ms=list(re.finditer(rx,t,re.I))
        if ms:
            tot[n]+=len(ms); per[n][rel]+=len(ms)
            if n not in ex: 
                m=ms[0]; ex[n]=(rel, re.sub(r"\s+"," ",t[max(0,m.start()-70):m.end()+70]))
print("files scanned:",len(files))
for n,rx,syn in PATS:
    print("\n== %s == total hits %d in %d files"%(n,tot[n],len(per[n])))
    for rel,c in per[n].most_common(6): print("   %3d  %s"%(c,rel))
    if n in ex: print("   e.g. [%s] …%s…"%(ex[n][0],ex[n][1][:200]))
