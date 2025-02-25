z=lambda x,y,t:[(x,y,t+1),(x+1,y,t+1),(x-1,y,t+1),(x,y+1,t+1),(x,y-1,t+1)];d=range;e=print;q=len
def o(l,m):
    h=q(m);w=q(m[0]);k=lambda x,y:0<=x<w and 0<=y<h;p=m[-1].index('F'),h-1;g=m[0].index('G'),0;v=set();x,y=p;b=[(x,y,0)];c=[[r[-i:]+r[:-i]if(j+(h%2==0))%2!=0else r[i:]+r[:i]for j,r in enumerate(m)]for i in d(w)]
    for a in b:
        x,y,t=a
        if not k(x,y)or c[t%w][y][x]=='X'or(x,y,t%w)in v:continue
        if t>l:break;
        if(x,y)==g:e(f"The minimum number of turns is {t}.");return
        v.add((x,y,t%w));b+=z(x,y,t);
    e("The problem has no solution.")
f=open(0).read().splitlines()
i=1
while i<q(f):l=int(f[i]);i+=1;h,w=map(int,f[i].split(" "));i+=1;m=f[i:i+h+2];i+=h+2;o(l,m)
