import heapq

def dijkstra(graph):
    n = len(graph)
    
    max_ws = [-float('inf')] * n
    max_ws[0] = 1.0  
    
    pq = [(-max_ws[0], 0)]  
    
    while pq:
        val, node_idx = heapq.heappop(pq)
        val = -val  
        
        for neighbor, w in graph[node_idx]:
            new_val = val * w
            
            if new_val > max_ws[neighbor]:
                max_ws[neighbor] = new_val
                heapq.heappush(pq, (-new_val, neighbor))
    
    return max_ws[-1]


if __name__ == "__main__":
    *f,=map(str.split, open(0).read().splitlines())
    idx = 0
    while (idx < len(f) - 1):
        n,m = f[idx]
        idx+=1
        *graph, = [[] for _ in range(int(n))]
        for _ in range(int(m)):
            x,y,w = f[idx]
            idx+=1
            graph[int(x)].append((int(y),float(w)))
            graph[int(y)].append((int(x),float(w)))
        
        print(f'{dijkstra(graph):.4f}')
