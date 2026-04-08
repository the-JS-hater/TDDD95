from collections import deque


def maxflow(adj, capacities, s, t):
    flow = 0
    new_flow, parent = bfs(s, t, adj, capacities)
    while new_flow:
        flow += new_flow
        cur = t
        while cur != s:
            prev = parent[cur]
            capacities[prev][cur] -= new_flow
            capacities[cur][prev] += new_flow
            cur = prev
        new_flow, parent = bfs(s, t, adj, capacities)

    return flow


def bfs(s, t, adj, capacities):
    n = len(adj)
    parent = [-1] * n
    parent[s] = -2
    q = deque([(s, float('inf'))])
    
    while len(q):
        cur, flow = q.popleft()
        for next in adj[cur]:
            if parent[next] == -1 and capacities[cur][next]:
                parent[next] = cur
                new_flow = min(flow, capacities[cur][next])
                if next == t:
                    return new_flow, parent
                q.append((next, new_flow))
    return 0, parent


if __name__ == "__main__":
    parse = lambda line_str: map(int, line_str.split())
    *input, = map(parse, open(0).readlines())
    n,m,s,t = input[0]
    adj = [[] for _ in range(n)]
    capacities = [[0]*n for _ in range(n)]
    
    for i in range(1, m+1):
        u,v,c = input[i]
        adj[u] += [v]
        adj[v] += [u]
        capacities[u][v] += c
    capacities_copy = [row[:] for row in capacities]
    f = maxflow(adj, capacities, s, t)
    e = []
    for u in range(n):
        for v in range(n):
            uv_flow = capacities_copy[u][v] - capacities[u][v]
            if uv_flow > 0: e += [(u,v,uv_flow)]
    print(n,f,len(e))
    for edge in e: print(*edge)
