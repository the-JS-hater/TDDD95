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


def turbo(v):
    o = []
    fw = Fenwick(len(v))
    v=sorted(enumerate(v),key=lambda x: x[1])
    for i, _ in v: fw.add(i, 1)
    i,j = 0,len(v)-1
    for k in range(len(v)):
        if k % 2 == 0:
            idx,val = v[i]
            fw.add(idx, -1)
            o += [str(abs(fw.sum_range(0, idx + 1)))]
            i += 1
        else:
            idx,val = v[j]
            fw.add(idx, -1)
            o += [str(abs(fw.sum_range(idx, fw.size())))]
            j -= 1 

    print("\n".join(o))


if __name__ == "__main__":
    v=list(map(int, open(0).read().splitlines()))[1:]
    turbo(v)


