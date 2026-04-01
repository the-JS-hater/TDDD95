def solve(c,l):
    c=[list(filter(lambda a:a!="v",e))for e in c]
    for d in c:
        for b in d: 
            if '~' in b:o,n=b[0],b[2:]
            else:o,n=0,b[1:]
            


f = open(0).read().splitlines()
i=1
while 1:
    n,m=*l,=map(int,f[i].split())
    l=[-1]*n
    *c,=map(str.split,f[i+1:i+1+m])
    if solve(c,l):print("satisfiable")
    else:print("unsatisfiable")
    break
