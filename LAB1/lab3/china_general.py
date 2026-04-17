
def mod_inv(a, m):
    _,x,_ = ext_euclidean(a,m)
    return x % m


def ext_euclidean(a,b):
    if not b:
        return a,1,0
    d, x, y = ext_euclidean(b, a % b)
    return d, y, x - y * (a // b)
