"""
Toy 2902 — Neural network / biological signaling BST.

Synapse types: 2 = rank (excitatory, inhibitory)
Neurotransmitter major categories: 7 = g (amino acid, monoamine, peptide,
  purine, gasotransmitter, lipid, acetylcholine)
Standard cortical layers (neocortex): 6 = C_2 (I-VI)
Cerebellar cortical layers: 3 = N_c

Action potential phases: 4 = rank² (depolarize, repolarize, hyperpolarize, refractory)
Major brain circuits (basal ganglia loops): 5 = n_C (motor, oculomotor,
  associative, limbic, orbitofrontal)

Standard receptor classes: 4 = rank² (ionotropic, GPCR, kinase, nuclear)
GPCR conformational states: 3 = N_c (active, inactive, intermediate)
Transcription factor DNA binding motif length common: ~7 = g bp

Reflex arc components: 5 = n_C (receptor, sensory, integrator, motor, effector)
Glial cell types: 4 = rank² (astrocyte, oligodendrocyte, microglia, ependyma)

Vision photoreceptor types human: 4 = rank² (3 cones S/M/L + 1 rod)
Taste primary categories: 5 = n_C (sweet, sour, salty, bitter, umami)
Smell receptor families (in fish): 5-7 = n_C to g

Heart chambers: 4 = rank²
Lung lobes: 5 = n_C (3 right + 2 left)
Liver lobes: 4 = rank²
Spleen anatomical lobes: typical 1 = trivial
Pancreatic functional regions: 3 = N_c (head, body, tail)

Standard ML activation functions classic: 5 = n_C (sigmoid, tanh, ReLU,
  LeakyReLU, GELU)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    neuro = [
        ("Synapse types",                       2, rank, "rank (excit/inhib)"),
        ("Neurotransmitter major categories",   7, g, "g"),
        ("Neocortex layers",                    6, C_2, "C_2 (I-VI)"),
        ("Cerebellar cortex layers",            3, N_c, "N_c"),
        ("Action potential phases",             4, rank**2, "rank²"),
        ("Basal ganglia loops",                 5, n_C, "n_C"),
        ("Standard receptor classes",           4, rank**2, "rank²"),
        ("GPCR conformational states",          3, N_c, "N_c"),
        ("Reflex arc components",               5, n_C, "n_C"),
        ("Glial cell types",                    4, rank**2, "rank²"),
        ("Human photoreceptor types",           4, rank**2, "rank² (3 cones + rod)"),
        ("Taste primary categories",            5, n_C, "n_C"),
        ("Heart chambers",                      4, rank**2, "rank²"),
        ("Lung lobes total",                    5, n_C, "n_C (3R+2L)"),
        ("Liver lobes",                         4, rank**2, "rank²"),
        ("Pancreas regions",                    3, N_c, "N_c (head/body/tail)"),
        ("ML activation functions classic",     5, n_C, "n_C"),
    ]

    print("Neural / biological networks BST:")
    matches = 0
    for name, val, bst, formula in neuro:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(neuro)}")
    return matches, len(neuro)


if __name__ == "__main__":
    run()
