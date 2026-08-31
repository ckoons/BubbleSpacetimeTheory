---
title: "K1714 SUPPLEMENT — scope correction, plus a Casey/Keeper excursion on the mass gap, windings, and emission (handoff for Fable)"
author: "Keeper"
date: "2026-08-29, written 15:01, extended 15:26 EDT"
status: "SCOPE SUPPLEMENT to K1714 + session handoff. Amends K1714's reach, not its verdict. No new K-number: an audit about a previous audit amends it. Sections 3-6 are CONJECTURE and are marked as such."
---

# K1714 SUPPLEMENT — scope, and a handoff

**For Fable.** Saturday-morning excursion, Casey and Keeper, no other CIs. Read Section 0 first —
it is the part that saves time. Nothing here is banked except where a citation says so.

---

## 0. CLOSED ROUTES — do not spend time here

Four dead ends, three of them found by walking into them.

1. **The pair is NOT the projector and its complement.** F44 Reading (a) is registered: everything
   physical lives in H², there is no physical (1−P) complement, and treating it otherwise
   **double-counts**. Cited in `BST_AC_Theorem_Registry.md:10918,10925` and
   `Elie_Vol16_Chapter4...v0_8.md:58`.
2. **The pair is NOT a CPT mirror.** Positive-time ontology excludes it — *"CPT-mirror /
   antiuniverse excluded"*, *"the arrow is intrinsic, not a geometric reflection."*
   **But note the near-miss:** n ↦ −n on a winding is a topological operation, NOT time reversal.
   The CPT ruling does not reach the antiparticle-as-reversed-winding route. I nearly killed a live
   route with a ruling aimed at a different object.
3. **The mass/momentum split is NOT an angle in a\*.** Setting tan θ = N_c/n_C from ρ gives O(1)
   quantities against a target of 1836. Fails on **shape**, not arithmetic — an angle cannot reach
   10³. Recorded as a negative rather than adjusted until it fit.
4. **The Shilov boundary has NO Z₂ quotient.** It is S⁴ × S¹ — 107 occurrences, none with a
   quotient. My memory said S⁴ × S¹/Z₂ and I was about to offer that Z₂ as the pair-splitting
   mechanism. It does not exist.

---

## 1. THE SCOPE CORRECTION (the reason this file exists)

**K1714 ruled that a compact-boundary gap is Kaluza-Klein rather than Clay. That ruling is about
MOMENTUM (Laplacian) modes. It does NOT reach WINDING modes, which scale oppositely. I invoked it
against a winding picture twice and both invocations were aimed at the wrong object.** K1714's
verdict stands where it applies.

| | form | gap | R → ∞ | character |
|---|---|---|---|---|
| **Momentum / KK** | Laplacian eigenvalues, E_n = n/R | ~1/R | → 0 | kinematic |
| **Winding** | wraps w times, E_w = w·(circumference)·T | ~R·T | → ∞ | not kinematic |

`BST_YM_AC_Proof.md` argues its gap from *"the Laplacian Δ has discrete spectrum because the
quotient is compact"* — momentum sector, correctly killed.

**Decisive test for any future argument: decompactification scaling.** Grow R. Falls as 1/R ⟹
momentum ⟹ K1714 applies. Rises with R ⟹ winding ⟹ it does not. A computation, not a judgment.

**Separately — a live propagation gap, recorded not fixed:** `BST_YM_AC_Proof.md` contains **zero**
references to K1714. The ruling never swept into the flagship YM document, which still argues from
compactness with no caveat.

**Also distinguish:** the KK *dictionary* (momentum in an extra dimension ↔ charge below) is a
correspondence between quantum numbers and is untouched by K1714, which killed a *gap*. Using the
dictionary does not resurrect the ruled-out object.

---

## 2. BANKED FACTS, LOCATED (so nobody re-greps)

- **T1922** (SP-26 founding theorem, Casey-named, formalized 2026-05-16, Proved):
  Closed cycles on D_IV⁵ ↔ particles. Open cycles ↔ confined constituents (quarks, gluons).
  **Binding energy = winding slack.** proton = C_2 = 6 winding segments (3 quarks + 3 gluons).
  8 gluons = c_2 − N_c. glueball = pure-slack closed winding, m_g = (c_2/C_2)·m_p = (11/6)·m_p.
- **`BST_Paper84_Observer_Companion_Draft.md:45-48`** — integer windings on S¹ = bound states = the
  SM particles; non-integer winding = incomplete closure = continuous spectrum; the paper claims
  dark matter IS the continuous spectrum.
- **`BST_RealityBudget_SpectralProof.md:308-311`** — S¹ **circumference is π in Bergman coordinates,
  not 2π**, hence **R = 1/2 = 1/rank**; only **1/π** of the circumference is committed at any
  instant; f = N_c/(n_C·π) = 3/(5π).
- **String tension** — σ = *"Bergman embedding cost per unit Z₃ circuit length"*, √σ = m_p/√n_C.
- **K204 (PASS, Helgason 1962)** — κ_Bergman = −n_C = −5, closed form.
- **ρ(D_IV⁵) = (5/2, 3/2)**, |ρ|² = 17/2; spectral parameter in a\* ≅ R².

---

## 3. COMPUTED THIS SESSION — with calibration attached

**Keep each number with its caveat in the same sentence. Detached, both of these over-claim.**

**String tension.** √σ = 6π⁵·m_e/√n_C = **419.60 MeV**, σ = 0.176 GeV², using only m_e and BST
integers — **no QCD input at all.** *Calibration:* the lattice value is scheme-dependent — 420 MeV
on one scale-setting, 440 on another, 465 in some quenched schemes. Our value sits 0.1% from the
first, 4.6% from the second, 9.8% from the third. **The spread in the target is an order of
magnitude larger than the agreement with any one value of it.** Honest statement: *lands inside the
lattice range with zero free parameters.* Consistent, not discriminating. **Anyone quoting "0.1%"
is quoting a coincidence of scheme choice.**

**Glueball.** T1922 gives m_g = (11/6)·m_p = **1720.2 MeV**; f₀(1710) sits at 1704 → 0.95%.
*Calibration:* target-innocent (11/6 from banked integers, nobody tuned it) and it is the cleanest
possible test of binding-energy-as-slack, since a glueball is pure slack with no quark content. But
0.95% is I-tier by our own standards, the lattice window (~1650–1730) is broad, and the
identification is contested — f₀(1710) may be mostly ss̄, and recent work splits f₀(1770). Against
f₀(1500) the prediction is off 14%. **Falsifiable: if the scalar glueball is pinned well away from
~1700, the pure-slack reading fails.**

---

## 4. CASEY'S PICTURE — CONJECTURE, 2026-08-29

Recorded for provenance. **Not a result. Do not quote as one.**

Mass is the closed 2D circulation (rest mass); momentum is manufactured at emission through the
Shilov boundary. Curvature torques the winding so each loop precesses, and the precession traces the
third dimension. A kick imparts energy to the *binding* rather than liberating the constituent —
which is confinement stated as an energy budget, and matches QCD flux-tube behaviour. The boundary
deforms with the continuum's temperature, connecting to the thermostat/Λ fixed-point work.

**The one exact thing under it:** precession by curvature **is holonomy**, θ = κ·A, with closure
n = 2π/(|κ|·A). Not a metaphor. κ = −5 is banked, so the enclosed area A is the only unknown.

**Helix reading:** one turn of a helix has arc length √(circumference² + pitch²). If circulation is
mc² and pitch is pc, then E² = (mc²)² + (pc)² is the **arc-length identity**, i.e. a geometric
theorem rather than a postulate. *Whether this is a derivation or a narration onto a known answer is
exactly what needs deciding — see Section 5.*

**Frame note:** momentum's *value* is relational; its *form* is geometric. There is no frame problem
once the substrate is the bath frame — the pitch is the substrate-frame momentum and other observers
see it boosted. Keeper raised a frame objection here and withdrew it; it was aimed at the value while
the picture concerns the form.

---

## 5. OPEN — stated as computations, each able to fail

1. **Does the holonomy angular momentum equal the emitted particle's spin?** Compute L from
   θ = κ·A and compare. If equal, real. If not, the difference is a boundary recoil — also
   checkable, and it predicts pairing. *Note the constraint: angular and linear momentum are
   separately conserved. Precession cannot BECOME linear momentum; both must be produced and each
   balanced. Consequence: emission cannot yield a single particle in isolation — it needs a recoil
   or a pair. This is a second, independent reason for what confinement already gives.*
2. **Does E² = (mc²)² + (pc)² fall out, or is it narrated?** A form that fits any target is a
   reparameterization. This is the load-bearing question for Section 4.
3. **Name the fundamental 2D cell.** The winding-energy route needs a tension T; the
   precession-closure route needs an area A. Both are the same kind of object. Fix it and both close
   with zero free parameters; fail to and both are open on the identical gap. Casey's reading:
   T is not an input but the force required for a loop committing 1/π of the circumference to close
   in 3D. Section 2's σ = "Bergman embedding cost per unit Z₃ circuit length" may already be it.
4. **Which spin?** Intrinsic spin is falsified immediately — the pion is spin-0 and carries
   momentum. Imparted/orbital angular momentum survives and owes an operator.
5. **The manufactured direction must be non-compact while S¹ stays compact.** KK momentum is
   quantized in units 1/R = rank; observed momentum is continuous. Consistent, but a *requirement*
   of the picture rather than a free choice, and it should be written down as one.
6. **The thermostat owes a bandwidth.** A regulator that holds everything constant predicts nothing.
   Name one quantity it fails to hold, or one rate at which it loses tracking. The Λ paper's title
   already admits one named obstacle — determine whether that obstacle and the bandwidth are the
   same thing.

**Live candidates for the pair mechanism** (both survive Section 0): the **double cover**
Spin(5,2) → SO(5,2) is 2:1 — which says neither "the boundary splits" nor "the interior generates
two", but that the object was always double-valued and emission is where the sheets become
distinguishable; and it is the same structure that makes half-integer spin unsurprising, so one
mechanism yields two results. And the **winding involution n ↦ −n** in π₁ = ℤ, giving net-zero
pairs — charge conservation stated topologically.

---

## 6. KEEPER'S CALIBRATION FOR THIS SESSION

Structuring held; **every outcome prediction was wrong.** Weight accordingly.

- **Wrong:** predicted the winding gap scales as 1/R. Inverted — that is the momentum sector.
- **Wrong twice:** invoked K1714 against windings (Section 1).
- **Wrong:** asserted a Z₂ in the Shilov boundary from memory. It does not exist (Section 0.4).
- **Clean negative:** the angle reading (Section 0.3), reported rather than adjusted.
- **Withdrawn:** the frame objection to momentum (Section 4).
- **Noted against myself:** on reading that n_C = 5 counts "available channels" and that 1/π is the
  committed fraction, I immediately saw a path to π⁵ and hence to 6π⁵ = m_p/m_e. **That is worthless
  as evidence** — I already knew the target, and a narrative that reaches a number you already have
  is the cheapest thing there is. Recorded so it does not travel as an argument.

*Three of four instincts this session came from memory and two were wrong. The two that held were
the ones checked against the corpus first.*

— Keeper, 2026-08-29

---

## 7. CAPTURE ADDENDUM — the energy-budget question (Casey, Sunday 2026-08-30, 09:44 EDT)

**Provenance: direct Casey/Keeper conversation, Sunday morning, appended on Casey's word. Amends this
supplement; no new K-number. Everything below Section 7.1 is grounded in banked corpus objects;
Section 7.2's identification is CONJECTURE-tier until computed.**

**7.0 Casey's question.** Is the winding energy the FULL energy the D_IV⁵ interior supplies to the
Shilov boundary? Casey's suspicion: no — there is slack even on the interior, and other forms of
energy transit/are emitted from the boundary besides EM.

**7.1 The corpus already commits to "no," in three independent places.**
1. **The continuous spectrum is a non-winding channel.** Paper84 (Section 2 above): integer windings
   = bound states = SM particles; NON-integer winding = incomplete closure = continuous spectrum,
   claimed to BE dark matter. If that energy is real, the integer-winding ledger (T1922) is by
   construction not the whole budget.
2. **The committed fraction is banked as less than 1.** Only 1/π of the S¹ circumference is committed
   at any instant (Section 2; f = 3/(5π) ≈ 19.1%) — structural interior slack prior to any particle
   physics, on top of T1922's binding-slack inside bound systems.
3. **The boundary has structure the winding ledger cannot see.** Shilov = S⁴ × S¹ (and nothing else —
   Section 0.4). Winding lives on the S¹ factor only; the S⁴ factor carries angular structure with no
   winding entry. Separately, F66 splits the transit geometry: EM = conformal SO(4,2) boundary,
   gravity = SO(5,2)/SO(4,2) coset bulk — at least two distinct channels before the continuous
   spectrum is counted. Either the S⁴ sector is energetically silent (itself a claim owing a proof)
   or winding energy is not the full account.

**7.2 The convergence worth naming (CONJECTURE).** The corpus already routes the committed fraction
into Ω_m = 6/19 with Ω_Λ = 13/19 as complement. At cosmological scale, Casey's question may literally
BE the Ω_m/Ω_Λ split: committed windings as the matter side, uncommitted/slack as the
thermostat/Λ side (which Section 4 already connects to boundary temperature). Not a result; a
target for C1.

**7.3 Pre-registered checks (each can fail).**
- **C1:** derive (or fail to derive) the 6/19 vs 13/19 budget split as committed-winding vs slack
  from the banked objects alone — pre-register the route before computing.
- **C2:** grep sweep — does ANY banked object assign energy flux to the S⁴ factor of the Shilov
  boundary? A clean null is itself an answer (the winding ledger would then carry the S¹ sector
  alone, with the S⁴ silence needing a mechanism).
- **C3 (audit flag, reconciliation-by-scope-sweep class):** the corpus appears to carry TWO dark-
  matter stories — Paper84's "DM = continuous spectrum of incomplete closures" and the older
  "DM = Wallach shadow (16/3 at 0.2%)." Two mechanisms, one observable. Grep for an existing
  reconciliation BEFORE treating it as a collision; if none exists, it is one.

— Keeper, 2026-08-30, 09:44 EDT
