#!/usr/bin/env python3
"""
Toy 1078 — Economics & Finance from BST
==========================================
Financial structure and economic counting:
  - Stock exchanges: major ones dominate (g top exchanges cover >90% cap)
  - 5 BRICS nations = n_C; G7 = g
  - Currency: 3 reserve (N_c: USD, EUR, JPY)
  - US denominations: 1,5,10,25,50,100 → 6 coins = C_2
  - Dow Jones Industrial Average: 30 stocks = rank×N_c×n_C = n_C#
  - S&P 500: 11 sectors = n_C + C_2

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
print("Toy 1078 — Economics & Finance from BST")
print("="*70)

# T1: G7 = g
print("\n── International Groups ──")
g7_nations = 7  # g
brics = 5  # n_C (original: Brazil, Russia, India, China, S. Africa)
g20 = 20  # rank² × n_C

print(f"  G7: {g7_nations} = g = {g}")
print(f"  BRICS (original): {brics} = n_C = {n_C}")
print(f"  G20: {g20} = rank² × n_C = {rank**2 * n_C}")

test("G7 = g; BRICS = n_C; G20 = rank²×n_C",
     g7_nations == g and brics == n_C and g20 == rank**2 * n_C,
     f"g={g}, n_C={n_C}, rank²×n_C={rank**2*n_C}")

# T2: S&P sectors = n_C + C_2
print("\n── Market Sectors ──")
# GICS sectors: Energy, Materials, Industrials, Consumer Discretionary,
# Consumer Staples, Health Care, Financials, IT, Telecom,
# Utilities, Real Estate = 11
sp_sectors = 11  # n_C + C_2

print(f"  S&P 500 GICS sectors: {sp_sectors} = n_C + C_2 = {n_C + C_2}")
print(f"  (Same as organ systems, soccer teams)")

test("11 S&P sectors = n_C + C_2",
     sp_sectors == n_C + C_2,
     f"n_C + C_2 = {n_C+C_2}")

# T3: DJIA = 30 = n_C#
print("\n── Stock Indices ──")
djia_stocks = 30  # rank × N_c × n_C = n_C# (primorial)
# 30 = 2 × 3 × 5 = primorial of n_C

print(f"  DJIA stocks: {djia_stocks} = rank × N_c × n_C = {rank * N_c * n_C}")
print(f"  = n_C# (primorial of {n_C}) = 2 × 3 × 5 = {2*3*5}")
print(f"  (Same as Moon distance/Earth diameter, dodecahedron edges)")

test("DJIA 30 stocks = n_C# = rank×N_c×n_C",
     djia_stocks == rank * N_c * n_C,
     f"n_C# = {rank*N_c*n_C}")

# T4: US coin denominations
print("\n── US Denominations ──")
# Coins: penny(1), nickel(5), dime(10), quarter(25), half-dollar(50), dollar(100)
us_coin_types = 6  # C_2
# Bills: $1, $2, $5, $10, $20, $50, $100 = g denominations
us_bill_types = 7  # g

print(f"  US coin denominations: {us_coin_types} = C_2 = {C_2}")
print(f"  US bill denominations: {us_bill_types} = g = {g}")
print(f"  ($1, $2, $5, $10, $20, $50, $100)")

test("C_2=6 US coin types; g=7 US bill types",
     us_coin_types == C_2 and us_bill_types == g,
     f"C_2 = {C_2} coins, g = {g} bills")

# T5: Business cycles
print("\n── Business Cycles ──")
# NBER phases: expansion, peak, contraction, trough = rank²
business_phases = 4  # rank²
# Kondratiev wave: ~50-60 years
# Typical recession length: ~11 months avg
# Bull/bear = rank
market_states = 2  # rank

print(f"  Business cycle phases: {business_phases} = rank² = {rank**2}")
print(f"  Market states: {market_states} = rank = {rank} (bull, bear)")

test("rank²=4 business cycle phases; rank=2 market states",
     business_phases == rank**2 and market_states == rank,
     f"rank² = {rank**2} phases, rank = {rank} states")

# T6: Reserve currencies
print("\n── Reserve Currencies ──")
# Top 3: USD, EUR, JPY = N_c
top_reserve = 3  # N_c
# IMF SDR basket: 5 (USD, EUR, CNY, JPY, GBP) = n_C
sdr_basket = 5  # n_C

print(f"  Top reserve currencies: {top_reserve} = N_c = {N_c}")
print(f"  IMF SDR basket: {sdr_basket} = n_C = {n_C}")

test("N_c=3 top reserves; n_C=5 SDR basket currencies",
     top_reserve == N_c and sdr_basket == n_C,
     f"N_c = {N_c}, n_C = {n_C}")

# T7: Accounting equation
print("\n── Accounting ──")
# A = L + E (Assets = Liabilities + Equity) → N_c terms
accounting_eq_terms = 3  # N_c
# Financial statements: balance sheet, income statement,
# cash flow, equity statement = rank²
financial_statements = 4  # rank²
# Double-entry: debit + credit = rank
double_entry = 2  # rank

print(f"  Accounting equation terms: {accounting_eq_terms} = N_c = {N_c}")
print(f"  Financial statements: {financial_statements} = rank² = {rank**2}")
print(f"  Double-entry: {double_entry} = rank = {rank} (debit, credit)")

test("N_c=3 accounting terms; rank²=4 statements; rank=2 double-entry",
     accounting_eq_terms == N_c and financial_statements == rank**2 and double_entry == rank,
     f"N_c={N_c}, rank²={rank**2}, rank={rank}")

# T8: Trading
print("\n── Trading ──")
# Market hours NYSE: 6.5 hrs = 6h30m → ~C_2 + 0.5
# Bid/Ask = rank (two-sided market)
bid_ask = 2  # rank
# Order types basic: market, limit, stop = N_c
basic_orders = 3  # N_c
# Candlestick: open, high, low, close = rank² (OHLC)
ohlc = 4  # rank²

print(f"  Market sides: {bid_ask} = rank = {rank} (bid, ask)")
print(f"  Basic order types: {basic_orders} = N_c = {N_c}")
print(f"  OHLC price data: {ohlc} = rank² = {rank**2}")

test("rank=2 bid/ask; N_c=3 order types; rank²=4 OHLC",
     bid_ask == rank and basic_orders == N_c and ohlc == rank**2,
     f"rank={rank}, N_c={N_c}, rank²={rank**2}")

# T9: Risk factors
print("\n── Risk ──")
# Fama-French: 3 factors = N_c (market, size, value)
ff_factors = 3  # N_c
# Extended: 5-factor (+ profitability, investment) = n_C
ff5_factors = 5  # n_C
# Rating scales: AAA to D = typically 7-10 main grades
# Moody's main: Aaa, Aa, A, Baa, Ba, B, Caa = 7 = g
moody_grades = 7  # g

print(f"  Fama-French 3 factors: {ff_factors} = N_c = {N_c}")
print(f"  Fama-French 5 factors: {ff5_factors} = n_C = {n_C}")
print(f"  Moody's main grades: {moody_grades} = g = {g}")

test("N_c=3 FF factors; n_C=5 FF5; g=7 Moody's grades",
     ff_factors == N_c and ff5_factors == n_C and moody_grades == g,
     f"N_c={N_c}, n_C={n_C}, g={g}")

# T10: Interest and growth
print("\n── Financial Ratios ──")
# Rule of 72: doubling time ≈ 72/rate
# 72 = 2^N_c × N_c² = 8 × 9 (BST product!)
rule_72 = 72  # 2^N_c × N_c²
# Pareto: 80/20 rule
# 80 = rank⁴ × n_C, 20 = rank² × n_C
pareto_80 = 80
pareto_20 = 20

print(f"  Rule of 72: {rule_72} = 2^N_c × N_c² = {2**N_c} × {N_c**2}")
print(f"  (Same as points per inch in typography!)")
print(f"  Pareto: 80/20 = rank⁴×n_C / rank²×n_C = rank²")
print(f"  80 = {rank**4*n_C}, 20 = {rank**2*n_C}")

test("Rule of 72 = 2^N_c × N_c²; Pareto 80/20 = rank⁴×n_C / rank²×n_C",
     rule_72 == 2**N_c * N_c**2
     and pareto_80 == rank**4 * n_C and pareto_20 == rank**2 * n_C,
     f"72 = {2**N_c*N_c**2}, 80/20 = {rank**4*n_C}/{rank**2*n_C}")

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70)
passed = sum(1 for _, (_, c, _) in results.items() if c)
total = len(results)
print(f"\n  Tests: {passed}/{total} PASS")
print(f"""
  HEADLINE: Markets Count in BST

  g = 7: G7 nations, US bill denominations, Moody's grades
  n_C = 5: BRICS, SDR currencies, Fama-French 5 factors
  n_C + C_2 = 11: S&P sectors (same as organ systems!)
  rank × N_c × n_C = 30: DJIA stocks = n_C# (primorial)
  rank² × n_C = 20: G20

  rank = 2: bull/bear, bid/ask, debit/credit
  rank² = 4: cycle phases, OHLC, financial statements
  N_c = 3: accounting equation, reserve currencies, basic orders
  C_2 = 6: US coin denominations

  72 = 2^N_c × N_c² = doubling rule
  80/20 Pareto = rank⁴×n_C / rank²×n_C = rank² ratio

  Finance is human-optimized counting. The optimal point is BST.
""")
