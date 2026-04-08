# Morgan Nordberg

# Problem: is finding the minimum spanning tree in a grapgh with wieghted edges.
# i.e find the edge set such that the total cost of all edge-weights is minimal
# while still having a connected grapgh

# Algortihm: Using a DSU from lab1, we start with each vertex in it's own
# tree/set. We then sort the edges according to weight value and iterate over
# them, and given they aren't already joined into the same tree do a union()
# operation on them. Then to check if we managed to achieve a MST we loop
# through all the vertices to see if they are all connected to the root vertex

# Time complexity for DSU.find() and DSU.union() are both O(log N) worst case
# scenario (see previous handin). So we iterate through all edges and for each
# call DSU.find() twice, then DSU.union(). So we get O(M * log N)


def min_span(n, e):
    c = 0
    res = []
    dsu = DSU(n)
    e.sort(key=lambda e: e[2])
    
    for u,v,w in e:
        if dsu.find(u) != dsu.find(v):
            c += w
            res += [(min(u,v),max(u,v))]
            dsu.union(u,v)

    r = dsu.find(0)
    for i in range(n):
        if dsu.find(i) != r:
            return None
    res.sort()
    return c, res 


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.size[x] < self.size[y]: x,y = y,x
        self.parents[y] = x
        self.size[x] = self.size[x] + self.size[y]



if __name__ == "__main__":
    parse = lambda line_str: map(int, line_str.split())
    *input, = map(parse, open(0).readlines())
    i = 0
    n,m = input[i]
    i+=1
    while n+m:
        e = []
        for _ in range(m):
            u,v,w = input[i]
            i+=1
            e += [(u,v,w)]
        
        res = min_span(n,e)
        if res:
            c, e = res; print(c)
            for edge in e: print(edge[0], edge[1])
        else: print("Impossible")

        n,m = input[i]
        i+=1
