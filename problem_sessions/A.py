from functools import cmp_to_key


def cmp(a,b):
    if a[1] < b[1]: return -1
    if a[1] == b[1]:
        if a[0] < b[0]: return -1  
    return 1


def solve(k, v):
    v.sort(key=cmp_to_key(cmp))
    available = k
    available_again = {}
    possible = 0

    for s,f in v:
        for key in available_again:
            if key <= s: 
                val = available_again.get(key, 0)
                available_again[key] -= val
                available += val
        if available <= 0: continue

        available -= 1
        possible += 1
        if f in available_again: available_again[f] += 1 
        else: available_again[f] = 1
    
    print(possible)


if __name__ == "__main__":
    f = open(0).read().splitlines()
    n,k = [int(i) for i in f[0].split(" ")]
    v = [(int(l.split(" ")[0]), int(l.split(" ")[1])) for l in f[1:]]
    solve(k,v)
