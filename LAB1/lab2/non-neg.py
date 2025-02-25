




if __name__ == "__main__":
    f = open(0).read().splitlines()
    
    i = 0
    while True:
        n,m,q,s = f[i].split(" ")


    
    g = [[] for i in range(n)]
    for i in range(1, m):
        u,v,w = f[i].split(" ")
        g[u].append((v,w))

    
