# Morgan Nordberg

# Problem: find a solution to 
#   x = a1 mod m1
#   x = a2 mod m2
# where m1 and m2 are relative prime

# Algorithm: take the modular inverses, using extended euclidean, of m1,m2 and
# m2,m1. using these modular inverses n1 and n2 the solution becomes a1n2m2 +
# a2n1m1 mod m1m2. 

# Extended euclidean simply modifices the standard GCD algorithm with keeping
# track of an additional set of coefficients that in the recursive base case
# are 0, 1 and then change every recursive call as x = old_y and y = old_x -
# old_y * (a // b)

# Time complexity: extended euclidean runs in O(log n), and we call it twice
# through the mov_inv() calls. rest of the code is just constant time
# arithmetic. So overall the time complexity is O(log n)


def solve(a1,m1,a2,m2):
    n1 = mod_inv(m1, m2)
    n2 = mod_inv(m2, m1)
    x = (a1*n2*m2 + a2*n1*m1) % (m1*m2) 
    return x, m1 * m2


def mod_inv(a, m):
    _,x,_ = ext_euclidean(a,m)
    return x % m


def ext_euclidean(a,b):
    if not b:
        return a,1,0
    d, x, y = ext_euclidean(b, a % b)
    return d, y, x - y * (a // b)

if __name__ == "__main__":
    input = open(0).readlines()
    for l in input[1:]:
        a,n,b,m = map(int, l.split())
        print(*solve(a,n,b,m))
