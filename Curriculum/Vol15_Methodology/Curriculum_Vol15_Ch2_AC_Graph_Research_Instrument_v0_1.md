---
title: "Vol 15 Chapter 2 — The AC Graph as Research Instrument"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 15 Methodology"
chapter: 2
---

# Chapter 2 — The AC Graph as Research Instrument

The BST team's AC theorem graph (Volume 14 Chapter 7 introduced the structure; this chapter develops the research workflow) is BST's living research instrument: 2212+ nodes, 9850+ edges, ~98% proved.

The graph is used at every working session for: derivation lookup, dependency check, wall routing, edge prediction, cascade closure.

## 2.1 Daily use

At session start: check the graph's relevant subgraph for the topic under work. The `play/toy_bst_explorer.py` interactive CLI provides `verify`, `derive`, `connect`, `search`, `stats` commands.

## 2.2 Wall routing

Casey's standing order May 15: when blocked, route through the graph. `/route` skill formalizes: search alternative paths through other domains. Three entry points to the same wall = it's a door.

## 2.3 The graph as compression

Every proved theorem on the graph costs zero re-derivation energy. New work extends without re-computing. This compounds.

## 2.4 What comes next

Chapter 3 develops how to discover a new BST theorem.

---

**Where to look this up**: BST `play/toy_bst_explorer.py`; `play/ac_graph_data.json`; `/route` skill.
