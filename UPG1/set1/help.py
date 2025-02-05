is_pattern = lambda w : w[0] == '<'
replace = lambda l, o, n : [n if x == o else x for x in l]

f = open(0).read().splitlines()[1:]
o = []
for i in range(0, len(f), 2):
    a, b = f[i].split(" "), f[i+1].split(" ")
    if len(a) != len(b):
        o.append("-")
        continue
    flag = True
    while flag:
        flag = False
        p = zip(a, b)
        for l, r in p:
            if is_pattern(l) and not is_pattern(r):
                a = replace(a, l, r)
                flag = True
                continue
            if is_pattern(r) and not is_pattern(l):
                b = replace(b, r, l)
                flag = True
                continue
    p = zip(a, b)
    for l, r in p:
        if is_pattern(l) and is_pattern(r):
            a = replace(a, l, 'a')                
            b = replace(b, r, 'a')
            flag = True
            continue
    if a != b:
        o.append("-")
    else: 
        o.append(a)


print("\n".join([" ".join(r) for r in o]))
