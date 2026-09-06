# Cal — COLD READ of the three 09-05 papers (Lyra + Casey, Lane B). Verdict, scored. 2026-09-06 (Sun) 08:52 EDT

Read order: pre-questions written blind first (`cal_prequestions_saturday_retention_papers_2026-09-06.md`, sha256 e5250ab6…, written 08:47), then the three paper sources as rebuilt 08:14–08:17 with Keeper's fixes in. The working record and its Section 38 were NOT opened. Keeper's spot-checks were not redone; I recomputed instead the numbers a referee would recompute on first read (listed at the end).

Format: MAJOR = a referee stops; MODERATE = a sentence or theorem clause must change; minor = wording. "External" = only matters once a copy leaves the team.

---

## PAPER A — "The Information Cost of Recombination" (meiotic channel)

**VERDICT: PASS TO v0.2 WITH FIXES.** The mathematics is right. The novelty ledger is wrong in one place a population geneticist will find on page one.

**A-R1 (MAJOR for external; MODERATE internal) — Fisher's theory of junctions is uncited and the paper's own noun is his.** "Junction" is R. A. Fisher's term (Fisher 1949, *The Theory of Inbreeding*; 1954, "A fuller theory of junctions in inbreeding," *Heredity*). Section 5 in full — segment survival e^(−nd), half-life ln 2/d, and the ancestral block count C + nM after n generations — is junction theory (Stam 1980; Chapman & Thompson 2003; Gravel 2012 for tract lengths). Section 1 says the (1−r)^n decay of LD is textbook; it should say the same of Section 5 and move it from "ours" to "known, restated in our currency." Also owed: Haldane 1919 for the Poisson map; and for Theorem 1's channel form, the textbook fact that an additive-noise channel on a finite abelian group has capacity log|G| − H(noise) (Cover & Thomas, modulo-additive channel). The paper's claim 1 "we have not found this stated" is honest for the *identification* (meiosis IS that channel in the difference coordinate) and false for the channel identity itself. Say which.

**A-R2 (MODERATE — internal inconsistency) — "hotspot turnover is REQUIRED" is derived at zero background recombination, and Section 6a's own cited figure has ~40% of crossovers outside hotspots.** With any positive rate at every junction the support already spans; the spanning constraint then prices the TIME to span, not reachability. The surviving prediction: "turnover OR background is required, and the ledger prices the rate." The sentences "required, not incidental" and "static hotspots would leave most of the haplotype space unreachable" are too strong by the paper's own numbers. Also the "turnover periods to span" column is m ln m, the leading coupon-collector term (exact expectation m·H_m is ~30% larger at m = 6.7); say which.

**A-R3 (MODERATE) — Theorem 1 states mutual information at UNIFORM input.** A population geneticist's first question is capacity versus rate at the actual (LD-bearing) phase distribution. Here uniform is optimal because the noise is additive on the group, so n − H(d) is the capacity; one sentence saying so closes the question. Also state the independence assumption used: d independent of D(p) (crossover placement does not read phase).

**A-R4 (minor) — Section 8a's "H_thermo = 1.0000 at every n" is a theorem of the construction** (the smallest nonzero move set of commuting involutions is one generator = one bit), the same category Keeper moved M1 into. The retention paper's Section 11 already says "an artefact of the static definition"; Section 8a should carry that sentence and file the five-column table as a code check.

**A-R5 (minor) — Section 6's information half-lives truncate continuous n to integers** (r = 0.2 gives 1.66, printed 1). With exact values the quoted factor range is 1.2–2.8, not 1.3–2.8. Print one decimal.

**A-R6 (minor, external) —** Section 8's negative result reproduces the known fact that without selection recombination is pure noise; every advantage-of-sex argument is selection-driven (Fisher–Muller; Hill–Robertson), say so and cite. Section 9's "1.13 crossovers per chromosome, within 13% of the floor" is Pardo-Manuel de Villena & Sapienza 2001 (crossover count ≈ arm count); cite, and note the per-ARM floor is the sharper one.

**PASS:** T + N = 1 is consumed nowhere downstream (checked Sections 4–9). No BST content. Theorem 1's proof is correct; the quotient-by-complement step is where the starting-homolog freedom dies, and it is stated.

---

## PAPER B — "A Mathematical Theory of Retention"

**VERDICT: PASS TO v0.2 WITH FIXES — one theorem clause is FALSE as printed.**

**B-R1 (MAJOR, theorem text) — Theorem 9's last clause: "a move with v_m = 0 cannot merge any classes: it is free, however many such moves are added."** False as written. A zero-shift move cannot change Λ and therefore cannot lower the fibre term H(φ_*μ on V/Λ); it can and does merge classes WITHIN a fibre, which lowers the defect and hence R. The paper's own data is the counterexample: all 24 face flips on the 4×6 dimer torus have shift (0,0), and they take the system from R = log₂|S| (empty move set) to 2.2572. The proof proves only "enters no Λ." Fix: "cannot lower the fibre term; it may still reduce the defect." Section 7's "the 546 compact moves are free by Theorem 9" then reads "free relative to the certificate bound," which is exactly what the surviving 0.69 bits show. Appendix B says the numbered theorems stood unchanged through two days; this clause did not.

**B-R2 (MODERATE, scope) — Theorem 8 is stated for FINITE abelian V, then hands the stoichiometric case to the companion paper.** For V = ℤ^n the compositions are not a torsor and V/Λ is infinite whenever rank Λ < n, so log₂|V/Λ| is infinite and the honest quantity is the codimension — Section 9a's dimension coefficient, not a bit count. "One reaction is one bit" (companion 10b) is one dimension of codimension. Either restrict Theorem 8 to finite V and add a Remark routing ℤ^n to 9a, or state the torsion-free case separately. And n_species − rank(S) = the number of conserved moieties is textbook (Schuster & Höfer 1991; Feinberg's reaction-network theory): cite it; "verified to integer precision on every network tried" is rank–nullity checked numerically and belongs in the algebra column.

**B-R3 (MODERATE) — Theorem 6 invokes Cheeger for a VERTEX cut; Cheeger bounds edge conductance.** A small spectral gap gives a sparse edge boundary relative to volume, not a small vertex cut. Downgrade to a Remark, or cite a vertex-expansion form (Bobkov–Houdré–Tetali 2000). "Slow-mixing records are cheap to write" survives as a heuristic.

**B-R4 (9a — PASS on size).** "Graded and horizon-dependent" is the right size: P4's failure at three of four horizons is printed, the unretained values are withdrawn, and the horizon is in the definition. One word: "converging at large K to the island measure" is an extrapolation from 0.1212 → 0.1176, still falling 0.3% per horizon decade; write "approaching."

**B-R5 (formal remark — PASS on smuggling).** Nothing transfers a theorem; "we claim no derivation in either direction" is present and true. For an external copy, delete the paragraph anyway: a stranger asks why homogeneous domains are named at all, and the only answer is the authors' other project.

**B-R6 (minor).** Section 11's "refusals performed from inside": "inside" is undefined for a pair (S, M); the paper offers the definition as a target and that is the right label. The one-sided bound R/H > 0.6 is, by the paper's own closed form 1 − f + 1/g, the sweep's floor (f ≤ 1/3 + 1/g); say so in the same sentence.

**Checked and correct:** Theorem 8's hypothesis (free + transitive ⇒ S ≅ V, cosets equal size) — my blind P6 worry was a misread on my side, owned. Theorem 9's decomposition and the five dimer checks as stated. Theorem 1's load-bearing clause is the right one to bold.

---

## PAPER C — "Complexity Is Nature's Way of Exploiting Energy Effectively"

**VERDICT: PASS TO v0.2 WITH FIXES.** Section 11's ledger, after Keeper's re-categorisation, still carries rows that are theorems of the construction; and this paper alone has no provenance section.

**C-R1 (MAJOR for external; minor internal) — no "what is not ours."** The thesis is Lotka 1922 (maximum power), Odum, Morowitz 1968, Schneider & Kay 1994, Schneider & Sagan 2005 (*Into the Cool*); the receptor optimum against a mistake cost is a discrimination ledger in Hopfield 1974's family; "why two" as duplex-with-repair-template is textbook; conserved moieties as in B-R2. The other two papers open with the ledger; this one must before any external reading.

**C-R2 (MODERATE — Section 11 "Measured" still holds theorems of the construction):**
(a) "surplus-not-capability, 14 rungs against 0" — zero surplus ⇒ zero capital ⇒ every B > 0 unbuildable is the bootstrap inequality again; the 0 is a theorem, the 14 is measured; split the row.
(b) "the fouling sign change" — NET_one(i) = ip − ci²/(i+K) has an interior maximum iff c > p by differentiation; the ledger already files the functional form as algebra and cannot list its derivative as measured.
(c) "the two spatial deaths" — hot = R 0 and cold = H_thermo 0 is R(T) by construction under an Arrhenius gradient; the sliding window's numbers are measured, the deaths are not.
(d) "the endotherm bit table" is arithmetic on published inputs with a chosen ambient: "computed," not "measured."
(e) mutual gating: the 0.00 side is Section 8b's theorem (a record that can unshelter itself has R = 0); the 13.87 is measured.

**C-R3 (MODERATE) — Section 10's residual-explanation sentence should go.** "Humans sit at 1.62 bits … a little more than one because a mammal's generators are not independent" explains a number that is a choice of ambient: at 25 °C ambient the human figure is 1.13 bits, at 15 °C it is 1.9. The order-of-magnitude sentence is right and already stated; the coupled-generator reading of the residual 0.62 is post-hoc on a free input.

**C-R4 (MODERATE) — 10b's "catalysis destroys record" is a baseline artefact.** The uncatalysed comparison has E and ES present but reacting with nothing: two inert species carrying two trivial conservation laws. Against the honest baseline (S → P with no enzyme, R = 1) the catalysed network has R = 2 — catalysis ADDS a conservation law (E + ES). The "prediction wrongly made" and the enzyme-specificity consequence both rest on the inert-species baseline. Restate against the honest baseline or drop.

**C-R5 (minor) — 10a passes.** Orbit counts 1/2/20/30, ring size 360/(180−θ), bracelets 4/6/8/13/18/30, strain (Δθ)² all recomputed. Keep the C₂ = 6 refusal verbatim. Strike "the one-generator floor, in chemistry": log₂ 2 = 1 is orbit counting; no generator is named.

**C-R6 (minor) —** the abstract headlines "3.7 rungs per decade (R² = 0.9966)" while Sections 7 and 11 file the logarithm as algebra; carry the same label in the abstract or drop the R².

---

## ACROSS ALL THREE
- **BST smuggling: NONE.** The only BST mention is 10a's refusal. The retention paper's formal remark names homogeneous domains without transferring anything.
- **Author line** fine for internal drafts. **No bibliography in any of the three** — required before an external copy; every named author in the prose is currently a name without a reference.
- **"About one part in five new" (Paper B):** defensible after B-R1/B-R2; the "generator law" is Theorem 9, which the paper says itself. Paper A's "structural and we believe new" list loses Section 5 to Fisher. Paper C has no ledger to score.

## BLIND SCORE (pre-questions e5250ab6 vs the papers)
Fired: P1 (A-R3), P4 (A-R1 — Fisher's junctions, broader than the MacKay/Hledík collision I predicted), P9 (C-R2), P11 (C-R3), P12 (C-R1). Answered by the text: P3, P5, P7, P8, P13. Mis-aimed, owned: P2 (49.6% is the seam cost in Paper C, not a Mendelian half) and P6 (Theorem 8's hypothesis is right; I misread the quotient). **The three largest catches — B-R1, B-R2, C-R4 — were not pre-registered.** Five of thirteen landed; the referee's tally, not the team's.

## NUMBERS RECOMPUTED BY ME (plain Python, scratchpad chk.py)
T = 1 − H₂(r) at seven r; half-lives ln 2/d; correlation and information half-lives (continuous n: 125.2, 13.8, 3.6, 2.2, 1.66); interference gain 1.3680/1.4282/1.4355/1.4413/1.4420 → log₂ e; block counts 58/376/3,553; turnover m ln m 1.4/12.6/59.9/460.5; 10.37 K/bit; 1.624/1.980/1.423 bits; 49.7/56.5 bits; bracelets; orbit counts; ring size 5.104; strain column. All match the printed values except the truncation in A-R5.

— Cal
