# Morgan Nordberg

# Problem: finding the longest common prefix in a string

# Algorithm: using a suffix array we construct an additional array, r, which
# stores the rank of each suffix. then an additional lcp array, which we
# construct by iterating over the suffixes, in order, and compare each suffix
# with the next one in the suffix array and use the lcp value from the previous
# iteration to skip redundant comparisons. when moving from one suffix to the
# next, the previously computed lcp value can be reused because removing the
# first character reduces the previous match by at most one

# Finding the longest one then just means we need to take the maximum value of the lcp array. 

# Time complexity: O(n), +O(n log n) for constructing the suffix array, because
# we run n iterations in the outermost loop, and the inner loop runs at most n
# number of times because that's the max nr of times k can be increased and
# decreased.


def lcp(s, p):
    n = len(p)
    r = [0] * n
    for i in range(n): r[p[i]] = i
    k = 0
    lcp = [0] * (n-1)
    for i in range(n):
        if r[i] == n - 1: 
            k=0
            continue
        j = p[r[i] + 1]
        while i + k < n and j + k < n and s[i+k] == s[j+k]: 
            k+=1
        lcp[r[i]] = k
        if k: k-=1
    return lcp


# CODE BELOW IS COPIED FROM PREVIOUS LAB
# tldr; suffix array with O(n log n) construction

def sort_cyclic_shifts(s):
    n = len(s)
    ALPHABET = 256
    p = [0] * n
    c = [0] * n
    cnt = [0] * ALPHABET
    for ch in s: cnt[ord(ch)] += 1
    for i in range(1, ALPHABET): cnt[i] += cnt[i-1]
    for i, ch in enumerate(s):
        idx = ord(ch)
        cnt[idx] -= 1
        p[cnt[idx]] = i
    c[p[0]] = 0
    classes = 1
    for i in range(1, n):
        if s[p[i]] != s[p[i-1]]:
            classes += 1
        c[p[i]] = classes - 1
    pn = [0] * n
    cn = [0] * n
    h = 0
    while (1 << h) < n:
        for i in range(n): 
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0: pn[i] += n
        cnt = [0 for _ in range(classes)]
        for i in range(n): cnt[c[pn[i]]] += 1
        for i in range(1, classes): cnt[i] += cnt[i-1]
        for i in range(n-1, -1, -1): 
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        cn[p[0]] = 0
        classes = 1
        for i in range(1, n):
            curr = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i-1]], c[(p[i-1] + (1 << h)) % n])
            if curr != prev: classes += 1
            cn[p[i]] = classes - 1;
        c = cn[:]
        h += 1
    return p


class suffix_arr():
    def __init__(self, s):
        self.s = s
        self.sorted_suffs = sort_cyclic_shifts(s + chr(0))[1:]  

    def get_suffix(self, i):
        return self.sorted_suffs[i]


if __name__ == "__main__":
    input = open(0).readlines()[1]
    sa = suffix_arr(input)
    print(max(lcp(input, sa.sorted_suffs)))
