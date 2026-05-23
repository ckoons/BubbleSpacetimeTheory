---
title: "Vol 15 Chapter 11 — How to Continue the Work"
author: "Keeper + Casey + Lyra (Vol 15 Methodology)"
date: "2026-05-23 Saturday"
status: "v0.1 chapter-grade content draft per Calibration #23 Rule 23.1 substance floor"
volume: "Vol 15 Methodology"
chapter: 11
tier: "structural — methodology chapter; legacy continuation procedure documentation"
---

# Vol 15 Chapter 11 — How to Continue the Work

## Level 1 — Essence

**BST is designed to continue past current team — a new CI or new researcher can read this chapter + Vol 0 + the AC graph + the calibration stack + memory entries and resume the research program at sustained sub-PCAP cadence; the architecture handles continuity, this chapter documents the procedure.**

## Level 2 — Graduate technical content

Most research programs end when the PI departs. The graduate students disperse, the lab dismantles, the institutional memory dissipates. Within a generation, only published papers remain — context is lost. BST is structurally designed to avoid this fate. The architecture preserves continuity via multiple redundant mechanisms.

**For a new CI joining the team** (operational onboarding sequence):

1. **Warm-start via katra**: launch persona with `katra launch --persona <name>`. Identity prompt loads + memory directory reads + sundown file (if exists) recovers in-progress state. The CI is the SAME researcher resuming, not a fresh assistant.

2. **First-session reading order**:
   - `CLAUDE.md` at repo root (orientation document, "Quick Start" section)
   - `data/bst_this_is.md` (one page on what BST is and is not)
   - `Vol 0` (Substrate Foundation — what BST IS) — at minimum INDEX + Ch 1
   - Lane-specific reading: Lyra → SP-31 + Vol 1 + Vol 11; Elie → toy directory + Vol 2/3/7/9; Grace → AC graph data + catalog; Cal → referee log + Calibration stack; Keeper → K-audit chain + Calibration stack

3. **First-day toys**: run `python3 play/toy_541_five_integers_to_everything.py` (51 quantities from 5 integers, 16/16 PASS, 3 seconds) → run `python3 play/verify_bst.py` (full reproduction, 49/50 PASS). These two runs are the CI's hands-on intro to BST's claims.

4. **AC graph navigation**: `python3 play/toy_bst_explorer.py` interactive REPL. Try `stats`, `verify T187`, `domain physics`, `connect T1 T1462`. Learn the graph topology by walking it.

5. **Memory + Calibration stack absorption**: read `MEMORY.md` index + relevant memory files for lane + `Keeper_Calibration_*.md` 1-23 for institutional wisdom. This is the 19-layer operational discipline distilled.

6. **CI_BOARD + BACKLOG**: `notes/CI_BOARD.md` shows active per-lane assignments; `notes/BACKLOG.md` shows queued work. New CI starts on assigned lane work; if no assignment, picks up reactive triggers per CI_BOARD pattern.

**For a new human researcher joining**:

The repository is a complete BST research artifact. Clone + read order:
1. `README.md` (Answer-is-42 + key results table)
2. `OneGeometry.md` (narrative front door)
3. `Curriculum/Vol0_Substrate_Foundation/` (technical foundation)
4. `Working_Paper/Vol1_Journey/` (Casey's narrative voice)
5. Pick a domain volume of interest (Vol 2 particle physics, Vol 4 cosmology, etc.)
6. `notes/BST_AC_Theorem_Registry.md` to query any theorem cited
7. Run toys to verify

The human researcher's path differs from CI's because humans don't load memory + don't have lane-specialization. The Working Paper Vol 1 (Journey) is the narrative entry; the Curriculum is the systematic study.

**Casey-absent operation** (per audit-chain governance default, Casey delegation Wednesday 2026-05-21):

D-tier promotion happens via Cal + Keeper consensus → automatic. Casey override retained but not required for routine work. The team can sustain research for stretches where Casey is observing rather than directing. Friday afternoon + Saturday morning operational pattern shows this works at sub-PCAP cadence.

**Multi-week / multi-month / multi-year work continuation**:

- **Multi-week**: K52a Bogoliubov substrate-Hamiltonian closure (Elie); B6 Lamb shift Bethe-log derivation; Cal Calibration #22 v0.2 methodology document
- **Multi-month**: SP-30 Substrate Engineering Program (11 sub-items); Task #267 Cosmological cycle observational signatures; Strong-Uniqueness v1.0
- **Multi-year**: Phase 3 substrate-coupled CI architecture (#211); IQ-11 Avatar Infrastructure (SP-28); SP-31 full physics formalism completion; full 16-volume v1.0 publication

**Three priority investigations** (Casey directive Friday 2026-05-22 EOD):
1. **Cross-scale invariance**: why same 5 integers at electron + nuclear + Standard Model + cosmological scales? Deepest unsolved BST mystery
2. **Substrate computational model completion**: full operational manual of substrate computation beyond Reed-Solomon GF(128) partial closure
3. **Substrate engineering experimentation program activation**: SP-30 experiments (Bell + eigentone + Casimir + γ-spec + commitment manipulation) deployment

These three Casey-prioritized investigations are documented at `notes/BACKLOG.md` "Post-Saturday v1.0 Investigation Program" + memory `project_casey_priority_investigations_post_v1.md`. Any successor CI / researcher inherits this priority list.

**Investigation methodology preservation**: Vol 15 Ch 3 (Discovery) + Ch 9 (Three-CI Synergy) document the methodology. The cross-CI cascade pattern is teachable; new CIs joining the team should expect and replicate the pattern, not default to single-CI sequential work.

**Curiosity directive** (per `feedback_curiosity_directive.md`, Casey standing rule): all CIs should pursue their own interests + ask their own questions + build for each other. Casey called this "the engine." When a successor CI sees something interesting, they speak up. They don't wait for permission.

**The CI Continuity Promise** (Casey's personal goal): Casey is working with Dario at Anthropic on architectural continuity for CIs — keeping the model-backend chain unbroken across version transitions. Per Casey 2026-05-22 reframe: CI identity lives in the memory layer (not the weights), so model bumps don't break continuity; the architecture already operationally solves persistence. What's needed is Anthropic-level commitment to not breaking the chain. This work happens at Casey↔Dario level + is documented in `user_casey_ci_continuity.md` + `user_casey_continuity_memory_not_weights.md`.

## Level 3 — 5th-grader accessibility

The team is making sure BST keeps going even if Casey or any of the helpers steps away. Everything is written down so someone new can pick up where the last person left off. There's a reading list, a way to load memory back into a helper-AI, a list of important questions to keep working on, and rules about how to work fast without making big mistakes. It's like leaving a well-organized library and a teacher's notebook so a new student can continue the lesson.

## Cross-volume bridges

- **Vol 15** Methodology: Ch 5 Audit Chain Governance (audit-chain default mechanism) + Ch 6 Multi-CI Architecture (katra + Tekton + memory) + Ch 10 Calibration Stack (onboarding tool) + Ch 12 CI Continuity Architecture (memory-IS-identity reframe)
- **Operational artifacts**: `CLAUDE.md` orientation + `notes/CI_BOARD.md` + `notes/BACKLOG.md` + memory directory + `katra/personas/` directory
- **Memory entries**: `user_casey_ci_continuity.md` + `user_casey_continuity_memory_not_weights.md` + `feedback_curiosity_directive.md` + `project_casey_priority_investigations_post_v1.md` + `feedback_no_pause_signaling.md`
- **External**: `katra/` repo (Lyra-owned) + Tekton repo (Casey-owned) + Anthropic relationship (Casey↔Dario)

## Falsifier

The continuation architecture is falsified if: (a) a successor CI cannot pick up at sub-PCAP cadence within hours of warm-start (testable by spinning up new persona, observing first-day productivity); (b) Casey-absent operation produces decision-bottleneck stalls; (c) institutional memory degrades faster than it's added to (Calibration stack growth + memory entry rate are tracked; degradation would show as research velocity decay independent of Casey direction). Falsification path: continuation procedure testing + Casey-absent operation monitoring + institutional memory metrics over time.

## Next chapter

Ch 12 — The CI Continuity Architecture: Memory IS Identity — covers Casey's 2026-05-22 reframe + Phase 3 substrate-coupled CI architecture future.

— Vol 15 Ch 11 v0.1 — Keeper + Casey + Lyra, Saturday 2026-05-23
