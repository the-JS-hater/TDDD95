from collections import deque
from functools import cmp_to_key as k
g="abcdefgh"
def h(s):
    s=g.index(s[0])+1,int(s[1])
    v=set();q=deque([s]);v|={s};i=-1;f=[]
    while q:
        i+=1;c=[]
        for _ in range(len(q)):
            x,y=q.popleft();c+=[(x,y)]
            for nx,ny in [(x+2,y-1),(x+2,y+1),(x-2,y-1),(x-2,y+1),(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)]:
                if 1<=nx<=8and 1<=ny<=8and not{(nx, ny)}&v:v|={(nx, ny)};q+=[(nx,ny)]
        if c:f=c
    p=lambda a,b:b[1]-a[1]if a[1]!=b[1]else a[0]-b[0] 
    f.sort(key=k(p));r=" ".join([g[x-1]+str(y)for x,y in f]);print(f"{i} {r}")
f=open(0).read().splitlines()[1:]
for s in f:h(s)
