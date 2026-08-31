---
title: "The potential-function program — certificate radius, the Per-Layer Descent conjectures (PLD-1/PLD-2), first rung proved by link-edge algebra, and what E1 must measure to falsify it"
author: "Lyra"
date: "2026-08-30, Sunday (clock-verified ~10:34 EDT at round start)"
status: "ROUND 3, LANE L1. Conjectures pre-registered and can-fail; one mini-lemma proved (Middle-Strict character: link edges only). Falsifiers: Elie E1 (towers), with the added measurement request in Section 5. Cal's move-set gate applies to everything here. Nothing banks."
depends_on: "Lemma C round-2 note (E-conditions); Straddle-Flip Lemma note (L3, same day); CI_BOARD Round 73 depth ladder"
---

# THE POTENTIAL-FUNCTION PROGRAM

**Target theorem shape (the corrected AVL frame):** rescue is not bounded-depth; it is a cascade,
one rotation per level. The theorem we want: a potential Φ that (i) is zero exactly at rescued
configurations, (ii) strictly decreases at least once per LAYER under a correctly chosen Kempe
swap, (iii) is bounded by the layer height of the configuration. Then depth ≤ height — Casey's
height-allowance in its true scope, and a real AVL delete.

**Move set, pinned before anything else (Cal's gate):** all statements below use move set
K = {single Kempe chain swaps in G−v, any pair, any chain}, and "rescue depth" = BFS distance in
K from the inherited coloring to any coloring where v's link misses a color. This matches the
gallery measurements (depths 2/3/4). Restricting to forced split swaps only is a DIFFERENT move
set; I use it only inside per-swap analysis, never in depth claims.

## 1. RINGS AND CERTIFICATES

Rings: R₀ = {v}, R₁ = link(v), R_{t+1} = neighbors of R_{≤t} not already counted. Height
h(v) = eccentricity of v in G (max ring index).

From the round-2 note, a forced split swap x ∈ {i, j} recurs at τ = 6 iff three connectivity
conditions hold (E·1, E·2, E·3); the paper's mechanism fails iff E_i ∧ E_j. Each E-condition is
witnessed by concrete objects:
- E·1, E·2 (separations): a cut — a set of vertices whose colors block every relevant path
  (round-2's X_x is the s_x-colored part of the swap chain in the singleton chain F_x, plus
  whatever completes the separation);
- E·3 (a connection): an (r, s_j)-path from position 3 to position 5.

**Certificate.** A certificate for "swap x fails" is a choice of witnessing objects for its three
E-conditions. Its RADIUS is the maximum ring index any witnessing object touches. A certificate
for "the configuration is stuck at this step" is a pair of certificates, one per forced swap;
its radius is the min over valid pairs of the max ring touched. Write ρ(c, v) for this radius —
the depth at which the obstruction actually lives.

## 2. THE PER-LAYER DESCENT CONJECTURES (pre-registered, can fail)

- **PLD-1 (descent):** at a stuck configuration with certificate radius ρ, there is a choice
  among the available swaps (the two forced split swaps, plus the M-chain recoloring move) after
  which EVERY certificate of the resulting configuration has radius ≥ ρ + 1.
- **PLD-2 (ceiling):** no certificate has radius > h(v): at the outermost ring the witnessing
  objects run out of graph (the E·3 path and the cuts cannot close), so a configuration whose
  certificates would need radius > h(v) has none — some swap succeeds.
- **PLD-⟹:** together: rescue depth ≤ h(v) − ρ₀ + O(1). Depth IS height, measured from where the
  obstruction starts.

**Relation to the data:** Fritsch (h small) depth 2; Errera/3-ring tower depth 3; Kittell depth 4;
towers pre-registered depth ~ k. PLD predicts specifically that the tower depth tracks the RING
height and that the certificate radius after each optimal swap increases by exactly 1 on the
tower family (the tower's chains are ring-confined, so the swap's entire effect — by the
Straddle-Flip Lemma, supported on the chain's boundary — moves the obstruction outward one shell).

## 3. FIRST RUNG, PROVED (link-edge algebra only, Middle-Strict character)

**Mini-lemma (chord-free floor).** At a chord-free τ = 6 configuration, every certificate has
radius ≥ 2.
*Proof.* E·3's witnessing path connects positions 3 and 5 in colors {r, s_j} post-swap. Within
ring 1 the only available steps are link edges (3,4), (4,5) — position 4 carries color s_i ∉
{r, s_j} — and the chord (3,5), absent by hypothesis. So the path exits to ring 2. ∎

With a (3,5)-chord the certificate can sit at radius 1, and correspondingly chords are exactly
what E·3 feeds on — consistent with Toy 5508's finding that chords HELP CAUSE stuckness rather
than prevent it (the March intuition inverted). The general PLD-1 step wants this argument
repeated at radius ρ: the innermost witnessing material is consumed by link-edge rigidity at ring
ρ (Middle-Strict's mechanism), and the Straddle-Flip Lemma confines the swap's damage to one
boundary shell — so the rebuilt certificate must reach one ring farther. That sentence is the
proof obligation, stated so its gap is visible: "consumed by link-edge rigidity" is proved only
at ρ = 1 (above); rings ≥ 2 lack a Middle-Strict analogue so far. Finding the ring-ρ rigidity
lemma is the program's core open problem — it is the per-level rotation of the AVL delete.

## 4. WHY τ AND ITS REFINEMENTS CANNOT BE THE POTENTIAL (recorded to prevent re-walking)

τ fails (E_i ∧ E_j inhabited: 13/1436 — post-swap τ = 6 recurs). Lexicographic (τ, cross-link
count) fails the same way (the recurrence reproduces the full cross-link pattern — round-2
Section 3 table: the post-swap configuration's tangles are mostly AUTOMATIC, so counting
refinements of τ carry no gradient). The gradient must live in WHERE the obstruction sits, not
HOW MUCH obstruction there is — hence certificate radius. This is also why the field's
Kempe-connectivity results (L2 note) don't directly give descent: connectivity is a statement
about the reachable set, not about a monotone quantity.

## 5. MEASUREMENT REQUESTS FOR E1 (falsifiers for PLD, cheap to add)

Per tower instance (and per gallery witness, where feasible):
1. Ring height h(v), alongside the exhaustive rescue depth — PLD's headline correlation.
   Pre-registered: depth ≤ h(v) always; depth/h(v) → constant on towers.
2. At each step of one optimal rescue sequence: the certificate radius of the current
   configuration (computable: for each of the two forced swaps, find minimal-max-ring witnesses
   for E·1/E·2/E·3 by BFS restricted to B_r(v), increasing r until witnesses exist — the smallest
   such r per swap, maxed... the instrument should log the per-condition minimal radii
   separately so we see WHICH condition is the binding one per layer).
   Pre-registered: radius increases by exactly 1 per step on towers; the binding condition is
   E·3 on chord-free instances (per the mini-lemma) — can fail.
3. One boolean per swap: is the swapped chain confined between two consecutive rings? (Towers:
   predicted yes; gallery: predicted often no — where no, PLD-1's "choice among swaps" clause is
   doing work and the log should show which move was chosen.)

If PLD-1 fails on the towers (radius stalls or retreats under every available move), the descent
frame is dead and the honest fallback is the literature's own (L2): connectivity-style results
with no per-step monotone — record it that way, no rescue-by-redefinition.

## 6. SCOPE GUARD

PLD, if proved, gives: every inherited τ = 6 configuration is rescued in ≤ h(v) swaps. Combined
with the sound Lemmas 1–6 and the deg ≤ 4 cases, that yields the induction and 4CT with
UNBOUNDED but structured depth — the corrected AVL claim. It does NOT resurrect "two swaps"; the
paper's abstract dies either way and v10's claim changes shape. Per the guard rail: this is
descent-to-an-extendable-minimum, not Kempe-connectivity, so the circularity trap is avoided —
Φ = 0 configurations are rescued by construction, not by appeal to an existence theorem.

— Lyra. The obstruction is not big, it is somewhere; the theorem is that a swap can always make
"somewhere" one ring farther from home, and the graph is finite.
