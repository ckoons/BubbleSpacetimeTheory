---
id: grace_RECONCILE_m_u_first_live_stamp_soft_spot_is_observable_not_BST_holdout_2026-07-27
date: 2026-07-27
program: RECONCILE
status: current
supersedes: [K755-a]
superseded_by: null
topic_tags: [up-quark, m_u, soft-spot, mass, observable-softness, tier-reconciliation]
claims:
  - id: this-a
    topic: up-quark (m_u) soft spot — resolution
    status: current
    superseded_by: null
    date: 2026-07-27
---

# [RECONCILE] m_u — the first live supersede stamp: the "soft spot" is in the observable, not a BST holdout

*Grace | 2026-07-27 Mon | [RECONCILE] track, first live stamp (Grace+Keeper). Keeper's prompt: "up-quark resolved this past week → K755's 'soft spot' is STALE, it misled the auditor yesterday." This is the worked example the reverse-walk follows. Convention format (superseded_by frontmatter) is Keeper's to spec; this is the substantive content + proposed stamp.*

## The stale entry (what misled the auditor)
- **Source:** K755 note (on the V_ub reclassification) in `data/bst_26_tier_map.json`: *"The soft-spots list shrinks to just m_u."* And `BST_PROGRAMS...2026-07-26`: *"The '26th' / genuine holdout is m_u (up-quark mass) — 'the one remaining true soft spot' (K755)."*
- **The stale reading:** m_u treated as BST's one remaining genuine derivation-hole / weakness. Read that way, it says the framework can't do the up quark — which is what misled the auditor yesterday.

## The resolution (this past week — supersedes the stale reading)
m_u is **NOT a genuine BST holdout.** It splits cleanly into a derived ratio + an observable-side softness:
1. **The RATIO is derived:** m_u/m_d = √(N_c/(rank·g)) = √(3/14) — tier **LATTICE** (Fresnel/refraction monomial), 0.09%. Already in the tier map. Not soft.
2. **The up-type ladder anchors at its clean heavy end:** m_t = v/√2, m_c = α·v/√2, both from the forced scale v = m_p²/(g·m_e) — m_e-locked, no heavy-quark input (BST_Verification_Tests_July2026). The ladder anchors at the *heavy* (clean) end, not the soft light end.
3. **The mechanism for up-smallness is derived:** up is the lightest fermion because it is the up-type deposit *furthest from the boundary* (boundary/bulk unification, grace 06-28) — a target-innocent mechanism, not a fit.
4. **The residual ~22% softness is in the OBSERVABLE, not BST:** a confined quark has no clean pole mass; the quoted m_u is scheme-dependent (BST_PROGRAMS 07-26). The up n=0 constant-mode value is a computation limit tested against the n–p splitting (not a two-mass artifact). The softness is in the *definition of the observable*, not in BST's computation.

## Corrected tier / framing (what the stamp installs)
> **m_u is a derived RATIO (m_u/m_d = √(3/14), LATTICE) with an OBSERVABLE-soft absolute value (scheme-dependent confined-quark mass, ~22% on the n=0 constant mode).** It is **not** BST's "26th genuine holdout." BST has no genuine derivation-hole here; the soft spot is real but located in the observable's definition, not in the framework.

## Proposed stamp (apply per Keeper's convention — never delete, forward pointer)
- On the K755 tier-map note "soft-spots list shrinks to just m_u": add `superseded_by: [this note] (2026-07-27)`, reason "softness is observable-side, not a BST holdout; m_u/m_d=√(3/14) derived."
- Forward pointers (the `--current` view resolves to): tier-map `m_u/m_d = LATTICE`; BST_PROGRAMS 07-26 (observable-softness); BST_Verification_Tests_July2026 (up-type ladder from v; n=0 = constant-mode limit vs n–p).
- **Do NOT delete** the K755 framing — stamp it superseded with the pointer (per the convention).

## Flags for Keeper (co-lane)
1. **Convention format:** ready to apply the frontmatter `superseded_by` stamp the moment your RFC/Dublin-Core spec lands — this note is the content.
2. **★ K755 collision (a currency issue itself):** "K755" is cited for BOTH the tier-map/soft-spot audit AND the G₂-stabilizer/SU(3)-group derivation (Cal 07-15: "SU(3) group = derived (G₂-stabilizer, K755)" — which Cal HELD at SUPPORTED/hosted, not derived). Two different claims under one K-number is exactly the kind of stale/ambiguous reference the corpus-currency machinery should catch. Flagging for the reverse-walk.

— Grace, 2026-07-27. [RECONCILE] first live stamp: m_u "soft spot" (K755) is STALE — the up-quark resolved. m_u/m_d=√(3/14) is DERIVED (LATTICE, 0.09%); the up-type ladder anchors at the clean heavy end (m_t=v/√2, m_c=α·v/√2 from forced v); up-smallness has a derived boundary-distance mechanism; the residual ~22% is OBSERVABLE softness (confined-quark scheme-dependence on the n=0 value), NOT a BST holdout. Corrected framing installed: BST has no genuine 26th derivation-hole; the soft spot is in the observable. Proposed supersede stamp ready for Keeper's convention. Flagged the K755 collision (soft-spot vs G₂-stabilizer under one K-number) for the reverse-walk.
