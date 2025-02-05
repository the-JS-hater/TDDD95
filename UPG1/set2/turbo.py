f=list(map(int,open(0).read().splitlines()))
s=0
e=f[0]-1
v=f[1:]
d=1
o=""
while s<=e:
    m=s+1 if d else e+1
    i=v.index(m, s, e+1)
    if d:
        v.insert(m-1, m)
    else:
        v.insert(m, m)
    a=abs(i-(m-1))
    o+=str(a)+"\n"
    if d:
        del v[i+1]
        s+=1
    else: 
        del v[i]
        e-=1
    d^=1
print(o)



#f=list(map(int,open(0).read().splitlines()))

