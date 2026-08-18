from fractions import Fraction as F
d=5; RAC=F(3,2); DI=F(2)
print("="*102)
print("TOY 5329 -- the composite<->SM assignment: running the #Rac IDENTITY as a FILTER")
print("  on the two conflicting corpus claims (Rac = Higgs, F338)  vs  (Rac = muon, Lepton_Sector).")
print("  Tables first, verdict after.")
print("="*102)

print("\n  The filter has two prongs, both already established, neither new:")
print("     (i)  #Rac PARITY   : boson needs (-1)^{#Rac} = +1 (even);  fermion needs -1 (odd)")
print("     (ii) SPIN          : the state's spin must match the particle's spin")
print("  A bare Rac is:  spin 0,  #Rac = 1  ->  (-1)^1 = -1  (FERMIONIC parity on a SCALAR)")

print("\nTABLE 1 -- *** run BOTH corpus claims through the filter ***")
print("   claim                 particle  spin needed  parity needed   bare Rac gives      verdict")
rows=[("Rac = Higgs  (F338)","Higgs",F(0),"+1 (boson)","spin 0 OK, parity -1","PARITY FAILS"),
      ("Rac = muon   (Lepton)","muon",F(1,2),"-1 (fermion)","parity OK, spin 0","SPIN FAILS")]
for c,p,s,par,gives,v in rows:
    print("   %-21s %-9s %-12s %-15s %-19s *** %s ***"%(c,p,str(s),par,gives,v))
print("\n   ==> BOTH FAIL -- and for DIFFERENT reasons. They are not two readings of one question;")
print("       they are two separate errors that happen to share the same shape.")

print("\nTABLE 2 -- what the composite reading assigns instead (Flato-Fronsdal towers)")
print("   tower          primary Delta      spins       #Rac   parity   statistics")
tow=[("Rac (x) Rac",F(d-2),"0,1,2,...",2),("Di  (x) Di ",F(d-1),"0,1,2,...",0),
     ("Rac (x) Di ",RAC+DI,"1/2,3/2,...",1)]
for nm,D,sp,nR in tow:
    print("   %-14s %-18s %-11s %-6d %-8s %s"%(nm,str(D)+" + l",sp,nR,"%+d"%((-1)**nR),
          "BOSON" if (-1)**nR>0 else "FERMION"))

print("\nTABLE 3 -- the three particles we have touched, placed consistently")
print("   particle   spin   needs parity   composite slot          Delta      passes both prongs")
place=[("Higgs",F(0),"+1","Rac (x) Rac, l=0",F(3),2),
       ("photon",F(1),"+1","Rac (x) Rac, l=1",F(4),2),
       ("muon",F(1,2),"-1","Rac (x) Di,  l=0",F(7,2),1)]
for p,s,par,slot,D,nR in place:
    ok = ((-1)**nR==(1 if par=="+1" else -1))
    print("   %-10s %-6s %-14s %-23s %-10s %s"%(p,str(s),par,slot,str(D),"YES" if ok else "no"))
print("\n   every SM state lands as a TWO-CONSTITUENT COMPOSITE. None is a bare singleton.")

print("\nTABLE 4 -- is the filter itself trustworthy? (#Rac parity as a conserved grading)")
print("   (-1)^{#Rac} = (-1)^F on composites [toy 5327, 384/384]. Fermion parity is conserved in")
print("   the SM. So #Rac mod 2 is a conserved Z_2 grading -- the filter is a SELECTION RULE,")
print("   not a heuristic. That is why it can rule things OUT cleanly.")

print("\n"+"="*102)
print("VERDICT -- from Tables 1-4 only")
print("="*102)
print(" (1) ***** BOTH CORPUS CLAIMS FAIL, FOR DIFFERENT REASONS. *****")
print("     'Rac = Higgs' (F338)  fails on PARITY: the Higgs is a boson and needs (-1)^{#Rac}=+1,")
print("        but a bare Rac has #Rac = 1 -> -1. A bare Rac cannot be any boson.")
print("     'Rac = muon' (Lepton_Sector) fails on SPIN: parity is right (-1), but a bare Rac is a")
print("        SCALAR and the muon is spin 1/2.")
print("     ==> @Keeper: the conflict does not need adjudicating between the two. NEITHER survives.")
print("         That is a cleaner outcome than a tie-break, and it removes the corpus inconsistency")
print("         by deleting both horns rather than choosing one.")
print()
print(" (2) THE COMMON ROOT: both claims identify an SM particle with a BARE SINGLETON. Under the")
print("     composite reading (decided for the vector row in 5328), SM particles are TWO-CONSTITUENT")
print("     composites; the singletons are CONSTITUENTS, not particles. One structural error, filed")
print("     twice in two sectors. Fixing the reading fixes both at once.")
print()
print(" (3) CONSISTENT PLACEMENTS (Table 3), all passing both prongs: Higgs -> Rac(x)Rac l=0 (Delta 3);")
print("     photon -> Rac(x)Rac l=1 (Delta 4, already decided); muon -> Rac(x)Di l=0 (Delta 7/2).")
print("     ** THESE ARE CANDIDATES, NOT DERIVATIONS. ** The filter RULES OUT; it does not construct.")
print("     Passing a Z_2 parity test and a spin test is necessary, nowhere near sufficient, and")
print("     @Keeper has correctly said the Higgs substrate identity still needs the FORCED MAP.")
print("     I am supplying an elimination, not the map. Do not let Table 3 be cited as an assignment.")
print()
print(" (4) WHY THE FILTER IS ALLOWED TO RULE OUT (Table 4): (-1)^{#Rac} = (-1)^F and fermion parity")
print("     is conserved, so #Rac mod 2 is a conserved Z_2 grading -- a selection rule. Selection")
print("     rules kill cleanly and build nothing. That is exactly the weight I am putting on it.")
