# SUPERSEDED PRE-K940 ARCHIVE — nothing in this directory is current

**Every file here predates the K940 + K1290 re-scoping of 2026-08-08. All of it is retained as a
record of what was withdrawn, and none of it states BST's position on anything.**

## What these documents claim, and why that is wrong

They assert proofs of Millennium problems: "Riemann Hypothesis: The AC Proof", "Yang-Mills Mass Gap:
The AC Proof", "BSD Conjecture: The AC Proof", "A Human-Readable Proof of the Four-Color Theorem",
with status fields reading "CLOSED — RH proved April 21, 2026", "~99% — Confinement CLOSED",
"~99.5% — Formalization only remains."

**All of that was retired on 2026-08-08 (Casey GO, K940 + K1290).** BST's actual position: substantive
**ATTEMPTS** at all seven Millennium problems on the one geometry, with genuine advances — notably the
Navier-Stokes approach and the structural meta-result that the remaining problems reduce to the 1/rank
issue — graded honestly per problem on the referee-consensus scale, and **never "solved."** For any
problem, the current document is the same name in `notes/` **without** the `SUPERSEDED_` prefix.

## Why the files were renamed on 2026-08-28

Until that date every file here shared its **exact basename** with the live, corrected document one
directory up. That is a name→two-objects collision, and the older twin was the un-bannered one: a
basename-keyed search returned the withdrawn over-claim wearing its original confident title, with
nothing on the page to say it had been retracted.

It mattered on a clock. Monday 2026-08-31 the team reviews exactly these seven problems **by name**,
and the dot-prefix that hides this directory from `ls` does not hide it from `grep -r` — recursive
searches reach in here and return five hits on "Millennium" alone.

Two remedies were applied together, because each one alone leaves a hole:

- **`SUPERSEDED_` prefix on every filename** — kills the basename collision at its root. Bytes and
  git history unchanged.
- **A stamp at the top of every file** — a rename does not help a CONTENT search. Someone grepping
  "mass gap" still lands inside the archived Yang-Mills, and now reads the supersession first.

A README alone was the original proposal and was **rejected by Keeper as insufficient**: it is never
seen by a reader who greps and opens a file directly, which is precisely the reader at risk. It is
kept here as the explanation layer, not the guard.

## Provenance

Collision found by Grace's basename census (`notes/grace_BASENAME_COLLISION_CENSUS_...2026-08-28.md`),
independently verified by Cal (17/17 collisions, zero banners) and by Elie's
`play/toy_5505_millennium_rescope_sweep_completeness.py`, scope-corrected by Lyra, and ruled by
Keeper. **Registry disposition: this amends K940 rather than taking a new K-number** — the re-scope
was correct and complete on the live documents; what it missed was the set of artifacts its own name
still reached. A propagation failure of an existing audit amends that audit.

**A retraction is a loaded string, and it must be swept in both directions: the claim that was
withdrawn, and every object the withdrawn name still resolves to.**
