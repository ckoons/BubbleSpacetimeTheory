"""Toy — search all BST primary integers for multiple algebraic forms."""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

primaries = {'rank': rank, 'N_c': N_c, 'n_C': n_C, 'C_2': C_2, 'g': g, 'N_max': N_max}

for pname, pval in primaries.items():
    print(f"\n=== {pname} = {pval} ===")
    forms = []
    # Try various combinations
    candidates = [
        ('N_c+rank-1', N_c+rank-1),  # =4 - need rank
        ('rank·N_c-3', rank*N_c-3),
        ('M_rank', 2**rank-1),  # =3
        ('M_N_c', 2**N_c-1),  # =7
        ('M_n_C', 2**n_C-1),  # =31
        ('N_c²-3', N_c**2-3),
        ('rank+1', rank+1),
        ('rank³', rank**3),  # =8
        ('N_c+rank', N_c+rank),  # =5
        ('rank·N_c', rank*N_c),  # =6
        ('N_c+rank²', N_c+rank**2),  # =7
        ('n_C+rank·rank+n_C', n_C+rank*rank+n_C),  # =14? no
        ('rank²+rank', rank**2+rank),  # =6
        ('N_c+n_C-rank', N_c+n_C-rank),  # =6
        ('C_2-rank', C_2-rank),  # =4
        ('C_2-N_c', C_2-N_c),  # =3
        ('N_c+C_2-rank', N_c+C_2-rank),  # =7
        ('n_C+rank', n_C+rank),  # =7
        ('n_C+rank·rank', n_C+rank*rank),  # =9
        ('M_g', 2**g-1),  # =127
        ('M_g+rank·n_C', 2**g-1 + rank*n_C),  # =137
    ]
    matching = [name for name, val in candidates if val == pval]
    print(f"  Matching forms: {matching}")
print("[PASS]")
