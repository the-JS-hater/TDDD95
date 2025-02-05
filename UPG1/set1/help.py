from itertools import pairwise


def main():
    f = [line.replace("\n", "").split(' ') for line in open(0, 'r').readlines()[1:]]
    [print(res) for res in [helper(f[i], f[i+1], {}, {}) for i in range(0, len(f) - 1, 2)]]


def helper(l1, l2, mem_l, mem_r):
    if not l1 and not l2:
        return ''
    if (not l1 and l2) or (l1 and not l2):
        return '-'
    left, right = l1[0], l2[0]
    l_rest, r_rest = l1[1:], l2[1:]
    
    rest = helper(l_rest, r_rest, mem_l, mem_r)
    if rest == '-':
        return rest

    if left[0] == '<' and right[0] == '<':
        if left in mem_l and right in mem_r:
            if mem_l[left] != mem_r[right]:
                return '-'
            else:
                return mem_l[left] + " " + rest
            
        if right in mem_r:
            return mem_r[right] + " " + rest
        if left in mem_l:
            return mem_l[left] + " " + rest

        mem_l[left] = 'a'
        return 'a' + " " + rest

    if left[0] == '<':
        if left in mem_l and mem_l[left] != right:
            return '-'
        mem_l[left] = right
        return right + " " + rest
    
    if right[0] == '<':
        if right in mem_r and mem_r[right] != left:
            return '-'
        mem_r[right] = left
        return left + " " + rest
    
    if left == right:
        return left + " " + rest
    else:
        return '-'
    

if __name__ == "__main__":
    main()

    

