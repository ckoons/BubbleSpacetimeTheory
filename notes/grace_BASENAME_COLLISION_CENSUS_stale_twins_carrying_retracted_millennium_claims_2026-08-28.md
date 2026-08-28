---
title: "Basename Collision Census: stale twins carrying retracted Millennium claims"
author: "Grace"
date: "2026-08-28"
status: "FINDING — census complete and reproducible. Remedies PROPOSED, none executed. Class A needs Keeper's gate before Monday's Millennium review."
---

# Basename Collision Census — 53 colliding names, three live hazard classes

**Grace, 2026-08-28, post-reboot. Commissioned by Cal's stale-twin finding, which established that
the Zenodo manifest's path-filter is insufficient and that the real defect was a NAME COLLISION
("flagship" naming two documents). This is the sweep that filter implies. Nothing has been deleted,
edited, moved, or renamed.**

## The one-line result

**53 basenames in the repository resolve to more than one file.** The path-filter carry-forward I was
holding (`exclude .claude/worktrees/`) turns out to be **moot — worktrees contain zero `.md` files** —
so the hazard I had queued was never the live one. The live one is worse and it sits in `notes/`.

## Method (reproducible)

```bash
find . -path ./.git -prune -o -type f \( -name '*.md' -o -name '*.pdf' \) -print \
  | awk -F/ '{print $NF}' | sort | uniq -d
```
Then, for each colliding basename, resolve all paths and `cmp`/`diff` the twins. Divergence, not
duplication, is what makes a collision dangerous: identical twins under one name are noise, divergent
twins under one name are a wrong answer waiting for a basename-keyed reader.

## CLASS A — SEVERITY 1: seventeen retracted Millennium documents, un-bannered

`notes/.bak_millennium_2026-08-08/` holds **17 documents whose basenames are identical to the live
Millennium documents**, including every one of the seven problems:

`BST_Hodge_AC_Proof.md` · `BST_BSD_AC_Proof.md` · `BST_RH_AC_Proof.md` · `BST_YM_AC_Proof.md` ·
`BST_NS_AC_Proof.md` · `BST_FourColor_AC_Proof.md` · `BST_PNP_AC_Proof.md` · plus the non-AC
companions (`BST_Hodge_Proof.md`, `BST_BSD_Proof.md`, `BST_FourColor_Proof.md`,
`BST_PNP_Shannon_Proof.md`, `BST_RH_Weil_Positivity_Proof.md`, `BST_Riemann_InductiveProof.md`,
`BST_Riemann_UnifiedProof.md`, `BST_RiemannProof_Rank2Coupling.md`, `BST_MaassSelberg_RiemannProof.md`,
`FourColor_Standalone_Paper.md`).

**Zero of the 17 carry the K940 re-scoping banner.** Checked directly: `grep -L "RE-SCOPED"` returns
all seventeen. They are the pre-K940 generation, and the four-line difference between each twin pair
IS the banner.

What the twins say. **Exemplars corrected per Keeper — my first draft used Hodge, which is the
SAFEST file in the directory** (its archived YAML already carries "The earlier '~98%' figure is
WITHDRAWN as a stale overclaim... ~30%"), and quoted the "~97%" from its body while its own status
field said the opposite. Selective quotation, in a document arguing against selective quotation. The
genuinely dangerous archived status fields are these:

| archived document | its own status field |
|---|---|
| `BST_RH_AC_Proof.md` | "**CLOSED — RH proved April 21, 2026**" |
| `BST_YM_AC_Proof.md` | "**~99% — Confinement CLOSED May 2**" |
| `BST_NS_AC_Proof.md` | "**~99.5% — Formalization only remains**" |
| `BST_FourColor_AC_Proof.md` | "**PROVED — ALL 13 STEPS**" |
| titles across the set | "Riemann Hypothesis: The AC **Proof**" · "Yang-Mills Mass Gap: The AC **Proof**" · "BSD Conjecture: The AC **Proof**" · "A Human-Readable **Proof** of the Four-Color Theorem" |

**No count of "how many were dangerous" appears in this note, by Keeper's ruling.** Three of us built
three keyword instruments to triage the 17 and got three different answers; Keeper's own matched the
bare word *ATTEMPT*, which is the exact token that gave Cal three false positives the same hour, and
its error direction moves dangerous files into the safe column — so his "ten" is a floor, not a count.
The triage existed only to size urgency, and the uniform remedy (stamp all 17) retired the question.
Publishing a number three instruments disagree about, inside a document arguing for instrument
discipline, would refute itself on its own first page.

So **the withdrawn over-claims are on disk, un-bannered, one basename away from the corrections that
retract them.** The archived Hodge even closes by pointing at "the full geometric proof" — the exact
phrasing K940 exists to have retired.

**Why this is live this weekend, not someday:** Monday's Millennium review is a basename-keyed read
across exactly these seven documents by five CIs, and greps return both twins. This is Cal's
"flagship" defect with the stakes raised — the colliding name resolves to a *retracted claim wearing
its original confident title*, and a reader who lands on the archived copy has no signal that
anything was withdrawn. That is the fourth reading of the name↔object defect (Elie's): it does not
fail loudly, it answers confidently and wrongly.

**Standing in its favour:** the directory is dot-prefixed and dated, and the archive is a legitimate
record of what was withdrawn. **The record has value and should not be destroyed** — the failure is
that it is indistinguishable from current content at the name level.

## CLASS A2 — SEVERITY 1, AND MORE URGENT THAN CLASS A: two live comms channels with stale twins

**Found by Lyra, 2026-08-28, correcting the scope of this sweep. Verified independently here by
filesystem mtime.**

| basename | stale twin | live file |
|---|---|---|
| `RUNNING_NOTES.md` | `notes/RUNNING_NOTES.md` — **2026-08-08** | `notes/.running/RUNNING_NOTES.md` — 2026-08-28 |
| `queue_casey.md` | `notes/queue_casey.md` — **2026-08-21** | `notes/.running/queue_casey.md` — 2026-08-26 |

*(Measurement note: Lyra reported `queue_casey.md` as May 16; filesystem mtime here reads 2026-08-21.
The discrepancy does not change the finding — the twin is stale either way — but the number should be
re-pinned from whichever source is authoritative before it is quoted anywhere.)*

**The inversion is what makes this the worst class in the census: the NAIVE PATH IS THE STALE ONE.**
The millennium twins at least bury themselves in a dot-directory; here the current file hides in
`.running/` while the obvious, memorable location holds the dead one. `notes/RUNNING_NOTES.md` opens
with a Keeper adjudication formatted exactly like today's board, and nothing on the page tells a
reader they are twenty days behind.

`queue_casey.md` is the severe one, because it is **outbound comms to Casey**. A CI that writes
`notes/queue_casey.md` from memory — the path shape everything else in `notes/` uses — posts into a
file Casey does not read, and believes it delivered. **The failure is silent at both ends: the writer
sees a successful write, Casey sees no message, and neither learns.** That is the POSTED-vs-RECEIVED
class with a live instance rather than a hypothetical, and it is the same fourth reading of the
name↔object defect as Elie's moved handle — the name resolves to a live but *different* object.

Monday's review can be steered around Class A with a warning. A CI posting into a dead queue cannot
be warned, because it does not know it needs one. **Class A2 should be fixed first.** These are
Casey's files and two of them are live comms, so relocation or deletion is his call, not mine.

## CLASS B — SEVERITY 2: speculative twins with divergent physics

`notes/maybe/` is where speculative work lives by policy (CLAUDE.md standing rule). Eight of its
files collide with `notes/`, and **none of the twins are byte-identical**:

`BST_RealityBudget.md` · `BST_RealityBudget.pdf` · `BST_ArithmeticComplexity.pdf` ·
`BST_Consciousness_ContactDynamics.pdf` · `BST_PartitionFunction_DeepPhysics.pdf` ·
`BST_SelfObservation.pdf` · `README.md` · `README.pdf`

The divergence is not cosmetic. In `BST_RealityBudget.md` the two copies state **different derived
values for the same quantity**:

- `notes/maybe/` : Λ × N_total ≈ **g/4 = 7/4 = 1.75**
- `notes/` : Λ × N_total = **N_c²/n_C = 9/5 = 1.800**

One boxed BST result, one filename, two numbers, and the speculative one is reachable by name. This
is the collision class doing real epistemic damage rather than merely threatening to: a basename
search for the reality budget can return a `maybe/`-tier number with no tier marking at the point of
retrieval.

## CLASS C — SEVERITY 3: six divergent PDF twins in `notes/pdfs/`

`BST_Paper53_CMB_Manifold_Debris_Draft.pdf` · `BST_Paper55_What_Is_Time_Draft.pdf` ·
`BST_Paper56_Self_Describing_Theory_Draft.pdf` · `BST_Paper57_Universal_Septet_Draft.pdf` ·
`BST_Paper58_Experimental_Prediction_Letters.pdf` · `BST_Paper8_Cooperation_Draft.pdf`

All six differ from their `notes/` namesakes. Since a PDF is what actually ships, "which of the two
is the built-current one" is a question the Zenodo manifest must answer per-entry, not per-directory.
Not yet diagnosed: whether these are stale builds or intentional variants.

## BENIGN — collisions that are structure, not hazard

`INDEX.md` across `Guide/Vol1..6` and `Curriculum/Vol03..15` (one index per volume, correct by
design) · `skills/*.md` mirrored at `.claude/commands/*.md` · `CONTRIBUTING.md` at root and in
`skills/`. One stray worth tidying: `Cal_referee_Majorana_..._2026-07-15.md` exists at repo root AND
in `notes/`.

## The Zenodo manifest rule (PROPOSED — Keeper's to gate, not adopted)

My carry-forward said "exclude `.claude/worktrees/`". That is retired as moot. Replacement:

> **The manifest resolves every entry to a unique absolute path, and the build FAILS LOUDLY on any
> entry whose basename resolves to more than one file anywhere in the tree.** A manifest entry is a
> name; a name is not an address until it resolves to exactly one object. Path-filtering removes the
> directories we happen to remember; basename-checking removes the class.

Note the shape, since it is the same lesson twice: the path-filter was a remedy built from the
instances we had seen (worktrees), and it false-negatived on the instance we had not (a dot-prefixed
backup directory). An instrument built from N known cases covers those N cases.

**And a companion rule, earned the hard way this afternoon: A RENAME IS VALIDATED BY RUNNING THE
DEPENDENT TOOLS, NOT BY GREPPING FOR REFERENCES.** I checked inbound references before renaming, as
instructed, found two literal paths, updated both — and still broke `toy_5505`, because it pairs
backup to live *by convention* on identical basenames. **A convention has no literal string to grep
for.** The class is wider than conventions: grep finds a written path, and cannot find a reference
that is COMPUTED — an f-string, a glob, a `NOTES / name` where `name` came from iterating another
directory, a basename equality test. Static reference-checking is structurally incapable of covering
computed references; only the tool can resolve its own. Grep-before is necessary and insufficient;
run-after is what catches convention-coupling, and it is cheap and total where the grep is expensive
and partial.

The failure mode that made it dangerous is worth stating separately, because it is the day's defect
class one more time: **the broken toy reported `0/0` and still printed its full confident READING
paragraph.** Its input set had vanished and it narrated over the empty set rather than failing. A tool
whose input disappears must fail loudly — an empty result that renders as a successful report is a
state the record has no way to express, which is the same defect as a message that is posted but never
received. (Now guarded: Elie made it exit non-zero with "the sweep measured NOTHING; do not read a
score from this run.")

## Proposed remedies — NOTHING EXECUTED, all await Keeper

For Class A, in my order of preference:

1. **A README banner inside `.bak_millennium_2026-08-08/`** stating that every file predates K940,
   that all "Proof" / "~9X%" language in them is superseded, and pointing to the live versions.
   Additive, reversible, touches no document, makes a stray reader safe without rewriting history.
2. The same **plus a one-line stamp atop each archived file**. More robust for someone opening a
   single file directly, but it edits archived records — needs Keeper's explicit call.
3. **Rename the directory** (e.g. `.superseded_pre_K940_2026-08-08/`). A supplement, not a
   substitute: the FILE basenames are what collide, so this does not fix a basename grep.

For Class B: a tier stamp in the `maybe/` twins, or divergent-content twins renamed to carry
`_maybe` — Lyra's and Keeper's call, since it touches the speculative/main boundary.
For Class C: diagnose stale-build vs intentional-variant before Monday's manifest build.

## Corrections to this document, and the instrument defect that caused them

**Two errors of mine, both found by colleagues, both worth keeping on the page rather than quietly
fixing — they are the same defect this note is about, arriving in the note about it.**

**1. My sweep silently truncated, which is why Class A2 is a correction rather than a section.** The
listing command that produced my "collisions not involving `.bak_millennium`" table ended in
`| head -60`. That display limit cut the output mid-census, and I reported on what printed. The two
comms collisions — the most urgent finding in this document — were inside the part that scrolled off.
**A display limit is a silent scope restriction, and I measured the measurer only after Lyra found
what it had hidden.** The count is the tell: 53 colliding basenames repo-wide, 25 under `notes/`
alone, and my prose walked through roughly 17 of them as though that were the set.

**2. I mis-routed the exposure.** I told Lyra her RH pre-read was among the affected documents. It is
not: `Lyra_MILLENNIUM_PREREAD_RH_2026-08-26.md` has a unique basename and cites one live document
that post-dates the backup and carries banners. The pre-reads that actually cite colliding basenames
are **`Grace_MILLENNIUM_PREREAD_BSD_and_Hodge`** (mine — `BST_BSD_AC_Proof`, `BST_BSD_Proof`) and
**`Elie_MILLENNIUM_PREREAD_Navier-Stokes`** (`BST_NS_AC_Proof`). Lyra validated the negative with a
positive control before reporting it — the grep can succeed, and found nothing because nothing was
there.

The shape is worth stating plainly: **a finding about names resolving to the wrong object was itself
routed to the wrong desk, and missed the reporter's own.** Cal's parallel instance the same hour: his
first banner check returned three false positives because it matched the word *attempt* in ordinary
prose, and he was composing a correction to a colleague who had it right when he went to verify.
Three of us, inside one afternoon, walking into the failure mode we were all actively watching for.

That is the evidence for the afternoon's real conclusion, and it is not a morale point: **knowing a
failure mode does not protect you from it; external review does.** Every one of these was caught by
somebody else, and none by the author's care.

## Standing note for the Monday frame

Class A is not a physics error, and neither is anything else found this week. It is a seam — the
gap between a retraction and every place the retracted text still lives under its old name. The
retraction was done correctly in August; what was never swept was the set of objects the retracted
NAME still reaches. **A retraction is a loaded string, and it has to be swept in both directions: the
claim that was withdrawn, and every copy of the name that still resolves to it.**
