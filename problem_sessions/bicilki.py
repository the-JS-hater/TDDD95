GOAL = 1
START = 0

def solve(graph, node, visited):

    #print(f"node: {node}")
    print(f"node: {node}, visited: {visited}")

    if node == GOAL:
        return 1

    if node in visited:
        return float("inf")
    
    neighbors = graph[node]
    visited.add(node)
    
    count = 0
    for neighbor in neighbors:
        res = solve(graph, neighbor, visited.copy())
        #if res == float("inf"): return float("inf")
        count += res

    return count


def solve_v2(graph):
    count = 0
    visited = {START}
    to_visit = graph[START]
    
    for current in to_visit:
        if current == GOAL:
            count += 1
        to_visit += graph[current]
        if current in visited: continue
        visited.add(current)
    
    return count

def solve_v3(graph, node, path):
    
    print(f"node: {node}, visited: {path}")
    
    if node == GOAL: return 1

    if node in path: return float("inf")
    
    neighbors = graph[node]
    new_path = path.copy()
    new_path.add(node)
    count = 0
    for neighbor in neighbors:
        res = solve_v3(graph, neighbor, new_path) 
        if res == float("inf"): return res
        count += res
    
    return count


if __name__ == "__main__":
    f = open(0).read().splitlines()
    n,m = f[0].split()
    t = [[] for i in range((int(n)))]  

    for i,j in map(str.split, f[1:]): 
        t[int(i) - 1].append(int(j) - 1)
   
    #print(solve(t, START, set()))
    #print(solve_v2(t))
    print(solve_v3(t, START, set()))
    
