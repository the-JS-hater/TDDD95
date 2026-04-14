def sort_cyclic_shifts(s):
    n = len(s)
    ALPHABET = 256
    p = [0] * n
    c = [0] * n
    cnt = [0] * ALPHABET
    for ch in s: cnt[ord(ch)] += 1
    for i in range(1, ALPHABET): cnt[i] += cnt[i-1]
    for i, ch in enumerate(s):
        p[cnt[ord(ch)]-1] = i
        cnt[ord(ch)] -= 1
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
        self.sorted_suffs = sort_cyclic_shifts(s + '$')[1:]

    def get_suffix(self, i):
        return self.sorted_suffs[i]


if __name__ == "__main__":
    input = open(0).readlines()
    for i in range(0, len(input), 2):
        s, qs = input[i].strip(), map(int, input[i+1].split())
        s_arr = suffix_arr(s)
        for q in qs:
            print(f"input:\nstring: {s}\nqueires: {list(qs)}")
            print(f"s_arr.sorted_suffs = {s_arr.sorted_suffs}")
            out = [s_arr.get_suffix(q) for q in qs]
            print(*out)
