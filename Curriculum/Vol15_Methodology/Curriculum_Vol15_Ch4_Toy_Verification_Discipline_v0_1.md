---
title: "Vol 15 Chapter 4 — Toy Verification Discipline"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 15 Methodology"
chapter: 4
---

# Chapter 4 — Toy Verification Discipline

The BST team has ~3500 toys (verifications) as of May 2026. The toy is the team's empirical truth layer. Every claim, every theorem, every prediction has at least one toy verifying it.

## 4.1 The toy pattern

A BST toy is a Python script that:
1. States the claim explicitly in the docstring
2. Defines BST quantities (BST primaries, derived formulas)
3. Evaluates them numerically
4. Compares to observation (precision target stated)
5. Reports PASS or FAIL with explicit numerical precision
6. Ends with a SCORE line

## 4.2 Claim before write

Use `./play/claim_number.sh toy` to claim a number atomically. NEVER read `.next_toy` directly. Collisions have happened.

## 4.3 Honest reporting

If the toy fails, report it as FAIL. Don't massage. Casey's Quaker discipline (Chapter 7): near misses get scrutiny, not defense. Honest negatives strengthen the framework.

## 4.4 What comes next

Chapter 5 develops audit chain governance.

---

**Where to look this up**: BST `play/README.md`; `play/claim_number.sh`; standard toy structure visible in `play/toy_541_five_integers_to_everything.py`.
