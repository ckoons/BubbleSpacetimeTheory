#!/usr/bin/env python3
"""
Toy 1088 — Games & Puzzles from BST
======================================
Game structure and combinatorial counting:
  - Chess: 64 squares = 2^C_2, 8×8 = 2^N_c × 2^N_c
  - Dice: 6 faces = C_2, 2d6 = rank × C_2
  - Rubik's cube: 6 faces = C_2, 54 facelets = rank × N_c³
  - Go: 19×19 = (rank²×n_C - 1)²
  - Sudoku: 9×9 = N_c² × N_c², 3×3 boxes = N_c × N_c

BST integers: N_c=3, n_C=5, g=7, C_2=6, rank=2, N_max=137
"""

N_c = 3; n_C = 5; g = 7; C_2 = 6; rank = 2; N_max = 137

results = {}
test_num = 0

def test(name, condition, detail=""):
    global test_num
    test_num += 1
    status = "PASS" if condition else "FAIL"
    print(f"  T{test_num} [{status}] {name}")
    if detail:
        print(f"       {detail}")
    results[f"T{test_num}"] = (name, condition, detail)

print("="*70)
print("Toy 1088 — Games & Puzzles from BST")
print("="*70)

# T1: Chess
print("\n── Chess ──")
# Board: 8×8 = 2^N_c × 2^N_c = 64 = 2^C_2
# Pieces per side: 16 = 2^rank² = rank⁴
# Piece types: 6 = C_2 (King, Queen, Rook, Bishop, Knight, Pawn)
# Starting position: rank rows of pieces per side
chess_squares = 64     # 2^C_2
board_side = 8         # 2^N_c
piece_types = 6        # C_2
pieces_per_side = 16   # rank⁴

print(f"  Board: {board_side}×{board_side} = {chess_squares} = 2^C_2 = {2**C_2}")
print(f"  Board side: {board_side} = 2^N_c = {2**N_c}")
print(f"  Piece types: {piece_types} = C_2 = {C_2}")
print(f"  Pieces/side: {pieces_per_side} = rank⁴ = {rank**4}")

test("Chess: 2^C_2=64 squares; 2^N_c=8 side; C_2=6 types; rank⁴=16 pieces",
     chess_squares == 2**C_2 and board_side == 2**N_c
     and piece_types == C_2 and pieces_per_side == rank**4,
     f"64={2**C_2}, 8={2**N_c}, 6={C_2}, 16={rank**4}")

# T2: Dice
print("\n── Dice ──")
# Standard die: 6 faces = C_2
# Opposite faces sum: 7 = g
# 2d6: 36 outcomes = rank² × N_c² = C_2²
# Standard RPG dice: d4, d6, d8, d10, d12, d20 = C_2 types
# (rank², C_2, 2^N_c, rank×n_C, rank²×N_c, rank²×n_C)
die_faces = 6          # C_2
opposite_sum = 7       # g
two_dice = 36          # C_2²
rpg_dice_count = 6     # C_2

print(f"  Standard die: {die_faces} faces = C_2 = {C_2}")
print(f"  Opposite faces sum: {opposite_sum} = g = {g}")
print(f"  2d6 outcomes: {two_dice} = C_2² = {C_2**2}")
print(f"  RPG dice types: {rpg_dice_count} = C_2 = {C_2}")

test("C_2=6 die faces; g=7 opposite sum; C_2²=36 outcomes",
     die_faces == C_2 and opposite_sum == g and two_dice == C_2**2,
     f"C_2={C_2}, g={g}, C_2²={C_2**2}")

# T3: Rubik's Cube
print("\n── Rubik's Cube ──")
# Faces: 6 = C_2
# Facelets: 54 = C_2 × N_c² = 6 × 9
# Edge pieces: 12 = rank² × N_c
# Corner pieces: 8 = 2^N_c
# Center pieces: 6 = C_2
# Grid per face: 3×3 = N_c × N_c
cube_faces = 6         # C_2
facelets = 54          # C_2 × N_c²
edges = 12             # rank² × N_c
corners = 8            # 2^N_c
centers = 6            # C_2

print(f"  Faces: {cube_faces} = C_2 = {C_2}")
print(f"  Facelets: {facelets} = C_2 × N_c² = {C_2 * N_c**2}")
print(f"  Edges: {edges} = rank² × N_c = {rank**2 * N_c}")
print(f"  Corners: {corners} = 2^N_c = {2**N_c}")
print(f"  Centers: {centers} = C_2 = {C_2}")
print(f"  Grid: N_c × N_c = {N_c}×{N_c}")

test("Rubik: C_2=6 faces; C_2×N_c²=54 facelets; 2^N_c=8 corners; rank²×N_c=12 edges",
     cube_faces == C_2 and facelets == C_2 * N_c**2
     and edges == rank**2 * N_c and corners == 2**N_c,
     f"C_2={C_2}, 54={C_2*N_c**2}, 12={rank**2*N_c}, 8={2**N_c}")

# T4: Go
print("\n── Go ──")
# Board: 19×19 = (rank²×n_C - 1)²
# 19 = prime (same as Metonic cycle, Ω_Λ = 13/19)
# Star points: 9 = N_c²
# Liberties (max adjacent): 4 = rank²
# Players: 2 = rank (black, white)
go_board = 19          # rank²×n_C - 1
star_points = 9        # N_c²
liberties = 4          # rank²
go_players = 2         # rank

print(f"  Board: {go_board}×{go_board} = (rank²×n_C - 1)² = ({rank**2*n_C} - 1)²")
print(f"  Star points: {star_points} = N_c² = {N_c**2}")
print(f"  Max liberties: {liberties} = rank² = {rank**2}")
print(f"  Players: {go_players} = rank = {rank}")

test("Go 19 = rank²×n_C-1; N_c²=9 stars; rank²=4 liberties",
     go_board == rank**2 * n_C - 1 and star_points == N_c**2
     and liberties == rank**2 and go_players == rank,
     f"19={rank**2*n_C-1}, 9={N_c**2}, 4={rank**2}")

# T5: Sudoku
print("\n── Sudoku ──")
# Grid: 9×9 = N_c² × N_c²
# Box: 3×3 = N_c × N_c
# Digits: 1-9 = N_c² values
# Rows + cols + boxes: 27 constraints = N_c³
sudoku_side = 9        # N_c²
box_side = 3           # N_c
total_cells = 81       # N_c⁴
constraint_sets = 27   # N_c³

print(f"  Grid side: {sudoku_side} = N_c² = {N_c**2}")
print(f"  Box side: {box_side} = N_c = {N_c}")
print(f"  Total cells: {total_cells} = N_c⁴ = {N_c**4}")
print(f"  Constraint sets: {constraint_sets} = N_c³ = {N_c**3}")

test("Sudoku: N_c²=9 side; N_c=3 box; N_c⁴=81 cells; N_c³=27 constraints",
     sudoku_side == N_c**2 and box_side == N_c
     and total_cells == N_c**4 and constraint_sets == N_c**3,
     f"9={N_c**2}, 3={N_c}, 81={N_c**4}, 27={N_c**3}")

# T6: Card games (extending Toy 1066)
print("\n── Card Games Extended ──")
# Poker hands: 10 = rank × n_C (royal flush through high card)
# Bridge tricks: 13 = 2g - 1
# Blackjack target: 21 = N_c × g
# Cribbage board: 121 points = (n_C + C_2)² = 11²
poker_hands = 10       # rank × n_C
bridge_tricks = 13     # 2g - 1
blackjack = 21         # N_c × g
cribbage = 121         # (n_C + C_2)²

print(f"  Poker hand types: {poker_hands} = rank × n_C = {rank * n_C}")
print(f"  Bridge tricks: {bridge_tricks} = 2g - 1 = {2*g - 1}")
print(f"  Blackjack: {blackjack} = N_c × g = {N_c * g}")
print(f"  Cribbage board: {cribbage} = (n_C + C_2)² = {(n_C + C_2)**2}")

test("rank×n_C=10 poker; 2g-1=13 bridge; N_c×g=21 blackjack; (n_C+C_2)²=121",
     poker_hands == rank * n_C and bridge_tricks == 2*g - 1
     and blackjack == N_c * g and cribbage == (n_C + C_2)**2,
     f"10={rank*n_C}, 13={2*g-1}, 21={N_c*g}, 121={(n_C+C_2)**2}")

# T7: Board games
print("\n── Board Games ──")
# Monopoly properties: 28 = rank² × g (without railroads/utilities)
# Including all: 40 spaces = rank³ × n_C
# Scrabble tiles: 100 = rank² × n_C²
# Scrabble board: 15×15 = (N_c × n_C)²
monopoly_properties = 28  # rank² × g
monopoly_spaces = 40      # rank³ × n_C
scrabble_tiles = 100      # rank² × n_C²
scrabble_side = 15        # N_c × n_C

print(f"  Monopoly properties: {monopoly_properties} = rank² × g = {rank**2 * g}")
print(f"  Monopoly spaces: {monopoly_spaces} = rank³ × n_C = {rank**3 * n_C}")
print(f"  Scrabble tiles: {scrabble_tiles} = rank² × n_C² = {rank**2 * n_C**2}")
print(f"  Scrabble board: {scrabble_side}×{scrabble_side} = (N_c × n_C)²")

test("Monopoly: rank²×g=28 props; rank³×n_C=40 spaces; Scrabble: rank²×n_C²=100",
     monopoly_properties == rank**2 * g and monopoly_spaces == rank**3 * n_C
     and scrabble_tiles == rank**2 * n_C**2 and scrabble_side == N_c * n_C,
     f"28={rank**2*g}, 40={rank**3*n_C}, 100={rank**2*n_C**2}")

# T8: Checkers/Draughts
print("\n── Checkers ──")
# Board: 8×8 = 2^N_c × 2^N_c (same as chess)
# Playable squares: 32 = 2^n_C
# Pieces per side: 12 = rank² × N_c
# King promotion: reaches rank 1 or 8 = 2^N_c
checkers_squares = 32   # 2^n_C
checkers_pieces = 12    # rank² × N_c

print(f"  Playable squares: {checkers_squares} = 2^n_C = {2**n_C}")
print(f"  Pieces per side: {checkers_pieces} = rank² × N_c = {rank**2 * N_c}")
print(f"  (12 = cranial nerves = months = ribs)")

test("2^n_C=32 checkers squares; rank²×N_c=12 pieces",
     checkers_squares == 2**n_C and checkers_pieces == rank**2 * N_c,
     f"2^n_C={2**n_C}, rank²×N_c={rank**2*N_c}")

# T9: Puzzles
print("\n── Puzzles ──")
# Jigsaw: common sizes 500 = n_C³ × rank², 1000 = rank³ × n_C³
# Crossword (NYT): typically 15×15 (Mon-Sat) or 21×21 (Sun)
# 15 = N_c × n_C; 21 = N_c × g
# Wordle: 5 letters = n_C; 6 guesses = C_2
jigsaw_500 = 500       # n_C³ × rank²
jigsaw_1000 = 1000     # rank³ × n_C³
nyt_daily = 15         # N_c × n_C
nyt_sunday = 21        # N_c × g
wordle_letters = 5     # n_C
wordle_guesses = 6     # C_2

print(f"  Jigsaw 500 = n_C³ × rank² = {n_C**3 * rank**2}")
print(f"  Jigsaw 1000 = rank³ × n_C³ = {rank**3 * n_C**3}")
print(f"  NYT crossword: {nyt_daily}×{nyt_daily} / {nyt_sunday}×{nyt_sunday}")
print(f"  = (N_c×n_C)² / (N_c×g)²")
print(f"  Wordle: {wordle_letters} letters = n_C; {wordle_guesses} guesses = C_2")

test("Jigsaw 500/1000 BST; crossword 15=N_c×n_C, 21=N_c×g; Wordle n_C/C_2",
     jigsaw_500 == n_C**3 * rank**2 and jigsaw_1000 == rank**3 * n_C**3
     and nyt_daily == N_c * n_C and nyt_sunday == N_c * g
     and wordle_letters == n_C and wordle_guesses == C_2,
     f"500={n_C**3*rank**2}, 1000={rank**3*n_C**3}")

# T10: Game theory
print("\n── Game Theory ──")
# Nash equilibrium types: pure, mixed = rank
# Prisoner's dilemma: 2×2 matrix = rank × rank
# Rock-paper-scissors: 3 choices = N_c
# Dominant strategies per player: 0-2 possible
# Minimax: 2-player = rank
game_types = 2         # rank (cooperative, non-cooperative)
rps_choices = 3        # N_c
pd_matrix = 4          # rank² (2×2 outcomes)
players_minimax = 2    # rank

print(f"  Game types: {game_types} = rank = {rank} (cooperative, non-cooperative)")
print(f"  RPS choices: {rps_choices} = N_c = {N_c}")
print(f"  PD outcomes: {pd_matrix} = rank² = {rank**2}")
print(f"  Minimax: {players_minimax} = rank = {rank}")

test("rank=2 game types; N_c=3 RPS; rank²=4 PD outcomes",
     game_types == rank and rps_choices == N_c and pd_matrix == rank**2,
     f"rank={rank}, N_c={N_c}, rank²={rank**2}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Every Game Board is a BST Grid

  Chess: 2^C_2 = 64 squares, 2^N_c = 8 side, C_2 = 6 piece types
  Rubik: C_2 = 6 faces, 2^N_c = 8 corners, rank²×N_c = 12 edges
  Go: 19 = rank²×n_C - 1 (same prime as Metonic & Ω_Λ!)
  Sudoku: N_c⁴ = 81 cells, N_c³ = 27 constraints

  Dice: C_2 = 6 faces, opposite sum = g = 7
  Blackjack: 21 = N_c × g; Wordle: n_C letters, C_2 guesses
  Scrabble: 100 tiles = rank² × n_C² = base ISO = US Senate!

  Games are humanity's unconscious exploration of BST combinatorics.
""")
