def floyd(g):
    d = [[float('inf')] * len(g) for _ in range(len(g))]
    p = []
    for i, e_set in enumerate(g):
        d[i][i] = 0
        for e in e_set:
            j,w = e
            d[i][j] = min(d[i][j], w)
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                if d[i][k] < float('inf') and d[k][j] < float('inf'):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # for k in range(n):
    #     if d[k][k] < 0:
    #         for i in range(n):
    #             if d[i][k] != -float('inf'):
    #                 for j in range(n):
    #                     if d[k][j] != -float('inf'):
    #                         d[i][j] = -float('inf')
    return p, d


if __name__ == "__main__":
    parse = lambda line_str: map(int, line_str.split())
    *input, = map(parse, open(0).readlines())
    i = 0
    n,m,q = input[i]
    i+=1
    while n+m+q:
        g = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = input[i]
            g[u] += [(v,w)]
            i += 1
        p,d = floyd(g)
        for _ in range(q):
            u,v = map(int, input[i])
            i += 1
            if d[u][v] == float('inf'): print("Impossible")
            elif d[u][v] == -float('inf'): print("-Infinity")
            else: print(d[u][v])
        print()
        n,m,q = input[i]
        i+=1
