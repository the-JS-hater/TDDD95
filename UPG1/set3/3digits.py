n=m=int(open(0).read())
for i in range(1,n-1):
    n*=m-i
    while n%10==0:
        n//=10
    n%=100000
print(str(n)[-3:])

