# *f,= map(str.split,open(0).read().splitlines())
# s=" divide"
# for n,m in f:
#     n=int(n);m=int(m)
#     
# 
#     # todo: primtals faktorisera 1->n, och m, kolla att alla 1->n mod
#     # primtalsfaktoriserade m <= 0 (?) för alla prim i m (?)
# 
#     print(f"{m}{s}s {n}!")if True else print(f"{m} does not{s} {n}!")


from math import *

g=lambda n:[i for i in range(2,sqrt(n))if n%i<1]



def foo(n):
    i=2;l=[]
    while n>1:
        for i in range(2,int(sqrt(n))):
            if n%i<0:l+=[i];n//=i;break
    return l

foo(656789)

