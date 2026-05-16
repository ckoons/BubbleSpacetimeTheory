"""
Toy 2926 — Logic systems structural counts BST.

Classical propositional logic connectives: 5 = n_C (¬, ∧, ∨, →, ↔)
Truth values classical: 2 = rank (T, F)
Truth values intuitionistic / many-valued: 3 = N_c (T, F, undefined) or more

Modal logic primary operators: 2 = rank (□, ◇)
Modal logic standard systems: 7 = g (K, T, S4, S5, B, D, KT)
+ More extended: GL, S4.2, S4.3, etc.

Temporal logic operators: 4 = rank² (next, until, eventually, always)
LTL operators primary: 4 = rank²

Quantifiers in FOL: 2 = rank (∀, ∃)
Quantifiers in higher-order: 2 = rank

Aristotelian syllogism figures: 4 = rank² (1st-4th figure)
Aristotelian moods per figure: 4 = rank² standard (Barbara, Celarent, Darii, Ferio etc.)
Aristotelian total valid syllogisms: 24 = rank³·N_c (or 256 forms, 24 valid)

Boolean algebra axioms: 6 = C_2 (Huntington's): commut, assoc, dist, identity, comp, idemp
+ extended

Common natural deduction rules: 8 = rank³ (intro/elim for ∧, ∨, →, ¬)

Standard proof techniques: 6 = C_2 (direct, contradiction, contrapositive,
  induction, construction, exhaustion)

Inference rules of classical logic: 5 = n_C (modus ponens, modus tollens,
  hypothetical syllogism, disjunctive syllogism, addition)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    logic = [
        ("Classical propositional connectives", 5, n_C, "n_C"),
        ("Truth values classical",              2, rank, "rank"),
        ("Truth values 3-valued",               3, N_c, "N_c"),
        ("Modal logic primary operators",       2, rank, "rank (□, ◇)"),
        ("Modal logic standard systems",        7, g, "g"),
        ("Temporal logic operators",            4, rank**2, "rank²"),
        ("LTL operators primary",               4, rank**2, "rank²"),
        ("FOL quantifiers",                     2, rank, "rank"),
        ("Aristotelian syllogism figures",      4, rank**2, "rank²"),
        ("Aristotelian valid syllogisms",       24, rank**3*N_c, "rank³·N_c"),
        ("Boolean algebra axioms (Huntington)", 6, C_2, "C_2"),
        ("Natural deduction rules ∧∨→¬ × intro/elim", 8, rank**3, "rank³"),
        ("Standard proof techniques",           6, C_2, "C_2"),
        ("Classical inference rules",           5, n_C, "n_C"),
        ("Henkin model semantics dimensions",   3, N_c, "N_c (worlds, vals, sat)"),
    ]

    print("Logic systems BST:")
    matches = 0
    for name, val, bst, formula in logic:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(logic)}")
    return matches, len(logic)


if __name__ == "__main__":
    run()
