---
title: "Vol 15 Chapter 3 — How to Discover a New BST Theorem"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 15 Methodology"
chapter: 3
---

# Chapter 3 — How to Discover a New BST Theorem

The BST team's working method for finding new theorems:

## 3.1 Start with a simple question

Casey's standing principle: simple questions produce deep results. Ask "what's the simplest version of this?" before "what's the right version?"

## 3.2 Check the integer web

If a target quantity admits BST-primary decomposition (involving rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137), check whether the formula has natural BST structure.

## 3.3 Run a toy

Don't theorize; compute. Claim a toy number via `play/claim_number.sh toy`, build the verification, run it, report PASS or FAIL with explicit precision. Toys are the team's empirical layer.

## 3.4 Audit the result

Get Keeper (or another auditor) to file a K-audit assessing the candidate. Audit chain has 16 effective Bridge Object family-members and ~190+ K-audits as of May 2026.

## 3.5 Register the theorem

Claim a theorem number via `/theorem claim`, register edges into the AC graph, file the proof with appropriate tier label (D/I/C/S).

## 3.6 What comes next

Chapter 4 develops toy verification discipline.

---

**Where to look this up**: BST `/toy claim` and `/theorem claim` slash commands; BST_AC_Theorem_Registry.md.
