def bellman(e, s, n, g):
    d = [float('inf')] * n 
    d[s] = 0
    p = [-1] * n
    count = [0] * n
    for _ in range(n - 1):
        for u,v,w in e:
            if d[u] < float('inf'):
                if d[v] > d[u] + w:
                    d[v] = max(-float('inf'), d[u]+w)
                    p[v] = u
                    count[v] += 1
    for u, val in enumerate(count):
        if val >= n and d[u] != -float('inf'):
            cycle = bfs(u, g)
            for v in cycle: d[v] = -float('inf')
    return p, d

def bfs(u, g):
    visited = set()
    to_visit = [u]
    while to_visit:
        u = to_visit.pop()
        visited.add(u)
        to_visit += [v for v in g[u] if v not in visited]
    return list(visited)   

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
        g = [[] for _ in range(n)]
        for j in range(m):
            u,v,w = map(int,input[i].split())
            e += [(u,v,w)]
            g[u] += [v]
            i += 1
        
        p, d = bellman(e, s, n, g)          
        
        for k in range(q):
            v = int(input[i])
            i+=1
            if (d[v] == float('inf')): print("Impossible")
            elif (d[v] == -float('inf')): print("-Infinity")
            else: print(d[v])
        n,m,q,s = map(int,input[i].split())
        i += 1
