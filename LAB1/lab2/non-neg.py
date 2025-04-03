import heapq


# Memory complexity is ...
#  
# Time Complexity is N*M, where N is the nr of edges in the grapgh, and M is the number of vertices in the graph. We will always have to traverse all nodes, and for every vertex we mmight need to reevaluate
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
    max_ws[s] = 0
    pq = [(max_ws[s], s)]  
    
    while pq:
        val, node_idx = heapq.heappop(pq)

        for neighbor, w in graph[node_idx]:
            if val + w < max_ws[neighbor]:
                max_ws[neighbor] = val + w
                heapq.heappush(pq, (val + w, neighbor))
    
    return max_ws

if __name__ == "__main__":
    *f, = map(str.split, open(0).read().splitlines())
    
    i = 0
    while True:
        n,m,q,s = [int(c) for c in f[i]] 
        if [n,m,q,s] == [0,0,0,0]: break
        g = [[] for _ in range(n)]
        
        for j in range(i + 1, i + 1 + m):
            u,v,w = [int(c) for c in f[j]] 
            g[u].append((v,w))
        
        max_ws = dijkstra(g,s)

        for k in range(q):
            e = int(f[i + 1 + m + k][0])
            if e == s: print(0)
            elif max_ws[e] == float("inf"): print("Impossible")
            else: print(max_ws[e])

        i += m + q + 1
