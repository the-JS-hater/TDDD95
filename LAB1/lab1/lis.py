# Morgan Nordberg (morno368)

# From a sequence of integers, finds an array of indices to that sequence that
# togheter form the longest possible strictly increasing sequence

# the list d contains the smallest value at d[i] that a increasing sequence of
# length i ends on. p is a list of "ancestor" indices, used to reconstruct the
# sequence of indices. p[i] points to the index of the element that came before
# it in the sequence. d_indices holds the indices in the original input that
# correspond to the value at d[i]

# the algorithm is then to intitally assume d[0] = -inf, and d[1 ... n] = inf,
# and iterating over the input and updatind d, with regards to the input. since
# d will always be sorted and there is only one spot a given value could end
# at, we can find the appropriate index using binary search

# so we iterate over the input once, O(n), and each time do a binary search
# O(log n). So the complexity of the LIS implementation is O(n log n)

def solve(input):
    # initialize arrays
    d = [float('inf') for i in range(len(input) + 1)]
    d[0] *= -1
    p = [-1 for i in range(len(input))]
    d_idxes = [-1 for i in range(len(d))] 
    
    # for each value, use bin_search to find the length l where it ends at
    for i,val in enumerate(input):
        l = bin_search(d, val)
        if d[l-1] < val and val < d[l]:
            # update all the arrays
            d[l] = val
            d_idxes[l] = i
            p[i] = d_idxes[l-1]
    
    # find the length of the longest sequence        
    l = 0
    for i, val in enumerate(d):
        if val < float('inf'):
            l = i
    
    # reconstruct indices
    idx = d_idxes[l]
    indices = []
    while idx != -1:
        indices += [idx]
        idx = p[idx]
    
    return indices[::-1]


def bin_search(l, val):
    left, right = 0, len(l)
    while left < right:
        mid = (left + right) // 2
        if l[mid] <= val: left = mid + 1
        else: right = mid
    return left


if __name__ == "__main__":
    inputs = [[int(i) for i in row] for row in list(map(str.split, open(0).readlines()))[1::2]]
    for input in inputs: 
        l = solve(input)
        print(len(l))
        print(*l)
