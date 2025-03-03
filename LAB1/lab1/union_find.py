# Morno368 - Morgan Nordberg
# TODO 
# Memory & Time complexity
# Description of problem
# How it works


class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.size[x] < self.size[y]: x,y = y,x
        self.parents[y] = x
        self.size[x] = self.size[x] + self.size[y]


if __name__ == "__main__":
    f = open(0).read()
    n = f.split("\n")[0].split(" ")[0]
    dsu = DSU(int(n))
    o = []
    for l in f.split("\n")[1:-1]:
        oper, op1, op2 = l.split(" ")
        op1, op2 = int(op1), int(op2)
        if oper == "?" and dsu.find(op1) == dsu.find(op2): o+=["yes"]
        if oper == "?" and dsu.find(op1) != dsu.find(op2): o+=["no"]
        if oper == "=": dsu.union(op1, op2)
    print("\n".join(o))
