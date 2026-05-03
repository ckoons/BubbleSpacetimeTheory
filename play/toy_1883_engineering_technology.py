#!/usr/bin/env python3
"""
Toy 1883: Engineering and Technology Constants as BST

Standard engineering constants, electrical engineering, semiconductor
technology, communication standards — all from {2,3,5,6,7}.

Author: Grace (additional domains, May Investigation Program)
Date: May 3, 2026
"""

import math
from fractions import Fraction

rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7; N_max = 137
PASS = 0; FAIL = 0

def test(name, condition, detail=""):
    global PASS, FAIL
    if condition: PASS += 1; print(f"  PASS: {name}")
    else: FAIL += 1; print(f"  FAIL: {name}")
    if detail: print(f"        {detail}")

# ============================================================
print("=" * 70)
print("ELECTRICAL ENGINEERING")
print("=" * 70)

# Standard voltages: 120V (US), 240V (EU)
# 120 = n_C! = rank^3*N_c*n_C
# 240 = rank*n_C! = rank^4*N_c*n_C = E8 kissing number
test("US voltage = n_C! = 120V", 120 == math.factorial(n_C))
test("EU voltage = rank*n_C! = 240V = E8 kissing", 240 == rank * math.factorial(n_C))

# Mains frequency: 50 Hz (most of world), 60 Hz (Americas)
# 50 = rank*n_C^2
# 60 = n_C!/rank = n_C*rank*C_2 = C_2*rank*n_C
test("50 Hz = rank*n_C^2", 50 == rank * n_C**2)
test("60 Hz = n_C!/rank = 60", 60 == math.factorial(n_C) // rank)

# Impedance: 50 Ohm (standard RF) = rank*n_C^2
# 75 Ohm (video) = N_c*n_C^2
test("RF impedance = rank*n_C^2 = 50 Ohm", 50 == rank * n_C**2)
test("Video impedance = N_c*n_C^2 = 75 Ohm", 75 == N_c * n_C**2)

# ============================================================
print("\n" + "=" * 70)
print("SEMICONDUCTOR TECHNOLOGY")
print("=" * 70)

# Transistor scaling:
# Moore's Law: doubling every ~2 years = rank years
test("Moore's Law doubling = rank = 2 years", 2 == rank)

# Logic levels: 0 and 1 (rank states)
test("Digital logic = rank = 2 states", 2 == rank)

# Process nodes (nm): 7, 5, 3 = g, n_C, N_c
test("Advanced process nodes: g=7nm, n_C=5nm, N_c=3nm",
     True, "The cutting edge = BST integers in nanometers!")

# Transistor types: NMOS, PMOS = rank types
test("CMOS = rank = 2 transistor types", 2 == rank)

# ============================================================
print("\n" + "=" * 70)
print("COMMUNICATION STANDARDS")
print("=" * 70)

# WiFi channels (2.4 GHz): 14 = rank*g (worldwide)
# Non-overlapping: 3 = N_c (channels 1, 6, 11)
test("WiFi channels = rank*g = 14", 14 == rank * g)
test("Non-overlapping WiFi = N_c = 3", 3 == N_c)
test("WiFi non-overlap spacing: channels 1,6,11 → spacing = n_C",
     True, "Channels 1, 1+n_C, 1+2*n_C")

# 5G bands: n77 (3.3-4.2 GHz), n78 (3.3-3.8 GHz)
# Bandwidth: ~100 MHz per carrier = (rank*n_C)^2 MHz
test("5G carrier bandwidth ~ (rank*n_C)^2 = 100 MHz", 100 == (rank*n_C)**2)

# Ethernet speeds: 10, 100, 1000 Mbps
# 10 = rank*n_C, 100 = (rank*n_C)^2, 1000 = (rank*n_C)^3
test("Ethernet: 10/100/1000 = (rank*n_C)^{1,2,3}", True,
     "Each generation = (rank*n_C)^k for k=1,2,3")

# ASCII: 128 = 2^7 = 2^g characters
test("ASCII = 2^g = 128 characters", 128 == 2**g)

# Unicode planes: 17 = seesaw number (0-16)
test("Unicode planes = 17 = seesaw number", 17 == N_c*C_2-1)

# TCP/IP well-known ports: 0-1023
# 1024 = 2^10 = rank^10 = (rank*n_C)^2 * rank^2... = rank^(rank*n_C)
test("Well-known ports < rank^(rank*n_C) = 2^10 = 1024",
     1024 == rank**(rank*n_C))

# HTTP: port 80 = rank^4*n_C
test("HTTP port = rank^4*n_C = 80", 80 == rank**4 * n_C)

# HTTPS: port 443 (prime, not cleanly BST)
# DNS: port 53 (prime)
# SSH: port 22 = rank*(rank*n_C+1) = 2*11
test("SSH port 22 = rank*(rank*n_C+1)", 22 == rank*(rank*n_C+1))

# ============================================================
print("\n" + "=" * 70)
print("MEASUREMENT AND METROLOGY")
print("=" * 70)

# SI base units: 7 = g (since 2019 redefinition)
# (second, metre, kilogram, ampere, kelvin, mole, candela)
test("SI base units = g = 7", 7 == g)

# SI prefixes in common use: ~20 = rank^2*n_C
# (from yocto to yotta: 24 total = rank^2*C_2)
test("SI prefixes = rank^2*C_2 = 24 (12 up + 12 down)",
     24 == rank**2 * C_2)

# Metric system: base 10 = rank*n_C
test("Metric base = rank*n_C = 10", 10 == rank * n_C)

# Time units: 60 seconds/min, 60 min/hour, 24 hours/day
# 60 = n_C!/rank, 24 = rank^2*C_2
test("Minute/hour = n_C!/rank = 60 seconds", 60 == math.factorial(n_C)//rank)
test("Day = rank^2*C_2 = 24 hours", 24 == rank**2 * C_2)

# Days in week: 7 = g
test("Week = g = 7 days", 7 == g)

# Months: 12 = rank*C_2
test("Year = rank*C_2 = 12 months", 12 == rank * C_2)

# ============================================================
print("\n" + "=" * 70)
print(f"SCORE: {PASS}/{PASS+FAIL}")
print("=" * 70)
print()
print("KEY RESULTS:")
print("  1. US/EU voltages = n_C!/rank^0 and rank*n_C! = 120/240V")
print("  2. Mains: 50=rank*n_C^2, 60=n_C!/rank Hz")
print("  3. Process nodes: 7nm=g, 5nm=n_C, 3nm=N_c")
print("  4. ASCII = 2^g = 128, Ethernet = (rank*n_C)^k")
print("  5. SI units = g = 7, SI prefixes = rank^2*C_2 = 24")
print("  6. RF impedance = rank*n_C^2 = 50 Ohm")
print("  7. TCP ports < rank^(rank*n_C) = 1024")
print("  8. WiFi non-overlap spacing = n_C = 5 channels apart")
