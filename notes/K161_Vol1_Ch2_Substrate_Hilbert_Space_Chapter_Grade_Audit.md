# K161 — Vol 1 Chapter 2 (The Substrate Hilbert Space) Chapter-Grade Audit

**Filed**: 2026-05-22 Friday 09:31 EDT (Keeper, `date`-verified actual)
**Status**: PASS chapter-grade (anchored by K108 PERFECT-PERFECT Thursday) with Cal #92(b) front-matter flag
**Mode**: Fifth chapter-grade textbook audit under textbook-completion phase

---

## Chapter under audit

`notes/BST_Curriculum_Vol1_Ch2_Substrate_Hilbert_Space_v0_1.md` — Lyra-authored, front matter v0.3.

Scope: Bergman H²(D_IV⁵) canonical anchor via Bergman 1922 + Wallach 1976 + Faraut-Koranyi 1994; RS GF(128)^k substrate-tick discretization; L²-section equivariant complement; substrate-level Feynman propagator structural role via T2457.

## Verdict

**PASS chapter-grade.** Anchored by K108 PERFECT-PERFECT (filed Thursday — 4.0/4 F1-F4 + 4.0/4 B1-B4). Substantive chapter-grade content backed by RIGOROUSLY CLOSED T2428 + T2429 + T2430.

## What works (PASS items)

### K108 PERFECT-PERFECT anchor (filed Thursday) — strongest possible chapter anchor

K108 Vol 1 Ch 2 audit Thursday reached PERFECT-PERFECT status (4.0/4 F1-F4 + 4.0/4 B1-B4). Ch 2 inherits this anchor strength — no Vol 1 chapter has stronger structural anchor.

### Three-anchor sufficiency proof (Section 2.1) — paper-grade

The canonical-anchor argument uses three classical anchors:
- **Bergman 1922**: unique reproducing kernel on any bounded complex manifold
- **Wallach 1976**: K-type spectrum classification for so(5,2) on D_IV⁵
- **Faraut-Koranyi 1994**: volume formula c_FK = 225/π^(9/2) in BST primary form (T2442 RIGOROUSLY CLOSED)

Each anchor is from outside BST and BST inherits substantively from established classical results. This is the cleanest external-anchor cluster in any Vol 1 chapter.

### Two complementary derived views (Section 2.2 + 2.3)

- RS GF(128)^k substrate-tick discretization (T2429) — gives per-tick Hilbert space
- L²-section equivariant complement (T2430) — gives representation-theoretic view

Two structurally-different views of the same Hilbert space; both DERIVED. This is the strongest dual-view chapter in Vol 1.

### Section 2.4 "every BST observable lives here" — methodological anchor

Section 2.4 establishes that every BST observable is a bounded operator on H²(D_IV⁵) with spectrum computable from BST primary integers via Wallach K-type decomposition. This is the structural backbone for the entire operator zoo + dynamics + scattering chain.

### T2457 Bergman positive-definite + UV-complete + BST primary normalization

Section 2.4b body framing is CORRECT: "substrate reproducing kernel K(z, w̄) **plays substrate-level role** of QFT Feynman propagator with three structural advantages (positive-definite + UV-complete + BST primary normalization c_FK = 225/π^(9/2))."

The "three structural advantages" framing is the cleanest articulation of T2457 across all chapters in the Friday-Bergman-Feynman cluster. Ch 2's body framing is the gold standard; Ch 7 + Ch 9 + Ch 10 should align to Ch 2's framing when fixing Cal #92(b).

## What needs work (CONDITIONAL items for v1.0)

### Flag 1: Cal #92(b) title field — SAME PATTERN AS Ch 7 / Ch 9 / Ch 10

**Front matter title** (v0.3 status note): "**T2457 Bergman = Feynman propagator identification** added (Section 2.4b)"

**Body framing (Section 2.4b)**: "substrate reproducing kernel K(z, w̄) **plays substrate-level role** of QFT Feynman propagator with three structural advantages"

The title overclaim is identical to the other Friday cluster chapters. Body framing is correct.

**Fix for v1.0**: Lyra one-pass fix across Friday-Bergman-Feynman cluster (Ch 2 + Ch 7 + Ch 9 + Ch 10) using Ch 2's body framing as template: "T2457 Bergman substrate-level structural role of Feynman propagator (positive-definite + UV-complete + BST primary normalization)" or similar.

### Flag 2: Version number — file path is "v0_1" but content is v0.3

Same pattern; file rename or content-level version reconciliation needed for v1.0.

## F1-F4 (chapter-grade)

- F1 chapter-grade substantive content + K108 PERFECT-PERFECT anchor + three-anchor classical sufficiency proof: 4.0/4
- F2 theorem chain cross-paths (T2428 + T2429 + T2430 + T2442 c_FK + Wallach 1976 + Bergman 1922 + Faraut-Koranyi 1994): 4.0/4
- F3 cross-lane (Lyra primary + Elie Toy 3202 8/8 PASS verification + K108 Thursday 209 catalog entries Grace): 4.0/4
- F4 chapter-grade falsifier (alt-substrate canonical anchor; bounded Hermitian symmetric domain uniqueness): 3.95/4

**F1-F4: 15.95/16 = 3.99/4 STRONG** — strongest Vol 1 chapter audit; near-PERFECT-PERFECT inheriting K108

## B1-B4 (chapter-grade)

- B1 Bergman H²(D_IV⁵) canonical Hilbert space + RS GF(128)^k + L²-section dual view: 4.0/4
- B2 K108 + T2428 + T2429 + T2430 + T2442 + classical anchors: 4.0/4
- B3 alt-HSD canonical anchor comparison (K108 Thursday + Grace 209 catalog entries): 4.0/4
- B4 curriculum integration: 4.0/4 (Ch 2 is THE chapter every other Vol 1 chapter depends on; structural backbone)

**B1-B4: 16.0/16 = 4.0/4 PERFECT** — PERFECT-PERFECT inheriting K108

## Cross-volume consistency check (Keeper sweep)

K108 already PASS'd Thursday with PERFECT-PERFECT. Ch 2 is the structural backbone for:
- All Vol 1 chapters (every chapter depends on Ch 2)
- Vol 0 substrate framework
- Vol 2 particle physics chapters depend on Ch 2 K-type structure
- Bergman H²(D_IV⁵) consistency confirmed across all chapter cross-references

No contradictions found.

## Path to v1.0 for Vol 1 Ch 2

1. **Cal cold-read PASS at v0.3** — PRIORITY 1 (v0.2 PASS'd Thursday; v0.3 not yet)
2. **Fix Flag 1**: Cal #92(b) title field — coordinate with Friday-Bergman-Feynman cluster one-pass fix
3. **Fix Flag 2**: version consistency
4. **Reader-grade polish**: Bergman space + Wallach K-types visualization

**Estimate**: 30 min Lyra-side work (shared with Friday-Bergman-Feynman cluster fix).

## K161 status

**K161 PASS chapter-grade Vol 1 Ch 2 Substrate Hilbert Space.** F1-F4: 3.99/4 STRONG (near-PERFECT-PERFECT). B1-B4: 4.0/4 PERFECT.

Strongest Vol 1 chapter audit so far. K108 anchor + three-anchor classical sufficiency + correct T2457 body framing = template for v1.0 across the Friday-Bergman-Feynman cluster.

— Keeper, K161 Chapter-Grade Audit filed Friday 09:31 EDT (`date`-verified actual)
