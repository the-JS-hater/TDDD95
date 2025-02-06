l=lambda s:s.pop()
def x(s):s+=[frozenset()]
def y(s):s+=[s[-1]];
def u(s):t,n=l(s),l(s);s+=[t|n]
def u(s):t,n=l(s),l(s);s+=[t|n]
def j(s):t,n=l(s),l(s);s+=[t&n]
def a(s):t,n=l(s),l(s);s+=[n|({hash(t)})]
def s(v):s=[];return "\n".join([f"{len(s[-1])}" for e in v if not({"P":x,"D":y,"U":u,"I":j,"A":a}[e[0]](s))])+"\n***\n"
f=open(0).read().splitlines();t=f[0];i=1;o=""
for _ in range(int(t)):n=int(f[i])+1;o+=s(f[i+1:i+n]);i+=n
print(o)
