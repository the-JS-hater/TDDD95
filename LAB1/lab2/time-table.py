import heapq

# Morgan Nordberg

# This is essentially the exact same code as the Dijkstra implementation in lab
# 2.1, nothing has changed that would affect the time complexity, just how the
# cost function is calculated and that we store some additional data in the
# edges of the graph, below i'll copy-paste my docs from the previous dijkstra
# lab (NOTE: when dicussing weight that would be replaced with the time cost
# calculation in this case):

# Time Complexity is V + E log E, since we visit every vertex once, and queue
# every edge. Retriving these edged from a priority queue (heapq.heappop()) is
# log N. 
#
# How the algorithm works:
# We initially have an array with the weight of each node set to INF, except
# the source node which has weight 0. We then keep going through a priority
# queue for the cheapest neighbor to go to. Cheap in the sense of current node
# cost + weight of edge to said neighbor. Every time we find a cheaper path to
# a particular node than what was previously in the weight array, we update the
# value, and add that node to the priority queue in order to also reavulate the
# paths to all it's neighbors since we now might have found a cheaper way to
# get there. If a node is unreachable from the starting node, the cost will
# remain at INF

def dijkstra(graph, s):
    max_ws = [float('inf')] * len(graph)
    prev = [-1] * len(graph)
    max_ws[s] = 0
    pq = [(0, s)]  
    
    while pq:
        val, u = heapq.heappop(pq)
        if val > max_ws[u]: continue
        for v, t0, p, d in graph[u]:
            if val <= t0: depart = t0
            elif p == 0: continue
            else:
                wait = (p - (val - t0) % p) % p
                depart = val + wait
            arrival = depart + d
            if arrival < max_ws[v]:
                max_ws[v] = arrival
                prev[v] = u
                heapq.heappush(pq, (arrival, v))
    
    return max_ws, prev


def get_path(prev, start, dest):
    # NOTE: i assume you'll only ever ask for reachable paths. Kattis doesn't
    # test this but seems reasonable to me
    path = []
    node = dest 
    while node != start:
        path.append(node)
        node = prev[node]
    return [start] + path[::-1]


if __name__ == "__main__":
    input = open(0).readlines()
    i = 0
    while i < len(input) - 1:
        n,m,q,s = map(int, input[i].split())
        g = [[] for _ in range(n)]
        i += 1
        for j in range(m):
            u,v,t_0,p,d = map(int, input[i].split())
            g[u] += [(v,t_0,p,d)]
            i += 1
        
        max_ws, prev = dijkstra(g, s)
        
        for k in range(q):
            e = int(input[i])
            i += 1
            if e == s: print(0)
            elif max_ws[e] == float("inf"): print("Impossible")
            else: print(max_ws[e])
