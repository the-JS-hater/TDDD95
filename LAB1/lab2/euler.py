def euler(g, n):
    return ["Impossible"]

if __name__ == "__main__":
    parse = lambda line_str: map(int, line_str.split())
    *input, = map(parse, open(0).readlines())
    i = 0
    n, m = input[i]
    i += 1
    while n+m:
        g = [[] for _ in range(n)]
        for j in range(i, i+m):
            u,v = input[j]
            g[u] += [v]
        print(*euler(g, n))
        i += m
        n, m = input[i]
        i += 1
