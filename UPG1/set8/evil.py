def f(s):
    if not s:return 0
    if s[0]==s[-1]:return f(s[1:-1])
    else:
        i=s[:-1].find(s[-1]);j=s[1:].rfind(s[0]);j+=j>=0
        if j==i==-1:return e
        a=len(s);b=a-j-1
        if i<0:i=a+1;
        c=min(i,b);s=s[i]+s[:i]+s[i+1:]if i<b else s[:j]+s[j+1:]+s[j];return c+t if (t:=f(s))!=e else e 
e="Impossible"
[print(f(s))for s in open(0).read().splitlines()[1:]]
