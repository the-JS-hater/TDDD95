from collections import deque

# Morgan Nordberg

# Problem is to find a minimum cut in a directed weighted grapgh. i.e a set of
# edges such that removing them would disconnect the grapgh and the sum of
# their weights is minimal.

# Algorithm: we use maxflow to get the matrix containg all the residual
# capacities after maxflow is achieved. If we then take the set of all vertices
# reachable from the source node, using only edges with residual capacity > 0,
# we get the set "to the left" of the minimal cut. This is done by DFS

# Time complexity: maxflow is O(V*E^2), we then need to run DFS so that's an
# additional O(E + V)


def min_cut(s, adj, capacities):
    set_u = set()
    q = [s]
    while q:
        u = q.pop()
        set_u.add(u)
        for v in adj[u]:
            if not v in set_u and capacities[u][v] > 0:
                set_u.add(v)
                q.append(v)
    return set_u

# CODE BELOW IS COPIED FROM PREVIOUS LAB
# tldr; maxflow - O(V*E^2)

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
    set_u = min_cut(s, adj, capacities)
    print(len(set_u)) 
    for v in set_u:
        print(v)
