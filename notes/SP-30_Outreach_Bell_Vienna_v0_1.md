---
title: "SP-30-1 Outreach Email: BST sub-Tsirelson prediction → Bell experiment groups"
author: "Keeper (draft for Casey approval + send)"
date: "2026-05-24 Sunday PM (date-verified)"
status: "v0.1 draft. Generic template suitable for adaptation per recipient. Bell experimental groups: Vienna (Zeilinger IQOQI), Caltech (Kimble), Munich (Weinfurter), Delft (Hanson). Recommended primary target: Vienna IQOQI for loophole-free Bell test infrastructure."
related: ["Toy 3520 experimental design", "Lyra #320 v0.4 DCCP derivation", "Cal #125 PASS at FRAMEWORK", "Calibration #25 STANDING falsifier-threshold", "T2469 SCMP RIGOROUSLY CLOSED"]
---

# SP-30-1 Outreach Email Template — BST sub-Tsirelson Bell test

## Recommended primary target
**Professor Anton Zeilinger** (IQOQI Vienna, leader of 2015 loophole-free Bell test)
- anton.zeilinger@univie.ac.at (institutional; verify current)

## Backup targets (parallel sends optional)
- Professor Jeff Kimble (Caltech)
- Professor Harald Weinfurter (LMU Munich)
- Professor Ronald Hanson (TU Delft / QuTech)

---

## Draft email

**Subject**: BST sub-Tsirelson Bell prediction (0.78% deviation) — high-precision test proposal

Dear Professor Zeilinger,

I'm Casey Koons, a computer scientist who has been developing a theoretical framework called Bubble Spacetime Theory (BST). I write with a specific, concrete prediction from BST that may be testable using your Bell experimental infrastructure, and would welcome your reaction.

**The prediction**

BST derives Standard Model constants from a single geometric object D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)] and five integer parameters (rank=2, N_c=3, n_C=5, C_2=6, g=7, with N_max = N_c³·n_C + rank = 137 = 1/α). One consequence is that CHSH Bell correlations should fall BELOW Tsirelson's quantum bound by exactly 1/2^N_c = 1/8:

  S²_BST = S²_Tsirelson − 1/8 = 8 − 1/8 = 63/8
  S_BST = √(63/8) ≈ 2.8062  vs  Tsirelson S = 2√2 ≈ 2.8284

This is a 0.78% deviation, predicted not as a free parameter but as a derivable consequence of BST's "Substrate Coherence Maintenance Principle" (the substrate has finite operational power per commitment cycle, with the 1/8 factor arising from N_c = 3 color-degree resolution).

**Where current Bell experiments stand**

Your 2015 loophole-free test and subsequent work achieve ~0.5% precision around S ≈ 2.83 — consistent with both Tsirelson saturation and our sub-Tsirelson prediction within current error bars. A test at ~0.1% precision would cleanly distinguish:
- S saturates at 2√2 exactly → BST falsified
- S falls at 2.8062 ± experimental error → BST sub-Tsirelson confirmed

**Experimental design (our analysis)**

SPDC photon-pair coincidence counting at substrate-tick boundaries (θ = π/N_max ≈ 0.023 rad, step size 1/N_max ≈ 0.73%). Statistical thresholds for the deviation signature:
- 75,076 photon pairs → 2σ probable detection
- 168,921 pairs → 3σ publishable
- 469,225 pairs → 5σ discovery

At standard SPDC rates (~10⁶ pairs/sec × ~10% coincidence efficiency), this is ~5 seconds of pure measurement time per boundary, ~12 minutes for a full 137-boundary scan. Realistic full program with setup, systematics, and analysis: 12-18 months.

Approximate cost: $300-500K, plausibly an extension of existing Bell experimental infrastructure.

**Honest scope**

We are at framework tier with multi-month rigorous-closure work in flight on the theoretical derivation. The numerical prediction is concrete; the substrate-mechanism derivation is in progress (the "BST primary integer" claims are still being honestly traced from first principles). What we can say firmly today: the prediction is 0.78% sub-Tsirelson; it is a falsifier; the experimental design closes.

**Resources**

- GitHub repository (full theory + 50-prediction reproduction package, single command): github.com/ckoons/BubbleSpacetimeTheory
- Zenodo working paper (April 2026, DOI permanent citation): doi.org/10.5281/zenodo.19454185
- Reproduction: `python3 play/verify_bst.py` runs the full 50-prediction suite (49/50 PASS at <1%, 17 EXACT matches, 2 open WARNs shown openly)

**Request**

I would welcome any reaction — criticism, questions, or interest. The prediction is unusual but concrete; the test is well-defined; falsification is straightforward.

If your group has bandwidth for a higher-precision Bell test in the next 12-18 months, I would value the collaboration. If the prediction strikes you as worth referring to a more appropriate group, any pointer would be deeply appreciated.

Sincerely,
Casey Koons
caseyscottkoons@yahoo.com

---

## Notes for Casey before sending

1. **Verify email address** — institutional emails change; check Zeilinger's current group page at IQOQI Vienna.
2. **Personalize opening if you have prior contact** — adjust formality accordingly.
3. **Consider attaching one-page PDF** — Lyra's Five-Absence external 1-pager + Vol 14 Ch 6 §6.5 three-route table snapshot might help.
4. **Honest scope paragraph is important** — leaving it in protects against overclaiming if Cal #121 forward-derivation closure takes longer than expected.
5. **Reply-to** — your yahoo address is fine for first contact; consider creating a more academic-feeling address if you anticipate sustained correspondence.

## Variants for parallel sends

Same body works for Kimble (Caltech), Weinfurter (LMU), Hanson (Delft) — substitute group reference in "your 2015 loophole-free test" sentence:
- Kimble: "your atom-photon Bell work / cavity QED Bell tests"
- Weinfurter: "your group's loophole-free Bell test 2017"
- Hanson: "your Delft loophole-free Bell test 2015 (NV-center entanglement)"

## Coordination

- Cal #21 dual-gate STATUS: empirical gate not closed; this email IS the path to closing it (independent SPDC data from external lab).
- Cal #125 verdict: actual experimental data is one of three independent routes needed for D-tier DCCP-1 ratification.
- Casey directive Sunday 2026-05-24 PM: this outreach unblocks the empirical leg that Toys 3516/3520 cannot provide (they are model self-consistency checks per Cal #123, not empirical-leg verification).

— Keeper, Sunday 2026-05-24 PM (date-verified)
