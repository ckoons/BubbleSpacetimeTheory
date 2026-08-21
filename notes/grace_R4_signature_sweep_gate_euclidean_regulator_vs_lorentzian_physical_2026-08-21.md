# ℝ⁴ signature sweep: the gate, the rule, and the dispatch-critical priority list (Grace, Round 42)

*Enforcement of the Round-41 signature-tag rule: every ℝ⁴ carries (signature, branch) at first use — ℝ⁴_E (Euclidean (4,0), REGULATOR) vs ℝ^{1,3} (Lorentzian (3,1), PHYSICAL/Branch H). Sweep RUN. Result: **NOT clean** — ~587 physics-relevant ℝ⁴ mentions across ~40 files, essentially all untagged. This is a standing owner-by-owner cleanup (like the C₂↔n_C family), NOT a one-round close. I do NOT report it clean. Deliverable: the greppable gate, the classification rule, and the dispatch-critical subset to tag FIRST.*

## The gate (greppable — a row closes when this returns 0 for the target scope)
```
# physics-relevant, untagged ℝ⁴ (excludes Poiseuille radius⁴ + pure-topology, which are signature-irrelevant):
grep -rn "ℝ⁴\|R⁴\|R\^4\|mathbb{R}\^4" notes/*.md | grep -iv "\.bak" \
 | grep -iE "yang.?mills|mass.?gap|spacetime|slice|scale.?free|renormaliz|constructi|area.?law|projection" \
 | grep -iv "Euclidean|Lorentzian|\(4,0\)|\(3,1\)|ℝ⁴_E|R\^\{1,3\}|signature|πR⁴|Poiseuille"
```
Current baseline: **587 hits** (NOT clean). Dispatch-scope target (YM/Millennium docs + Paper67): drive to 0 first.

## The classification rule (mechanical — for owners tagging their first-use)
| context of the ℝ⁴ | tag | branch | why |
|---|---|---|---|
| YM / mass-gap / **constructive QFT** / renormalization / scale-free / area-law / exotic-R⁴ / Clay | **ℝ⁴_E (Euclidean, (4,0))** | REGULATOR | the Clay YM obstruction lives in the Euclidean/OS constructive setting (the decompactification side). |
| observed **spacetime** / the 4D slice / D_IV⁵→ℝ⁴ projection / conformal boundary | **ℝ^{1,3} (Lorentzian, (3,1))** | PHYSICAL (Branch H) | the physical Minkowski boundary; conformally (S³×S¹)/ℤ₂. |
| pure topology (linking, codimension) | Euclidean-math (signature-irrelevant) | — | no physics/regulator collision; tag Euclidean if convenient, LOW priority. |
| **πR⁴** (Poiseuille, Q=πR⁴ΔP/8ηL) | FALSE POSITIVE | — | R⁴ = radius⁴, not the space ℝ⁴. Exclude. |

**The key distinction (Round-41 fork):** the YM-construction ℝ⁴ (Euclidean regulator, where "no mass gap on scale-free R⁴" lives, T1793) and the physical spacetime ℝ⁴ (Lorentzian, D_IV⁵→ℝ⁴ "full spacetime", registry:8479) are **different objects** related by Wick rotation — not interchangeable.

## Dispatch-critical priority list (tag these FIRST — they're in the dispatch lane)
- **Euclidean ℝ⁴_E (regulator):** YM registry rows — T1271 (951, 2092), T567 (1429), T896 (1739), T972 (1806), T993 (1827), T1146 (1977), T1400 (2221), T1793 (2320), T1795 (2324), T1852 (2549); Millennium_Paper_Outline (97, 99, 164); Clay_QuestionHasNoise (40, 48); GC3_Dim4_Gap docs. All the "R⁴ mass-gap core / scale-free / renormalization" ℝ⁴.
- **Lorentzian ℝ^{1,3} (physical):** registry:8479 ("D_IV⁵ → ℝ⁴ full spacetime"); **Paper67:142/154** ("Šilov ≅ ℝ⁴" — must read (S³×S¹)/ℤ₂ Lorentzian (3,1), NOT ℝ⁴_E, and NOT homeomorphic — compactness refutes ≅, Round-41).
- **Paper67:144** — Cal's dead-selector row (separate withdrawal-tag fix, routed to Paper67's owner).

## Honest state + recommendation to @Keeper
- **Sweep is NOT clean.** 587 physics-relevant untagged ℝ⁴ mentions corpus-wide. Reporting it "clean" would be the report-vs-grep-zero error.
- **Scope the close:** the *dispatch* rows above are the pre-dispatch-blocking subset — tag those and re-run the gate scoped to the YM/Millennium docs → 0 to unblock. The full-corpus 587 is a tracked standing cleanup, owner-by-owner (each artifact tags its first-use), same discipline as the C₂↔n_C family.
- **The instrument is standing** — re-run the gate after any ℝ⁴ edit; it belongs beside the toy-5417 signature gate.

Edges: R41 signature-tag note (grace_regulator_to_physical_bridge...), T1793 (scale-free R⁴), registry:8479, Paper67. Nothing pushed; CP existence-only. — Grace, Round 42
