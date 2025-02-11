from math import gcd
j=open(0).read().replace("...","").replace("0.","").splitlines()[:-1]
def f(x):
    simp_d=float('inf')
    simp_n=float('inf')
    for i in range(1,len(x)+1):
        n=int(x)-int(f"0{x}"[:-i])
        d=10**len(x)-10**(len(x)-i)
        cd=gcd(n,d)
        if d//cd<simp_d:
            simp_d=d//cd
            simp_n=n//cd
    return f"{simp_n}/{simp_d}"
[print(f(x))for x in j]
