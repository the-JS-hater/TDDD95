import heapq


def dijkstra(graph, s):
    max_ws = [float('inf')] * len(graph)
    max_ws[s] = 0
    pq = [(max_ws[s], s)]  
    
    prev = [-1] * len(graph)
    
    while pq:
        val, node_idx = heapq.heappop(pq)
        # rewrite to calc weight from time table data
        for neighbor, w in graph[node_idx]:
            if val + w < max_ws[neighbor]:
                max_ws[neighbor] = val + w
                prev[neighbor] = node_idx
                heapq.heappush(pq, (val + w, neighbor))
    
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
            g[u] += [(u,v,t_0,p,d)]
            i += 1
        
        max_ws, prev = dijkstra(g, s)
        
        for j in range(q):
            goal = int(input[i])
            # lookup answer in prev/max_ws
            i += 1
