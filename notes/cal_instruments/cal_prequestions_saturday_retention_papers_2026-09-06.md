# Cal — referee pre-questions, written BLIND before opening any of the three 09-05 papers
Stamped: 2026-09-06 (Sun) 08:5x EDT. Inputs used: the three titles, Lyra's 08:18/08:45 board posts, Keeper's K1861 summary. Nothing from the PDFs, nothing from the working record.

Purpose: the referee's objection goes on paper BEFORE the team's answer is read. Scored after.

## Domain calibration (what the outside referee already knows, from memory — each pin owed a source before it is cited in a verdict)
Population genetics / information:
- Kimura 1961, "Natural selection as the process of accumulating genetic information" — the bits-per-generation framing is sixty-five years old.
- Worden 1995 (J. Theor. Biol.), "A speed limit for evolution" — ~1 bit per generation per population under selection.
- MacKay 2003, ITILA ch. 19 "Why have sex?" — asexual ~1 bit/gen, sexual ~√G bits/gen; recombination AS a channel is textbook.
- Hledík, Barton, Tkačik 2022 (PNAS), "Accumulation and maintenance of information in evolution" — quantitative bit budgets, mutation–selection–drift; the closest modern competitor to any "meiotic channel" capacity claim.
- Watkins 2008, "Selective breeding analysed as a communication channel". Adami's "information theory of evolution" line.
- Haldane's cost of selection; Eigen error threshold (a Shannon-type bound on genome length × mutation rate).
Chemistry / stoichiometry:
- Conserved moieties = n_species − rank(S) is standard (Schuster & Höfer 1991; Feinberg's CRN theory; any metabolic-network text). If Theorem 8's stoichiometric form is stated as new, that is the referee's first strike.
Dynamics:
- Standard map: Greene's K_c ≈ 0.9716; island/regular fraction vs K is in Chirikov 1979 and Meiss 1992 (RMP 64, 795). A "measure of the non-mixing set" needs to be pinned to island measure (T → ∞ limit) or to a finite-horizon trapping fraction; these are different objects and the finite-horizon one is not a property of the map.
Thermodynamics of complexity:
- Landauer kT ln 2; Lotka 1922 maximum power; Morowitz; Kleiber 3/4; Herculano-Houzel neuron/energy scaling; Schneider & Kay. "Complexity exploits energy" as a thesis is not new; what would be new is a forced number.

## Pre-questions (blind)
P1. Meiotic paper: what is the channel — input alphabet, output alphabet, noise model? If capacity is quoted, is it a Shannon capacity (sup over input distributions) or a rate at one fixed input (the actual population)? Referees conflate these; so do authors.
P2. Meiotic: "49.6% seam loss" — a number that close to 1/2 is a Mendelian half by construction unless something breaks the symmetry. What is the 0.4% and is it inside the instrument's resolution?
P3. Meiotic: T + N = 1 is now labelled definitional (good). Does anything DOWNSTREAM still consume it as if it were a constraint (a "check" that cannot fail, a corollary that inherits the tautology)?
P4. Meiotic: does the novelty ledger cite MacKay's √G and Hledík–Barton–Tkačik? If the paper's bits/generation number sits inside their bounds, that is confirmation not novelty; if outside, that is a problem for the paper, not for them.
P5. Retention: R = log₂|V/Λ| — retention defined as a quotient count. Is Λ a lattice the dynamics forces, or one chosen so the number lands? (Target-innocence: what was Λ before the number was known?)
P6. Retention Theorem 8: "free transitive abelian action ⇒ R = log₂|V/Λ| exactly". Free AND transitive means V is a Λ-torsor — then V/Λ is a point and R = 0. Something in the statement must be off; read the hypothesis literally. Expect the intended statement to be: Λ acts freely on V, V/Λ finite, R counts orbits. Check whether "transitive" is a slip.
P7. Retention 9a: the standard-map paragraph — after the downgrade, does the paper still say anything the map forces? "Graded and horizon-dependent" is a description of the instrument, not of the map. The referee asks: what is the T → ∞ object, and does the paper claim it?
P8. Retention 9a "formal remark": the BST smuggling site. Expect a sentence of the form "the same quotient structure appears in D_IV⁵ / the height record / the Kempe class". A resemblance stated as a remark is fine; a resemblance used to TRANSFER a theorem is a derivation and contradicts the standing sentence.
P9. Complexity paper Section 11: after re-categorisation, every "measured" row must be able to FAIL. For each row: name the outcome that would have been reported as a miss. Bootstrap 2000/2000 cannot fail if the statistic is resampled from its own definition.
P10. Complexity: "ceiling slope 3.7, R² 0.9966" — slope of what against log of what, how many points, and is 3.7 predicted or fitted? A fitted slope with R² 0.9966 on ≤ 8 points is a description. If the paper predicts a number and gets 3.7, say what was predicted.
P11. Complexity: 10.4 K/bit — units are temperature per bit. That is kT ln 2 per bit divided by some heat capacity or an Arrhenius reading. Which, and is the constant forced or chosen?
P12. All three: "about one part in five new" — a ratio needs a denominator. Count the ledger rows; check that each "known" row has a citation and each "new" row has a search that could have found it known (search disease: one object, many names — "moiety conservation", "conserved quantity", "first integral", "stoichiometric invariant").
P13. All three: author line "Lyra and Casey" — for internal drafts fine; the standing sentence "no derivation to or from BST" must be in the abstract or Section 1 of each, not only in the board post.

## Predicted verdict shape (blind)
- Meiotic: PASS-with-fixes; the risk is a known-result collision on bits/generation, not an error.
- Retention: the one with a live hole; Theorem 8's hypothesis and 9a's remark are where the referee stops.
- Complexity: PASS-with-fixes; residual "measured" rows that are theorems of the construction.
