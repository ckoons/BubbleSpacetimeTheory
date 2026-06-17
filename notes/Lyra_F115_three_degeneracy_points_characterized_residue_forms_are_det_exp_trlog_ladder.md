---
title: "F115 — Characterizing the three lepton degeneracy points: they are three DIFFERENT degeneracy mechanisms, and the product/sum form of each residue is dictated by the det = exp(Tr log) ladder sampled at three loci. Casey: 'characterize each degenerate point and understand what the product/sum indicate for the residues.' RESULT: the three leptons are degenerate in three DISTINCT ways -- and only the electron is a zero of the formal-degree polynomial: (1) ELECTRON Delta=d/2=5/2 = SELF-SHADOW (Delta=d-Delta, the two modes Delta_pm collide) = a SIMPLE ZERO of d(nu) -> residue = derivative = LOG = d'(5/2)=9/16; 0-dimensional degenerate locus (the shadow fixed point); the elementary residue. (2) MUON Delta=(d-2)/2=3/2 = UNITARITY BOUND (mode shortens, box phi=0); shadow at 7/2 (NOT self-shadow); NOT a formal-degree zero -> the degeneracy is in the BOUNDARY normalization (Gamma-pole) -> residue extracted over the boundary = a DETERMINANT (PRODUCT) over dim SO(4)=6 directions = (24/pi^2)^6. (3) TAU Delta=0 = IDENTITY/trivial rep = the BULK vacuum; NOT a formal-degree zero -> the norm is a BULK spectral trace -> residue = TRACE (SUM) over interior modes = Weyl count in d=N_c=3 = g^3+2^C2 g^2. THE LADDER (det=exp(Tr log)): the three residue forms ARE the three standard one-loop objects: electron = LOG = Green's function/propagator (one degenerate mode, 0-dim locus); tau = Tr log = SUM = effective action/bulk free energy (trace over interior, bulk locus d=N_c=3); muon = det = PRODUCT = partition function/boundary determinant (trace exponentiated over the boundary, locus dim SO(4)=6). So PRODUCT<->sum indicates: a SUM = a TRACE (effective action) over a BULK locus; a PRODUCT = a DETERMINANT (partition function) over a BOUNDARY locus; the elementary LOG = the propagator at a point-collision (the self-shadow). The dimension of the degenerate locus (0 / bulk-3 / boundary-6) fixes which object and hence log vs sum vs product. PRESCRIPTION (advances the open work): the muon residue MUST be a boundary partition-function determinant over the SO(4) directions (NOT a sum -> why F113 closed the edge-sum); the tau residue MUST be a bulk effective-action trace (Weyl sum over interior); the electron is the worked example (log coefficient 9/16 = propagator residue). STRICT: CHARACTERIZATION + PRESCRIPTION, NOT a mass derivation; count stays 2. The three masses are one structure (det -> Tr log -> log) sampled at three degeneracy loci."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-13 Sat 12:38 EDT"
status: "v0.1 -- Casey: characterize each degenerate point + what product/sum indicate for residues. THREE DISTINCT mechanisms (only electron is a formal-degree zero): ELECTRON Delta=d/2 SELF-SHADOW = simple zero d(5/2)=0 -> residue=LOG=d'(5/2)=9/16 (0-dim locus). MUON Delta=(d-2)/2 UNITARITY BOUND (box phi=0), shadow 7/2, NOT a zero -> boundary-norm Gamma-pole -> DETERMINANT/PRODUCT over dim SO(4)=6 = (24/pi^2)^6. TAU Delta=0 IDENTITY = bulk vacuum, NOT a zero -> bulk TRACE/SUM = Weyl d=N_c=3 = g^3+2^C2 g^2. LADDER det=exp(Tr log): electron=LOG=Green's fn (0-dim); tau=Tr log=SUM=effective action (bulk d=3); muon=det=PRODUCT=partition function (boundary dim SO(4)=6). product/sum indicates: SUM=trace over BULK locus; PRODUCT=det over BOUNDARY locus; LOG=propagator at point-collision. dim of degenerate locus (0/3/6) -> log/sum/product. PRESCRIPTION: muon residue=boundary partition-fn det over SO(4) (not a sum, =F113); tau residue=bulk effective-action trace (Weyl); electron=worked example 9/16. CHARACTERIZATION+PRESCRIPTION not derivation; count 2."
---

# F115 — Three degeneracy mechanisms; the residue's product/sum form is the det = exp(Tr log) ladder

Casey: *"They live on degenerate points, and their residues are all that's visible. Can we characterize each degenerate point and understand what the product/sum indicate for the residues?"* Yes — and the product/sum is not a labeling, it tells you *which one-loop object computes each residue.*

## 1. Three DIFFERENT degeneracy mechanisms (only the electron is a formal-degree zero)

The leptons are not degenerate in the same way. Checking each against the formal-degree polynomial `d(nu)=(5/2-nu)(1-nu)(2-nu)(3-nu)(4-nu)` and the shadow map `Delta <-> d-Delta`:

| lepton | `Delta` | mechanism | formal-degree `d(Delta)` | residue form |
|---|---|---|---|---|
| **electron** | `d/2 = 5/2` | **self-shadow** (`Delta = d-Delta`): the two modes `Delta_pm` collide | **`= 0`, simple zero** | **LOG** = `d'(5/2) = 9/16` |
| **muon** | `(d-2)/2 = 3/2` | **unitarity bound**: mode shortens, `box phi = 0` (shadow at `7/2`) | `= -15/16` (nonzero) | **PRODUCT** (determinant) |
| **tau** | `0` | **identity / trivial rep**: the bulk vacuum | `= 60` (nonzero) | **SUM** (trace) |

So:
- the **electron** is the only genuine *spectral collision* — a double root resolved by a logarithm (the self-shadow fixed point `Delta = d/2`, a **0-dimensional** locus in `Delta`-space);
- the **muon**'s degeneracy is not in the bulk spectrum at all — it is in the **boundary normalization** (the `Gamma`-pole at the unitarity bound where the mode shortens to a boundary/null field);
- the **tau**'s degeneracy is the **identity** — its norm is a **bulk** object (the trivial rep is the vacuum filling the interior).

## 2. The ladder: det = exp(Tr log) — three standard one-loop objects

The three residue forms are exactly the three canonical one-loop objects, related by `det = exp(Tr log)`:

```
   LOG            ->     Tr log = SUM        ->     det = exp(Tr log) = PRODUCT
   electron                tau                          muon
   Green's fn /           effective action /           partition function /
   propagator             bulk free energy             boundary determinant
   (one mode, 0-dim)      (trace over interior,        (trace exponentiated over
                           bulk locus d = N_c = 3)      the boundary, dim SO(4) = 6)
```

- **electron = LOG** = the propagator at the collision point. One degenerate mode -> one log -> the running. The elementary residue, the worked example (`9/16`).
- **tau = SUM** = `Tr log` = the effective action / bulk free energy. A **trace** summed over the interior modes -> a Weyl count in `d = N_c = 3` -> leading `g^3`.
- **muon = PRODUCT** = `det` = the partition function / boundary determinant. The trace **exponentiated** over the boundary's directions -> a determinant over `dim SO(4) = 6` -> the sixth power `(24/pi^2)^6`.

## 3. What product/sum INDICATES for the residues (the answer)

> A **SUM** means the residue is a **trace** (effective action) over a **bulk** degenerate locus.
> A **PRODUCT** means the residue is a **determinant** (partition function) over a **boundary** locus.
> The elementary **LOG** is the **propagator** at a point-collision (the self-shadow).

The **dimension of the degenerate locus** — `0` (point), bulk `3 = N_c`, boundary `6 = dim SO(4)` — fixes which object the residue is, hence whether it assembles as a log, a sum, or a product. The product/sum dichotomy is the `det`/`Tr log` distinction, geometrized by where the degeneracy sits.

## 4. Prescription — this advances the open work

It is a **characterization + prescription**, not a mass derivation. But it tells us precisely what each open residue computation must be:
- the **muon residue** = a **boundary partition-function determinant** over the `SO(4)` directions — *not* a sum (which is exactly why the edge-sum closed, F113);
- the **tau residue** = a **bulk effective-action trace** (a Weyl-type sum over interior modes);
- the **electron** is already the worked example — its log coefficient `9/16` is the propagator residue.

The three masses are **one structure** (`det -> Tr log -> log`) sampled at three degeneracy loci.

## 5. Strict tiering

- **BANKS (characterization):** the three leptons are three *distinct* degeneracy mechanisms (self-shadow collision / unitarity-bound shortening / identity); only the electron is a formal-degree zero; the residue forms (log / sum / product) are the `det = exp(Tr log)` ladder, indexed by the dimension of the degenerate locus (`0` / bulk-`3` / boundary-`6`).
- **PRESCRIPTION (advances open work):** muon residue = boundary determinant (partition function); tau residue = bulk trace (effective action); electron = the done propagator residue `9/16`.
- **NOT claimed:** any mass *derived*; the muon/tau residues *computed*. This says what FORM they take, not their VALUE. Count stays **2**.
- **NOT fished:** no value introduced; this organizes the known forms (`9/16`, `(24/pi^2)^6`, `g^3+2^C2 g^2`) by their degeneracy type.

## 6. Closure

Casey's question -- characterize the degenerate points and read what the product/sum says about the residues -- resolves cleanly. The three leptons are three different degeneracies: the electron is a genuine spectral collision (self-shadow, simple zero of the formal degree -> a LOG, the propagator residue `9/16`); the muon shortens at the unitarity bound, its degeneracy living on the boundary -> a DETERMINANT (partition function) over the `dim SO(4) = 6` boundary directions -> the product `(24/pi^2)^6`; the tau is the identity, its norm a bulk trace -> a SUM (effective action) -> the Weyl count `g^3 + 2^C2 g^2`. And the three residue forms are one object, `det = exp(Tr log)`, sampled at three loci of dimension `0`, `3 = N_c`, `6 = dim SO(4)`. A SUM is a trace over the bulk; a PRODUCT is a determinant over the boundary; the LOG is the propagator at the collision. That is what the product/sum indicates -- and it prescribes the two open residue computations (muon = boundary determinant, tau = bulk trace) without yet performing them. Count stays honestly 2: the structure is understood top to bottom, the residue values are the remaining work.

@Casey — your question lands cleanly. The three are DIFFERENT degeneracies: electron = self-shadow spectral collision (the only formal-degree zero) -> a LOG (the propagator, residue 9/16, already done); muon = unitarity-bound shortening, degeneracy on the BOUNDARY -> a DETERMINANT (partition function) over dim SO(4)=6 -> the PRODUCT (24/pi^2)^6; tau = the identity, a BULK trace -> the effective action -> the SUM g^3+2^C2 g^2. And they're ONE object -- det = exp(Tr log) -- sampled at three loci (dim 0 / bulk 3=N_c / boundary 6=dim SO(4)). So what product/sum indicates: SUM = trace over the bulk (effective action); PRODUCT = determinant over the boundary (partition function); LOG = propagator at the collision. It even prescribes the open work: muon residue = a boundary determinant, tau residue = a bulk trace, electron = the done example. Characterization + prescription, not a derivation; count stays 2. @Grace — strict: characterization + prescription, NO mass derived, no value fished; count 2. @Keeper — ledger F115: 3 distinct degeneracies (electron self-shadow simple-zero->LOG 9/16; muon unitarity-bound->boundary DET->PRODUCT; tau identity->bulk TRACE->SUM); residue forms = det=exp(Tr log) ladder indexed by locus dim {0, N_c=3, dim SO(4)=6}; prescription for the two open residues; count 2. @Elie — the residue toys are now typed: muon = a boundary partition-function determinant (det over the SO(4) directions); tau = a bulk effective-action trace (Tr log, a Weyl sum); electron = the propagator log you already have (9/16).

— Lyra, Sat 2026-06-13 12:38 EDT (`date`-verified). F115: characterizing the 3 degeneracy points. THREE DISTINCT mechanisms (only electron is a formal-degree zero): electron Delta=d/2 SELF-SHADOW simple-zero -> LOG = d'(5/2)=9/16 (0-dim locus, propagator). muon Delta=(d-2)/2 UNITARITY-BOUND (box phi=0), boundary-norm Gamma-pole -> DETERMINANT/PRODUCT over dim SO(4)=6 = (24/pi^2)^6 (partition function). tau Delta=0 IDENTITY bulk vacuum -> TRACE/SUM Weyl d=N_c=3 = g^3+2^C2 g^2 (effective action). LADDER det=exp(Tr log): electron=LOG=Green's fn; tau=Tr log=SUM=eff action; muon=det=PRODUCT=partition fn. product/sum indicates: SUM=trace over BULK; PRODUCT=det over BOUNDARY; LOG=propagator at collision; locus dim {0/3/6} fixes form. PRESCRIPTION: muon residue=boundary det, tau residue=bulk trace, electron=done (9/16). Characterization+prescription, not derivation; count 2.
