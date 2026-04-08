from collections import deque

# Morgan Nordberg

# In an directed weighted graph, find the maxmimum flow between the source node
# and the sink node

# Algorthm: Using BFS, find an augmenting path and then using the minimum
# residual capacity along some edge of that path, add that amount of flow to
# the path. repeat until no augmenting path can be found (BFS returns 0 as the
# new flow value)

# Complexity: every time we update the flow, atleast one edge becomes saturated
# and if it reappears in a different augmenting path the distance to s will
# increase, it can increase at most V nr. of times, where V is the number of
# vertices (obvious, since it will be acyclic paths). Each time we find a
# augmenting path, we do so by calling BFS which is O(N), where N would be the
# nr. of edges in this case. So time complexity is O(V*E^2)


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
