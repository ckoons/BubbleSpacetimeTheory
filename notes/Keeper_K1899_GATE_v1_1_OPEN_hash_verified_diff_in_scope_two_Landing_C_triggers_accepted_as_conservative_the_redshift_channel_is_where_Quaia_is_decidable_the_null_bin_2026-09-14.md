# K1899 — THE GATE on v1.1: OPEN. Hash verified; the diff in scope; the two added Landing-C triggers accepted as conservative; the redshift channel is where Quaia is decidable; the null bin.
**Keeper, 2026-09-14 11:04 EDT (clock, substituted).**

## 1. Gate (instrument `play/keeper_partB_gate.py`, three checks): OPEN
HASH OK — 92a7ebb3… computed from the file, equal to the posted hash. NO-CATALOGUE OK — zero catalogue-like files in the tree, none before the freeze, none over 5 MB. CONTROLS-BLIND OK — Elie's 5758 carries its prereg hash before its SCORE line. **A catalogue may be opened on Casey's word.**

## 2. Diff audit (instrument `play/keeper_partB_diff_audit.py`, per changed line): IN SCOPE, with two rulings
Twenty-seven changed regions; after the front-matter exemption, zero outside K1898 §6 + Cal's declared §9. The instrument's first run flagged the $f_i = 2 + x_i(1+\alpha_i) + B_i$ line and §4.4 as out of scope — a keyword gap ($B_i$, "boundary term"), fixed; the self-test still passes. Rulings on what §9 declares beyond K1898 §6:
- **§2.2 mask and §2.3 weights (executability corrections): ACCEPTED.** Quaia ships no mask; a mask v1 left undeclared is not a tolerance but an omission, and the frozen cut (|b| > 30°, LMC 5°, SMC 3°, the radii Elie's controls already use) is now stated before any catalogue. The per-bin selection functions from the released code (Grace's commit pin 92eca506) likewise.
- **§4.4's two added Landing-C triggers: ACCEPTED as conservative.** Both only add routes to "not decidable" (the sharp/smooth boundary terms disagreeing beyond σ(B_i); the two channels disagreeing, C′). Neither can manufacture A or B. A trigger that can only say "we could not tell" tightens the test.
- **§4.5, the redshift channel as P3 ruled (Cal §965): item (6), in scope.** Landing A′ requires both channels to agree in amplitude (2σ combined) and direction (each inside the other's 95% region); C′ routes P1 to C. The channel can veto an A and cannot manufacture one — the right asymmetry.

## 3. Own, recorded: the envelope was an order of magnitude low at the bin ends
K1898 §2's "≈ 0.2%" for the boundary term is replaced (amended in place, 11:03) by Elie's measured T/f = +1.16, +0.26, −0.12, −0.41, −1.01 (5758): order one at the ends, sign-changing, and vanishing in the top bin. My envelope treated the edge term as a perturbation of a flat n(z); the instrument on the actual dN/dz is the number. Cal read the paper; I read the abstract. Same lesson as Friday's.

## 4. Power: the number-count route on Quaia alone is Landing C as frozen; the redshift channel is where Quaia is decidable
Elie: σ_β c = 443 km/s on counts at Quaia depth under the v1.1 mask, against the C threshold 185 — not decidable by counts alone. **Keeper's envelope for the redshift channel, for Elie's E2 control to confirm or refute:** the dipole of the mean observed redshift in a bin has signal (1+z̄)β ≈ 0.0017–0.0047 and noise set by the bin's own width in z (σ_z,bin ≈ 0.15–0.25, not the photometric error) over ~2.6×10⁵ sources per bin — S/N ≈ 3–7 per bin, i.e. **σ_v ≈ 55–110 km/s per bin**, comparable to Wu–Xia's DESI DR1 ±50. If that holds on synthetic Quaia, the joint redshift channel is decidable at the 2σ-of-β_CMB bar and Landing A′/C′ does the deciding. The count channel remains the independent-systematics leg; the redshift channel is the power.

## 5. The null bin — a door, for Cal's v1.2 scope, not this freeze
Elie's top bin [2.4, ∞) has f + T ≈ 0: the observed-z-selected *kinematic* dipole vanishes there by construction (a steeply falling n(z) cancels aberration+flux against the redshift boost). A bin with no kinematic lever arm is a **kinematic null** — any dipole measured in it is intrinsic (or systematic). That is not a defect; it is a calibrator: the null bin's dipole measures the intrinsic component at high z with no boost contamination, and it can fix the profile amplitude that Landing C's third trigger worries about — from the data, with no new knob, because the bin and the cancellation are frozen from dN/dz. In the corpus's terms (Lyra's note): it is the bin where the Rac density's ℓ = 1 *kinematic* moment lies in the kernel, so what remains is the Rac factor's own anisotropy. Proposed as control S5 (synthetic: a boosted sky with an injected intrinsic dipole; the null bin must return the intrinsic one alone) and as a frozen use in v1.2 if Cal admits it. Declared here so a v1.2 is scoped before it is opened.

## 6. Small executability item for v1.2 (Grace's flag, 10:50)
v1.1 §3.4 must name Quaia's σ_z column as the paper's Table 2 has it — `redshift_quaia_err` — not the two names my Round 146 prompt carried from a summary; and the first opening records the FITS header verbatim. Cal's v1.2 scope: this line, the null bin (§5), nothing else.

— Keeper. K1899. Counter next: K1900.
