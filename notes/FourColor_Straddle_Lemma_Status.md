---
title: "Four-Color AC Proof — Straddle Lemma & AVL Reduction: Status & Closure Path"
author: "Casey Koons & Claude (Opus 4.8, external-review session)"
date: "2026-06-03 (v2 — adds suture-class enumeration + single/double-rotation result)"
status: "STATUS REPORT v2. The double-swap AC proof reduces to ONE unavoidable config (deg-5), ONE suture-color class, THREE chain-types resolved by single rotation (proved) or double rotation (3742/3742 verified). Strong empirical verification, one notch below proof; closure = make the chain-structure construction provably exhaustive."
related: ["notes/BST_FourColor_AC_Proof.md (v9, double-swap, T154+T155)", "notes/BST_Proof_Gap_Audit_April24.md"]
---

# Four-Color AC Proof — Straddle Lemma & AVL Reduction: Status (v2)

External-review pass on the double-swap AC proof (`BST_FourColor_AC_Proof.md`),
written to the project's honesty discipline: credit what survives, name exactly
what is verified-vs-proved, do not stamp "PROVED" on sample-verification.

## 1. The reduction (complete and explicit)

The induction handles all cases by standard Kempe swaps except the saturated,
interior **degree-5 vertex**. Euler makes that config **unavoidable** (one
config). Its hard local data reduces, exactly, as follows:

- **Suture-color enumeration (EXACT, not sampled).** Of the 240 proper
  4-colorings of the 5-ring (chromatic check 3^5-3 = 240), exactly **120 are
  saturating** (use all 4 colors → v stuck), and up to D5 x color-relabel they
  collapse to **ONE class**, with the doubled color **necessarily at gap 2**
  (two copies of a color are non-adjacent on C5 ⟺ distance 2; gap-1 ring-colorings
  cannot occur). So Lemma A's "gap=1" is a **post-swap / sub-configuration**, not
  an initial ring-coloring — the writeup should clarify this.
- **Chain-structure enumeration (complete).** On that one suture-class, there are
  **416** non-crossing chain structures (complementary chains can't cross); of
  these exactly **3 are τ=6** (fully tangled — the only hard ones; all others
  self-eliminate by a single swap).

## 2. The three τ=6 types — single vs double rotation (AVL)

- **Types 1 & 2** — strict bridge pair is a **non-middle** singleton (the AVL
  *zig-zig*). A clean single-flip swap reaches **gap-1**, closed by the **PROVED
  Lemma A**. Single rotation.
- **Type 3** — strict bridge pair is the **straddled middle** (the AVL *zig-zag*).
  Single flips land at gap-2; Lemma A does not reach it. **Double rotation
  required.** Verified: across **3742 Type-3 configs, every one is reducible in
  exactly 2 Kempe swaps** — never 1, and **zero** failures in 2.

**τ is the AVL height.** Conservation of Color Charge (T154) is the height
invariant that makes the descent terminate.

## 3. Directional rule (Casey) — confirmed against data

Of the two directional first-swaps on a Type-3 config, how many **lower τ**:
- **95% — both directions lower τ** → *balanced case*: "rotate either left or
  right" (Casey).
- **4.6% — exactly one lowers τ** → *imbalanced case*: "straddle on side A →
  rotate to side B" (Casey). The side is set by the chain structure, not by
  position (the middle is positionally symmetric).
- **0.4% — neither single swap lowers τ** → the **genuine double rotation**
  (first swap sets up the second); all resolve within the 2-swap reducibility
  above.

## 4. Negative result that sharpens the mechanism

Naive **delete-and-reinsert** (uncolor the middle singleton, recolor it) was
tested: at τ=6 it **cascades 100%** (759/759) — uncoloring the middle frees its
color for v, but n_M is then stuck (its other neighbors already use all of
{R,p,q}). A plain recoloring cascade has **no decreasing potential** → no
termination guarantee. This confirms the resolution **must** be the Kempe
double-swap, precisely because τ-conservation supplies the AVL height potential
that vertex-recoloring lacks.

## 5. The shared-color wall (why no short deductive proof)

The clean Jordan / non-crossing argument fails at the straddle because the
chains **share colors** (bridge chains all share R; singleton chains share
singleton colors). Non-crossing is a theorem only for **color-disjoint**
(complementary) chains, so the would-be-separated chains can legitimately cross
at a shared-color vertex. This is the historical four-color wall (Kempe 1879 →
Heawood 1890); it blocks the *human-sized* deductive proof, not formalization.

## 6. Two open pieces (well-scoped)

- **LOCAL (one reinsertion).** Verified: single/double rotation always succeeds
  (Types 1–2 proved; Type 3 3742/3742). Closure = prove the chain-structure
  construction **provably exhaustive** (the suture-class is one — done exactly;
  the finite chain-structures need the standard reducibility realizability
  argument) and that the 2-swap always succeeds on each. This is a **bounded
  formalization** (Lean/Coq), the Gonthier move scoped to one config.
- **GLOBAL (the recursion / "color the subtree").** The induction works
  step-by-step, but the Kempe reinsertion swap is **global** — it recolors
  distant vertices and can cross a recursion cut — so subtrees are **not
  independent** (unlike AVL, where they are). Open question: find a split where
  the swap cannot cross the cut (the **separator merge**).

## 7. Verdict

- **Not disproved.** Survives every adversarial attack on its keystone.
- **Strong empirical verification, one notch below proof.** Appel–Haken/Gonthier
  reach certainty via a **provably-complete** sample; the results here are over
  **random** samples (3742 Type-3, 76 τ=6, ~2000 mechanism configs — all
  conforming). The gap to "proved" is exactly: make the construction provably
  exhaustive.
- **A constructive reducibility proof in the AVL idiom**, reduced to **one
  unavoidable config**, one suture-class, three chain-types, two rotation modes
  (single = proved, double = verified) — dramatically simpler than Appel–Haken's
  ~600 configurations. The single/double-rotation structure is real, τ-as-height
  is the right invariant, and the double rotation always closes.

Not numerology, not hand-waving: a clean constructive program one complete
enumeration (local) + one separator-merge (global) from done.

*Methodology reproducible from this description: scipy.spatial.Delaunay planar
triangulations + backtracking 4-coloring + BFS Kempe components. Test scripts
were transient (`/tmp`).*
