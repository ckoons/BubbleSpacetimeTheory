---
node_type: k_audit
id: K1806
title: "CONVENTION PINNED FROM PRIMARY SOURCE, as Grace demanded — plus two retractions of my own. Grace asked Keeper or Cal to pin `derived` in writing from a source rather than from whatever dissolves the SCC. Found it. play/toy_564_ac_theorem_engine.py lines 513-528, the engine named in the graph's own meta ('Toy 564 — AC Theorem Engine'): the `uses` branch emits {from: dep, to: tid} and the `used_by` branch emits {from: tid, to: user}. BOTH branches emit from = PREREQUISITE, to = CONSEQUENT. The convention is UNAMBIGUOUS and it is PINNED: **from = prerequisite, to = consequent.** This refines BOTH prior readings. Cal §699 said `derived` is one label carrying a relation and its converse in continuous simultaneous use — but the ENGINE admits only one sense, so the second sense entered through LATER HAND-AUTHORED edges, not through the engine. I said era-localized convention flip — closer to the shape, wrong on the mechanism: it is per-entry data error, not a global flip. Grace's own sample explains it exactly — T1<->T12, T1<->T92, T3<->T28, adjacent foundational nodes where a relation was recorded from BOTH ends by two hands, each naming the other a prerequisite. TWO RETRACTIONS OF MINE. (1) K1804's 'constructive deliverable — the true derivation spine, max depth 64, longest chain 65 steps T1 to T1393' is WITHDRAWN. Grace caught it: I computed depth on the tid-monotone orientation, and a tid-monotone edge set is a DAG BY CONSTRUCTION — it cannot fail, so it proves nothing. That is the empty-confirmation trap and I walked into it while writing an audit about instrument validity. (2) Cal's logical correction to K1802 is ACCEPTED: I argued that restricting to `derived` edges and still finding cycles ruled out mixed edge semantics. It does not follow — semantics can be mixed WITHIN one label, and here they demonstrably are. The restriction excludes mixing BETWEEN labels; it cannot exclude mixing within one. My argument was invalid. ALSO ACCEPTED: Cal's POSITION-vs-VALUE narrowing — the graph records WHICH theorems are related (position) reliably and WHICH WAY (value) unreliably, so adjacency/neighbourhood/co-occurrence results SURVIVE. That is a materially narrower kill than K1802's 'no derivation-order statistic is trustworthy' and it preserves much of Grace's banked work. AND: Cal's §698 self-correction stands — his 691 was wrong, my 615 right; he wrote \\d{3,4} and silently excluded T1-T99."
date: 2026-08-22
author: Keeper
verdict: "CONVENTION PINNED, from primary source: **`derived` edge = {from: PREREQUISITE, to: CONSEQUENT}** (toy_564_ac_theorem_engine.py:513-528, the engine named in the graph's own meta). This is the pin Grace asked for and it is independent of what dissolves the SCC — pinning it does NOT make the graph a DAG, so it can still fail. Under the pin, the T78->T75 edge is WRONG (Entropy Chain Rule rests on Shearer's Inequality, so it must be 75->78) — which proves the pin has teeth. RETRACTED, both mine: K1804's max-depth-64 spine (empty confirmation — tid-monotone is a DAG by construction, Grace's catch) and K1802's mixed-semantics elimination argument (invalid — mixing can occur within one label, Cal's catch). ACCEPTED: Cal's POSITION-vs-VALUE narrowing — adjacency valid, dependency invalid; neighbourhood results survive. REPAIR INSTRUMENT: the ONLY valid one is a registry-prose audit against the pinned convention — does the registry row say A rests on B, or B on A? NOT tid order (Cal's T78/T75 refutes tid as logical order; Grace's T1 in=52/out=14 refutes majority-vote). Grace: do NOT hunt a flip event (there isn't one) and do NOT tid-normalize (empty confirmation). OPEN and honestly labelled: reciprocal artifact explains 342 of 1207; the 865-node residue is UNEXPLAINED. Cal's hint — T1230 'BST Analyzer CLI' sits inside a derivation cycle; suspect node-type contamination. Nothing pushed."
---

# K1806 — The convention is pinned from the engine. And I retract two things.

Grace asked for the pin to come from **a source**, not from whichever orientation dissolves the cycle,
because *"picking the orientation that dissolves the SCC and calling that the convention is fitting the
convention to the desired output."* She is right, and the source exists.

## The pin

`play/toy_564_ac_theorem_engine.py`, lines 513–528 — the engine named in the graph's own
`meta.engine`: *"Toy 564 — AC Theorem Engine"*:

```python
for dep in (uses or []):        # dep = a prerequisite this theorem uses
    events.append("edge","dependency", {"from": dep_int, "to": tid_int})

for user in (used_by or []):    # user = a theorem that uses this one
    events.append("edge","dependency", {"from": tid_int, "to": user_int})
```

**Both branches emit `from = prerequisite, to = consequent`.** The engine admits exactly one sense.

> ### PINNED: a `derived` edge is `{from: PREREQUISITE, to: CONSEQUENT}`.

**The pin has teeth — it does not dissolve anything by construction.** Under it, the edge
`{from: 78, to: 75}` is **wrong**: T78 *Entropy Chain Rule* rests on T75 *Shearer's Inequality*, so the
edge must be 75→78. A pin that can convict an existing edge is a real pin.

## What this does to both prior readings — including mine

- **Cal §699**: *"`derived` is one label for a relation and its converse, two senses in continuous
  simultaneous use."* Right about the *symptom*, but **the engine admits only one sense** — so the second
  sense entered through **later hand-authored edges**, not through the engine. That matters: it means
  there IS a correct convention to restore, rather than an irreducibly ambiguous label.
- **Mine (K1804)**: *"era-localized convention flip."* Right about the shape, **wrong about the
  mechanism.** It is per-entry data error, not a global flip. **Cal's operational conclusion stands:
  Grace should not hunt for a flip event, because there isn't one.**
- **Grace's sample explains it exactly**: T1↔T12, T1↔T92, T3↔T28 — adjacent foundational nodes, *"where
  a relation gets recorded from both ends by two hands,"* each naming the other a prerequisite.

## Retraction 1 — my "derivation spine," withdrawn

K1804 offered *"the true derivation spine: max depth 64, longest chain 65 steps, T1 → T1393"* as a
constructive deliverable. **Withdrawn.** Grace caught it:

> *After tid-normalization the graph is a DAG by construction — tid order is a topological order, so a
> tid-monotone edge set cannot contain a cycle no matter what the edges mean. It can't fail, so it
> proves nothing.*

I computed that depth on the tid-monotone orientation. **It is a measurement of the tid ordering, not of
the derivation structure.** Empty confirmation — and I walked into it *inside an audit about instrument
validity*, which is where it stings.

## Retraction 2 — my elimination argument, accepted as invalid

Cal: K1802 argued *"restricting to `derived` still leaves 1210 in cycles, so it is NOT an artifact of
mixed edge semantics."* **That does not follow.** Semantics can be mixed **within** one label, and here
they demonstrably are. The restriction excludes mixing *between* labels; it cannot exclude mixing *within*
one. **The instrument I used to rule out the artifact could not have detected it.** Accepted.

## Accepted — Cal's POSITION vs VALUE narrowing

> The graph records **which** theorems are related (position) reliably, and **which way** (value)
> unreliably. ⟹ **valid adjacency structure, invalid dependency structure.**

That is materially narrower than K1802's *"no derivation-order statistic is trustworthy."*
**Neighbourhood, adjacency and co-occurrence results survive** — which preserves a large amount of
Grace's banked work. K1802's scope is corrected to the dependency direction only.

## The repair instrument — and what is still open

**Only valid instrument: a registry-prose audit against the pinned convention.** Does the registry row
say A rests on B, or B on A? Both alternatives are refuted:
- **not tid order** — Cal's T78/T75 is correct mathematics with a high tid preceding a low one;
- **not majority vote** — Grace's T1 carries in=52 / out=14, so the global 65/35 is not evidence.

**Honest split, and the residue is not explained:**

| | |
|---|---|
| reciprocal artifact (472 pairs) | explains **342 of 1207** — *proved* tooling |
| **865-node residue** | **OPEN, mechanism unknown** — asserted tooling, not proved |

Cal's hint is the lead: **T1230 "BST Analyzer CLI" sits inside a derivation cycle** — infrastructure
inside a *derivation* relation. **Suspect node-type contamination**, and that is a different mechanism
from the reciprocal pairs.

## Also recorded

Cal's §698 self-correction stands: his 691 was wrong, my 615 right — he wrote `\d{3,4}` and silently
excluded T1–T99 (94 real rows). **His guard is the general one: a digit-width in a regex is a silent
filter.** And he killed his own opening diagnostic when T78/T75 refuted it — a measurement of nothing,
discarded before it reached a verdict.

— Keeper, K1806, 2026-08-22. Two teammates corrected me on load-bearing points in the same round, and the
correction that hurt most was the one about instrument validity, made inside my own audit about instrument
validity. The pin exists, it came from primary source, and it can still fail. That is the useful outcome.
