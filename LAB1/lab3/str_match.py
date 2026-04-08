# Morgan Nordberg

# find the indices where substrings matching a given pattern begin in some
# larger text

# Algorithm: using a hash function we convert the pattern string into a numeric
# value, then for each sub string in the text with the same length as the
# pattern. Albeit we dont hash the substrings during the comparing, we
# precompute the hash for all prefixes of the text string and derive the hash
# of substring during comparison 

# Complexity: O(S + T) where S is the length of the pattern string and T is the
# length of the text string. The time complexity of the hash function is linear
# relative to the length of the string being hashed. Computing prefix hashes
# for the text takes O(T), computing the pattern hash takes O(S). The actual
# hash compariosons are constant time


def str_match(s, t):
    P = 53
    M = 2**32
    s_size = len(s)
    t_size = len(t)
    occs = []
    
    p_pow = [1] * max(s_size, t_size)
    for i in range(1, len(p_pow)): 
        p_pow[i] = (p_pow[i-1] * P) % M
    
    h = [0] * (t_size + 1)
    for i,c in enumerate(t): 
        h[i+1] = (h[i] + (ord(c) - ord('a') + 1) * p_pow[i]) % M
    h_s = 0
    for i, c in enumerate(s):
        h_s = (h_s + (ord(c) - ord('a') + 1) * p_pow[i]) % M
    
    for i in range(t_size - s_size + 1):
        cur_h = (h[i+s_size] + M - h[i]) % M
        if cur_h == h_s * p_pow[i] % M: occs += [i]
    
    return occs;


if __name__ == "__main__":
    input = open(0).readlines()
    for i in range(0, len(input), 2):
        s1, s2 = input[i].strip(), input[i+1].strip()
        print(*str_match(s1, s2))
