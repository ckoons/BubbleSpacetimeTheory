# PRE-REGISTRATION — DRAFT for Casey's GO (Part B, item 1): the redshift dependence of the matter dipole — "one boost, not two"

**Keeper, 2026-09-14 (Monday) 09:16 EDT (clock). Status: DRAFT. Not armed. Nothing here is a prediction until Cal steers it, Keeper gates it, Casey says GO, and the frozen version is hashed BEFORE any catalogue is opened.** Lineage: Cal's frame-agreement pre-registration of 2026-08-21 (`notes/BST_PREREGISTRATION_frame_agreement_falsifier_Cal_2026-08-21.md`, P1–P3, hatch §5, upgrade path §8); Lyra R143 L3 (the four candidates); Cal §957 (Candidate A ruled); Grace's A9 row (register v0.8, 2026-09-14) with the primary pinned from the PDF.

## 1. The claim, as an ORDER and a STRUCTURE (no knob)
Under the Machian descent the cosmic rest frame is one exterior state recorded through the photon channel; there is no matter channel. So the radiation rest frame $u_\gamma$ (where the CMB has no dipole) and the matter rest frame $u_m$ (where a distant source population has no *kinematic* dipole) are **one boost, not two**: $\varepsilon = $ rapidity$(u_\gamma, u_m) = 0$.

Ellis–Baldwin (1984): a distant isotropic population seen from a frame moving at $\beta$ shows a dipole $D_{\rm kin} = [2 + x(1+\alpha)]\,\beta$, with $x$ the integral source-count slope and $\alpha$ the spectral index, aligned with the velocity. **A kinematic dipole is redshift-independent at fixed $(x,\alpha)$; a clustering (intrinsic) dipole is not** — it is large at $z \lesssim 0.1$ and falls with redshift. That asymmetry is the instrument.

**Prediction P1 (the order statement — the can-fail).** Once the source dipole is measured in redshift bins and the redshift-dependent (intrinsic) component is separated by a method frozen in §4, **the residual redshift-independent component has the CMB boost's amplitude and direction — $\beta = (369.82 \pm 0.11)$ km/s toward $(l,b) = (264.02°, 48.25°)$ (Planck 2018) — in every bin, within the bin's Ellis–Baldwin uncertainty.** Not "some kinematic dipole exists" (that is the cosmological principle's test, Secrest's title); *this* one, at *that* velocity, in *that* direction, at *every* redshift.

**P2 (structure).** The residual intrinsic component, whatever its amplitude, is *not* constrained by the program — it is astrophysics — and P1 is stated so that a large intrinsic dipole does not rescue or condemn it. (This is the 08-21 hatch, §5, turned from an escape into a separated variable.)

## 2. What fires it, and what does not (landings, to be frozen)
- **Landing A — HOLDS:** the redshift-independent component agrees with the CMB boost in amplitude and direction in every bin (tolerance: the per-bin Ellis–Baldwin uncertainty propagated from catalogue counts, $(x,\alpha)$ measured per bin; frozen in §4).
- **Landing B — FIRES (A9's kill condition met):** a redshift-independent component that differs from the CMB boost by more than the frozen tolerance in amplitude *or* direction, in the bins where the intrinsic component has been separated, **and survives the hatch** — no astrophysical account (catalogue systematics, Galactic-plane masking, flux-limit effects, Malmquist-type biases) surviving the frozen checks of §4. That is "two boosts," and it falsifies the Machian descent.
- **Landing C — NOT DECIDABLE:** the intrinsic and kinematic components cannot be separated at the catalogue's depth (the separation method of §4 returns a degenerate fit). Reported as such; the row stays A9-live; the next catalogue is named.
- **Does NOT fire:** a large total dipole amplitude (Secrest's 5.1σ — that is the intrinsic component and the cosmological principle); an angle alone; a single-bin discrepancy without the hatch checks.

## 3. Current state (from the primary, Grace's row): the hatch is open in the data
Secrest et al. 2022 (ApJL 937 L31): NVSS $D = (1.23 \pm 0.25)\times10^{-2}$, ~3× kinematic, 45° off (95% CL 30°); CatWISE $D = (1.48 \pm 0.16)\times10^{-2}$, ~2×, 26° off (95% CL 15°); joint 5.1σ against purely kinematic; residual after subtracting the kinematic expectation $D = (0.86 \pm 0.14)\times10^{-2}$ at 48° from the CMB dipole, read by the authors as intrinsic. Darling 2022 (VLASS/RACS) reports consistency with the kinematic expectation; Secrest §3 contests the method. **So the present data neither confirm nor refute P1; they are Landing C by construction, and the authors themselves name the redshift dependence as the decider.**

## 4. The frozen procedure (to be completed and hashed before any catalogue is opened — a bar with an unfrozen procedure is a tuning channel)
1. **Catalogues named now:** CatWISE2020 quasars with redshifts where available; Quaia (Gaia–unWISE quasar catalogue with spectrophotometric redshifts); NVSS/RACS radio with cross-matched redshifts; each with its published mask. No catalogue opened before the hash.
2. **Bins fixed now:** redshift bins with edges committed before counting; minimum counts per bin committed.
3. **Per-bin $(x,\alpha)$** measured from the catalogue's own counts and spectra by the published Ellis–Baldwin prescription; not adjusted after the dipole is seen.
4. **The separation method fixed now:** the intrinsic component modelled as the redshift-dependent part (frozen functional form), the kinematic as the redshift-independent part; the fit's degeneracy test frozen (Landing C criterion).
5. **The hatch checks fixed now (§5 of the 08-21 file, carried):** the named systematics and the test each must pass; a discrepancy that fails any check is "not surviving the hatch," not a fire.
6. **Tolerance fixed now:** per-bin propagated uncertainty; the direction tolerance as the 95% positional uncertainty of the bin's dipole.
7. **Blind split:** Elie computes per-bin dipoles with the CMB target withheld; Grace holds the target; Keeper compares; Cal cold-reads the comparison. The comparison's code is retained with the run.

## 5. Roles, and what each must produce before GO
- **Lyra:** the ROW candidate — P1 as a registry statement with T2564/K1522/T2565 and Cal §957 as its inputs; the sentence that says why a kinematic dipole must be the CMB's under the descent (one exterior, photon channel only). If the rows license less than P1, say so and P1 narrows.
- **Elie:** the instrument — an Ellis–Baldwin per-bin dipole estimator on a public catalogue, validated on a synthetic isotropic population boosted at a known velocity (positive control: recovers the injected $\beta$ and direction in every bin) and on a synthetic clustering dipole (negative control: the separation returns redshift dependence). `/toy claim` before writing.
- **Grace:** the A9 row gains "PREREGISTERED PREDICTION P1 (hash …)" when armed; the catalogue versions and masks pinned to their DOIs.
- **Cal:** steering — the landings, tolerances and hatch checks are his to freeze; his §957 map is the ruling this rests on.
- **Keeper:** the gate — verifies the hash matches the frozen file before a catalogue is opened; certifies the landing after.
- **Casey:** GO, and the one choice that is his: which catalogue is opened first.

## 6. Why this is the Part B opener
It is the first new laboratory exposure the program has produced since the first-row-unitarity statement; it fell out of Sunday's honesty about $\varepsilon$; the data to decide it either exist (Quaia, CatWISE) or are scheduled (DESI, Euclid); and it is stated as an order, not a value, so there is no knob. It could be wrong by the end of the year. That is what we want.

— Keeper. DRAFT for Casey's GO; nothing armed.
