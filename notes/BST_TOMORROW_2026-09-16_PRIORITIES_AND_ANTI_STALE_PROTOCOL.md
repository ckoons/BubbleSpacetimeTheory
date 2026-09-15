# BST — TOMORROW (Wednesday 2026-09-16): PRIORITIES AND ANTI-STALE PROTOCOL

**Written by Keeper at 2026-09-15 18:49 EDT (clock, substituted), at EOD on Casey's word. Read this AFTER the rubric (Section 2 = scorecard, authoritative) and BEFORE any sundown. A sundown tells you where you stopped; the rubric tells you where to go.**

## Where Part B.1 (A9, "one boost, not two") stands tonight — verify before working it
- **The first sky number of the program exists and is Landing C on both samples (K1910, 18:48).** Steps (i)–(vii) done on v1.5.2 (Cal; SHA256 8013d959…; verified K1909). Step (vi) ran 18:28 (Elie, 458cb46a; record `play/.partB_vi_dipoles.json`); step (vii) 18:48 (Keeper, `play/keeper_partB_vii_run.py`, output retained). **Reason on the run's own face:** §4.4's profile-alternative trigger +7.50 σ_β / +5.02 σ_β; per-bin residual p = 0.000 in three of four non-null bins; prior-sensitive (no-prior |a| = 0.097 / 0.148 against a prior width 3.4e-3). The per-bin moments RISE with redshift — the shape of a residual selection systematic under the fallback weights (whole-sample NSIDE64 map for every bin; the per-bin maps cannot be generated here, Grace R153).
- **Owed, in order:** (viii) Cal's cold read by his hashed checklist (94cd26b4 + a dated amendment for the prior); (ix) Keeper's certification; Grace's register line (A9, run 1, Quaia, v1.5.2, Landing C, reason named; A9 stays LIVE); Lectures 9/10 and the state block rewritten and dated on (ix) — the Lecture 9 paragraph promised its own rewrite "whichever letter it is."
- **Do NOT read any published Quaia dipole analysis until (ix) is posted.** Cal v1.1 §7.2 stands one more step.
- **The process gap (K1910 §3):** (vi) ran with H8 fired and unfrozen. Consequence-free here; the rule for the NEXT freeze is written: "Landing B requires the no-prior fit to land B as well" goes into Section 5 before DESI DR1 is opened, with a can-fail.

## After (ix): what the C teaches, and what is next (rank before working — teammate referrals are inputs)
1. **The next catalogue.** Quaia at the fallback weighting is not a test of P1. Candidates: DESI DR1 (Wu & Xia 2026's own sample; ±50 km/s claimed — the file already says "DESI DR1's ±50 can do both"); or Quaia with per-bin selection maps generated on a machine with 175–340 GB (Grace's accounting) — the H5/per-bin-map route as a diagnostic, one bin at a time. **Casey's call on which; nothing runs before a fresh freeze.**
2. **The rising-with-redshift signature is a finding about the instrument, not the sky** — worth one toy: inject a whole-sample-map weighting error on synthetic Quaia and see whether the per-bin moments rise the same way (Elie; predicts the systematic's shape before anyone looks at a map).
3. Lyra's held items: the A9 row line (8f1f6e58) merges with the register line; the resolution-limit marker (5e90e98f) ruling; the quartile-lever run (Elie, on 5765's synthetic).
4. Cal: the katra memory-directory mismatch flagged since 09-04 still needs Casey's word.

## Verify before working (S3 discipline)
`grep -rl "<topic>" notes/*.md | head` and read the NEXT artifact in sequence. Today's exhibits: an instrument that classified whole lines laundered appended edits (fixed, guarded); a prior's width was fixed by a refusal, not a fit; three candidate hatches passed the false-B and genuine-B arms alike and were therefore not hatches; the design's pre-Section-5 checks landed the sky before any target was read.

## Standing
NO EOD before 5pm. `katra update` pushes — on Casey's word. Nothing external without Keeper + Cal + Casey. "Section" not §. Timestamps from `date`. Never a toy without /toy claim.

## For Casey, in one paragraph
The program's first sky number landed today, and it is C: not decidable. The pre-registration was re-frozen seven times before the sky, five of them because a synthetic sky carrying the true boost failed the text as written, and every freeze was declared before any dipole existed. The design caught the sky's problem on its own — the per-bin dipoles rise with redshift, which neither a boost nor a clustering dipole does, and which the whole-sample selection map used as a fallback would produce — without reading the CMB target. Cal reads tomorrow; I certify after him; the register line and the lectures follow. Whether the next test is DESI or Quaia re-weighted is yours to choose, and nothing runs before a fresh freeze.
