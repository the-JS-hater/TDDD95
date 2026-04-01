def g(n):
    l=[]
    for i in range(1,n+1): 
        if n%i<1:l+=[i]
    return l
*f,= map(str.split,open(0).read().splitlines())
s=" divide"
for n,m in f:
    n=int(n);m=int(m)
    if set(g(n)).issubset(set(g(m))):print(f"{m}{s}s {n}!")
    else:print(f"{m} does not{s} {n}!")
