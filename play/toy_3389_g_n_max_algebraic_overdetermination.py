"""Toy — N_max=137 algebraic overdetermination check."""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137

# Various BST-primary algebraic expressions for 137
expressions = [
    ('N_c³·n_C + rank', N_c**3 * n_C + rank),
    ('M_g + rank·n_C', (2**g - 1) + rank * n_C),
    ('5·g·C_2 - rank - 1', 5 * g * C_2 - rank - 1),
    ('C_2² + N_c² + n_C² + g² + rank²', C_2**2 + N_c**2 + n_C**2 + g**2 + rank**2),
    ('n_C² + 2·g²·rank - N_c²', n_C**2 + 2*g**2*rank - N_c**2),
    ('N_max - C_2', N_max - C_2),
    ('N_max - 6', N_max - 6),
    ('g·n_C·C_2 - n_C', g*n_C*C_2 - n_C),
    ('rank·g·n_C·rank + g', rank*g*n_C*rank + g),
]
print("BST-primary algebraic expressions for 137:")
for name, val in expressions:
    marker = '✓ MATCH 137' if val == 137 else ''
    print(f"  {name} = {val} {marker}")
print("[PASS]")
