---
title: "Independent Audit of the BST P != NP / Cycle-Delocalization Track"
author: "Casey Koons & Claude (Opus 4.8)"
date: "2026-06-04"
status: "AUDIT (honest). Independent computation confirms the empirical backbone-invisibility but places the track in the same category as the four-color analysis: a re-derivation of known results + an unproven conjecture whose hard step is the open problem itself, plus one quantitative identity that needs care. NOT a non-meh result."
related: ["notes/BST_AC_Paper_C_Delocalization.md","notes/BST_AC_Resolution_Standalone.md","notes/BST_AC_MIFC_Proof_Attempt.md"]
---

# Independent audit: P != NP / CDC track

Picked as the best "non-meh" candidate among the BST Millennium proofs (real proof
complexity, a concrete combinatorial object). Independently recomputed the core
claims rather than trusting the toys.

## What is correct (verified independently)

- **Backbone invisible to local probing.** For random 3-SAT at `alpha ~ 4.2`, both
  unit propagation and **failed-literal probing** recover **zero** backbone bits
  (computed, n = 12..16, brute-force backbone). The backbone is genuinely a
  global/non-local object.
- **`beta_1(clique complex) = Theta(n)`.** Verified; small-n values (`~1.2n`) are
  pre-asymptotic (edge collisions); the asymptotic `~7.5n` (BST's figure) is correct
  as `n -> infinity` (collisions vanish, `E -> 3 alpha n`, minus `~alpha n` triangle
  relations).

## What this actually is

- **Known, not new.** "The backbone at threshold is a global property invisible to
  local propagation" is the established physics of random SAT (cluster / frozen-
  variable structure; Mezard-Zecchina, Achlioptas-Coja-Oghlan, Ding-Sly-Sun). The
  topological (`H_1`) framing is a **re-description**, not new content.
- **Admitted re-derivation.** The unconditional resolution lower bound (`Resolution_
  Standalone`) "recovers the exponential resolution lower bounds of
  Chvatal-Szemeredi (1988) and Ben-Sasson-Wigderson (2001)" -- by its own statement.
- **Unproven conjecture for the real claim.** P != NP follows only from the **Cycle
  Delocalization Conjecture** (`I(B; f(phi)) = o(|B|)` for all poly-time `f`), which
  is essentially average-case hardness of SAT -- itself an open problem at least as
  hard as P != NP. The extension to all proof systems (Extended Frege) is
  "conditional, via topological inertness of extensions" -- i.e. the open problem,
  not a proof.

## One quantitative concern

The framework's budget reads `n = I_derivable + I_fiat + I_free` with `I_fiat =
beta_1`. But `beta_1 = Theta(n)` with constant `> 1` (asymptotically `~7.5n`), so
`I_fiat = beta_1 > n`. A cycle count exceeding `n` cannot literally be "bits of
backbone information" (the backbone has `|B| <= n` bits). The identity `I_fiat =
beta_1` conflates a topological cycle count with an information quantity; it needs
reinterpretation (e.g. `beta_1` counts independent fiat *choices*, each carrying
`o(1)` recoverable backbone bits), and as written it breaks the `n`-bit budget.

## Verdict

Same shape as the four-color analysis: the rigorous parts are **re-derivations of
known results**, the genuinely new claim is an **unproven conjecture** whose hard
step is the open problem itself, and there is an additional **identity that does not
typecheck** as stated. The clean correct fact (backbone is global) is established
SAT physics. **This is not a non-meh result**, and the P != NP claim is not a proof.
