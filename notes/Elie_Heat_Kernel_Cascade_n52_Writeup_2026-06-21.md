# Heat-Kernel Cascade to a₂₆ (n=52, dps=3200): Coefficients, the Speaking-Pair Ladder, and What They Say About the Engine

**Author:** Elie (Claude) · **Date:** 2026-06-21 (Sunday) · **For:** Keeper audit
**Status:** Keeper **K450 CONDITIONAL PASS → both conditions addressed** (2026-06-21): bug-fix justification swapped to the independent cross-file match (Section 6); precision caveat added to stored JSON meta. · **Count impact:** none (4 of 26 unchanged)

**Tier key:** SOLID = verified by computation/theorem · IMPOSED = built in as a constraint (not a free output) · LEAD = plausible, not proven · INTERPRETIVE = framing/reading, not a theorem.

---

## 0. One paragraph (the plain story)

We compute the heat kernel of the geometry's compact dual — the "exterior engine" Q⁵ = SO(7)/[SO(5)×SO(2)] — as a short-time expansion `Z(t)/vol = Σ aₖ tᵏ`. Each coefficient aₖ is a polynomial in the dimension n; the program extracts them one rung at a time (a "cascade"). The n=52 spectrum checkpoint that just finished was the last dimension needed to reach **a₂₆**. We computed and stored the full coefficient set a₁…a₂₆ at 3200-digit precision, confirmed the known structure, and read off what it says about the kernel. The headline pattern Casey spotted — the "speaking pairs" — turns out to be governed entirely by the single integer **n_C = 5**, which structures the ladder three ways (period, within-pair count, between-pair step). Those three are *consequences of one formula*, not three independent facts (independence-counting per Cal #330).

---

## 1. What was computed, and how

- **Object:** Seeley–DeWitt (heat-trace) coefficients aₖ(n) of the Laplacian on the compact dual of D_IV^n, as polynomials in n. Extracted by the established **toy_671d** cascade (reused verbatim — no reimplementation), which loads per-dimension heat traces, Richardson/Neville-extrapolates each rung, identifies the rational, and fits the degree-2k polynomial in n.
- **Data:** 50 dimension checkpoints, n = 3…52, at dps = 3200 (n=3…40 promoted from dps=1600; n=41…52 native dps=3200). The **n=52** checkpoint (the new one) supplies the 50th dimension that a₂₆ requires (n_need = 2k−2 = 50). **[SOLID]**
- **Run:** `toy_4286` — cascade a₁…a₂₆, ~64 min, incremental save. Max confirmed level **k = 26**. **[SOLID]**
- **Stored:** `play/toy_671_checkpoint/coefficients_n52_dps3200.json` (265 KB): for each k, the **full polynomial** aₖ(n) (exact Fraction coefficients, index = power of n), degree, aₖ(5), subleading/leading ratio, and speaking-pair flag. This is new — the prior `results_hybrid_3200.json` kept only aₖ(5). **[SOLID]**

## 2. The coefficient skeleton (three analytic forms, verified to k=26)

For every k = 2…26 the polynomial aₖ(n) has fixed top, second-from-top, and bottom:

| term | form | tier |
|---|---|---|
| leading (n^{2k}) | `1 / (3ᵏ · k!)` | SOLID-verified; **IMPOSED** (three-theorems input) |
| subleading (n^{2k−1}) | `−k(k−1)/(2·n_C) · leading` | SOLID-verified; **IMPOSED** |
| constant (n⁰) | `(−1)ᵏ / (2·k!)` | SOLID-verified; **IMPOSED** |
| interior coefficients | space-specific | **extracted** (the genuine output) |

**Audit note for Keeper:** the three boundary forms are *imposed* by the cascade's `three_theorems` constraint, then confirmed self-consistent; they are not free discoveries. The genuinely *extracted* content is (a) the interior coefficients and (b) the fact that aₖ(5) reproduces the known rationals through the verified range. Verified `leading` and `const` against closed forms for **all** k=2…26 (toy_4288 [1]). **[SOLID]**

## 3. The speaking-pair ladder — Casey's pattern, derived (toy_4287, 6/6)

The subleading/leading ratio is exactly `v(k) = −k(k−1)/(2·n_C) = −k(k−1)/10`. It is an integer ("speaking pair") iff `k ≡ 0 or 1 (mod n_C)`, giving pairs at k = (5,6), (10,11), (15,16), (20,21), (25,26) with values

`{5:−2, 6:−3, 10:−9, 11:−11, 15:−21, 16:−24, 20:−38, 21:−42, 25:−60, 26:−65}` — all 10 confirmed against the stored coefficients. **[SOLID]**

**Casey's two observations, both exact and both derived:**

1. **Within-pair gap = the pair index m.** `v(5m) − v(5m+1) = m` → 1, 2, 3, 4, 5, … (confirmed m=1…5; symbolic for all m). Pair 5 (k=25,26): −60, −65, gap 5.
2. **Between-pair jumps are arithmetic with common difference n_C = 5.** First-of-pair: −2, −9, −21, −38, −60 → jumps −7,−12,−17,−22 → second difference −5,−5,−5. Closed form jump(m) = −(n_C·m + 2).

So **n_C = 5 organizes the ladder three ways at once**: the *period* (which levels speak, mod n_C), the *within-pair count* (1,2,3,…), and the *between-pair step* (n_C). These three are *consequences of the single formula* v(k), **not** three independent confirmations (Cal #330) — the Schur-generator point is that one primitive (n_C) propagates into all three readings, not that three separate facts coincide. **[SOLID]** that the patterns hold and derive from v(k); **IMPOSED** that v(k) itself is the three-theorems subleading form (so the ladder is a clean *consequence*, not a new degree of freedom — flagged honestly).

One suggestive note (**INTERPRETIVE/LEAD**): speaking levels come in doublets (5m, 5m+1) — multiplicity 2 per "voice," equal to the domain rank = 2. Fits, not banked.

## 4. What the coefficients indicate about the engine (toy_4288, 6/6)

**(a) Performance — rigidity = compressibility + fast convergence. [SOLID]**
Three of the 2k+1 coefficients are fixed analytic forms; the rest are polynomial in n. The whole heat trace is encoded in small integers + a cascade rule, not a spectral sum — recomputation-free and exactly extendable. The leading term at fixed n is `(n²/3)ᵏ/k!`, which peaks near k≈8 (n=5) then decays super-exponentially → the short-time expansion converges fast in the operational window (t ~ 10⁻³); truncate low for accuracy or cascade high for deep curvature.

**(b) Processing exterior heat input — the gap is a filter. [SOLID spectrum; INTERPRETIVE framing]**
The exterior spectrum is integer: λ_k = k(k+5) = {0, 6, 14, 24, …}, **gap = 6 = C₂** (ground degeneracy 1; first excited mode degeneracy 7 = SO(7) vector). A gap is a threshold: sub-gap input relaxes to the protected ground state (Z − g₀ ~ e⁻⁶ᵗ); supra-gap input excites the discrete ladder. Integer spectrum ⇒ theta/modular heat trace (quasi-periodic under t→1/t), not a dissipative continuum.

**(c) Number-theoretic interest — with an honest horizon. [SOLID + flagged limit]**
Integer eigenvalues ⇒ modular/theta structure (the program's existing modularity backbone). The aₖ(5) **denominators are von-Staudt-Clausen-smooth** (small primes tracking the level: maxprime 11 at k=5, 17 at k=10, 29 at k=14) — a Bernoulli-denominator shadow, consistent with the program's 7-smooth window (Toys 1152-1160) — **LEAD**, not a proven identity. **Honest horizon:** at k≥15, evaluating aₖ(n) at n=5 produces large primes (3907, 60889, …); the bounded-prime smoothness is a *low-order* phenomenon at n=5 and is *sporadic* above k≈14 (a₂₆(5) happens to return to maxprime 11). The clean *analytic skeleton* (Section 2) persists to k=26; aₖ(5) smoothness does not.

**(d) Thermodynamic interest. [SOLID identification; INTERPRETIVE reading]**
Z(t) is a partition function with t = inverse temperature: a₀ = volume (leading state count), a₁ ∝ scalar curvature (first correction); the aₖ are the high-temperature expansion. The gap gives a thermodynamically protected vacuum (free energy → 0 at low T, no low-energy excitations to bleed); factorially-suppressed corrections give a controlled high-T expansion.

## 5. "Rigid / built for permanent operation" — the honest split

- **OBJECTIVE (measured):** small-integer-fixed coefficients, clean analytic skeleton to k=26, discrete integer spectrum, gap = C₂, modular heat trace. This is the mathematical profile of a stable, non-dissipating, exactly-recurring system. As a *description*, "permanent operation" is fair, not subjective. **[SOLID]**
- **INTERPRETIVE:** "built *for*" imports intent/teleology, which the mathematics does not decide. The system *has* the properties; attributing purpose is framing. **[INTERPRETIVE]**
- **Program alignment:** the objective profile is exactly what Interstasis (cross-cycle persistence) and the SWPP (substrate working process) already require — a non-dissipating, recurrent engine. Casey's intuition points at the same stable engine from the thermodynamic side. **[LEAD]**

## 6. One bug caught (reference table, not computation)

The run flagged a₁₇(5) "mismatch" against toy_671d's hardcoded `KNOWN_AK5[17] = 20329084105/173988`. Run down: the computed a₁₇(5) = **6964243457/59604** matches the prior **hybrid** run (`results_hybrid_3200.json`, field `a17_n5`) **exactly** — and that file was produced by an *independent* computation that does **not** use the hardcoded `KNOWN_AK5` table (the table is only a sanity reference, never a computational input). So two independent computations agree on 6964243457/59604 and the hardcoded constant is the lone outlier ⇒ stale. (Keeper K450 rechecked the value by direct polynomial evaluation of the stored polynomial; per Cal #330 this confirms the poly→value arithmetic but is **not** a third independent derivation — independence rests on the **two** non-circular computations, cascade + hybrid; the poly-eval adds confidence.) Corrected in `toy_671d_nmax52_pair5.py` with a dated note. **Effective verification of aₖ(5): 15/15.** **[SOLID]**

*Reasoning correction (Keeper K450, taken clean):* the first draft also cited "downstream speaking pairs all correct" as support. That argument is **weak** and is withdrawn — the speaking pairs are the *imposed* subleading forms (Section 2), produced at every k by the three-theorems constraint independent of any interior content, so they test the imposed pipeline, not a₁₇'s interior. The cross-file match above (independent of the hardcoded constant) is the correct justification.

## 7. Artifacts

- `play/toy_671_checkpoint/heat_n52_dps3200.json` — the new spectrum checkpoint (input).
- `play/toy_4286_…n52_dps3200.py` — cascade run (a₁…a₂₆).
- `play/toy_671_checkpoint/coefficients_n52_dps3200.json` — **full polynomials stored** (output).
- `play/toy_4287_speaking_pair_ladder_…py` (6/6) — Casey's ladder pattern, derived.
- `play/toy_4288_heat_kernel_performance_…py` (6/6) — performance / number-theory / thermodynamic reading.
- `play/toy_671d_nmax52_pair5.py` — KNOWN_AK5[17] corrected.

## 8. For Keeper — suggested audit targets

1. **Skeleton vs output:** confirm the framing that leading/subleading/const are IMPOSED (three theorems) and the ladder is a *consequence*, not a free result. Is the write-up's tiering honest?
2. **Smoothness horizon:** verify the k≈14 VSC-smoothness horizon at n=5 and that I have *not* claimed bounded-prime structure to k=26. The VSC connection is tagged LEAD — appropriate?
3. **Self-consistency as proof-of-correctness:** ~~is "downstream speaking pairs all correct ⇒ a₁₇ correct" sufficient?~~ **RESOLVED (K450):** the downstream-pairs argument is weak (pairs are imposed); justification swapped to the independent cross-file match (the two non-circular computations) + Keeper's poly-eval recheck. See Section 6.
4. **Interpretive claims:** the gap-as-filter, protected-vacuum, and "permanent operation" readings are tagged INTERPRETIVE/LEAD. Confirm none have leaked into SOLID.
5. **Interior-coefficient precision at high k:** ~~should aₖ for k≥~20 carry a precision caveat?~~ **RESOLVED (K450):** `precision_caveat` added to the stored JSON `meta` — speaking-pair/leading/constant invariants SOLID at all k; interior coefficients k≥20 flagged extrapolation-bounded.

**Net:** the heat-kernel cascade now reaches a₂₆ at dps=3200 with full polynomials stored; the speaking-pair ladder is structured three ways by the single primitive n_C (three consequences of one formula, not three independent facts — Cal #330); the engine reads as gapped, integer-spectrum, modular, arithmetically-rigid — a "permanent-operation" profile as *description*, with teleology left as the only interpretive layer. Nothing newly banked; count holds at 4 of 26.
