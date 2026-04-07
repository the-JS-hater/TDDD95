def bellman(e, v, n):
    d = [float('inf')] * n 
    d[v] = 0
    p = [-1] * n
    for _ in range(n - 1):
        for u,v,w in e:
            if d[u] < float('inf'):
                if d[v] > d[u] + w:
                    d[v] = max(-float('inf'), d[u]+w)
                    p[v] = u
    
    x = -1
    for u,v,w in e:
        if d[u] < float('inf'):
            if d[v] > d[u] + w:
                d[v] = max(-float('inf'), d[u]+w)
                p[v] = u
                x = v
    if x != -1: 
        # make sure the appropriate indices of d are -float('inf')
        pass
    return p, d



def get_path(p, v):
    path = []
    cur = p[v]
    print(p,v)
    while cur != -1:
        path += [cur]
        cur  =  p[cur]
    return path[::-1]


if __name__ == "__main__":
    i = 0
    input = open(0).readlines()
    n,m,q,s = map(int,input[i].split())
    i += 1
    while n + m + q + s:
        e = [] * n
        for j in range(m):
            u,v,w = map(int,input[i].split())
            e += [(u,v,w)]
            i += 1
        
        # run bellman ford here
        p, d = bellman(e, s, n)          
        
        for k in range(q):
            v = int(input[i])
            i+=1
            # query the results of bellman
            if (d[v] == float('inf')): print("Impossible")
            elif (d[v] == -float('inf')): print("-Infinity")
            else: print(d[v])
        n,m,q,s = map(int,input[i].split())
        i += 1
