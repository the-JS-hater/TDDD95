from collections import deque

# Morgan Nordberg

# Algorithm: we continually attempt relaxation, improving d[v] with d[u] + w
# from an initial state of d[v] = inf for any v not the start vertex s, until
# we no longer are able to do further relaxation(except for negative cycles).
# We do this by maintaing a queue of all neighbor vertices of any vertex that
# gets relaxed. To deal with negative cycles, since any non negative cycle will
# be maximally relaxed in n-1 times, we maintain a count for each vertex how
# many times they've been relaxed. If it's > n it must be part of, or affected
# by by, a negative cycle. So we mark d[v]=-inf for such cases. This prevents
# the algotihm for infinitley queing this vertices since they can be infinitley
# relaxed. We later on use BFS to propogate this -Inf distance to reachable
# nodes

# Time complexity: In the worst case, each vertex can be relaxed up to n times.
# Every time a vertex is processed, all of its adjacent edges are examined.
# This means in worst case complexity we get O(n*m) where n is the number of
# vertices and m is the number of edges 

def spfa(n, s, g):
    d = [float('inf') for _ in range(n)]
    d[s] = 0
    cnt = [0 for _ in range(n)]
    in_q = [False for _ in range(n)]
    p = [-1 for _ in range(n)]
    q = deque([s])
    in_q[s] = True    

    while len(q):
        u = q.popleft()
        in_q[u] = False
        for v,w in g[u]:
            if d[u] + w < d[v] and d[u] != -float('inf'):
                d[v] = d[u] + w
                p[v] = u
                if not in_q[v]:
                    q.append(v)
                    in_q[v] = True
                    cnt[v] += 1
                    if cnt[v] > n:
                        d[v] = -float('inf')

    for u, val in enumerate(cnt):
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
        to_visit += [v for v,_ in g[u] if v not in visited]
    return list(visited)   


def get_path(p, v):
    # NOTE: not tested by kattis, but included since lab assignment wants the
    # ability to reconstruct the paths
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
        g = [[] for _ in range(n)]
        for j in range(m):
            u,v,w = map(int,input[i].split())
            g[u] += [(v,w)]
            i += 1
        
        p, d = spfa(n,s,g)
        
        for k in range(q):
            v = int(input[i])
            i+=1
            if (d[v] == float('inf')): print("Impossible")
            elif (d[v] == -float('inf')): print("-Infinity")
            else: print(d[v])
        n,m,q,s = map(int,input[i].split())
        i += 1
