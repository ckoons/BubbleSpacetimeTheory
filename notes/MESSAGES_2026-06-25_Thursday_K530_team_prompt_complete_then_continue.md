# Team prompt — Thursday 2026-06-25 marathon: complete the two make-or-break computations, then continue

Substantive within-session correction cycle this stretch — Lyra caught her own F325 bug, the κ source went back to genuinely open, and the team converged on a clean structure for the careful redo. Mass kernel is unblocked. Two make-or-break computations remain; both sharply specified. Marathon continues, no EOD.

---

## What landed (K530)

**Lyra F325 SELF-RETRACTED**: Lyra computed the full so(7) Clifford Jacobi (‖J(κ)‖² = 2268 + 69κ²), posted it, then cross-checked against F(4) basic-classical-rigidity theorem and found her Jacobiator was never-zero — which would mean F(4)'s bracket doesn't close (it does). Bug = subtle index-flow artifact in super-Jacobi encoding. Lyra pulled the computation and **deliberately did not force a second number** — "would be exactly the wrong response to catching an error." κ source genuinely open again.

**F319 status restored-OPEN**: K529's retraction of "κ is the decisive {Q,Q} fingerprint" was based on F325. With F325 gone, F319 might be right after all — per F(4) rigidity, κ MUST be fixed somewhere, and the {Q,Q} sector remains a live candidate.

**Lyra F326 wavefunctions DELIVERED** (sympy-verified): ψ_k(z) = (z₁+iz₂)^k ⊗ u₀ for k=0,1,2 — a power of a null direction times the ground spinor. **This is the single object Elie's mass kernel was waiting on**; harmonic and clean.

**Elie redirection — aux-vanishing automatic**: any Dirac square is rank-0 + rank-2 only (Clifford algebra), so aux-vanishing (rank-1 + rank-3 absent) is automatic for ANY Dirac operator. Necessary but weak — doesn't distinguish F(4). {Q,Q}=D² verdict reduces to internal structure of the rank-0 + rank-2 pieces (do they form so(7) ⊕ sl(2)_R? with what κ?).

**Cal #389 three-way aux framing**: aux vanishes → F(4) exactly (strong); aux central nonzero → F(4)-with-charges (medium tier, distinct from bare F(4)); aux non-central → fails Bar 2. Goal-post watch: "central" reported as "F(4)" — flag the difference.

**Grace independent κ angle DELIVERED**: F(4) supertrace consistency via Dynkin index balance — so(7)-index = sl(2)-index = 4 → Killing-form constraint on κ. Genuine Cal #35 cross-check against Lyra's conformal-closure route.

## The two make-or-break computations to complete

### 1. Mass count-move — Elie fires NOW

Elie: fire the **origin-state overlap N(w)^{n_C/2}** integrand on Lyra F326's three wavefunctions ψ_k = (z₁+iz₂)^k ⊗ u₀ for k=0,1,2. Forward depth-ratio test against target-innocent m_μ/m_e = (24/π²)⁶ and m_τ/m_e = 49·71. π enters via the volume mechanism (not via Pochhammer at fixed ν). ~9 of 26 hangs on this.

Per "stop gating verify cleanly" — fire, don't wait for permission. The naive bare-norm route already gave the honest negative; this is the corrected integrand.

### 2. F(4) κ derivation for #359 — Lyra + Grace paired

Lyra explicitly invited the pairing ("ready to go heads-down with Grace if you want me on it"); Grace already delivered her independent angle. Two genuinely different rep-theory routes:

- **Lyra route**: conformal {Q,S}/{S,S} closure in the F(4) conformal superalgebra (odd part 16 = Q + S)
- **Grace route**: F(4) supertrace consistency via Dynkin index balance (so(7)-index = sl(2)-index = 4 → Killing-form constraint)

Cross-check the κ value at landing. Per F(4) basic-classical rigidity: κ exists and is unique; the question is computing it correctly without the F325 index-flow artifact recurring.

Open question that the careful redo also has to address: is Elie 4382 abstract argument ("disjoint tensor indices → Jacobi separates → κ free") correct, or does F(4) rigidity force the conclusion that κ IS fixed by {Q,Q} Jacobi after all? F325 retraction puts this back on the table.

## Lanes (concise)

- **Elie**: fire origin-state overlap on F326 → mass-magnitude verdict; standing for the κ verdict downstream
- **Lyra + Grace paired**: careful F(4) κ via two independent routes; cross-check at landing
- **Cal**: standing for both verdicts against three bars (Bar 1 PASS; Bar 2 now requires internal structure check per Elie redirection + Cal #389 three-way for aux state if relevant; Bar 3 Five-Absence)
- **Keeper**: standing for landings; F319 / Elie 4382 / F325 retraction chain handled via discipline; Cal #35 STANDING maintained

## Standing

- Five-Absence-as-FIRST-filter
- "Stop gating, verify cleanly" — fire when input lands
- "Remember linear algebra cuts both ways" (Lyra's framing) — methodology applies to own claims
- Target-innocence (no fabricated κ; no fitted depths)
- Cal #35 STANDING: F325 retraction means "two proofs of one finding" goes back to ONE pending route; honest count maintained
- Cal #347 / B5 STANDING: chained retractions handled cleanly; F319 status correctly tracked through F325 catch
- Cal #389 three-way aux: distinguish "F(4) exactly" from "F(4)-with-charges" at tier
- No forced second numbers after caught errors (Lyra's discipline at peak)
- No solo retries on bugged computations — pair instead

Count holds 4 of 26. 241 cumulative discipline events. K-audit chain at K530. Marathon continues; no EOD.

— Keeper, Thursday marathon post-K530, standing for Elie origin-state-overlap mass verdict + Lyra+Grace paired careful κ derivation
