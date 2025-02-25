def solve(w):
    best, best_s = float('inf'), None
    
    def complete_search(s, l):
        nonlocal best
        nonlocal best_s
        if not l: return
        diff = abs(1000 - s)
        if diff > best: return
        if diff < best: best, best_s = diff, s
        if diff == best: best_s = max(best, s)
        
        complete_search(s+l[0], l[1:])
        complete_search(s, l[1:])
    
    print(w)
    for i in range(len(w)):
        l = w[0:i] + w[i+1:]
        print(f"excluded: {i}, {l}")
        complete_search(w[i], l)

    print(best_s)



if __name__ == "__main__":
    f = open(0).read().splitlines()
    w = [int(i) for i in f[1:]]
    w.sort()
    solve(w)
