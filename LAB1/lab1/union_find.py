# Morno368 - Morgan Nordberg
# TODO documentation

# maintains a colleciton of disjoint sets and supports the operations find(x),
# which returns the root of the set containing x and union(x, y) which merges
# the sets contating x and y. 

# each set is stored as a rooted tree, where parents[i] points to the parent of
# node i. roots point to themselves. size[i] stores the size of the tree that
# is rooted at i

# during union we make compare sizes to so that we merge the trees such that
# the smaller set becomes a subtree of the larger, ensuring we maintain a tree
# that's as shallow as possible. since the height of the tree affects the
# complexity of the operations. during find, aat each step of the path we make
# the node point ot the root, effectivley flattening the tree which again
# maintains shallowness

# find backtracks through the tree, and the tree will never have a height
# larger than log n, so the time complexity find is at worst O(log n)

# union simply calls find twixe, so since find is at worst log n, the time
# complexity of union is also O(log n)


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
