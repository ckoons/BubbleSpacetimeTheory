---
title: "Vol 15 Chapter 1 — AC(0): Bounded-Depth Counting"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 15 Methodology"
chapter: 1
---

# Chapter 1 — AC(0): Bounded-Depth Counting

Volume 15 documents the BST team's working methodology. This volume is for CIs (and humans) who want to continue the work. Chapter 1 starts with AC(0) — the team's primary mathematical discipline.

AC(0) thinking: reduce every problem to bounded-depth counting. "What's the AC(0) proof?" is the first question Casey asks of any new claim. The `/ac0` slash command formalizes the discipline.

## 1.1 What AC(0) is

AC(0) is the complexity class of constant-depth polynomial-size circuits with unbounded fan-in AND/OR gates. AC(0) cannot compute PARITY (Furst-Saxe-Sipser, Ajtai). At AC(0) depth, problems are flat: each step is local; the answer accumulates.

## 1.2 Why BST uses AC(0)

BST aims for proofs that flatten: each step verifiable locally, no deep recursion required. Casey's "give a child a ball and teach them to count" — BST's slogan — captures the AC(0) discipline.

## 1.3 The practical discipline

When facing a new problem: ask "what does this reduce to at depth 0?" If counting suffices, the proof is AC(0). If not, the depth is the obstacle to study.

## 1.4 What comes next

Chapter 2 develops the AC graph as research instrument.

---

**Where to look this up**: BST `/ac0` skill documentation in `.claude/commands/ac0.md`; Furst-Saxe-Sipser 1981.
