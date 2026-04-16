# Morgan Nordberg

# Problem: build a data structure that stores all suffixes of a string in
# sorted order

# Algorithm: we sort the cyclic shifts of a string because if we append a char
# that strictly smaller than all others in the string to it, the sorted cyclic
# shifts will match the sorted suffixes 

# We iterate over substring lengths 1, 2, 4, 8, ... and maintain an array of
# equivalence classes for each position. instead of doing string comaprison on
# substrings we reuse results from the previous iteration and compare the
# equivalence classes of the substring separate halves. So instead string
# comparison we get comparing pairs of integers. the values of these integers
# is also bounded by the number of characters in the alphabet. So we can sort
# them using radix sort

# Time complexity: each iteration takes O(n) time (radix sort), and we do O(log
# n) iterations as the substring length doubles each time. so time complexity
# is O(n log n).


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
        # chr(0) because '$' < ' ' so strings with spaces break ordering
        # otherwise. This alone has wasted hours of my precious time on earth
        self.sorted_suffs = sort_cyclic_shifts(s + chr(0))[1:]  

    def get_suffix(self, i):
        return self.sorted_suffs[i]


if __name__ == "__main__":
    input = open(0).readlines()
    for i in range(0, len(input), 2):
        s, qs = input[i].strip(), map(int, input[i+1].split())
        s_arr = suffix_arr(s)
        for q in qs:
            out = [s_arr.get_suffix(q) for q in qs]
            print(*out)
