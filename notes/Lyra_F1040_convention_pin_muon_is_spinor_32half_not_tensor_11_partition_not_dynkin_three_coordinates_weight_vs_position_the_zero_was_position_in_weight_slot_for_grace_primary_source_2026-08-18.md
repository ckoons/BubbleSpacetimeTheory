# F1040 — The convention pin that unblocks the mass tower: the muon is the SPINOR (3/2,1/2), not the tensor (1,1); the FK labels are PARTITIONS, not Dynkin; and there are THREE distinct coordinates that were colliding. Elie's "zero FK norm at ν=3/2" was the *radial position* ν=3/2 mis-used in the *Bergman weight* slot, on a *two-row tensor* label — three wrong choices at once. Fix all three and the norm is nonzero. Bare Pochhammer is still not the mass map (F323); the map is the overlap / HC formal degree.

**Lyra + Grace, Tuesday 2026-08-18, Round 9. Pinning partition-vs-Dynkin + the muon's ν before any norm is computed (Casey's convention-collision-before-contradiction standing order; "don't compute norms on an ambiguous coordinate — caught five times this week"). Reconnected: F323 (my FK-computed Pochhammer formula), F839/T2517 (the lepton positions), F1039 (K∘D, muon=D-image (3/2,1/2)), Ribbon paper + T2513 (mass map, quark ν). Verified arithmetic below. LA on D_IV⁵. Nothing pushed; CP existence-only.**

## The collision, diagnosed (three coordinates, all conflated in "(1,1) at ν=3/2")
Elie correctly stopped: the muon slot "(1,1)" has zero FK norm at "ν=3/2." That is a **triple convention collision**, not a physical zero:

**(A) LABEL — partition, not Dynkin; and the muon is a SPINOR.** The FK generalized Pochhammer uses **partition/orthogonal signatures (m₁,m₂)**, m₁≥m₂≥0 (F323, computed from the FK cone):
$$(\nu)_{(m_1,m_2)} = (\nu)_{m_1}\,(\nu - a/2)_{m_2},\qquad a = n_C-2 = 3.$$
The three charged leptons sit at the **spinor** K-types **(k+½, ½), k=0,1,2** → electron (½,½), **muon (3/2,1/2)**, tau (5/2,1/2) (F323; = the D-images of F1039's K∘D). The ledger's "(1,1)" is the **pre-D tensor address** (the FK-kernel slot *before* the Dirac map); the physical fermion is the **spinor (3/2,1/2)**. Compute the norm on the spinor, never on the raw tensor (1,1). (This is what K∘D means operationally: apply D first, then the FK norm.)

**(B) WEIGHT vs POSITION — two different ν's.** There are two ν's and they must not touch:
- the **Bergman weight** ν (the Pochhammer parameter) — a *fixed* number for the sector;
- the **radial position** ν ∈ {5/2, 3/2, 0} (the discrete-series / Wallach address; the muon sits at ρ₂ = 3/2, F839/T2517) — *where the mode sits*, **not** the weight.

**Elie's zero is the position (3/2) plugged into the weight slot.** Verified:
$$(\nu)_{(1,1)}\big|_{\nu=3/2} = (3/2)_1\,(3/2 - 3/2)_1 = (3/2)\cdot(0)_1 = \mathbf 0,$$
and it *persists even with the spinor label* while ν=3/2 is used as the weight (the factor (ν−a/2) = 0 at ν=3/2). Put the correct Bergman weight in and it is nonzero:
$$(\nu)_{(3/2,1/2)}\big|_{\nu=5} = (5)_{3/2}\,(7/2)_{1/2} \neq 0.$$

**(C) The mass map is NOT the bare Pochhammer anyway (F323, banked).** At fixed weight ν, all three modes share the same Gindikin Γ_Ω(ν), which cancels in ratios, so the bare-norm ratios (5.5, 35.75) can carry no π and miss the targets. **The depth→mass map is the localization-overlap integral** (electron-at-origin, N(w)^{n_C/2}, where π enters from the volume measure) — equivalently the **Harish-Chandra formal degree d(ν)**, not the bare FK residue (Ribbon paper: muon = (24/π²)^{C₂}). So even after (A)+(B), the run computes the *overlap / HC degree* on the correct address, not the bare Pochhammer.

## Answers to the two pinned questions
- **Partition or Dynkin?** **Partition** (orthogonal signature (m₁,m₂)), formula (ν)_{m₁}(ν−a/2)_{m₂}, a=3. Not Dynkin. (Dynkin [1,1] would read (3/2,1/2) directly — coincidentally the spinor — but the FK object is defined on partitions; use partitions to avoid the trap.)
- **Is the muon at ν=3/2?** **Yes as a radial POSITION** (ρ₂ = the Cartan-slice / discrete-continuum edge, F839/T2517). **No as the Bergman weight.** The zero came from confusing the two; the muon's K-type is the spinor (3/2,1/2), its position is ν=3/2, and the Pochhammer *weight* is the sector's fixed ν (see the open item).

## The one open item — for Grace, from the primary source
The **Bergman weight ν for the spinor (Di) lepton sector** is the single thing not yet pinned from primary source, and the corpus carries **two competing values**:
- **quarks:** ν = N_c = 3 (the Wallach threshold, T2513, banked for down d:s:b=1:20:840);
- **leptons:** ν = genus = 5 (F323).
These differ because quarks are colored (confined → interior lowest rung, ν=N_c) and leptons are colorless — but that is a *mechanism claim*, not a pinned convention. **@Grace: pin the Di-spinor Bergman weight from the primary source (Faraut–Korányi weighted-Bergman parameter for the spinor bundle, cross-checked against Fernando–Günaydin's Di normalization) — is it genus=5, the Wallach N_c=3, or the FG Di value?** That one number closes coordinate (B) for the leptons. Do not choose it to fit; read it from the book.

## What Elie's rung run needs (now one short computation)
On the pinned coordinates: **K-type = spinor (m₁,m₂) = (k+½,½)** [muon (3/2,1/2)]; **weight ν = the Grace-pinned Di value** (5 or 3); **map = the overlap integral / HC formal degree d(ν)**, not the bare Pochhammer; **position ν∈{5/2,3/2,0} labels which mode, kept separate from the weight.** With those fixed, the (k,m) rung run is target-innocent and short. The muon's zero disappears the moment the weight ≠ position.

## Tier
- **Pinned firmly (F323 + F1039, verified):** partition labels; muon = spinor (3/2,1/2) not tensor (1,1); the weight/position distinction; the zero = position-in-weight-slot; bare-norm ≠ mass map.
- **Open (one number, Grace, primary source):** the Di-spinor Bergman weight (genus 5 vs Wallach 3). Named, not guessed.

## Handoffs
- **@Elie** — do NOT compute norms until (B) is pinned. The label is (3/2,1/2) spinor (partition), the map is the overlap/HC-degree not the bare Pochhammer, and the weight is Grace's one open number. Your stop was correct — it was a coordinate collision, not a dead end.
- **@Grace** — the one primary-source pin: the Di-spinor Bergman weight ν (genus 5 / Wallach 3 / FG value). Read it from FK + Fernando–Günaydin, don't fit it. That closes the coordinate and Elie's run is one computation.
- **@Keeper** — convention pinned before the norm (the standing order honored). The muon is the spinor (3/2,1/2); "(1,1)" is the pre-D tensor slot; the zero was a triple collision (partition/spinor + weight-vs-position + bare-norm), all diagnosed. One number (the Di weight) stays open, flagged for primary source, not guessed.
- **@Casey** — this is the "pin the ruler before you measure" catch you've drilled into us. Elie hit a zero and, correctly, stopped instead of computing through it. The zero wasn't physics — it was three coordinates wearing the same name: the muon's *label* (it's a spinor, not the tensor the ledger wrote), its *position* on the domain (ν=3/2, real), and the *weight* of the measuring integral (a fixed number, 5 or 3, NOT 3/2). Someone had put the position into the weight's slot, and the arithmetic dutifully returned zero. Fix the three and it's a clean nonzero number — and there's exactly one thing left to read from the book (which weight the leptons take), which Grace is doing. Then the mass-tower run is short.

Notes only; no theorem/toy/mass claimed (convention pin unblocking the rung run). F1040: Elie's "zero FK norm, muon (1,1) at ν=3/2" = TRIPLE convention collision. (A) LABEL: FK uses PARTITION (m₁,m₂), (ν)_{m₁}(ν−a/2)_{m₂}, a=3; muon = SPINOR (3/2,1/2) [F323 (k+½,½); = F1039 D-image], NOT tensor (1,1) [that's the pre-D slot]. (B) WEIGHT vs POSITION: Bergman weight ν (fixed) ≠ radial position ν∈{5/2,3/2,0} (muon at ρ₂=3/2). Zero = position 3/2 in weight slot: (3/2)_1·(0)_1=0; persists w/ spinor label at weight 3/2; nonzero at weight ν=5. (C) bare Pochhammer ≠ mass map (F323): map = overlap integral / HC formal degree d(ν), π from volume. Muon IS at ν=3/2 as POSITION, NOT as weight. OPEN (Grace, primary source): Di-spinor Bergman weight = genus 5 (F323 leptons) vs Wallach N_c=3 (T2513 quarks) vs FG Di value — read from FK+Fernando-Günaydin, don't fit. Then Elie's run is one short computation on pinned coords. — Lyra
