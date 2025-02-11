f=list(map(int, open(0).readlines()));o="";c=lambda n:str(n) if n<7 else str(n%7)+c(n//7);m=lambda x:"".join([['0','1','2','5','9','8','6'][int(c)] for c in c(x)]);[print(m(n)) for n in f]
