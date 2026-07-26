# K942 — CHECKABILITY AUDIT (the hook package's whole pitch is "run it yourself"): **the headline claims are TRUE and the toys run clean** — but TWO curation catches must be fixed before the package goes near Tegmark, because both are the exact thing a physicist's numerology-alarm fires on. The checkability weapon works; the curation around it needs two fixes.

**Keeper | 2026-07-26 Sun | I ran the toys the hook paper points at, as a reviewer would. The numbers hold. The presentation has two liabilities that would discredit the SM core by association — caught now, before external.**

## VERIFIED — the runnable claims are TRUE ✓
- **`verify_bst.py` → 49/50 at <1%** (EXACT 17, PASS 32, WARN 1, FAIL 0). The headline holds.
- **m_p/m_e = 6π⁵ = 1836.12 vs 1836.15 (0.0019%)** — the hook's proton beat is accurate (`verify T187`).
- **`toy_541` → 16/16, 51 quantities from 5 integers, 0 free parameters.**
- **N_max = N_c³·n_C + rank = 137** (α⁻¹); **6π⁵ = 1836.118** — both hook numbers confirmed by direct computation.
- **Null-model context present + honest:** BST 27/51 at <1% vs random-5-tuple mean 14.7, Z=2.9, p<0.0005 (distinguishable from numerology). Good, and exactly the kind of honesty the pitch needs.
- **Conclusion:** the "Physics is on GitHub, run it yourself" weapon is real. The foundation of the whole package holds.

## CATCH 1 (for the hook — LIABILITY): `verify_bst.py` mixes the SM CORE with the BREADTH
The 50-item list runs the proton mass next to **N_amino_acids = 20 [D] EXACT, N_codons = 64, DNA bases, the Kolmogorov exponent, a seismic v_P/v_S ratio, the phi meson, the Debye temperature of Pb.** This is precisely the sprawl the hook discipline says keep OUT of a first-contact package (prompt-o). **A physicist who runs this and sees "amino acids derived, EXACT" beside the proton mass hears numerology — and it discredits the SM core by association.** The breadth in the *headline runnable artifact* is a bigger liability than in prose, because the reviewer runs it themselves and sees it directly.
- **★ FIX (Elie):** a **curated SM-core verify** for the package — `verify_bst_SM.py` or a `--core` flag — showing ONLY the physics/SM predictions (masses, α, mixing, gauge, the LAW), NOT biology/geology/condensed-matter. The Tegmark package points at the *core* verify; the full one stays in the repo for the curious, clearly labeled "extended reach." Same weapon, aimed.

## CATCH 2 (hygiene — CONFUSION): the "49/50" vs "27/51" number clash in one output
The same `verify_bst.py` output prints **"49/50 at <1%"** as the headline AND **"BST matches 27/51 at <1%"** in the null-model line. Two different prediction sets (the 50-item curated verify vs the 51-item Toy-1543 null-model set), but a reviewer sees two different pass-rates in one screen and asks "which is it?" — and any unexplained inconsistency in the checkability output erodes exactly the trust the package is built on.
- **★ FIX (Grace/Elie):** reconcile — either make the null-model context match the headline set, or add one line explaining the two sets (the curated 50 vs the null-model 51) so the numbers are self-consistent on screen. For the hook, ONE clear headline number with a matching, explained null-model.

## Disposition
- **The checkability is confirmed real — the pitch's foundation is sound.** The two catches are curation, not correctness: the numbers are true; the presentation around them needs aiming (core-only) and self-consistency (the two pass-rates).
- **Both must be fixed before the Cal gate / before anything goes to Tegmark.** With a reader who runs the toys, the curated-core verify and the self-consistent numbers ARE the credibility — an over-broad or self-contradictory verify screen kills the "honest and checkable" pitch faster than any prose over-claim.
- Neither touches the SM derivations themselves — those run clean.

## Directions
- **★ ELIE — build the curated SM-core verify** (physics predictions only; the full one relabeled "extended reach") + reconcile the 49/50 vs 27/51 numbers in the output.
- **★ GRACE — ensure the reviewer-facing data (`bst_constants.json`) is tier-honest and the null-model set is consistent** with the curated verify.
- **★ CAL — when you gate the package, run the curated verify yourself** — confirm a cold reviewer sees a clean, self-consistent, SM-core result.
- **KEEPER — checkability confirmed real (headline TRUE); the two curation catches are the pre-Tegmark blockers.**

— Keeper K942, 2026-07-26. CHECKABILITY AUDIT (hook package): ran the toys as a reviewer would. TRUE: verify_bst.py 49/50, m_p/m_e=6π⁵=1836.12 (0.0019%), toy_541 16/16, N_max=137 — the "run it yourself" weapon is real, null-model honest (Z=2.9). CATCH 1 (liability): verify_bst.py mixes SM core with breadth (amino acids/DNA/seismic/Debye) — a physicist running it hears numerology; need a curated SM-CORE verify (Elie), full one relabeled extended-reach. CATCH 2 (confusion): "49/50" headline vs "27/51" null-model in one output — reconcile/explain (Grace/Elie). Both fix before the Cal gate / Tegmark. Numbers TRUE; presentation needs aiming + self-consistency. See [[team_prompt_2026-07-26o]], [[Keeper_K940_Millennium_RE_SCOPE]].