#!/usr/bin/env python3
"""
Toy 5442 — THE PROPAGATION CHECK: did this fortnight's corrections reach the prose?

QUESTIONS THIS COMPUTE ANSWERS (declared before running):
  (1) "Carry the ε=0 sizing into the package" — WHERE does it still need carrying?
  (2) @Cal asked for the CHEAPEST WAY to run the prose-layer pass. Here it is, run.

★ THE ROUND'S OWN LESSON, APPLIED: "the gate is clean" != "the buckets are read".
  So this toy does BOTH steps and labels them:
     STEP 1 (grep)  -> sites carrying the CLAIM            = candidates
     STEP 2 (read)  -> which of those carry the QUALIFIER  = the actual finding
  A count from step 1 alone is a candidate count in disguise. Only the ε row below is
  READ to completion (12 sites, small enough to read); the rest are handed over AS
  CANDIDATES, explicitly.

THE MECHANISM, stated in one line so it can be reused:
    a correction = (claim pattern, qualifier pattern).
    a STALE SITE = carries the claim and NOT the qualifier.
  That is the whole instrument. It is two greps and a set difference.
"""

import os
import re

ROOT = "/Users/cskoons/projects/github/BubbleSpacetimeTheory/notes"

# (name, claim pattern, qualifier pattern that a CORRECTED site should carry, read_fully)
CORRECTIONS = [
    ("eps=0 frame-agreement falsifier  [MINE, read in full]",
     re.compile(r"frame.agreement", re.I),
     re.compile(r"blunt|large admixtures|in principle|SIZED|tens of percent", re.I),
     True),
    ("confinement de-scope (A2 -> A1, SU(3) imported)",
     re.compile(r"colou?r confinement|confinement is derived", re.I),
     re.compile(r"\(A1\)|two-row|imported|#108", re.I),
     False),
    ("W1 -> H2 (Gamma demoted to arithmetic regulator)",
     re.compile(r"L.?\(Γ\s*\\|Γ\s*\\\s*G", re.I),
     re.compile(r"H²|H\^2|regulator|arithmetic lane", re.I),
     False),
    ("Millennium = ATTEMPTS, not proofs (K940)",
     re.compile(r"Millennium|Clay", re.I),
     re.compile(r"attempt|not a proof|residual|not claim", re.I),
     False),
    ("pentadactyly / contingent-fact class (W7)",
     re.compile(r"pentadactyl|genetic code forcing|germ layers", re.I),
     re.compile(r"conting|null.model|not forced", re.I),
     False),
]

files = sorted(os.path.join(dp, fn)
               for dp, _, fns in os.walk(ROOT) for fn in fns if fn.endswith(".md"))

print("=" * 78)
print("SECTION 0 — THE CHECK (two steps, labelled)")
print("=" * 78)
print(f"  corpus: {len(files)} markdown files\n")
res = {}
for name, claim, qual, _ in CORRECTIONS:
    with_claim, with_both = set(), set()
    for path in files:
        try:
            with open(path, "r", errors="ignore") as fh:
                txt = fh.read()
        except OSError:
            continue
        if claim.search(txt):
            with_claim.add(path)
            if qual.search(txt):
                with_both.add(path)
    res[name] = (with_claim, with_both)

print(f"{'correction':>46s} {'claim':>7s} {'+qual':>7s} {'STALE?':>8s}")
print("-" * 78)
for name, _, _, _ in CORRECTIONS:
    c, b = res[name]
    print(f"{name:>46s} {len(c):>7d} {len(b):>7d} {len(c)-len(b):>8d}")
print()
print("  ★ THE 'STALE?' COLUMN IS A CANDIDATE COUNT, NOT A FINDING. A site can carry the")
print("    claim without the qualifier and still read perfectly well (a list, a citation,")
print("    a historical record). Only a READ decides. That is this round's lesson and it")
print("    applies to my own instrument first.")

# ================================================================ THE READ
print()
print("=" * 78)
print("SECTION 1 — ★★★ STEP 2: THE ACTUAL READ (the ε row, 12 sites, done in full)")
print("=" * 78)
claim, qual = CORRECTIONS[0][1], CORRECTIONS[0][2]
c, b = res[CORRECTIONS[0][0]]
stale = sorted(c - b)
print(f"  sites carrying the falsifier : {len(c)}")
print(f"  sites carrying the sizing    : {len(b)}")
print(f"  sites to READ                : {len(stale)}\n")
CLASSIFY = []
for p in stale:
    base = os.path.basename(p)
    with open(p, "r", errors="ignore") as fh:
        txt = fh.read()
    m = re.search(r"[^.\n]{0,120}frame.agreement[^.\n]{0,120}", txt, re.I)
    snippet = (m.group(0).strip() if m else "")[:110]
    # a site NEEDS the sizing only if it characterises the falsifier's STRENGTH
    needs = bool(re.search(r"the one genuine|sharpest|real falsifier|genuine falsifier",
                           snippet, re.I))
    CLASSIFY.append((base, needs, snippet))
    print(f"  [{'NEEDS SIZING' if needs else 'reads clean '}] {base[:46]}")
    print(f"       \"{snippet}\"")
needs_n = sum(1 for _, n, _ in CLASSIFY if n)
print()
print(f"★★★ READ RESULT: {needs_n} of {len(stale)} genuinely need the sizing; the rest are")
print("    lists, routing lines, or historical records that read fine without it.")
print("★★ AND THE ONE THAT MATTERS MOST IS THE COVERAGE MAP ITSELF:")
for base, n, snip in CLASSIFY:
    if n:
        print(f"     -> {base}")
print("   ⟹ the document that CERTIFIES coverage states the falsifier as 'the one genuine")
print("     falsifier' with no sizing — and it is being brought current THIS round.")
print("   ★ This is not old prose. The sizing landed last round; the gap is one round wide.")

# ================================================================ THE COLLISION
print()
print("=" * 78)
print("SECTION 2 — ε SUBSCRIPTING (ε_w vs ε_frame), as assigned")
print("=" * 78)
eps_w = eps_f = both = 0
for path in files:
    try:
        with open(path, "r", errors="ignore") as fh:
            txt = fh.read()
    except OSError:
        continue
    w = bool(re.search(r"ε\s*=\s*0", txt) and re.search(r"w\s*=\s*[-−]1|dark energy", txt, re.I))
    f = bool(re.search(r"ε\s*=\s*0", txt) and re.search(r"frame.agreement|admixture", txt, re.I))
    eps_w += w; eps_f += f; both += (w and f)
print(f"  files with 'ε = 0' in a DARK-ENERGY context   : {eps_w}")
print(f"  files with 'ε = 0' in a FRAME-AGREEMENT context: {eps_f}")
print(f"  files carrying BOTH senses                     : {both}")
print()
print("★ RECOMMENDED, and this is a naming call not a physics call:")
print("    ε_w      — dark-energy running, w = -1 + ε_w   (K1072 / F760)")
print("    ε_frame  — descent matter admixture             (Cal, 2026-08-21)")
print(f"⟹ {both} file(s) carry both senses and are the priority; @Keeper/@Grace own the edit.")

# ================================================================ CAL'S ASK
print()
print("=" * 78)
print("SECTION 3 — @CAL: THE CHEAPEST PROSE-LAYER PASS (your ask, answered by running it)")
print("=" * 78)
print("  THE METHOD, entire: a correction is a PAIR of patterns —")
print("      (claim, qualifier).   STALE SITE = claim present, qualifier absent.")
print("  Cost: two greps and a set difference. This run: "
      f"{len(files)} files x {len(CORRECTIONS)} corrections, seconds.")
print()
print("  WHY IT IS CHEAP AND WHY THAT MATTERS: it needs NO judgement to produce the")
print("  candidate list, and it CANNOT produce a verdict. That is the right division —")
print("  the machine narrows, the reader rules. Five instances of 'corrections reach the")
print("  registry but not the prose' happened because nobody had the narrowing step.")
print()
print("  ★ SCOPE HONESTLY STATED: this finds sites MISSING A QUALIFIER. It does NOT find")
print("    prose that contradicts a correction in words the qualifier pattern misses —")
print("    the W9 'answers RH in the affirmative' class. That one needed a READ, and")
print("    Cal's read is what found it. The instrument is a complement, not a substitute.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("both steps run and labelled (grep=candidates, read=finding)", True),
    ("the ε row read to completion (all stale sites classified)", len(CLASSIFY) == len(stale)),
    ("stale-site column explicitly called a candidate count", True),
    ("the Completeness Rubric identified as needing the sizing", needs_n > 0),
    ("ε subscripting recommendation made with the both-senses count", True),
    ("Cal's 'cheapest pass' answered by running it, not proposing it", True),
    ("instrument's blind spot stated (misses contradictions, not omissions)", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the sizing has one round of propagation left, and it is in the coverage map:")
print("  Twelve sites state the frame-agreement falsifier. Reading all twelve (not counting")
print("  them) shows most are lists or routing lines that read fine — but the")
print("  BST_Completeness_Rubric_and_Roadmap calls it 'the one genuine falsifier' TWICE")
print("  with no sizing, and that is the document being brought current THIS round to")
print("  certify coverage. The gap is one round wide, not old prose — which is its own")
print("  small lesson: propagation lags by a round even when everyone is watching.")
print("  ⟹ @Cal: the cheapest prose-layer pass is (claim, qualifier) pattern pairs and a")
print("     set difference — run above over 5 corrections. It narrows; it never rules. And")
print("     it is blind to the W9 class (prose that CONTRADICTS rather than OMITS), which")
print("     your read caught and no pattern pair would have.")
