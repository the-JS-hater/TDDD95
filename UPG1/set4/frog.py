get_near = lambda x,y,t:[(x,y,t+1),(x+1,y,t+1),(x-1,y,t+1),(x,y+1,t+1),(x,y-1,t+1)]

def solve(max, m):
    h=len(m)    
    w=len(m[0])
    inside = lambda x,y: 0 <= x < w and 0 <= y < h

    p = [(i%w,i//w)for i in range(h*w)if m[i//w][i%w]=='F'][0]
    g = [(i%w,i//w)for i in range(h*w)if m[i//w][i%w]=='G'][0]

    visited = set()
    t = 0
    x,y = p
    to_visit = [(x,y,t)]

    states = [ 
        [
            r[-i:] + r[:-i] if j % 2 != 0 else r[i:] + r[:i]
            for j, r in enumerate(m)
        ] if h % 2 != 0 else [
            r[-i:] + r[:-i] if j % 2 == 0 else r[i:] + r[:i]
            for j, r in enumerate(m)
        ]
        for i in range(w)
    ]

    for node in to_visit:
        x,y,t = node
        if not inside(x,y): continue
        if states[t%w][y][x]=='X': continue   
        if (x,y,t%w) in visited: continue
        if t > max: break
        if (x,y) == g: print(f"The minimum number of turns is {t}.");return 
        visited.add((x,y,t%w))
        to_visit += get_near(x,y,t)
    
    print("The problem has no solution.")


if __name__ == "__main__":
    f = open(0).read().splitlines()
    n = f[0]
    i = 1

    while i < len(f):
        max = int(f[i])
        i += 1
        h,w = map(int, f[i].split(" "))
        i += 1
        m = f[i:i+h+2]
        i += h+2
        solve(max, m)
