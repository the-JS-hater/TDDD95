from functools import cmp_to_key


def cmp(a, b):
    if a[0] > b[0]: return 1
    if a[0] == b[0]: return 0
    if a[2] > b[2]: return 1
    if a[2] == b[2]: return 0
    return -1



if __name__ == "__main__":
    *f, = map(str.split, open(0).read().splitlines())

    n,m,p = f[0]
    p_set = set(f[1])
    

    foo = lambda x : x[1] not in p_set
    connections = sorted(filter(foo ,f[2:]), key=cmp_to_key(cmp))
        
    print(connections)

    connected = {'1'}
    cost = 0

    for s,e,c in connections:
        print(f"s {s}, e {e}, c {c}")
        if e in connected: continue
        print("bought it")
        connected.add(e)
        cost += int(c)

    print(cost)
        
