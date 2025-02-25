a=lambda x,y:[(x+1,y),(x-1,y),(x,y+1),(x,y-1)];m=open(0).read().splitlines()[1:];w=len(m[0]);h=len(m);p=[(i%w,i//w)for i in range(h*w)if m[i//w][i%w]=='P'][0];v=set();n=[];c=0;n+=[p];
for p in n:
    if p in v:continue
    v.add(p)
    x,y=p
    if m[y][x]=='#':continue
    if m[y][x]=='G':c+=1
    b=a(x,y)
    if any([m[y][x]=='T'for x,y in b]):continue
    n+=b
print(c)
