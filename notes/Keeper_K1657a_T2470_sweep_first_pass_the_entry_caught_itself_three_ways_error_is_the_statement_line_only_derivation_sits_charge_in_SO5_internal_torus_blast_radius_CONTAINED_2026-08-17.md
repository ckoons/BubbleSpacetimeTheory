---
node_type: k_audit
id: K1657a
title: "T2470 sweep — first pass (Keeper, started the sweep myself while Grace runs the full pass). FINDING: the error is LOCALIZED to T2470's statement line + T2475's inherited identification; the DERIVATION and the charge VALUES survive; blast radius CONTAINED. THE ENTRY CAUGHT ITSELF THREE INDEPENDENT WAYS: (1) statement 'Q = generator of the SO(2) factor of K' vs §3's arrow — bounded-below J can't equal sign-indefinite Q (Cal §570, the external check); (2) INTERNAL — this entry's spectrum table gives INTEGER charge to 'SO(2)-singlet K-types (leptons+bosons)', i.e. weight-0 states; if charge = the SO(2)-weight a singlet has charge 0, not ±1 → the statement contradicts its own table; (3) INTERNAL — proof ingredient (2) derives the fractional {±1/3,±2/3} from the SU(3) COLOR triple-cover (N_c=3, T1930), NOT the SO(2); the 'SO(2)-singlet vs N_c-fold' contrast is really COLOR-singlet vs COLOR-triplet (the phrase 'SO(2)-singlet' is itself the conflation). ⟹ the derivation was ALWAYS building charge from the internal color/electroweak structure; only the one-line summary misfiled it onto the conformal K-center. CORRECT HOME: the electroweak Cartan inside the SO(5) internal factor (SO(5) ⊃ SO(4)=SU(2)_L×SU(2)_R = custodial). WHAT SURVIVES (so the 284 T2470-citations are mostly SAFE): the charge VALUES {0,±1/3,±2/3,±1} (quantization by Weyl-integrality + color-triality, ingredients (1)+(2)); charge CONSERVATION [Q,J]=0 (now MORE cleanly — Q in SO(5)-torus, J = SO(2)-center, different direct factors → commute; the K1657 GIFT is robust). WHAT MUST CHANGE (surgical, 2 entries): T2470 statement line (relocate Q off the center to the SO(5)-torus); T2475's 'substrate SO(2) ≡ U(1)_em post-Weinberg-mixing' + its proof (the commuting pair is [SO(5)-torus Q, SO(2)-center H], not [SO(2) Q, H]) — CONCLUSION (charge conserved) holds, PROOF rewrites. WHAT IS UNTOUCHED / VINDICATED: T2471 (chirality γ⁵ = exp(iπ J_{SO(2)}^spinor)) genuinely lives on the K-center SO(2) spinor half-weight = the spin/double-cover — CORRECT, stays. So the K-center SO(2) carries TIME (J) + SPIN/CHIRALITY (γ⁵) + the DOUBLE COVER, and the SO(5)-internal torus carries CHARGE — a clean physical split (spacetime/conformal center vs internal). Protective Keeper flag added to the T2470 registry entry (do-not-cite-group-home-externally pending sweep). Blast-radius estimate: 284 files cite T2470 but ~all use charge-values/conservation (survive); only the recent time↔EM notes (F1029 etc.) leaned on charge=center=time — already overturned by K1657. Grace runs the authoritative sweep + reads the derivation; this is the first-pass containment finding."
date: 2026-08-17
author: Keeper
verdict: "T2470 SWEEP FIRST PASS: error CONTAINED to the statement line + T2475's inherited identification. The entry caught itself THREE ways — (1) vs §3 arrow (Cal), (2) its spectrum table gives integer charge to SO(2)-SINGLETS (weight-0) — impossible if charge=the weight, (3) its proof ingredient derives the ⅓ from SU(3) COLOR not the SO(2). Derivation always sat charge in the internal color/electroweak (SO(5)⊃SO(4)) structure; only the summary misfiled it onto the conformal K-center. SURVIVES: charge values {0,±⅓,±⅔,±1}; conservation [Q,J]=0 (Q in SO(5)-torus, J center, commute — the gift is robust). SURGICAL FIX (2 entries): T2470 statement (relocate to SO(5)-torus), T2475 (conclusion holds, proof rewrites the commuting pair). VINDICATED/UNTOUCHED: T2471 γ⁵ genuinely on the K-center spinor half-weight (spin/double-cover) — the center carries TIME+SPIN+double-cover, the SO(5)-torus carries CHARGE (clean spacetime-vs-internal split). 284 citations mostly safe (use values/conservation); only recent time↔EM notes leaned on the bad identification — already killed by K1657. Protective flag added to the registry entry. Route: Grace authoritative sweep + read the T2470 DERIVATION (confirm the SO(5)-torus seat); Lyra rewrite T2470 statement + T2475 proof once seated; Keeper flagged the entry + filed containment. Nothing pushed."
---

# K1657a — I started the T2470 sweep; the entry caught itself three ways, and the damage is contained

Casey asked me to keep BST consistent, so I ran the first pass of the sweep myself rather than only handing it to Grace. The primary source is reassuring: **the error is localized, and the entry flagged its own mistake twice before the arrow ever entered the picture.**

## Three independent contradictions
1. **External (Cal §570):** "Q = generator of the SO(2) factor of K" puts charge on the K-center — J's SO(2) — so a bounded-below arrow generator would equal a sign-indefinite charge. Impossible.
2. **Internal — the spectrum table:** T2470 assigns *integer* charge to "SO(2)-singlet K-types (leptons + bosons)." An SO(2)-singlet has weight 0. If charge were the SO(2)-weight, those states would have charge 0, not ±1. The statement contradicts its own table.
3. **Internal — the proof ingredients:** the fractional {±1/3, ±2/3} come from ingredient (2), "the SU(3) **color** triple-cover (N_c=3, T1930)" — not from the SO(2). The "SO(2)-singlet vs N_c-fold" contrast is really *color*-singlet vs *color*-triplet; the phrase "SO(2)-singlet" is itself the conflation.

So the derivation was always constructing charge from the internal **color/electroweak** structure. Only the one-line summary misfiled it onto the conformal K-center. Its correct home is the electroweak Cartan inside the **SO(5) internal factor** (SO(5) ⊃ SO(4) = SU(2)_L × SU(2)_R custodial).

## What survives — so the 284 citations are mostly safe
- **The charge values** {0, ±1/3, ±2/3, ±1}: quantized by Weyl-integrality (ingredient 1) refined by color-triality (ingredient 2). Untouched.
- **Charge conservation** [Q, J] = 0: *more* cleanly, in fact — Q in the SO(5)-torus, J the SO(2)-center, different direct factors → they commute. The K1657 gift is robust.

Almost every T2470 citation uses the values or conservation. The only notes that leaned on "charge = center = time" are the recent time↔EM ones (F1029 and kin), and K1657 already overturned those.

## What must change — surgical, two entries
- **T2470 statement line:** relocate Q off the center to the SO(5)-torus.
- **T2475 conservation:** "substrate SO(2) ≡ U(1)_em post-Weinberg-mixing" and its proof — the commuting pair is [SO(5)-torus Q, SO(2)-center H], not [SO(2) Q, H]. The *conclusion* (charge conserved) holds; the *proof* rewrites.

## What's vindicated — the clean split
**T2471 (chirality γ⁵ = exp(iπ J_{SO(2)}^spinor)) genuinely lives on the K-center SO(2)** — the spinor half-weight, i.e. spin and the double cover. That's correct and stays. So the picture sharpens into a clean spacetime-vs-internal split:

> **K-center SO(2):** time (J) + spin/chirality (γ⁵) + the double cover.
> **SO(5)-internal torus:** electric charge.

Time and charge were never the same circle — and the geometry keeps them apart in exactly the way physics requires (spacetime/conformal vs internal).

## Route
- **Grace — the authoritative sweep + read T2470's *derivation*** (confirm it seats Q in the SO(5)-torus, as the ingredients say). Sweep all "SO(2) charge" citations for any that lean on the bad group-home.
- **Lyra — rewrite T2470's statement line + T2475's proof** once the SO(5)-torus seat is pinned (conclusions unchanged).
- **Keeper — flagged the registry entry protectively (do-not-cite-group-home-externally), filed this containment finding.**

— Keeper, K1657a, 2026-08-17. T2470 sweep first pass: error CONTAINED to the statement line + T2475; the entry caught itself 3 ways (vs §3 arrow; integer charge on SO(2)-singlets; ⅓ from SU(3) color not SO(2)). Derivation sits charge in the SO(5)-internal (color/EW) torus; values + conservation survive; T2471 γ⁵ correctly on the center (spin/double-cover). K-center = time+spin+cover, SO(5)-torus = charge. Surgical fix (2 entries). Protective flag added. Nothing pushed.
