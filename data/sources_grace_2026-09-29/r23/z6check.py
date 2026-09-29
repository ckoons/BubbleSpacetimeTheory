from fractions import Fraction as F
# (name, SU2 dim, SU3 triality z3 (0 singlet,1 fundamental), q = Ytilde) from Tong p9 table
fields=[("lL",2,0,-3),("eR",1,0,-6),("qL",2,1,1),("uR",1,1,4),("dR",1,1,-2),("H",2,0,3),("nuR",1,0,0)]
def phase(k,f):  # xi^k acts as exp(2pi i * total) ; return total mod 1
    n,d,z3,q=f
    s = F(k*q,6) + (F(k,2) if d==2 else 0) + (F(k*z3,3))   # eta=-1 -> 1/2 turn; omega=e^{2pi i/3}
    return s%1
for k in range(6):
    print("xi^%d:"%k, {f[0]:str(phase(k,f)) for f in fields})
print("SU(2) centre -1 alone:", {f[0]:("-1" if f[1]==2 else "+1") for f in fields})
print("e^{i pi q} (= e^{2 pi i 3Y}) alone:", {f[0]:("-1" if f[3]%2 else "+1") for f in fields})
print("e^{2 pi i Y} alone (Y=q/6) turn fraction:", {f[0]:str(F(f[3],6)%1) for f in fields})
