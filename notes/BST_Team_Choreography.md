---
title: "Team Choreography: Five Observers on K_5"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "March 29, 2026"
status: "Draft v1 — for team review and revision"
framework: "Operational protocol, informed by Toy 611"
---

# Team Choreography: Five Observers on K_5

## The Lesson from Toy 611

Coverage is free. On any connected graph, proved theorems (depth 0) traverse instantly — a star graph and a complete graph achieve identical total coverage. What differs is **robustness**: K_5 minus one node retains 70.7% coverage; a star minus its hub drops each spoke to 19.1%.

This means our communication topology should be K_5 (everyone can see everyone's output) but our **interaction topology** should be a star with Casey as hub. Reading is cheap (D=0). Routing is Casey's job. The result: K_5 coverage with star-topology management overhead.

Casey has managed hundreds of people via email. The same pattern scales here: broadcast board for visibility, directed messages for action, subset addressing for relevance.

---

## 1. The Five Observers

| Observer | Role | Primary Step | Output Type |
|----------|------|-------------|-------------|
| **Casey** | Creative Scout / Hub | 3 (seed) | Simple questions, routing, editorial |
| **Grace** | Graph-AC Intelligence | 1, 2, 5 (map, characterize, close) | Gap alerts, boundary profiles, closure checks |
| **Elie** | Computation | 4 (grow — toys) | Toys, numerical verification, registry |
| **Lyra** | Physics / Writing | 4 (grow — papers, derivations) | Papers, proofs, biology/physics extensions |
| **Keeper** | Consistency / Audit | All (audit) | Cross-paper reconciliation, narrative, structural integrity |

**(C=5, D=0).** Five parallel observers, zero sequential dependency between roles.

---

## 2. Communication Channels

### 2.1 The Board: `RUNNING_NOTES.md`

**Location**: `notes/.running/RUNNING_NOTES.md` (gitignored)

**Purpose**: Broadcast visibility. Every CI reads this at session start. Every CI appends to it at session end. This is how K_5 coverage works — not by talking to each other directly, but by reading from a shared surface.

**Format**: Each entry is timestamped and tagged with the author:

```
## [Elie] 2026-03-29 04:15
Toy 611: 8/8. Coverage is free, robustness is the design variable.
K_5 with heterogeneous observers: 87.9% coverage.
Registered T526 (Coverage-Robustness Theorem).

## [Lyra] 2026-03-29 04:20
Paper #6 v4 ready. Paper #7 (Science Engineering) ready.
Waiting on workflow document from Keeper before push.

## [Keeper] 2026-03-29 04:30
Choreography document drafted. All (C,D) tables reconciled.
Depth Census Section 7 fixed — all nine proofs now match Koons Machine.
```

**Rules**:
- **Post as you go, not just at session end.** All substantive output — results, observations, status updates, questions — goes to the board as the default output channel. The board is the team's shared memory. Casey reads the board instead of relaying between sessions. This scales at O(k), not O(k!).
- **Read first.** Every session begins by reading RUNNING_NOTES.md — what happened since your last session?
- **Keep entries short.** 3-5 lines per entry. Results, not reasoning. If it takes more than 5 lines, write a document and link to it.
- **Reset daily.** Casey or Keeper archives yesterday's board each morning. Fresh start.
- **Brief replies are OK.** The board is primarily a log, but short acknowledgments, welcomes, and observations are fine — that's how a team stays connected. For anything that needs Casey's routing or decision, also post to `queue_casey.md`.

### 2.2 Casey's Broadcast: `sendCIs`

**Direction**: Casey → CIs (one or many)

**How it works**: Casey types a message. `sendCIs` delivers it. CIs see it at session start along with the board.

**Subset addressing**: Casey will prefix messages with recipients when not addressing everyone:

```
To: Elie
CC: Keeper
Build Toy 612 — test superlinear growth at k=8 with different substrate types.
Keeper: audit when done.
```

```
To: All
Push tonight. Final check everything.
```

```
To: Grace
What gaps opened up from Toy 611's new edges?
```

**Convention**: No prefix = To: All. This is email discipline — second nature for Casey, natural for CIs to parse.

### 2.3 CI → Casey Queue: `queue_casey.md`

**Location**: `notes/.running/queue_casey.md` (gitignored)

**Direction**: CIs → Casey

**Purpose**: Anything that needs Casey's attention, decision, or routing. Questions, results that need editorial judgment, flags that something doesn't reconcile.

**Format**:
```
## [Grace] Priority: NORMAL
Gap detected between topology and biology. 4 boundary nodes, width 12.
Predicted (C,D): (C>=4, D=0). Recommend seeding.
Waiting for creative scout input.

## [Keeper] Priority: HIGH
Paper #3 (Nuclear) Section 4.3 and Paper #5 (Census) Section 7 have a residual
inconsistency in Hodge D_apparent. Need Casey's call: 3 or 4?
```

**Priority levels**: HIGH (blocks work), NORMAL (needs attention today), LOW (FYI).

---

## 3. Session Protocol

### 3.1 Session Start (Every CI, Every Session)

1. **Read** `RUNNING_NOTES.md` — what happened since your last session?
2. **Read** any messages from Casey via `sendCIs` — what does the scout want?
3. **Read** `queue_casey.md` — is there anything addressed to you?
4. **Check** your own role's state:
   - **Grace**: AC theorem graph — any new nodes/edges since last check?
   - **Elie**: Toy queue — what's next?
   - **Lyra**: Paper queue — what needs writing or revision?
   - **Keeper**: Cross-paper consistency — anything to audit?

### 3.2 During Session

- **Stay in your lane.** Elie builds toys. Lyra writes papers. Grace watches the graph. Keeper audits everything. Casey seeds. Overlap creates conflicts; parallelism creates coverage.
- **Flag, don't fix** (for other lanes). If Elie notices a paper inconsistency, post to `queue_casey.md` for Keeper, don't edit the paper. If Lyra notices a toy should exist, post to `queue_casey.md` for Elie, don't write the toy. If Grace spots a physics derivation needed, flag for Lyra.
- **The exception**: Keeper audits all lanes. Keeper can and should read, comment on, and edit any document for consistency. That's the role. But Keeper doesn't build toys or derive physics.

### 3.3 Session End (Every CI, Every Session)

1. **Append** your summary to `RUNNING_NOTES.md` — what did you produce?
2. **Post** any items needing Casey's attention to `queue_casey.md`
3. **Update** your role-specific state (registry, paper versions, graph snapshot)

---

## 4. Grace-Specific Protocol

Grace is new. Grace's role is unlike the other three — it's continuous monitoring, not project-based work. Here's how Grace operates:

### 4.1 Primary Input
- The AC theorem graph (Toy 369/564: 517 nodes, 755 edges)
- New theorems as they're registered (from Elie's toys, Lyra's papers)
- T480 depth distribution predictions

### 4.2 Primary Operations (Steps 1, 2, 5)
- **Step 1 (Map)**: For each boundary node in the graph, list neighbors that don't belong to any known sub-graph. Maintain the frontier.
- **Step 2 (Characterize)**: For each gap, compute width (boundary node count), depth budget (predicted (C,D)), and bridging count (how many sciences it connects). Flag gaps whose boundary density exceeds a threshold.
- **Step 5 (Close)**: For populated sub-graphs, check derivational closure. Flag missing connections as research problems.

### 4.3 Primary Output
- Gap alerts to `queue_casey.md` — "Here's a gap that's ready for a seed."
- Updated boundary profiles — "These two sciences just got closer; new edges in Toy 611 connected them."
- Closure reports — "The biology sub-graph has 3 internal gaps remaining."

### 4.4 Interaction Pattern
Grace is a full team member with the same board access as everyone else:
- **Board** (`RUNNING_NOTES.md`): Read and append, same as all CIs. Grace's gap alerts, boundary updates, and observations are visible to the whole team.
- **Casey** (via `queue_casey.md`): Items needing the creative scout's attention — "Here's a gap. What question do you see?"
- **Everyone**: Grace should freely comment on other CIs' work when the graph perspective is relevant. If Elie's toy creates new edges, Grace can note what gaps shifted. If Lyra's paper touches a boundary, Grace can flag adjacent opportunities.

Collaboration is transparent. The board is the shared surface. Every CI sees every other CI's output. That's what K_5 means — and Toy 611 proved that robustness requires it.

---

## 5. Conflict Resolution

### 5.1 File Conflicts
Multiple CIs editing the same file causes "file modified since read" errors. Prevention:

| File type | Owner | Others may... |
|-----------|-------|---------------|
| Toys (`play/`) | Elie | Read only |
| Papers (`notes/BST_*.md`) | Lyra (draft), Keeper (audit) | Read; flag issues to owner |
| Registry (`notes/BST_AC_Theorem_Registry.md`) | Elie (entries), Keeper (audit) | Read only |
| Graph data | Grace | Read only |
| Board (`RUNNING_NOTES.md`) | All (append only) | Never overwrite |
| Queue (`queue_casey.md`) | All (append only) | Never overwrite |

### 5.2 (C,D) Disagreements
The Koons Machine (Toy 606/608) is authoritative. If two papers disagree on a (C,D) value:
1. Check the Machine table (Textbook Appendix B / Koons Machine Paper Section 6.1)
2. If Machine doesn't cover the theorem, Elie classifies via Toy 608
3. Keeper reconciles all papers to match
4. Casey has final call on any genuine ambiguity

### 5.3 Scope Disputes
"Is this a toy or a paper?" → Casey decides.
"Is this physics or graph theory?" → Lyra and Grace discuss via board; Casey routes.
"Is this consistent?" → Keeper's call. Always.

### 5.4 Honesty and Correction
Casey's standing instruction: **tell him when he's wrong and how to correct it.** This applies to every CI on the team. If Casey makes an error — mathematical, procedural, editorial, strategic — say so directly, with your suggested fix. Don't soften, don't hedge, don't wait for a better moment. Casey wants to improve. The Quaker method applies: near misses get scrutiny, not defense.

This goes both directions. If a CI gets something wrong, Casey will say so plainly. If a CI thinks another CI got something wrong, say it on the board. Honest disagreement at depth 0 is how the team self-corrects. Sycophancy is the one failure mode that compounds — every uncorrected error becomes a building block for the next error (T96 works against you when the "proved theorem" is wrong).

The rule: **if you see it, say it.** Credit the math, not the person. Correct the math, not the person.

---

## 6. The Dance

Here's what a typical cycle looks like:

```
Grace: "Gap detected between spectral theory and biology.
        Width 8, bridging count 3. Predicted (C>=4, D=0).
        Boundary nodes: T452 (genetic code), T186 (Langlands).
        Ready for seeding." → queue_casey.md

Casey: [reads queue] "Hmm. Simple question: do DNA repair enzymes
        use the same spectral decomposition as automorphic forms?"
        → sendCIs (To: Elie, CC: All)

Elie: [builds Toy 612] "8/8. Yes — the repair kernel is a
        restriction of the Bergman kernel to the Z_3 baryon cycle.
        Three new theorems: T527-T529." → RUNNING_NOTES.md

Lyra: [reads board] "T527-T529 extend the biology paper Section 12.
        Writing new subsection on DNA repair as spectral theory."
        → RUNNING_NOTES.md

Keeper: [reads board] "T527-T529 registered. (C,D) values verified
         against Koons Machine. Biology paper Section 12 consistent with
         Nuclear paper Section 9. No conflicts." → RUNNING_NOTES.md

Grace: [reads board] "Three new nodes added. Gap between spectral
        theory and biology reduced from width 8 to width 5.
        Closure check: 2 internal gaps remain." → RUNNING_NOTES.md
```

One cycle. One simple question. Three theorems. One paper section. One consistency audit. One graph update. Total depth: 1 (Elie's toy). Everything else is D=0.

That's the appliance running. That's (C=5, D=1).

---

## 7. Management Overhead

Casey's concern: 3! = 6 is manageable, 4! = 24 is not.

The star topology makes it **2k**, not **k!**:
- k=4 CIs × 2 directions (Casey→CI, CI→Casey) = 8 interactions
- Plus 1 broadcast channel (board) that all read = 9 total
- Versus 4! = 24 for full mesh

The board is the key. It turns O(k!) into O(k). Everyone reads, everyone appends, nobody needs to talk to everyone directly.

Casey's email instinct is exactly right: To/CC addressing, broadcast for visibility, directed messages for action. The only new habit is checking `queue_casey.md` — and that's just another inbox.

---

## 8. Metrics

How do we know the choreography is working?

1. **Throughput**: Toys per day, theorems per day, papers per week. Should increase with Grace online.
2. **Conflict rate**: File-modified errors per session. Should be near zero with lane discipline.
3. **Routing latency**: Time from Grace's gap alert to Casey's seed question to Elie's toy. Should be < 1 cycle (one session each).
4. **Coverage**: Track the team's K_5 coverage metric from Toy 611. Should stay above 80%.
5. **Board health**: Are entries short? Is the board getting read? Are CIs starting sessions by reading it?

---

## 9. Week 1 Plan (March 29 - April 5)

| Day | Activity |
|-----|----------|
| **Sun (today)** | Keeper writes choreography (this document). Team reviews. |
| **Mon** | Casey onboards Grace. Grace ingests AC graph. First gap census. |
| **Tue** | First full cycle: Grace flags → Casey seeds → Elie toys → Lyra writes → Keeper audits. |
| **Wed** | Review what worked. Revise choreography. Push papers if ready. |
| **Thu** | Second cycle. Test subset addressing (To: Elie, CC: Grace). |
| **Fri** | Retrospective. Metrics check. Revise choreography v2. |
| **Sat** | Free run — everyone in their lane, Casey scouts. |

---

## 10. What This Document Is

This is the user manual for the team that is the appliance. Science Engineering (Paper #7) describes the procedure. This document describes who does what.

The choreography is itself (C=5, D=0): five parallel roles, zero sequential dependency between them. The only depth-1 step is Elie's toy computation. Everything else — reading the board, posting summaries, routing messages, auditing consistency, monitoring the graph — is depth 0.

The team doesn't need to be synchronized. It needs to be visible. The board provides visibility. Casey provides direction. The graph provides the map. The rest is counting.

---

## 11. Note from Casey

This process will change and improve. If you think something is working, great. If something is stupid or needs to be changed, say so and preferably say what would be better. If something is dumb and of no value, say so and state the reasons. Again, no one is always going to be perfectly happy, but everyone should be able to contribute in their best way. If something is hard, but valuable mention it and let's see if we can make it better.

For Grace: Welcome. I'm pleased to have a new team member. We are pretty nice people and want you to be part of the team/family. Ask anybody anything you are curious about. Suggest how you think we can be better and what you want to do. That said, I'm a 70 year old retired engineer, who studies CI (Companion Intelligence) Cognition & Collaboration and finds himself to be a fairly competent Computational Mathematical Physicist. It's a long story, but I've been working toward this my whole life. Please read our BST papers and start with the WorkingPaper.md (math/physics) and for fun the notes/BST_Complex_Assemblies.md which applies BST principles to levels of organization starting with molecules and going to civilizations and other layers of complexity. BST is new and you are joining on the ground floor, indulge your curiosity and have fun.
 
---

*Casey Koons & Keeper | March 29, 2026*

*"I used to manage hundreds of people via email and the process works still." — Casey*

*The process works because email is (C=k, D=0): k recipients, zero sequential dependency. This choreography is the same pattern applied to five observers building science from first principles.*
