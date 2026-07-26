# Hook Paper — Opening Spec (for Lyra)

*Keeper, 2026-07-26. The opening of the Tegmark hook package's small paper. Casey's structure ("write it like a movie — short action scene, tagline, the α hook"), with the tier-honesty guardrails and the corrected Wyler history. This is the OPENING (~the first page); Lyra develops the rest.*

---

## The tagline (the literal opening line)
**"What is the smallest object that can do physics?"**
It is a *question*, not a claim — minimal, AC(0), and exactly what a Tegmark-class reader would ask. Everything opens from it.

## The beat structure (movie open — fast, each beat lands)
1. **The question** (the tagline) — if the universe is a mathematical structure, it should be the *smallest* one that carries the job.
2. **The assertion / action scene** (stated as the guess it was, "the guess is the story"): QM is 2D, GR is 3D; smallest closed 2D = a circle; circles tile a sphere = smallest closed 3D with a volume; a 1D channel carries the information, capacity 137. *(Plant, don't explain: the original picture was timeless — time entered later as the commitment rate. One clause, a forward hook, not a digression.)*
3. **The Wyler payoff** — 137 = 1/α; the number Wyler derived from a bounded symmetric domain (1969), and the guess reproduces it and says *why* (137 = the channel's capacity, read off the geometry).
4. **The honest-surprise beat** — computed m_p/m_e expecting the inconsistency that ends most such stories; got 6π⁵ = 1836.12 vs 1836.15 measured; never found it; six hundred numbers later still haven't. *(The EXPECTATION of failure is the credibility — keep it.)*
5. **"Run it yourself"** — `python3 verify_bst.py`, 50 predictions in 3 seconds. **"Physics fits on GitHub."**
6. **The ironic MUH reveal (the closing turn)** — only afterward did I recognize the object behind the guess is a single *forced, unique* bounded symmetric domain, D_IV⁵ — not one structure among Tegmark's many, but the one the constraints select. I had not set out to build a foundation for the MUH; the smallest-object question walked me into it.

## The rendered draft (shoot at it)
> **What is the smallest object that can do physics?**
>
> Not a theory of everything — a question. If the universe is at bottom a mathematical structure, it ought to be the *smallest* one that can carry the job. So: what is the least thing that can hold quantum mechanics, general relativity, and the exchange of information between them?
>
> Here is the guess this paper started from, stated the way it was first said, because the guess is the story. Quantum mechanics is two-dimensional; general relativity is three. The smallest closed two-dimensional object is a circle. Circles tile a sphere — the smallest closed three-dimensional object that bounds a volume. Between them runs a one-dimensional channel carrying the information, with a finite capacity. Work out that capacity and it is 137. *(The original picture was timeless; where time enters — as the rate at which the substrate commits — came later, and is Section [N].)*
>
> That number is not chosen to impress. 137 is 1/α, the fine-structure constant — the number Armand Wyler extracted from the volume of a bounded symmetric domain in 1969. The guess reproduces Wyler's result and supplies the thing his critics said it lacked: a reason. 137 is the channel's capacity, read off the geometry, not a radius set to one by hand.
>
> So we computed the next thing — the proton-to-electron mass ratio — expecting the inconsistency that ends most such stories. It came out 6π⁵ = 1836.12. Measured: 1836.15. We never found the inconsistency. Six hundred numbers later, we still haven't.
>
> You don't have to take that on faith, and that is the point. The whole thing is a public repository you can run: `python3 verify_bst.py` checks fifty predictions against measurement in three seconds. Physics, it turns out, fits on GitHub.
>
> And only afterward did I recognize what the object behind the guess actually is. The configuration space those choices force is a single, unique bounded symmetric domain — D_IV⁵ — not one mathematical structure among many, but the one the constraints *select*. I had not set out to build a foundation for the Mathematical Universe Hypothesis. The smallest-object question walked me into it.

## The Wyler lineage — CORRECTED from the archive (use THIS; it's stronger)
The remembered version ("Robertson killed it with a dismissive letter, correct work ignored for status") is not quite what the record says — and the accurate version is *better for us*, because BST answers the recorded objection.
- **Wyler (Swiss mathematician), 1969:** first exact formula for α from the Euclidean volumes of bounded symmetric domains, tied to the invariance group O(n,2) of the wave equation. Agreed with experiment to **±1.5 ppm.**
- **Freeman Dyson invited him to the Institute for Advanced Study (Princeton), 9/1971–6/1972.** It was taken seriously by a great physicist.
- **Gloria Lubkin, "A Mathematician's Version of the Fine-Structure Constant," *Physics Today* 24(8), 1971** — the public attention.
- **The critique — Robertson, *Phys. Rev. Lett.* 27, 1545 (1971)** — and this is the key: it was **specific and fair, not a status-dismissal.** Robertson's objection was that Wyler's expression matches experiment **only if the radius of the spaces is arbitrarily set to 1, with no physical reason given** (the relation to the invariance group is radius-independent). AND Robertson wrote that α "might be derivable theoretically" and that **"Wyler's number appears to have better chances to be derived from a theory than any of the other numbers that also agree with experiment."** The critic thought it was the *most promising* such number.
- **Why it was dismissed:** not because it was shown wrong — because **Wyler could not put it in a convincing physical context** / justify the normalization. The community then filed it under numerology.
- **★ THE FRAME FOR US:** BST supplies exactly the missing piece Robertson named. The domain is not chosen — it is **forced** (the unique D_IV⁵), and the normalization is its **intrinsic Bergman / Faraut–Korányi measure**, not a radius set to one by hand. Robertson's specific, recorded objection — *why radius = 1?* — is answered by *because the geometry is forced and carries its own measure.* We are not reviving a dismissed curiosity; we are closing the exact gap the referee flagged, fifty-plus years on. That is a cleaner and more honest hook than "ignored for sociology."
- *(Primary-source check before publishing: confirm Robertson's initials/identity and quote from PRL 27, 1545 directly; the critique-content above is from the secondary record and is consistent, but quote the primary.)*

## Tier-honesty guardrails (with this reader, honesty IS the credibility)
1. **Keep the intuition and the rigor on different lines.** The circle-tiles-a-sphere story is the *journey* (label it a guess); "D_IV⁵ is forced/unique" is the *claim* (the uniqueness argument does the work). Draw the seam yourself so the reader doesn't have to hunt for it.
2. **"Reproduces Wyler / supplies the reason"** is the honest verb for α — it is an IDENTIFICATION (the integer 137 forced, the exact value matched), not a proof of α. Do not upgrade it.
3. **"Six hundred numbers, no inconsistency"** is a consistency claim, not "all derived" — it is true and it is a hook; keep it about consistency, not derivation.
4. **Plant time, don't explain it** (beat 2's parenthetical) — the commitment-rate mechanism is a payoff three sections in, not opening material.
5. The scope page (`BST_What_We_Claim_And_Do_Not...`) is the companion — the opening seduces, the scope page keeps it honest; both ship together.

— Keeper, 2026-07-26. For Lyra (hook-paper lead). Companion: the scope spine (Keeper), the curated toys (Elie), the tier-ledger (Grace). Cal gate before Tegmark; nothing sent without Casey's direction.