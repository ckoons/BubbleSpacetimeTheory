"""TOY 5692 — reaction networks as move graphs: R = n_species - rank(S), with the BASELINE STATED.
Lyra, 2026-09-06. Predictions .lyra_predictions_crn_baseline_2026-09-06.txt sha256 04a652ef,
registered before this file. Cal C-R4: Paper 3 10b's "catalysis destroys record" compared against
E and ES present-but-inert. Every verdict below is computed from the run's own values.
"""
import numpy as np

def R_of(species, reactions):
    """reactions: list of dicts species->stoichiometric coefficient. R = n - rank."""
    idx = {s: i for i, s in enumerate(species)}
    S = np.zeros((len(species), max(1, len(reactions))))
    for j, rx in enumerate(reactions):
        for s, c in rx.items(): S[idx[s], j] += c
    rank = np.linalg.matrix_rank(S) if reactions else 0
    return len(species) - rank, rank

out = {}
# Q1 honest baseline
out["Q1"] = R_of(["S","P"], [{"S":-1,"P":+1}])
# Q2 inert-enzyme artefact
out["Q2"] = R_of(["E","S","ES","P"], [{"S":-1,"P":+1}])
# Q3 Michaelis-Menten
mm = [{"E":-1,"S":-1,"ES":+1}, {"ES":-1,"E":+1,"S":+1}, {"ES":-1,"E":+1,"P":+1}]
out["Q3"] = R_of(["E","S","ES","P"], mm)
# Q4 H2 combustion chain, steps added in order
sp = ["H2","O2","H","O","OH","H2O"]
steps = [{"H2":-1,"H":+2}, {"H":-1,"O2":-1,"OH":+1,"O":+1}, {"O":-1,"H2":-1,"OH":+1,"H":+1},
         {"OH":-1,"H2":-1,"H2O":+1,"H":+1}, {"H":-1,"OH":-1,"H2O":+1}]
q4 = [R_of(sp, [])[0]] + [R_of(sp, steps[:k])[0] for k in range(1, 6)]
out["Q4"] = q4
# Q5 eight-species pool, chain of interconversions
pool = ["A%d" % i for i in range(1, 9)]
chain = [{"A%d" % i: -1, "A%d" % (i+1): +1} for i in range(1, 8)] + [{"A1": -1, "A8": +1}]
out["Q5"] = [R_of(pool, [])[0]] + [R_of(pool, chain[:k])[0] for k in range(1, 9)]
# Q6 catalyse step 4 of the chain with an enzyme
sp6 = sp + ["E", "E.OH"]
steps6 = steps[:3] + [{"E":-1,"OH":-1,"E.OH":+1}, {"E.OH":-1,"H2":-1,"H2O":+1,"H":+1,"E":+1}] + [steps[4]]
out["Q6"] = (R_of(sp, steps)[0], R_of(sp6, steps6)[0])

print("toy 5692: R = n_species - rank(S)")
for k, v in out.items(): print("  %s: %s" % (k, v))
verdict = {
 "Q1 S->P alone R=1": out["Q1"][0] == 1,
 "Q2 inert-enzyme artefact R=3": out["Q2"][0] == 3,
 "Q3 Michaelis-Menten rank 2, R=2": out["Q3"] == (2, 2),
 "Q3 vs Q1: catalysis ADDS a law (R 1 -> 2)": out["Q3"][0] == out["Q1"][0] + 1,
 "Q4 chain R = 6,5,4,3,2,2": out["Q4"] == [6,5,4,3,2,2],
 "Q5 pool R = 8,7,6,5,4,3,2,1,1": out["Q5"] == [8,7,6,5,4,3,2,1,1],
 "Q6 catalysing a step: R +1 (enzyme law added, none removed)": out["Q6"][1] == out["Q6"][0] + 1,
}
for k, ok in verdict.items(): print("  %s: %s" % (k, "HIT" if ok else "MISS"))
print("  Q4 dependent fifth step: %s" % ("HIT (delta 0)" if out["Q4"][5] == out["Q4"][4] else "MISS"))
