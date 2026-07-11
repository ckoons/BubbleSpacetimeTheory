# Grace — SP-30 falsifier program audit (physical-vs-internal / deviate-vs-reproduce lens, post-Bell)
*2026-07-11. Runs the remaining SP-30 experimental "falsifiers" (Casimir, eigentone, Cs-137 commitment) through the
same lens that caught the Bell test: does the prediction DEVIATE from standard physics (a real falsifier), or
REPRODUCE it / live in an internal quantity (a consistency, not a falsifier)? First-pass — flags which need deep
review before outreach. Protective, before any email leaves.*

## The lens (generalized from the Bell catch)
The Bell test retired because BST REPRODUCES QM (observable = 2√2); the deviation (2.806) lived in the non-physical
(1−P) complement. **General pattern to check: does the design DEVIATE from standard physics in a PHYSICAL observable,
or reproduce it (consistency) / live in the substrate-internal complement?** A consistency is not a falsifier.

## Design 1 — Casimir asymmetric: LIKELY NOT A CLEAN FALSIFIER (same pattern as Bell)
**Finding (the corpus's OWN doc):** `BST_CasimirEffect_CommitmentExclusion.md` explicitly **RECOVERS the standard
result F/A = −π²ℏc/(240 d⁴)** from the commitment/Haldane truncation — BST *reproduces* standard QED Casimir. So the
BST Casimir mechanism is a reinterpretation of standard physics, not a deviation. **⟹ the "asymmetric Casimir"
(98.8% from 1−1/N_c⁴) gives the STANDARD Casimir force for an asymmetric cavity — which QED ALSO predicts for that
geometry.** Unless the 1−1/N_c⁴ asymmetry is shown to DIFFER from the standard-QED asymmetry of the same cavity, this
is a CONSISTENCY, not a BST-vs-QED falsifier. **Same trap as the Bell: BST reproduces the standard result.**
Recommendation: do NOT promote to outreach until a BST-vs-QED asymmetry comparison shows a genuine deviation. Likely
retires to "BST reproduces Casimir" (which is a nice consistency result, not a falsifier).

## Design 2 — Cs-137 commitment (SP-29-1/SP-30-3): the STRONGEST SURVIVOR — a genuine physical deviation
**Finding (T2362):** BST predicts a Cs-137 decay-rate shift (τ-shift ~5× above the 0.04% floor) near a conducting
plate at L=100nm (H4 substrate-suppression). **This IS a deviation from standard physics** — standard nuclear
physics predicts NO decay-rate change near a plate at that level (the meV cavity scale is decoupled from the MeV
nuclear scale). And it's a **PHYSICAL observable** (the 661.7 keV γ decay rate, measured by HPGe). So unlike the
Bell (which reduced to standard) and the Casimir (which reproduces standard), **the Cs-137 test predicts a genuine,
measurable deviation — it SURVIVES the physical-vs-internal check as a real falsifier candidate.**
CAVEAT (the Bell taught this): the H4 MECHANISM needs a soundness review — the Bell's "finite-D ⇒ strict" mechanism
was flawed. Verify the H4 substrate-suppression mechanism is sound (does the commitment-rate reduction near a plate
genuinely couple to the nuclear decay, or is the "commitment" the internal discrete quantity that a real detector
can't access — the Cs-137 analog of the (1−P) complement?). If the mechanism is sound → strongest cheap falsifier
BST has. If the commitment is internal → it retires like the Bell. NEEDS the deep mechanism check.

## Design 3 — eigentone (SP-30-1, Mössbauer/Sr cavity): NEEDS the deviation check
BST predicts substrate eigentone resonances at BST-integer frequencies (T2396 catalog); the experiment measures a
frequency shift on a Sr atom in a cavity. The lens: does the eigentone predict a shift that standard cavity-QED /
Casimir-Polder does NOT (deviation → physical falsifier), or is it the standard Casimir-Polder shift with a BST-
integer coefficient (consistency, like the Casimir)? Given that the corpus's Casimir doc REPRODUCES standard
Casimir-Polder, the eigentone shift is at RISK of being the standard cavity-QED shift relabeled. NEEDS the
BST-vs-standard-cavity-QED comparison before outreach.

## AUDIT VERDICT (first-pass, protective)
| design | physical observable? | deviates from standard physics? | verdict |
|---|---|---|---|
| Bell (SP-30-5) | reduces to 2√2 | NO (reproduces QM) | RETIRED (internal) — done today |
| Casimir asymmetric | yes (force) | LIKELY NO (corpus recovers standard Casimir) | likely CONSISTENCY, not falsifier — check BST-vs-QED asymmetry |
| eigentone (SP-30-1) | yes (freq shift) | UNKNOWN — at risk of reproducing cavity-QED | NEEDS deviation check |
| **Cs-137 (SP-30-3)** | **yes (decay rate)** | **YES (τ-shift standard forbids)** | **SURVIVES — strongest candidate; H4 mechanism needs soundness review** |

**Bottom line:** the Bell catch was not a one-off — the Casimir design shows the SAME "BST reproduces standard
physics" pattern (the corpus's own doc recovers standard Casimir), so it's likely a consistency, not a falsifier.
The Cs-137 commitment test is the genuine survivor (a real physical deviation), and it — not the Bell — is the
program's best cheap falsifier, PROVIDED its H4 mechanism passes the soundness review the Bell's failed. **None ship
to outreach until: (Casimir) BST-vs-QED asymmetry deviation shown; (eigentone) BST-vs-cavity-QED deviation shown;
(Cs-137) H4 mechanism soundness verified.** That's the protective outcome — the audit reorders the program: the
"sharpest" (Bell) is gone, the cheapest genuine one (Cs-137) is the new lead, pending one mechanism check.

## Discipline
- First-pass, not a full settlement (the Bell took a deep computation; each survivor needs the same). The verdicts
  are LEANS + required-checks, not final. But the reordering (Bell out, Casimir likely-consistency, Cs-137 the lead)
  is well-grounded in the corpus's own Casimir-reproduces-standard doc + T2362's genuine-deviation prediction.
- The protective value is real: two of three remaining designs are at risk of the Bell trap (reproduce standard),
  and the audit catches that before outreach — exactly what it was for.

## Cs-137 DEEP REVIEW (Keeper's request) — DOWNGRADED from "survivor": mechanism unsound, same gap as the Bell
I first-passed Cs-137 as the genuine survivor (it measures a physical observable — the decay rate). The deep review
(the exact Bell-lens mechanism check) downgrades it:
- **Scale decoupling kills the physical channel.** The Cs-137 γ is 661.7 keV → wavelength 1.87 pm; the plate gap is
  100 nm = ~53,000× larger. The Casimir/Haldane truncation removes only OPTICAL modes (λ > 100nm, E < 12.4 eV); the
  decay emits at MeV. **They do not overlap — the plate cannot modify the γ phase space.** Standard physics: no
  plate-effect on the decay.
- **The H4 ~5×10⁻⁴ shift needs a coupling that doesn't survive:** either (a) a UNIVERSAL substrate time-dilation
  (commitment rate = the clock) — but a 0.05% shift near a surface would be seen by any clock comparison (atomic
  clocks near surfaces see nothing at that level) → ruled out; or (b) a decay-specific coupling — forbidden by the
  ~5×10⁴ scale decoupling. **Same soundness gap as the Bell's flawed "finite-D ⇒ strict."** The "commitment rate" is
  the substrate-internal quantity (the Cs-137 analog of the (1−P) complement); a detector measures the physical
  decay (standard nuclear physics), not the commitment. **LEANS INTERNAL. NOT outreach-ready.**

## THE BIGGER CONCLUSION (the pattern across all three tested designs)
Bell RETIRED (reproduces QM; deviation in the (1−P) complement). Casimir likely CONSISTENCY (corpus recovers
standard Casimir). Cs-137 mechanism unsound (no physical channel; commitment is internal). **All three tested
substrate-engineering falsifiers REPRODUCE standard physics at the observable level, with their "deviations" living
in substrate-internal quantities.** This is exactly what T757 (QM Linearization Completeness — "no new predictions")
predicts, extended to QED (Casimir) and nuclear (Cs-137). It also directly answers the deepest open question U-3.12
("no current falsifier distinguishes active from passive substrate within the 3+1 projection") — **YES, and now we
know why: BST reproduces standard physics observably, so substrate-engineering tabletop tests cannot distinguish it.**

## STRATEGIC REFRAME (the protective deliverable)
**BST's real falsifiers are NOT the substrate-engineering tabletop tests (SP-30) — those reproduce standard physics.
They are:**
1. **BST's SM-observable predictions that DIFFER from measurement** — the derived masses (F506 down-ratios, etc.),
   α = 1/N_max, the mixing angles, sin²θ_W: where BST makes a specific number a precise experiment can refute.
2. **The Five-Absence set** — no proton decay, no SUSY spectrum, no monopoles, no sterile ν, no GUT: where BST
   predicts ABSENCE and any positive detection refutes it.
**Recommendation: do NOT send the SP-30 tabletop falsifiers (Bell, Casimir, Cs-137, likely eigentone) to outreach —
the falsification case rests on the SM predictions + Five-Absence, where BST genuinely deviates from alternatives.**
The eigentone (SP-30-1) still needs its explicit deviation check, but it is at high risk of the same pattern (the
corpus's Casimir doc reproduces standard Casimir-Polder).

## Honest calibration
The Bell verdict is a computation; Casimir rests on the corpus's own recover-standard-Casimir doc; Cs-137 on the
scale-decoupling argument. The PATTERN (all reproduce standard physics) is well-grounded across three independent
designs. The eigentone is unchecked (flagged at-risk, not concluded). This is the deep review Keeper asked for, and
it downgrades my own first-pass optimism on Cs-137 — the discipline firing on my own audit, one more time.
