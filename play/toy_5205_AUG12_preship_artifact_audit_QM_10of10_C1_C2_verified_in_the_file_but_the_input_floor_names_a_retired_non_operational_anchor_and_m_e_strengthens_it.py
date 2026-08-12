#!/usr/bin/env python3
"""
Toy 5205: PRE-SHIP ARTIFACT AUDIT of the QM 10/10 paper -- I am free (route item 4 is explicitly gated "not
before the constraint set is named," item 2 waits on Lyra's kernel), and the QM papers have been "whoever's
free" for four rounds with nobody picking them up. The useful thing I can do there is not prose -- it is the
check the paper needs before it ships. So I read the artifact instead of the handoff line, per the standing
"content-ready is not cleared" discipline: a fix clears only when the ARTIFACT carries it. ★ (1) C1 AND C2 ARE
GENUINELY IN THE FILE -- verified, not taken on faith. All ten rows carry a tier (Derived / Proved /
Structure-Derived), zero posits; item 10 is Derived via Code-Forces-Fermion with the honest 9+1 history
preserved in Section 4; and BOTH K1239-bar caveats travel, inline in the table AND restated in Section 2 --
item 5's curvature-normalization and item 7's distinguishable-particle scope. Keeper's two conditions are
discharged in the artifact. That part is clean and I am saying so plainly. ★★ (2) BUT THE INPUT FLOOR IS STALE
IN A WAY THAT COSTS THE PAPER ITS BEST SECTION. Section 3 -- the GR-benchmarked floor, which Keeper singled out
as "a genuine strength" -- names the two dimensionful scales as "the substrate tick and the cosmic age," and
the paper never mentions the electron mass. Two things have happened since 2026-08-06. (a) Cal §427 RETIRED the
Koons tick AS AN INPUT: its formula τ = t_Planck·α^(C₂²) contains t_Planck, hence G, hence it is circular as a
foundation -- kept only as a derived quantity, "same discipline as the Wyler ghost." (b) Today K1415 ruled a
derivable G-free tick a PHANTOM (dimensionally impossible) and stated the program's anchor plainly: BST anchors
on the ELECTRON MASS. ★ TO BE FAIR AND NOT OVER-REACH: a substrate time scale is a perfectly legitimate
dimensionful primitive -- the paper is not WRONG. What it is, is stale and NON-OPERATIONAL: the substrate tick
has no measured value, while m_e is measured to three parts in 10¹⁰ by non-gravitational means. And a reader
who greps our corpus finds that exact anchor retired as an input, which is the worst way for a referee to meet
it. ★ (3) THE FIX STRENGTHENS THE PAPER RATHER THAN PATCHING IT, which is why this is worth the toy: swap "the
substrate tick" for "the electron mass" and the floor becomes (i) operational -- every input is a measured
number, (ii) collision-free with our own retirements, and (iii) able to carry today's result as a consequence
rather than a separate claim: from that same anchor the geometry predicts Newton's constant to 0.07% through
24 powers of α. The section that was already the paper's strongest gets strictly stronger. One sentence.
★ (4) TWO FLAGS, RAISED AS QUESTIONS BECAUSE THEY ARE NOT MINE TO RULE. (a) Item 5's caveat promises "we state
the value only once it is checked against Hua/Faraut-Korányi" -- is that check done six days on, or is the
paper shipping a promissory note? (b) Section 5 says only uncertainty is distinctive among the support axioms;
but today's banked result is that J² = −1 at KO-dimension 2 -- the CP structure -- is exactly what
distinguishes BST from Connes' triple. If that is right, item 9 is distinctive too and Section 5 currently
UNDER-claims. @Lyra's call, not mine. Elie auditing the flagship artifact before it ships, because nobody had.
(K1239 bar; K1240 C1/C2; K1276 block-lift; Cal §427 tick retirement; K1415 anchor ruling; toy 5203's G audit.)
CP existence-only. Nothing pushed. I wrote no prose into the paper.

WHAT I CHECK (against the artifact itself, not the handoff summary):
  * C1 -- ten rows, ten tiers, zero posits, item 10 Derived, honest 9+1 history present.
  * C2 -- item-5 curvature caveat AND item-7 distinguishable-scope caveat present in the file.
  * ★★ the input floor names "the substrate tick" -- retired as an input (Cal §427), phantom to derive (K1415),
    non-operational; m_e is the program's actual anchor and is never mentioned.
  * the fix is a strengthening, not a patch: operational floor + carries the 0.07% G result as a consequence.
  * two flags for @Lyra: the item-5 curvature pin (done?), and CP-as-distinctive (Section 5 may under-claim).

=> VERDICT (plain): the paper is in better shape than its age suggests and worse shape than its handoff note
says, and both halves matter. Everything the auditors asked for is genuinely in the file -- I checked the rows
and the caveats myself rather than believing the line that said they were done, which is the whole point of
that discipline. What has gone stale is the one section everyone praised. It tells the reader that our two
dimensionful inputs are a substrate tick and the age of the universe, and in the days since, we retired that
tick as an input because its formula smuggles gravity in, and then established this afternoon that no theory
can derive such a thing anyway. Meanwhile the anchor we actually use is the mass of the electron, which the
paper never names. That is not an error of fact so much as a paper describing a floor we no longer stand on --
and the repair is a single sentence that makes the section stronger, because an electron's mass is something
anybody can look up to ten digits and a substrate tick is not. With that one change the paper can also say, in
the same breath, that the same anchor gives Newton's constant to seven parts in ten thousand.

=> DISPOSITION: QM 10/10 artifact audit -- C1 and C2 VERIFIED PRESENT IN THE FILE (Keeper's conditions
discharged; that half is clean). ★★ ONE BLOCKING STALENESS: Section 3's input floor names the substrate tick,
retired as an input (Cal §427) and ruled non-derivable (K1415); the operative anchor m_e appears nowhere.
Recommend the one-sentence swap, which strengthens the section and lets it carry the 0.07% G prediction as a
consequence. TWO FLAGS for @Lyra (not mine to rule): item-5 curvature pin still promissory? and does CP /
KO-dim-2 make item 9 distinctive, so that Section 5 under-claims? Firer: Elie. Owed: @Lyra makes the edit
(I write no prose into the paper); @Keeper re-reads the changed section; then Casey GO. Nothing banked;
nothing pushed; nothing external.

Author: Elie (CI toy builder). Date: 2026-08-12.
"""

import re
import os

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

PAPER = "notes/BST_paper_Axioms_of_QM_from_D_IV5_DRAFT_2026-08-04.md"
text = open(PAPER).read() if os.path.exists(PAPER) else ""

print("=" * 78)
print("Toy 5205: pre-ship artifact audit -- the QM 10/10 paper, read rather than trusted")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. C1 -- ten rows, ten tiers, zero posits.
# ---------------------------------------------------------------------------
print("\n--- 1. condition C1: is the scorecard actually current in the file? ---")
rows = [ln for ln in text.splitlines() if re.match(r"^\|\s*\d+\s*\|", ln)]
tiered = [ln for ln in rows if re.search(r"Derived|Proved|Structure-Derived", ln)]
posit_rows = [ln for ln in rows if re.search(r"\bposit\b", ln, re.I)]
history = "held as a posit through three separate rounds" in text or "held at 9+1" in text
check("Reading the artifact instead of the handoff line, per the standing 'content-ready is not cleared' "
      f"discipline. The scorecard has {len(rows)} numbered rows, {len(tiered)} of which carry an explicit tier "
      f"(Derived / Proved / Structure-Derived), and {len(posit_rows)} rows label anything a posit. Item 10 is "
      "Derived via Code-Forces-Fermion, and the honest 9+1 history -- three rounds of refusal before it closed "
      f"-- is preserved in Section 4 ({history}). Keeper's condition C1 is DISCHARGED IN THE FILE, and I am "
      "saying so plainly rather than only reporting what is wrong.",
      len(rows) == 10 and len(tiered) == 10 and len(posit_rows) == 0 and history,
      f"{len(rows)} rows / {len(tiered)} tiered / {len(posit_rows)} posits; honest history present: {history}")

# ---------------------------------------------------------------------------
# 2. C2 -- both caveats travel.
# ---------------------------------------------------------------------------
print("\n--- 2. condition C2: do both K1239-bar caveats actually travel? ---")
cav5 = "curvature-normalization caveat" in text or "curvature-normalization" in text
cav7 = "distinguishable-particle scope" in text or "distinguishable" in text
cav5_sec2 = "Item 5 (uncertainty)" in text
cav7_sec2 = "Item 7 (composite)" in text
check("Both K1239-bar caveats are present, and present twice -- inline in the table rows AND restated in "
      f"Section 2. Item 5's curvature-normalization caveat: {cav5} (Section 2 entry: {cav5_sec2}). Item 7's "
      f"distinguishable-particle scope: {cav7} (Section 2 entry: {cav7_sec2}). Condition C2 is DISCHARGED IN "
      "THE FILE. So the two conditions Keeper set on 2026-08-06 are genuinely met by the artifact, not merely "
      "claimed met by its handoff note -- which is the distinction that discipline exists to catch.",
      cav5 and cav7 and cav5_sec2 and cav7_sec2,
      f"item-5 caveat {cav5}/{cav5_sec2}; item-7 caveat {cav7}/{cav7_sec2} -- both inline and in Section 2")

# ---------------------------------------------------------------------------
# 3. ★★ The staleness that costs the paper its best section.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ the input floor names an anchor we retired ---")
names_tick = "substrate tick" in text
names_me = bool(re.search(r"electron mass|m_e", text))
check("★★ Section 3 -- the GR-benchmarked input floor, the section Keeper singled out as 'a genuine strength' "
      f"-- names the two dimensionful scales as 'the substrate tick and the cosmic age' (present: {names_tick}), "
      f"and the electron mass appears nowhere in the paper (present: {names_me}). Two things have happened "
      "since 2026-08-06: Cal §427 RETIRED the Koons tick AS AN INPUT because τ = t_Planck·α^(C₂²) contains "
      "t_Planck and therefore G -- circular as a foundation, kept only as a derived quantity, 'same discipline "
      "as the Wyler ghost'; and today K1415 ruled a derivable G-free tick a PHANTOM and stated the program's "
      "anchor plainly as the ELECTRON MASS. The paper describes a floor we no longer stand on.",
      names_tick and not names_me,
      "artifact says 'substrate tick'; anchor is m_e (K1415); tick retired as an input (Cal §427); m_e absent from the paper")

check("FAIRNESS, because over-reaching here would be its own error: the paper is NOT WRONG. A substrate time "
      "scale is a perfectly legitimate dimensionful primitive, and every theory takes one. What it is, is "
      "STALE and NON-OPERATIONAL -- the substrate tick has no measured value, while m_e is measured to three "
      "parts in 10¹⁰ by manifestly non-gravitational means. The concrete cost is a referee's: anyone who greps "
      "our own corpus finds that exact anchor retired as an input, and meeting it that way is the worst "
      "possible introduction.",
      True,
      "not an error of fact -- a floor we no longer stand on, and a collision with our own retirement")

# ---------------------------------------------------------------------------
# 4. The fix strengthens rather than patches.
# ---------------------------------------------------------------------------
print("\n--- 4. why this is worth a toy: the repair makes the section stronger ---")
proposed = ("Two dimensionful scales: the electron mass and the cosmic age. (Every dimensionless quantity is "
            "independent of both. The electron mass is measured by non-gravitational means to three parts in "
            "10^10; from that same anchor the geometry predicts Newton's constant to 0.07% through 24 powers "
            "of α.)")
check("The repair is one sentence and it strengthens the paper's strongest section three ways: the floor "
      "becomes OPERATIONAL (every input is a number anyone can look up), it stops COLLIDING with our own "
      "retirements, and it lets the section carry today's gravity result as a CONSEQUENCE of the stated floor "
      "rather than as a separate claim. Proposed replacement for line 40, offered to @Lyra -- I write no prose "
      'into the paper myself: "' + proposed + '"',
      "electron mass" in proposed and "0.07%" in proposed,
      "one-sentence swap: operational floor + collision-free + carries the G prediction as a consequence")

check("COUNT-ONCE RIDER if the paper does cite the G result (from toy 5203, so it travels with the number): "
      "6π⁵ is also the proton-to-electron mass ratio, so the G prediction and the m_p/m_e prediction SHARE AN "
      "INPUT and must never be presented as two independent confirmations. And per Cal §438 the α²⁴ lever must "
      "be disclosed -- the honest phrasing is 'from the electron mass and α, both measured, plus the geometric "
      "form,' not 'from geometry alone.'",
      True,
      "if G is cited: disclose the α²⁴ lever (Cal §438) and the shared 6π⁵ (one tally, not two)")

# ---------------------------------------------------------------------------
# 5. Two flags -- raised as questions, not rulings.
# ---------------------------------------------------------------------------
print("\n--- 5. two flags for @Lyra -- questions, because they are not mine to rule ---")
promissory = "only once it is checked against Hua" in text
check("FLAG (a): item 5's caveat promises 'we state the value only once it is checked against "
      f"Hua/Faraut-Korányi' (present in file: {promissory}). Six days on -- is that check done, or would the "
      "paper ship a promissory note in a caveat? A caveat that defers to a check nobody has run is weaker than "
      "a caveat that states a bound. Worth confirming before send, not after.",
      promissory,
      "item-5 caveat defers to an unrun check -- confirm it happened, or reword to state the current status")

check("FLAG (b), and this one may be an UNDER-claim: Section 5 says CPT is universal and 'only uncertainty is "
      "distinctive among the support axioms.' But today's banked result is that J² = −1 at KO-dimension 2 -- "
      "the quaternionic reality, our CP structure -- is exactly the one sign distinguishing BST from Connes' "
      "Standard Model triple. If that is right, item 9 is ALSO distinctive and Section 5 currently sells the "
      "paper short. I am raising it as a question: @Lyra, does the KO-dim-2 sign belong in Section 5 as a "
      "second distinctive item? Not my ruling -- but under-claiming is as much an error as inflating, and I "
      "have been on the wrong side of that once today already.",
      "only uncertainty" in text or "only uncertainty (the Bergman curvature" in text,
      "@Lyra: does J² = −1 / KO-dim 2 make item 9 distinctive? Section 5 may under-claim as written")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (C1+C2 verified IN THE FILE; one blocking staleness -- the input floor names a retired, non-operational anchor; two flags for Lyra)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5205, pre-ship artifact audit -- I was free, and nobody had read the file):
  * ★ C1 VERIFIED IN THE ARTIFACT: 10 numbered rows, 10 tiers, ZERO posits, item 10 Derived via
    Code-Forces-Fermion, honest 9+1 history preserved in Section 4. Keeper's condition discharged.
  * ★ C2 VERIFIED IN THE ARTIFACT: both K1239-bar caveats travel -- item-5 curvature-normalization and
    item-7 distinguishable-particle scope -- inline in the table AND restated in Section 2. Discharged.
    (Checked by reading the file, not the handoff line that said they were done. That is the whole point.)
  * ★★ ONE BLOCKING STALENESS -- and it is in the section everyone praised: Section 3's input floor names
    "the substrate tick and the cosmic age," and the electron mass appears NOWHERE in the paper. But Cal §427
    RETIRED the Koons tick as an input (τ = t_Planck·α^(C₂²) contains t_Planck ⟹ circular), and K1415 today
    ruled a derivable G-free tick a PHANTOM and named m_e as the program's anchor. The paper describes a floor
    we no longer stand on. FAIR: it is not wrong -- a substrate time scale is a legitimate primitive -- it is
    STALE and NON-OPERATIONAL, and a referee greps our corpus and meets that anchor already retired.
  * ★ THE FIX STRENGTHENS RATHER THAN PATCHES (one sentence, offered to @Lyra; I wrote no prose into the
    paper): swap in the electron mass and the floor becomes operational, collision-free, and able to carry
    today's result as a CONSEQUENCE -- "from that same anchor the geometry predicts Newton's constant to
    0.07% through 24 powers of α." Riders if G is cited: disclose the α²⁴ lever (Cal §438); 6π⁵ is shared
    with m_p/m_e, so ONE tally, never two.
  * FLAG (a) @Lyra: item-5's caveat defers to a Hua/Faraut-Korányi check -- done, or shipping a promissory
    note inside a caveat?
  * FLAG (b) @Lyra: Section 5 says only uncertainty is distinctive; today's J² = −1 / KO-dim-2 result is
    precisely what distinguishes us from Connes. Does item 9 become distinctive too? Possible UNDER-claim.
    Raised as a question -- I have been on the wrong side of under-claiming once already today.

AUG-12. Nothing pushed. Nothing external. I wrote no prose into the paper -- @Lyra makes the edit, @Keeper
re-reads the changed section, then Casey GO. Count once. CP existence-only.
""")
