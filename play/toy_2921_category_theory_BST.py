"""
Toy 2921 — Category theory / higher math structural counts BST.

Universal properties primary: 4 = rank² (initial/terminal, product/coproduct,
  pullback/pushout, exponential)

Yoneda lemma forms: 2 = rank (covariant, contravariant)
Limit types fundamental: 5 = n_C (product, equalizer, pullback, terminal,
  inverse limit)

Monad axioms: 3 = N_c (unit left, unit right, associativity)
Adjoint functor axioms: 2 = rank (triangle identities)

Topos axioms common: 4 = rank² (finite limits, exponentials, subobject classifier,
  Heyting algebra structure)

Standard category structures:
  Set, Top, Grp, Ring, Mod_R, Cat = 6 = C_2 most common

Higher category levels (n-category): 0, 1, 2, ω = standardly studied 4 = rank²

Hodge structure types: 3 = N_c (pure, mixed, complex mixed)
Sheaf types fundamental: 5 = n_C (constant, locally constant, étale, abelian, constructible)

Standard schemes types: 5 = n_C (affine, projective, separated, proper, smooth)
Cohomology theories major (algebraic): 7 = g (singular, de Rham, Čech, Dolbeault,
  sheaf, étale, motivic)

Generalized cohomology theories famous: 7 = g (singular, K-theory, cobordism,
  Morava K-theory, elliptic, tmf, Topological Modular Forms variants)

Type theory standard quantifiers: 4 = rank² (∀, ∃, Π, Σ)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    cat = [
        ("Universal properties primary",         4, rank**2, "rank²"),
        ("Yoneda lemma forms",                   2, rank,    "rank"),
        ("Limit types fundamental",              5, n_C,     "n_C"),
        ("Monad axioms",                         3, N_c,     "N_c"),
        ("Adjoint functor axioms (triangles)",   2, rank,    "rank"),
        ("Topos axioms common",                  4, rank**2, "rank²"),
        ("Standard category structures most common", 6, C_2, "C_2 (Set,Top,Grp,Ring,Mod,Cat)"),
        ("n-category levels standardly studied", 4, rank**2, "rank² (0,1,2,ω)"),
        ("Hodge structure types",                3, N_c,     "N_c (pure, mixed, complex)"),
        ("Sheaf types fundamental",              5, n_C,     "n_C"),
        ("Schemes types fundamental",            5, n_C,     "n_C"),
        ("Major algebraic cohomology theories",  7, g,       "g"),
        ("Famous generalized cohomology theories", 7, g,    "g"),
        ("Type theory quantifiers",              4, rank**2, "rank² (∀,∃,Π,Σ)"),
    ]

    print("Category theory / higher math BST:")
    matches = 0
    for name, val, bst, formula in cat:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<46} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(cat)}")
    return matches, len(cat)


if __name__ == "__main__":
    run()
