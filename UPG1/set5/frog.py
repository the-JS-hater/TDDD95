def o(l,m):
    h=q(m);w=q(m[0]);p=m[-1].index('F'),h-1;g=m[0].index('G'),0;v=set();x,y=p;b=[(x,y,0)];c=[[r[-i:]+r[:-i]if(j+(h%2==0))%2!=0else r[i:]+r[:i]for j,r in enumerate(m)]for i in d(w)]
    for a in b:
        x,y,t=a 
        if t>l:break
        if not(0<=x<w)*(0<=y<h)or c[t%w][y][x]=='X'or(x,y,t%w)in v:continue 
        if(x,y)==g:e(f"The minimum number of turns is {t}.");return
        v.add((x,y,t%w));
        t+=1;b+=[(x,y,t),(x+1,y,t),(x-1,y,t),(x,y+1,t),(x,y-1,t)]
    e("The problem has no solution.")
d=range;e=print;q=len
f=open(0).read().splitlines()
i=1
while i<q(f):l=int(f[i]);h,w=map(int,f[i+1].split());m=f[i+2:i+h+4];i+=h+4;o(l,m)
