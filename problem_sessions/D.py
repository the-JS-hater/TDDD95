class Fenwick():
    def __init__(self, n):
        self.arr = [0] * (n+1)

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.arr[i]
            i -= -i & i
        return r
    
    def sum_range(self, i, j):
        return self.sum(i) - self.sum(j - 1)
    
    def add(self, i, x):
        i += 1
        while i < len(self.arr):
            self.arr[i] += x
            i += -i & i

    def size(self):
        return len(self.arr)


def movies(m, r):
    o = []
    fw = Fenwick(m)
    m=sorted(enumerate(range(1, m+1)),key=lambda x: x[1])
    for i, _ in m: fw.add(i, 1)
        
    for i in r:
        print(f"\nrequest {i}")
        print(f"above: {fw.sum(i-1)}\n")
        fw.add(i, -1)
        for i in range(len(m)): 
            #print(f"idx: {i+1} -> {fw.sum_range(i+1, fw.size())}")
            print(f"idx: {i+1} -> {fw.sum_range(i+1, fw.size())}")

    #for i in range(len(m)): 
    #    print(f"idx: {i+1} -> {fw.sum(i)}")
    #print("____________")
    #
    #fw.add(2, 1)

    #for i in range(len(m)): 
    #    print(f"idx: {i+1} -> {fw.sum_range(0, i)}")
    #print("____________")
    
    return
    #o = []
    #fw = Fenwick(len(v))
    #v=sorted(enumerate(v),key=lambda x: x[1])
    #for i, _ in v: fw.add(i, 1)
    #i,j = 0,len(v)-1
    #for k in range(len(v)):
    #    if k % 2 == 0:
    #        idx,val = v[i]
    #        fw.add(idx, -1)
    #        o += [str(abs(fw.sum_range(0, idx + 1)))]
    #        i += 1
    #    else:
    #        idx,val = v[j]
    #        fw.add(idx, -1)
    #        o += [str(abs(fw.sum_range(idx, fw.size())))]
    #        j -= 1 

    #print("\n".join(o))


if __name__ == "__main__":
    f=open(0).read().splitlines()
    n=int(f[0])
    for i in range(1, n + 1, 2):
        m,r = list(map(int, f[i].split(" ")))
        r = [int(i) for i in f[i+1].split(" ")]
        print(f"m: {m}, r: {r}")
        movies(m, r)












