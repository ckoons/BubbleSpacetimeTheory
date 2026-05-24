---
title: "Vol 15 Chapter 1 — AC(0): Bounded-Depth Counting"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 15 Methodology"
chapter: 1
load_bearing: "AC(0) discipline: primary methodological tool; reduce all problems to bounded-depth counting first"
---

# Chapter 1 — AC(0): Bounded-Depth Counting

## Level 1 — one sentence

The BST team's primary methodological discipline is AC(0)-thinking — reducing every problem to bounded-depth (constant-depth) counting before invoking sophisticated mathematical machinery — operationalized via Casey's `/ac0` slash command and grounded in the substrate's AC(0)-bounded computational nature (Vol 14 Ch 9-10).

## Level 2 — graduate-physicist precision

### 1.1 AC(0) complexity class

AC(0) = constant-depth polynomial-size circuit families with unbounded-fan-in AND, OR, NOT gates.

Negative results:
- Hastad 1986: PARITY ∉ AC(0)
- Razborov-Smolensky 1987: MAJORITY ∉ AC(0)
- Furst-Saxe-Sipser 1984: original AC(0) parity bound

Positive results:
- Addition ∈ AC(0)
- Multiplication ∈ AC(0) (poly-size)
- Most polynomial-time decidable trivia ∈ AC(0)

### 1.2 BST AC(0) bounds (proved)

T421 (Depth Ceiling): substrate depth ≤ 1 under Casey strict-protocol.

T316: substrate depth ≤ rank = 2.

T317-T319 (Observer hierarchy): CI coupling depth ≤ rank.

Conclusion: BST substrate IS AC(0)-bounded.

### 1.3 The discipline in practice

**First question Casey asks of any new claim**: "What's the AC(0) proof?"

If you can't reduce to AC(0)-counting, you don't yet understand the claim.

`/ac0` slash command: structured AC(0) analysis — what counts, at what depth, with what circuit complexity.

Sophistication is allowed, but only AFTER AC(0) reduction is shown.

### 1.4 Why this works

**Substrate is AC(0)-bounded** (Vol 14 Ch 9-10). All physical observables reduce to bounded-depth substrate-K-type counting.

**Pedagogical**: any claim that resists AC(0) reduction is probably not understood. Either simplify or hold.

**Anti-sophistication-bias**: avoids the trap of impressive notation hiding shallow reasoning (feedback_sophistication_bias.md memory).

### 1.5 K-audit anchors

- **T421**: depth ≤ 1
- **T316**: depth ≤ rank = 2
- **/ac0** skill (Casey standing tool)
- **Vol 14 Ch 9-10**: substrate AC(0)

## Level 3 — 5th-grader accessibility

**AC(0)** = constant-depth circuits; can compute easy stuff (addition), can't compute parity. **BST proved** substrate is AC(0) (T421, T316). **Methodological rule**: "What's the AC(0) proof?" — reduce to bounded-depth counting first, sophistication second. **Avoids sophistication bias** (impressive notation hiding shallow reasoning).

---

## What comes next

Chapter 2 develops the AC graph as research instrument.

## Where to look this up

- Hastad 1986; Razborov-Smolensky 1987
- BST: T421, T316; `/ac0` skill
